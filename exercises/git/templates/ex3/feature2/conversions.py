"""Unit conversions for the compressor test bench."""

BAR_TO_PSI = 14.5
KELVIN_OFFSET = 273.15


def bar_to_psi(pressure_bar):
    """Convert a pressure from bar to psi."""
    return pressure_bar * BAR_TO_PSI


def celsius_to_kelvin(temperature_c):
    """Convert a temperature from degrees Celsius to Kelvin."""
    return temperature_c + KELVIN_OFFSET


def celsius_to_fahrenheit(temperature_c):
    """Convert a temperature from degrees Celsius to Fahrenheit."""
    return temperature_c * 9 / 5 + 32
