from datetime import datetime
from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.user import User
from models.transaction import Transaction


class UserService:
    @staticmethod
    async def get_or_create_user(
        db: AsyncSession, 
        tg_user_id: int, 
        username: Optional[str], 
        first_name: str
    ) -> User:
        """Get existing user or create new one"""
        result = await db.execute(select(User).filter(User.tg_user_id == tg_user_id))
        user = result.scalar_one_or_none()
        
        if not user:
            user = User(
                tg_user_id=tg_user_id,
                username=username,
                first_name=first_name,
                role="traffic",  # Default role, can be changed later
                balance=0.00,
                frozen_balance=0.00,
                created_at=datetime.utcnow().isoformat()
            )
            db.add(user)
            await db.commit()
            await db.refresh(user)
        
        return user
    
    @staticmethod
    async def update_user_role(db: AsyncSession, tg_user_id: int, role: str) -> bool:
        """Update user role"""
        result = await db.execute(select(User).filter(User.tg_user_id == tg_user_id))
        user = result.scalar_one_or_none()
        
        if user:
            user.role = role
            await db.commit()
            return True
        
        return False
    
    @staticmethod
    async def get_user_by_id(db: AsyncSession, user_id: int) -> Optional[User]:
        """Get user by internal ID"""
        result = await db.execute(select(User).filter(User.id == user_id))
        return result.scalar_one_or_none()
    
    @staticmethod
    async def get_user_by_tg_id(db: AsyncSession, tg_user_id: int) -> Optional[User]:
        """Get user by Telegram ID"""
        result = await db.execute(select(User).filter(User.tg_user_id == tg_user_id))
        return result.scalar_one_or_none()
    
    @staticmethod
    async def get_balance(db: AsyncSession, user_id: int) -> dict:
        """Get user balance information"""
        result = await db.execute(select(User).filter(User.id == user_id))
        user = result.scalar_one_or_none()
        
        if user:
            return {
                "available": float(user.balance),
                "frozen": float(user.frozen_balance),
                "total": float(user.balance) + float(user.frozen_balance)
            }
        
        return {"available": 0.0, "frozen": 0.0, "total": 0.0}
    
    @staticmethod
    async def deposit_funds(db: AsyncSession, user_id: int, amount: float) -> bool:
        """Add funds to user account"""
        result = await db.execute(select(User).filter(User.id == user_id))
        user = result.scalar_one_or_none()
        
        if user:
            user.balance = user.balance + amount
            await db.commit()
            
            # Create transaction record
            transaction = Transaction(
                user_id=user.id,
                type="deposit",
                amount=amount,
                status="completed",
                created_at=datetime.utcnow().isoformat()
            )
            db.add(transaction)
            await db.commit()
            
            return True
        
        return False
    
    @staticmethod
    async def withdraw_funds(db: AsyncSession, user_id: int, amount: float) -> bool:
        """Withdraw funds from user account"""
        result = await db.execute(select(User).filter(User.id == user_id))
        user = result.scalar_one_or_none()
        
        if user and float(user.balance) >= amount:
            user.balance = user.balance - amount
            await db.commit()
            
            # Create transaction record
            transaction = Transaction(
                user_id=user.id,
                type="withdrawal",
                amount=amount,
                status="completed",
                created_at=datetime.utcnow().isoformat()
            )
            db.add(transaction)
            await db.commit()
            
            return True
        
        return False
    
    @staticmethod
    async def freeze_funds(db: AsyncSession, user_id: int, amount: float) -> bool:
        """Freeze funds on user account"""
        result = await db.execute(select(User).filter(User.id == user_id))
        user = result.scalar_one_or_none()
        
        if user and float(user.balance) >= amount:
            user.balance = user.balance - amount
            user.frozen_balance = user.frozen_balance + amount
            await db.commit()
            
            # Create transaction record
            transaction = Transaction(
                user_id=user.id,
                type="freeze",
                amount=amount,
                status="completed",
                created_at=datetime.utcnow().isoformat()
            )
            db.add(transaction)
            await db.commit()
            
            return True
        
        return False
    
    @staticmethod
    async def release_funds(db: AsyncSession, user_id: int, amount: float) -> bool:
        """Release frozen funds to available balance"""
        result = await db.execute(select(User).filter(User.id == user_id))
        user = result.scalar_one_or_none()
        
        if user and float(user.frozen_balance) >= amount:
            user.balance = user.balance + amount
            user.frozen_balance = user.frozen_balance - amount
            await db.commit()
            
            # Create transaction record
            transaction = Transaction(
                user_id=user.id,
                type="release",
                amount=amount,
                status="completed",
                created_at=datetime.utcnow().isoformat()
            )
            db.add(transaction)
            await db.commit()
            
            return True
        
        return False
    
    @staticmethod
    async def payout_funds(db: AsyncSession, from_user_id: int, to_user_id: int, amount: float) -> bool:
        """Transfer funds from one user to another (for escrow payments)"""
        # Get both users
        from_result = await db.execute(select(User).filter(User.id == from_user_id))
        from_user = from_result.scalar_one_or_none()
        
        to_result = await db.execute(select(User).filter(User.id == to_user_id))
        to_user = to_result.scalar_one_or_none()
        
        if from_user and to_user and float(from_user.frozen_balance) >= amount:
            # Deduct from frozen balance of sender
            from_user.frozen_balance = from_user.frozen_balance - amount
            
            # Add to balance of receiver
            to_user.balance = to_user.balance + amount
            
            await db.commit()
            
            # Create transaction records for both users
            from_transaction = Transaction(
                user_id=from_user.id,
                type="payout",
                amount=-amount,
                status="completed",
                created_at=datetime.utcnow().isoformat()
            )
            to_transaction = Transaction(
                user_id=to_user.id,
                type="payout",
                amount=amount,
                status="completed",
                created_at=datetime.utcnow().isoformat()
            )
            
            db.add(from_transaction)
            db.add(to_transaction)
            await db.commit()
            
            return True
        
        return False