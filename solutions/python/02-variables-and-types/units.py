# Reference solution for exercise 02.

serial_number = "CB-0042"
pressure_bar = 7.5
temperature_c = 82
is_running = True

print(serial_number, type(serial_number))
print(pressure_bar, type(pressure_bar))
print(temperature_c, type(temperature_c))
print(is_running, type(is_running))

BAR_TO_PSI = 14.5038

pressure_psi = pressure_bar * BAR_TO_PSI
temperature_k = temperature_c + 273.15

print("Pressure in psi:", pressure_psi)
print("Temperature in K:", temperature_k)

message = f"Unit {serial_number} runs at {pressure_bar:.2f} bar and {temperature_c:.1f} C"
print(message)

print(serial_number.lower(), len(serial_number))

text_value = "7.8"
corrected_bar = float(text_value) + 0.2
print("Corrected:", corrected_bar)
print(int(7.9), str(7.9))  # int() cuts off the decimals, it does not round

is_alarm = pressure_bar > 8.0
print("Alarm:", is_alarm)
