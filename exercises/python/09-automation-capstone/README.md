# 09 - Capstone: automate a repetitive task

Time: about 35 minutes.

## Goal

Your team collects a CSV log for every compressor test run. Someone has to summarise each log by hand. You will write a script that does it for all files in seconds. It must survive bad data.

You use everything from today: functions, loops, `if`, `pathlib`, `csv`, `json`, `try/except`, and reading tracebacks.

## Background

- The folder `data/` has six logs: `run_01.csv` to `run_06.csv`. Columns: `timestamp`, `pressure_bar`, `temperature_c`, `flow_l_s`, `power_kw`. One row per minute.
- Real data is messy. Some logs have problems on purpose. Open the files in VS Code and try to find them before you write code.
- `Path.glob("*.csv")` lists the files in a folder that match a pattern.
- `path.stem` is the file name without the extension: `run_01`.
- `csv.DictWriter` writes dicts as CSV rows.
- A reading counts as an **alarm** when the pressure is above 8.5 bar **or** the temperature is above 95 degrees C.
- A **skipped row** is a row you could not read. Skip it, count it, print a warning, and keep going. Do not let one bad row stop the whole job.

You can see how the data was made in `generate_data.py`. You do not need to run it.

## Tasks

1. Inspect the six files. Write down which file has which problem.
2. Open `summarize_runs.py`. It has a stub for each step (TODO 1 to 6). Run it first. It should list the files without crashing:

   ```powershell
   uv run python exercises/python/09-automation-capstone/summarize_runs.py
   ```

3. Do the TODOs in order. Run after each step. Use `print` to check your values.
4. When you get a traceback, read it from the bottom up. Which line is yours?
5. Open `output/summary.csv` and `output/summary.json`. The `output/` folder is ignored by Git.
6. Check the results against the table below.

## Check yourself

`summary.csv` should have 5 rows, one for each readable run:

| run | rows_used | rows_skipped | alarm_count |
|---|---|---|---|
| run_01 | 20 | 0 | 0 |
| run_02 | 20 | 0 | 3 |
| run_03 | 19 | 1 | 0 |
| run_04 | 20 | 0 | 1 |
| run_05 | 19 | 1 | 0 |

`run_06.csv` has a header and no rows, so it appears in `skipped_files` in the JSON file. The last line of the script output is:

```text
Summarised 5 runs, skipped 1 files.
```

## Stretch

- Add the mean flow and the mean power to the summary.
- Print a warning for any run with more than 2 alarms.
- Make the data folder a command line argument: `uv run python ... summarize_runs.py some_folder`. Use `sys.argv`.
