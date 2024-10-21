import pytest
from app.db.base import Base
from app.db.session import SessionLocal, engine
from app.main import app
from fastapi.testclient import TestClient


@pytest.fixture(scope="module")
def test_client():
    Base.metadata.create_all(bind=engine)
    with TestClient(app) as client:
        yield client
    Base.metadata.drop_all(bind=engine)
