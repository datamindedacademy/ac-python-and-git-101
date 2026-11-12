# 01 - Your first script

**Words to use:** interpreter, script, notebook, cell, kernel, PATH, virtual environment.

## Goal

Run a Python script from PowerShell and from VS Code. Find out which Python ran it. Find out how a notebook can show a result that nobody can reproduce.

## Why this matters

Most "it works on my laptop but not on yours" problems come down to which Python ran the script. Checking which one ran takes one command and can save hours. Whether you hand over a script or a notebook decides if a colleague gets the same result when they run your work.

## Background

- **Python** is the programming language. The **interpreter** is the program that reads your `.py` file and runs it, line by line.
- A **script** is a text file with Python code. You run it with one command and it runs from top to bottom.
- A **notebook** (`.ipynb`) is a document made of cells. You run cells one at a time and see the result under each cell. The **kernel** is the Python process that keeps the variables between cells.
- The module `sys` knows about the running interpreter: `sys.version` is a text with its version and build details, and `sys.executable` is the path of the `python.exe` that runs your script.
- **PATH** is a list of folders. When you type a command, Windows looks in these folders to find the program.
- **uv** manages Python for you. It installed Python 3.13 and it creates the `.venv` folder, a private Python environment for this repo. `uv run` always uses that environment.

All commands below are for **PowerShell**, run from the **repo root** (the folder `ac-python-and-git-101`). Check where you are with `pwd`.

## Tasks

### Task 1: run a script

Run `exercises/python/01-first-script/hello.py` from PowerShell and from VS Code. In VS Code use the Run button (the triangle at the top right of the editor). If VS Code asks for an interpreter, press `Ctrl+Shift+P`, type `Python: Select Interpreter` and choose the one that ends in `.venv`.

```powershell
uv run python exercises/python/01-first-script/hello.py
```

Change the script so that it greets you by name and prints the Python version and the path of the `python.exe` that ran it. Compare that path with what `Get-Command python` shows. Are they the same?

```text
Hello, Ada!
Compressor: CB-0042
Average pressure in bar: 7.233333333333333
Python version: 3.13.0 (main, Oct 16 2024, 00:33:24) [MSC v.1929 64 bit (AMD64)]
Python runs from: C:\path\to\ac-python-and-git-101\.venv\Scripts\python.exe
```

(Your name, the version text and the path differ. The version starts with `3.13`. The path must end in `.venv\Scripts\python.exe`.)

### Task 2: hidden state in a notebook

This one is much harder.

Open `exercises/python/01-first-script/first_notebook.ipynb` in VS Code and select the `.venv` kernel at the top right. Run the cells. Then get the notebook into a state where one cell shows a result that **Restart** followed by **Run All** does not give. Write in the last cell of the notebook why that happens.

Rules:

- Do not edit the code of the cell that shows the wrong result.
- Do not edit the data in the first code cell. Add a cell if you need one.

## Open question

`uv run python hello.py` starts in a fraction of a second. What happens between pressing Enter and the first line of your script running? Which part of that work does Python save for next time, and where? (Look for a folder called `__pycache__` after exercise 05.)
