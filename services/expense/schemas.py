from pydantic import BaseModel, validator
from typing import List, Optional
from datetime import datetime
from .models import SplitType

class ExpenseSplitBase(BaseModel):
    user_id: int
    amount: Optional[float] = None
    percentage: Optional[float] = None

class ExpenseSplitCreate(ExpenseSplitBase):
    pass

class ExpenseSplit(ExpenseSplitBase):
    id: int
    expense_id: int

    class Config:
        orm_mode = True

class ExpenseBase(BaseModel):
    description: str
    amount: float
    split_type: SplitType

class ExpenseCreate(ExpenseBase):
    splits: List[ExpenseSplitCreate]

    @validator('splits')
    def validate_splits(cls, v, values):
        split_type = values.get('split_type')
        total_amount = values.get('amount')

        if split_type == SplitType.EXACT:
            if sum(split.amount for split in v) != total_amount:
                raise ValueError("Sum of split amounts must equal total expense amount")
        elif split_type == SplitType.PERCENTAGE:
            if sum(split.percentage for split in v) != 100:
                raise ValueError("Sum of split percentages must equal 100%")
        return v

class Expense(ExpenseBase):
    id: int
    created_by: int
    created_at: datetime
    splits: List[ExpenseSplit]

    class Config:
        orm_mode = True