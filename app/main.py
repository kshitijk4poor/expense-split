from app.api.routers import balance_sheet, expenses, users
from app.core.config import settings
from app.db import base, session
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

base.Base.metadata.create_all(bind=session.engine)

app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)

# Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routers
app.include_router(users.router)
app.include_router(expenses.router)
app.include_router(balance_sheet.router)
