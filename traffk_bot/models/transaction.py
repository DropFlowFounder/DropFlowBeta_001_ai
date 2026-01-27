from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from .database import Base


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    type = Column(String(20), nullable=False)  # 'deposit', 'withdrawal', 'freeze', 'payout', 'release'
    amount = Column(DECIMAL(15, 2), nullable=False)
    status = Column(String(20), nullable=False)  # 'pending', 'completed', 'cancelled'
    created_at = Column(String)  # Will store ISO format datetime string

    # Relationships
    user = relationship("User")

    __table_args__ = (
        CheckConstraint(status.in_(['pending', 'completed', 'cancelled']), name='check_transaction_status'),
    )