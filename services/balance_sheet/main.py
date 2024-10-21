from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import crud, models, schemas
from shared.database import engine, get_db
from shared.auth import get_current_user
from services.user.schemas import User
from fastapi.responses import StreamingResponse
import io
import csv

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/balance-sheet/", response_model=schemas.BalanceSheet)
def read_balance_sheet(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return crud.update_balance_sheet(db, user_id=current_user.id)

@app.get("/balance-sheet/download/")
def download_balance_sheet(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    balance_sheet = crud.update_balance_sheet(db, user_id=current_user.id)
    
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(['User ID', 'Total Spent', 'Total Owed', 'Net Balance', 'Updated At'])
    writer.writerow([
        balance_sheet.user_id,
        balance_sheet.total_spent,
        balance_sheet.total_owed,
        balance_sheet.net_balance,
        balance_sheet.updated_at
    ])
    
    output.seek(0)
    return StreamingResponse(
        iter([output.getvalue()]),
        media_type="text/csv",
        headers={"Content-Disposition": f"attachment; filename=balance_sheet_{current_user.id}.csv"}
    )