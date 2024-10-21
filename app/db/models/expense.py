from app.db.base import Base
from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    total_amount = Column(Float, nullable=False)
    split_method = Column(String, nullable=False)  # 'equal', 'exact', 'percentage'
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="expenses")
    participants = relationship("ExpenseParticipant", back_populates="expense")


class ExpenseParticipant(Base):
    __tablename__ = "expense_participants"

    id = Column(Integer, primary_key=True, index=True)
    expense_id = Column(Integer, ForeignKey("expenses.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    amount = Column(Float, nullable=True)
    percentage = Column(Float, nullable=True)

    expense = relationship("Expense", back_populates="participants")
    user = relationship("User")
