from datetime import datetime
from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.transaction import Transaction


class TransactionService:
    @staticmethod
    async def get_user_transactions(db: AsyncSession, user_id: int) -> List[Transaction]:
        """Get all transactions for a user"""
        result = await db.execute(
            select(Transaction).filter(Transaction.user_id == user_id)
        )
        return result.scalars().all()
    
    @staticmethod
    async def create_transaction(
        db: AsyncSession,
        user_id: int,
        transaction_type: str,
        amount: float,
        status: str = "completed"
    ) -> Optional[Transaction]:
        """Create a new transaction"""
        transaction = Transaction(
            user_id=user_id,
            type=transaction_type,
            amount=amount,
            status=status,
            created_at=datetime.utcnow().isoformat()
        )
        db.add(transaction)
        await db.commit()
        await db.refresh(transaction)
        return transaction
    
    @staticmethod
    async def get_transaction_by_id(db: AsyncSession, transaction_id: int) -> Optional[Transaction]:
        """Get transaction by ID"""
        result = await db.execute(
            select(Transaction).filter(Transaction.id == transaction_id)
        )
        return result.scalar_one_or_none()