# Python exercises - day 1

All exercises use one story: measurements from a (fictional) compressor test bench.

| # | Folder | Topic | Why it matters |
|---|---|---|---|
| 01 | `01-first-script` | Run a script, where Python lives, script versus notebook | Same Python for everyone, same result |
| 02 | `02-variables-and-types` | Variables, types, string methods, text to number, f-strings, a first traceback | Wrong type or unit gives wrong numbers silently |
| 03 | `03-collections` | Lists, tuples, dicts and sets, indexing, slicing, sorting, splitting a line | Data structure decides how the script reads |
| 04 | `04-control-flow` | `if`, `for`, `enumerate`, list comprehensions | Core of automation, and of Copilot code |
| 05 | `05-functions` | Functions, modules, `import`, your first tests with pytest | Functions and tests make code you can trust |
| 06 | `06-standard-library` | `pathlib`, `csv`, `json`: summarise a folder of CSV logs | One script for a whole folder of logs |
| 07 | `07-files-and-exceptions` | Reading a traceback, `try/except`, skip a bad row or stop | Bad rows and tracebacks in real logs |
| 08 | `08-uv-project` | New uv project, a script with inline metadata, `pyproject.toml`, `uv.lock` | Same package versions on every machine |

## How an exercise works

Start with the `README.md` in the folder. It has these parts:

- **Words to use**: the terms of that exercise. Use them with the trainer and with Copilot.
- **Tasks**: two or three per exercise. Each states the result to reach, not the code. The last one is much harder. Most people will not finish it in class.
- **No hints**: use the Background section, the slides, `help()` or Copilot.
- **Open question**: goes beyond today. Most people cannot answer it yet. Try it, or bring it to the trainer.

A reference solution is in `solutions/python/<same-folder>/`. Try first, then look.

## How to run

Use PowerShell and work from the repo root (`ac-python-and-git-101`). Check with `pwd`.

```powershell
uv run python exercises/python/01-first-script/hello.py
```

- `uv run` uses the project's `.venv`, so everybody has the same Python and packages.
- In VS Code, select the `.venv` interpreter (`Ctrl+Shift+P`, `Python: Select Interpreter`) and use the Run button.
- Starter files run before you change them, but they print placeholders or nothing.
- Scripts that write files write them to an `output/` folder next to the script. Git ignores these folders.
- Stuck? Read the traceback from the bottom up.

## Using Copilot

You may use GitHub Copilot all day. No task needs it.

AI is a multiplier of experience. If you have zero experience, AI has nothing to multiply.

- Ask it to explain an error or a line you do not understand.
- Ask for a second way to do something, and compare the two.
- Keep a line only when you understand what it does. You are the author of what you run and commit.
