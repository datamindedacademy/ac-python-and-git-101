# Solution notes - 08

The reference script `plot_pressure.py` is the exercise script plus the inline script metadata block from task 2.

## Task 3

```powershell
uv tree --invert --package tzdata
uv add "matplotlib==3.9.*"
Remove-Item -Recurse -Force .venv
uv sync --locked
uv run python -c "import matplotlib; print(matplotlib.__version__)"
```

Then edit `pyproject.toml` to `"matplotlib==3.10.*"` and run:

```powershell
uv sync --locked
uv sync --frozen
uv run --frozen python -c "import matplotlib; print(matplotlib.__version__)"
uv sync
uv run python -c "import matplotlib; print(matplotlib.__version__)"
```

- `tzdata` comes from `python-dateutil`, which comes from `matplotlib`. `uv tree --invert --package` reads the tree from the bottom up.
- `uv sync --locked` after the hand edit fails: the lockfile does not match `pyproject.toml`. This is the check to use in CI.
- `uv sync --frozen` ignores `pyproject.toml` and installs exactly what `uv.lock` says, so it stays on 3.9.x.
- Plain `uv sync` re-resolves, rewrites `uv.lock` and installs 3.10.x. `uv lock --upgrade` also rewrites `uv.lock`, but to the newest versions allowed by `pyproject.toml`, and does not touch the environment.
- A plain `uv run` between the steps would also sync, and so would hide the difference. That is why the check uses `--frozen`.

## Open question

uv reports that it cannot find a set of versions that satisfies both packages, and it adds nothing. One environment has one `numpy` folder, so only one version can be imported, and no tool can change that. The hash lets uv check that a downloaded file is exactly the one that was locked. A changed or tampered file is rejected.
