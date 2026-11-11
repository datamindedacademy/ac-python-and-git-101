# Python exercises - day 1

Hands-on exercises for day 1 of the Python Programming and Data Analysis training. They assume basic scripting experience, for example in MATLAB or VBA. You do not need to know Python. All examples use one story: measurements from a (fictional) compressor test bench.

## Exercises

| # | Folder | Topic | Why it matters |
|---|---|---|---|
| 01 | `01-first-script` | Run a script from PowerShell and VS Code, where Python lives (PATH), script versus notebook | Same Python for everyone, same result |
| 02 | `02-variables-and-types` | Variables, types, text to number, `split()`, f-strings, unit conversions, a first traceback | Wrong type or unit gives wrong numbers silently |
| 03 | `03-collections` | Lists, tuples, dicts and sets, indexing, slicing, sorting, no loops yet | Data structure decides how the script reads |
| 04 | `04-control-flow` | `if/elif/else`, `for`, `enumerate`, list comprehensions, alarm limits (`range` and `while` optional) | Core of automation, and of Copilot code |
| 05 | `05-functions` | Functions, parameters, defaults, return values, modules, `import`, your first tests with pytest (test first, red and green) | Functions and tests make code you can trust |
| 06 | `06-standard-library` | `math`, `pathlib`, `csv`, `json`: a script that summarises a folder of CSV logs | One script for a whole folder of logs |
| 07 | `07-files-and-exceptions` | Text files, `try/except`, reading a traceback (1 core broken script, 2 optional) | Bad rows and tracebacks in real logs |
| 08 | `08-uv-project` | New uv project, adding a package, `pyproject.toml`, `uv.lock`, `.venv`, a plot in a project, comparison with pip | Same package versions on every machine |

Exercise 05 introduces tests: you run tests that fail, write functions until they pass, and write one test yourself before the function exists. Day 3 covers pytest in depth.

Exercise 06 delivers the outcome "automate a repetitive task with a script that reads and writes files": it loops over all CSV logs in a folder and writes one summary file.

Every README has an **Optional: if you have time** section (extra tasks, more tracebacks, a folder script that survives bad data, and one task **With Copilot**). Do these only after the core tasks.

Exercises 02 to 08 have a **Challenge**: one open task for those who finish early. There are no TODOs and no hints.

In exercises 02 to 08 the TODOs state the result to reach, not the code. The hints are in the README of the exercise, under Tasks, in collapsed blocks. Try with the hint closed first. Open it when you are stuck. A reference solution is in `solutions/python/<same-folder>/`.

Each README has a **Why this matters** section after the goal. The last section is an **Open question** that goes beyond the day.

Exercise 04 teaches list comprehensions: a short way to build a list with one `for` and one `if`.

Every README starts with a **Words to use** line: the specialist terms of that exercise. Use them when you talk to the trainer and to Copilot.

## Using Copilot

You may use GitHub Copilot in VS Code during the whole training: the inline suggestions and Copilot Chat. No core task needs it, so you can do everything without it too.

AI can write the code. Your job is to ask for the right thing, to judge what comes back, and to choose between approaches. For that you need the vocabulary and the tradeoffs. That is what these exercises train.

- Use it freely.
- Ask it to explain an error or a line you do not understand.
- Ask for a second way to do something, and compare the two.
- Keep a line only when you understand what it does.
- You are the author of what you run and commit, whoever typed it.

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
- Files marked `# TODO` are for you to complete. A TODO says which result to reach, for example what must be printed. Work out the code yourself. If you are stuck, open the collapsed hint for that TODO in the README of the exercise.
- Starter files run before you change them, but they print placeholders or nothing.
- Scripts that write files write them to an `output/` folder next to the script. Git ignores these folders.
- Stuck? Read the traceback from the bottom up. Then look in `solutions/python/<same-folder>/`. Try first, then peek.

## About the broken scripts

`07-files-and-exceptions/broken_1.py` to `broken_3.py` crash on purpose. That is the exercise. `broken_1.py` is core. `broken_2.py` and `broken_3.py` are optional.
