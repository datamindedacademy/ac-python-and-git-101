# Reference solution for exercise 02.

BAR_TO_PSI = 14.5038
ALARM_LIMIT_BAR = 7.0

# --- Task 1: text to numbers ---
pressure_text = "7.5 bar"
temperature_text = "82 degC"

pressure_bar = float(pressure_text.split()[0])
pressure_psi = pressure_bar * BAR_TO_PSI
print(f"Pressure: {pressure_bar:.2f} bar = {pressure_psi:.2f} psi")

temperature_c = float(temperature_text.split()[0])
temperature_k = temperature_c + 273.15
print(f"Temperature: {temperature_c:.2f} degC = {temperature_k:.2f} K")

# --- Task 2: read an error ---
# The broken line was: print("Pressure: " + pressure_bar)
print("Pressure: " + str(pressure_bar) + " bar")

# --- Task 3: a full reading ---
reading_line = "2026-01-15 09:00:00;P1;108.8 psi;179.6 degF"

timestamp_text, sensor, psi_text, degf_text = reading_line.split(";")
date_text, time_text = timestamp_text.split(" ")
reading_bar = float(psi_text.split(" ")[0]) / BAR_TO_PSI
reading_c = (float(degf_text.split(" ")[0]) - 32) * 5 / 9
above_limit = reading_bar > ALARM_LIMIT_BAR

print(f"Sensor {sensor} at {time_text} on {date_text}")
print(f"Pressure: {reading_bar:.2f} bar")
print(f"Temperature: {reading_c:.2f} degC")
print("Above limit:", above_limit)
