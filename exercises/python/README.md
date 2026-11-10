# Python exercises - day 1

Hands-on exercises for day 1 of the Python Programming and Data Analysis training. They assume no programming experience. All examples use one story: measurements from a (fictional) compressor test bench.

## Exercises

| # | Folder | Topic | Time |
|---|---|---|---|
| 01 | `01-first-script` | Run a script from PowerShell and VS Code, the REPL, where Python lives (PATH), script versus notebook | 15 min |
| 02 | `02-variables-and-types` | Variables, numbers, text, booleans, `type()`, conversions, f-strings, unit conversions | 15 min |
| 03 | `03-collections` | Lists, tuples, dicts and sets, indexing, slicing, methods | 20 min |
| 04 | `04-control-flow` | `if/elif/else`, `for`, `while`, `range`, `enumerate`, alarm limits | 20 min |
| 05 | `05-functions` | Functions, parameters, defaults, return values, docstrings, modules, `import` | 25 min |
| 06 | `06-standard-library` | `math`, `pathlib`, `csv`, `json`: read a CSV, compute statistics, write JSON | 25 min |
| 07 | `07-files-and-exceptions` | Text files, `try/except`, reading a traceback (3 broken scripts) | 25 min |
| 08 | `08-uv-project` | New uv project, `uv add`, `pyproject.toml`, `uv.lock`, `.venv`, comparison with pip | 20 min |
| 09 | `09-automation-capstone` | Process a folder of CSV logs and write a CSV and JSON summary | 35 min |

Total hands-on time: about 3 hours 20 minutes. The rest of the day is for setup (about 1 hour) and Git (about 2 hours).

Each folder has a `README.md` with the goal, background, numbered tasks, expected output and optional stretch tasks. Start every exercise by reading it.

## How to run

- Use **PowerShell** and work from the **repo root** (the folder `ac-python-and-git-101`). Check with `pwd`.
- Run a script with `uv run python <path-to-script>`:

  ```powershell
  uv run python exercises/python/01-first-script/hello.py
  ```

- Forward slashes in paths work in PowerShell. Press `Tab` to complete file names.
- `uv run` uses the project's `.venv`, so everybody has the same Python and packages.
- In VS Code, select the `.venv` interpreter (`Ctrl+Shift+P`, `Python: Select Interpreter`) and use the Run button.
- Files marked `# TODO` are for you to complete. Starter files run before you change them, but they print placeholders.
- Scripts that write files write them to an `output/` folder next to the script. Git ignores these folders.
- Stuck? Read the traceback from the bottom up. Then look in `solutions/python/<same-folder>/`. Try first, then peek.

## About the broken scripts

`07-files-and-exceptions/broken_1.py` to `broken_3.py` crash on purpose. That is the exercise.
