# Hints: 06 - The standard library: math, pathlib, csv, json

Try the task first. Read a hint only when you are stuck.

## Hint for task 1

`with open(path, newline="") as file:` and `csv.DictReader(file)` give one dict per row. Every value is text, so use `float(row["pressure_bar"])` and collect the numbers in a list. Then `sum()`, `len()` and `max()`.

## Hint for task 2

`sorted(runs_folder.glob("*.csv"))` lists the files. Put your task 1 code in a `for path in ...` loop and use `path.stem` for the run name. Round the mean with `round(x, 2)`. `output_folder.mkdir(exist_ok=True)` makes the folder, then `json.dump(summaries, file, indent=2)` inside `with open(..., "w") as file:`.
