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
            # TODO 1: put the conversion in try/except ValueError.
            # On success append the pressure. On failure add 1 to skipped
            # and print a warning with path.name.
            pressures_bar.append(row["pressure_bar"])

    # TODO 2: calculate the mean of pressures_bar and build the line below.
    mean_bar = ...
    lines.append(f"{path.stem}: mean {mean_bar} bar, {skipped} rows skipped")

# TODO 3: create the output folder and write the lines to output_path,
# one per line (use "\n".join(lines)).
print("\n".join(lines))
