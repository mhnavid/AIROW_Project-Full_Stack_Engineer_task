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

    def process_activity_overview(self):
        """
        Processes the activity overview from the summary JSON.
        """
        summary_json_data = json.loads(self.summary)
        output_data = {
            "userId": summary_json_data["userId"],
            "type": summary_json_data["activityType"],
            "device": summary_json_data["deviceName"],
            "maxHeartRate": summary_json_data["maxHeartRateInBeatsPerMinute"],
            "duration": summary_json_data["durationInSeconds"],
        }

        return output_data

    def process_heart_rate_sample(self):
        """
        Processes heart rate samples from the samples JSON.
        """
        heart_rate_samples = []
        idx = 0
        for sample in json.loads(self.samples):
            if sample["sample-type"] == "2":
                heart_rates = sample["data"].split(",")
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
        for lap in json.loads(self.laps):
            lap_data = {
                "startTime": lap["startTimeInSeconds"],
                "distance": lap["totalDistanceInMeters"],
                "duration": lap["timerDurationInSeconds"],
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
