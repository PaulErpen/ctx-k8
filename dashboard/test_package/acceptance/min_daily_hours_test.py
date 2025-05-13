import unittest
from ctxdashboard.acceptance.min_daily_hours import simple_min_hours_daily_acceptance_criterion


class MinDailyHoursTest(unittest.TestCase):
    def test_given_a_minimum_of_3_daily_hours__when_calling_the_criterion_with_300_seconds_then_it_must_return_false(
        self,
    ) -> None:
        min_hours = 3
        criterion = simple_min_hours_daily_acceptance_criterion(min_hours)

        result = criterion(None, 300)

        self.assertFalse(result)

    def test_given_a_minimum_of_3_daily_hours__when_calling_the_criterion_with_10800_seconds_then_it_must_return_true(
        self,
    ) -> None:
        min_hours = 3
        criterion = simple_min_hours_daily_acceptance_criterion(min_hours)

        result = criterion(None, 10800)

        self.assertTrue(result)
