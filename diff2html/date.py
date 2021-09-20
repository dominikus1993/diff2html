
from typing import Union
from datetime import datetime

def get_first_day_of_month(date: datetime) -> str:
    return str(date.replace(day=1))

def get_first_day_of_month_when_none(date: Union[str, None]) -> str:
    return get_first_day_of_month(datetime.today()) if date is None else date

def get_last_day_of_month(date: datetime) -> str:
    return str(date.replace(day=1))

def get_last_day_of_month_when_none(date: Union[str, None]) -> str:
    return get_first_day_of_month(datetime.today()) if date is None else date