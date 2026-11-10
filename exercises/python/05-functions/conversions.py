"""Helper functions to convert units on the test bench.

This file is a module: other scripts can import the functions from it.
"""

BAR_TO_PSI = 14.5038


def bar_to_psi(pressure_bar):
    """Convert a pressure from bar to psi."""
    # TODO 1: return pressure_bar multiplied by BAR_TO_PSI.
    return 0.0


def celsius_to_kelvin(temperature_c):
    """Convert a temperature from degrees Celsius to kelvin."""
    # TODO 2: return temperature_c plus 273.15.
    return 0.0


def l_s_to_m3_h(flow_l_s):
    """Convert a flow from litres per second to cubic metres per hour."""
    # This one is done for you as an example: 1 l/s is 3.6 m3/h.
    return flow_l_s * 3.6


def average(values, decimals=2):
    """Return the average of a list of numbers, rounded to `decimals` decimals."""
    # TODO 4: return round(sum(values) / len(values), decimals)
    return 0.0


if __name__ == "__main__":
    # This block only runs when you run this file directly, not when you import it.
    # TODO 6: print bar_to_psi(7.5) here as a quick self-test.
    print("conversions.py was run directly")
