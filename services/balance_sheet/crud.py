from sqlalchemy.orm import Session
from . import models, schemas
from services.expense.models import Expense, ExpenseSplit

def get_balance_sheet(db: Session, user_id: int):
    balance_sheet = db.query(models.BalanceSheet).filter(models.BalanceSheet.user_id == user_id).first()
    if not balance_sheet:
        balance_sheet = models.BalanceSheet(user_id=user_id)
        db.add(balance_sheet)
        db.commit()
        db.refresh(balance_sheet)
    return balance_sheet

def update_balance_sheet(db: Session, user_id: int):
    expenses = db.query(Expense).filter(Expense.created_by == user_id).all()
    splits = db.query(ExpenseSplit).filter(ExpenseSplit.user_id == user_id).all()

    total_spent = sum(expense.amount for expense in expenses)
    total_owed = sum(split.amount for split in splits)
    net_balance = total_spent - total_owed

    balance_sheet = get_balance_sheet(db, user_id)
    balance_sheet.total_spent = total_spent
    balance_sheet.total_owed = total_owed
    balance_sheet.net_balance = net_balance

    db.commit()
    db.refresh(balance_sheet)
    return balance_sheet