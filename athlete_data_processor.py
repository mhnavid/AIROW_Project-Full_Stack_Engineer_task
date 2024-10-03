"""
AthleteDataProcessor: A class to process athlete data including activity overview, 
heart rate samples, and lap data.
"""

import json


class AthleteDataProcessor:
    """
    This class processes the athlete data and returns the final result in JSON format.
    """

    def __init__(self, summary, samples, laps):
        """
        Constructs the necessary attributes for the AthleteDataProcessor object.
        """
        self.summary = summary
        self.samples = samples
        self.laps = laps

    def check_json_key(self, json_data, key):
        """
        Check for the key exists or not in json data.
        """
        if key in json_data:
            return json_data[key]
        return "Null"

    def process_activity_overview(self):
        """
        Processes the activity overview from the summary JSON.
        """
        try:
            summary_json_data = json.loads(self.summary)
        except ValueError:
            return "Invalid Json Format!"

        output_data = {
            "userId": self.check_json_key(summary_json_data, "userId"),
            "type": self.check_json_key(summary_json_data, "activityType"),
            "device": self.check_json_key(summary_json_data, "deviceName"),
            "maxHeartRate": self.check_json_key(
                summary_json_data, "maxHeartRateInBeatsPerMinute"
            ),
            "duration": self.check_json_key(summary_json_data, "durationInSeconds"),
        }

        return output_data

    def process_heart_rate_sample(self):
        """
        Processes heart rate samples from the samples JSON.
        """
        heart_rate_samples = []
        idx = 0
        try:
            sample_json_data = json.loads(self.samples)
        except ValueError:
            return "Invalid Json Format!"

        for sample in sample_json_data:
            if self.check_json_key(sample, "sample-type") == "2":
                heart_rates = self.check_json_key(sample, "data").split(",")
                for data in heart_rates:
                    if data != "null":
                        format_data = {"sampleIndex": idx, "heartRate": data}
                        heart_rate_samples.append(format_data)
                        idx += 1
        return heart_rate_samples

    def process_laps_data(self):
        """
        Processes laps data from the laps JSON.
        """
        processed_lap_data = []
        try:
            lap_json_data = json.loads(self.laps)
        except ValueError:
            return "Invalid Json Format!"
        for lap in lap_json_data:
            lap_data = {
                "startTime": self.check_json_key(lap, "startTimeInSeconds"),
                "distance": self.check_json_key(lap, "totalDistanceInMeters"),
                "duration": self.check_json_key(lap, "timerDurationInSeconds"),
                "heartRateSamples": self.process_heart_rate_sample(),
            }

            processed_lap_data.append(lap_data)

        return processed_lap_data

    def get_final_result(self):
        """
        Combines processed activity overview and laps data into a final JSON result.
        """
        output_json = {}
        output_json["activityOverview"] = self.process_activity_overview()
        output_json["laps"] = self.process_laps_data()
        return json.dumps(output_json, indent=2)


if __name__ == "__main__":
    from data import SUMMARY, SAMPLES, LAPS

    process = AthleteDataProcessor(SUMMARY, SAMPLES, LAPS)
    print(process.get_final_result())
