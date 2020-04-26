import random
import string
from typing import Dict
from datetime import datetime, date, timedelta

from fastapi.testclient import TestClient

from app.core.config import settings
from app.utils import PeriodEnum
from app.utils import CurrencyEnum


def random_period() -> str:
    return random.choice(list(PeriodEnum))


def random_currency() -> str:
    return random.choice(list(CurrencyEnum))


def random_date(min_year=1900, max_year=datetime.now().year) -> date:
    start = date(min_year, 1, 1)
    years = max_year - min_year + 1
    end = start + timedelta(days=365 * years)
    return start + (end - start) * random.random()


def random_bool() -> bool:
    return random.choice([True, False])


def random_integer() -> int:
    return random.randint(-99999999999, 99999999999)


def random_isin() -> str:
    return random_two_letters() + str(random.randint(0, 9999999999))


def random_two_letters() -> str:
    return random.choice(string.ascii_letters) + random.choice(string.ascii_letters) 

def random_lower_string() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=32))


def random_email() -> str:
    return f"{random_lower_string()}@{random_lower_string()}.com"


def random_url() -> str:
    return f"https://www.{random_lower_string()}.com"


def get_superuser_token_headers(client: TestClient) -> Dict[str, str]:
    login_data = {
        "username": settings.FIRST_SUPERUSER,
        "password": settings.FIRST_SUPERUSER_PASSWORD,
    }
    r = client.post(f"{settings.API_V1_STR}/login/access-token", data=login_data)
    tokens = r.json()
    a_token = tokens["access_token"]
    headers = {"Authorization": f"Bearer {a_token}"}
    return headers
