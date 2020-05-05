from typing import List

from datetime import date

from pydantic import BaseModel, HttpUrl

from app.utils import PeriodEnum
from app.utils import CurrencyEnum

# Shared properties
class ValueMetricBase(BaseModel):
    period: PeriodEnum = None
    end_date: date = None
    currency: CurrencyEnum = None
    book_value: int = None
    tangible_book_value: int = None
    tangible_book_value_per_share: float = None
    debt_to_equity: float = None
    equity_ratio: float = None
    debt_ratio: float = None
    cash_ratio: float = None
    gross_profit_margin: float = None
    net_profit_margin: float = None
    ebit_margin: float = None
    operating_margin: float = None
    ebitda_margin: float = None
    cash_return_on_capital_invested: float = None 
    debt_to_ebitda: float = None
    return_on_equity: float = None
    return_on_assets: float = None
    current_ratio: float = None
    working_capital: int = None
  
    company_id: int = None


# Properties to receive on value metric creation
class ValueMetricCreate(ValueMetricBase):
    pass


# Properties to receive on value metric update
class ValueMetricUpdate(ValueMetricBase):
    pass


# Properties shared by models stored in DB
class ValueMetricInDBBase(ValueMetricBase):
    id: int

    class Config:
        orm_mode = True


# Properties to return to client
class ValueMetric(ValueMetricInDBBase):
    pass


# Properties properties stored in DB
class ValueMetricInDB(ValueMetricInDBBase):
    pass
