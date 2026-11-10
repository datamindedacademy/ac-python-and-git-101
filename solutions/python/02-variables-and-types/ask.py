# Reference solution for exercise 02, task 8.

BAR_TO_PSI = 14.5038

text = input("Pressure in bar: ")
pressure_bar = float(text)
print(f"{pressure_bar} bar is {pressure_bar * BAR_TO_PSI:.1f} psi")
