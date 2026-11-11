# Variables, types and conversions for a compressor test bench.
# The data arrives as text, as it does from a file.
# Run from the repo root:
#   uv run python exercises/python/02-variables-and-types/units.py

serial_number = "CB-0042"
pressure_text = "7.5 bar"
temperature_text = "82"
BAR_TO_PSI = 14.5038
ALARM_LIMIT_BAR = 8.0

# TODO 1: print each of the three text values above together with its type, one line each.
# The first line must read: CB-0042 <class 'str'>

# TODO 2: turn temperature_text into a number, keep it in temperature_c.
# Keep the temperature in kelvin in temperature_k and print it as: Temperature in K: 355.15
temperature_c = ...
temperature_k = ...

# TODO 3: split pressure_text into a number pressure_bar (a float) and a text unit.
# Print both, each followed by its type. The first line must read: 7.5 <class 'float'>
pressure_bar = ...
unit = ...

# TODO 4: convert pressure_bar to psi, keep it in pressure_psi.
# Print it as: Pressure in psi: 108.7785
pressure_psi = ...

# TODO 5: build one line of text in message and print it. It must read exactly:
#   Unit CB-0042 runs at 7.50 bar (108.78 psi) and 355.15 K
# Build it from the variables, not by typing the numbers.
message = ...

# TODO 6: make a boolean is_alarm that is True when pressure_bar is above ALARM_LIMIT_BAR.
# Print it as: Alarm: False
is_alarm = ...
