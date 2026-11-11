# Reference solution for exercise 06 (all three tasks).
#
# Usage:
#   uv run python solutions/python/06-standard-library/summarize_runs.py
#   (optional: a runs folder and a threshold in standard deviations)

import csv
import json
import math
import sys
from pathlib import Path

folder = Path(__file__).parent
runs_folder = Path(sys.argv[1]) if len(sys.argv) > 1 else folder / "runs"
threshold = float(sys.argv[2]) if len(sys.argv) > 2 else 1.8
output_folder = folder / "output"


def read_pressures(path):
    with open(path, newline="") as file:
        return [float(row["pressure_bar"]) for row in csv.DictReader(file)]


# Task 1: one file
pressures_bar = read_pressures(runs_folder / "run_01.csv")
print(f"Rows: {len(pressures_bar)}")
print(f"Mean pressure: {round(sum(pressures_bar) / len(pressures_bar), 2)} bar")
print(f"Max pressure: {max(pressures_bar)} bar")

# Task 2: every file, one JSON summary
pressures_by_run = {path.stem: read_pressures(path) for path in sorted(runs_folder.glob("*.csv"))}
summaries = [
    {
        "run": run,
        "rows": len(values),
        "pressure_mean_bar": round(sum(values) / len(values), 2),
        "pressure_max_bar": max(values),
    }
    for run, values in pressures_by_run.items()
]
output_folder.mkdir(exist_ok=True)
with open(output_folder / "summary.json", "w") as file:
    json.dump(summaries, file, indent=2)
print(f"Wrote {len(summaries)} summaries to output/summary.json")

# Task 3: compare each run with all the other runs
rows = []
for run, values in pressures_by_run.items():
    others = [p for other, vs in pressures_by_run.items() if other != run for p in vs]
    others_mean = sum(others) / len(others)
    others_std = math.sqrt(sum((p - others_mean) ** 2 for p in others) / len(others))
    mean = sum(values) / len(values)
    deviation = (mean - others_mean) / others_std
    rows.append(
        {
            "run": run,
            "mean_bar": round(mean, 2),
            "others_mean_bar": round(others_mean, 2),
            "deviation_std": round(deviation, 2),
            "flagged": abs(deviation) > threshold,
        }
    )
rows.sort(key=lambda row: abs(row["deviation_std"]), reverse=True)
with open(output_folder / "outliers.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=list(rows[0].keys()), lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
for row in rows:
    if row["flagged"]:
        print(
            f"Flagged: {row['run']} ({row['deviation_std']} standard deviations, "
            f"limit {threshold})"
        )
