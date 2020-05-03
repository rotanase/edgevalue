from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean, BigInteger, Float
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .company import Company  # noqa: F401


class FinancialStatement(Base):
    __tablename__ = 'financial_statement'

    id = Column(Integer, primary_key=True, index=True)
    period = Column(String)
    end_date = Column(DateTime)
    publish_date = Column(DateTime)
    url = Column(String, unique=True)
    audited = Column(Boolean)
    currency = Column(String)
 
    # balance sheet
    non_current_assets = Column(BigInteger)
    cash_and_equivalents = Column(BigInteger) 
    current_assets = Column(BigInteger)
    total_assets = Column(BigInteger)
    short_term_debt = Column(BigInteger)
    current_liabilities = Column(BigInteger)
    long_term_debt = Column(BigInteger)
    long_term_liabilities = Column(BigInteger)
    total_debt = Column(BigInteger)
    total_liabilities = Column(BigInteger)
    total_equity = Column(BigInteger)
    total_equities_and_liabilities = Column(BigInteger)
 
    # income statement
    total_revenues = Column(BigInteger)
    cost_of_revenue = Column(BigInteger)
    costs_of_goods_sold = Column(BigInteger)
    gross_profit = Column(BigInteger)
    operating_income = Column(BigInteger)
    interest_expense = Column(BigInteger) 
    profit_before_tax = Column(BigInteger)
    tax_expense = Column(BigInteger)
    depreciation = Column(BigInteger)
    amortization = Column(BigInteger)
    net_income = Column(BigInteger)
    earnings_per_share = Column(Float)
    
    company_id = Column(Integer, ForeignKey("company.id"))
    company = relationship("Company", back_populates="financial_statements")
