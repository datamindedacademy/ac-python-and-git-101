# Summarise every CSV test-run log in the runs/ folder.
# Run from the repo root:
#   uv run python exercises/python/06-standard-library/summarize_runs.py

import csv
import json
import math
from pathlib import Path

# Path(__file__) is the path of this script. .parent is its folder.
# Building paths this way works on Windows and Linux, from any folder.
folder = Path(__file__).parent
runs_folder = folder / "runs"
output_path = folder / "output" / "summary.json"

summaries = []

# glob("*.csv") finds all CSV files in the folder. sorted() puts them in order.
for path in sorted(runs_folder.glob("*.csv")):
    pressures_bar = []
    temperatures_c = []

    with open(path, newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Every value from a CSV is text. Convert it to a number.
            # TODO 1: append float(row["pressure_bar"]) to pressures_bar
            # and float(row["temperature_c"]) to temperatures_c.
            pass

    # TODO 2: calculate the mean pressure (sum divided by len).
    mean_bar = ...

    # TODO 3: calculate the standard deviation of the pressure:
    #   take math.sqrt of the mean of (p - mean_bar) ** 2 for every p.
    # Hint: the sum of squares can be a comprehension inside sum(...).
    std_bar = ...

    # TODO 4: find the maximum temperature with max().
    max_temperature_c = ...

    print(f"{path.name}: {len(pressures_bar)} rows, mean pressure {mean_bar} bar")

    # TODO 5: fill the dict with your results, rounded to 2 decimals with round().
    summary = {
        "run": path.stem,
        "rows": len(pressures_bar),
        "pressure_mean_bar": mean_bar,
        "pressure_std_bar": std_bar,
        "temperature_max_c": max_temperature_c,
    }
    summaries.append(summary)

# TODO 6: make sure the output folder exists with output_path.parent.mkdir(exist_ok=True).
# Then write the summaries to output_path with json.dump(summaries, file, indent=2).
print("TODO: write", output_path)
