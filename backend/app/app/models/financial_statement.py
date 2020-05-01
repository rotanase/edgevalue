from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean, BigInteger
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
    non_current_assets = Column(BigInteger)
    current_assets = Column(BigInteger)
    total_assets = Column(BigInteger)
    total_equity = Column(BigInteger)
    long_term_liabilities = Column(BigInteger)
    current_liabilities = Column(BigInteger)
    total_liabilities = Column(BigInteger)
    total_equities_and_liabilities = Column(BigInteger)
    total_revenues = Column(BigInteger)
    gross_profit = Column(BigInteger)
    operating_income = Column(BigInteger)
    profit_before_tax = Column(BigInteger)
    net_income = Column(BigInteger)
    
    company_id = Column(Integer, ForeignKey("company.id"))
    company = relationship("Company", back_populates="financial_statements")
