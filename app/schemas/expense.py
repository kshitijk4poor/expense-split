from typing import List, Optional

from pydantic import BaseModel, validator


class ExpenseParticipantCreate(BaseModel):
    user_id: int
    amount: Optional[float] = None
    percentage: Optional[float] = None


class ExpenseCreate(BaseModel):
    title: str
    total_amount: float
    split_method: str  # 'equal', 'exact', 'percentage'
    participants: List[ExpenseParticipantCreate]

    @validator("split_method")
    def validate_split_method(cls, v):
        if v not in {"equal", "exact", "percentage"}:
            raise ValueError("Invalid split method")
        return v

    @validator("participants")
    def validate_participants(cls, v, values):
        split_method = values.get("split_method")
        if split_method == "percentage":
            total_percentage = sum(p.percentage for p in v if p.percentage is not None)
            if total_percentage != 100:
                raise ValueError("Total percentage must add up to 100%")
        return v


class ExpenseRead(BaseModel):
    id: int
    title: str
    total_amount: float
    split_method: str
    owner_id: int
    participants: List[ExpenseParticipantCreate]

    class Config:
        orm_mode = True
