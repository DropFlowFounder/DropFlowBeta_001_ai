from datetime import datetime
from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.task import Task
from models.user import User
from models.assignment import Assignment


class TaskService:
    @staticmethod
    async def create_task(
        db: AsyncSession,
        advertiser_id: int,
        title: str,
        original_url: str,
        description: str,
        reward: float,
        task_type: str
    ) -> Optional[Task]:
        """Create a new task"""
        task = Task(
            advertiser_id=advertiser_id,
            title=title,
            original_url=original_url,
            description=description,
            reward=reward,
            type=task_type,
            status="active",
            created_at=datetime.utcnow().isoformat()
        )
        db.add(task)
        await db.commit()
        await db.refresh(task)
        return task
    
    @staticmethod
    async def get_task_by_id(db: AsyncSession, task_id: int) -> Optional[Task]:
        """Get task by ID"""
        result = await db.execute(select(Task).filter(Task.id == task_id))
        return result.scalar_one_or_none()
    
    @staticmethod
    async def get_public_tasks(db: AsyncSession) -> List[Task]:
        """Get all public active tasks"""
        result = await db.execute(
            select(Task).filter(
                Task.type == "public",
                Task.status == "active"
            )
        )
        return result.scalars().all()
    
    @staticmethod
    async def get_tasks_by_advertiser(db: AsyncSession, advertiser_id: int) -> List[Task]:
        """Get all tasks created by specific advertiser"""
        result = await db.execute(
            select(Task).filter(Task.advertiser_id == advertiser_id)
        )
        return result.scalars().all()
    
    @staticmethod
    async def get_assignments_for_task(db: AsyncSession, task_id: int) -> List[Assignment]:
        """Get all assignments for a specific task"""
        result = await db.execute(
            select(Assignment).filter(Assignment.task_id == task_id)
        )
        return result.scalars().all()
    
    @staticmethod
    async def update_task_status(db: AsyncSession, task_id: int, status: str) -> bool:
        """Update task status"""
        result = await db.execute(select(Task).filter(Task.id == task_id))
        task = result.scalar_one_or_none()
        
        if task:
            task.status = status
            await db.commit()
            return True
        
        return False