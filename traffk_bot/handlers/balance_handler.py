from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from models.database import async_session
from services.user_service import UserService
from services.user_service import UserService


router = Router()


@router.message(Command("balance"))
@router.callback_query(lambda c: c.data == "balance")
async def cmd_balance(update, state: FSMContext):
    """Handle /balance command and callback"""
    # Determine if it's a message or callback query
    if hasattr(update, 'message'):
        message = update.message
        user_id = message.from_user.id
    else:  # It's a callback query
        message = update.message
        user_id = update.from_user.id
        await update.answer()  # Answer the callback query
    
    async with async_session() as db:
        # Find the user in the database
        user = await UserService.get_user_by_tg_id(db, user_id)
        if not user:
            await message.answer("Пользователь не найден. Пожалуйста, используйте /start для регистрации.")
            return
        
        # Get balance information
        balance_info = await UserService.get_balance(db, user.id)
        
        # Format and send balance information
        balance_text = (
            f"💰 Ваш баланс:\n\n"
            f"Доступно: {balance_info['available']:.2f}\n"
            f"Заморожено: {balance_info['frozen']:.2f}\n"
            f"Всего: {balance_info['total']:.2f}"
        )
        
        await message.answer(balance_text)


def register_balance_handler(dp):
    """Register balance handler with dispatcher"""
    dp.include_router(router)