import datetime

from pydantic import BaseModel

class Spent(BaseModel):
    amount: float
    reason: str
    priority: str

    class Config:
        orm_mode = True