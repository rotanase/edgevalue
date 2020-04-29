from sqlalchemy.orm import Session

from app import crud, models
from app.schemas.dividend import DividendCreate
from app.tests.utils.company import create_random_company
from app.tests.utils.utils import random_date
from app.tests.utils.utils import random_currency
from app.tests.utils.utils import random_dividend_payout


def create_random_dividend(db: Session) -> models.Dividend:
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
    return crud.dividend.create(db=db, obj_in=dividend_in)
