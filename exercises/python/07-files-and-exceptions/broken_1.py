# This script is broken on purpose. Run it, read the traceback and fix it.
#   uv run python exercises/python/07-files-and-exceptions/broken_1.py

pressures_bar = [7.1, 7.4, 7.6, 7.2]

total = 0
for pressure in pressures_bar:
    total = total + pressure

average_bar = total / len(pressures_bar)
print("Average pressure:", average_bar)
print("Highest pressure:", maximum_bar)
