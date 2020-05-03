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
    
    # balance sheet
    non_current_assets: int = None
    cash_and_equivalents: int = None
    current_assets: int = None
    total_assets: int = None
    short_term_debt: int = None
    current_liabilities: int = None
    long_term_debt: int = None
    long_term_liabilities: int = None
    total_debt: int = None
    total_liabilities: int = None
    total_equity: int = None
    total_equities_and_liabilities: int = None

    # income statement
    total_revenues: int = None
    cost_of_revenue: int = None
    costs_of_goods_sold: int = None
    gross_profit: float = None
    operating_income: int = None
    interest_expense: int = None
    profit_before_tax: int = None
    tax_expense: int = None
    depreciation: int = None
    amortization: int = None
    net_income: int = None
    earnings_per_share: float = None

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
