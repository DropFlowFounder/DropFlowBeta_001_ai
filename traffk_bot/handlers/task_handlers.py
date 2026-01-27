from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from urllib.parse import urlparse
import re
from models.database import async_session
from services.user_service import UserService
from services.task_service import TaskService


router = Router()


# Define states for task creation FSM
class CreateTaskStates(StatesGroup):
    waiting_for_title = State()
    waiting_for_url = State()
    waiting_for_description = State()
    waiting_for_reward = State()
    waiting_for_task_type = State()
    waiting_for_private_username = State()


@router.message(Command("create_task"))
@router.callback_query(lambda c: c.data == "create_task")
async def cmd_create_task(update, state: FSMContext):
    """Start task creation process"""
    # Determine if it's a message or callback query
    if hasattr(update, 'message'):
        message = update.message
        user_id = message.from_user.id
    else:  # It's a callback query
        message = update.message
        user_id = update.from_user.id
        await update.answer()  # Answer the callback query
    
    async with async_session() as db:
        # Check if user is an advertiser
        user = await UserService.get_user_by_tg_id(db, user_id)
        if not user or user.role != "advertiser":
            await message.answer("Только рекламодатели могут создавать задания.")
            return
    
    # Ask for task title
    await message.answer("Введите название задания:")
    await state.set_state(CreateTaskStates.waiting_for_title)


@router.message(CreateTaskStates.waiting_for_title)
async def process_title(message: Message, state: FSMContext):
    """Process task title"""
    title = message.text.strip()
    
    if len(title) < 3:
        await message.answer("Название должно содержать минимум 3 символа. Введите название заново:")
        return
    
    await state.update_data(title=title)
    await message.answer("Введите исходную ссылку (URL):")
    await state.set_state(CreateTaskStates.waiting_for_url)


@router.message(CreateTaskStates.waiting_for_url)
async def process_url(message: Message, state: FSMContext):
    """Process task URL"""
    url = message.text.strip()
    
    # Validate URL
    try:
        result = urlparse(url)
        if not all([result.scheme, result.netloc]):
            raise ValueError("Invalid URL")
    except ValueError:
        await message.answer("Некорректный URL. Пожалуйста, введите действительный URL:")
        return
    
    await state.update_data(original_url=url)
    await message.answer("Введите описание задания (гео, запреты, крео и т.д.):")
    await state.set_state(CreateTaskStates.waiting_for_description)


@router.message(CreateTaskStates.waiting_for_description)
async def process_description(message: Message, state: FSMContext):
    """Process task description"""
    description = message.text.strip()
    
    await state.update_data(description=description)
    await message.answer("Введите сумму вознаграждения (в числовом формате):")
    await state.set_state(CreateTaskStates.waiting_for_reward)


@router.message(CreateTaskStates.waiting_for_reward)
async def process_reward(message: Message, state: FSMContext):
    """Process reward amount"""
    try:
        reward = float(message.text.strip().replace(',', '.'))
        if reward <= 0:
            raise ValueError("Reward must be positive")
    except ValueError:
        await message.answer("Некорректная сумма. Пожалуйста, введите число:")
        return
    
    await state.update_data(reward=reward)
    
    # Create keyboard for task type selection
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="публичное", callback_data="task_type_public")],
        [InlineKeyboardButton(text="приватное", callback_data="task_type_private")]
    ])
    
    await message.answer("Выберите тип задания:", reply_markup=keyboard)
    await state.set_state(CreateTaskStates.waiting_for_task_type)


@router.callback_query(lambda c: c.data.startswith("task_type_"), CreateTaskStates.waiting_for_task_type)
async def process_task_type(callback_query: CallbackQuery, state: FSMContext):
    """Process task type selection"""
    await callback_query.answer()
    
    task_type = callback_query.data.split("_")[2]  # Extract 'public' or 'private'
    await state.update_data(task_type=task_type)
    
    user_data = await state.get_data()
    
    # Show preview of entered data
    preview_text = (
        f"Предварительный просмотр задания:\n\n"
        f"Название: {user_data['title']}\n"
        f"Ссылка: {user_data['original_url']}\n"
        f"Описание: {user_data['description']}\n"
        f"Вознаграждение: {user_data['reward']}\n"
        f"Тип: {'публичное' if task_type == 'public' else 'приватное'}\n\n"
        f"Подтвердите создание задания:"
    )
    
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="✅ Создать", callback_data="confirm_task_creation")],
        [InlineKeyboardButton(text="❌ Отмена", callback_data="cancel_task_creation")]
    ])
    
    await callback_query.message.edit_text(preview_text, reply_markup=keyboard)


@router.callback_query(lambda c: c.data == "confirm_task_creation")
async def confirm_task_creation(callback_query: CallbackQuery, state: FSMContext):
    """Confirm task creation"""
    await callback_query.answer()
    
    user_data = await state.get_data()
    user_id = callback_query.from_user.id
    
    async with async_session() as db:
        # Get user from DB
        user = await UserService.get_user_by_tg_id(db, user_id)
        
        if not user:
            await callback_query.message.answer("Ошибка: пользователь не найден.")
            await state.clear()
            return
        
        # Check if user has sufficient balance to cover the reward
        total_required = float(user_data['reward'])
        if float(user.balance) < total_required:
            await callback_query.message.answer(
                f"Недостаточно средств для создания задания. "
                f"Требуется: {total_required}, доступно: {float(user.balance)}"
            )
            await state.clear()
            return
        
        # Reserve funds
        success = await UserService.freeze_funds(db, user.id, total_required)
        if not success:
            await callback_query.message.answer("Ошибка при резервировании средств.")
            await state.clear()
            return
        
        # Create the task
        task = await TaskService.create_task(
            db,
            user.id,  # advertiser_id
            user_data['title'],
            user_data['original_url'],
            user_data['description'],
            user_data['reward'],
            user_data['task_type']
        )
        
        if task:
            await callback_query.message.answer(f"Задание '{task.title}' успешно создано! Сумма {task.reward} была заморожена на вашем балансе.")
        else:
            await callback_query.message.answer("Ошибка при создании задания.")
        
        await state.clear()


@router.callback_query(lambda c: c.data == "cancel_task_creation")
async def cancel_task_creation(callback_query: CallbackQuery, state: FSMContext):
    """Cancel task creation"""
    await callback_query.answer("Создание задания отменено.")
    await callback_query.message.answer("Создание задания отменено.")
    await state.clear()


def register_task_handlers(dp):
    """Register task handlers with dispatcher"""
    dp.include_router(router)