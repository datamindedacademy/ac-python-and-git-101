# Reference solution for task 2 in exercise 07.

import csv
from pathlib import Path

logs_folder = Path(__file__).parent / "logs"

for path in sorted(logs_folder.glob("*.csv")):
    pressures_bar = []
    skipped = 0

    with open(path, newline="") as file:
        for row in csv.DictReader(file):
            try:
                pressures_bar.append(float(row["pressure_bar"]))
            except ValueError:
                skipped += 1

    mean_bar = round(sum(pressures_bar) / len(pressures_bar), 2)
    print(f"{path.stem}: mean {mean_bar} bar, {skipped} rows skipped")
