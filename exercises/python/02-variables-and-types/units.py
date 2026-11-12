# Variables, types and conversions for a compressor test bench.
# The data arrives as text, as it does from a file.
# Run from the repo root:
#   uv run python exercises/python/02-variables-and-types/units.py
# No loop and no `if` is needed. They come in exercise 04.

BAR_TO_PSI = 14.5038
ALARM_LIMIT_BAR = 7.0

# --- Task 1: text to numbers ---
pressure_text = "7.5 bar"
temperature_text = "82 degC"
# Print these two lines. Build them from the text values above, not by typing the numbers.
#   Pressure: 7.50 bar = 108.78 psi
#   Temperature: 82.00 degC = 355.15 K


# --- Task 2: read an error ---
# See the README. Add the line there below this comment.


# --- Task 3: a messy reading ---
# See the README. Do not edit these three values.
raw_sensor = " p1 "
raw_pressure = "108,8 PSI  "
raw_temperature = "  179.6 degF"
