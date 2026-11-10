"""Print the mean discharge pressure and temperature of a run."""

import csv
from pathlib import Path

from conversions import bar_to_psi, celsius_to_kelvin


def main():
    with Path("measurements.csv").open() as file:
        rows = list(csv.DictReader(file))
    pressures = [float(row["discharge_pressure_bar"]) for row in rows]
    temperatures = [float(row["discharge_temperature_c"]) for row in rows]
    mean_bar = sum(pressures) / len(pressures)
    mean_c = sum(temperatures) / len(temperatures)
    print(f"Mean pressure: {mean_bar:.2f} bar ({bar_to_psi(mean_bar):.2f} psi)")
    print(f"Mean temperature: {mean_c:.1f} C ({celsius_to_kelvin(mean_c):.2f} K)")


if __name__ == "__main__":
    main()
