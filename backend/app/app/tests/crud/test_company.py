from sqlalchemy.orm import Session


from app import crud
from app.schemas.company import CompanyCreate, CompanyUpdate
from app.tests.utils.utils import random_lower_string
from app.tests.utils.utils import random_date
from app.tests.utils.utils import random_url
from app.tests.utils.utils import random_isin


def test_create_company(db: Session) -> None:
    name = random_lower_string()
    isin = random_isin()
    url = random_url()
    ticker = random_lower_string()
    ipo_date = random_date()
    stock_exchange = random_lower_string()
    
    company_in = CompanyCreate(       
        name=name,
        isin=isin,
        url=url,
        ticker=ticker,
        ipo_date=ipo_date,
        stock_exchange=stock_exchange
    )
    company = crud.company.create(db=db, obj_in=company_in)
    assert company.name == name
    assert company.isin == isin
    assert company.url == url
    assert company.ticker == ticker
    assert company.ipo_date.strftime("%Y-%m-%d") == ipo_date.strftime("%Y-%m-%d")
    assert company.stock_exchange == stock_exchange


def test_get_company(db: Session) -> None:
    name = random_lower_string()
    isin = random_isin()
    url = random_url()
    ticker = random_lower_string()
    ipo_date = random_date()
    stock_exchange = random_lower_string()

    company_in = CompanyCreate(       
        name=name,
        isin=isin,
        url=url,
        ticker=ticker,
        ipo_date=ipo_date,
        stock_exchange=stock_exchange
    )
    company = crud.company.create(db=db, obj_in = company_in)
    stored_company = crud.company.get(db=db, id=company.id)
    assert company.id == stored_company.id
    assert company.name == stored_company.name
    assert company.isin == stored_company.isin
    assert company.url == stored_company.url
    assert company.ticker == stored_company.ticker
    assert company.ipo_date.strftime("%Y-%m-%d") == stored_company.ipo_date.strftime("%Y-%m-%d")
    assert company.stock_exchange == stored_company.stock_exchange


def test_update_company(db: Session) -> None:
    name = random_lower_string()
    isin = random_isin()
    url = random_url()
    ticker = random_lower_string()
    ipo_date = random_date()
    stock_exchange = random_lower_string()
    
    company_in = CompanyCreate(       
        name=name,
        isin=isin,
        url=url,
        ticker=ticker,
        ipo_date=ipo_date,
        stock_exchange=stock_exchange
    )
    company = crud.company.create(db=db, obj_in = company_in)
    name2 = random_lower_string()
    isin2 = random_isin()
    url2 = random_url()
    ipo_date2 = random_date()
   
    company_update = CompanyUpdate(
        name=name2,
        isin=isin2,
        url=url2,
        ipo_date=ipo_date2,
        )
    company2 = crud.company.update(db=db, db_obj=company, obj_in=company_update)
    assert company.id == company2.id
    assert company2.name == name2
    assert company2.isin == isin2
    assert company2.url == url2
    assert company.ticker == company2.ticker
    assert company2.ipo_date.strftime("%Y-%m-%d") == ipo_date2.strftime("%Y-%m-%d")
    assert company.stock_exchange == company2.stock_exchange


def test_delete_company(db: Session) -> None:
    name = random_lower_string()
    isin = random_isin()
    url = random_url()
    ticker = random_lower_string()
    ipo_date = random_date()
    stock_exchange = random_lower_string()

    company_in = CompanyCreate(       
        name=name,
        isin=isin,
        url=url,
        ticker=ticker,
        ipo_date=ipo_date,
        stock_exchange=stock_exchange
    )
    company = crud.company.create(db=db, obj_in=company_in)
    company2 = crud.company.remove(db=db, id=company.id)
    company3 = crud.company.get(db=db, id=company.id)
    assert company3 is None
    assert company2.id == company.id
    assert company2.name == name
    assert company2.isin == isin
    assert company2.url == url
    assert company2.ticker == ticker
    assert company2.ipo_date.strftime("%Y-%m-%d") == ipo_date.strftime("%Y-%m-%d")
    assert company2.stock_exchange == stock_exchange
    