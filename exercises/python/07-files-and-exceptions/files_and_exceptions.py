# Reading and writing text files, and handling errors.
# Run from the repo root:
#   uv run python exercises/python/07-files-and-exceptions/files_and_exceptions.py

from pathlib import Path

folder = Path(__file__).parent
input_path = folder / "pressures.txt"
missing_path = folder / "does_not_exist.txt"
output_path = folder / "output" / "report.txt"

# --- Part 1: read a text file ---
# TODO 1: read all lines of input_path into `lines`, as a list of text lines.
# The next print must show: Lines read: 6
lines = []
print("Lines read:", len(lines))

# --- Part 2: convert lines to numbers, handle bad lines ---
pressures_bar = []
bad_lines = []
for line in lines:
    text = line.strip()  # removes the newline at the end
    # TODO 2: put the number of each line in pressures_bar. A line that is not a valid
    # number goes into bad_lines instead, as text, and the script must not crash.
    pass

print("Good values:", pressures_bar)
print("Bad lines:", bad_lines)

# --- Part 3: a missing file ---
# TODO 3: try to open missing_path. The file does not exist, but the script must not crash.
# Print this line instead: File not found: does_not_exist.txt
# Build the file name from missing_path.

# --- Part 4: write a text file ---
# TODO 4: write one line per good pressure to output_path, numbered from 1:
#   Reading 1: 7.1 bar
# The folder of output_path may not exist yet. Make sure it does.
print("Wrote", output_path)

# --- Part 5 (optional): append ---
# TODO 5 (optional): add one line to the end of output_path, without losing the other lines:
#   Bad lines: 2
# Then print the whole file. The count must come from bad_lines.
