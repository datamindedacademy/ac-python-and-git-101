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
            # Every value from a CSV is text.
            # TODO 1: fill pressures_bar and temperatures_c with the values of all rows,
            # as numbers. run_01.csv gives 8 values in each list.
            pass

    # TODO 2: calculate the mean pressure of the run, and keep it in mean_bar.
    # run_01 gives 7.25 (the print below rounds it to 2 decimals).
    mean_bar = 0.0

    # TODO 3: calculate the standard deviation of the pressures, and keep it in std_bar.
    # Use the population standard deviation: the square root of the mean of the squared
    # differences between each pressure and mean_bar. Divide by the number of rows.
    # run_01 gives 0.2 after rounding to 2 decimals.
    std_bar = 0.0

    # TODO 4: find the highest temperature of the run, and keep it in max_temperature_c.
    # run_01 gives 82.7.
    max_temperature_c = 0.0

    print(f"{path.name}: {len(pressures_bar)} rows, mean pressure {round(mean_bar, 2)} bar")

    # TODO 5: fill the dict with your results, each rounded to 2 decimals.
    summary = {
        "run": path.stem,
        "rows": len(pressures_bar),
        "pressure_mean_bar": mean_bar,
        "pressure_std_bar": std_bar,
        "temperature_max_c": max_temperature_c,
    }
    summaries.append(summary)

# TODO 6: write the summaries to output_path as a JSON file, indented by 2 spaces.
# The folder of output_path may not exist yet. Make sure it does.
# The file must hold a list of three objects, one per run.
print("TODO: write", output_path)
