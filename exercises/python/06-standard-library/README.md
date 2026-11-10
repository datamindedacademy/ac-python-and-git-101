# 06 - The standard library: math, pathlib, csv, json

Time: about 25 minutes.

## Goal

Use four modules that come with Python: read a measurement CSV, compute statistics, and write a JSON summary.

## Background

- The **standard library** is the set of modules that ship with Python. You do not install them. You only `import` them.
- `math` has maths tools: `math.sqrt`, `math.pi`, `math.isclose` and more.
- `pathlib` gives you `Path` objects for file paths. Join paths with `/`: `folder / "data.csv"`. This works on Windows and Linux, so never type `\` in a path yourself.
- `csv` reads and writes CSV files. `csv.DictReader` gives you every row as a dict, with the header names as keys.
- `json` saves and loads data in the JSON format: a text format for dicts, lists, numbers and text. Many tools and web services use it.
- `open(path, newline="")` opens a file. The `with` keyword closes it for you when the block ends.

## Tasks

1. Look at `measurements.csv` in this folder. How many rows and columns does it have?
2. Open `stats.py`. Do the TODOs from 1 to 6.
3. Run it from the repo root:

   ```powershell
   uv run python exercises/python/06-standard-library/stats.py
   ```

4. Open the new file `exercises/python/06-standard-library/output/summary.json` in VS Code and read it. This folder is ignored by Git, so it will not show up as a change.
5. Add `flow_l_s` to the summary: its minimum and maximum.

## Check yourself

The summary file should look like this:

```json
{
  "source_file": "measurements.csv",
  "rows": 10,
  "pressure_mean_bar": 7.43,
  "pressure_std_bar": 0.21,
  "temperature_max_c": 84.6
}
```

## Stretch

- Use `math.isclose(a, b, rel_tol=1e-3)` to compare two floats. Why is it safer than `==`?
- Write the rows with power above 57 kW to a new CSV with `csv.DictWriter`.
