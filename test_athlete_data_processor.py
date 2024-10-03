import unittest
import json
from athlete_data_processor import (
    AthleteDataProcessor,
)


class TestAthleteDataProcessor(unittest.TestCase):

    def setUp(self):
        """
        Set up test data before each test.
        """
        self.summary = json.dumps(
            {
                "userId": "12345",
                "activityType": "Running",
                "deviceName": "Watch X",
                "maxHeartRateInBeatsPerMinute": 180,
                "durationInSeconds": 3600,
            }
        )

        self.samples = json.dumps(
            [
                {"sample-type": "2", "data": "120,130,140,null,150"},
                {"sample-type": "1", "data": "200,220,240"},
            ]
        )

        self.laps = json.dumps(
            [
                {
                    "startTimeInSeconds": 0,
                    "totalDistanceInMeters": 1000,
                    "timerDurationInSeconds": 600,
                },
                {
                    "startTimeInSeconds": 600,
                    "totalDistanceInMeters": 1000,
                    "timerDurationInSeconds": 600,
                },
            ]
        )

        self.processor = AthleteDataProcessor(self.summary, self.samples, self.laps)

    def test_process_activity_overview(self):
        expected_output = {
            "userId": "12345",
            "type": "Running",
            "device": "Watch X",
            "maxHeartRate": 180,
            "duration": 3600,
        }
        result = self.processor.process_activity_overview()
        self.assertEqual(result, expected_output)

    def test_process_heart_rate_sample(self):
        expected_output = [
            {"sampleIndex": 0, "heartRate": "120"},
            {"sampleIndex": 1, "heartRate": "130"},
            {"sampleIndex": 2, "heartRate": "140"},
            {"sampleIndex": 3, "heartRate": "150"},
        ]
        result = self.processor.process_heart_rate_sample()
        self.assertEqual(result, expected_output)

    def test_process_laps_data(self):
        expected_output = [
            {
                "startTime": 0,
                "distance": 1000,
                "duration": 600,
                "heartRateSamples": [
                    {"sampleIndex": 0, "heartRate": "120"},
                    {"sampleIndex": 1, "heartRate": "130"},
                    {"sampleIndex": 2, "heartRate": "140"},
                    {"sampleIndex": 3, "heartRate": "150"},
                ],
            },
            {
                "startTime": 600,
                "distance": 1000,
                "duration": 600,
                "heartRateSamples": [
                    {"sampleIndex": 0, "heartRate": "120"},
                    {"sampleIndex": 1, "heartRate": "130"},
                    {"sampleIndex": 2, "heartRate": "140"},
                    {"sampleIndex": 3, "heartRate": "150"},
                ],
            },
        ]
        result = self.processor.process_laps_data()
        self.assertEqual(result, expected_output)

    def test_get_final_result(self):
        result = json.loads(self.processor.get_final_result())

        self.assertIn("activityOverview", result)
        self.assertIn("laps", result)

        expected_activity_overview = {
            "userId": "12345",
            "type": "Running",
            "device": "Watch X",
            "maxHeartRate": 180,
            "duration": 3600,
        }
        self.assertEqual(result["activityOverview"], expected_activity_overview)

        self.assertEqual(len(result["laps"]), 2)


if __name__ == "__main__":
    unittest.main()
