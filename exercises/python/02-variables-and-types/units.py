# Variables, types and conversions for a compressor test bench.
# Run from the repo root:
#   uv run python exercises/python/02-variables-and-types/units.py

# --- Part 1: variables and types ---
serial_number = "CB-0042"
pressure_bar = 7.5
temperature_c = 82
is_running = True

print(serial_number, type(serial_number))
# TODO 1: print the type of the other three variables, like the line above.

# --- Part 2: unit conversions ---
BAR_TO_PSI = 14.5038

# TODO 2: convert pressure_bar to psi (multiply by BAR_TO_PSI).
pressure_psi = ...

# TODO 3: convert temperature_c to kelvin (add 273.15).
temperature_k = ...

print("Pressure in psi:", pressure_psi)
print("Temperature in K:", temperature_k)

# --- Part 3: strings and f-strings ---
# TODO 4: build this text with an f-string and print it:
#   Unit CB-0042 runs at 7.50 bar and 82.0 C
# Hint: {pressure_bar:.2f} shows 2 decimals.
message = ...
print(message)

# TODO 5: print serial_number in lower case and its length.
# Hint: serial_number.lower() and len(serial_number)

# --- Part 4: conversions between types ---
text_value = "7.8"
# TODO 6: convert text_value to a float and add 0.2 to it.
# Then convert int(7.9) and str(7.9) and print what you get. Is int() rounding?
corrected_bar = ...
print("Corrected:", corrected_bar)

# --- Part 5: booleans ---
# TODO 7: make a variable is_alarm that is True when pressure_bar is above 8.0.
is_alarm = ...
print("Alarm:", is_alarm)
