from .crud_user import user
from .base import CRUDBase

from app.models.financial_statement import FinancialStatement
from app.schemas.financial_statement import FinancialStatementCreate, FinancialStatementUpdate

from app.models.company import Company
from app.schemas.company import CompanyCreate, CompanyUpdate


financial_statement = CRUDBase[FinancialStatement, FinancialStatementCreate, FinancialStatementUpdate](FinancialStatement)
company = CRUDBase[Company, CompanyCreate, CompanyUpdate](Company)

