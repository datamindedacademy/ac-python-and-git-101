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

## Challenge

There is no solution file. The steps:

1. In `pressure-demo`, copy `conversions.py` and `test_conversions.py` from your exercise 05 folder next to `main.py`.
2. Run `uv add --dev pytest`. `pyproject.toml` gets a `[dependency-groups]` section with `dev = ["pytest>=..."]`, and `uv.lock` is updated.
3. Run `uv run pytest`. All tests pass, for example `6 passed`.

Without step 2, `uv run pytest` reports that pytest is not found, because the project `.venv` does not have it.

## Open question

uv reports that it cannot find a set of versions that satisfies both packages, and it adds nothing. One environment has one `numpy` folder, so only one version can be imported, and no tool can change that. The hash lets uv check that a downloaded file is exactly the one that was locked. A changed or tampered file is rejected.
