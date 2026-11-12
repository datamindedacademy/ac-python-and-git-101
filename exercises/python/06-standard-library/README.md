# 06 - The standard library: math, pathlib, csv, json

**Words to use:** standard library, import, path, glob pattern, header, DictReader, DictWriter, JSON, command-line argument.

## Goal

Use a few modules that come with Python. Write your first **automation script**: it loops over all CSV logs in a folder, reads each one, and writes files with the results.

## Why this matters

This is the main outcome of the day: work you now do by hand for each file is done by one script for a whole folder of test-bench logs. Everything used here ships with Python, so there is nothing extra to install or get approved.

## Background

- The **standard library** is the set of modules that ship with Python. You do not install them. You only `import` them.
- `math` has maths tools: `math.sqrt`, `math.pi`, `math.isclose` and more.
- `pathlib` gives you `Path` objects for file paths. Join paths with `/`: `folder / "data.csv"`. This works on Windows and Linux, so never type `\` in a path yourself.
- `folder.glob("*.csv")` lists all files in a folder that match a pattern. `path.name` is `run_01.csv`, `path.stem` is `run_01`.
- `csv.DictReader` reads a CSV file and gives you every row as a dict, with the header names as keys.
- `json` saves and loads data in the JSON format: a text format for dicts, lists, numbers and text. `json.dump(data, file, indent=2)` writes `data` to an open file, with line breaks and 2 spaces of indentation. `json.load(file)` reads it back.
- `csv.DictWriter` writes dicts as rows. It needs the column names, and the file opened for writing (`"w"`):

  ```python
  rows = [{"run": "run_01", "rows": 8}, {"run": "run_02", "rows": 8}]
  with open(path, "w", newline="") as file:
      writer = csv.DictWriter(file, fieldnames=["run", "rows"])
      writer.writeheader()
      writer.writerows(rows)
  ```
- `with open(path, newline="") as file:` opens a file for reading and closes it for you when the block ends. `open(path, "w")` opens it for writing and replaces what was there.
- `some_folder.mkdir(exist_ok=True)` creates a folder, and does nothing when it already exists. Writing a file into a folder that does not exist fails.
- `sys.argv` is the list of words typed after the script name. `sys.argv[0]` is the script itself, `sys.argv[1]` the first argument. It holds text.

## Tasks

Open `exercises/python/06-standard-library/summarize_runs.py`. The folder `runs/` holds three test-run logs: one row per minute, with a `timestamp`, `pressure_bar` and `temperature_c` column. Each task states the output to reach. Run with:

```powershell
uv run python exercises/python/06-standard-library/summarize_runs.py
```

### Task 1: one file

Read `runs/run_01.csv` and print its number of rows, its mean pressure and its max pressure.

```text
Rows: 8
Mean pressure: 7.25 bar
Max pressure: 7.5 bar
```

### Task 2: every file

Do the same for every CSV file in `runs/`, and write the results to `output/summary.json`: a list with one object per run. The `output/` folder may not exist yet. Open the file in VS Code and read it. The folder is ignored by Git.

```text
Wrote 3 summaries to output/summary.json
```

The first object of `summary.json`:

```json
{
  "run": "run_01",
  "rows": 8,
  "pressure_mean_bar": 7.25,
  "pressure_max_bar": 7.5
}
```

### Task 3: find the odd run

This one is much harder.

Compare every run with all the other runs, and flag the runs that do not fit. For one run: take the readings of all the other runs together, and calculate their mean and their standard deviation (divide by the number of readings). The deviation of the run is its mean pressure minus the mean of the others, divided by the standard deviation of the others. Flag the run when the deviation is above a threshold, in either direction.

Write `output/outliers.csv`, with one row per run, sorted from the largest deviation to the smallest (ignore the sign). Print a line for every flagged run. The runs folder is the first command-line argument and the threshold the second. Both are optional: the defaults are the `runs/` folder and 1.8.

```text
Flagged: run_01 (-1.85 standard deviations, limit 1.8)
```

`output/outliers.csv`:

```text
run,mean_bar,others_mean_bar,deviation_std,flagged
run_01,7.25,7.61,-1.85,True
run_02,7.73,7.37,1.74,False
run_03,7.49,7.49,0.0,False
```

Run it with a different threshold, to see more runs flagged:

```powershell
uv run python exercises/python/06-standard-library/summarize_runs.py exercises/python/06-standard-library/runs 1.5
```

Rules:

- Only `math`, `csv`, `json`, `sys` and `pathlib`. No `statistics`, no pandas.
- Write the CSV with `csv.DictWriter`.
- Adding a fourth file to `runs/` must work without changing the code.

## Open question

Your script reads each log completely into memory. How would you summarise a 50 GB log on a laptop with 16 GB of memory, with only the standard library? Can you still get the standard deviation if you may read every row only once?
