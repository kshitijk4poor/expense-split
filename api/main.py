from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from services.user.main import app as user_app
from services.expense.main import app as expense_app
from services.balance_sheet.main import app as balance_sheet_app

app = FastAPI(title="Daily Expenses Sharing Application")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/users", user_app)
app.mount("/expenses", expense_app)
app.mount("/balance-sheet", balance_sheet_app)

@app.get("/")
async def root():
    return {"message": "Welcome to the Daily Expenses Sharing Application"}