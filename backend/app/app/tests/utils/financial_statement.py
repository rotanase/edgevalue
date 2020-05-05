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
from app.tests.utils.utils import random_float


def create_random_financial_statement(db: Session) -> models.FinancialStatement:
    company = create_random_company(db)
    company_id = company.id
    period = random_period()
    end_date = random_date()
    publish_date = random_date()
    url = random_url()
    audited = random_bool()
    currency = random_currency()
    non_current_assets = random_integer()
    cash_and_equivalents = random_integer()
    current_assets = random_integer()
    total_assets = random_integer()
    short_term_debt = random_integer()
    current_liabilities = random_integer()
    long_term_debt = random_integer()
    long_term_liabilities = random_integer()
    total_debt = random_integer()
    total_liabilities = random_integer()
    total_equity = random_integer()
    total_equities_and_liabilities = random_integer()
    total_revenues = random_integer()
    cost_of_revenue = random_integer()
    costs_of_goods_sold = random_integer()
    gross_profit = random_integer()
    ebitda = random_integer()
    ebit = random_integer()
    operating_income = random_integer()
    interest_expense = random_integer()
    profit_before_tax = random_integer()
    tax_expense = random_integer()
    depreciation = random_integer()
    amortization = random_integer()
    net_income = random_integer()
    earnings_per_share = random_float()
    
    financial_statement_in = FinancialStatementCreate(       
        period=period,
        end_date=end_date,
        publish_date=publish_date,
        url=url,
        audited=audited,
        currency=currency,
        non_current_assets=non_current_assets,
        cash_and_equivalents=cash_and_equivalents,
        current_assets=current_assets,
        total_assets=total_assets,
        short_term_debt=short_term_debt,
        current_liabilities=current_liabilities,
        long_term_debt=long_term_debt,
        long_term_liabilities=long_term_liabilities,
        total_debt=total_debt,
        total_liabilities=total_liabilities,
        total_equity=total_equity,
        total_equities_and_liabilities=total_equities_and_liabilities,
        total_revenues=total_revenues,
        cost_of_revenue=cost_of_revenue,
        costs_of_goods_sold=costs_of_goods_sold,
        gross_profit=gross_profit,
        ebitda=ebitda,
        ebit=ebit,
        operating_income=operating_income,
        interest_expense=interest_expense,
        profit_before_tax=profit_before_tax,
        tax_expense=tax_expense,
        depreciation=depreciation,
        amortization=amortization,
        net_income=net_income,
        earnings_per_share=earnings_per_share,
        company_id=company_id
        )
    return crud.financial_statement.create(db=db, obj_in=financial_statement_in)
