# Reference solution for the challenge in exercise 06.
# The first half (the folder from sys.argv) is also in summarize_runs.py.
#
# Usage:
#   uv run python solutions/python/06-standard-library/challenge.py <runs-folder>

import csv
import statistics
import sys
from pathlib import Path

LIMIT_STD_BAR = 0.18

runs_folder = Path(sys.argv[1])

for path in sorted(runs_folder.glob("*.csv")):
    with open(path, newline="") as file:
        pressures_bar = [float(row["pressure_bar"]) for row in csv.DictReader(file)]
    std_bar = round(statistics.pstdev(pressures_bar), 2)
    print(f"{path.name}: standard deviation {std_bar} bar")
    if std_bar > LIMIT_STD_BAR:
        print(
            f"Warning: {path.stem} has a pressure standard deviation of {std_bar} bar "
            f"(limit {LIMIT_STD_BAR})"
        )
