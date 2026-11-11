# 08 - A uv project with a package

**Words to use:** package, dependency, transitive dependency, virtual environment, project file (`pyproject.toml`), lockfile (`uv.lock`), sync, inline script metadata.

## Goal

Make a uv project and see what uv creates. Run a script with its package without any project. Then keep an environment identical to what the lockfile says.

This exercise is different: you work **outside** this repo, in scratch folders.

## Why this matters

A script that only runs on your own laptop is not a tool yet. The project file and the lockfile let a colleague, a build server or you in a year run it with the same package versions.

## Background

- A **package** is code written by somebody else that you can install and `import`, like `matplotlib` for plots.
- A **virtual environment** (the `.venv` folder) is a private copy of Python plus the packages for one project.
- **`pyproject.toml`** lists the **dependencies**, the packages you asked for. **`uv.lock`** records the exact version of every package, including the ones your packages need.
- Plain pip needs a manual `venv`, activation and `requirements.txt`. uv does all three for you.
- `uv sync` makes `.venv` match the project. `uv sync --locked` stops with an error when `uv.lock` is out of date compared with `pyproject.toml`. `uv sync --frozen` does not look at `pyproject.toml` at all and installs what `uv.lock` says.
- Only install packages that are on the IT-approved list. `matplotlib` is. So are `numpy`, `pandas` and `requests`.

## Tasks

Stuck on a task? The hints are in `HINTS.md` in this folder.

Work in PowerShell. `plot_pressure.py` in this exercise folder already draws the picture, you only run it.

### Task 1: a project

Make a new uv project called `pressure-demo` in your home folder. `uv init` also creates a Git repository and some starter files there. Ignore them for now. Add matplotlib. Copy `plot_pressure.py` into the project and run it with uv. End with a `pressure.png` in the project folder that shows a pressure line with round markers and a red dashed alarm line at 8.5 bar. Say what `pyproject.toml`, `uv.lock` and `.venv` are for.

```text
Saved pressure.png
```

### Task 2: one script, no project

Make the same script run from an **empty folder** with no project, so it can be mailed around as one file. The script must carry its own dependency list. Check by running it in the empty folder.

```text
Saved pressure.png
```

### Task 3: the same environment, from the lockfile

This one is much harder. There is no hint.

Go back to the project of task 1. Do these things with uv commands only, and answer the questions from the output:

- Which package requires `tzdata`, and which package brought that one in?
- Pin matplotlib to the minor version 3.9 (any 3.9.x, nothing newer), so that `uv.lock` records 3.9.x.
- Delete `.venv`. Rebuild it so it holds the locked matplotlib, without touching `uv.lock`.
- Now change the matplotlib line in `pyproject.toml` by hand to the minor version 3.10 (any 3.10.x) and do not run `uv lock`. Run `uv sync` three ways, in this order: one that stops with an error because `uv.lock` is out of date, one that installs the old locked 3.9.x anyway, and one that updates the lockfile and the environment to 3.10.x.

Output, with your own version numbers (the three syncs in order):

```text
tzdata v2026.6
└── python-dateutil v4.0.0
    └── matplotlib v3.11.2
        └── pressure-demo v0.1.0

3.9.4
error: The lockfile at `uv.lock` needs to be updated, but `--locked` was provided.
3.9.4
 - matplotlib==3.9.4
 + matplotlib==3.10.9
3.10.9
```

Rules:

- Do not edit `uv.lock` by hand.
- Do not use `uv pip`.
- Print the matplotlib version with `uv run python -c "import matplotlib; print(matplotlib.__version__)"`. `uv run` syncs the environment before it runs. After the second sync, check the version in a way that does not sync.

## Open question

Package A needs `numpy` below version 2 and package B needs `numpy` 2 or higher. What does `uv add` do when you ask for both, and why can no tool give you both in one environment? `uv.lock` also stores a hash for every package. What is that hash for?
