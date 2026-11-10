# Lists, tuples, dicts and sets with test bench readings.
# Run from the repo root:
#   uv run python exercises/python/03-collections/collections_intro.py

# --- Lists: an ordered, changeable collection ---
pressures_bar = [7.1, 7.3, 7.4, 7.2, 7.6, 7.5]

print("First:", pressures_bar[0])
# TODO 1: print the last reading with a negative index (-1).

# TODO 2: print the first three readings with a slice [start:stop].
# Remember: the stop index is not included.

# TODO 3: add a new reading 7.8 to the end with .append().
# Then print how many readings there are with len().

# TODO 4: print the highest, lowest and average reading.
# Hint: max(), min(), sum() and len().

# TODO 5: sort the list from high to low and print it.
# Hint: sorted(pressures_bar, reverse=True)

# --- Tuples: an ordered collection that cannot change ---
position = (52.01, 4.36)  # latitude and longitude of the test hall
# TODO 6: unpack the tuple into two variables: latitude, longitude.
# Then try position[0] = 0.0 in the Python REPL and read the error.

# --- Dicts: key and value pairs ---
measurement = {
    "timestamp": "2026-01-15 09:00:00",
    "pressure_bar": 7.5,
    "temperature_c": 82.0,
}
print("Pressure:", measurement["pressure_bar"])
# TODO 7: add the key "flow_l_s" with the value 41.5.
# TODO 8: change the temperature to 83.5.
# TODO 9: print every key and value. Hint: for key, value in measurement.items():

# --- A list of dicts: one dict per measurement ---
measurements = [
    {"timestamp": "09:00", "pressure_bar": 7.1, "temperature_c": 80.5},
    {"timestamp": "09:01", "pressure_bar": 7.4, "temperature_c": 81.9},
    {"timestamp": "09:02", "pressure_bar": 7.6, "temperature_c": 83.2},
]
# TODO 10 (optional): print the temperature of the second measurement.
# TODO 11 (optional): build a list with only the pressures.
# Hint: start with [], use a for loop and .append().

# --- Sets: unique values only ---
sensor_ids = ["P1", "T1", "P1", "F1", "T1", "P2"]
# TODO 12 (optional): find the unique sensor ids with set(sensor_ids) and print how many there are.
# Is "F1" in the set? Use the word in.
