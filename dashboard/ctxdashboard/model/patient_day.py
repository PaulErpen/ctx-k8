import datetime as dt
from typing import Callable


class CTxPatientDay:
    ZERO_TIME_STRING = "00:00:00"

    def __init__(
        self,
        day_date: dt.date,
        duration_s: int,
        accepted: bool,
        formatted_duration: str,
    ) -> None:
        self.day_date = day_date
        self.duration_s = duration_s
        self.accepted = accepted
        self.formatted_duration = formatted_duration

    @classmethod
    def create_patient_day(
        cls,
        day_date: dt.date,
        duration_s: int,
        daily_criterion: Callable[[dt.date, int], bool],
    ) -> "CTxPatientDay":
        return cls(
            day_date=day_date,
            duration_s=duration_s,
            accepted=daily_criterion(day_date, duration_s),
            formatted_duration=cls.format_daily_seconds(duration_s),
        )

    @staticmethod
    def format_daily_seconds(duration_s: int) -> str:
        hours = duration_s // 3600
        minutes = duration_s // 60 - hours * 60
        seconds = duration_s - hours * 60 * 60 - minutes * 60
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, CTxPatientDay):
            return (
                self.day_date == __o.day_date
                and self.duration_s == __o.duration_s
                and self.accepted == __o.accepted
                and self.formatted_duration == __o.formatted_duration
            )
        else:
            return False
