# Solution notes - 08

## What you should see

After `uv init pressure-demo`:

```text
.git/  .gitignore  .python-version  README.md  main.py  pyproject.toml
```

After `uv add matplotlib`: the files `uv.lock` and `.venv/` appear, and `pyproject.toml` gets a line like:

```toml
dependencies = [
    "matplotlib>=3.10.0",
]
```

## Questions

- **Plain `python plot_pressure.py` (step 6)**: it uses the Python found on PATH. That Python usually has no matplotlib, so you get `ModuleNotFoundError: No module named 'matplotlib'`. `uv run` uses the project `.venv`, which has it.
- **After `uv remove`**: `uv run` reports the same `ModuleNotFoundError`, because the package is gone from the environment and from `pyproject.toml`.
- **Why delete `.venv` and run `uv sync`?** `.venv` can always be rebuilt from `pyproject.toml` and `uv.lock`. So you commit those two files to Git and do not commit `.venv`. `uv init` already created a `.gitignore` that excludes it.
- **Why does `uv.lock` list more than matplotlib?** matplotlib needs numpy, pillow and others. The lockfile pins them all, so a colleague gets exactly the same versions.

## Explain it: model answers

Your own words are fine. What matters is that you name the tradeoff.

**What breaks for a colleague if you share your project without `uv.lock`? And why is it fine to leave out `.venv`?**

Without `uv.lock` the colleague gets whatever versions are newest on that day, so the same code can behave differently or fail on their laptop. `.venv` can be left out because `uv sync` rebuilds it from `pyproject.toml` and `uv.lock`. It is also large and only works on the machine that made it.

**`pyproject.toml` says something like `matplotlib>=3.10`, and `uv.lock` names one exact version. Why keep both files?**

`pyproject.toml` states what you need, as a range that you write and read as a human. `uv.lock` records what was actually installed, including transitive dependencies, so that everybody gets the same set. The range keeps upgrades possible, the lockfile keeps the result reproducible.
