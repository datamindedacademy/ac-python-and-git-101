"""Helper functions for the test bench readings.

This file is a module: other scripts can import the functions from it.
The tests in test_bench.py describe what each function must do.
"""

# How many of each unit make 1 bar.
UNITS_PER_BAR = {"bar": 1.0, "psi": 14.5038, "kPa": 100.0}


def parse_reading(text: str) -> tuple[float, str]:
    """Split a reading like "7.5 bar" into its value and its unit."""
    # Task 1: make test_parse_reading and its two friends pass.
    return 0.0, ""


def to_bar(value: float, unit: str = "bar") -> float:
    """Convert a pressure in bar, psi or kPa to bar."""
    # Done for you as an example: look the unit up in the dict.
    return value / UNITS_PER_BAR[unit]


def summarize(values: list[float], decimals: int = 2) -> dict:
    """Return count, min, max, mean and median of the values, rounded."""
    # Task 1: make the four test_summarize tests pass.
    return {}


# Task 2, part A: write the function classify here, after its tests fail.
# Write its tests in test_bench.py FIRST.
# Task 3 does not go in this file. See the README.
