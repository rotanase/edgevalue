from .crud_user import user
from .crud_company import company
from .base import CRUDBase

# from app.models.company import Company
# from app.schemas.company import CompanyCreate, CompanyUpdate

from app.models.financial_statement import FinancialStatement
from app.schemas.financial_statement import FinancialStatementCreate, FinancialStatementUpdate

from app.models.dividend import Dividend
from app.schemas.dividend import DividendCreate, DividendUpdate

from app.models.daily_ratio import DailyRatio
from app.schemas.daily_ratio import DailyRatioCreate, DailyRatioUpdate

from app.models.value_metric import ValueMetric
from app.schemas.value_metric import ValueMetricCreate, ValueMetricUpdate


# company = CRUDBase[Company, CompanyCreate, CompanyUpdate](Company)
financial_statement = CRUDBase[FinancialStatement, FinancialStatementCreate, FinancialStatementUpdate](FinancialStatement)
dividend = CRUDBase[Dividend, DividendCreate, DividendUpdate](Dividend)
daily_ratio = CRUDBase[DailyRatio, DailyRatioCreate, DailyRatioUpdate](DailyRatio)
value_metric = CRUDBase[ValueMetric, ValueMetricCreate, ValueMetricUpdate](ValueMetric)
