# Exercise 1: Your first commit

Core tasks: 1 to 8. Everything under "Optional" is extra.

Words to use: repository, working tree, staging area, commit, commit message, hash, untracked, diff.

## Goal

Create your first Git repository, make two commits, and understand the three places where your files can live.

## Why this matters

A commit is the unit you can undo and the unit a colleague reviews. Staging lets you make a commit that says one thing, also when you (or Copilot) changed five things at once. Without it you get one large commit that nobody can review or undo in part.

## Background

A **repository** (repo) is a folder that Git watches. Git stores the history of your files inside it, in a hidden folder called `.git`. Never edit or delete `.git` by hand.

A **commit** is a saved snapshot of your files, with a message that says what changed and why. Think of it as a save point in a game. You can always go back to it.

Your files live in three places:

| Place | Name | What it means |
|---|---|---|
| 1 | **Working tree** | The files you see and edit in your folder. |
| 2 | **Staging area** | A waiting room. You choose which changes go into the next commit. |
| 3 | **Repository** | The saved history of commits. |

The commands move changes from left to right:

```
working tree  --git add-->  staging area  --git commit-->  repository
```

## Setup

Run this from the root of the course repository (the folder `ac-python-and-git-101`):

```powershell
uv run python exercises/git/setup_exercise.py 1
```

It creates the folder `git-exercises\exercise_1` in your home folder, outside the course repository. It prints a `cd` command. Copy and run it. You can check where you are with `pwd` and what is in the folder with `ls`.

If you get "The folder ... already exists", you ran the setup before. Add `--force` to delete the folder and start again.

## Tasks

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

### 2. Look at the folder before it is a repository

```powershell
ls
git status
```

`ls` shows two files: `conversions.py` and `measurements.csv`.

`git status` says:

```
fatal: not a git repository (or any of the parent directories): .git
```

This is fine. Git only works inside a repository, and you have not made one yet.

### 3. Create the repository

```powershell
git init -b main
git status
```

`-b main` names the first branch `main`. A **branch** is a line of commits. For now you have only one.

You should see something like:

```
Initialized empty Git repository in .../exercise_1/.git/
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	conversions.py
	measurements.csv

nothing added to commit but untracked files present (use "git add" to track)
```

**Untracked** means Git sees the files but does not follow them yet.

### 4. Stage one file

```powershell
git add conversions.py
git status
```

`conversions.py` is now listed under "Changes to be committed". It is in the staging area. `measurements.csv` is still untracked. That is on purpose: you choose what goes into each commit.

### 5. Make the first commit

```powershell
git commit -m "Add bar to psi conversion"
```

Always use `-m "message"`. Without it, Git opens a text editor that is hard to leave.

Expected output:

```
[main (root-commit) <hash>] Add bar to psi conversion
 1 file changed, 8 insertions(+)
 create mode 100644 conversions.py
```

`<hash>` is a short code that identifies the commit. Yours will differ from the one in this text.

Write messages in the form "Add ...", "Fix ...", "Change ...". Say what the commit does.

### 6. Read the history

```powershell
git log
```

You see one commit with its hash, author, date and message. If the output fills the screen and shows `:` or `(END)` at the bottom, you are in a pager. Press `q` to leave it.

For a compact view:

```powershell
git log --oneline
```

Expected:

```
<hash> Add bar to psi conversion
```

### 7. Change a file and look at the difference

Open the folder in VS Code (`code .`) and open `conversions.py`. Add this function at the end of the file:

```python


def celsius_to_kelvin(temperature_c):
    """Convert a temperature from degrees Celsius to Kelvin."""
    return temperature_c + 273.15
```

Save the file. Now:

```powershell
git status
git diff
```

`git status` says `modified: conversions.py` under "Changes not staged for commit". `git diff` shows the difference between your working tree and the last commit. Lines that start with `+` were added. Lines that start with `-` were removed.

```
@@ -6,3 +6,8 @@ BAR_TO_PSI = 14.5
 def bar_to_psi(pressure_bar):
     """Convert a pressure from bar to psi."""
     return pressure_bar * BAR_TO_PSI
+
+
+def celsius_to_kelvin(temperature_c):
+    """Convert a temperature from degrees Celsius to Kelvin."""
+    return temperature_c + 273.15
```

If `git diff` opens a pager, press `q`.

### 8. Stage, check, commit

```powershell
git add conversions.py
git diff
git diff --staged
```

After `git add`, plain `git diff` prints nothing. The change moved to the staging area. `git diff --staged` shows what is waiting there.

```powershell
git commit -m "Add Celsius to Kelvin conversion"
git log --oneline
```

Expected:

```
<hash> Add Celsius to Kelvin conversion
<hash> Add bar to psi conversion
```

## Check yourself

Short questions to test yourself after class. The answers are in `solutions/git/README.md`.

1. After `git add`, why does `git diff` show nothing? Which command shows the staged change?
2. What does "untracked" mean?
3. Why do we write `-m "..."` after `git commit`?

## Optional: if you have time

### 9. Commit the data file

`measurements.csv` is still untracked. Add it in a third commit:

```powershell
git add measurements.csv
git commit -m "Add first measurements"
git status
```

The last command should say:

```
On branch main
nothing to commit, working tree clean
```

"Working tree clean" means the files on disk match the last commit.

### With Copilot

Let Copilot change the code, then use Git to judge the result. Open Copilot Chat in VS Code (`Ctrl+Alt+I`) and ask:

> Add a function `kelvin_to_celsius` to `conversions.py`. Do not change the existing functions.

Before you commit, run `git diff`. Did it change anything you did not ask for? Is the formula right? If you are happy, stage and commit it with your own commit message. If not, discard the change with `git restore conversions.py`. Either way, you decide: you are the author of the commit.

### More

- Run `git log --stat`. What extra information do you get?
- Edit `measurements.csv`, add a fourth run, then use `git diff` and commit it with a clear message.
- Run `ls -Force` and find the `.git` folder. Do not open it.

## Challenge

For those who finish early. No commands given: find them with `git help <command>` or Copilot, and check the result with `git log` and `git status`.

In `conversions.py`, make two unrelated edits in different places of the file: add a new function, and change a comment or docstring of an existing one. Commit them as two separate commits, one per edit. Do not undo either edit and do not edit the file again between the commits.

## Open question

This goes beyond today. Most people cannot answer it yet. Try it anyway, or bring it to the trainer.

You commit the same 50 MB file twice, under two different names. How much space does Git need for it, and why? Then a harder one: you and a colleague each make a commit with exactly the same files and the same message. Do the two commits get the same hash?
