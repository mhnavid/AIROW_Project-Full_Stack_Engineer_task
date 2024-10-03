# Athlete Data Processor

This library processes athlete data and returns the final result in JSON format. It includes methods to process activity overview, heart rate samples, and lap data.

## Prerequisites

- Python 3.x
- `pip` (Python package installer)

## Setup

1. Clone the repository:

```sh
git clone https://github.com/mhnavid/AIROW_Project-Full_Stack_Engineer_task.git

cd AIROW_Project-Full_Stack_Engineer_task
```

2. [If requires] Create a virtual environment and activate it:

```sh
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install the required packages:

```sh
pip install -r requirements.txt
```

## Running the Code

To run the main script and see the processed athlete data using sample dataset:

```sh
python athlete_data_processor.py
```

## Running Tests

To run the tests and check the coverage:

1. Install coverage:

```sh
pip install coverage
```

2. Run the tests with coverage:

```sh
coverage run -m unittest discover
```

3. Generate the coverage report:

```sh
coverage report -m
```

## Development

To modify or develop the project:

1. Make your changes in the appropriate files `athlete_data_processor.py`
2. Add or modify tests in `test_athlete_data_processor.py` to ensure your changes are covered.
3. Run the tests and check the coverage as described above.