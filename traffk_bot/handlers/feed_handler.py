from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from models.database import async_session
from services.user_service import UserService
from services.task_service import TaskService


router = Router()


@router.message(Command("feed"))
@router.callback_query(lambda c: c.data == "feed")
async def cmd_feed(update, state: FSMContext):
    """Show public task feed"""
    # Determine if it's a message or callback query
    if hasattr(update, 'message'):
        message = update.message
    else:  # It's a callback query
        message = update.message
        await update.answer()  # Answer the callback query
    
    async with async_session() as db:
        # Get all public active tasks
        tasks = await TaskService.get_public_tasks(db)
        
        if not tasks:
            await message.answer("В настоящее время нет доступных публичных заданий.")
            return
        
        # Display tasks
        for task in tasks[:10]:  # Show max 10 tasks
            task_text = (
                f"📝 <b>{task.title}</b>\n"
                f"💰 Вознаграждение: {float(task.reward)}\n"
                f"📋 Описание: {task.description[:100]}{'...' if len(task.description) > 100 else ''}\n"
            )
            
            # Create keyboard with "Take task" button
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(
                    text=" взять в работу ", 
                    callback_data=f"take_task_{task.id}"
                )]
            ])
            
            await message.answer(task_text, reply_markup=keyboard)


@router.callback_query(lambda c: c.data.startswith("take_task_"))
async def take_task_callback(callback_query: CallbackQuery, state: FSMContext):
    """Handle taking a task"""
    await callback_query.answer()
    
    task_id = int(callback_query.data.split("_")[2])
    traffic_id = callback_query.from_user.id
    
    async with async_session() as db:
        # Get the task
        task = await TaskService.get_task_by_id(db, task_id)
        if not task:
            await callback_query.message.answer("Задание не найдено.")
            return
        
        # Get the traffic user
        traffic = await UserService.get_user_by_tg_id(db, traffic_id)
        if not traffic or traffic.role != "traffic":
            await callback_query.message.answer("Только трафик может брать задания в работу.")
            return
        
        # Check if the user already took this task
        from services.assignment_service import AssignmentService
        existing_assignment = await AssignmentService.get_assignment_by_ids(db, task_id, traffic.id)
        if existing_assignment:
            await callback_query.message.answer("Вы уже взяли это задание в работу.")
            return
        
        # Generate unique link (for MVP, we'll just use a simple redirect with assignment ID)
        # In a real implementation, you might want to use a URL shortener service
        unique_link = f"https://traffk.example.com/r?r={traffic_id}_{task_id}"
        
        # Create assignment
        from services.assignment_service import AssignmentService
        assignment = await AssignmentService.create_assignment(
            db,
            task.id,
            traffic.id,
            unique_link
        )
        
        if assignment:
            await callback_query.message.answer(
                f"Вы взяли задание '{task.title}' в работу!\n\n"
                f"Ваша уникальная ссылка: {unique_link}\n\n"
                f"После выполнения задания не забудьте отметить его как выполненное."
            )
        else:
            await callback_query.message.answer("Ошибка при взятии задания в работу.")


def register_feed_handler(dp):
    """Register feed handler with dispatcher"""
    dp.include_router(router)