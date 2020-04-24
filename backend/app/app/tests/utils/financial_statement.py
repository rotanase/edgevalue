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
    total_non_current_assets = random_integer()
    total_current_assets = random_integer()
    total_assets = random_integer()
    total_equity = random_integer()
    total_long_term_liabilities = random_integer()
    total_current_liabilities = random_integer()
    total_liabilities = random_integer()
    total_equities_and_liabilities = random_integer()
    total_revenues = random_integer()
    other_revenues = random_integer()
    total_operating_expenses = random_integer()
    operating_profit = random_integer()
    net_financial_result = random_integer()
    profit_before_income_tax = random_integer()
    net_profit = random_integer()
    
    financial_statement_in = FinancialStatementCreate(       
        period=period,
        currency=currency,
        url=url,
        publish_date=publish_date,
        end_date=end_date,
        audited=audited,
        total_non_current_assets=total_non_current_assets,
        total_current_assets=total_current_assets,
        total_assets=total_assets,
        total_equity=total_equity,
        total_long_term_liabilities=total_long_term_liabilities,
        total_current_liabilities=total_current_liabilities,
        total_liabilities=total_liabilities,
        total_equities_and_liabilities=total_equities_and_liabilities,
        total_revenues=total_revenues,
        other_revenues=other_revenues,
        total_operating_expenses=total_operating_expenses,
        operating_profit=operating_profit,
        net_financial_result=net_financial_result,
        profit_before_income_tax=profit_before_income_tax,
        net_profit=net_profit,
        company_id=company_id
        )
    return crud.financial_statement.create(db=db, obj_in=financial_statement_in)
