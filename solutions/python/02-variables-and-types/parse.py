# Reference solution for the challenge in exercise 02.

BAR_TO_PSI = 14.5038

for text in ["7.5 bar", "108.8 psi", "3 atm"]:
    value_text, unit = text.split()
    value = float(value_text)
    if unit == "bar":
        print(f"{value} bar = {value * BAR_TO_PSI:.2f} psi")
    elif unit == "psi":
        print(f"{value} psi = {value / BAR_TO_PSI:.2f} bar")
    else:
        print(f"Unknown unit {unit!r} in {text!r}. Use bar or psi.")
