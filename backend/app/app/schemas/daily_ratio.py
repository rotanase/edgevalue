from typing import List

from datetime import date

from pydantic import BaseModel, HttpUrl

from app.utils import PeriodEnum
from app.utils import CurrencyEnum

# Shared properties
class DailyRatioBase(BaseModel):
    period: PeriodEnum = None
    end_date: date = None
    currency: CurrencyEnum = None
    market_cap: int = None
    price_to_earnings_ratio_ttm: float = None
    price_to_book_ratio: float = None
    market_to_book_ratio: float = None
    price_to_tangible_book_value: float = None
    enterprise_value: int = None
    ev_to_revenue: float = None
    ev_to_net_income: float = None
    ev_to_ebit: float = None
    ev_to_ebitda: float = None
    ev_to_assets: float = None

    company_id: int = None


# Properties to receive on daily ratio creation
class DailyRatioCreate(DailyRatioBase):
    pass


# Properties to receive on daily ratio update
class DailyRatioUpdate(DailyRatioBase):
    pass


# Properties shared by models stored in DB
class DailyRatioInDBBase(DailyRatioBase):
    id: int

    class Config:
        orm_mode = True


# Properties to return to client
class DailyRatio(DailyRatioInDBBase):
    pass


# Properties properties stored in DB
class DailyRatioInDB(DailyRatioInDBBase):
    pass
