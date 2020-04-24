from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.core.config import settings
from app.tests.utils.financial_statement import create_random_financial_statement
from app.tests.utils.utils import random_currency
from app.tests.utils.utils import random_url
from app.tests.utils.utils import random_period
from app.tests.utils.utils import random_date
from app.tests.utils.utils import random_integer


def test_create_financial_statement(client: TestClient, db: Session) -> None:
    data = {
        "period": random_period(),
        "currency": random_currency(),
        "url": random_url(),
        "publish_date": random_date().strftime("%Y-%m-%d"),
        "end_date": random_date().strftime("%Y-%m-%d"),
        "audited": True,
        "total_non_current_assets": random_integer(),
        "total_current_assets": random_integer(),
        "total_assets": random_integer(),
        "total_equity": random_integer(),
        "total_long_term_liabilities": random_integer(),
        "total_current_liabilities": random_integer(),
        "total_liabilities": random_integer(),
        "total_equities_and_liabilities": random_integer(),
        "total_revenues": random_integer(),
        "other_revenues": random_integer(),
        "total_operating_expenses": random_integer(),
        "operating_profit": random_integer(),
        "net_financial_result": random_integer(),
        "profit_before_income_tax": random_integer(),
        "net_profit": random_integer()
        }

    response = client.post(f"{settings.API_V1_STR}/financialstatements/", json=data)

    assert response.status_code == 200
    content = response.json()
    assert content["period"] == data["period"]
    assert content["currency"] == data["currency"]
    assert content["url"] == data["url"]
    assert content["publish_date"] == data["publish_date"]
    assert content["end_date"] == data["end_date"]
    assert content["audited"] == data["audited"]
    assert content["total_non_current_assets"] == data["total_non_current_assets"]
    assert content["total_current_assets"] == data["total_current_assets"]
    assert content["total_assets"] == data["total_assets"]
    assert content["total_equity"] == data["total_equity"]
    assert content["total_long_term_liabilities"] == data["total_long_term_liabilities"]
    assert content["total_current_liabilities"] == data["total_current_liabilities"]
    assert content["total_liabilities"] == data["total_liabilities"]
    assert content["total_equities_and_liabilities"] == data["total_equities_and_liabilities"]
    assert content["total_revenues"] == data["total_revenues"]
    assert content["other_revenues"] == data["other_revenues"]
    assert content["total_operating_expenses"] == data["total_operating_expenses"]
    assert content["operating_profit"] == data["operating_profit"]
    assert content["net_financial_result"] == data["net_financial_result"]
    assert content["profit_before_income_tax"] == data["profit_before_income_tax"]
    assert content["net_profit"] == data["net_profit"]
    assert "id" in content


def test_read_financial_statement(client: TestClient, db: Session) -> None:
    financial_statement = create_random_financial_statement(db)
    
    response = client.post(f"{settings.API_V1_STR}/financialstatements/{financial_statement.id}")
    
    assert response.status_code == 200
    content = response.json()
    assert content["publish_date"] == financial_statement.publish_date.strftime("%Y-%m-%d")
    assert content["end_date"] == financial_statement.end_date.strftime("%Y-%m-%d")
    assert content["period"] == financial_statement.period
    assert content["currency"] == financial_statement.currency
    assert content["url"] == financial_statement.url
    assert content["audited"] == financial_statement.audited
    assert content["total_non_current_assets"] == financial_statement.total_non_current_assets
    assert content["total_current_assets"] == financial_statement.total_current_assets
    assert content["total_assets"] == financial_statement.total_assets
    assert content["total_equity"] == financial_statement.total_equity
    assert content["total_long_term_liabilities"] == financial_statement.total_long_term_liabilities
    assert content["total_current_liabilities"] == financial_statement.total_current_liabilities
    assert content["total_liabilities"] == financial_statement.total_liabilities
    assert content["total_equities_and_liabilities"] == financial_statement.total_equities_and_liabilities
    assert content["total_revenues"] == financial_statement.total_revenues
    assert content["other_revenues"] == financial_statement.other_revenues
    assert content["total_operating_expenses"] == financial_statement.total_operating_expenses
    assert content["operating_profit"] == financial_statement.operating_profit
    assert content["net_financial_result"] == financial_statement.net_financial_result
    assert content["profit_before_income_tax"] == financial_statement.profit_before_income_tax
    assert content["net_profit"] == financial_statement.net_profit
    assert content["id"] == financial_statement.id
