from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, BigInteger, Float
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .company import Company  # noqa: F401


class DailyRatio(Base):
    __tablename__ = 'daily_ratio'

    id = Column(Integer, primary_key=True, index=True)
    period = Column(String)
    end_date = Column(DateTime)
    currency = Column(String)
    market_cap = Column(BigInteger)
    price_to_earnings_ratio_ttm = Column(Float)
    price_to_book_ratio = Column(Float)
    market_to_book_ratio = Column(Float)
    price_to_tangible_book_value = Column(Float)
    enterprise_value = Column(BigInteger)
    ev_to_revenue = Column(Float)
    ev_to_net_income = Column(Float)
    ev_to_ebit = Column(Float)
    ev_to_ebitda = Column(Float)
    ev_to_assets = Column(Float)

    company_id = Column(Integer, ForeignKey("company.id"))
    company = relationship("Company", back_populates="daily_ratios")
