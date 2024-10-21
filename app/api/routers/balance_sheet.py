from app import schemas
from app.api.dependencies import get_current_user
from app.services.balance_sheet_service import BalanceSheetService
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(prefix="/balance-sheet", tags=["balance_sheet"])


@router.get("/", response_model=schemas.balance_sheet.BalanceSheet)
async def download_balance_sheet(
    current_user: schemas.user.UserRead = Depends(get_current_user),
    db: AsyncSession = Depends(get_current_user),
):
    balance_service = BalanceSheetService(db)
    balance = await balance_service.generate_balance_sheet(current_user.id)
    return schemas.balance_sheet.BalanceSheet(balances=[balance])
