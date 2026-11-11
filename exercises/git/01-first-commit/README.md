# Exercise 1: Your first commit

Words to use: repository, working tree, staging area, commit, commit message, hash, untracked, diff.

## Goal

Create your first Git repository, make commits that each say one thing, and understand the three places where your files can live.

## Why this matters

A commit is the unit you can undo and the unit a colleague reviews. Staging lets you make a commit that says one thing, also when you (or Copilot) changed five things at once. Without it you get one large commit that nobody can review or undo in part.

## Background

A **repository** (repo) is a folder that Git watches. Git stores the history of your files inside it, in a hidden folder called `.git`. Never edit or delete `.git` by hand.

A **commit** is a saved snapshot of your files, with a message that says what changed and why. Think of it as a save point in a game. You can always go back to it.

Your files live in three places:

| Place | Name | What it means |
|---|---|---|
| 1 | **Working tree** | The files you see and edit in your folder. |
| 2 | **Staging area** (also called the **index**) | A waiting room. You choose which changes go into the next commit. |
| 3 | **Repository** | The saved history of commits. |

A change moves from left to right: from the working tree into the staging area, and from there into a commit.

```
working tree  --git add-->  staging area  --git commit-->  repository
```

A commit contains what is in the staging area, not what is in the working tree. Two commands compare the places: one shows working tree against staging area, the other shows staging area against the last commit.

## Setup

Run this from the root of the course repository (the folder `ac-python-and-git-101`):

```powershell
uv run python exercises/git/setup_exercise.py 1
```

It creates the folder `git-exercises\exercise_1` in your home folder, outside the course repository. It prints a `cd` command. Copy and run it. You can check where you are with `pwd` and what is in the folder with `ls`.

If you get "The folder ... already exists", you ran the setup before. Add `--force` to delete the folder and start again.

## Tasks

Stuck on a task? The hints are in `HINTS.md` in this folder.

Hashes are written as `<hash>`. Yours differ.

### Task 1: A repository with two commits

Set your name and email for Git, make the folder a repository whose first branch is called `main`, and commit `conversions.py` and `measurements.csv` as two separate commits. Write the messages in the imperative ("Add ...") and pass them on the command line with `-m`, because Git otherwise opens an editor that is hard to leave.

End state:

```
$ git log --oneline
<hash> Add first measurements
<hash> Add bar to psi conversion
```

### Task 2: Two changes, two commits

Make both changes and save both files. Add this function at the end of `conversions.py`:

```python

def celsius_to_kelvin(temperature_c):
    """Convert a temperature from degrees Celsius to Kelvin."""
    return temperature_c + 273.15
```

Add a fourth run as a new last line of `measurements.csv`:

```
4,8.5,91.2
```

Before you run `git status`, predict what it will show. Then commit each change on its own, with a message that says one thing. Run `git diff --staged` before each commit to check that only that change is in it.

End state:

```
$ git log --oneline
<hash> Add fourth measurement run
<hash> Add Celsius to Kelvin conversion
<hash> Add first measurements
<hash> Add bar to psi conversion

$ git status
On branch main
nothing to commit, working tree clean
```

### Task 3: Two edits in one file, and a typo in history

This one is much harder. There is no hint. Use `git help <command>` or Copilot to find the commands.

Make two unrelated edits in `conversions.py`, save the file, and only then start staging:

- Add this function at the end:

```python

def kelvin_to_celsius(temperature_k):
    """Convert a temperature from Kelvin to degrees Celsius."""
    return temperature_k - 273.15
```

- Change the module docstring on line 1 to `"""Unit conversions for the compressor test bench (pressure and temperature)."""`

Commit the function first with the message `Add kelvin_to_celcius` (yes, with the typo), then the docstring change with the message `Reword the module docstring`. Each commit holds one edit.

Now you notice the typo in the message of the commit before the last one. Fix the history so that `git log` shows the correct messages, without losing either edit.

Rules:

- Do not edit the file again after the first save.
- Do not use an interactive rebase.
- Do not delete the folder and start again.

End state:

```
$ git log --oneline
<hash> Reword the module docstring
<hash> Add kelvin_to_celsius
<hash> Add fourth measurement run
<hash> Add Celsius to Kelvin conversion
<hash> Add first measurements
<hash> Add bar to psi conversion

$ git status
On branch main
nothing to commit, working tree clean
```

`git show HEAD~1` shows only the function, and `git show HEAD` shows only the docstring change.

## Open question

You commit the same 50 MB file twice, under two different names. How much space does Git need for it, and why? Then a harder one: you and a colleague each make a commit with exactly the same files and the same message. Do the two commits get the same hash?
