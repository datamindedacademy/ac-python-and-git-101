# Reference solution for the challenge in exercise 03.

measurements = [
    {"timestamp": "09:00", "pressure_bar": 7.1, "temperature_c": 80.5},
    {"timestamp": "09:01", "pressure_bar": 7.4, "temperature_c": 81.9},
    {"timestamp": "09:02", "pressure_bar": 7.6, "temperature_c": 83.2},
    {"timestamp": "09:03", "pressure_bar": 7.3, "temperature_c": 82.4},
]

columns = {key: [item[key] for item in measurements] for key in measurements[0]}
print(columns)
