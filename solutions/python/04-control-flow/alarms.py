# Reference solution for exercise 04.

PRESSURE_WARNING_BAR = 8.0
PRESSURE_ALARM_BAR = 8.5

pressures_bar = [7.1, 7.6, 8.1, 8.4, 8.7, 7.9, 8.6, 7.3]


def classify(pressure):
    if pressure > PRESSURE_ALARM_BAR:
        return "ALARM"
    elif pressure > PRESSURE_WARNING_BAR:
        return "WARNING"
    else:
        return "OK"


for test_value in [7.0, 8.2, 9.0]:
    print(test_value, classify(test_value))

for pressure in pressures_bar:
    print(f"{pressure} bar -> {classify(pressure)}")

for number in range(1, 6):
    print(number)

for number, pressure in enumerate(pressures_bar, start=1):
    print(f"Reading {number}: {pressure}")

alarm_count = 0
for pressure in pressures_bar:
    if pressure > PRESSURE_ALARM_BAR:
        alarm_count += 1
print("Alarms:", alarm_count)

level = 7.0
minutes = 0
while level <= PRESSURE_ALARM_BAR:
    level += 0.4
    minutes += 1
print("Minutes to alarm:", minutes)

for pressure in pressures_bar:
    if pressure < 8.0:
        continue
    if pressure > PRESSURE_ALARM_BAR:
        print("First alarm reading:", pressure)
        break

# Stretch
alarm_readings = [p for p in pressures_bar if p > PRESSURE_ALARM_BAR]
share = len(alarm_readings) / len(pressures_bar) * 100
print(f"Share in alarm: {share:.1f} %")
