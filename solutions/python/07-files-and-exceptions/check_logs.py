# Reference solution for task 3 in exercise 07.
# Usage: check_logs.py [--strict] [file ...]   (no files: all of logs/)

import csv
import sys
from pathlib import Path

MAX_BAD_SHARE = 0.2
logs_folder = Path(__file__).parent / "logs"


def read_pressures(path, strict):
    """Return (good pressures, number of bad rows) of one log."""
    pressures_bar = []
    bad = 0
    with open(path, newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                pressures_bar.append(float(row["pressure_bar"]))
            except ValueError as err:
                value = row["pressure_bar"]
                message = f"{path.name} line {reader.line_num}: cannot convert {value!r}"
                if strict:
                    raise ValueError(message) from err
                bad += 1
                print("Warning:", message)
    rows = len(pressures_bar) + bad
    if bad / rows > MAX_BAD_SHARE:
        limit = f"{MAX_BAD_SHARE:.0%}"
        raise ValueError(f"{path.name}: {bad} of {rows} rows are bad, the limit is {limit}")
    return pressures_bar, bad


strict = "--strict" in sys.argv
paths = [Path(arg) for arg in sys.argv[1:] if arg != "--strict"]
try:
    for path in paths or sorted(logs_folder.glob("*.csv")):
        pressures_bar, bad = read_pressures(path, strict)
        mean_bar = round(sum(pressures_bar) / len(pressures_bar), 2)
        print(f"{path.stem}: mean {mean_bar} bar, {bad} rows skipped")
except FileNotFoundError as err:
    sys.exit(f"File not found: {Path(err.filename).name}")
except ValueError as err:
    sys.exit(f"Error: {err}")
