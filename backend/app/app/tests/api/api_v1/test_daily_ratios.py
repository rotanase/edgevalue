from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.core.config import settings
from app.tests.utils.daily_ratio import create_random_daily_ratio
from app.tests.utils.utils import random_period
from app.tests.utils.utils import random_date
from app.tests.utils.utils import random_currency
from app.tests.utils.utils import random_integer
from app.tests.utils.utils import random_float


def test_create_daily_ratio(client: TestClient, db: Session) -> None:
    data = {
        "period": random_period(),
        "end_date": random_date().strftime("%Y-%m-%d"),
        "currency": random_currency(),
        "market_cap": random_integer(),
        "price_to_earnings_ratio_ttm": random_float(),
        "price_to_book_ratio": random_float(),
        "market_to_book_ratio": random_float(),
        "price_to_tangible_book_value": random_float(),
        "enterprise_value": random_integer(),
        "ev_to_revenue": random_float(),
        "ev_to_net_income": random_float(),
        "ev_to_ebit": random_float(),
        "ev_to_ebitda": random_float(),
        "ev_to_assets": random_float()
        }

    response = client.post(f"{settings.API_V1_STR}/dailyratios/", json=data)

    assert response.status_code == 200
    content = response.json()
    assert content["period"] == data["period"]
    assert content["end_date"] == data["end_date"]
    assert content["currency"] == data["currency"]
    assert content["market_cap"] == data["market_cap"]
    assert content["price_to_earnings_ratio_ttm"] == data["price_to_earnings_ratio_ttm"]
    assert content["price_to_book_ratio"] == data["price_to_book_ratio"]
    assert content["market_to_book_ratio"] == data["market_to_book_ratio"]
    assert content["price_to_tangible_book_value"] == data["price_to_tangible_book_value"]
    assert content["enterprise_value"] == data["enterprise_value"]
    assert content["ev_to_revenue"] == data["ev_to_revenue"]
    assert content["ev_to_net_income"] == data["ev_to_net_income"]
    assert content["ev_to_ebit"] == data["ev_to_ebit"]
    assert content["ev_to_ebitda"] == data["ev_to_ebitda"]
    assert content["ev_to_assets"] == data["ev_to_assets"]
    assert "id" in content


def test_read_daily_ratio(client: TestClient, db: Session) -> None:
    daily_ratio = create_random_daily_ratio(db)
    
    response = client.get(f"{settings.API_V1_STR}/dailyratios/{daily_ratio.id}")
    
    assert response.status_code == 200
    content = response.json()
    assert content["period"] == daily_ratio.period
    assert content["end_date"] == daily_ratio.end_date.strftime("%Y-%m-%d")
    assert content["currency"] == daily_ratio.currency
    assert content["market_cap"] == daily_ratio.market_cap
    assert content["price_to_earnings_ratio_ttm"] == daily_ratio.price_to_earnings_ratio_ttm
    assert content["price_to_book_ratio"] == daily_ratio.price_to_book_ratio
    assert content["market_to_book_ratio"] == daily_ratio.market_to_book_ratio
    assert content["price_to_tangible_book_value"] == daily_ratio.price_to_tangible_book_value
    assert content["enterprise_value"] == daily_ratio.enterprise_value
    assert content["ev_to_revenue"] == daily_ratio.ev_to_revenue
    assert content["ev_to_net_income"] == daily_ratio.ev_to_net_income
    assert content["ev_to_ebit"] == daily_ratio.ev_to_ebit
    assert content["ev_to_ebitda"] == daily_ratio.ev_to_ebitda
    assert content["ev_to_assets"] == daily_ratio.ev_to_assets
    assert content["id"] == daily_ratio.id
