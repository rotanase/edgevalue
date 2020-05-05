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
from app.tests.utils.utils import random_float


def test_create_financial_statement(db: Session) -> None:
    company = create_random_company(db)
    company_id = company.id
    period = random_period()
    end_date = random_date()
    publish_date = random_date()
    url = random_url()
    audited = random_bool()
    currency = random_currency()
    non_current_assets = random_integer()
    cash_and_equivalents = random_integer()
    current_assets = random_integer()
    total_assets = random_integer()
    short_term_debt = random_integer()
    current_liabilities = random_integer()
    long_term_debt = random_integer()
    long_term_liabilities = random_integer()
    total_debt = random_integer()
    total_liabilities = random_integer()
    total_equity = random_integer()
    total_equities_and_liabilities = random_integer()
    total_revenues = random_integer()
    cost_of_revenue = random_integer()
    costs_of_goods_sold = random_integer()
    gross_profit = random_integer()
    ebitda = random_integer()
    ebit = random_integer()
    operating_income = random_integer()
    interest_expense = random_integer()
    profit_before_tax = random_integer()
    tax_expense = random_integer()
    depreciation = random_integer()
    amortization = random_integer()
    net_income = random_integer()
    earnings_per_share = random_float()
    
    financial_statement_in = FinancialStatementCreate(       
        period=period,
        end_date=end_date,
        publish_date=publish_date,
        url=url,
        audited=audited,
        currency=currency,
        non_current_assets=non_current_assets,
        cash_and_equivalents=cash_and_equivalents,
        current_assets=current_assets,
        total_assets=total_assets,
        short_term_debt=short_term_debt,
        current_liabilities=current_liabilities,
        long_term_debt=long_term_debt,
        long_term_liabilities=long_term_liabilities,
        total_debt=total_debt,
        total_liabilities=total_liabilities,
        total_equity=total_equity,
        total_equities_and_liabilities=total_equities_and_liabilities,
        total_revenues=total_revenues,
        cost_of_revenue=cost_of_revenue,
        costs_of_goods_sold=costs_of_goods_sold,
        gross_profit=gross_profit,
        ebitda=ebitda,
        ebit=ebit,
        operating_income=operating_income,
        interest_expense=interest_expense,
        profit_before_tax=profit_before_tax,
        tax_expense=tax_expense,
        depreciation=depreciation,
        amortization=amortization,
        net_income=net_income,
        earnings_per_share=earnings_per_share,
        company_id=company_id
        )
    financial_statement = crud.financial_statement.create(db=db, obj_in=financial_statement_in)
    assert financial_statement.period == period
    assert financial_statement.end_date.strftime("%Y-%m-%d") == end_date.strftime("%Y-%m-%d")
    assert financial_statement.publish_date.strftime("%Y-%m-%d") == publish_date.strftime("%Y-%m-%d")
    assert financial_statement.url == url
    assert financial_statement.audited == audited
    assert financial_statement.currency == currency
    assert financial_statement.non_current_assets == non_current_assets
    assert financial_statement.cash_and_equivalents == cash_and_equivalents
    assert financial_statement.current_assets == current_assets
    assert financial_statement.total_assets == total_assets
    assert financial_statement.short_term_debt == short_term_debt
    assert financial_statement.current_liabilities == current_liabilities
    assert financial_statement.long_term_debt == long_term_debt
    assert financial_statement.long_term_liabilities == long_term_liabilities
    assert financial_statement.total_debt == total_debt
    assert financial_statement.total_liabilities == total_liabilities
    assert financial_statement.total_equity == total_equity
    assert financial_statement.total_equities_and_liabilities == total_equities_and_liabilities
    assert financial_statement.total_revenues == total_revenues
    assert financial_statement.cost_of_revenue == cost_of_revenue
    assert financial_statement.costs_of_goods_sold == costs_of_goods_sold
    assert financial_statement.gross_profit == gross_profit
    assert financial_statement.ebitda == ebitda
    assert financial_statement.ebit == ebit
    assert financial_statement.operating_income == operating_income
    assert financial_statement.interest_expense == interest_expense
    assert financial_statement.profit_before_tax == profit_before_tax
    assert financial_statement.tax_expense == tax_expense
    assert financial_statement.depreciation == depreciation
    assert financial_statement.amortization == amortization
    assert financial_statement.net_income == net_income
    assert financial_statement.earnings_per_share == earnings_per_share
    assert financial_statement.company_id == company_id


def test_get_financial_statement(db: Session) -> None:
    company = create_random_company(db)
    company_id = company.id
    period = random_period()
    end_date = random_date()
    publish_date = random_date()
    url = random_url()
    audited = random_bool()
    currency = random_currency()
    non_current_assets = random_integer()
    cash_and_equivalents = random_integer()
    current_assets = random_integer()
    total_assets = random_integer()
    short_term_debt = random_integer()
    current_liabilities = random_integer()
    long_term_debt = random_integer()
    long_term_liabilities = random_integer()
    total_debt = random_integer()
    total_liabilities = random_integer()
    total_equity = random_integer()
    total_equities_and_liabilities = random_integer()
    total_revenues = random_integer()
    cost_of_revenue = random_integer()
    costs_of_goods_sold = random_integer()
    gross_profit = random_integer()
    ebitda = random_integer()
    ebit = random_integer()
    operating_income = random_integer()
    interest_expense = random_integer()
    profit_before_tax = random_integer()
    tax_expense = random_integer()
    depreciation = random_integer()
    amortization = random_integer()
    net_income = random_integer()
    earnings_per_share = random_float()

    financial_statement_in = FinancialStatementCreate(       
        period=period,
        end_date=end_date,
        publish_date=publish_date,
        url=url,
        audited=audited,
        currency=currency,
        non_current_assets=non_current_assets,
        cash_and_equivalents=cash_and_equivalents,
        current_assets=current_assets,
        total_assets=total_assets,
        short_term_debt=short_term_debt,
        current_liabilities=current_liabilities,
        long_term_debt=long_term_debt,
        long_term_liabilities=long_term_liabilities,
        total_debt=total_debt,
        total_liabilities=total_liabilities,
        total_equity=total_equity,
        total_equities_and_liabilities=total_equities_and_liabilities,
        total_revenues=total_revenues,
        cost_of_revenue=cost_of_revenue,
        costs_of_goods_sold=costs_of_goods_sold,
        gross_profit=gross_profit,
        ebitda=ebitda,
        ebit=ebit,
        operating_income=operating_income,
        interest_expense=interest_expense,
        profit_before_tax=profit_before_tax,
        tax_expense=tax_expense,
        depreciation=depreciation,
        amortization=amortization,
        net_income=net_income,
        earnings_per_share=earnings_per_share,
        company_id=company_id
        )
    financial_statement = crud.financial_statement.create(db=db, obj_in = financial_statement_in)
    stored_financial_statement = crud.financial_statement.get(db=db, id=financial_statement.id)
    assert financial_statement.id == stored_financial_statement.id
    assert financial_statement.period == stored_financial_statement.period
    assert financial_statement.end_date == stored_financial_statement.end_date
    assert financial_statement.publish_date == stored_financial_statement.publish_date
    assert financial_statement.url == stored_financial_statement.url
    assert financial_statement.audited == stored_financial_statement.audited
    assert financial_statement.currency == stored_financial_statement.currency
    assert financial_statement.non_current_assets == stored_financial_statement.non_current_assets
    assert financial_statement.cash_and_equivalents == stored_financial_statement.cash_and_equivalents
    assert financial_statement.current_assets == stored_financial_statement.current_assets
    assert financial_statement.total_assets == stored_financial_statement.total_assets
    assert financial_statement.short_term_debt == stored_financial_statement.short_term_debt
    assert financial_statement.current_liabilities == stored_financial_statement.current_liabilities
    assert financial_statement.long_term_debt == stored_financial_statement.long_term_debt
    assert financial_statement.long_term_liabilities == stored_financial_statement.long_term_liabilities
    assert financial_statement.total_debt == stored_financial_statement.total_debt
    assert financial_statement.total_liabilities == stored_financial_statement.total_liabilities
    assert financial_statement.total_equity == stored_financial_statement.total_equity
    assert financial_statement.total_equities_and_liabilities == stored_financial_statement.total_equities_and_liabilities
    assert financial_statement.total_revenues == stored_financial_statement.total_revenues
    assert financial_statement.cost_of_revenue == stored_financial_statement.cost_of_revenue
    assert financial_statement.costs_of_goods_sold == stored_financial_statement.costs_of_goods_sold
    assert financial_statement.gross_profit == stored_financial_statement.gross_profit
    assert financial_statement.ebitda == stored_financial_statement.ebitda
    assert financial_statement.ebit == stored_financial_statement.ebit
    assert financial_statement.operating_income == stored_financial_statement.operating_income
    assert financial_statement.interest_expense == stored_financial_statement.interest_expense
    assert financial_statement.profit_before_tax == stored_financial_statement.profit_before_tax
    assert financial_statement.tax_expense == stored_financial_statement.tax_expense
    assert financial_statement.depreciation == stored_financial_statement.depreciation
    assert financial_statement.amortization == stored_financial_statement.amortization
    assert financial_statement.net_income == stored_financial_statement.net_income
    assert financial_statement.earnings_per_share == stored_financial_statement.earnings_per_share
    assert financial_statement.company_id == stored_financial_statement.company_id


def test_update_financial_statement(db: Session) -> None:
    company = create_random_company(db)
    company_id = company.id
    period = random_period()
    end_date = random_date()
    publish_date = random_date()
    url = random_url()
    audited = random_bool()
    currency = random_currency()
    non_current_assets = random_integer()
    cash_and_equivalents = random_integer()
    current_assets = random_integer()
    total_assets = random_integer()
    short_term_debt = random_integer()
    current_liabilities = random_integer()
    long_term_debt = random_integer()
    long_term_liabilities = random_integer()
    total_debt = random_integer()
    total_liabilities = random_integer()
    total_equity = random_integer()
    total_equities_and_liabilities = random_integer()
    total_revenues = random_integer()
    cost_of_revenue = random_integer()
    costs_of_goods_sold = random_integer()
    gross_profit = random_integer()
    ebitda = random_integer()
    ebit = random_integer()
    operating_income = random_integer()
    interest_expense = random_integer()
    profit_before_tax = random_integer()
    tax_expense = random_integer()
    depreciation = random_integer()
    amortization = random_integer()
    net_income = random_integer()
    earnings_per_share = random_float()
    
    financial_statement_in = FinancialStatementCreate(       
        period=period,
        end_date=end_date,
        publish_date=publish_date,
        url=url,
        audited=audited,
        currency=currency,
        non_current_assets=non_current_assets,
        cash_and_equivalents=cash_and_equivalents,
        current_assets=current_assets,
        total_assets=total_assets,
        short_term_debt=short_term_debt,
        current_liabilities=current_liabilities,
        long_term_debt=long_term_debt,
        long_term_liabilities=long_term_liabilities,
        total_debt=total_debt,
        total_liabilities=total_liabilities,
        total_equity=total_equity,
        total_equities_and_liabilities=total_equities_and_liabilities,
        total_revenues=total_revenues,
        cost_of_revenue=cost_of_revenue,
        costs_of_goods_sold=costs_of_goods_sold,
        gross_profit=gross_profit,
        ebitda=ebitda,
        ebit=ebit,
        operating_income=operating_income,
        interest_expense=interest_expense,
        profit_before_tax=profit_before_tax,
        tax_expense=tax_expense,
        depreciation=depreciation,
        amortization=amortization,
        net_income=net_income,
        earnings_per_share=earnings_per_share,
        company_id=company_id
        )
    financial_statement = crud.financial_statement.create(db=db, obj_in = financial_statement_in)

    period2 = random_period()
    end_date2 = random_date()
    url2 = random_url()
    audited2 = random_bool()
    currency2 = random_currency()
    non_current_assets2 = random_integer()
    
    financial_statement_update = FinancialStatementUpdate(
        period=period2,
        end_date=end_date2,
        url=url2,
        audited=audited2,
        currency=currency2,
        non_current_assets=non_current_assets2
        )
    financial_statement2 = crud.financial_statement.update(db=db, db_obj=financial_statement, obj_in=financial_statement_update)
    assert financial_statement.id == financial_statement2.id
    assert financial_statement2.period == period2
    assert financial_statement.end_date.strftime("%Y-%m-%d") == financial_statement2.end_date.strftime("%Y-%m-%d")
    assert financial_statement.publish_date.strftime("%Y-%m-%d") == financial_statement2.publish_date.strftime("%Y-%m-%d")
    assert financial_statement2.url == url2
    assert financial_statement2.audited == audited2
    assert financial_statement2.currency == currency2
    assert financial_statement2.non_current_assets == non_current_assets2
    assert financial_statement.cash_and_equivalents == financial_statement2.cash_and_equivalents
    assert financial_statement.current_assets == financial_statement2.current_assets
    assert financial_statement.total_assets == financial_statement2.total_assets
    assert financial_statement.short_term_debt == financial_statement2.short_term_debt
    assert financial_statement.current_liabilities == financial_statement2.current_liabilities
    assert financial_statement.long_term_debt == financial_statement2.long_term_debt
    assert financial_statement.long_term_liabilities == financial_statement2.long_term_liabilities
    assert financial_statement.total_debt == financial_statement2.total_debt
    assert financial_statement.total_liabilities == financial_statement2.total_liabilities
    assert financial_statement.total_equity == financial_statement2.total_equity
    assert financial_statement.total_equities_and_liabilities == financial_statement2.total_equities_and_liabilities
    assert financial_statement.total_revenues == financial_statement2.total_revenues
    assert financial_statement.cost_of_revenue == financial_statement2.cost_of_revenue
    assert financial_statement.costs_of_goods_sold == financial_statement2.costs_of_goods_sold
    assert financial_statement.gross_profit == financial_statement2.gross_profit
    assert financial_statement.ebitda == financial_statement2.ebitda
    assert financial_statement.ebit == financial_statement2.ebit
    assert financial_statement.operating_income == financial_statement2.operating_income
    assert financial_statement.interest_expense == financial_statement2.interest_expense
    assert financial_statement.profit_before_tax == financial_statement2.profit_before_tax
    assert financial_statement.tax_expense == financial_statement2.tax_expense
    assert financial_statement.depreciation == financial_statement2.depreciation
    assert financial_statement.amortization == financial_statement2.amortization
    assert financial_statement.net_income == financial_statement2.net_income
    assert financial_statement.earnings_per_share == financial_statement2.earnings_per_share
    assert financial_statement.company_id == financial_statement2.company_id


def test_delete_financial_statement(db: Session) -> None:
    company = create_random_company(db)
    company_id = company.id
    period = random_period()
    end_date = random_date()
    publish_date = random_date()
    url = random_url()
    audited = random_bool()
    currency = random_currency()
    non_current_assets = random_integer()
    cash_and_equivalents = random_integer()
    current_assets = random_integer()
    total_assets = random_integer()
    short_term_debt = random_integer()
    current_liabilities = random_integer()
    long_term_debt = random_integer()
    long_term_liabilities = random_integer()
    total_debt = random_integer()
    total_liabilities = random_integer()
    total_equity = random_integer()
    total_equities_and_liabilities = random_integer()
    total_revenues = random_integer()
    cost_of_revenue = random_integer()
    costs_of_goods_sold = random_integer()
    gross_profit = random_integer()
    ebitda = random_integer()
    ebit = random_integer()
    operating_income = random_integer()
    interest_expense = random_integer()
    profit_before_tax = random_integer()
    tax_expense = random_integer()
    depreciation = random_integer()
    amortization = random_integer()
    net_income = random_integer()
    earnings_per_share = random_float()

    financial_statement_in = FinancialStatementCreate(       
        period=period,
        end_date=end_date,
        publish_date=publish_date,
        url=url,
        audited=audited,
        currency=currency,
        non_current_assets=non_current_assets,
        cash_and_equivalents=cash_and_equivalents,
        current_assets=current_assets,
        total_assets=total_assets,
        short_term_debt=short_term_debt,
        current_liabilities=current_liabilities,
        long_term_debt=long_term_debt,
        long_term_liabilities=long_term_liabilities,
        total_debt=total_debt,
        total_liabilities=total_liabilities,
        total_equity=total_equity,
        total_equities_and_liabilities=total_equities_and_liabilities,
        total_revenues=total_revenues,
        cost_of_revenue=cost_of_revenue,
        costs_of_goods_sold=costs_of_goods_sold,
        gross_profit=gross_profit,
        ebitda=ebitda,
        ebit=ebit,
        operating_income=operating_income,
        interest_expense=interest_expense,
        profit_before_tax=profit_before_tax,
        tax_expense=tax_expense,
        depreciation=depreciation,
        amortization=amortization,
        net_income=net_income,
        earnings_per_share=earnings_per_share,
        company_id=company_id
        )
    financial_statement = crud.financial_statement.create(db=db, obj_in=financial_statement_in)
    financial_statement2 = crud.financial_statement.remove(db=db, id=financial_statement.id)
    financial_statement3 = crud.financial_statement.get(db=db, id=financial_statement.id)
    assert financial_statement3 is None
    assert financial_statement2.id == financial_statement.id
    assert financial_statement2.period == period
    assert financial_statement2.end_date.strftime("%Y-%m-%d") == end_date.strftime("%Y-%m-%d")
    assert financial_statement2.publish_date.strftime("%Y-%m-%d") == publish_date.strftime("%Y-%m-%d")
    assert financial_statement2.url == url
    assert financial_statement2.audited == audited
    assert financial_statement2.currency == currency
    assert financial_statement2.non_current_assets == non_current_assets
    assert financial_statement2.cash_and_equivalents == cash_and_equivalents
    assert financial_statement2.current_assets == current_assets
    assert financial_statement2.total_assets == total_assets
    assert financial_statement2.short_term_debt == short_term_debt
    assert financial_statement2.current_liabilities == current_liabilities
    assert financial_statement2.long_term_debt == long_term_debt
    assert financial_statement2.long_term_liabilities == long_term_liabilities
    assert financial_statement2.total_debt == total_debt
    assert financial_statement2.total_liabilities == total_liabilities
    assert financial_statement2.total_equity == total_equity
    assert financial_statement2.total_equities_and_liabilities == total_equities_and_liabilities
    assert financial_statement2.total_revenues == total_revenues
    assert financial_statement2.cost_of_revenue == cost_of_revenue
    assert financial_statement2.costs_of_goods_sold == costs_of_goods_sold
    assert financial_statement2.gross_profit == gross_profit
    assert financial_statement2.ebitda == ebitda
    assert financial_statement2.ebit == ebit
    assert financial_statement2.operating_income == operating_income
    assert financial_statement2.interest_expense == interest_expense
    assert financial_statement2.profit_before_tax == profit_before_tax
    assert financial_statement2.tax_expense == tax_expense
    assert financial_statement2.depreciation == depreciation
    assert financial_statement2.amortization == amortization
    assert financial_statement2.net_income == net_income
    assert financial_statement2.earnings_per_share == earnings_per_share
    assert financial_statement2.company_id == company_id
