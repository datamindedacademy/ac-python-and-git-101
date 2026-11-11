# Your first Python script.
# Run it from PowerShell, from the repo root:
#   uv run python exercises/python/01-first-script/hello.py
import sys

serial_number = "CB-0042"
pressures_bar = [7.2, 7.4, 7.1]
average_bar = sum(pressures_bar) / len(pressures_bar)

print("Hello, test engineer!")
print("Compressor:", serial_number)
print("Average pressure in bar:", average_bar)

# --- Task 1 ---
# Make the first line greet you by name. Then add two lines that print the Python version
# and the path of the python.exe that runs this script.
