# Reference solution for exercise 06.
#
# Usage:
#   uv run python solutions/python/06-standard-library/summarize_runs.py
#   (optional: add a runs folder and an output folder as two arguments)

import csv
import json
import math
import sys
from pathlib import Path

folder = Path(__file__).parent


def summarize_folder(runs_folder, output_folder):
    summaries = []

    for path in sorted(runs_folder.glob("*.csv")):
        pressures_bar = []
        temperatures_c = []

        with open(path, newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                pressures_bar.append(float(row["pressure_bar"]))
                temperatures_c.append(float(row["temperature_c"]))

        mean_bar = sum(pressures_bar) / len(pressures_bar)
        variance = sum((p - mean_bar) ** 2 for p in pressures_bar) / len(pressures_bar)
        std_bar = math.sqrt(variance)
        max_temperature_c = max(temperatures_c)

        print(f"{path.name}: {len(pressures_bar)} rows, mean pressure {round(mean_bar, 2)} bar")

        summaries.append(
            {
                "run": path.stem,
                "rows": len(pressures_bar),
                "pressure_mean_bar": round(mean_bar, 2),
                "pressure_std_bar": round(std_bar, 2),
                "temperature_max_c": round(max_temperature_c, 2),
            }
        )

    output_folder.mkdir(parents=True, exist_ok=True)
    with open(output_folder / "summary.json", "w") as file:
        json.dump(summaries, file, indent=2)

    # Optional: the same summaries as CSV.
    with open(output_folder / "summary.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=list(summaries[0].keys()), lineterminator="\n")
        writer.writeheader()
        writer.writerows(summaries)

    return summaries


if __name__ == "__main__":
    arguments = sys.argv[1:]
    if len(arguments) == 2:
        summarize_folder(Path(arguments[0]), Path(arguments[1]))
    else:
        summarize_folder(folder / "runs", folder / "output")
