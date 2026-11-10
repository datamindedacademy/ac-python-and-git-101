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
