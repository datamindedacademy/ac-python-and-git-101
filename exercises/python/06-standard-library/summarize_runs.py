# Work with the CSV test-run logs in the runs/ folder.
# Run from the repo root:
#   uv run python exercises/python/06-standard-library/summarize_runs.py

# Add the imports you need (csv, json, math, sys ...).
from pathlib import Path

# Path(__file__) is the path of this script. .parent is its folder.
# Building paths this way works on Windows and Linux, from any folder.
folder = Path(__file__).parent
runs_folder = folder / "runs"
output_folder = folder / "output"

# Task 1: read runs/run_01.csv and print its number of rows, its mean pressure
# and its max pressure. Every value from a CSV is text.

# Task 2: do the same for every CSV file in runs_folder, and write one JSON file,
# output/summary.json, with one object per run. Create the output folder if needed.

# Task 3: flag the runs that differ from the other runs. See the README.
