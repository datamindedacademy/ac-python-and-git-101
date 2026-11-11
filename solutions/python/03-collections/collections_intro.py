# Reference solution for exercise 03.

timestamps = ["09:00", "09:01", "09:02", "09:03", "09:04", "09:05"]
pressures_bar = [7.1, 7.3, 7.4, 7.2, 7.6, 7.5]

# --- Task 1: lists ---
print("Last:", pressures_bar[-1])
print("Top three:", sorted(pressures_bar, reverse=True)[:3])
middle = sorted(pressures_bar)[1:-1]
print("Trimmed mean:", round(sum(middle) / len(middle), 3))

# --- Task 2: dicts, tuples and sets ---
measurements = [
    {"timestamp": "09:00", "sensor": "P1", "pressure_bar": 7.1},
    {"timestamp": "09:01", "sensor": "P2", "pressure_bar": 7.4},
    {"timestamp": "09:02", "sensor": "P1", "pressure_bar": 7.6},
]
position = (52.01, 4.36)  # latitude and longitude of the test hall
sensor_ids = ["P1", "T1", "P1", "F1", "T1", "P2"]

measurements.append({"timestamp": "09:03", "sensor": "P2", "pressure_bar": 7.3})
print("Measurements:", len(measurements))
print("Pressure of last:", measurements[-1]["pressure_bar"])
print("Unique sensors:", len(set(sensor_ids)))
latitude, longitude = position
print(f"Hall: {latitude} N, {longitude} E")

# --- Task 3: median and peak ---
# For an odd count both indexes point at the middle item.
# For an even count they point at the two middle items.
ordered = sorted(pressures_bar)
count = len(ordered)
median_all = (ordered[(count - 1) // 2] + ordered[count // 2]) / 2
print("Median of all six:", round(median_all, 3))

ordered = sorted(pressures_bar[:5])
count = len(ordered)
median_five = (ordered[(count - 1) // 2] + ordered[count // 2]) / 2
print("Median of first five:", round(median_five, 3))

peak_bar = max(pressures_bar)
peak_time = timestamps[pressures_bar.index(peak_bar)]
print(f"Peak: {peak_bar} bar at {peak_time}")
