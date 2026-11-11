# Exercise 1: Your first commit

Core tasks: 1 to 7. Everything under "Optional" is extra.

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

## Core tasks

Try each task with the hint closed. Open it when you are stuck.

### 1. Tell Git who you are

Every commit has an author. Check what Git knows about you:

```powershell
git config user.name
git config user.email
```

If either command prints nothing, set them once for this laptop. Use your own name and work email:

```powershell
git config --global user.name "Your Name"
git config --global user.email "your.name@example.com"
```

Run the two check commands again. You should see your name and email.

### 2. Make the folder a repository

Result: the folder is a repository whose first branch is called `main`. A **branch** is a line of commits. For now you have only one.

Check: `git status` says "No commits yet" and lists `conversions.py` and `measurements.csv` as untracked. **Untracked** means Git sees the files but does not follow them yet.

<details>
<summary>Hint</summary>

```powershell
git init -b main
git status
```

Expected:

```
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	conversions.py
	measurements.csv

nothing added to commit but untracked files present (use "git add" to track)
```

</details>

### 3. First commit: one file only

Result: the first commit contains only `conversions.py`. Give it a short message in the imperative ("Add ...", "Fix ...", "Change ..."), and always pass the message on the command line, because Git otherwise opens an editor that is hard to leave.

Check: `git log --oneline` shows one commit, and `git status` still lists `measurements.csv` as untracked.

Question: why might you want a file to stay out of a commit?

<details>
<summary>Hint</summary>

```powershell
git add conversions.py
git status
git commit -m "Add bar to psi conversion"
git log --oneline
git status
```

After `git add`, `git status` lists `conversions.py` under "Changes to be committed". The commit prints something like:

```
[main (root-commit) <hash>] Add bar to psi conversion
 1 file changed, 8 insertions(+)
 create mode 100644 conversions.py
```

`<hash>` is a short code that identifies the commit. Yours differs from the one in this text. If `git log` fills the screen and shows `:` or `(END)`, press `q`.

</details>

### 4. Second commit: the data file

Result: `measurements.csv` is committed in its own commit, with its own message.

Check: `git log --oneline` shows two commits.

<details>
<summary>Hint</summary>

```powershell
git add measurements.csv
git commit -m "Add first measurements"
git log --oneline
```

</details>

### 5. Two unrelated changes

Make both changes now, and save both files:

1. Add this function at the end of `conversions.py`:

```python


def celsius_to_kelvin(temperature_c):
    """Convert a temperature from degrees Celsius to Kelvin."""
    return temperature_c + 273.15
```

2. Add a fourth run as a new last line of `measurements.csv`:

```
4,8.5,91.2
```

Question: before you stage anything, which command shows exactly what you changed? Run it and read the output. Lines that start with `+` were added, lines that start with `-` were removed.

<details>
<summary>Hint</summary>

```powershell
git status
git diff
```

If `git diff` opens a pager, press `q`.

</details>

### 6. Two separate commits

Result: each change is in its own commit with its own message. Do not undo or re-edit anything.

Stop after you staged the first file and before you commit it. Compare the plain diff with the staged diff. Question: what does each one show now?

Check: `git log --oneline` shows four commits, and `git status` says "nothing to commit, working tree clean".

<details>
<summary>Hint</summary>

```powershell
git add conversions.py
git diff
git diff --staged
git commit -m "Add Celsius to Kelvin conversion"
git add measurements.csv
git commit -m "Add fourth measurement run"
git log --oneline
git status
```

</details>

### 7. Predict, then check

1. In the docstring of `bar_to_psi`, change `Convert a pressure from bar to psi.` to `Convert a pressure from bar (absolute) to psi.` Save, and stage the file.
2. In `conversions.py`, change `BAR_TO_PSI = 14.5` to `BAR_TO_PSI = 14.5038`. Save. Do **not** stage this.

Question: before you run it, what will `git status` say about `conversions.py`? Write your prediction down, then run it.

Then make one commit that contains only the docstring change, and a second commit with the rest.

Check: `git log --oneline` shows six commits.

<details>
<summary>Hint</summary>

```powershell
git status
git diff --staged
git diff
git commit -m "Clarify the bar_to_psi docstring"
git add conversions.py
git commit -m "Use a more precise psi factor"
git log --oneline
```

</details>

## Check yourself

Short questions to test yourself after class. The answers are in `solutions/git/README.md`.

1. Which command shows the changes that are not staged yet? Which one shows the staged changes?
2. What does "untracked" mean?
3. Why do we write `-m "..."` after `git commit`?
4. A file is listed under both "Changes to be committed" and "Changes not staged for commit". How can that be?

## Optional: if you have time

### With Copilot

Let Copilot change the code, then use Git to judge the result. Open Copilot Chat in VS Code (`Ctrl+Alt+I`) and ask:

> Add a function `kelvin_to_celsius` to `conversions.py`. Do not change the existing functions.

Before you commit, run `git diff`. Did it change anything you did not ask for? Is the formula right? If you are happy, stage and commit it with your own commit message. If not, discard the change with `git restore conversions.py`. Either way, you decide: you are the author of the commit.

### More

- Run `git log --stat`. What extra information do you get?
- Run `ls -Force` and find the `.git` folder. Do not open it.

## Challenge

For those who finish early. No commands given: find them with `git help <command>` or Copilot, and check the result with `git log` and `git status`.

Tasks 5 to 7 split changes by file, or by the moment you stage. Here both changes are in the same file at the same time. In `conversions.py`, make two unrelated edits in different places: add a new function, and change the module docstring. Save the file, and only then start staging. Commit the two edits as two separate commits, one per edit. Do not undo either edit and do not edit the file again between the commits.

## Open question

This goes beyond today. Most people cannot answer it yet. Try it anyway, or bring it to the trainer.

You commit the same 50 MB file twice, under two different names. How much space does Git need for it, and why? Then a harder one: you and a colleague each make a commit with exactly the same files and the same message. Do the two commits get the same hash?
