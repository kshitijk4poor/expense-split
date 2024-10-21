from typing import List

from pydantic import BaseModel


class BalanceDetail(BaseModel):
    user_id: int
    total_spent: float
    total_owed: float
    net_balance: float


class BalanceSheet(BaseModel):
    balances: List[BalanceDetail]
