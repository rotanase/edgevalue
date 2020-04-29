from sqlalchemy.orm import Session

from app import crud
from app.schemas.financial_statement import FinancialStatementCreate, FinancialStatementUpdate
from app.tests.utils.company import create_random_company
from app.tests.utils.utils import random_integer
from app.tests.utils.utils import random_bool
from app.tests.utils.utils import random_date
from app.tests.utils.utils import random_url
from app.tests.utils.utils import random_currency
from app.tests.utils.utils import random_period


def test_create_financial_statement(db: Session) -> None:
    company = create_random_company(db)
    company_id = company.id
    period = random_period()
    currency = random_currency()
    url = random_url()
    publish_date = random_date()
    end_date = random_date()
    audited = random_bool()
    non_current_assets = random_integer()
    current_assets = random_integer()
    total_assets = random_integer()
    total_equity = random_integer()
    long_term_liabilities = random_integer()
    current_liabilities = random_integer()
    total_liabilities = random_integer()
    total_equities_and_liabilities = random_integer()
    total_revenues = random_integer()
    gross_profit = random_integer()
    operating_income = random_integer()
    profit_before_tax = random_integer()
    net_profit = random_integer()
    
    financial_statement_in = FinancialStatementCreate(       
        period=period,
        currency=currency,
        url=url,
        publish_date=publish_date,
        end_date=end_date,
        audited=audited,
        non_current_assets=non_current_assets,
        current_assets=current_assets,
        total_assets=total_assets,
        total_equity=total_equity,
        long_term_liabilities=long_term_liabilities,
        current_liabilities=current_liabilities,
        total_liabilities=total_liabilities,
        total_equities_and_liabilities=total_equities_and_liabilities,
        total_revenues=total_revenues,
        gross_profit=gross_profit,
        operating_income=operating_income,
        profit_before_tax=profit_before_tax,
        net_profit=net_profit,
        company_id=company_id
        )

    financial_statement = crud.financial_statement.create(db=db, obj_in=financial_statement_in)
    assert financial_statement.publish_date.strftime("%Y-%m-%d") == publish_date.strftime("%Y-%m-%d")
    assert financial_statement.end_date.strftime("%Y-%m-%d") == end_date.strftime("%Y-%m-%d")
    assert financial_statement.period == period
    assert financial_statement.currency == currency
    assert financial_statement.url == url
    assert financial_statement.audited == audited
    assert financial_statement.non_current_assets == non_current_assets
    assert financial_statement.current_assets == current_assets
    assert financial_statement.total_assets == total_assets
    assert financial_statement.total_equity == total_equity
    assert financial_statement.long_term_liabilities == long_term_liabilities
    assert financial_statement.current_liabilities == current_liabilities
    assert financial_statement.total_liabilities == total_liabilities
    assert financial_statement.total_equities_and_liabilities == total_equities_and_liabilities
    assert financial_statement.total_revenues == total_revenues
    assert financial_statement.gross_profit == gross_profit
    assert financial_statement.operating_income == operating_income
    assert financial_statement.profit_before_tax == profit_before_tax
    assert financial_statement.net_profit == net_profit
    assert financial_statement.company_id == company_id


def test_get_financial_statement(db: Session) -> None:
    company = create_random_company(db)
    company_id = company.id
    period = random_period()
    currency = random_currency()
    url = random_url()
    publish_date = random_date()
    end_date = random_date()
    audited = random_bool()
    non_current_assets = random_integer()
    current_assets = random_integer()
    total_assets = random_integer()
    total_equity = random_integer()
    long_term_liabilities = random_integer()
    current_liabilities = random_integer()
    total_liabilities = random_integer()
    total_equities_and_liabilities = random_integer()
    total_revenues = random_integer()
    gross_profit = random_integer()
    operating_income = random_integer()
    profit_before_tax = random_integer()
    net_profit = random_integer()

    financial_statement_in = FinancialStatementCreate(       
        period=period,
        currency=currency,
        url=url,
        publish_date=publish_date,
        end_date=end_date,
        audited=audited,
        non_current_assets=non_current_assets,
        current_assets=current_assets,
        total_assets=total_assets,
        total_equity=total_equity,
        long_term_liabilities=long_term_liabilities,
        current_liabilities=current_liabilities,
        total_liabilities=total_liabilities,
        total_equities_and_liabilities=total_equities_and_liabilities,
        total_revenues=total_revenues,
        gross_profit=gross_profit,
        operating_income=operating_income,
        profit_before_tax=profit_before_tax,
        net_profit=net_profit,
        company_id=company_id
        )
    
    financial_statement = crud.financial_statement.create(db=db, obj_in = financial_statement_in)
    stored_financial_statement = crud.financial_statement.get(db=db, id=financial_statement.id)
    assert financial_statement.id == stored_financial_statement.id
    assert financial_statement.period == stored_financial_statement.period
    assert financial_statement.currency == stored_financial_statement.currency
    assert financial_statement.url == stored_financial_statement.url
    assert financial_statement.publish_date == stored_financial_statement.publish_date
    assert financial_statement.end_date == stored_financial_statement.end_date
    assert financial_statement.audited == stored_financial_statement.audited
    assert financial_statement.non_current_assets == stored_financial_statement.non_current_assets
    assert financial_statement.current_assets == stored_financial_statement.current_assets
    assert financial_statement.total_assets == stored_financial_statement.total_assets
    assert financial_statement.total_equity == stored_financial_statement.total_equity
    assert financial_statement.long_term_liabilities == stored_financial_statement.long_term_liabilities
    assert financial_statement.current_liabilities == stored_financial_statement.current_liabilities
    assert financial_statement.total_liabilities == stored_financial_statement.total_liabilities
    assert financial_statement.total_equities_and_liabilities == stored_financial_statement.total_equities_and_liabilities
    assert financial_statement.total_revenues == stored_financial_statement.total_revenues
    assert financial_statement.gross_profit == stored_financial_statement.gross_profit
    assert financial_statement.operating_income == stored_financial_statement.operating_income
    assert financial_statement.profit_before_tax == stored_financial_statement.profit_before_tax
    assert financial_statement.net_profit == stored_financial_statement.net_profit
    assert financial_statement.company_id == stored_financial_statement.company_id


def test_update_financial_statement(db: Session) -> None:
    company = create_random_company(db)
    company_id = company.id
    period = random_period()
    currency = random_currency()
    url = random_url()
    publish_date = random_date()
    end_date = random_date()
    audited = random_bool()
    non_current_assets = random_integer()
    current_assets = random_integer()
    total_assets = random_integer()
    total_equity = random_integer()
    long_term_liabilities = random_integer()
    current_liabilities = random_integer()
    total_liabilities = random_integer()
    total_equities_and_liabilities = random_integer()
    total_revenues = random_integer()
    gross_profit = random_integer()
    operating_income = random_integer()
    profit_before_tax = random_integer()
    net_profit = random_integer()
    
    financial_statement_in = FinancialStatementCreate(       
        period=period,
        currency=currency,
        url=url,
        publish_date=publish_date,
        end_date=end_date,
        audited=audited,
        non_current_assets=non_current_assets,
        current_assets=current_assets,
        total_assets=total_assets,
        total_equity=total_equity,
        long_term_liabilities=long_term_liabilities,
        current_liabilities=current_liabilities,
        total_liabilities=total_liabilities,
        total_equities_and_liabilities=total_equities_and_liabilities,
        total_revenues=total_revenues,
        gross_profit=gross_profit,
        operating_income=operating_income,
        profit_before_tax=profit_before_tax,
        net_profit=net_profit,
        company_id=company_id
        )

    financial_statement = crud.financial_statement.create(db=db, obj_in = financial_statement_in)

    period2 = random_period()
    currency2 = random_currency()
    url2 = random_url()
    end_date2 = random_date()
    audited2 = random_bool()
    non_current_assets2 = random_integer()
    
    financial_statement_update = FinancialStatementUpdate(
        period=period2,
        currency=currency2,
        url=url2,
        end_date=end_date2,
        audited=audited2,
        non_current_assets=non_current_assets2
        )
    financial_statement2 = crud.financial_statement.update(db=db, db_obj=financial_statement, obj_in=financial_statement_update)
    assert financial_statement.publish_date.strftime("%Y-%m-%d") == financial_statement2.publish_date.strftime("%Y-%m-%d")
    assert financial_statement.end_date.strftime("%Y-%m-%d") == financial_statement2.end_date.strftime("%Y-%m-%d")
    assert financial_statement.id == financial_statement2.id
    assert financial_statement2.period == period2
    assert financial_statement2.currency == currency2
    assert financial_statement2.url == url2
    assert financial_statement2.audited == audited2
    assert financial_statement2.non_current_assets == non_current_assets2
    assert financial_statement.current_assets == financial_statement2.current_assets
    assert financial_statement.total_assets == financial_statement2.total_assets
    assert financial_statement.total_equity == financial_statement2.total_equity
    assert financial_statement.long_term_liabilities == financial_statement2.long_term_liabilities
    assert financial_statement.current_liabilities == financial_statement2.current_liabilities
    assert financial_statement.total_liabilities == financial_statement2.total_liabilities
    assert financial_statement.total_equities_and_liabilities == financial_statement2.total_equities_and_liabilities
    assert financial_statement.total_revenues == financial_statement2.total_revenues
    assert financial_statement.gross_profit == financial_statement2.gross_profit
    assert financial_statement.operating_income == financial_statement2.operating_income
    assert financial_statement.profit_before_tax == financial_statement2.profit_before_tax
    assert financial_statement.net_profit == financial_statement2.net_profit
    assert financial_statement.company_id == financial_statement2.company_id


def test_delete_financial_statement(db: Session) -> None:
    company = create_random_company(db)
    company_id = company.id
    period = random_period()
    currency = random_currency()
    url = random_url()
    publish_date = random_date()
    end_date = random_date()
    audited = random_bool()
    non_current_assets = random_integer()
    current_assets = random_integer()
    total_assets = random_integer()
    total_equity = random_integer()
    long_term_liabilities = random_integer()
    current_liabilities = random_integer()
    total_liabilities = random_integer()
    total_equities_and_liabilities = random_integer()
    total_revenues = random_integer()
    gross_profit = random_integer()
    operating_income = random_integer()
    profit_before_tax = random_integer()
    net_profit = random_integer()

    financial_statement_in = FinancialStatementCreate(       
        period=period,
        currency=currency,
        url=url,
        publish_date=publish_date,
        end_date=end_date,
        audited=audited,
        non_current_assets=non_current_assets,
        current_assets=current_assets,
        total_assets=total_assets,
        total_equity=total_equity,
        long_term_liabilities=long_term_liabilities,
        current_liabilities=current_liabilities,
        total_liabilities=total_liabilities,
        total_equities_and_liabilities=total_equities_and_liabilities,
        total_revenues=total_revenues,
        gross_profit=gross_profit,
        operating_income=operating_income,
        profit_before_tax=profit_before_tax,
        net_profit=net_profit,
        company_id=company_id
        )
    financial_statement = crud.financial_statement.create(db=db, obj_in=financial_statement_in)
    financial_statement2 = crud.financial_statement.remove(db=db, id=financial_statement.id)
    financial_statement3 = crud.financial_statement.get(db=db, id=financial_statement.id)
    assert financial_statement3 is None
    assert financial_statement2.publish_date.strftime("%Y-%m-%d") == publish_date.strftime("%Y-%m-%d")
    assert financial_statement2.end_date.strftime("%Y-%m-%d") == end_date.strftime("%Y-%m-%d")
    assert financial_statement2.id == financial_statement.id
    assert financial_statement2.period == period
    assert financial_statement2.currency == currency
    assert financial_statement2.url == url
    assert financial_statement2.audited == audited
    assert financial_statement2.non_current_assets == non_current_assets
    assert financial_statement2.current_assets == current_assets
    assert financial_statement2.total_assets == total_assets
    assert financial_statement2.total_equity == total_equity
    assert financial_statement2.long_term_liabilities == long_term_liabilities
    assert financial_statement2.current_liabilities == current_liabilities
    assert financial_statement2.total_liabilities == total_liabilities
    assert financial_statement2.total_equities_and_liabilities == total_equities_and_liabilities
    assert financial_statement2.total_revenues == total_revenues
    assert financial_statement2.gross_profit == gross_profit
    assert financial_statement2.operating_income == operating_income
    assert financial_statement2.profit_before_tax == profit_before_tax
    assert financial_statement2.net_profit == net_profit
    assert financial_statement2.company_id == company_id