import unittest
from dashboard.ctxdashboard.acceptance.overall_consecutive_days import (
    minimum_overall_and_consecutive_days_patient_acceptance_criterion,
)
from dashboard.ctxdashboard.model.patient_day import CTxPatientDay
import datetime as dt


class OverallConsecutiveDaysTest(unittest.TestCase):
    def test_given_a_criterion_with_minimum_of_3_days__when_calling_with_3_accepted_days__then_the_criterion_must_return_true(
        self,
    ) -> None:
        min_days = 3
        min_consecutive_days = 1
        criterion = minimum_overall_and_consecutive_days_patient_acceptance_criterion(
            min_days, min_consecutive_days
        )

        result = criterion(
            [
                CTxPatientDay.create_patient_day(
                    dt.date(2023, 10, 1), 3600, lambda _date, _duration: True
                ),
                CTxPatientDay.create_patient_day(
                    dt.date(2023, 10, 2), 3600, lambda _date, _duration: True
                ),
                CTxPatientDay.create_patient_day(
                    dt.date(2023, 10, 3), 3600, lambda _date, _duration: True
                ),
            ]
        )

        self.assertTrue(result)

    def test_given_a_criterion_with_minimum_of_3_days__when_calling_with_2_accepted_days__then_the_criterion_must_return_false(
        self,
    ) -> None:
        min_days = 3
        min_consecutive_days = 1
        criterion = minimum_overall_and_consecutive_days_patient_acceptance_criterion(
            min_days, min_consecutive_days
        )

        result = criterion(
            [
                CTxPatientDay.create_patient_day(
                    dt.date(2023, 10, 1), 3600, lambda _date, _duration: True
                ),
                CTxPatientDay.create_patient_day(
                    dt.date(2023, 10, 2), 3600, lambda _date, _duration: False
                ),
                CTxPatientDay.create_patient_day(
                    dt.date(2023, 10, 3), 3600, lambda _date, _duration: True
                ),
            ]
        )

        self.assertFalse(result)

    def test_given_a_criterion_that_required_3_consecutive_days__when_calling_with_3_consecutive_accepted_days__then_the_criterion_must_return_true(
        self,
    ) -> None:
        min_days = 3
        min_consecutive_days = 3
        criterion = minimum_overall_and_consecutive_days_patient_acceptance_criterion(
            min_days, min_consecutive_days
        )

        result = criterion(
            [
                CTxPatientDay.create_patient_day(
                    dt.date(2023, 10, 1), 3600, lambda _date, _duration: True
                ),
                CTxPatientDay.create_patient_day(
                    dt.date(2023, 10, 2), 3600, lambda _date, _duration: True
                ),
                CTxPatientDay.create_patient_day(
                    dt.date(2023, 10, 3), 3600, lambda _date, _duration: True
                ),
            ]
        )

        self.assertTrue(result)

    def test_given_a_criterion_that_required_3_consecutive_days__when_calling_with_2_consecutive_accepted_days__then_the_criterion_must_return_false(
        self,
    ) -> None:
        min_days = 3
        min_consecutive_days = 3
        criterion = minimum_overall_and_consecutive_days_patient_acceptance_criterion(
            min_days, min_consecutive_days
        )

        result = criterion(
            [
                CTxPatientDay.create_patient_day(
                    dt.date(2023, 10, 1), 3600, lambda _date, _duration: True
                ),
                CTxPatientDay.create_patient_day(
                    dt.date(2023, 10, 2), 3600, lambda _date, _duration: True
                ),
                CTxPatientDay.create_patient_day(
                    dt.date(2023, 10, 3), 3600, lambda _date, _duration: False
                ),
                CTxPatientDay.create_patient_day(
                    dt.date(2023, 10, 4), 3600, lambda _date, _duration: True
                ),
            ]
        )

        self.assertFalse(result)
