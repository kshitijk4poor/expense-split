from pydantic import BaseModel, EmailStr, Field


class UserCreate(BaseModel):
    email: EmailStr
    name: str = Field(..., min_length=1)
    mobile_number: str = Field(..., min_length=10)
    password: str = Field(..., min_length=6)


class UserRead(BaseModel):
    id: int
    email: EmailStr
    name: str
    mobile_number: str

    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str
