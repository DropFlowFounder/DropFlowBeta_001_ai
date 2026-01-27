from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from models.database import async_session
from services.user_service import UserService
from services.assignment_service import AssignmentService


router = Router()


@router.message(Command("my_assignments"))
@router.callback_query(lambda c: c.data == "my_assignments")
async def cmd_my_assignments(update, state: FSMContext):
    """Show user's assignments"""
    # Determine if it's a message or callback query
    if hasattr(update, 'message'):
        message = update.message
        user_id = message.from_user.id
    else:  # It's a callback query
        message = update.message
        user_id = update.from_user.id
        await update.answer()  # Answer the callback query
    
    async with async_session() as db:
        # Get user from DB
        user = await UserService.get_user_by_tg_id(db, user_id)
        if not user:
            await message.answer("Пользователь не найден. Пожалуйста, используйте /start для регистрации.")
            return
        
        # Get user's assignments
        assignments = await AssignmentService.get_assignments_by_traffic(db, user.id)
        
        if not assignments:
            await message.answer("У вас нет взятых заданий.")
            return
        
        # Group assignments by status
        from models.task import Task
        from sqlalchemy.future import select
        
        for assignment in assignments:
            # Get the related task
            task_result = await db.execute(
                select(Task).filter(Task.id == assignment.task_id)
            )
            task = task_result.scalar_one_or_none()
            
            if task:
                status_text = {
                    "in_progress": "🔄 В работе",
                    "pending_payment": "⏳ Ожидает оплаты",
                    "completed": "✅ Завершено"
                }.get(assignment.status, assignment.status)
                
                assignment_text = (
                    f"📋 <b>{task.title}</b>\n"
                    f"💰 Вознаграждение: {float(task.reward)}\n"
                    f"🔗 Ссылка: {assignment.unique_link}\n"
                    f"📊 Статус: {status_text}\n"
                )
                
                # Create appropriate keyboard based on status
                keyboard = None
                if assignment.status == "in_progress":
                    keyboard = InlineKeyboardMarkup(inline_keyboard=[
                        [InlineKeyboardButton(
                            text=" ✅ Отметить выполненным ", 
                            callback_data=f"mark_done_{assignment.id}"
                        )]
                    ])
                elif assignment.status == "pending_payment":
                    assignment_text += "\nОжидает подтверждения рекламодателем."
                elif assignment.status == "completed":
                    assignment_text += "\nЗадание завершено. Оплата получена."
                
                await message.answer(assignment_text, reply_markup=keyboard)


@router.callback_query(lambda c: c.data.startswith("mark_done_"))
async def mark_assignment_done(callback_query: CallbackQuery, state: FSMContext):
    """Mark assignment as done"""
    await callback_query.answer()
    
    assignment_id = int(callback_query.data.split("_")[2])
    
    async with async_session() as db:
        # Update assignment status to pending payment
        success = await AssignmentService.mark_assignment_as_pending_payment(db, assignment_id)
        
        if success:
            # Get the assignment to notify the advertiser
            from models.assignment import Assignment
            from sqlalchemy.future import select
            from models.task import Task
            
            assignment_result = await db.execute(
                select(Assignment).filter(Assignment.id == assignment_id)
            )
            assignment = assignment_result.scalar_one_or_none()
            
            if assignment:
                # Get the task to find the advertiser
                task_result = await db.execute(
                    select(Task).filter(Task.id == assignment.task_id)
                )
                task = task_result.scalar_one_or_none()
                
                if task:
                    # Get the advertiser user
                    advertiser = await UserService.get_user_by_id(db, task.advertiser_id)
                    
                    if advertiser:
                        # In a real implementation, you would notify the advertiser via bot
                        # For now, we'll just send a message to the traffic user
                        await callback_query.message.answer(
                            "Задание отмечено как выполненное. "
                            "Рекламодатель будет уведомлен для подтверждения оплаты."
                        )
                        
                        # In a real implementation, you would send a notification to the advertiser here
                        # await bot.send_message(advertiser.tg_user_id, f"...")
                        return
        
        await callback_query.message.answer("Ошибка при обновлении статуса задания.")


def register_my_assignments_handler(dp):
    """Register my assignments handler with dispatcher"""
    dp.include_router(router)