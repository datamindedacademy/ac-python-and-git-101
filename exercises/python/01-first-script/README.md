# 01 - Your first script

Time: about 15 minutes.

## Goal

Run a Python script from PowerShell and from VS Code. Find out where Python lives on your laptop. Compare a script with a notebook.

## Background

- **Python** is the programming language. The **interpreter** is the program that reads your `.py` file and runs it, line by line.
- A **script** is a text file with Python code. You run it with one command and it runs from top to bottom.
- A **notebook** (`.ipynb`) is a document made of cells. You run cells one at a time and see the result under each cell.
- **PATH** is a list of folders. When you type a command, Windows looks in these folders to find the program.
- **uv** manages Python for you. It installed Python 3.13 and it creates the `.venv` folder, a private Python environment for this repo. `uv run` always uses that environment.

All commands below are for **PowerShell**, run from the **repo root** (the folder `ac-python-and-git-101`). Check where you are with `pwd`.

## Tasks

1. Check the Python version:

   ```powershell
   uv run python --version
   ```

2. Find out where Python lives. These commands show which `python` Windows finds on your PATH and which Pythons uv knows about:

   ```powershell
   Get-Command python
   uv python list
   ```

   Write down the path you see. Is it the same as the one in `.venv`? (Hint: run `uv run python -c "import sys; print(sys.executable)"`.)

3. Open `exercises/python/01-first-script/hello.py` in VS Code. Do the three TODOs.

4. Run it from PowerShell:

   ```powershell
   uv run python exercises/python/01-first-script/hello.py
   ```

5. Run it from VS Code. Press the Run button (the triangle at the top right of the editor). If VS Code asks for an interpreter, press `Ctrl+Shift+P`, type `Python: Select Interpreter` and choose the one that ends in `.venv`.

6. Try the REPL, the interactive Python prompt. Type this and press Enter after each line:

   ```powershell
   uv run python
   ```

   ```python
   >>> 7.2 + 7.4
   >>> "bar" * 3
   >>> exit()
   ```

7. Open `first_notebook.ipynb` in VS Code. Select the `.venv` kernel at the top right. Fill in the TODO and run both code cells with `Shift+Enter`.

8. Fill in the table: write two advantages and two disadvantages for each way of working.

   | | Advantages | Disadvantages |
   |---|---|---|
   | Script | | |
   | Notebook | | |

## Check yourself

Step 4 should print:

```text
Hello, test engineer!
Compressor: CB-0042
Average pressure in bar: 7.233333333333334
```

(Your greeting may differ. The last digits of the average can differ slightly.)

## Stretch

- Print the average rounded to 2 decimals with `round(average_bar, 2)`.
- Use `uv run python -c "print(2 + 2)"` to run a single line without a file. When is that handy?
