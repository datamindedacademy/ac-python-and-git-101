# Optional task: the folder script from exercise 06, now safe against bad values.
# One log in logs/ contains a value that is not a number.
# Run from the repo root:
#   uv run python exercises/python/07-files-and-exceptions/summarize_logs.py

import csv
from pathlib import Path

folder = Path(__file__).parent
logs_folder = folder / "logs"
output_path = folder / "output" / "log_summary.txt"

lines = []

for path in sorted(logs_folder.glob("*.csv")):
    pressures_bar = []
    skipped = 0

    with open(path, newline="") as file:
        for row in csv.DictReader(file):
            # TODO 1: a row with a value that is not a number is skipped.
            # Count it in `skipped` and print a warning that names the file.
            # A row with a good value adds its pressure, as a number, to pressures_bar.
            pressures_bar.append(row["pressure_bar"])

    # TODO 2: calculate the mean of pressures_bar, rounded to 2 decimals, in mean_bar.
    # run_01 gives 7.25 and run_02 gives 7.71 (one row skipped).
    mean_bar = ...
    lines.append(f"{path.stem}: mean {mean_bar} bar, {skipped} rows skipped")

# TODO 3: write the lines to output_path, one per line.
# The folder of output_path may not exist yet. Make sure it does.
print("\n".join(lines))
