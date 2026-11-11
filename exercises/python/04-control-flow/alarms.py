# Control flow: classify readings against alarm limits.
# Run from the repo root:
#   uv run python exercises/python/04-control-flow/alarms.py

PRESSURE_WARNING_BAR = 8.0
PRESSURE_ALARM_BAR = 8.5

pressures_bar = [7.1, 7.6, 8.1, 8.4, 8.7, 7.9, 8.6, 7.3]

# --- Task 1: classify every reading ---
# Print one line per reading, counting from 1, and then the number of alarms:
#   Reading 1: 7.1 bar -> OK
#   ...
#   Reading 8: 7.3 bar -> OK
#   Alarms: 2
# ALARM is above PRESSURE_ALARM_BAR, WARNING is above PRESSURE_WARNING_BAR, OK is the rest.


# --- Task 2: list comprehensions ---
# Print these two lines. Each list is one list comprehension.
#   Alarm readings: [8.7, 8.6]
#   In psi: [103.0, 110.2, 117.5, 121.8, 126.2, 114.6, 124.7, 105.9]
# 1 bar is 14.5038 psi. Round each value to 1 decimal.


# --- Task 3: alarm episodes ---
# See the README. No hints for this one.
trend_bar = [7.2, 8.1, 8.3, 8.2, 7.6, 8.4, 7.9, 8.2, 8.6, 8.9, 8.1, 7.8, 8.3, 8.5]
