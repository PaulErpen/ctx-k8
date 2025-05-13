from typing import Callable, List
from dashboard.ctxdashboard.model.patient_day import CTxPatientDay


def minimum_overall_and_consecutive_days_patient_acceptance_criterion(
    min_days: int, min_consecutive_days: int
) -> Callable[[List[CTxPatientDay]], bool]:
    def accept_patient(days: List[CTxPatientDay]) -> bool:
        n_accepted_days = 0
        for day in days:
            if day.accepted:
                n_accepted_days += 1
        min_days_criterion = n_accepted_days >= min_days

        sequences = []
        prev = None
        for day in days:
            if day.accepted:
                if prev is None or prev.accepted is False:
                    sequences.append(1)
                else:
                    sequences[-1] = sequences[-1] + 1
            prev = day
        consecutive_days_criterion = (
            len(sequences) > 0 and max(sequences) >= min_consecutive_days
        )
        return min_days_criterion and consecutive_days_criterion

    return accept_patient
