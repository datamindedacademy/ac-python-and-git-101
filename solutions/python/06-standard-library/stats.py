# Reference solution for exercise 06.

import csv
import json
import math
from pathlib import Path

folder = Path(__file__).parent
csv_path = folder / "measurements.csv"
output_path = folder / "output" / "summary.json"

pressures_bar = []
temperatures_c = []
flows_l_s = []

with open(csv_path, newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        pressures_bar.append(float(row["pressure_bar"]))
        temperatures_c.append(float(row["temperature_c"]))
        flows_l_s.append(float(row["flow_l_s"]))

print("Rows read:", len(pressures_bar))

mean_bar = sum(pressures_bar) / len(pressures_bar)
variance = sum((p - mean_bar) ** 2 for p in pressures_bar) / len(pressures_bar)
std_bar = math.sqrt(variance)
max_temperature_c = max(temperatures_c)

print(f"Mean pressure: {mean_bar} bar")

summary = {
    "source_file": csv_path.name,
    "rows": len(pressures_bar),
    "pressure_mean_bar": round(mean_bar, 3),
    "pressure_std_bar": round(std_bar, 3),
    "temperature_max_c": round(max_temperature_c, 3),
    "flow_min_l_s": min(flows_l_s),
    "flow_max_l_s": max(flows_l_s),
}

output_path.parent.mkdir(exist_ok=True)
with open(output_path, "w") as file:
    json.dump(summary, file, indent=2)
print("Wrote", output_path)

with open(output_path) as file:
    loaded = json.load(file)
print("Mean pressure from file:", loaded["pressure_mean_bar"])
