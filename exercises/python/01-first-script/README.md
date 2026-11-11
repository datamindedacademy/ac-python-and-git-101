# 01 - Your first script

**Words to use:** interpreter, script, notebook, cell, kernel, PATH, virtual environment.

## Goal

Run a Python script from PowerShell and from VS Code. Find out where Python lives on your laptop. Compare a script with a notebook.

## Why this matters

Most "it works on my laptop but not on yours" problems come down to which Python ran the script. Checking which one ran takes one command and can save hours. Whether you hand over a script or a notebook decides if a colleague gets the same result when they run your work.

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

6. Open `first_notebook.ipynb` in VS Code. Select the `.venv` kernel at the top right. Fill in the TODO and run both code cells with `Shift+Enter`.

## Check yourself

Step 4 should print:

```text
Hello, test engineer!
Compressor: CB-0042
Average pressure in bar: 7.233333333333334
```

(Your greeting may differ. The last digits of the average can differ slightly.)

## Optional: if you have time

1. Try the REPL, the interactive Python prompt. Type this and press Enter after each line:

   ```powershell
   uv run python
   ```

   ```python
   >>> 7.2 + 7.4
   >>> "bar" * 3
   >>> exit()
   ```

2. Print the average rounded to 2 decimals with `round(average_bar, 2)`.
3. Use `uv run python -c "print(2 + 2)"` to run a single line without a file. When is that handy?

4. Fill in a table with two advantages and two disadvantages of a script and of a notebook. Compare with the solution notes.

### With Copilot

Open Copilot Chat and ask: *"Explain step by step what happens when I run `uv run python hello.py`. Use the terms interpreter, PATH and virtual environment."* Compare the answer with the Background section above. Did it use a word you do not know yet? Ask it to define that word. Is there a sentence in the answer that you cannot check yourself? How would you check it?

## Open question

This goes beyond today. Most people cannot answer it yet. Try it anyway, or bring it to the trainer.

`uv run python hello.py` starts in a fraction of a second. What happens between pressing Enter and the first line of your script running? Which part of that work does Python save for next time, and where? (Look for a folder called `__pycache__` after exercise 05.)
