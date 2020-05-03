from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.core.config import settings
from app.tests.utils.financial_statement import create_random_financial_statement
from app.tests.utils.utils import random_currency
from app.tests.utils.utils import random_url
from app.tests.utils.utils import random_period
from app.tests.utils.utils import random_date
from app.tests.utils.utils import random_integer
from app.tests.utils.utils import random_eps


def test_create_financial_statement(client: TestClient, db: Session) -> None:
    data = {
        "period": random_period(),
        "end_date": random_date().strftime("%Y-%m-%d"),
        "publish_date": random_date().strftime("%Y-%m-%d"),
        "url": random_url(),
        "audited": True,
        "currency": random_currency(),
        "non_current_assets": random_integer(),
        "cash_and_equivalents": random_integer(),
        "current_assets": random_integer(),
        "total_assets": random_integer(),
        "short_term_debt": random_integer(),
        "current_liabilities": random_integer(),
        "long_term_debt": random_integer(),
        "long_term_liabilities": random_integer(),
        "total_debt": random_integer(),
        "total_liabilities": random_integer(),
        "total_equity": random_integer(),
        "total_equities_and_liabilities": random_integer(),
        "total_revenues": random_integer(),
        "cost_of_revenue": random_integer(),
        "costs_of_goods_sold": random_integer(),
        "gross_profit": random_integer(),
        "operating_income": random_integer(),
        "interest_expense": random_integer(),
        "profit_before_tax": random_integer(),
        "tax_expense": random_integer(),
        "depreciation": random_integer(),
        "amortization": random_integer(),
        "net_income": random_integer(),
        "earnings_per_share": random_eps()
        }

    response = client.post(f"{settings.API_V1_STR}/financialstatements/", json=data)

    assert response.status_code == 200
    content = response.json()
    assert content["period"] == data["period"]
    assert content["end_date"] == data["end_date"]
    assert content["publish_date"] == data["publish_date"]
    assert content["url"] == data["url"]
    assert content["audited"] == data["audited"]
    assert content["currency"] == data["currency"]
    assert content["non_current_assets"] == data["non_current_assets"]
    assert content["cash_and_equivalents"] == data["cash_and_equivalents"]
    assert content["current_assets"] == data["current_assets"]
    assert content["total_assets"] == data["total_assets"]
    assert content["short_term_debt"] == data["short_term_debt"]
    assert content["current_liabilities"] == data["current_liabilities"]
    assert content["long_term_debt"] == data["long_term_debt"]
    assert content["long_term_liabilities"] == data["long_term_liabilities"]
    assert content["total_debt"] == data["total_debt"]
    assert content["total_liabilities"] == data["total_liabilities"]
    assert content["total_equity"] == data["total_equity"]
    assert content["total_equities_and_liabilities"] == data["total_equities_and_liabilities"]
    assert content["total_revenues"] == data["total_revenues"]
    assert content["cost_of_revenue"] == data["cost_of_revenue"]
    assert content["costs_of_goods_sold"] == data["costs_of_goods_sold"]
    assert content["gross_profit"] == data["gross_profit"]
    assert content["operating_income"] == data["operating_income"]
    assert content["interest_expense"] == data["interest_expense"]
    assert content["profit_before_tax"] == data["profit_before_tax"]
    assert content["tax_expense"] == data["tax_expense"]
    assert content["depreciation"] == data["depreciation"]
    assert content["amortization"] == data["amortization"]
    assert content["net_income"] == data["net_income"]
    assert content["earnings_per_share"] == data["earnings_per_share"]
    assert "id" in content


def test_read_financial_statement(client: TestClient, db: Session) -> None:
    financial_statement = create_random_financial_statement(db)
    
    response = client.get(f"{settings.API_V1_STR}/financialstatements/{financial_statement.id}")
    
    assert response.status_code == 200
    content = response.json()
    assert content["period"] == financial_statement.period
    assert content["end_date"] == financial_statement.end_date.strftime("%Y-%m-%d")
    assert content["publish_date"] == financial_statement.publish_date.strftime("%Y-%m-%d")
    assert content["url"] == financial_statement.url
    assert content["audited"] == financial_statement.audited
    assert content["currency"] == financial_statement.currency
    assert content["non_current_assets"] == financial_statement.non_current_assets
    assert content["cash_and_equivalents"] == financial_statement.cash_and_equivalents
    assert content["current_assets"] == financial_statement.current_assets
    assert content["total_assets"] == financial_statement.total_assets
    assert content["short_term_debt"] == financial_statement.short_term_debt
    assert content["current_liabilities"] == financial_statement.current_liabilities
    assert content["long_term_debt"] == financial_statement.long_term_debt
    assert content["long_term_liabilities"] == financial_statement.long_term_liabilities
    assert content["total_debt"] == financial_statement.total_debt
    assert content["total_liabilities"] == financial_statement.total_liabilities
    assert content["total_equity"] == financial_statement.total_equity
    assert content["total_equities_and_liabilities"] == financial_statement.total_equities_and_liabilities
    assert content["total_revenues"] == financial_statement.total_revenues
    assert content["cost_of_revenue"] == financial_statement.cost_of_revenue
    assert content["costs_of_goods_sold"] == financial_statement.costs_of_goods_sold
    assert content["gross_profit"] == financial_statement.gross_profit
    assert content["operating_income"] == financial_statement.operating_income
    assert content["interest_expense"] == financial_statement.interest_expense
    assert content["profit_before_tax"] == financial_statement.profit_before_tax
    assert content["tax_expense"] == financial_statement.tax_expense
    assert content["depreciation"] == financial_statement.depreciation
    assert content["amortization"] == financial_statement.amortization
    assert content["net_income"] == financial_statement.net_income
    assert content["earnings_per_share"] == financial_statement.earnings_per_share
    assert content["id"] == financial_statement.id
