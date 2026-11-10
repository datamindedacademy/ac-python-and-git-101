# Fixed version of broken_1.py.
# Error: NameError: name 'maximum_bar' is not defined (line 12 of the broken file).
# The variable maximum_bar was never created. Python only knows names that you assigned before.

pressures_bar = [7.1, 7.4, 7.6, 7.2]

total = 0
for pressure in pressures_bar:
    total = total + pressure

average_bar = total / len(pressures_bar)
maximum_bar = max(pressures_bar)
print("Average pressure:", average_bar)
print("Highest pressure:", maximum_bar)
