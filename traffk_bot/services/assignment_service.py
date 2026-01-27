from datetime import datetime
from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.assignment import Assignment
from models.user import User


class AssignmentService:
    @staticmethod
    async def create_assignment(
        db: AsyncSession,
        task_id: int,
        traffic_id: int,
        unique_link: str
    ) -> Optional[Assignment]:
        """Create a new assignment"""
        assignment = Assignment(
            task_id=task_id,
            traffic_id=traffic_id,
            status="in_progress",
            unique_link=unique_link,
            created_at=datetime.utcnow().isoformat()
        )
        db.add(assignment)
        await db.commit()
        await db.refresh(assignment)
        return assignment
    
    @staticmethod
    async def get_assignment_by_ids(
        db: AsyncSession,
        task_id: int,
        traffic_id: int
    ) -> Optional[Assignment]:
        """Get assignment by task and traffic IDs"""
        result = await db.execute(
            select(Assignment).filter(
                Assignment.task_id == task_id,
                Assignment.traffic_id == traffic_id
            )
        )
        return result.scalar_one_or_none()
    
    @staticmethod
    async def get_assignments_by_traffic(db: AsyncSession, traffic_id: int) -> List[Assignment]:
        """Get all assignments for specific traffic user"""
        result = await db.execute(
            select(Assignment).filter(Assignment.traffic_id == traffic_id)
        )
        return result.scalars().all()
    
    @staticmethod
    async def get_assignments_by_task(db: AsyncSession, task_id: int) -> List[Assignment]:
        """Get all assignments for specific task"""
        result = await db.execute(
            select(Assignment).filter(Assignment.task_id == task_id)
        )
        return result.scalars().all()
    
    @staticmethod
    async def update_assignment_status(
        db: AsyncSession,
        assignment_id: int,
        status: str
    ) -> bool:
        """Update assignment status"""
        result = await db.execute(
            select(Assignment).filter(Assignment.id == assignment_id)
        )
        assignment = result.scalar_one_or_none()
        
        if assignment:
            assignment.status = status
            await db.commit()
            return True
        
        return False
    
    @staticmethod
    async def mark_assignment_as_pending_payment(
        db: AsyncSession,
        assignment_id: int
    ) -> bool:
        """Mark assignment as pending payment"""
        return await AssignmentService.update_assignment_status(
            db, 
            assignment_id, 
            "pending_payment"
        )
    
    @staticmethod
    async def mark_assignment_as_completed(
        db: AsyncSession,
        assignment_id: int
    ) -> bool:
        """Mark assignment as completed"""
        return await AssignmentService.update_assignment_status(
            db, 
            assignment_id, 
            "completed"
        )
    
    @staticmethod
    async def set_proof_text(
        db: AsyncSession,
        assignment_id: int,
        proof_text: str
    ) -> bool:
        """Set proof text for assignment"""
        result = await db.execute(
            select(Assignment).filter(Assignment.id == assignment_id)
        )
        assignment = result.scalar_one_or_none()
        
        if assignment:
            assignment.proof_text = proof_text
            await db.commit()
            return True
        
        return False