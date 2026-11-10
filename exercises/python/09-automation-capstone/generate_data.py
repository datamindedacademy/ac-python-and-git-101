"""Generate the fictional test-run logs in the data/ folder.

You do NOT need to run this script. The CSV files are already committed.
It is here so you can see where the data comes from. The random numbers are
seeded, so running it again gives exactly the same files.

    uv run python exercises/python/09-automation-capstone/generate_data.py
"""

import csv
import random
from datetime import datetime, timedelta
from pathlib import Path

HEADER = ["timestamp", "pressure_bar", "temperature_c", "flow_l_s", "power_kw"]
ROWS_PER_RUN = 20

# base pressure, base temperature, and the minutes where a spike happens
RUNS = {
    "run_01": {"pressure": 7.2, "temperature": 80.0, "spikes": []},
    "run_02": {"pressure": 7.6, "temperature": 84.0, "spikes": [8, 9, 10]},
    "run_03": {"pressure": 7.4, "temperature": 82.0, "spikes": []},
    "run_04": {"pressure": 7.0, "temperature": 88.0, "spikes": [15]},
    "run_05": {"pressure": 7.3, "temperature": 81.0, "spikes": []},
    "run_06": {"pressure": 7.5, "temperature": 83.0, "spikes": []},
}


def make_rows(run_number, settings):
    rng = random.Random(1000 + run_number)
    start = datetime(2026, 1, 12 + run_number, 9, 0, 0)
    rows = []
    for minute in range(ROWS_PER_RUN):
        pressure = settings["pressure"] + rng.uniform(-0.3, 0.3)
        temperature = settings["temperature"] + minute * 0.15 + rng.uniform(-0.8, 0.8)
        if minute in settings["spikes"]:
            pressure += 1.4
            temperature += 9.0
        flow = 5.7 * pressure + rng.uniform(-0.5, 0.5)
        power = 7.6 * pressure + rng.uniform(-0.4, 0.4)
        timestamp = start + timedelta(minutes=minute)
        rows.append(
            [
                timestamp.strftime("%Y-%m-%d %H:%M:%S"),
                f"{pressure:.2f}",
                f"{temperature:.1f}",
                f"{flow:.1f}",
                f"{power:.1f}",
            ]
        )
    return rows


def main():
    data_folder = Path(__file__).parent / "data"
    data_folder.mkdir(exist_ok=True)

    for number, (name, settings) in enumerate(RUNS.items(), start=1):
        rows = make_rows(number, settings)

        if name == "run_03":
            rows[6][1] = "ERR"  # a sensor wrote text instead of a number
        if name == "run_05":
            rows[11][2] = ""  # a missing temperature
        if name == "run_06":
            rows = []  # a log with a header and no data at all

        path = data_folder / f"{name}.csv"
        with open(path, "w", newline="") as file:
            writer = csv.writer(file, lineterminator="\n")
            writer.writerow(HEADER)
            writer.writerows(rows)
        print("Wrote", path.name, f"({len(rows)} rows)")


if __name__ == "__main__":
    main()
