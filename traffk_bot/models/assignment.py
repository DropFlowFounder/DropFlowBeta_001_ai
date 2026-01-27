from sqlalchemy import Column, Integer, String, Text, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from .database import Base


class Assignment(Base):
    __tablename__ = "assignments"

    id = Column(Integer, primary_key=True, index=True)
    task_id = Column(Integer, ForeignKey("tasks.id"), nullable=False)
    traffic_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    status = Column(String(20), default='in_progress')  # 'in_progress', 'pending_payment', 'completed'
    unique_link = Column(Text)  # Сгенерированная уникальная ссылка
    proof_text = Column(Text)  # Текст-подтверждение от трафика
    created_at = Column(String)  # Will store ISO format datetime string

    # Relationships
    task = relationship("Task", back_populates="assignments")
    traffic = relationship("User", back_populates="assignments")

    __table_args__ = (
        CheckConstraint(status.in_(['in_progress', 'pending_payment', 'completed']), name='check_assignment_status'),
    )