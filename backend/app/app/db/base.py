# Import all the models, so that Base has them before being
# imported by Alembic
from app.db.base_class import Base  # noqa
from app.models.user import User  # noqa
from app.models.company import Company  # noqa
from app.models.financial_statement import FinancialStatement  # noqa