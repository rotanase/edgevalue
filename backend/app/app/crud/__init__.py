from .crud_user import user
from .base import CRUDBase

from app.models.company import Company
from app.schemas.company import CompanyCreate, CompanyUpdate

from app.models.financial_statement import FinancialStatement
from app.schemas.financial_statement import FinancialStatementCreate, FinancialStatementUpdate

from app.models.dividend import Dividend
from app.schemas.dividend import DividendCreate, DividendUpdate


company = CRUDBase[Company, CompanyCreate, CompanyUpdate](Company)
financial_statement = CRUDBase[FinancialStatement, FinancialStatementCreate, FinancialStatementUpdate](FinancialStatement)
dividend = CRUDBase[Dividend, DividendCreate, DividendUpdate](Dividend)
