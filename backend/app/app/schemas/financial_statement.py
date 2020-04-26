from typing import List

from datetime import date

from pydantic import BaseModel, HttpUrl

from app.utils import CurrencyEnum
from app.utils import PeriodEnum

# Shared properties
class FinancialStatementBase(BaseModel):
    period: PeriodEnum = None
    end_date: date = None
    publish_date: date = None
    url: HttpUrl = None
    audited: bool = None
    currency: CurrencyEnum = None
    non_current_assets: int = None 
    current_assets: int = None
    total_assets: int = None
    total_equity: int = None
    long_term_liabilities: int = None
    current_liabilities: int = None
    total_liabilities: int = None
    total_equities_and_liabilities: int = None
    total_revenues: int = None
    gross_profit: float = None
    operating_income: int = None
    profit_before_tax: int = None
    net_profit: int = None

    company_id: int = None


# Properties to receive on financial statement creation
class FinancialStatementCreate(FinancialStatementBase):
    pass


# Properties to receive on financial statement update
class FinancialStatementUpdate(FinancialStatementBase):
    pass


# Properties shared by models stored in DB
class FinancialStatementInDBBase(FinancialStatementBase):
    id: int

    class Config:
        orm_mode = True


# Properties to return to client
class FinancialStatement(FinancialStatementInDBBase):
    pass


# Properties properties stored in DB
class FinancialStatementInDB(FinancialStatementInDBBase):
    pass
