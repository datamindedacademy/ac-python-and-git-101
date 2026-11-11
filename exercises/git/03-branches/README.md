# Exercise 3: Branches and merging

Words to use: branch, HEAD, switch, merge, fast-forward, merge commit, merge conflict, rebase.

## Goal

Work on a change in a separate branch and merge it back into `main`. Resolve a merge conflict. Rebase a branch so the history stays a straight line.

## Why this matters

A branch lets you try something without breaking the version that works. Conflicts are normal as soon as two people touch the same script. Solving one calmly is a skill you need in the first week of working together.

## Background

A **branch** is a separate line of work. You make a branch to try something without disturbing `main`. When the work is good, you **merge** it back.

A branch is only a label that points to a commit. Making one costs nothing. `HEAD` tells you which branch you are on.

There are two kinds of merge:

- **Fast-forward**: `main` did not change while you worked. Git just moves the `main` label forward. No new commit.
- **Merge commit**: `main` moved on while you worked. Git combines both lines in a new commit with two parents. If both lines changed the same lines, you decide first: a **merge conflict**.

A **rebase** is the other way to combine them. Git replays your commits one by one on top of the latest `main`, so the history stays a straight line.

## Setup

From the root of the course repository:

```powershell
uv run python exercises/git/setup_exercise.py 3
```

Run the `cd` command it prints. You get a repository with 4 commits on `main` and two other branches: `experiment/psi-precision` (used in task 2) and `feature/temperature-report` (used in task 3). Leave them alone until then. Look at all branches in one graph at any time with `git log --oneline --graph --all --decorate`. If the output opens in a pager, press `q`.

## Tasks

Stuck on a task? Look at the slides, the cheat sheet in `exercises/git/README.md`, or `git help <command>`.

Do the tasks in order, in the same repository.

### Task 1: Branch and fast-forward

Make a branch `feature/pressure-kpa` and commit this function on it, at the end of `conversions.py`:

```python

def bar_to_kpa(pressure_bar):
    """Convert a pressure from bar to kPa."""
    return pressure_bar * 100
```

Use the commit message `Add bar to kPa conversion`. Merge the branch into `main` as a fast-forward, then delete the branch. Check that `conversions.py` on `main` contains the function.

End state:

```
* <hash> (HEAD -> main) Add bar to kPa conversion
* <hash> Round psi factor to 3 decimals
| * <hash> (experiment/psi-precision) Try a more precise psi factor
|/
| * <hash> (feature/temperature-report) Print mean temperature in Fahrenheit
| * <hash> Add Celsius to Fahrenheit conversion
| * <hash> Print min temperature
|/
* <hash> Add README
* <hash> Add measurements and analyse_run script
* <hash> Add unit conversions
```

The merge output says `Fast-forward`.

### Task 2: A merge conflict

`main` and `experiment/psi-precision` both changed the line with `BAR_TO_PSI`. Merge `experiment/psi-precision` into `main`. Git reports a conflict. Resolve it so that `BAR_TO_PSI = 14.5038`, with no conflict markers left in the file, and the `bar_to_kpa` function still there. Finish the merge with the message `Merge experiment/psi-precision`.

End state:

```
*   <hash> (HEAD -> main) Merge experiment/psi-precision
|\
| * <hash> (experiment/psi-precision) Try a more precise psi factor
* | <hash> Add bar to kPa conversion
* | <hash> Round psi factor to 3 decimals
|/
| * <hash> (feature/temperature-report) Print mean temperature in Fahrenheit
| * <hash> Add Celsius to Fahrenheit conversion
| * <hash> Print min temperature
|/
* <hash> Add README
* <hash> Add measurements and analyse_run script
* <hash> Add unit conversions
```

The top of `conversions.py`:

```
"""Unit conversions for the compressor test bench."""

BAR_TO_PSI = 14.5038  # psi per bar, more precise
KELVIN_OFFSET = 273.15
```

### Task 3: Rebase

This one is much harder.

The branch `feature/temperature-report` has three commits. It was started before `main` moved on, and one of its commits clashes with `main`. Get its three commits on top of the current `main`, with the same messages, so that the history after `main` is a straight line. Then merge the branch into `main` as a fast-forward and delete it.

Rules:

- Use `git rebase`, not `git merge`, to bring the branch up to date. Resolve the conflict so that both `bar_to_kpa` and `celsius_to_fahrenheit` are in `conversions.py`.
- Before you start, add the line `TODO: check the units` at the end of `README.md`. Do not commit it. It must still be there, uncommitted, when you are done.
- Find the commands with `git help rebase`, `git help stash` or Copilot.

End state:

```
* <hash> (HEAD -> main) Print mean temperature in Fahrenheit
* <hash> Add Celsius to Fahrenheit conversion
* <hash> Print min temperature
*   <hash> Merge experiment/psi-precision
|\
| * <hash> (experiment/psi-precision) Try a more precise psi factor
* | <hash> Add bar to kPa conversion
* | <hash> Round psi factor to 3 decimals
|/
* <hash> Add README
* <hash> Add measurements and analyse_run script
* <hash> Add unit conversions
```

`git status --short` shows ` M README.md`, and `uv run python analyse_run.py` prints a minimum temperature and a mean temperature in Fahrenheit.

Question: the three commits have new hashes now. Why?

## Open question

Git does not record on which branch a commit was made. So how can `git log --graph` draw the lines? And what is a branch, physically, inside the `.git` folder?
