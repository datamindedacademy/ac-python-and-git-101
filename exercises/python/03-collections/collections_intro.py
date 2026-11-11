# Lists, tuples, dicts and sets with test bench readings.
# Run from the repo root:
#   uv run python exercises/python/03-collections/collections_intro.py
# No loop and no `if` is needed. They come in exercise 04.

timestamps = ["09:00", "09:01", "09:02", "09:03", "09:04", "09:05"]
pressures_bar = [7.1, 7.3, 7.4, 7.2, 7.6, 7.5]

# --- Task 1: lists ---
# Print these three lines. The code must still be right when the list gets longer.
#   Last: 7.5
#   Top three: [7.6, 7.5, 7.4]
#   Trimmed mean: 7.35
# The trimmed mean is the mean without the single highest and single lowest reading.


# --- Task 2: dicts, tuples and sets ---
measurements = [
    {"timestamp": "09:00", "sensor": "P1", "pressure_bar": 7.1},
    {"timestamp": "09:01", "sensor": "P2", "pressure_bar": 7.4},
    {"timestamp": "09:02", "sensor": "P1", "pressure_bar": 7.6},
]
position = (52.01, 4.36)  # latitude and longitude of the test hall
sensor_ids = ["P1", "T1", "P1", "F1", "T1", "P2"]

# Add a fourth measurement: timestamp "09:03", sensor "P2", pressure 7.3.
# Then print these four lines:
#   Measurements: 4
#   Pressure of last: 7.3
#   Unique sensors: 4
#   Hall: 52.01 N, 4.36 E


# --- Task 3: median and peak ---
# See the README.
