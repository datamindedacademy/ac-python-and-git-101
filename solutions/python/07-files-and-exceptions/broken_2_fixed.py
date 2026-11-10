# Fixed version of broken_2.py.
# Error: TypeError: can only concatenate str (not "float") to str (line 8 of the broken file).
# You cannot add text and a number with +. Use an f-string, or convert with str().

serial_number = "CB-0042"
pressure_bar = 7.5
limit_bar = 8

message = f"Unit {serial_number} runs at {pressure_bar} bar"
print(message)

if pressure_bar < limit_bar:
    print("Pressure is below the limit")
