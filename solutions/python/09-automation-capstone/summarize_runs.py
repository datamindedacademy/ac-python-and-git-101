# Reference solution for the capstone.
#
# Usage:
#   uv run python solutions/python/09-automation-capstone/summarize_runs.py
#   (optional: add a data folder and an output folder as two arguments)
#
# By default it reads the CSV files in the exercise folder
# and writes to the output/ folder next to this script.

import csv
import json
import sys
from pathlib import Path

FOLDER = Path(__file__).parent
DEFAULT_DATA_FOLDER = FOLDER.parents[2] / "exercises" / "python" / "09-automation-capstone" / "data"
DEFAULT_OUTPUT_FOLDER = FOLDER / "output"

PRESSURE_ALARM_BAR = 8.5
TEMPERATURE_ALARM_C = 95.0


def parse_row(row):
    """Convert one CSV row (a dict of text) into a dict of numbers.

    Raise ValueError when a value is missing or is not a number.
    """
    try:
        return {
            "pressure_bar": float(row["pressure_bar"]),
            "temperature_c": float(row["temperature_c"]),
        }
    except TypeError as error:
        # A row with too few columns gives None values.
        raise ValueError("incomplete row") from error


def read_run(path):
    """Read one CSV file. Return (readings, skipped_rows)."""
    readings = []
    skipped_rows = 0
    with open(path, newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                readings.append(parse_row(row))
            except ValueError as error:
                skipped_rows += 1
                print(f"Warning: {path.name}, line {reader.line_num}: skipped ({error})")
    return readings, skipped_rows


def summarize_run(name, readings, skipped_rows):
    """Return a dict with the summary of one run."""
    pressures = [reading["pressure_bar"] for reading in readings]
    temperatures = [reading["temperature_c"] for reading in readings]

    alarm_count = 0
    for reading in readings:
        if (
            reading["pressure_bar"] > PRESSURE_ALARM_BAR
            or reading["temperature_c"] > TEMPERATURE_ALARM_C
        ):
            alarm_count += 1

    return {
        "run": name,
        "rows_used": len(readings),
        "rows_skipped": skipped_rows,
        "pressure_min_bar": round(min(pressures), 2),
        "pressure_max_bar": round(max(pressures), 2),
        "pressure_mean_bar": round(sum(pressures) / len(pressures), 2),
        "temperature_max_c": round(max(temperatures), 1),
        "alarm_count": alarm_count,
    }


def write_csv(summaries, path):
    """Write the summaries to a CSV file."""
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = list(summaries[0].keys()) if summaries else []
    with open(path, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(summaries)


def write_json(summaries, skipped_files, path):
    """Write the summaries and the list of skipped files to a JSON file."""
    path.parent.mkdir(parents=True, exist_ok=True)
    result = {"runs": summaries, "skipped_files": skipped_files}
    with open(path, "w") as file:
        json.dump(result, file, indent=2)


def main(data_folder=DEFAULT_DATA_FOLDER, output_folder=DEFAULT_OUTPUT_FOLDER):
    summaries = []
    skipped_files = []

    for path in sorted(data_folder.glob("*.csv")):
        readings, skipped_rows = read_run(path)
        if not readings:
            print(f"Warning: {path.name} has no usable rows, file skipped")
            skipped_files.append(path.name)
            continue
        summaries.append(summarize_run(path.stem, readings, skipped_rows))

    write_csv(summaries, output_folder / "summary.csv")
    write_json(summaries, skipped_files, output_folder / "summary.json")
    print(f"Summarised {len(summaries)} runs, skipped {len(skipped_files)} files.")


if __name__ == "__main__":
    arguments = sys.argv[1:]
    if len(arguments) == 2:
        main(Path(arguments[0]), Path(arguments[1]))
    else:
        main()
