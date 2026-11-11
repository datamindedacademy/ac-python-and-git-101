# Python and Git 101

[![Dataminded Academy](https://raw.githubusercontent.com/datamindedacademy/branding/main/assets/badge.svg)](https://github.com/datamindedacademy)
[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/datamindedacademy/ac-python-and-git-101)

Course material for **day 1** of the Dataminded training *Python Programming and Data
Analysis* for Atlas Copco: development environment, programming fundamentals, and
version control.

Day 1 assumes basic scripting experience, for example in MATLAB or VBA. You do not need
to know Python. After this day you can:

- Set up a Python environment and run a script from PowerShell.
- Create a virtual environment per project and install packages with uv.
- Write a script with functions, conditionals and loops, import a package into it, and
  run it from VS Code.
- Read a stack trace and find the error it points to.
- Automate a repetitive task with a script that reads and writes files.
- Clone a GitHub repository, commit on a branch, push and pull.

You may use GitHub Copilot throughout. Do not keep a line you do not understand.

## What is in this repository

| Path | What it is |
| --- | --- |
| [`exercises/python/`](exercises/python/) | Python exercises, one folder per topic |
| [`exercises/git/`](exercises/git/) | Git exercises, with a script that prepares a practice repository |
| [`solutions/`](solutions/) | Reference solutions. Try the exercise first. |
| [`slides/`](slides/) | The slide deck |

## Getting started

You need the tools from the setup manual: Git for Windows, uv, and Visual Studio Code
with GitHub Copilot. Open **PowerShell** and run these commands one by one:

```powershell
cd $HOME\Documents
git clone https://github.com/datamindedacademy/ac-python-and-git-101
cd ac-python-and-git-101
uv sync
uv run python exercises/python/01-first-script/hello.py
code .
```

In VS Code, accept the recommended extensions and select the interpreter in `.venv`
(`Ctrl+Shift+P`, then *Python: Select Interpreter*).

Start with [`exercises/python/`](exercises/python/) and continue with
[`exercises/git/`](exercises/git/) in the afternoon.

If your laptop setup does not work in time, use the Codespaces button at the top. It
opens the same tools in the browser, with PowerShell as the terminal.
