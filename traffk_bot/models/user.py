from sqlalchemy import Column, Integer, String, BigInteger, DECIMAL, CheckConstraint
from sqlalchemy.orm import relationship
from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    tg_user_id = Column(BigInteger, unique=True, nullable=False, index=True)  # ID пользователя в Telegram
    username = Column(String(32))  # @username
    first_name = Column(String(255))
    role = Column(String(10), nullable=False)  # 'advertiser', 'traffic', 'admin'
    balance = Column(DECIMAL(15, 2), default=0.00)
    frozen_balance = Column(DECIMAL(15, 2), default=0.00)  # Замороженные средства
    created_at = Column(String)  # Will store ISO format datetime string

    # Relationships
    created_tasks = relationship("Task", back_populates="advertiser")
    assignments = relationship("Assignment", back_populates="traffic")

    __table_args__ = (
        CheckConstraint(role.in_(['advertiser', 'traffic', 'admin']), name='check_role'),
    )