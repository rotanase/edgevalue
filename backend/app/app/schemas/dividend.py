from typing import List

from datetime import date

from pydantic import BaseModel, HttpUrl

from app.utils import CurrencyEnum

# Shared properties
class DividendBase(BaseModel):
    currency: CurrencyEnum = None
    ex_dividend_date: date = None
    pay_date: date = None
    dividend_payout: float = None

    company_id: int = None


# Properties to receive on dividend creation
class DividendCreate(DividendBase):
    pass


# Properties to receive on dividend update
class DividendUpdate(DividendBase):
    pass


# Properties shared by models stored in DB
class DividendInDBBase(DividendBase):
    id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Dividend(DividendInDBBase):
    pass


# Properties properties stored in DB
class DividendInDB(DividendInDBBase):
    pass
