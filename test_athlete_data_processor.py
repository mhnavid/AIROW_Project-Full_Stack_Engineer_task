import unittest
import json
from athlete_data_processor import (
    AthleteDataProcessor,
)
from test_data import (
    SUMMARY_1,
    SUMMARY_2,
    SUMMARY_3,
    SAMPLES_1,
    SAMPLES_2,
    LAPS_1,
    LAPS_2,
    LAPS_3,
    PROCESS_ACTIVITY_OVERVIEW_EXPECTED_1,
    PROCESS_ACTIVITY_OVERVIEW_EXPECTED_2,
    PROCESS_ACTIVITY_OVERVIEW_EXPECTED_3,
    PROCESS_HEART_RATE_SAMPLE_EXPECTED_1,
    PROCESS_HEART_RATE_SAMPLE_EXPECTED_2,
    PROCESS_LAPS_DATA_1,
    PROCESS_LAPS_DATA_2,
    PROCESS_LAPS_DATA_3,
)


class TestAthleteDataProcessor(unittest.TestCase):

    def setUp(self):
        self.processor_1 = AthleteDataProcessor(SUMMARY_1, SAMPLES_1, LAPS_1)
        self.processor_2 = AthleteDataProcessor(SUMMARY_2, SAMPLES_2, LAPS_2)
        self.processor_3 = AthleteDataProcessor(SUMMARY_3, SAMPLES_1, LAPS_3)

    def test_process_activity_overview(self):
        result_1 = self.processor_1.process_activity_overview()
        result_2 = self.processor_2.process_activity_overview()
        result_3 = self.processor_3.process_activity_overview()
        self.assertEqual(result_1, PROCESS_ACTIVITY_OVERVIEW_EXPECTED_1)
        self.assertEqual(result_2, PROCESS_ACTIVITY_OVERVIEW_EXPECTED_2)
        self.assertEqual(result_3, PROCESS_ACTIVITY_OVERVIEW_EXPECTED_3)

    def test_process_heart_rate_sample(self):
        result_1 = self.processor_1.process_heart_rate_sample()
        result_2 = self.processor_2.process_heart_rate_sample()
        self.assertEqual(result_1, PROCESS_HEART_RATE_SAMPLE_EXPECTED_1)
        self.assertEqual(result_2, PROCESS_HEART_RATE_SAMPLE_EXPECTED_2)

    def test_process_laps_data(self):
        result_1 = self.processor_1.process_laps_data()
        result_2 = self.processor_2.process_laps_data()
        result_3 = self.processor_3.process_laps_data()
        self.assertEqual(result_1, PROCESS_LAPS_DATA_1)
        self.assertEqual(result_2, PROCESS_LAPS_DATA_2)
        self.assertEqual(result_3, PROCESS_LAPS_DATA_3)

    def test_get_final_result(self):
        result_1 = json.loads(self.processor_1.get_final_result())
        result_2 = json.loads(self.processor_2.get_final_result())

        self.assertIn("activityOverview", result_1)
        self.assertIn("activityOverview", result_2)
        self.assertIn("laps", result_1)
        self.assertIn("laps", result_2)

        self.assertEqual(
            result_1["activityOverview"], PROCESS_ACTIVITY_OVERVIEW_EXPECTED_1
        )
        self.assertEqual(
            result_2["activityOverview"], PROCESS_ACTIVITY_OVERVIEW_EXPECTED_2
        )

        self.assertEqual(len(result_1["laps"]), 2)
        self.assertEqual(len(result_2["laps"]), 0)


if __name__ == "__main__":
    unittest.main()
