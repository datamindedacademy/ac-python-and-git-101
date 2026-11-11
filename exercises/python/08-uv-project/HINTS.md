# Hints: 08 - A uv project with a package

Try the task first. Read a hint only when you are stuck.

## Hint for task 1

`uv init pressure-demo`, then `cd pressure-demo`, then `uv add matplotlib`. Copy the script from the repo with `Copy-Item` and run it with `uv run python plot_pressure.py`. Open `pyproject.toml` and `uv.lock` in VS Code. Running the script with plain `python` fails: that Python does not know the `.venv`.

## Hint for task 2

The slide before this exercise shows it. Copy the script into a new empty folder, then run `uv add --script plot_pressure.py matplotlib` and look at the top of the file. Run it with `uv run plot_pressure.py`.
