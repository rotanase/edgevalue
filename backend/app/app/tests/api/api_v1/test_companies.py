from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.core.config import settings
from app.tests.utils.company import create_random_company
from app.tests.utils.utils import random_currency
from app.tests.utils.utils import random_url
from app.tests.utils.utils import random_period
from app.tests.utils.utils import random_date
from app.tests.utils.utils import random_integer
from app.tests.utils.utils import random_lower_string
from app.tests.utils.utils import random_isin
from app.tests.utils.utils import random_number_of_shares


def test_create_company(client: TestClient, db: Session) -> None:
    data = {
        "name": random_lower_string(),
        "isin": random_isin(),
        "number_of_shares": random_number_of_shares(),
        "url": random_url(),
        "ticker": random_lower_string(),
        "ipo_date": random_date().strftime("%Y-%m-%d"),
        "stock_exchange": random_lower_string()
        }

    response = client.post(f"{settings.API_V1_STR}/companies/", json=data)

    assert response.status_code == 200
    content = response.json()
    assert content["name"] == data["name"]
    assert content["isin"] == data["isin"]
    assert content["number_of_shares"] == data["number_of_shares"]
    assert content["url"] == data["url"]
    assert content["ticker"] == data["ticker"]
    assert content["ipo_date"] == data["ipo_date"]
    assert content["stock_exchange"] == data["stock_exchange"]
    assert "id" in content


def test_read_company(client: TestClient, db: Session) -> None:
    company = create_random_company(db)
    
    response = client.get(f"{settings.API_V1_STR}/companies/{company.id}")

    assert response.status_code == 200
    content = response.json()
    assert content["name"] == company.name
    assert content["isin"] == company.isin
    assert content["number_of_shares"] == company.number_of_shares
    assert content["url"] == company.url
    assert content["ticker"] == company.ticker
    assert content["ipo_date"] == company.ipo_date.strftime("%Y-%m-%d")
    assert content["stock_exchange"] == company.stock_exchange
    assert content["id"] == company.id
