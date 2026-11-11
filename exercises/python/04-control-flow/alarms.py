# Control flow: classify readings against alarm limits.
# Run from the repo root:
#   uv run python exercises/python/04-control-flow/alarms.py

PRESSURE_WARNING_BAR = 8.0
PRESSURE_ALARM_BAR = 8.5

pressures_bar = [7.1, 7.6, 8.1, 8.4, 8.7, 7.9, 8.6, 7.3]

# --- if / elif / else ---
pressure = 8.1
# TODO 1: print the class of pressure as one word:
#   ALARM when it is above PRESSURE_ALARM_BAR,
#   WARNING when it is above PRESSURE_WARNING_BAR,
#   OK otherwise.
# With 8.1 it prints WARNING. Try 7.0 (OK) and 9.0 (ALARM) too.

# --- for loop ---
# TODO 2: print every pressure in pressures_bar with its class, one line each, like:
#   8.1 bar -> WARNING
# The class must come from the same rules as TODO 1.

# TODO 3 (optional): print the numbers 1 to 5, one per line.

# --- enumerate: index and value together ---
# TODO 4: print every pressure with its number, counting from 1, one line each, like:
#   Reading 1: 7.1

# --- counting ---
alarm_count = 0
# TODO 5: make alarm_count the number of readings above PRESSURE_ALARM_BAR.
print("Alarms:", alarm_count)

# --- building a list: loop and list comprehension ---
# TODO 8: fill alarm_readings with all readings above PRESSURE_ALARM_BAR, in a loop.
# Then fill alarm_readings_short with the same readings, in one line, as a list comprehension.
# Both lists must read [8.7, 8.6].
alarm_readings = []
print("Alarm readings (loop):", alarm_readings)
alarm_readings_short = ...
print("Alarm readings (comprehension):", alarm_readings_short)

# --- while loop ---
# The pressure rises 0.4 bar per minute, starting at 7.0 bar.
level = 7.0
minutes = 0
# TODO 6 (optional): count the minutes until level is above PRESSURE_ALARM_BAR.
# Update level and minutes until then. The result is 4 minutes.
print("Minutes to alarm:", minutes)

# --- break and continue ---
# TODO 7 (optional): print the first reading above PRESSURE_ALARM_BAR as:
#   First alarm reading: 8.7
# Skip readings below 8.0 on the way, and stop at the first alarm.
