from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

from app.services.rate import get_conversion_rate


router = APIRouter()

@router.get("/{currency}")
def get_exchange_rate(currency: str):
    rate = get_conversion_rate(currency)
    print(rate)
    if not rate:
        raise HTTPException(status_code=404, detail="Exchange rate not found")
    return JSONResponse({
        "currency": f"{currency.upper()}/USDT",
        "rate": rate
    })
