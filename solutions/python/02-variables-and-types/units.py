# Reference solution for exercise 02.

BAR_TO_PSI = 14.5038
ALARM_LIMIT_BAR = 7.0

# --- Task 1: text to numbers ---
pressure_text = "7.5 bar"
temperature_text = "82 degC"

pressure_bar = float(pressure_text.removesuffix(" bar"))
pressure_psi = pressure_bar * BAR_TO_PSI
print(f"Pressure: {pressure_bar:.2f} bar = {pressure_psi:.2f} psi")

temperature_c = float(temperature_text.removesuffix(" degC"))
temperature_k = temperature_c + 273.15
print(f"Temperature: {temperature_c:.2f} degC = {temperature_k:.2f} K")

# --- Task 2: read an error ---
# The broken line was: print("Pressure: " + pressure_bar)
print("Pressure: " + str(pressure_bar) + " bar")

# --- Task 3: a messy reading ---
raw_sensor = " p1 "
raw_pressure = "108,8 PSI  "
raw_temperature = "  179.6 degF"

sensor = raw_sensor.strip().upper()
reading_psi = float(raw_pressure.strip().removesuffix(" PSI").replace(",", "."))
reading_bar = reading_psi / BAR_TO_PSI
reading_f = float(raw_temperature.strip().removesuffix(" degF"))
reading_c = (reading_f - 32) * 5 / 9
above_limit = reading_bar > ALARM_LIMIT_BAR

print(f"Sensor {sensor}")
print(f"Pressure: {reading_bar:.2f} bar")
print(f"Temperature: {reading_c:.2f} degC")
print("Above limit:", above_limit)
