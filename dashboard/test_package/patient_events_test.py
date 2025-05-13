import unittest
import pandas as pd
from ctxdashboard.model.patient_events import create_patient_events_sheets
from ctxdashboard.model.dailies_columns import DailiesColumns as dc
import datetime as dt


class PatientEventsTest(unittest.TestCase):
    example_dailies = pd.DataFrame(
        data={
            f"{dc.START_DT.value}": [dt.datetime(2020, 11, 11, 12, 00), dt.datetime(2020, 11, 13, 12, 00)],
            f"{dc.USER_LAST_NAME.value}": ["1", "2"],
            f"{dc.DAILY_DURATION_S.value}": [50, 10]
        }
    )

    def test_create_patient_events_sheets_number(self) -> None:
        event_tuples = list(create_patient_events_sheets(
            PatientEventsTest.example_dailies))
        self.assertEquals(len(event_tuples), 2)

    def test_create_patient_events_sheets_shape(self) -> None:
        event_tuples = list(create_patient_events_sheets(
            PatientEventsTest.example_dailies))
        self.assertEqual(event_tuples[0].sheet.shape, (2, 15))

    def test_create_patient_events_sheets_tracker_ids(self) -> None:
        t_ids = [t.tracker_id for t in create_patient_events_sheets(
            PatientEventsTest.example_dailies)]
        self.assertCountEqual(t_ids, ["1", "2"])
