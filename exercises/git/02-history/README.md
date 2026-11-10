# Exercise 2: Explore the history

Time: **10 minutes** for the core tasks (1 to 4). Tasks 5 to 9 are optional.

## Goal

Read the history of a repository: see what changed, when, and who did it. Throw away a change you do not want.

## Background

Every commit is a snapshot of the whole project. Git can show you what each commit changed. This is the main reason to use version control: you can always answer "what changed, and when did it break?".

Each commit has a **hash**, a code like `3f2a9c1`. You only need the first 7 characters to refer to a commit. You can copy a hash from `git log --oneline` with the mouse.

**HEAD** is the name for "the commit you are on now".

## Setup

From the root of the course repository:

```powershell
uv run python exercises/git/setup_exercise.py 2
```

Run the `cd` command it prints. The repository contains a `.gitignore` file that hides Python cache folders (`__pycache__/`), so they do not clutter `git status`. Exercise 6 explains `.gitignore`.

You now have a repository with 5 commits by three colleagues. The commit hashes in this text are written as `<hash>`. Yours are the ones you see on your screen.

## Core tasks

### 1. See the history

```powershell
git status
git log --oneline
```

Expected:

```
nothing to commit, working tree clean
```

```
<hash> Use more precise bar to psi factor
<hash> Fix Kelvin offset
<hash> Add measurements and analyse_run script
<hash> Add Celsius to Kelvin conversion
<hash> Add bar to psi conversion
```

The newest commit is on top. Now the long form:

```powershell
git log
```

Each commit shows its author and date. Press `q` if you end up in the pager (a screen with `:` or `(END)` at the bottom).

### 2. Look inside a commit

Pick the hash of "Fix Kelvin offset" from the `--oneline` list:

```powershell
git show <hash>
```

You see the message, the author, the date, and the exact lines that changed. Lines that start with `-` were removed. Lines that start with `+` were added. Press `q` to leave the pager if needed.

Question: what was the old value of `KELVIN_OFFSET`, and what is the new one?

### 3. Find when a value changed, and who changed it

Your colleague asks: "Who changed the Kelvin offset, and when?" You already have the answer from task 2: read the `Author:` and `Date:` lines of the commit. To find such a commit in a longer history, list only the commits that touched one file:

```powershell
git log conversions.py
```

Read the messages. Which commit is about the offset? Who made it?

Expected: "Fix Kelvin offset" by Sofie Claes, 5 March 2025. She changed `273.0` into `273.15`.

### 4. Throw away a change

Open `conversions.py` in VS Code. Change `KELVIN_OFFSET = 273.15` to `KELVIN_OFFSET = 0`. Save.

```powershell
git status
git diff
```

You see the change in red and green. You decide it was a mistake. Restore the file to the last commit:

```powershell
git restore conversions.py
git status
```

Expected:

```
nothing to commit, working tree clean
```

Check that `KELVIN_OFFSET` is back to `273.15`.

Be careful: `git restore` on a file permanently throws away your uncommitted changes. Git cannot get them back, because they were never committed. This is why you commit often.

## Check yourself

1. Which command shows the changes of one single commit?
2. Who changed `KELVIN_OFFSET` to `273.15`, and in which commit?
3. What does `git log conversions.py` show that `git log` does not?
4. Why can Git not bring back a change you removed with `git restore <file>`?

## Optional: if you have time

### 5. Compare two commits

```powershell
git diff <hash-of-first-commit> <hash-of-last-commit>
```

Use the hash of "Add bar to psi conversion" first and the hash of "Use more precise bar to psi factor" second. You see everything that changed between those two points. Press `q` if needed.

A shortcut: `HEAD~1` means "one commit before HEAD".

```powershell
git diff HEAD~1 HEAD
```

### 6. Search the history

Ask Git which commits added or removed a piece of text:

```powershell
git log -S 273.15
git log --oneline --author=Jan
```

The first command lists one commit, "Fix Kelvin offset", with its author and date. The second lists the commits by one author.

### 7. Who wrote each line

```powershell
git blame conversions.py
```

`git blame` prints each line of the file with the commit and author that last changed it. Press `q` if needed.

### 8. Visit an old version

Go back to the commit "Add measurements and analyse_run script". It is the first commit that has `analyse_run.py`.

```powershell
git switch --detach <hash>
uv run python analyse_run.py
```

You get a message about "detached HEAD". That is expected. It means you are looking at an old snapshot, not working on a branch. Your files now match that old commit. The output uses the wrong Kelvin offset:

```
Mean pressure: 7.50 bar (108.75 psi)
Mean temperature: 85.3 C (358.33 K)
```

Do not make commits here. Go back to the present:

```powershell
git switch main
uv run python analyse_run.py
```

Now the output is:

```
Mean pressure: 7.50 bar (108.78 psi)
Mean temperature: 85.3 C (358.48 K)
```

Always come back with `git switch main` when you are done looking.

### 9. Unstage a file

Edit `README.md`, add any line, and run `git add README.md`. Then:

```powershell
git status
git restore --staged README.md
git status
```

The first `status` says "Changes to be committed". After `git restore --staged`, the file is back in "Changes not staged for commit". Your edit is still there. Finally run `git restore README.md` to discard the edit.

Questions for this part:

1. What does `git switch --detach <hash>` do? How do you return?
2. What is the difference between `git restore <file>` and `git restore --staged <file>`?

### More

- Which commit added `analyse_run.py`? Find it with `git log --oneline -- analyse_run.py`.
- Run `git log --stat`. Which commit changed the most files?
- Run `git log --oneline --reverse`. What changes?
