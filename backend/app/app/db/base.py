# Import all the models, so that Base has them before being
# imported by Alembic
from app.db.base_class import Base  # noqa
from app.models.user import User  # noqa
from app.models.company import Company  # noqa
from app.models.financial_statement import FinancialStatement  # noqa
from app.models.dividend import Dividend  # noqa
from app.models.daily_ratio import DailyRatio  # noqa
from app.models.value_metric import ValueMetric  # noqa
