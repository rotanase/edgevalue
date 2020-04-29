from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Float
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .company import Company  # noqa: F401


class Dividend(Base):
    __tablename__ = 'dividend'

    id = Column(Integer, primary_key=True, index=True)
    currency = Column(String)
    ex_dividend_date = Column(DateTime)
    pay_date = Column(DateTime)
    dividend_payout = Column(Float)

    company_id = Column(Integer, ForeignKey("company.id"))
    company = relationship("Company", back_populates="dividends")



