from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from models.database import async_session
from services.user_service import UserService


router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    """Handle /start command and register user"""
    async with async_session() as db:
        # Get user data from Telegram
        tg_user_id = message.from_user.id
        username = message.from_user.username
        first_name = message.from_user.first_name
        
        # Register or get existing user
        user = await UserService.get_or_create_user(db, tg_user_id, username, first_name)
        
        # Create main menu keyboard
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="💰 Баланс", callback_data="balance")],
            [InlineKeyboardButton(text="📋 Мои задания", callback_data="my_assignments")],
            [InlineKeyboardButton(text="📊 Лента заданий", callback_data="feed")],
            [InlineKeyboardButton(text="📝 Создать задание", callback_data="create_task")],
            [InlineKeyboardButton(text="📋 Мои задачи", callback_data="my_tasks")]
        ])
        
        # Send welcome message
        await message.answer(
            f"Привет, {first_name}!\n"
            f"Вы зарегистрированы как {user.role}.\n\n"
            f"Добро пожаловать в Traffk - платформу для безопасных сделок между рекламодателями и арбитражниками.",
            reply_markup=keyboard
        )


def register_start_handler(dp):
    """Register start handler with dispatcher"""
    dp.include_router(router)