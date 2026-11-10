# Reference solution for exercise 01.

serial_number = "CB-0042"
pressures_bar = [7.2, 7.4, 7.1]

print("Hello, Ada!")
print("Compressor:", serial_number)

average_bar = (pressures_bar[0] + pressures_bar[1] + pressures_bar[2]) / 3

print("Average pressure in bar:", average_bar)

average_psi = average_bar * 14.5038
print("Average pressure in psi:", round(average_psi, 1))
print("Rounded:", round(average_bar, 2))
