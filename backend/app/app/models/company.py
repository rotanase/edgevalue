from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String, DateTime, BigInteger
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .financial_statement import FinancialStatement  # noqa: F401

if TYPE_CHECKING:
    from .dividend import Dividend  # noqa: F401

if TYPE_CHECKING:
    from .value_metric import ValueMetric  # noqa: F401
    
if TYPE_CHECKING:
    from .daily_ratio import DailyRatio  # noqa: F401


class Company(Base):
    __tablename__ = 'company'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    isin = Column(String, unique=True)
    number_of_shares = Column(BigInteger)
    url = Column(String, unique=True)
    ticker = Column(String)
    ipo_date = Column(DateTime)
    stock_exchange = Column(String)

    financial_statements = relationship("FinancialStatement", back_populates="company")
    dividends = relationship("Dividend", back_populates="company")
    value_metrics = relationship("ValueMetric", back_populates="company")
    daily_ratios = relationship("DailyRatio", back_populates="company")
