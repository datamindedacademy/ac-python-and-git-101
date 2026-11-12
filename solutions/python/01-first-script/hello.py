# Reference solution for exercise 01.
import sys

serial_number = "CB-0042"
pressures_bar = [7.2, 7.4, 7.1]
average_bar = sum(pressures_bar) / len(pressures_bar)

print("Hello, Ada!")
print("Compressor:", serial_number)
print("Average pressure in bar:", average_bar)
print("Python version:", sys.version)
print("Python runs from:", sys.executable)
