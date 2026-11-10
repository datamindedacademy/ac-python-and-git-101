"""Unit conversions for the compressor test bench."""

BAR_TO_PSI = 14.5


def bar_to_psi(pressure_bar):
    """Convert a pressure from bar to psi."""
    return pressure_bar * BAR_TO_PSI
