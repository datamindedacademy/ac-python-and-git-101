# Python and Git 101

[![Dataminded Academy](https://raw.githubusercontent.com/datamindedacademy/branding/main/assets/badge.svg)](https://github.com/datamindedacademy)

Course material for **day 1** of the Dataminded training *Python Programming and Data
Analysis* for the FD and FT departments of Atlas Copco: development environment,
programming fundamentals, and version control.

Day 1 assumes no programming experience. After this day you can:

- Set up a Python environment and run a script from PowerShell.
- Create a virtual environment per project and install packages with uv.
- Write a script with functions, conditionals and loops, import a package into it, and
  run it from VS Code.
- Read a stack trace and find the error it points to.
- Automate a repetitive task with a script that reads and writes files.
- Clone an Azure DevOps repository, commit on a branch, push and pull.

## What is in this repository

| Path | What it is |
| --- | --- |
| [`exercises/python/`](exercises/python/) | Python exercises, one folder per topic, each with its own `README.md` |
| [`exercises/git/`](exercises/git/) | Git exercises, with a setup script that prepares a practice repository per exercise |
| [`solutions/`](solutions/) | Reference solutions. Try the exercise first. |
| [`slides/`](slides/) | The slide deck, written in [Slidev](https://sli.dev) with the Dataminded theme |
| [`tests/`](tests/) | Checks that the solutions and the Git setup script keep working. For trainers. |
| [`.devcontainer/`](.devcontainer/) | Fallback environment, see below |

## Schedule

| Time | Block | Exercises |
| --- | --- | --- |
| 09:00 | Setup check with the trainer (30 minutes at most) | |
| 09:30 | Scripts and notebooks, running Python on your laptop | `python/01` |
| 10:15 | Language fundamentals: variables, types, collections, control flow, functions | `python/02` to `python/05` |
| 12:30 | Lunch | |
| 13:15 | The standard library, files and exceptions, reading a traceback | `python/06`, `python/07` |
| 14:20 | Projects and dependencies with uv | `python/08` |
| 15:05 | Version control with Git and Azure DevOps | `git/01` to `git/05`, `git/06` as a demo |
| 16:50 | Wrap-up and preparation for day 2 | |

Each exercise has core tasks that fit the schedule and optional tasks for those who
finish early. The day has about two hours of instruction and three and a half hours of
hands-on work.

## Getting started on your Atlas Copco laptop

You need the tools from the setup manual you received before the training: Git for
Windows, uv, Python 3.13 (installed by uv) and Visual Studio Code. The first half hour of
the day is a check that everything works; come with the manual applied.

Open **PowerShell** and run these commands one by one. The trainer gives you the URL of
this repository.

```powershell
cd $HOME\Documents
git clone <url-of-this-repository>
cd ac-python-and-git-101
uv sync
uv run python exercises/python/01-first-script/hello.py
code .
```

`uv sync` creates a virtual environment in the `.venv` folder and installs everything
the exercises need. `uv run` runs a command inside that environment, so you never have
to activate it yourself.

In VS Code, accept the recommended extensions when asked, and pick the interpreter in
`.venv` when VS Code asks which Python to use (`Ctrl+Shift+P`, then
*Python: Select Interpreter*).

Then start with [`exercises/python/`](exercises/python/) and continue with
[`exercises/git/`](exercises/git/) in the afternoon.

> PowerShell on Atlas Copco laptops does not run `.ps1` scripts. Nothing in this
> repository needs one: every command is either typed directly or is a Python script
> started with `uv run python`.

## Fallback: the devcontainer

Most participants work directly on their Windows workstation, and that is the setup
the exercises are written for. If your laptop setup cannot be completed in time, the
repository also contains a [devcontainer](.devcontainer/devcontainer.json) with the
same tools (Python 3.13, uv, Git, PowerShell, Node.js for the slides):

- **GitHub Codespaces**: on the repository page, choose *Code*, *Codespaces*, *Create
  codespace*. Everything runs in the browser.
- **VS Code with Docker or Podman**: install the *Dev Containers* extension, open the
  repository folder and choose *Reopen in Container*.

The terminal in the devcontainer is PowerShell (`pwsh`) on Linux, so the commands in
the exercises work unchanged. The parts of the exercises about Windows itself (PATH,
where Python is installed) differ there: follow along with your neighbour for those.

## For trainers

```powershell
uv run pytest                 # checks the solutions and the Git setup script
uv run ruff check .           # lint
cd slides
npm install
npm run dev                   # slides on http://localhost:3030, "p" opens presenter mode
npm run export                # PDF handout
```

Before the training, prepare the Azure DevOps training repository as described in
[`exercises/git/TRAINER.md`](exercises/git/TRAINER.md).

Days 2 (data analysis and scientific computing) and 3 (CI/CD, code quality and agentic
AI) have their own repositories.
