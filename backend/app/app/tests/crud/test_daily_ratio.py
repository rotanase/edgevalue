from sqlalchemy.orm import Session

from app import crud
from app.schemas.daily_ratio import DailyRatioCreate, DailyRatioUpdate
from app.tests.utils.company import create_random_company
from app.tests.utils.utils import random_period
from app.tests.utils.utils import random_date
from app.tests.utils.utils import random_currency
from app.tests.utils.utils import random_integer
from app.tests.utils.utils import random_float


def test_create_daily_ratio(db: Session) -> None:
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
    daily_ratio = crud.daily_ratio.create(db=db, obj_in=daily_ratio_in)
    assert daily_ratio.period == period
    assert daily_ratio.end_date.strftime("%Y-%m-%d") == end_date.strftime("%Y-%m-%d")
    assert daily_ratio.currency == currency
    assert daily_ratio.market_cap == market_cap
    assert daily_ratio.price_to_earnings_ratio_ttm == price_to_earnings_ratio_ttm
    assert daily_ratio.price_to_book_ratio == price_to_book_ratio
    assert daily_ratio.market_to_book_ratio == market_to_book_ratio
    assert daily_ratio.price_to_tangible_book_value == price_to_tangible_book_value
    assert daily_ratio.enterprise_value == enterprise_value
    assert daily_ratio.ev_to_revenue == ev_to_revenue
    assert daily_ratio.ev_to_net_income == ev_to_net_income
    assert daily_ratio.ev_to_ebit == ev_to_ebit
    assert daily_ratio.ev_to_ebitda == ev_to_ebitda
    assert daily_ratio.ev_to_assets == ev_to_assets
    assert daily_ratio.company_id == company_id


def test_get_daily_ratio(db: Session) -> None:
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
    daily_ratio = crud.daily_ratio.create(db=db, obj_in = daily_ratio_in)
    stored_daily_ratio = crud.daily_ratio.get(db=db, id=daily_ratio.id)

    assert daily_ratio.id == stored_daily_ratio.id
    assert daily_ratio.period == stored_daily_ratio.period
    assert daily_ratio.end_date.strftime("%Y-%m-%d") == stored_daily_ratio.end_date.strftime("%Y-%m-%d")
    assert daily_ratio.currency == stored_daily_ratio.currency
    assert daily_ratio.market_cap == stored_daily_ratio.market_cap
    assert daily_ratio.price_to_earnings_ratio_ttm == stored_daily_ratio.price_to_earnings_ratio_ttm
    assert daily_ratio.price_to_book_ratio == stored_daily_ratio.price_to_book_ratio
    assert daily_ratio.market_to_book_ratio == stored_daily_ratio.market_to_book_ratio
    assert daily_ratio.price_to_tangible_book_value == stored_daily_ratio.price_to_tangible_book_value
    assert daily_ratio.enterprise_value == stored_daily_ratio.enterprise_value
    assert daily_ratio.ev_to_revenue == stored_daily_ratio.ev_to_revenue
    assert daily_ratio.ev_to_net_income == stored_daily_ratio.ev_to_net_income
    assert daily_ratio.ev_to_ebit == stored_daily_ratio.ev_to_ebit
    assert daily_ratio.ev_to_ebitda == stored_daily_ratio.ev_to_ebitda
    assert daily_ratio.ev_to_assets == stored_daily_ratio.ev_to_assets
    assert daily_ratio.company_id == stored_daily_ratio.company_id


def test_update_daily_ratio(db: Session) -> None:
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
    daily_ratio = crud.daily_ratio.create(db=db, obj_in = daily_ratio_in)

    period2 = random_period()
    market_cap2 = random_integer()
    ev_to_revenue2 = random_float()
    ev_to_ebit2 = random_float()

    daily_ratio_update = DailyRatioUpdate(
        period=period2,
        market_cap=market_cap2,
        ev_to_revenue=ev_to_revenue2,
        ev_to_ebit2=ev_to_ebit2
        )
    daily_ratio2 = crud.daily_ratio.update(db=db, db_obj=daily_ratio, obj_in=daily_ratio_update)
    assert daily_ratio.id == daily_ratio2.id
    assert daily_ratio2.period == period2
    assert daily_ratio.end_date.strftime("%Y-%m-%d") == daily_ratio2.end_date.strftime("%Y-%m-%d")
    assert daily_ratio.currency == daily_ratio2.currency
    assert daily_ratio2.market_cap == market_cap2
    assert daily_ratio.price_to_earnings_ratio_ttm == daily_ratio2.price_to_earnings_ratio_ttm
    assert daily_ratio.price_to_book_ratio == daily_ratio2.price_to_book_ratio
    assert daily_ratio.market_to_book_ratio == daily_ratio2.market_to_book_ratio
    assert daily_ratio.price_to_tangible_book_value == daily_ratio2.price_to_tangible_book_value
    assert daily_ratio.enterprise_value == daily_ratio2.enterprise_value
    assert daily_ratio2.ev_to_revenue == ev_to_revenue2
    assert daily_ratio.ev_to_net_income == daily_ratio2.ev_to_net_income
    assert daily_ratio2.ev_to_ebit == ev_to_ebit2
    assert daily_ratio.ev_to_ebitda == daily_ratio2.ev_to_ebitda
    assert daily_ratio.ev_to_assets == daily_ratio2.ev_to_assets


def test_delete_daily_ratio(db: Session) -> None:
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
    daily_ratio = crud.daily_ratio.create(db=db, obj_in=daily_ratio_in)
    daily_ratio2 = crud.daily_ratio.remove(db=db, id=daily_ratio.id)
    daily_ratio3 = crud.daily_ratio.get(db=db, id=daily_ratio.id)
    assert daily_ratio3 is None
    assert daily_ratio2.id == daily_ratio.id
    assert daily_ratio2.period == period
    assert daily_ratio2.end_date.strftime("%Y-%m-%d") == end_date.strftime("%Y-%m-%d")
    assert daily_ratio2.currency == currency
    assert daily_ratio2.market_cap == market_cap
    assert daily_ratio2.price_to_earnings_ratio_ttm == price_to_earnings_ratio_ttm
    assert daily_ratio2.price_to_book_ratio == price_to_book_ratio
    assert daily_ratio2.market_to_book_ratio == market_to_book_ratio
    assert daily_ratio2.price_to_tangible_book_value == price_to_tangible_book_value
    assert daily_ratio2.enterprise_value == enterprise_value
    assert daily_ratio2.ev_to_revenue == ev_to_revenue
    assert daily_ratio2.ev_to_net_income == ev_to_net_income
    assert daily_ratio2.ev_to_ebit == ev_to_ebit
    assert daily_ratio2.ev_to_ebitda == ev_to_ebitda
    assert daily_ratio2.ev_to_assets == ev_to_assets
    assert daily_ratio2.company_id == company_id
