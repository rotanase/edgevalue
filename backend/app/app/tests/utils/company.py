from sqlalchemy.orm import Session

from app import crud, models
from app.schemas.company import CompanyCreate
from app.tests.utils.utils import random_lower_string
from app.tests.utils.utils import random_date
from app.tests.utils.utils import random_url
from app.tests.utils.utils import random_isin
from app.tests.utils.utils import random_number_of_shares


def create_random_company(db: Session) -> models.Company:
    name = random_lower_string()
    isin = random_isin()
    number_of_shares = random_number_of_shares()
    url = random_url()
    ticker = random_lower_string()
    ipo_date = random_date()
    stock_exchange = random_lower_string()

    company_in = CompanyCreate(       
        name=name,
        isin=isin,
        number_of_shares=number_of_shares,
        url=url,
        ticker=ticker,
        ipo_date=ipo_date,
        stock_exchange=stock_exchange,
        id=id)

    return crud.company.create(db=db, obj_in=company_in)
