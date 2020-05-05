from sqlalchemy.orm import Session

from app import crud, models
from app.schemas.value_metric import ValueMetricCreate
from app.tests.utils.company import create_random_company
from app.tests.utils.utils import random_period
from app.tests.utils.utils import random_date
from app.tests.utils.utils import random_currency
from app.tests.utils.utils import random_integer
from app.tests.utils.utils import random_float


def create_random_value_metric(db: Session) -> models.ValueMetric:
    company = create_random_company(db)
    company_id = company.id
    period = random_period()
    end_date = random_date()
    currency = random_currency()
    book_value = random_integer()
    tangible_book_value = random_integer()
    tangible_book_value_per_share = random_float()
    debt_to_equity = random_float()
    equity_ratio = random_float()
    debt_ratio = random_float()
    cash_ratio = random_float()
    gross_profit_margin = random_float()
    net_profit_margin = random_float()
    ebit_margin = random_float()
    operating_margin = random_float()
    ebitda_margin = random_float()
    cash_return_on_capital_invested = random_float() 
    debt_to_ebitda = random_float()
    return_on_equity = random_float()
    return_on_assets = random_float()
    current_ratio = random_float()
    working_capital = random_integer()

    value_metric_in = ValueMetricCreate(
        period=period,
        end_date=end_date,
        currency=currency,
        book_value=book_value,
        tangible_book_value=tangible_book_value,
        tangible_book_value_per_share=tangible_book_value_per_share,
        debt_to_equity=debt_to_equity,
        equity_ratio=equity_ratio,
        debt_ratio=debt_ratio,
        cash_ratio=cash_ratio,
        gross_profit_margin=gross_profit_margin,
        net_profit_margin=net_profit_margin,
        ebit_margin=ebit_margin,
        operating_margin=operating_margin,
        ebitda_margin=ebitda_margin,
        cash_return_on_capital_invested=cash_return_on_capital_invested, 
        debt_to_ebitda=debt_to_ebitda,
        return_on_equity=return_on_equity,
        return_on_assets=return_on_assets,
        current_ratio=current_ratio,
        working_capital=working_capital,
        company_id=company_id
        )
    return crud.value_metric.create(db=db, obj_in=value_metric_in)
