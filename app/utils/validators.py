from pydantic import BaseModel, validator


class PercentageSplit(BaseModel):
    participants: list

    @validator("participants")
    def check_percentage_sum(cls, v):
        total = sum(participant.get("percentage", 0) for participant in v)
        if total != 100:
            raise ValueError("Total percentage must equal 100")
        return v
