# This script is broken on purpose. Run it, read the traceback and fix it.
#   uv run python exercises/python/07-files-and-exceptions/broken_2.py

serial_number = "CB-0042"
pressure_bar = 7.5
limit_bar = 8

message = "Unit " + serial_number + " runs at " + pressure_bar + " bar"
print(message)

if pressure_bar < limit_bar:
    print("Pressure is below the limit")
