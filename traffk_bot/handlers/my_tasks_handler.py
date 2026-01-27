from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from models.database import async_session
from services.user_service import UserService
from services.task_service import TaskService
from services.assignment_service import AssignmentService
from services.escrow_service import EscrowService


router = Router()


@router.message(Command("my_tasks"))
@router.callback_query(lambda c: c.data == "my_tasks")
async def cmd_my_tasks(update, state: FSMContext):
    """Show advertiser's tasks"""
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
        if not user or user.role != "advertiser":
            await message.answer("Только рекламодатели могут просматривать свои задачи.")
            return
        
        # Get user's tasks
        tasks = await TaskService.get_tasks_by_advertiser(db, user.id)
        
        if not tasks:
            await message.answer("У вас нет созданных задач.")
            return
        
        # Display each task
        for task in tasks:
            # Get assignments for this task
            assignments = await TaskService.get_assignments_for_task(db, task.id)
            
            task_text = (
                f"📝 <b>{task.title}</b>\n"
                f"💰 Вознаграждение: {float(task.reward)}\n"
                f"📊 Статус: {task.status}\n"
                f"👥 Взято в работу: {len(assignments)} раз\n"
            )
            
            # Create keyboard for each assignment
            if assignments:
                from models.user import User
                from sqlalchemy.future import select
                
                for assignment in assignments:
                    # Get traffic user info
                    traffic_result = await db.execute(
                        select(User).filter(User.id == assignment.traffic_id)
                    )
                    traffic = traffic_result.scalar_one_or_none()
                    
                    if traffic:
                        status_text = {
                            "in_progress": "🔄 В работе",
                            "pending_payment": "💸 Ожидает подтверждения",
                            "completed": "✅ Завершено"
                        }.get(assignment.status, assignment.status)
                        
                        assignment_info = f" - @{traffic.username or 'no_username'}: {status_text}"
                        
                        # Add button if pending payment
                        if assignment.status == "pending_payment":
                            keyboard = InlineKeyboardMarkup(inline_keyboard=[
                                [InlineKeyboardButton(
                                    text=f" Подтвердить выплату ({float(task.reward)}) ", 
                                    callback_data=f"confirm_payout_{assignment.id}"
                                )]
                            ])
                            
                            await message.answer(
                                f"{task_text}{assignment_info}", 
                                reply_markup=keyboard
                            )
                        else:
                            await message.answer(f"{task_text}{assignment_info}")
            else:
                await message.answer(task_text)


@router.callback_query(lambda c: c.data.startswith("confirm_payout_"))
async def confirm_payout(callback_query: CallbackQuery, state: FSMContext):
    """Confirm payout for an assignment"""
    await callback_query.answer()
    
    assignment_id = int(callback_query.data.split("_")[2])
    
    async with async_session() as db:
        # Process the payout through escrow service
        success = await EscrowService.process_payout(db, assignment_id)
        
        if success:
            await callback_query.message.answer("Выплата подтверждена. Средства перечислены трафику.")
        else:
            await callback_query.message.answer("Ошибка при подтверждении выплаты.")


def register_my_tasks_handler(dp):
    """Register my tasks handler with dispatcher"""
    dp.include_router(router)