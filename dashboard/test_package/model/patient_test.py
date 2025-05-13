import unittest

from ctxdashboard.model.patient import CTxPatient
from ctxdashboard.model.dailies_columns import DailiesColumns as dc
import pandas as pd


class PatientTest(unittest.TestCase):
    def test_given_valid_parameters__when_initializing__then_create_a_patient(self) -> None:
        patient = CTxPatient(
            "PATIENT_ID",
            [],
            True,
        )

        self.assertIsInstance(patient, CTxPatient)
    
    def test_given_a_frame_with_one_row__when_initializing__then_create_a_patient(self) -> None:
        patient = CTxPatient.from_frame(
            "PATIENT_ID",
            pd.DataFrame.from_dict({
                dc.START_DT: [pd.Timestamp("2023-10-01")],
                dc.END_DT: [pd.Timestamp("2023-10-02")],
                dc.DAILY_DURATION_S: [3600],
            }),
            lambda _date, _duration: True,
            lambda _days: True,
        )

        self.assertIsInstance(patient, CTxPatient)
        self.assertEqual(patient.patient_id, "PATIENT_ID")
        self.assertEqual(len(patient.patient_days), 1)
        self.assertTrue(patient.accepted)