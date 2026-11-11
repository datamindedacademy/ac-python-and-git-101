# Summarise the logs in logs/, even when a value is not a number.
# Run from the repo root:
#   uv run python exercises/python/07-files-and-exceptions/summarize_logs.py

import csv
from pathlib import Path

logs_folder = Path(__file__).parent / "logs"

# --- Task 2: skip and count ---
# Some rows hold a value that is not a number, like ERR. Skip such a row, count it in
# `skipped`, and keep going. Put the mean of the good values, rounded to 2 decimals,
# in `mean_bar`. Catch ValueError only. The last line of each log must look like:
#   run_02: mean 7.71 bar, 1 rows skipped

for path in sorted(logs_folder.glob("*.csv")):
    pressures_bar = []
    skipped = 0

    with open(path, newline="") as file:
        for row in csv.DictReader(file):
            pressures_bar.append(row["pressure_bar"])

    mean_bar = ...
    print(f"{path.stem}: mean {mean_bar} bar, {skipped} rows skipped")
