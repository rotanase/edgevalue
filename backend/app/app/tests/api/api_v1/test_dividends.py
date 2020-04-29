from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.core.config import settings
from app.tests.utils.dividend import create_random_dividend
from app.tests.utils.utils import random_date
from app.tests.utils.utils import random_currency
from app.tests.utils.utils import random_dividend_payout

def test_create_dividend(client: TestClient, db: Session) -> None:
    data = {
        "currency": random_currency(),
        "ex_dividend_date": random_date().strftime("%Y-%m-%d"),
        "pay_date": random_date().strftime("%Y-%m-%d"),
        "dividend_payout": random_dividend_payout()
    }
    response = client.post(f"{settings.API_V1_STR}/dividends/", json=data)

    assert response.status_code == 200
    content = response.json()
    assert content["currency"] == data["currency"]
    assert content["ex_dividend_date"] == data["ex_dividend_date"]
    assert content["pay_date"] == data["pay_date"]
    assert content["dividend_payout"] == data["dividend_payout"]
    assert "id" in content


def test_read_dividend(client: TestClient, db: Session) -> None:
    dividend = create_random_dividend(db)
    response = client.get(f"{settings.API_V1_STR}/dividends/{dividend.id}")
    
    assert response.status_code == 200
    content = response.json()
    assert content["currency"] == dividend.currency
    assert content["ex_dividend_date"] == dividend.ex_dividend_date.strftime("%Y-%m-%d")
    assert content["pay_date"] == dividend.pay_date.strftime("%Y-%m-%d")
    assert content["dividend_payout"] == dividend.dividend_payout
    assert content["id"] == dividend.id
