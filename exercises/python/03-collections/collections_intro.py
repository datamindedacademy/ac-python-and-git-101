# Lists, tuples, dicts and sets with test bench readings.
# Run from the repo root:
#   uv run python exercises/python/03-collections/collections_intro.py
# No loops are needed for the core TODOs. Loops come in exercise 04.

# --- Lists: an ordered, changeable collection ---
pressures_bar = [7.1, 7.3, 7.4, 7.2, 7.6, 7.5]

print("First:", pressures_bar[0])
# TODO 1: print the last reading as: Last: 7.5

# TODO 2: print the first three readings as: First three: [7.1, 7.3, 7.4]

# TODO 3: add the reading 7.8 at the end of the list.
# Print the number of readings as: Number of readings: 7

# TODO 4: print the highest, lowest and mean reading on one line, as:
#   Max: 7.8 Min: 7.1 Mean: 7.414285714285714

# TODO 5: print the three highest readings, highest first, as: Top three: [7.8, 7.6, 7.5]

# TODO 6: print the mean of the readings without the single highest and the single
# lowest one (a trimmed mean), rounded to 3 decimals, as: Trimmed mean: 7.4
# Do it without a loop.
trimmed_mean_bar = ...

# --- Tuples: an ordered collection that cannot change ---
position = (52.01, 4.36)  # latitude and longitude of the test hall
# TODO 7: split position into two variables latitude and longitude.
# Print them as: Latitude: 52.01 Longitude: 4.36
latitude = ...
longitude = ...

# --- Dicts: key and value pairs ---
measurement = {
    "timestamp": "2026-01-15 09:00:00",
    "pressure_bar": 7.5,
    "temperature_c": 82.0,
}
print("Pressure:", measurement["pressure_bar"])
# TODO 8: add the key "flow_l_s" with the value 41.5 and change the temperature to 83.5.
# Print the whole dict. The output is one line that starts with
#   {'timestamp': '2026-01-15 09:00:00', 'pressure_bar': 7.5,
# and ends with
#   'temperature_c': 83.5, 'flow_l_s': 41.5}

# --- A list of dicts: one dict per measurement ---
measurements = [
    {"timestamp": "09:00", "pressure_bar": 7.1, "temperature_c": 80.5},
    {"timestamp": "09:01", "pressure_bar": 7.4, "temperature_c": 81.9},
    {"timestamp": "09:02", "pressure_bar": 7.6, "temperature_c": 83.2},
]
# TODO 9: print the temperature of the second measurement as: Temperature of second: 81.9
# Print the pressure of the last measurement as: Pressure of last: 7.6
# Pick the last one from the end of the list, so it still works when the list grows.

# TODO 10: add a fourth measurement to the list: timestamp "09:03", pressure 7.3,
# temperature 82.4. Print the number of measurements as: Number of measurements: 4

# --- Sets: unique values only ---
sensor_ids = ["P1", "T1", "P1", "F1", "T1", "P2"]
# TODO 11: print the number of unique sensor ids as: Unique sensors: 4
# Print whether "F1" is one of them as: F1 present: True
