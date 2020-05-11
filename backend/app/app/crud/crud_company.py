from typing import Any

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.company import Company
from app.schemas.company import CompanyCreate, CompanyUpdate


class CRUDCompany(CRUDBase[Company, CompanyCreate, CompanyUpdate]):
    def get_by_ticker(
        self, db:Session, *, ticker: str
    ) -> Company:
        return (db.query(self.model).filter(Company.ticker == ticker).first())


company = CRUDCompany(Company)