from sqlalchemy.orm import Session
from . import models, schemas
from shared.exceptions import ExpenseNotFoundException, InvalidSplitException

def create_expense(db: Session, expense: schemas.ExpenseCreate, user_id: int):
    db_expense = models.Expense(
        description=expense.description,
        amount=expense.amount,
        split_type=expense.split_type,
        created_by=user_id
    )
    db.add(db_expense)
    db.flush()

    for split in expense.splits:
        db_split = models.ExpenseSplit(
            expense_id=db_expense.id,
            user_id=split.user_id,
            amount=split.amount,
            percentage=split.percentage
        )
        db.add(db_split)

    db.commit()
    db.refresh(db_expense)
    return db_expense

def get_expense(db: Session, expense_id: int):
    expense = db.query(models.Expense).filter(models.Expense.id == expense_id).first()
    if expense is None:
        raise ExpenseNotFoundException()
    return expense

def get_user_expenses(db: Session, user_id: int):
    return db.query(models.Expense).filter(models.Expense.created_by == user_id).all()

def get_all_expenses(db: Session):
    return db.query(models.Expense).all()