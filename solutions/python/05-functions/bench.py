"""Helper functions for the test bench readings.

This file is a module: other scripts can import the functions from it.
"""

# How many of each unit make 1 bar.
UNITS_PER_BAR = {"bar": 1.0, "psi": 14.5038, "kPa": 100.0}


def parse_reading(text: str) -> tuple[float, str]:
    """Split a reading like "7.5 bar" into its value and its unit."""
    value, unit = text.replace(",", ".").split()
    return float(value), unit


def to_bar(value: float, unit: str = "bar") -> float:
    """Convert a pressure in bar, psi or kPa to bar."""
    return value / UNITS_PER_BAR[unit]


def summarize(values: list[float], decimals: int = 2) -> dict:
    """Return count, min, max, mean and median of the values, rounded."""
    if not values:
        return {"count": 0}
    ordered = sorted(values)
    middle = len(ordered) // 2
    if len(ordered) % 2 == 1:
        median = ordered[middle]
    else:
        median = (ordered[middle - 1] + ordered[middle]) / 2
    return {
        "count": len(values),
        "min": round(ordered[0], decimals),
        "max": round(ordered[-1], decimals),
        "mean": round(sum(values) / len(values), decimals),
        "median": round(median, decimals),
    }


def classify(pressure_bar, warning_bar=8.0, alarm_bar=8.5):
    """Return "OK", "WARNING" or "ALARM" for a pressure."""
    if pressure_bar >= alarm_bar:
        return "ALARM"
    if pressure_bar >= warning_bar:
        return "WARNING"
    return "OK"


if __name__ == "__main__":
    print(round(to_bar(108.8, "psi"), 4))
