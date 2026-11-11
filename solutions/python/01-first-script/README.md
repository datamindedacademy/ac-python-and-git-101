# Solution notes - 01

## Script or notebook?

| | Advantages | Disadvantages |
|---|---|---|
| Script | Runs the same way every time. Easy to schedule and automate. Works well with Git (plain text). Easy to import into other code. | No instant feedback per step. Plots and tables are not shown next to the code. Needs the terminal. |
| Notebook | Run step by step and see results at once. Mix text, code and plots. Good for exploring data and for sharing a story. | Cells can run out of order, so results may not be reproducible. Hidden state. Hard to review in Git. Harder to test and reuse. |

Rule of thumb: explore in a notebook, then move the stable code to a script or module.

## Where does Python live?

`Get-Command python` shows the first `python` on PATH. This can be a different Python than the one in `.venv`. That is why we always start with `uv run`: it picks the project `.venv`, so everybody gets the same Python and packages.

## Open question

When you press Enter, the interpreter starts and imports a few modules it needs at startup. It then compiles your source to bytecode and runs that. Python saves the bytecode of modules you import in a `__pycache__` folder next to them, so the next start skips the compile step. The script you run directly is not cached, it is compiled every time.
