from pydantic import BaseModel
from datetime import datetime

class RateOut(BaseModel):
    base_currency: str
    target_currency: str
    rate: float
    timestamp: datetime

    class Config:
        orm_mode = True
