# Reference solution for exercise 07, part A.

from pathlib import Path

folder = Path(__file__).parent
input_path = folder / "pressures.txt"
missing_path = folder / "does_not_exist.txt"
output_path = folder / "output" / "report.txt"

with open(input_path) as file:
    lines = file.readlines()
print("Lines read:", len(lines))

pressures_bar = []
bad_lines = []
for line in lines:
    text = line.strip()
    try:
        pressures_bar.append(float(text))
    except ValueError:
        bad_lines.append(text)

print("Good values:", pressures_bar)
print("Bad lines:", bad_lines)

try:
    with open(missing_path) as file:
        file.read()
except FileNotFoundError:
    print("File not found:", missing_path.name)

output_path.parent.mkdir(exist_ok=True)
with open(output_path, "w") as file:
    for number, value in enumerate(pressures_bar, start=1):
        file.write(f"Reading {number}: {value} bar\n")
print("Wrote", output_path)

with open(output_path, "a") as file:
    file.write(f"Bad lines: {len(bad_lines)}\n")
print(output_path.read_text())
