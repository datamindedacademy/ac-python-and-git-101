"""Helper functions to convert units on the test bench.

This file is a module: other scripts can import the functions from it.
"""

BAR_TO_PSI = 14.5038


def bar_to_psi(pressure_bar):
    """Convert a pressure from bar to psi."""
    return pressure_bar * BAR_TO_PSI


def psi_to_bar(pressure_psi):
    """Convert a pressure from psi to bar."""
    return pressure_psi / BAR_TO_PSI


def celsius_to_kelvin(temperature_c):
    """Convert a temperature from degrees Celsius to kelvin."""
    return temperature_c + 273.15


def l_s_to_m3_h(flow_l_s):
    """Convert a flow from litres per second to cubic metres per hour."""
    return flow_l_s * 3.6


def average(values, decimals=2):
    """Return the average of a list of numbers, rounded to `decimals` decimals."""
    return round(sum(values) / len(values), decimals)


def classify(pressure, limit=8.5):
    """Return "ALARM" when the pressure is above the limit, else "OK"."""
    if pressure > limit:
        return "ALARM"
    return "OK"


if __name__ == "__main__":
    print(bar_to_psi(7.5))
