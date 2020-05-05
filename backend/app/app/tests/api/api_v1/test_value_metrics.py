from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.core.config import settings
from app.tests.utils.value_metric import create_random_value_metric
from app.tests.utils.utils import random_period
from app.tests.utils.utils import random_date
from app.tests.utils.utils import random_currency
from app.tests.utils.utils import random_integer
from app.tests.utils.utils import random_float


def test_create_value_metric(client: TestClient, superuser_token_headers: dict, db: Session) -> None:
    data = {
        "period": random_period(),
        "end_date": random_date().strftime("%Y-%m-%d"),
        "currency": random_currency(),
        "book_value": random_integer(),
        "tangible_book_value": random_integer(),
        "tangible_book_value_per_share": random_float(),
        "debt_to_equity": random_float(),
        "equity_ratio": random_float(),
        "debt_ratio": random_float(),
        "cash_ratio": random_float(),
        "gross_profit_margin": random_float(),
        "net_profit_margin": random_float(),
        "ebit_margin": random_float(),
        "operating_margin": random_float(),
        "ebitda_margin": random_float(),
        "cash_return_on_capital_invested": random_float(), 
        "debt_to_ebitda": random_float(),
        "return_on_equity": random_float(),
        "return_on_assets": random_float(),
        "current_ratio": random_float(),
        "working_capital": random_integer()
        }

    response = client.post(f"{settings.API_V1_STR}/valuemetrics/", headers=superuser_token_headers, json=data)

    assert response.status_code == 200
    content = response.json()
    assert content["period"] == data["period"]
    assert content["end_date"] == data["end_date"]
    assert content["currency"] == data["currency"]
    assert content["book_value"] == data["book_value"]
    assert content["tangible_book_value"] == data["tangible_book_value"]
    assert content["tangible_book_value_per_share"] == data["tangible_book_value_per_share"]
    assert content["debt_to_equity"] == data["debt_to_equity"]
    assert content["equity_ratio"] == data["equity_ratio"]
    assert content["debt_ratio"] == data["debt_ratio"]
    assert content["cash_ratio"] == data["cash_ratio"]
    assert content["gross_profit_margin"] == data["gross_profit_margin"]
    assert content["net_profit_margin"] == data["net_profit_margin"]
    assert content["ebit_margin"] == data["ebit_margin"]
    assert content["operating_margin"] == data["operating_margin"]
    assert content["ebitda_margin"] == data["ebitda_margin"]
    assert content["cash_return_on_capital_invested"] == data["cash_return_on_capital_invested"] 
    assert content["debt_to_ebitda"] == data["debt_to_ebitda"]
    assert content["return_on_equity"] == data["return_on_equity"]
    assert content["return_on_assets"] == data["return_on_assets"]
    assert content["current_ratio"] == data["current_ratio"]
    assert content["working_capital"] == data["working_capital"]
    assert "id" in content


def test_read_value_metric(client: TestClient, db: Session) -> None:
    value_metric = create_random_value_metric(db)
    
    response = client.get(f"{settings.API_V1_STR}/valuemetrics/{value_metric.id}")
    
    assert response.status_code == 200
    content = response.json()
    assert content["period"] == value_metric.period
    assert content["end_date"] == value_metric.end_date.strftime("%Y-%m-%d")
    assert content["currency"] == value_metric.currency
    assert content["book_value"] == value_metric.book_value
    assert content["tangible_book_value"] == value_metric.tangible_book_value
    assert content["tangible_book_value_per_share"] == value_metric.tangible_book_value_per_share
    assert content["debt_to_equity"] == value_metric.debt_to_equity
    assert content["equity_ratio"] == value_metric.equity_ratio
    assert content["debt_ratio"] == value_metric.debt_ratio
    assert content["cash_ratio"] == value_metric.cash_ratio
    assert content["gross_profit_margin"] == value_metric.gross_profit_margin
    assert content["net_profit_margin"] == value_metric.net_profit_margin
    assert content["ebit_margin"] == value_metric.ebit_margin
    assert content["operating_margin"] == value_metric.operating_margin
    assert content["ebitda_margin"] == value_metric.ebitda_margin
    assert content["cash_return_on_capital_invested"] == value_metric.cash_return_on_capital_invested
    assert content["debt_to_ebitda"] == value_metric.debt_to_ebitda
    assert content["return_on_equity"] == value_metric.return_on_equity
    assert content["return_on_assets"] == value_metric.return_on_assets
    assert content["current_ratio"] == value_metric.current_ratio
    assert content["working_capital"] == value_metric.working_capital
    assert content["id"] == value_metric.id
