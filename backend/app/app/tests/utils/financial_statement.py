from sqlalchemy.orm import Session

from app import crud, models
from app.schemas.financial_statement import FinancialStatementCreate
from app.tests.utils.company import create_random_company
from app.tests.utils.utils import random_integer
from app.tests.utils.utils import random_bool
from app.tests.utils.utils import random_date
from app.tests.utils.utils import random_url
from app.tests.utils.utils import random_currency
from app.tests.utils.utils import random_period


def create_random_financial_statement(db: Session) -> models.FinancialStatement:
    company = create_random_company(db)
    company_id = company.id
    period = random_period()
    currency = random_currency()
    url = random_url()
    publish_date = random_date()
    end_date = random_date()
    audited = random_bool()
    non_current_assets = random_integer()
    current_assets = random_integer()
    total_assets = random_integer()
    total_equity = random_integer()
    long_term_liabilities = random_integer()
    current_liabilities = random_integer()
    total_liabilities = random_integer()
    total_equities_and_liabilities = random_integer()
    total_revenues = random_integer()
    gross_profit = random_integer()
    operating_income = random_integer()
    profit_before_tax = random_integer()
    net_profit = random_integer()
    
    financial_statement_in = FinancialStatementCreate(       
        period=period,
        currency=currency,
        url=url,
        publish_date=publish_date,
        end_date=end_date,
        audited=audited,
        non_current_assets=non_current_assets,
        current_assets=current_assets,
        total_assets=total_assets,
        total_equity=total_equity,
        long_term_liabilities=long_term_liabilities,
        current_liabilities=current_liabilities,
        total_liabilities=total_liabilities,
        total_equities_and_liabilities=total_equities_and_liabilities,
        total_revenues=total_revenues,
        gross_profit=gross_profit,
        operating_income=operating_income,
        profit_before_tax=profit_before_tax,
        net_profit=net_profit,
        company_id=company_id
        )
    return crud.financial_statement.create(db=db, obj_in=financial_statement_in)
