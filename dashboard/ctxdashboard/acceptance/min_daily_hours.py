import datetime as dt
from typing import Callable

N_SECS_HOUR = 60 * 60

def simple_min_hours_daily_acceptance_criterion(min_hours: int) -> Callable[[dt.date, int], bool]:
    def accept_day(_day: dt.date, sec: int) -> bool:
        return sec >= min_hours * N_SECS_HOUR

    return accept_day