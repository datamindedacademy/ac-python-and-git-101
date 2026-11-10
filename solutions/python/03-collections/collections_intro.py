# Reference solution for exercise 03.

pressures_bar = [7.1, 7.3, 7.4, 7.2, 7.6, 7.5]

print("First:", pressures_bar[0])
print("Last:", pressures_bar[-1])
print("First three:", pressures_bar[0:3])

pressures_bar.append(7.8)
print("Number of readings:", len(pressures_bar))

mean_bar = sum(pressures_bar) / len(pressures_bar)
print("Max:", max(pressures_bar), "Min:", min(pressures_bar), "Mean:", mean_bar)

print("High to low:", sorted(pressures_bar, reverse=True))

position = (52.01, 4.36)
latitude, longitude = position
print("Latitude:", latitude, "Longitude:", longitude)

measurement = {
    "timestamp": "2026-01-15 09:00:00",
    "pressure_bar": 7.5,
    "temperature_c": 82.0,
}
print("Pressure:", measurement["pressure_bar"])
measurement["flow_l_s"] = 41.5
measurement["temperature_c"] = 83.5
for key, value in measurement.items():
    print(f"{key}: {value}")

measurements = [
    {"timestamp": "09:00", "pressure_bar": 7.1, "temperature_c": 80.5},
    {"timestamp": "09:01", "pressure_bar": 7.4, "temperature_c": 81.9},
    {"timestamp": "09:02", "pressure_bar": 7.6, "temperature_c": 83.2},
]
print("Temperature of second:", measurements[1]["temperature_c"])

only_pressures = []
for item in measurements:
    only_pressures.append(item["pressure_bar"])
print("Pressures:", only_pressures)

sensor_ids = ["P1", "T1", "P1", "F1", "T1", "P2"]
unique_ids = set(sensor_ids)
print("Unique sensors:", len(unique_ids))
print("F1 present:", "F1" in unique_ids)

# Stretch
print(measurement.get("humidity", "unknown"))
print([p for p in pressures_bar if p > 7.3])
