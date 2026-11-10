# Solution notes - 01

## Script or notebook?

| | Advantages | Disadvantages |
|---|---|---|
| Script | Runs the same way every time. Easy to schedule and automate. Works well with Git (plain text). Easy to import into other code. | No instant feedback per step. Plots and tables are not shown next to the code. Needs the terminal. |
| Notebook | Run step by step and see results at once. Mix text, code and plots. Good for exploring data and for sharing a story. | Cells can run out of order, so results may not be reproducible. Hidden state. Hard to review in Git. Harder to test and reuse. |

Rule of thumb: explore in a notebook, then move the stable code to a script or module.

## Where does Python live?

`Get-Command python` shows the first `python` on PATH. This can be a different Python than the one in `.venv`. That is why we always start with `uv run`: it picks the project `.venv`, so everybody gets the same Python and packages.

## Explain it: model answers

Your own words are fine. What matters is that you name the tradeoff.

**You ran the same calculation as a script and as a notebook. Name one job where you would choose a script and one where you would choose a notebook. Say why.**

A script fits work you repeat or hand over: it runs the same way every time, from top to bottom, and it is plain text. A notebook fits exploring: you run one cell at a time and see the result directly. The price of the notebook is hidden state: cells can run in any order, so the result is harder to reproduce.

**What does `uv run` do for you before it starts `python`? Why do we not just type `python hello.py`?**

`uv run` makes sure the project's virtual environment (`.venv`) exists and matches the project file, then starts the Python inside it. Plain `python` starts whatever interpreter is first on PATH, which can be another version without your packages. `uv run` costs a few extra characters and gives everybody the same interpreter.
