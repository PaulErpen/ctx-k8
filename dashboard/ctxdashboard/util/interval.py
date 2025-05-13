import datetime as dt
from typing import Generator

class Interval:
    @staticmethod
    def gen_days_in_interval(start: dt.date, end: dt.date) -> Generator[dt.date, None, None]:
        for curr_date in (start + dt.timedelta(n) for n in range((end - start).days)):
            yield curr_date