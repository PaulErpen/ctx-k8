from typing import Callable, List
import pandas as pd
from ctxdashboard.model.patient_day import CTxPatientDay
import datetime as dt
from ctxdashboard.model.dailies_columns import DailiesColumns as dc
from ctxdashboard.util.interval import Interval


class CTxPatient:
    def __init__(
        self, patient_id: str, patient_days: List[CTxPatientDay], accepted: bool
    ) -> None:
        self.patient_id = patient_id
        self.patient_days = patient_days
        self.accepted = accepted

    @classmethod
    def from_frame(
        cls,
        patient_id: str,
        df: pd.DataFrame,
        daily_criterion: Callable[[dt.date, int], bool],
        patient_acceptance_criterion: Callable[[List[CTxPatientDay]], bool],
    ):
        start_date = df[dc.START_DT].min().to_pydatetime().date()
        end_date = df[dc.END_DT].max().to_pydatetime().date()
        existing_durations = dict(
            [
                (r[dc.START_DT].to_pydatetime().date(), r[dc.DAILY_DURATION_S])
                for l, r in df.iterrows()
            ]
        )
        patient_days: List[CTxPatientDay] = []
        for day in Interval.gen_days_in_interval(start_date, end_date):
            duration: float = (
                0 if day not in existing_durations else existing_durations[day]
            )
            patient_days.append(
                CTxPatientDay.create_patient_day(
                    day_date=day,
                    duration_s=int(duration),
                    daily_criterion=daily_criterion,
                )
            )
        return cls(patient_id, patient_days, patient_acceptance_criterion(patient_days))

    def get_days(self) -> List[dt.date]:
        return [d.day_date for d in self.patient_days]

    def get_durations(self) -> List[int]:
        return [d.duration_s for d in self.patient_days]

    def get_accepted(self) -> List[bool]:
        return [d.accepted for d in self.patient_days]

    def get_formatted_durations(self) -> List[str]:
        return [d.formatted_duration for d in self.patient_days]

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, CTxPatient):
            return self.patient_days == __o.patient_days
        return False

    def get_sum_accepted_days(self) -> int:
        return sum(self.get_accepted())
