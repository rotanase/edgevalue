from sqlalchemy.orm import Session

from app import crud
from app.schemas.dividend import DividendCreate, DividendUpdate
from app.tests.utils.company import create_random_company
from app.tests.utils.utils import random_date
from app.tests.utils.utils import random_currency
from app.tests.utils.utils import random_dividend_payout


def test_create_dividend(db: Session) -> None:
    company = create_random_company(db)
    company_id = company.id
    currency = random_currency()
    ex_dividend_date = random_date()
    pay_date = random_date()
    dividend_payout = random_dividend_payout()
    
    dividend_in = DividendCreate(
        currency=currency,
        ex_dividend_date=ex_dividend_date,
        pay_date=pay_date,
        dividend_payout=dividend_payout,
        company_id=company_id
    )

    dividend = crud.dividend.create(db=db, obj_in=dividend_in)
    assert dividend.currency == currency
    assert dividend.ex_dividend_date.strftime("%Y-%m-%d") == ex_dividend_date.strftime("%Y-%m-%d")
    assert dividend.pay_date.strftime("%Y-%m-%d") == pay_date.strftime("%Y-%m-%d")
    assert dividend.dividend_payout == dividend_payout
    assert dividend.company_id == company_id


def test_get_dividend(db: Session) -> None:
    company = create_random_company(db)
    company_id = company.id
    currency = random_currency()
    ex_dividend_date = random_date()
    pay_date = random_date()
    dividend_payout = random_dividend_payout()

    dividend_in = DividendCreate(
        currency=currency,
        ex_dividend_date=ex_dividend_date,
        pay_date=pay_date,
        dividend_payout=dividend_payout,
        company_id=company_id
    )
    
    dividend = crud.dividend.create(db=db, obj_in = dividend_in)
    stored_dividend = crud.dividend.get(db=db, id=dividend.id)
    assert dividend.currency == stored_dividend.currency
    assert dividend.ex_dividend_date.strftime("%Y-%m-%d") == stored_dividend.ex_dividend_date.strftime("%Y-%m-%d")
    assert dividend.pay_date.strftime("%Y-%m-%d") == stored_dividend.pay_date.strftime("%Y-%m-%d")
    assert dividend.dividend_payout == stored_dividend.dividend_payout
    assert dividend.company_id == stored_dividend.company_id
    

def test_update_dividend(db: Session) -> None:
    company = create_random_company(db)
    company_id = company.id
    currency = random_currency()
    ex_dividend_date = random_date()
    pay_date = random_date()
    dividend_payout = random_dividend_payout()

    dividend_in = DividendCreate(
        currency=currency,
        ex_dividend_date=ex_dividend_date,
        pay_date=pay_date,
        dividend_payout=dividend_payout,
        company_id=company_id
    )

    dividend = crud.dividend.create(db=db, obj_in = dividend_in)

    ex_dividend_date2 = random_date()
    pay_date2 = random_date()
    dividend_payout2 = random_dividend_payout()
    
    dividend_update = DividendUpdate(
        ex_dividend_date=ex_dividend_date2,
        pay_date=pay_date2,
        dividend_payout=dividend_payout2
    )
    
    dividend2 = crud.dividend.update(db=db, db_obj=dividend, obj_in=dividend_update)
    assert dividend.currency == dividend2.currency
    assert dividend2.ex_dividend_date.strftime("%Y-%m-%d") == ex_dividend_date2.strftime("%Y-%m-%d")
    assert dividend2.pay_date.strftime("%Y-%m-%d") == pay_date2.strftime("%Y-%m-%d")
    assert dividend2.dividend_payout == dividend_payout2
    assert dividend.company_id == dividend2.company_id


def test_delete_dividend(db: Session) -> None:
    company = create_random_company(db)
    company_id = company.id
    currency = random_currency()
    ex_dividend_date = random_date()
    pay_date = random_date()
    dividend_payout = random_dividend_payout()

    dividend_in = DividendCreate(
        currency=currency,
        ex_dividend_date=ex_dividend_date,
        pay_date=pay_date,
        dividend_payout=dividend_payout,
        company_id=company_id
    )
    dividend = crud.dividend.create(db=db, obj_in=dividend_in)
    dividend2 = crud.dividend.remove(db=db, id=dividend.id)
    dividend3 = crud.dividend.get(db=db, id=dividend.id)
    assert dividend3 is None
    assert dividend2.id == dividend.id
    assert dividend2.currency == currency
    assert dividend2.ex_dividend_date.strftime("%Y-%m-%d") == ex_dividend_date.strftime("%Y-%m-%d")
    assert dividend2.pay_date.strftime("%Y-%m-%d") == pay_date.strftime("%Y-%m-%d")
    assert dividend2.dividend_payout == dividend_payout
    assert dividend2.company_id == company_id
