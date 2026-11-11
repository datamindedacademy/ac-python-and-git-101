# 08 - A uv project with a package

**Words to use:** package, dependency, transitive dependency, virtual environment, project file (`pyproject.toml`), lockfile (`uv.lock`), sync.

## Goal

Create a new Python project with uv, add a package, look at the files uv creates, and run a script that imports the package.

This exercise is different: you work **outside** this repo, in a scratch folder.

## Why this matters

A script that only runs on your own laptop is not a tool yet. The project file and the lockfile let a colleague, a build server or you in a year run it with the same package versions.

## Background

- A **package** is code written by somebody else that you can install and `import`, like `matplotlib` for plots.
- A **virtual environment** (the `.venv` folder) is a private copy of Python plus the packages for one project. Each project gets its own, so projects do not disturb each other.
- **`pyproject.toml`** is the project file. It lists the name, the Python version and the **dependencies** (the packages you asked for).
- **`uv.lock`** is the **lockfile**. It records the exact version of every package, including packages your packages need. With the same lockfile everybody installs exactly the same versions.
- uv has one command each to add a package, remove it, rebuild the environment from the lockfile, show the dependency tree and run a command inside the environment. The hints show them.
- Only install packages that are on the IT-approved list. `matplotlib` is. So are `numpy`, `pandas` and `requests`.

## Tasks

Work in PowerShell. Try each step with the hint closed first. Open the hint when you are stuck.

1. Make a new project called `pressure-demo` in your home folder, and go into it. Look at what is in the folder. There is no `.venv` yet.

   <details>
   <summary>Hint for step 1</summary>

   ```powershell
   cd ~
   uv init pressure-demo
   cd pressure-demo
   ls
   ```

   </details>

   `uv init` also creates a Git repository in this folder, so you will see a hidden `.git` folder and a `.gitignore` file. Ignore them for now. Git is explained this afternoon.

2. Add matplotlib to the project. Then answer three questions:
   - In which file is the dependency recorded?
   - In which file is the exact version pinned?
   - How many packages came along that you did not ask for?

   <details>
   <summary>Hint for step 2</summary>

   Run `uv add matplotlib`. Run `ls` again and open `pyproject.toml` and `uv.lock` in VS Code. In `uv.lock`, search for `[[package]]`: every package has one block. The project itself has a block too.

   </details>

3. Copy `plot_pressure.py` from this repo folder into your project and open the project in VS Code. If your repo is in `~/Documents/ac-python-and-git-101` (adjust the path if you cloned it somewhere else):

   ```powershell
   Copy-Item ~/Documents/ac-python-and-git-101/exercises/python/08-uv-project/plot_pressure.py .
   code .
   ```

   Do the TODO in the file. It describes the picture to draw. Matplotlib is a day 2 topic, so you get hints. Asking Copilot for this plot with the right words is a valid way to do it, as long as you read what comes back and understand each line.

   <details>
   <summary>Hint 1 for the plot: the functions</summary>

   You need these functions from `plt`: `plt.plot`, `plt.axhline`, `plt.xlabel`, `plt.ylabel`, `plt.title`, `plt.legend`, `plt.savefig`. Look up their arguments with Copilot or in the matplotlib documentation. `marker`, `color`, `linestyle`, `label` and `dpi` are the ones to find.

   </details>

   <details>
   <summary>Hint 2 for the plot: the full code</summary>

   ```python
   plt.plot(minutes, pressures_bar, marker="o", label="Pressure")
   plt.axhline(alarm_limit_bar, color="red", linestyle="--", label="Alarm limit")
   plt.xlabel("Time (min)")
   plt.ylabel("Pressure (bar)")
   plt.title("Test run CB-0042")
   plt.legend()
   plt.savefig(output_file, dpi=150)
   ```

   </details>

4. Run the script inside the project. Then look at the picture: open `pressure.png` in VS Code (it shows images).

   <details>
   <summary>Hint for step 4</summary>

   ```powershell
   uv run python plot_pressure.py
   ls *.png
   ```

   </details>

5. Run the script with plain `python plot_pressure.py`. Does it work? Say why it fails or works.

6. Show the dependency tree and say which package pulled in `numpy`.

   <details>
   <summary>Hint for step 6</summary>

   Run `uv tree`.

   </details>

7. Remove matplotlib from the project and run the script again. Name the exception. Then add the package back.

   <details>
   <summary>Hint for step 7</summary>

   ```powershell
   uv remove matplotlib
   uv run python plot_pressure.py
   uv add matplotlib
   ```

   </details>

8. Delete the `.venv` folder. Restore it with one command, as a colleague would after cloning your project, and run the script again.

   <details>
   <summary>Hint for step 8</summary>

   ```powershell
   Remove-Item -Recurse -Force .venv
   uv sync
   uv run python plot_pressure.py
   ```

   </details>

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

- Step 1: the folder holds `pyproject.toml`, `README.md`, `.python-version` and a starter script (`main.py`, or a `src` folder, depending on your uv version). There is no `.venv`.
- Step 2: the dependency is in `pyproject.toml`, in a line like `dependencies = ["matplotlib>=3.10"]` (your version number may differ). The exact versions are in `uv.lock`. About 10 packages came along (the number depends on the version).
- Step 4: the script prints `Saved pressure.png`, and `pressure.png` shows a line with round markers, a red dashed line at 8.5 bar, axis labels with units, the title and a legend.
- Step 5: `ModuleNotFoundError: No module named 'matplotlib'`, because the Python on your PATH does not know about the `.venv`. If it works on your laptop, that Python has its own matplotlib, which is not the one of the project.
- Step 6: `matplotlib` asks for `numpy`, and so does `contourpy`, which matplotlib needs.
- Step 7: `ModuleNotFoundError: No module named 'matplotlib'`.
- Step 8: the script works again without any `uv add`.

## Optional: if you have time

1. Select the `.venv` interpreter in VS Code (`Ctrl+Shift+P`, `Python: Select Interpreter`) and run the script with the Run button.
2. Add `numpy` with `uv add` and use `numpy.mean(pressures_bar)` in the title of the plot.
3. Add pytest as a development dependency. See that it goes in a separate `dev` group in `pyproject.toml`. (Look up the flag with `uv add --help`.)

### With Copilot

Ask Copilot Chat: *"What is the difference between `uv add`, `uv sync` and `uv pip install` in a project with a lockfile?"* Check one claim from the answer yourself with `uv help add` or by looking at `pyproject.toml` and `uv.lock` before and after. Which of the three commands should you use in a project like this one, and which one would silently leave the lockfile out of date?

## Challenge

For those who finish early. There are no TODOs and no hints.

In your `pressure-demo` project, copy in `conversions.py` and `test_conversions.py` from exercise 05 (your own versions, with all tests green there). Add pytest as a development dependency with `uv add --dev pytest`. Get `uv run pytest` green in the new project.

## Open question

This goes beyond today. Most people cannot answer it yet. Try it anyway, or bring it to the trainer.

Package A needs `numpy` below version 2 and package B needs `numpy` 2 or higher. What does `uv add` do when you ask for both, and why can no tool give you both in one environment? `uv.lock` also stores a hash for every package. What is that hash for?
