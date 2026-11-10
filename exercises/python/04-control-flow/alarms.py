# Control flow: classify readings against alarm limits.
# Run from the repo root:
#   uv run python exercises/python/04-control-flow/alarms.py

PRESSURE_WARNING_BAR = 8.0
PRESSURE_ALARM_BAR = 8.5

pressures_bar = [7.1, 7.6, 8.1, 8.4, 8.7, 7.9, 8.6, 7.3]

# --- if / elif / else ---
pressure = 8.1
# TODO 1: print "ALARM" if pressure is above PRESSURE_ALARM_BAR,
# "WARNING" if it is above PRESSURE_WARNING_BAR, and "OK" otherwise.
# Try the values 7.0, 8.2 and 9.0.

# --- for loop and range ---
# TODO 2: use a for loop to print every pressure with its classification.
# Example line: 8.1 bar -> WARNING
for pressure in pressures_bar:
    pass  # replace this line

# TODO 3: print the numbers 1 to 5 with a for loop and range(1, 6).

# --- enumerate: index and value together ---
# TODO 4: print "Reading 1: 7.1" ... for every pressure.
# Hint: for number, pressure in enumerate(pressures_bar, start=1):

# --- counting ---
alarm_count = 0
# TODO 5: count how many readings are above PRESSURE_ALARM_BAR.
# Add 1 to alarm_count inside the loop with alarm_count += 1.
print("Alarms:", alarm_count)

# --- while loop ---
# The pressure rises 0.4 bar per minute. How many minutes until the alarm limit?
level = 7.0
minutes = 0
# TODO 6: use a while loop: while level is not above PRESSURE_ALARM_BAR,
# add 0.4 to level and 1 to minutes.
print("Minutes to alarm:", minutes)

# --- break and continue ---
# TODO 7 (optional): loop over the pressures. Skip (continue) readings below 8.0.
# Stop (break) at the first reading above PRESSURE_ALARM_BAR and print it.
