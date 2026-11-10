# 08 - A uv project with a package

Time: about 20 minutes.

## Goal

Create a new Python project with uv, add a package, look at the files uv creates, and run a script that imports the package.

This exercise is different: you work **outside** this repo, in a scratch folder.

## Background

- A **package** is code written by somebody else that you can install and `import`, like `matplotlib` for plots.
- A **virtual environment** (the `.venv` folder) is a private copy of Python plus the packages for one project. Each project gets its own, so projects do not disturb each other.
- **`pyproject.toml`** is the project file. It lists the name, the Python version and the **dependencies** (the packages you asked for).
- **`uv.lock`** is the **lockfile**. It records the exact version of every package, including packages your packages need. With the same lockfile everybody installs exactly the same versions.
- `uv add` installs a package and records it in both files. `uv remove` undoes that. `uv sync` makes `.venv` match the lockfile. `uv run` runs a command inside the environment.
- Only install packages that are on the IT-approved list. `matplotlib` is. So are `numpy`, `pandas` and `requests`.

## Tasks

Work in PowerShell. Choose a place outside the repo, for example your user folder.

1. Create a scratch folder and a new project in it:

   ```powershell
   cd ~
   uv init pressure-demo
   cd pressure-demo
   ls
   ```

   You should see `main.py`, `pyproject.toml`, `README.md` and `.python-version`. There is no `.venv` yet.

2. Read the project file:

   ```powershell
   cat pyproject.toml
   ```

3. Add the package:

   ```powershell
   uv add matplotlib
   ```

   Run `ls` again. Now you also have `uv.lock` and `.venv`. Read `pyproject.toml` again: the `dependencies` list has a new line. Open `uv.lock` in VS Code and search for `matplotlib`. Notice that it also lists `numpy` and other packages. Those are dependencies of matplotlib.

4. Copy `plot_pressure.py` from this repo folder into your project and open it in VS Code. If your repo is in `~/Documents/ac-python-and-git-101` (adjust the path if you cloned it somewhere else):

   ```powershell
   Copy-Item ~/Documents/ac-python-and-git-101/exercises/python/08-uv-project/plot_pressure.py .
   code .
   ```

   Do TODO 1 to 4.

5. Run it, then look at the picture:

   ```powershell
   uv run python plot_pressure.py
   ls *.png
   ```

   Open `pressure.png` in VS Code (it shows images).

6. Try running it with plain `python`:

   ```powershell
   python plot_pressure.py
   ```

   Does it work? Why (not)? (Hint: this uses the Python on your PATH, which does not know about the `.venv`.)

7. Remove the package, see the error, then restore it:

   ```powershell
   uv remove matplotlib
   uv run python plot_pressure.py
   uv add matplotlib
   ```

8. Delete the environment and rebuild it from the lockfile, as a colleague would after cloning your project:

   ```powershell
   Remove-Item -Recurse -Force .venv
   uv sync
   uv run python plot_pressure.py
   ```

9. Select the `.venv` interpreter in VS Code (`Ctrl+Shift+P`, `Python: Select Interpreter`) and run the script with the Run button.

## Compare with pip

| | uv | pip + venv + requirements.txt |
|---|---|---|
| Create environment | `uv init`, or automatic with `uv run` | `python -m venv .venv`, then activate it |
| Activate | not needed, `uv run` does it | `.venv\Scripts\Activate.ps1`, which is blocked by the PowerShell policy on your laptop |
| Install a package | `uv add matplotlib` | `pip install matplotlib` |
| Record the dependency | automatic, in `pyproject.toml` | by hand, or `pip freeze > requirements.txt` |
| Exact versions of all packages | `uv.lock`, automatic | only if you freeze them yourself |
| Remove a package | `uv remove matplotlib`, also cleans the files | `pip uninstall matplotlib`, files not updated |
| Python version | `uv python install`, set in `.python-version` | you install it yourself |
| Speed | very fast | slower |

## Check yourself

- After step 3, `pyproject.toml` contains something like `dependencies = ["matplotlib>=3.10"]` (your version number may differ).
- After step 5, `pressure.png` shows a line with markers and a red dashed line at 8.5 bar.
- After step 8, the script works again without any `uv add`.

## Stretch

- Run `uv tree` to see which packages matplotlib pulled in.
- Add `requests` or `numpy` with `uv add` and use `numpy.mean(pressures_bar)` in the title of the plot.
- Run `uv add --dev pytest`. See that it goes in a separate `dev` group in `pyproject.toml`.
