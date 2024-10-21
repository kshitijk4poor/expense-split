from app.db.models import Expense, ExpenseParticipant
from app.schemas.balance_sheet import BalanceDetail
from sqlalchemy import func
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select


class BalanceSheetService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def generate_balance_sheet(self, user_id: int) -> BalanceDetail:
        # Total spent by the user
        total_spent_result = await self.db.execute(
            select(func.sum(Expense.total_amount)).where(Expense.owner_id == user_id)
        )
        total_spent = total_spent_result.scalar() or 0

        # Total owed by the user
        total_owed_result = await self.db.execute(
            select(func.sum(ExpenseParticipant.amount)).where(
                ExpenseParticipant.user_id == user_id
            )
        )
        total_owed = total_owed_result.scalar() or 0

        # Net balance
        net_balance = total_spent - total_owed

        return BalanceDetail(
            user_id=user_id,
            total_spent=total_spent,
            total_owed=total_owed,
            net_balance=net_balance,
        )
