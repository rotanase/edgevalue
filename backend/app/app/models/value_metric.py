from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, BigInteger, Float
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .company import Company  # noqa: F401


class ValueMetric(Base):
    __tablename__ = 'value_metrics'

    id = Column(Integer, primary_key=True, index=True)
    period = Column(String)
    end_date = Column(DateTime)
    currency = Column(String)
    book_value = Column(BigInteger)
    tangible_book_value = Column(BigInteger)
    tangible_book_value_per_share = Column(Float)
    debt_to_equity = Column(Float)
    equity_ratio = Column(Float)
    debt_ratio = Column(Float)
    cash_ratio = Column(Float)
    gross_profit_margin = Column(Float)
    net_profit_margin = Column(Float)
    ebit_margin = Column(Float)
    operating_margin = Column(Float)
    ebitda_margin = Column(Float)
    cash_return_on_capital_invested = Column(Float) 
    debt_to_ebitda = Column(Float)
    return_on_equity = Column(Float)
    return_on_assets = Column(Float)
    current_ratio = Column(Float)
    working_capital = Column(BigInteger)
  
    company_id = Column(Integer, ForeignKey('company.id'))
    company = relationship("Company", back_populates="value_metrics")
