from typing import Union
import datetime
import calendar

def get_first_day_of_month(date: datetime) -> str:
    return str(date.replace(day=1).date())

def get_first_day_of_month_when_none(date: Union[str, None]) -> str:
    return get_first_day_of_month(datetime.date.today()) if date is None else date

def get_last_day_of_month(d: datetime) -> str:
    date = datetime.date(d.year, d.month, calendar.monthrange(d.year, d.month)[-1])
    return str(date)

def get_last_day_of_month_when_none(date: Union[str, None]) -> str:
    return get_first_day_of_month(datetime.date.today()) if date is None else date