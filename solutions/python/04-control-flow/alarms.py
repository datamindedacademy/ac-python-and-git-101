# Reference solution for exercise 04.

PRESSURE_WARNING_BAR = 8.0
PRESSURE_ALARM_BAR = 8.5

pressures_bar = [7.1, 7.6, 8.1, 8.4, 8.7, 7.9, 8.6, 7.3]

# --- Task 1: classify every reading ---
alarm_count = 0
for number, pressure in enumerate(pressures_bar, start=1):
    if pressure > PRESSURE_ALARM_BAR:
        label = "ALARM"
        alarm_count += 1
    elif pressure > PRESSURE_WARNING_BAR:
        label = "WARNING"
    else:
        label = "OK"
    print(f"Reading {number}: {pressure} bar -> {label}")
print("Alarms:", alarm_count)

# --- Task 2: list comprehensions ---
alarm_readings = [p for p in pressures_bar if p > PRESSURE_ALARM_BAR]
pressures_psi = [round(p * 14.5038, 1) for p in pressures_bar]
print("Alarm readings:", alarm_readings)
print("In psi:", pressures_psi)

# --- Task 3: alarm episodes ---
trend_bar = [7.2, 8.1, 8.3, 8.2, 7.6, 8.4, 7.9, 8.2, 8.6, 8.9, 8.1, 7.8, 8.3, 8.5]

episodes = []  # each item: (start, end, length, peak), readings counted from 1
start = None
peak = 0.0
for number, pressure in enumerate(trend_bar, start=1):
    if pressure > PRESSURE_WARNING_BAR:
        if start is None:
            start = number
            peak = pressure
        peak = max(peak, pressure)
    elif start is not None:
        episodes.append((start, number - 1, number - start, peak))
        start = None
# An episode can still be open when the list ends.
if start is not None:
    episodes.append((start, len(trend_bar), len(trend_bar) - start + 1, peak))

if not episodes:
    print("No episodes")
else:
    longest = episodes[0]
    for i, episode in enumerate(episodes, start=1):
        first, last, length, high = episode
        print(f"Episode {i}: readings {first} to {last}, length {length}, peak {high}")
        if length > longest[2]:
            longest = episode
    print(f"Longest: readings {longest[0]} to {longest[1]}, {longest[2]} readings")
