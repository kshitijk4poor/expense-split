from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import crud, models, schemas
from shared.database import engine, get_db
from shared.auth import get_current_user
from services.user.schemas import User
from typing import List

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/expenses/", response_model=schemas.Expense)
def create_expense(expense: schemas.ExpenseCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return crud.create_expense(db=db, expense=expense, user_id=current_user.id)

@app.get("/expenses/{expense_id}", response_model=schemas.Expense)
def read_expense(expense_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return crud.get_expense(db, expense_id=expense_id)

@app.get("/expenses/user/", response_model=List[schemas.Expense])
def read_user_expenses(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return crud.get_user_expenses(db, user_id=current_user.id)

@app.get("/expenses/", response_model=List[schemas.Expense])
def read_all_expenses(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return crud.get_all_expenses(db)