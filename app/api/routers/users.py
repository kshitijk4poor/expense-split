from datetime import timedelta
from typing import List

from app import schemas
from app.api.dependencies import get_current_user, get_user_service
from app.core.security import create_access_token, verify_password
from app.services.user_service import UserService
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(prefix="/users", tags=["users"])


@router.post(
    "/register",
    response_model=schemas.user.UserRead,
    status_code=status.HTTP_201_CREATED,
)
async def register_user(
    user: schemas.user.UserCreate, user_service: UserService = Depends(get_user_service)
):
    existing_user = await user_service.get_user_by_email(user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    new_user = await user_service.create_user(user)
    return new_user


@router.post("/login", response_model=dict)
async def login(
    user: schemas.user.UserLogin, user_service: UserService = Depends(get_user_service)
):
    db_user = await user_service.get_user_by_email(user.email)
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token = create_access_token(data={"user_id": db_user.id})
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/{user_id}", response_model=schemas.user.UserRead)
async def get_user(user_id: int, user_service: UserService = Depends(get_user_service)):
    user = await user_service.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.get("/", response_model=List[schemas.user.UserRead])
async def list_users(
    skip: int = 0,
    limit: int = 100,
    user_service: UserService = Depends(get_user_service),
):
    users = await user_service.get_users(skip=skip, limit=limit)
    return users
