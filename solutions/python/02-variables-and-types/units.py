# Reference solution for exercise 02.

serial_number = "CB-0042"
pressure_text = "7.5 bar"
temperature_text = "82"
BAR_TO_PSI = 14.5038
ALARM_LIMIT_BAR = 8.0

print(serial_number, type(serial_number))
print(pressure_text, type(pressure_text))
print(temperature_text, type(temperature_text))

temperature_c = float(temperature_text)
temperature_k = temperature_c + 273.15
print("Temperature in K:", temperature_k)

parts = pressure_text.split()
pressure_bar = float(parts[0])
unit = parts[1]
print(pressure_bar, type(pressure_bar))
print(unit, type(unit))

pressure_psi = pressure_bar * BAR_TO_PSI
print("Pressure in psi:", pressure_psi)

message = (
    f"Unit {serial_number} runs at {pressure_bar:.2f} bar "
    f"({pressure_psi:.2f} psi) and {temperature_k:.2f} K"
)
print(message)

is_alarm = pressure_bar > ALARM_LIMIT_BAR
print("Alarm:", is_alarm)
