from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from .user_service import UserService
from .assignment_service import AssignmentService


class EscrowService:
    @staticmethod
    async def process_payout(
        db: AsyncSession,
        assignment_id: int
    ) -> bool:
        """
        Process escrow payout: transfer funds from advertiser's frozen balance
        to traffic's available balance
        """
        # Get the assignment
        from models.assignment import Assignment
        from sqlalchemy.future import select
        
        result = await db.execute(
            select(Assignment).filter(Assignment.id == assignment_id)
        )
        assignment = result.scalar_one_or_none()
        
        if not assignment:
            return False
        
        # Get related task to find advertiser
        from models.task import Task
        task_result = await db.execute(
            select(Task).filter(Task.id == assignment.task_id)
        )
        task = task_result.scalar_one_or_none()
        
        if not task:
            return False
        
        # Perform the payout
        success = await UserService.payout_funds(
            db, 
            task.advertiser_id,  # From advertiser's frozen funds
            assignment.traffic_id,  # To traffic's balance
            float(task.reward)
        )
        
        if success:
            # Mark assignment as completed
            await AssignmentService.mark_assignment_as_completed(
                db, 
                assignment.id
            )
        
        return success
    
    @staticmethod
    async def reserve_funds(
        db: AsyncSession,
        user_id: int,
        amount: float
    ) -> bool:
        """Reserve funds for a task (move from available to frozen)"""
        return await UserService.freeze_funds(db, user_id, amount)
    
    @staticmethod
    async def admin_arbitrage(
        db: AsyncSession,
        assignment_id: int,
        decision: str  # 'advertiser' or 'traffic'
    ) -> bool:
        """
        Admin arbitrage function to resolve disputes
        decision: 'advertiser' - return funds to advertiser
                 'traffic' - pay funds to traffic
        """
        # Get the assignment
        from models.assignment import Assignment
        from sqlalchemy.future import select
        
        result = await db.execute(
            select(Assignment).filter(Assignment.id == assignment_id)
        )
        assignment = result.scalar_one_or_none()
        
        if not assignment:
            return False
        
        # Get related task to find advertiser and reward amount
        from models.task import Task
        task_result = await db.execute(
            select(Task).filter(Task.id == assignment.task_id)
        )
        task = task_result.scalar_one_or_none()
        
        if not task:
            return False
        
        amount = float(task.reward)
        
        if decision == 'advertiser':
            # Return funds to advertiser (release frozen funds back to available)
            await UserService.release_funds(db, task.advertiser_id, amount)
        elif decision == 'traffic':
            # Pay funds to traffic (same as normal payout)
            await UserService.payout_funds(
                db,
                task.advertiser_id,
                assignment.traffic_id,
                amount
            )
        else:
            return False  # Invalid decision
        
        # Mark assignment as completed regardless of decision
        await AssignmentService.mark_assignment_as_completed(
            db,
            assignment.id
        )
        
        return True