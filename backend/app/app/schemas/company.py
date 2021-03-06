from typing import List

from datetime import date

from pydantic import BaseModel, HttpUrl

from app.schemas.financial_statement import FinancialStatement
from app.schemas.dividend import Dividend
from app.schemas.value_metric import ValueMetric
from app.schemas.daily_ratio import DailyRatio



# Shared properties
class CompanyBase(BaseModel):
    name: str = None
    isin: str = None
    number_of_shares: int = None
    url: HttpUrl = None
    ticker: str = None
    ipo_date: date = None
    stock_exchange: str = None
    financial_statements: List[FinancialStatement] = []
    dividends: List[Dividend] = []
    value_metrics: List[ValueMetric] = []
    daily_ratios: List[DailyRatio] = []


# Properties to receive on company creation
class CompanyCreate(CompanyBase):
    pass


# Properties to receive on company update
class CompanyUpdate(CompanyBase):
    pass


# Properties shared by models stored in DB
class CompanyInDBBase(CompanyBase):
    id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Company(CompanyInDBBase):
    pass


# Properties properties stored in DB
class CompanyInDB(CompanyInDBBase):
    pass
