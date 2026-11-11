# 06 - The standard library: math, pathlib, csv, json

**Words to use:** standard library, import, path, glob pattern, header, DictReader, JSON, context manager (`with`).

## Goal

Use four modules that come with Python. Write your first **automation script**: it loops over all CSV logs in a folder, reads each one, and writes one summary file.

## Why this matters

This is the main outcome of the day: work you now do by hand for each file is done by one script for a whole folder of test-bench logs. Everything used here ships with Python, so there is nothing extra to install or get approved.

## Background

- The **standard library** is the set of modules that ship with Python. You do not install them. You only `import` them.
- `math` has maths tools: `math.sqrt`, `math.pi`, `math.isclose` and more.
- `pathlib` gives you `Path` objects for file paths. Join paths with `/`: `folder / "data.csv"`. This works on Windows and Linux, so never type `\` in a path yourself.
- `folder.glob("*.csv")` lists all files in a folder that match a pattern. `path.name` is `run_01.csv`, `path.stem` is `run_01`.
- `csv.DictReader` reads a CSV file and gives you every row as a dict, with the header names as keys.
- `json` saves and loads data in the JSON format: a text format for dicts, lists, numbers and text.
- `with open(path, newline="") as file:` opens a file and closes it for you when the block ends.

## Core tasks

1. Open one file in the `runs/` folder (for example `run_01.csv`). It is a test-run log: one row per minute. There are three logs. How many rows and columns does each have?
2. Open `summarize_runs.py`. Read the whole script first. It loops over the files, and for each file it reads the rows. Do TODO 1 to 6.
3. Run it from the repo root:

   ```powershell
   uv run python exercises/python/06-standard-library/summarize_runs.py
   ```

4. Open the new file `exercises/python/06-standard-library/output/summary.json` in VS Code and read it. The `output/` folder is ignored by Git.

## Check yourself

The script prints three lines like this:

```text
run_01.csv: 8 rows, mean pressure 7.25 bar
```

and `summary.json` is a list of three objects. The first one looks like this:

```json
{
  "run": "run_01",
  "rows": 8,
  "pressure_mean_bar": 7.25,
  "pressure_std_bar": 0.2,
  "temperature_max_c": 82.7
}
```

## Optional: if you have time

- Add a fourth CSV file to `runs/` (copy one and change a number). Run the script again. The summary has four entries without changing the code. That is the point of automation.
- Also write the summaries to `output/summary.csv` with `csv.DictWriter`. Use `writer.writeheader()` and `writer.writerows(summaries)`.
- Use `math.isclose(a, b, rel_tol=1e-3)` to compare two floats. Why is it safer than `==`?
- Read `summary.json` back with `json.load` and print the run with the highest mean pressure.

### With Copilot

Ask Copilot Chat: *"Rewrite the mean and the standard deviation in this script with the `statistics` module from the standard library."* Run it and compare the standard deviation with your own. The module has `stdev` (sample) and `pstdev` (population). Which one did Copilot pick, and which one matches your formula? Would you have noticed the difference without your own version?

## Challenge

For those who finish early. There are no TODOs and no hints.

Change `summarize_runs.py` in two ways:

1. It takes the folder with the runs as a command-line argument (`sys.argv`) instead of the fixed `runs/` folder.
2. It prints a warning for every run whose pressure standard deviation is above a limit that you choose, for example:

```text
Warning: run_01 has a pressure standard deviation of 0.2 bar (limit 0.18)
```

## Open question

This goes beyond today. Most people cannot answer it yet. Try it anyway, or bring it to the trainer.

Your script reads each log completely into memory. How would you summarise a 50 GB log on a laptop with 16 GB of memory, with only the standard library? Can you still get the standard deviation if you may read every row only once?
