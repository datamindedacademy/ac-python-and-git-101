# Reading and writing text files, and handling errors.
# Run from the repo root:
#   uv run python exercises/python/07-files-and-exceptions/files_and_exceptions.py

from pathlib import Path

folder = Path(__file__).parent
input_path = folder / "pressures.txt"
missing_path = folder / "does_not_exist.txt"
output_path = folder / "output" / "report.txt"

# --- Part 1: read a text file ---
# TODO 1: open input_path with `with open(input_path) as file:`
# and read all lines with file.readlines(). Store them in `lines`.
lines = []
print("Lines read:", len(lines))

# --- Part 2: convert lines to numbers, handle bad lines ---
pressures_bar = []
bad_lines = []
for line in lines:
    text = line.strip()  # removes the newline at the end
    # TODO 2: put the next two steps in try/except ValueError:
    #   try:    pressures_bar.append(float(text))
    #   except ValueError:  append text to bad_lines
    pass

print("Good values:", pressures_bar)
print("Bad lines:", bad_lines)

# --- Part 3: a missing file ---
# TODO 3: try to open missing_path. Catch FileNotFoundError and
# print "File not found: <name>" (use missing_path.name) instead of crashing.

# --- Part 4: write a text file ---
# TODO 4: create the folder output_path.parent (mkdir with exist_ok=True).
# Then open output_path with "w" and write one line per good pressure:
#   Reading 1: 7.1 bar
# Hint: file.write(f"Reading {number}: {value} bar\n")
print("Wrote", output_path)

# --- Part 5 (optional): append ---
# TODO 5 (optional): open output_path again with "a" (append) and add the line:
#   Bad lines: 2
# Then read the file back and print it with print(output_path.read_text()).
