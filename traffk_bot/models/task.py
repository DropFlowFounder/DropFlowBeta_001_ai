from sqlalchemy import Column, Integer, String, Text, DECIMAL, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from .database import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    advertiser_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    title = Column(String(255), nullable=False)
    original_url = Column(Text, nullable=False)  # Исходная ссылка рекламодателя
    description = Column(Text)
    reward = Column(DECIMAL(15, 2), nullable=False)  # Вознаграждение
    type = Column(String(10), nullable=False)  # 'public', 'private'
    status = Column(String(20), default='active')  # 'active', 'paused', 'completed'
    created_at = Column(String)  # Will store ISO format datetime string

    # Relationships
    advertiser = relationship("User", back_populates="created_tasks")
    assignments = relationship("Assignment", back_populates="task")

    __table_args__ = (
        CheckConstraint(type.in_(['public', 'private']), name='check_task_type'),
        CheckConstraint(status.in_(['active', 'paused', 'completed']), name='check_task_status'),
    )