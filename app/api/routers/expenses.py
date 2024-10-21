from typing import List

from app import schemas
from app.api.dependencies import get_current_user, get_user_service
from app.core.config import settings
from app.services.expense_service import ExpenseService
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(prefix="/expenses", tags=["expenses"])


@router.post(
    "/", response_model=schemas.expense.ExpenseRead, status_code=status.HTTP_201_CREATED
)
async def add_expense(
    expense: schemas.expense.ExpenseCreate,
    current_user: schemas.user.UserRead = Depends(get_current_user),
    db: AsyncSession = Depends(get_user_service),
):
    expense_service = ExpenseService(db)
    new_expense = await expense_service.create_expense(expense, current_user.id)
    return new_expense


@router.get("/user/{user_id}", response_model=List[schemas.expense.ExpenseRead])
async def get_user_expenses(
    user_id: int, expense_service: ExpenseService = Depends(ExpenseService)
):
    expenses = await expense_service.get_user_expenses(user_id)
    return expenses


@router.get("/", response_model=List[schemas.expense.ExpenseRead])
async def get_all_expenses(expense_service: ExpenseService = Depends(ExpenseService)):
    expenses = await expense_service.get_all_expenses()
    return expenses
