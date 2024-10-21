from typing import List

from app.db.models import Expense, ExpenseParticipant
from app.schemas.expense import ExpenseCreate
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select


class ExpenseService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_expense(self, expense: ExpenseCreate, owner_id: int) -> Expense:
        db_expense = Expense(
            title=expense.title,
            total_amount=expense.total_amount,
            split_method=expense.split_method,
            owner_id=owner_id,
        )
        self.db.add(db_expense)
        await self.db.commit()
        await self.db.refresh(db_expense)

        for participant in expense.participants:
            db_participant = ExpenseParticipant(
                expense_id=db_expense.id,
                user_id=participant.user_id,
                amount=participant.amount,
                percentage=participant.percentage,
            )
            self.db.add(db_participant)
        await self.db.commit()
        return db_expense

    async def get_user_expenses(self, user_id: int) -> List[Expense]:
        result = await self.db.execute(
            select(Expense).where(Expense.owner_id == user_id)
        )
        return result.scalars().all()

    async def get_all_expenses(self) -> List[Expense]:
        result = await self.db.execute(select(Expense))
        return result.scalars().all()
