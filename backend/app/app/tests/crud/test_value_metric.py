from sqlalchemy.orm import Session

from app import crud
from app.schemas.value_metric import ValueMetricCreate, ValueMetricUpdate
from app.tests.utils.company import create_random_company
from app.tests.utils.utils import random_period
from app.tests.utils.utils import random_date
from app.tests.utils.utils import random_currency
from app.tests.utils.utils import random_integer
from app.tests.utils.utils import random_float


def test_create_value_metric(db: Session) -> None:
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
    value_metric = crud.value_metric.create(db=db, obj_in=value_metric_in)
    assert value_metric.period == period
    assert value_metric.end_date.strftime("%Y-%m-%d") == end_date.strftime("%Y-%m-%d")
    assert value_metric.currency == currency
    assert value_metric.book_value == book_value
    assert value_metric.tangible_book_value == tangible_book_value
    assert value_metric.tangible_book_value_per_share == tangible_book_value_per_share
    assert value_metric.debt_to_equity == debt_to_equity
    assert value_metric.equity_ratio == equity_ratio
    assert value_metric.debt_ratio == debt_ratio
    assert value_metric.cash_ratio == cash_ratio
    assert value_metric.gross_profit_margin == gross_profit_margin
    assert value_metric.net_profit_margin == net_profit_margin
    assert value_metric.ebit_margin == ebit_margin
    assert value_metric.operating_margin == operating_margin
    assert value_metric.ebitda_margin == ebitda_margin
    assert value_metric.cash_return_on_capital_invested == cash_return_on_capital_invested 
    assert value_metric.debt_to_ebitda == debt_to_ebitda
    assert value_metric.return_on_equity == return_on_equity
    assert value_metric.return_on_assets == return_on_assets
    assert value_metric.current_ratio == current_ratio
    assert value_metric.working_capital == working_capital
    assert value_metric.company_id == company_id


def test_get_value_metric(db: Session) -> None:
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
    value_metric = crud.value_metric.create(db=db, obj_in = value_metric_in)
    stored_value_metric = crud.value_metric.get(db=db, id=value_metric.id)

    assert value_metric.id == stored_value_metric.id
    assert value_metric.period == stored_value_metric.period
    assert value_metric.end_date.strftime("%Y-%m-%d") == stored_value_metric.end_date.strftime("%Y-%m-%d")
    assert value_metric.currency == stored_value_metric.currency
    assert value_metric.book_value == stored_value_metric.book_value
    assert value_metric.tangible_book_value == stored_value_metric.tangible_book_value
    assert value_metric.tangible_book_value_per_share == stored_value_metric.tangible_book_value_per_share
    assert value_metric.debt_to_equity == stored_value_metric.debt_to_equity
    assert value_metric.equity_ratio == stored_value_metric.equity_ratio
    assert value_metric.debt_ratio == stored_value_metric.debt_ratio
    assert value_metric.cash_ratio == stored_value_metric.cash_ratio
    assert value_metric.gross_profit_margin == stored_value_metric.gross_profit_margin
    assert value_metric.net_profit_margin == stored_value_metric.net_profit_margin
    assert value_metric.ebit_margin == stored_value_metric.ebit_margin
    assert value_metric.operating_margin == stored_value_metric.operating_margin
    assert value_metric.ebitda_margin == stored_value_metric.ebitda_margin
    assert value_metric.cash_return_on_capital_invested == stored_value_metric.cash_return_on_capital_invested 
    assert value_metric.debt_to_ebitda == stored_value_metric.debt_to_ebitda
    assert value_metric.return_on_equity == stored_value_metric.return_on_equity
    assert value_metric.return_on_assets == stored_value_metric.return_on_assets
    assert value_metric.current_ratio == stored_value_metric.current_ratio
    assert value_metric.working_capital == stored_value_metric.working_capital
    assert value_metric.company_id == stored_value_metric.company_id


def test_update_value_metric(db: Session) -> None:
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
    value_metric = crud.value_metric.create(db=db, obj_in = value_metric_in)

    period2 = random_period()
    book_value2 = random_float()
    ebitda_margin2 = random_float()

    value_metric_update = ValueMetricUpdate(
        period=period2,
        book_value=book_value2,
        ebitda_margin=ebitda_margin2
        )
    value_metric2 = crud.value_metric.update(db=db, db_obj=value_metric, obj_in=value_metric_update)
    assert value_metric.id == value_metric2.id
    assert value_metric2.period == period2
    assert value_metric.end_date.strftime("%Y-%m-%d") == value_metric2.end_date.strftime("%Y-%m-%d")
    assert value_metric.currency == value_metric2.currency
    assert value_metric2.book_value == book_value2
    assert value_metric.tangible_book_value == value_metric2.tangible_book_value
    assert value_metric.tangible_book_value_per_share == value_metric2.tangible_book_value_per_share
    assert value_metric.debt_to_equity == value_metric2.debt_to_equity
    assert value_metric.equity_ratio == value_metric2.equity_ratio
    assert value_metric.debt_ratio == value_metric2.debt_ratio
    assert value_metric.cash_ratio == value_metric2.cash_ratio
    assert value_metric.gross_profit_margin == value_metric2.gross_profit_margin
    assert value_metric.net_profit_margin == value_metric2.net_profit_margin
    assert value_metric.ebit_margin == value_metric2.ebit_margin
    assert value_metric.operating_margin == value_metric2.operating_margin
    assert value_metric2.ebitda_margin == ebitda_margin2
    assert value_metric.cash_return_on_capital_invested == value_metric2.cash_return_on_capital_invested 
    assert value_metric.debt_to_ebitda == value_metric2.debt_to_ebitda
    assert value_metric.return_on_equity == value_metric2.return_on_equity
    assert value_metric.return_on_assets == value_metric2.return_on_assets
    assert value_metric.current_ratio == value_metric2.current_ratio
    assert value_metric.working_capital == value_metric2.working_capital


def test_delete_value_metric(db: Session) -> None:
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
    value_metric = crud.value_metric.create(db=db, obj_in=value_metric_in)
    value_metric2 = crud.value_metric.remove(db=db, id=value_metric.id)
    value_metric3 = crud.value_metric.get(db=db, id=value_metric.id)
    assert value_metric3 is None
    assert value_metric2.id == value_metric.id
    assert value_metric2.period == period
    assert value_metric2.end_date.strftime("%Y-%m-%d") == end_date.strftime("%Y-%m-%d")
    assert value_metric2.currency == currency
    assert value_metric2.book_value == book_value
    assert value_metric2.tangible_book_value == tangible_book_value
    assert value_metric2.tangible_book_value_per_share == tangible_book_value_per_share
    assert value_metric2.debt_to_equity == debt_to_equity
    assert value_metric2.equity_ratio == equity_ratio
    assert value_metric2.debt_ratio == debt_ratio
    assert value_metric2.cash_ratio == cash_ratio
    assert value_metric2.gross_profit_margin == gross_profit_margin
    assert value_metric2.net_profit_margin == net_profit_margin
    assert value_metric2.ebit_margin == ebit_margin
    assert value_metric2.operating_margin == operating_margin
    assert value_metric2.ebitda_margin == ebitda_margin
    assert value_metric2.cash_return_on_capital_invested == cash_return_on_capital_invested 
    assert value_metric2.debt_to_ebitda == debt_to_ebitda
    assert value_metric2.return_on_equity == return_on_equity
    assert value_metric2.return_on_assets == return_on_assets
    assert value_metric2.current_ratio == current_ratio
    assert value_metric2.working_capital == working_capital
    assert value_metric2.company_id == company_id
