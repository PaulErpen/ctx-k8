import unittest
import datetime as dt
from dashboard.ctxdashboard.model.patient_day import CTxPatientDay


class PatientDayTest(unittest.TestCase):
    def test_given_valid_parameters__when_initializing__then_create_patient_day(
        self,
    ) -> None:
        patient_day = CTxPatientDay(
            dt.date(2023, 10, 1),
            3600,
            True,
            "FORMATTED_DURATION",
        )

        self.assertIsInstance(patient_day, CTxPatientDay)

    def test_given_valid_parameters__when_initializing_via_the_class_method__then_create_patient_day(
        self,
    ) -> None:
        patient_day = CTxPatientDay.create_patient_day(
            dt.date(2023, 10, 1),
            3600,
            lambda _date, _duration: True,
        )

        self.assertIsInstance(patient_day, CTxPatientDay)

    def test_given_a_true_acceptance_cirterion__when_initializing_via_the_class_method__then_the_day_must_be_accepted(
        self,
    ) -> None:
        patient_day = CTxPatientDay.create_patient_day(
            dt.date(2023, 10, 1),
            3600,
            lambda _date, _duration: True,
        )

        self.assertTrue(patient_day.accepted)

    def test_given_a_false_acceptance_cirterion__when_initializing_via_the_class_method__then_the_day_must_not_be_accepted(
        self,
    ) -> None:
        patient_day = CTxPatientDay.create_patient_day(
            dt.date(2023, 10, 1),
            3600,
            lambda _date, _duration: False,
        )

        self.assertFalse(patient_day.accepted)

    def test_given_a_duration_of_3600__when_initializing_via_the_class_method__then_the_day_must_be_accepted(
        self,
    ) -> None:
        patient_day = CTxPatientDay.create_patient_day(
            dt.date(2023, 10, 1),
            3600,
            lambda _date, duration: duration >= 3600,
        )

        self.assertTrue(patient_day.accepted)

    def test_given_a_duration_of_3500__when_initializing_via_the_class_method__then_the_day_must_be_accepted(
        self,
    ) -> None:
        patient_day = CTxPatientDay.create_patient_day(
            dt.date(2023, 10, 1),
            3500,
            lambda _date, duration: duration >= 3600,
        )

        self.assertFalse(patient_day.accepted)
    
    def test_given_a_duration_of_3600__when_formatting__then_the_formatted_duration_must_be_01_00_00(
        self,
    ) -> None:
        patient_day = CTxPatientDay.create_patient_day(
            dt.date(2023, 10, 1),
            3600,
            lambda _date, duration: duration >= 3600,
        )

        self.assertEqual(patient_day.formatted_duration, "01:00:00")
    
    def test_given_a_duration_of_3661__when_formatting__then_the_formatted_duration_must_be_01_01_01(
        self,
    ) -> None:
        patient_day = CTxPatientDay.create_patient_day(
            dt.date(2023, 10, 1),
            3661,
            lambda _date, duration: duration >= 3600,
        )

        self.assertEqual(patient_day.formatted_duration, "01:01:01")
