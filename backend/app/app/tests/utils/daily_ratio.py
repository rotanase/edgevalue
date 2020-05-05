from sqlalchemy.orm import Session

from app import crud, models
from app.schemas.daily_ratio import DailyRatioCreate
from app.tests.utils.company import create_random_company
from app.tests.utils.utils import random_period
from app.tests.utils.utils import random_date
from app.tests.utils.utils import random_currency
from app.tests.utils.utils import random_integer
from app.tests.utils.utils import random_float


def create_random_daily_ratio(db: Session) -> models.DailyRatio:
    company = create_random_company(db)
    company_id = company.id
    period = random_period()
    end_date = random_date()
    currency = random_currency()
    market_cap = random_integer()
    price_to_earnings_ratio_ttm = random_float()
    price_to_book_ratio = random_float()
    market_to_book_ratio = random_float()
    price_to_tangible_book_value = random_float()
    enterprise_value = random_integer()
    ev_to_revenue = random_float()
    ev_to_net_income = random_float()
    ev_to_ebit = random_float()
    ev_to_ebitda = random_float()
    ev_to_assets = random_float()

    daily_ratio_in = DailyRatioCreate(
        period=period,
        end_date=end_date,
        currency=currency,
        market_cap=market_cap,
        price_to_earnings_ratio_ttm=price_to_earnings_ratio_ttm,
        price_to_book_ratio=price_to_book_ratio,
        market_to_book_ratio=market_to_book_ratio,
        price_to_tangible_book_value=price_to_tangible_book_value,
        enterprise_value=enterprise_value,
        ev_to_revenue=ev_to_revenue,
        ev_to_net_income=ev_to_net_income,
        ev_to_ebit=ev_to_ebit,
        ev_to_ebitda=ev_to_ebitda,
        ev_to_assets=ev_to_assets,
        company_id=company_id
        )
    return crud.daily_ratio.create(db=db, obj_in=daily_ratio_in)
