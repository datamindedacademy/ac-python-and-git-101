# Reference solution for the challenge in exercise 07.
# A bad value stops the script. Add --skip to skip bad rows instead.

import csv
import sys
from pathlib import Path

SKIP_BAD_ROWS = "--skip" in sys.argv

logs_folder = Path(__file__).parent / "logs"

for path in sorted(logs_folder.glob("*.csv")):
    pressures_bar = []
    skipped = 0

    with open(path, newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                pressures_bar.append(float(row["pressure_bar"]))
            except ValueError:
                bad = row["pressure_bar"]
                message = f"{path.name} line {reader.line_num}: cannot convert {bad!r}"
                if not SKIP_BAD_ROWS:
                    raise ValueError(message) from None
                skipped += 1
                print("Warning:", message)

    mean_bar = round(sum(pressures_bar) / len(pressures_bar), 2)
    print(f"{path.stem}: mean {mean_bar} bar, {skipped} rows skipped")
