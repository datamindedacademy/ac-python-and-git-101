# Exercise 2: Explore the history

Extra exercise: do it when you are ahead, or after class. Exercises 3 to 5 do not depend on it.

Words to use: history, log, hash, HEAD, author, commit message, diff, restore.

## Goal

Read the history of a repository: see what changed, when, and who did it. Throw away a change you do not want.

## Why this matters

When a number in a report changes, the history tells you what changed, who did it and why. That only works when commits are small and the messages say something. Without it you compare old and new files by hand and guess.

## Background

Every commit is a snapshot of the whole project. Git can show you what each commit changed. This is the main reason to use version control: you can always answer "what changed, and when did it break?".

Each commit has a **hash**, a code like `3f2a9c1`. You only need the first 7 characters to refer to a commit. You can copy a hash from `git log --oneline` with the mouse.

**HEAD** is the name for "the commit you are on now".

## Setup

From the root of the course repository:

```powershell
uv run python exercises/git/setup_exercise.py 2
```

Run the two commands it prints: `cd` goes to the exercise folder and `code .` opens it in a second VS Code window, where you edit the files and type your Git commands (terminal: ``Ctrl+` ``). The repository contains a `.gitignore` file that hides Python cache folders (`__pycache__/`), so they do not clutter `git status`. Exercise 6 explains `.gitignore`.

You now have a repository with 5 commits by three colleagues. The commit hashes in this text are written as `<hash>`. Yours are the ones you see on your screen.

## Tasks

Stuck on a task? Look at the slides, the cheat sheet in `exercises/git/README.md`, or `git help <command>`.

### Task 1: Read the history

Find out which 5 commits the repository has, newest first, and what the commit "Add measurements and analyse_run script" changed: which files, and how many lines.

Expected:

```
$ git log --oneline
<hash> Use more precise bar to psi factor
<hash> Fix Kelvin offset
<hash> Add measurements and analyse_run script
<hash> Add Celsius to Kelvin conversion
<hash> Add bar to psi conversion
```

The commit changed two files:

```
 analyse_run.py   | 21 +++++++++++++++++++++
 measurements.csv |  4 ++++
 2 files changed, 25 insertions(+)
```

### Task 2: Find a change, then throw one away

Your colleague asks: "Which commit changed the Kelvin offset to `273.15`, who made it and when?" Answer it with one Git command that searches the history, without opening every commit.

Then open `conversions.py` in VS Code, change `KELVIN_OFFSET = 273.15` to `KELVIN_OFFSET = 0` and save. You decide it was a mistake. Get the file back to the last commit and check that the working tree is clean.

Expected for the question:

```
$ git log -S273.15 --format="%h %an %ad %s" --date=short
<hash> Sofie Claes 2025-03-05 Fix Kelvin offset
```

Expected after the restore:

```
$ git status
On branch main
nothing to commit, working tree clean
```

### Task 3: Undo one old commit, keep the later ones

This one is much harder. Use `git help <command>` or Copilot to find the commands.

A report must match old results, so the Kelvin offset has to go back to `273.0`. Undo the commit "Fix Kelvin offset" only. Do not delete it from the history, and keep the commit "Use more precise bar to psi factor" that came after it, so `BAR_TO_PSI` stays `14.5038`.

Rules:

- Do not edit the file by hand before Git has asked you to.
- Do not use `git reset`.
- Git will stop and ask you to resolve a conflict. Finish the job so that no `<<<<<<<`, `=======` or `>>>>>>>` is left in the file and the undo is committed.

End state:

```
$ git log --oneline
<hash> Revert "Fix Kelvin offset"
<hash> Use more precise bar to psi factor
<hash> Fix Kelvin offset
<hash> Add measurements and analyse_run script
<hash> Add Celsius to Kelvin conversion
<hash> Add bar to psi conversion

$ git status
On branch main
nothing to commit, working tree clean

$ uv run python analyse_run.py
Mean pressure: 7.50 bar (108.78 psi)
Mean temperature: 85.3 C (358.33 K)
```

## Open question

`git restore` threw your edit away for good. A commit that no branch points to any more is different: Git keeps it for a while. How would you find it again?
