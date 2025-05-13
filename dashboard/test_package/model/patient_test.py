import unittest

from ctxdashboard.model.patient import CTxPatient


class PatientTest(unittest.TestCase):
    def test_given_valid_parameters__when_initializing__then_create_a_patient(self) -> None:
        patient = CTxPatient(
            "PATIENT_ID",
            [],
            True,
        )

        self.assertIsInstance(patient, CTxPatient)