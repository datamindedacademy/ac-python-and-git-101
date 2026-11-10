# Reference solution for the optional task in exercise 07.

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
            try:
                pressures_bar.append(float(row["pressure_bar"]))
            except ValueError:
                skipped += 1
                print(f"Warning: {path.name}: bad value {row['pressure_bar']!r} skipped")

    mean_bar = round(sum(pressures_bar) / len(pressures_bar), 2)
    lines.append(f"{path.stem}: mean {mean_bar} bar, {skipped} rows skipped")

output_path.parent.mkdir(exist_ok=True)
output_path.write_text("\n".join(lines) + "\n")
print("\n".join(lines))
