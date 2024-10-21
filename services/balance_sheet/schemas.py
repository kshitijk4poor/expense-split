from pydantic import BaseModel
from datetime import datetime

class BalanceSheetBase(BaseModel):
    total_spent: float
    total_owed: float
    net_balance: float

class BalanceSheet(BalanceSheetBase):
    id: int
    user_id: int
    updated_at: datetime

    class Config:
        orm_mode = True