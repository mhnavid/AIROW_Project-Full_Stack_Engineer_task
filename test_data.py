SUMMARY_1 = """
{
  "userId": "1234567890",
  "activityId": 9480958402,
  "activityName": "Indoor Cycling",
  "durationInSeconds": 3667,
  "startTimeInSeconds": 1661158927,
  "startTimeOffsetInSeconds": 7200,
  "activityType": "INDOOR_CYCLING",
  "averageHeartRateInBeatsPerMinute": 150,
  "activeKilocalories": 561,
  "deviceName": "instinct2",
  "maxHeartRateInBeatsPerMinute": 190
}
"""

SUMMARY_2 = """
{
  "activityId": 9480958402,
  "activityName": "Indoor Cycling"
}
"""

SUMMARY_3 = """
{
  "userId": "1234567890",
  "activityId": 9480958402,
  "activityName": "Indoor Cycling",
  "durationInSeconds": 3667,
  "startTimeInSeconds": 1661158927,
  "startTimeOffsetInSeconds": 7200,
  "activityType": "INDOOR_CYCLING",
  "averageHeartRateInBeatsPerMinute": 150,
  "activeKilocalories": 561
  "deviceName": "instinct2"
  "maxHeartRateInBeatsPerMinute": 190
}
"""

SAMPLES_1 = """
[
  {
    "recording-rate": 5,
    "sample-type": "0",
    "data": "86,87,88,88,88,90,91"
  },
  {
    "recording-rate": 5,
    "sample-type": "2",
    "data": "120,126,122,140,142,155,145"
  },
  {
    "recording-rate": 5,
    "sample-type": "2",
    "data": "141,147,155,160,180,152,120"
  },
  {
    "recording-rate": 5,
    "sample-type": "0",
    "data": "86,87,88,88,88,90,91"
  },
  {
    "recording-rate": 5,
    "sample-type": "1",
    "data": "143,87,88,88,88,90,91"
  },
  {
    "recording-rate": 5,
    "sample-type": "2",
    "data": "143,151,164,null,173,181,180"
  },
  {
    "recording-rate": 5,
    "sample-type": "2",
    "data": "182,170,188,181,174,172,158"
  },
    {
    "recording-rate": 5,
    "sample-type": "3",
    "data": "143,87,88,88,88,90,91"
  }
]
"""

SAMPLES_2 = """
[
  {
    "recording-rate": 5,
    "data": "86,87,88,88,88,90,91"
  },
  {
    "recording-rate": 5,
    "sample-type": "2",
    "data": "182,170,188,181,174,172,158"
  }
    {
    "recording-rate": 5,
    "sample-type": "3",
    "data": "143,87,88,88,88,90,91"
  }
]
"""

LAPS_1 = """
[
  {
    "startTimeInSeconds": 1661158927,
    "airTemperatureCelsius": 28,
    "heartRate": 109,
    "totalDistanceInMeters": 15,
    "timerDurationInSeconds": 600
  },
  {
    "startTimeInSeconds": 1661158929,
    "airTemperatureCelsius": 28,
    "heartRate": 107,
    "totalDistanceInMeters": 30,
    "timerDurationInSeconds": 900
  }
]
"""

LAPS_2 = """


 []
"""

LAPS_3 = """
[
  {
    "startTimeInSeconds": 1661158927,
    "airTemperatureCelsius": 28,
    "heartRate": 109,
    "totalDistanceInMeters": 15,
    "timerDurationInSeconds": 600
  }
  {
    "startTimeInSeconds": 1661158929,
    "airTemperatureCelsius": 28,
    "heartRate": 107,
    "totalDistanceInMeters": 30,
    "timerDurationInSeconds": 900
  }
]
"""

PROCESS_ACTIVITY_OVERVIEW_EXPECTED_1 = {
    "userId": "1234567890",
    "type": "INDOOR_CYCLING",
    "device": "instinct2",
    "maxHeartRate": 190,
    "duration": 3667,
}
PROCESS_ACTIVITY_OVERVIEW_EXPECTED_2 = {
    "userId": "Null",
    "type": "Null",
    "device": "Null",
    "maxHeartRate": "Null",
    "duration": "Null",
}
PROCESS_ACTIVITY_OVERVIEW_EXPECTED_3 = "Invalid Json Format!"

PROCESS_HEART_RATE_SAMPLE_EXPECTED_1 = [
    {"sampleIndex": 0, "heartRate": "120"},
    {"sampleIndex": 1, "heartRate": "126"},
    {"sampleIndex": 2, "heartRate": "122"},
    {"sampleIndex": 3, "heartRate": "140"},
    {"sampleIndex": 4, "heartRate": "142"},
    {"sampleIndex": 5, "heartRate": "155"},
    {"sampleIndex": 6, "heartRate": "145"},
    {"sampleIndex": 7, "heartRate": "141"},
    {"sampleIndex": 8, "heartRate": "147"},
    {"sampleIndex": 9, "heartRate": "155"},
    {"sampleIndex": 10, "heartRate": "160"},
    {"sampleIndex": 11, "heartRate": "180"},
    {"sampleIndex": 12, "heartRate": "152"},
    {"sampleIndex": 13, "heartRate": "120"},
    {"sampleIndex": 14, "heartRate": "143"},
    {"sampleIndex": 15, "heartRate": "151"},
    {"sampleIndex": 16, "heartRate": "164"},
    {"sampleIndex": 17, "heartRate": "173"},
    {"sampleIndex": 18, "heartRate": "181"},
    {"sampleIndex": 19, "heartRate": "180"},
    {"sampleIndex": 20, "heartRate": "182"},
    {"sampleIndex": 21, "heartRate": "170"},
    {"sampleIndex": 22, "heartRate": "188"},
    {"sampleIndex": 23, "heartRate": "181"},
    {"sampleIndex": 24, "heartRate": "174"},
    {"sampleIndex": 25, "heartRate": "172"},
    {"sampleIndex": 26, "heartRate": "158"},
]

PROCESS_HEART_RATE_SAMPLE_EXPECTED_2 = "Invalid Json Format!"
PROCESS_LAPS_DATA_1 = [
    {
        "startTime": 1661158927,
        "distance": 15,
        "duration": 600,
        "heartRateSamples": [
            {"sampleIndex": 0, "heartRate": "120"},
            {"sampleIndex": 1, "heartRate": "126"},
            {"sampleIndex": 2, "heartRate": "122"},
            {"sampleIndex": 3, "heartRate": "140"},
            {"sampleIndex": 4, "heartRate": "142"},
            {"sampleIndex": 5, "heartRate": "155"},
            {"sampleIndex": 6, "heartRate": "145"},
            {"sampleIndex": 7, "heartRate": "141"},
            {"sampleIndex": 8, "heartRate": "147"},
            {"sampleIndex": 9, "heartRate": "155"},
            {"sampleIndex": 10, "heartRate": "160"},
            {"sampleIndex": 11, "heartRate": "180"},
            {"sampleIndex": 12, "heartRate": "152"},
            {"sampleIndex": 13, "heartRate": "120"},
            {"sampleIndex": 14, "heartRate": "143"},
            {"sampleIndex": 15, "heartRate": "151"},
            {"sampleIndex": 16, "heartRate": "164"},
            {"sampleIndex": 17, "heartRate": "173"},
            {"sampleIndex": 18, "heartRate": "181"},
            {"sampleIndex": 19, "heartRate": "180"},
            {"sampleIndex": 20, "heartRate": "182"},
            {"sampleIndex": 21, "heartRate": "170"},
            {"sampleIndex": 22, "heartRate": "188"},
            {"sampleIndex": 23, "heartRate": "181"},
            {"sampleIndex": 24, "heartRate": "174"},
            {"sampleIndex": 25, "heartRate": "172"},
            {"sampleIndex": 26, "heartRate": "158"},
        ],
    },
    {
        "startTime": 1661158929,
        "distance": 30,
        "duration": 900,
        "heartRateSamples": [
            {"sampleIndex": 0, "heartRate": "120"},
            {"sampleIndex": 1, "heartRate": "126"},
            {"sampleIndex": 2, "heartRate": "122"},
            {"sampleIndex": 3, "heartRate": "140"},
            {"sampleIndex": 4, "heartRate": "142"},
            {"sampleIndex": 5, "heartRate": "155"},
            {"sampleIndex": 6, "heartRate": "145"},
            {"sampleIndex": 7, "heartRate": "141"},
            {"sampleIndex": 8, "heartRate": "147"},
            {"sampleIndex": 9, "heartRate": "155"},
            {"sampleIndex": 10, "heartRate": "160"},
            {"sampleIndex": 11, "heartRate": "180"},
            {"sampleIndex": 12, "heartRate": "152"},
            {"sampleIndex": 13, "heartRate": "120"},
            {"sampleIndex": 14, "heartRate": "143"},
            {"sampleIndex": 15, "heartRate": "151"},
            {"sampleIndex": 16, "heartRate": "164"},
            {"sampleIndex": 17, "heartRate": "173"},
            {"sampleIndex": 18, "heartRate": "181"},
            {"sampleIndex": 19, "heartRate": "180"},
            {"sampleIndex": 20, "heartRate": "182"},
            {"sampleIndex": 21, "heartRate": "170"},
            {"sampleIndex": 22, "heartRate": "188"},
            {"sampleIndex": 23, "heartRate": "181"},
            {"sampleIndex": 24, "heartRate": "174"},
            {"sampleIndex": 25, "heartRate": "172"},
            {"sampleIndex": 26, "heartRate": "158"},
        ],
    },
]
PROCESS_LAPS_DATA_2 = []
PROCESS_LAPS_DATA_3 = "Invalid Json Format!"