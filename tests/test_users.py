import pytest
from app.db.base import Base
from app.db.session import get_db
from app.main import app
from httpx import AsyncClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


# Dependency override
async def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


@pytest.mark.asyncio
async def test_register_user():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post(
            "/users/register",
            json={
                "email": "test@example.com",
                "name": "Test User",
                "mobile_number": "1234567890",
                "password": "securepassword",
            },
        )
    assert response.status_code == 201
    assert response.json()["email"] == "test@example.com"


@pytest.mark.asyncio
async def test_login_user():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # First, register the user
        await ac.post(
            "/users/register",
            json={
                "email": "login@example.com",
                "name": "Login User",
                "mobile_number": "0987654321",
                "password": "securepassword",
            },
        )
        # Then, attempt to login
        response = await ac.post(
            "/users/login",
            json={"email": "login@example.com", "password": "securepassword"},
        )
    assert response.status_code == 200
    assert "access_token" in response.json()
