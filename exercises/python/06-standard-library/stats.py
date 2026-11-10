# Read a CSV file, compute statistics and write a JSON summary.
# Run from the repo root:
#   uv run python exercises/python/06-standard-library/stats.py

import csv
import json
import math
from pathlib import Path

# Path(__file__) is the path of this script. .parent is its folder.
# Building paths this way works on Windows and Linux, from any folder.
folder = Path(__file__).parent
csv_path = folder / "measurements.csv"
output_path = folder / "output" / "summary.json"

# --- Read the CSV ---
pressures_bar = []
temperatures_c = []

with open(csv_path, newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Every value from a CSV is text. Convert it to a number.
        # TODO 1: append float(row["pressure_bar"]) to pressures_bar
        # and float(row["temperature_c"]) to temperatures_c.
        pass

print("Rows read:", len(pressures_bar))

# --- Statistics ---
# TODO 2: calculate the mean pressure (sum / len).
mean_bar = ...

# TODO 3: calculate the standard deviation of the pressure:
#   take the square root (math.sqrt) of the mean of (p - mean_bar) ** 2 for every p.
std_bar = ...

# TODO 4: find the maximum temperature with max().
max_temperature_c = ...

print(f"Mean pressure: {mean_bar} bar")

# --- Write the JSON summary ---
summary = {
    "source_file": csv_path.name,
    "rows": len(pressures_bar),
    "pressure_mean_bar": mean_bar,
    "pressure_std_bar": std_bar,
    "temperature_max_c": max_temperature_c,
}

# TODO 5: make sure the output folder exists:
#   output_path.parent.mkdir(exist_ok=True)
# Then write the summary with json.dump(summary, file, indent=2).
# Round the numbers to 3 decimals first with round().
print("TODO: write", output_path)

# TODO 6: read the file back with json.load and print the mean pressure from it.
