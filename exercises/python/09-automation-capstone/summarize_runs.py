# Capstone: summarise all test-run logs in the data/ folder.
# Run from the repo root:
#   uv run python exercises/python/09-automation-capstone/summarize_runs.py
#
# Goal: read every CSV in data/, handle bad files and bad rows without crashing,
# and write output/summary.csv and output/summary.json.

import csv
import json
from pathlib import Path

FOLDER = Path(__file__).parent
DATA_FOLDER = FOLDER / "data"
OUTPUT_FOLDER = FOLDER / "output"

PRESSURE_ALARM_BAR = 8.5
TEMPERATURE_ALARM_C = 95.0


def parse_row(row):
    """Convert one CSV row (a dict of text) into a dict of numbers.

    Raise ValueError when a value is missing or is not a number.
    """
    # TODO 1: return a dict with the keys "pressure_bar" and "temperature_c",
    # each converted with float(row["..."]).
    # float("") and float("ERR") raise ValueError, that is what we want.
    # A short row gives None instead of text: float(None) raises TypeError.
    # Catch that too: raise ValueError("incomplete row") from it,
    # or use `except (ValueError, TypeError)` in the caller.
    return {"pressure_bar": 0.0, "temperature_c": 0.0}


def read_run(path):
    """Read one CSV file. Return (readings, skipped_rows).

    readings is a list of dicts from parse_row. skipped_rows is the number of bad rows.
    """
    readings = []
    skipped_rows = 0
    # TODO 2: open the file with csv.DictReader. For every row, call parse_row
    # inside try/except. On success, append the result to readings.
    # On failure, add 1 to skipped_rows and print a warning with the file name.
    return readings, skipped_rows


def summarize_run(name, readings, skipped_rows):
    """Return a dict with the summary of one run."""
    # TODO 3: calculate from readings:
    #   pressure min, max and mean (rounded to 2 decimals),
    #   the maximum temperature,
    #   the alarm count: number of readings with pressure above PRESSURE_ALARM_BAR
    #   OR temperature above TEMPERATURE_ALARM_C.
    return {
        "run": name,
        "rows_used": len(readings),
        "rows_skipped": skipped_rows,
        "pressure_min_bar": None,
        "pressure_max_bar": None,
        "pressure_mean_bar": None,
        "temperature_max_c": None,
        "alarm_count": None,
    }


def write_csv(summaries, path):
    """Write the summaries to a CSV file."""
    # TODO 4: create the output folder, then use csv.DictWriter.
    # fieldnames = the keys of the first summary. Call writeheader() and writerows().
    print("TODO: write", path)


def write_json(summaries, skipped_files, path):
    """Write the summaries and the list of skipped files to a JSON file."""
    # TODO 5: build {"runs": summaries, "skipped_files": skipped_files}
    # and write it with json.dump(..., indent=2).
    print("TODO: write", path)


def main():
    summaries = []
    skipped_files = []

    # sorted() gives a stable order. glob("*.csv") finds all CSV files in the folder.
    for path in sorted(DATA_FOLDER.glob("*.csv")):
        print("Found", path.name)
        # TODO 6: for every file:
        #   readings, skipped_rows = read_run(path)
        #   if there are no readings, add path.name to skipped_files, print a warning
        #   and continue. Otherwise append summarize_run(path.stem, readings, skipped_rows).

    write_csv(summaries, OUTPUT_FOLDER / "summary.csv")
    write_json(summaries, skipped_files, OUTPUT_FOLDER / "summary.json")
    print(f"Summarised {len(summaries)} runs, skipped {len(skipped_files)} files.")


if __name__ == "__main__":
    main()
