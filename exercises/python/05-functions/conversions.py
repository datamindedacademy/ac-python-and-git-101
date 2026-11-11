"""Helper functions to convert units on the test bench.

This file is a module: other scripts can import the functions from it.
The tests in test_conversions.py describe what each function must do.
"""

BAR_TO_PSI = 14.5038


def l_s_to_m3_h(flow_l_s):
    """Convert a flow from litres per second to cubic metres per hour."""
    # This one is done for you as an example: 1 l/s is 3.6 m3/h.
    return flow_l_s * 3.6


def bar_to_psi(pressure_bar):
    """Convert a pressure from bar to psi."""
    # TODO 1: return the pressure in psi, using the constant BAR_TO_PSI above.
    # Worked number: 2 bar is 29.0076 psi.
    return 0.0


def celsius_to_kelvin(temperature_c):
    """Convert a temperature from degrees Celsius to kelvin."""
    # TODO 2: return the temperature in kelvin.
    # Worked number: 0 C is 273.15 K.
    return 0.0


def average(values, decimals=2):
    """Return the average of a list of numbers, rounded to `decimals` decimals."""
    # TODO 3: return the mean of the values, rounded to `decimals` decimals.
    # Worked number: [7.1, 7.2, 7.4] gives 7.23, and 7.2 with decimals=1.
    return 0.0


# TODO 4: write the function psi_to_bar here.
# Write its test in test_conversions.py FIRST and see it fail.
