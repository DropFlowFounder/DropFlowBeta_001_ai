from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from models.database import async_session
from services.user_service import UserService
from services.transaction_service import TransactionService


router = Router()


@router.message(Command("history"))
@router.callback_query(lambda c: c.data == "history")
async def cmd_history(update, state: FSMContext):
    """Handle /history command and callback"""
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
        
        # Get transaction history
        transactions = await TransactionService.get_user_transactions(db, user.id)
        
        if not transactions:
            await message.answer("У вас пока нет транзакций.")
            return
        
        # Format transaction history
        history_text = "💳 История транзакций:\n\n"
        for transaction in reversed(transactions[-10:]):  # Show last 10 transactions
            sign = "+" if transaction.amount >= 0 else ""
            history_text += (
                f"{sign}{float(transaction.amount):.2f} "
                f"({transaction.type}) - {transaction.status} "
                f"({transaction.created_at})\n"
            )
        
        await message.answer(history_text)


def register_history_handler(dp):
    """Register history handler with dispatcher"""
    dp.include_router(router)