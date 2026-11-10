# Exercise 3: Branches and merging

Time: **15 minutes** for the core tasks (1 to 5). The merge conflict at the end is optional (10 minutes).

Words to use: branch, HEAD, switch, merge, fast-forward, merge commit, merge conflict.

## Goal

Work on a change in a separate branch, then merge it back into `main`. See both kinds of merge: fast-forward and merge commit.

## Background

A **branch** is a separate line of work. You make a branch to try something without disturbing `main`. When the work is good, you **merge** it back.

`main` is the branch that holds the "official" version of the project. A common rule: never work directly on `main`. Do your work on a branch, then merge.

A branch is only a label that points to a commit. Making one costs nothing. `HEAD` tells you which branch you are on.

There are two kinds of merge:

- **Fast-forward**: `main` did not change while you worked. Git just moves the `main` label forward. No new commit.
- **Merge commit**: `main` moved on while you worked. Git combines both lines in a new commit with two parents.

## Setup

From the root of the course repository:

```powershell
uv run python exercises/git/setup_exercise.py 3
```

Run the `cd` command it prints. The repository contains a `.gitignore` file that hides Python cache folders (`__pycache__/`), so they do not clutter `git status`. Exercise 6 explains `.gitignore`. You get a repository with 4 commits on `main`, and a second branch called `experiment/psi-precision`. Leave that branch alone until the optional part.

## Core tasks

### 1. Look at where you are

```powershell
git branch
git log --oneline --graph --all --decorate
```

`git branch` lists the local branches. The `*` marks the one you are on.

```
  experiment/psi-precision
* main
```

The graph looks like this:

```
* <hash> (HEAD -> main) Round psi factor to 3 decimals
| * <hash> (experiment/psi-precision) Try a more precise psi factor
|/
* <hash> Add README
* <hash> Add measurements and analyse_run script
* <hash> Add unit conversions
```

Read it from top to bottom, newest first. Each `*` is a commit. `HEAD -> main` means you are on `main`. If the output opens in a pager, press `q`.

### 2. Make a branch and commit on it

Create a branch and switch to it in one step:

```powershell
git switch -c feature/pressure-kpa
```

Expected:

```
Switched to a new branch 'feature/pressure-kpa'
```

Branch names are free text. A common habit is `feature/<what-it-does>` or `fix/<what-it-fixes>`.

Open the folder in VS Code (`code .`). Add this function at the end of `conversions.py` and save:

```python


def bar_to_kpa(pressure_bar):
    """Convert a pressure from bar to kPa."""
    return pressure_bar * 100
```

Commit it:

```powershell
git status
git add conversions.py
git commit -m "Add bar to kPa conversion"
git log --oneline --graph --all --decorate
```

The graph now shows your commit on top, on the branch `feature/pressure-kpa`, as a straight line on top of `main`:

```
* <hash> (HEAD -> feature/pressure-kpa) Add bar to kPa conversion
* <hash> (main) Round psi factor to 3 decimals
| * <hash> (experiment/psi-precision) Try a more precise psi factor
|/
* <hash> Add README
...
```

### 3. Merge: the fast-forward

Go back to `main` and look at `conversions.py` in VS Code. The new function is gone. It lives only on your branch. Switching branches changes the files on disk.

```powershell
git switch main
git merge feature/pressure-kpa
```

Expected:

```
Updating <hash>..<hash>
Fast-forward
 conversions.py | 5 +++++
 1 file changed, 5 insertions(+)
```

"Fast-forward" means `main` had no new commits, so Git only moved the label. Check the file again: the function is back, now on `main`.

Delete the branch. It is merged, so the commits are safe:

```powershell
git branch -d feature/pressure-kpa
git log --oneline --graph --all --decorate
```

`-d` refuses to delete a branch that is not merged yet. That is a safety net.

### 4. Merge: the merge commit

Now a more realistic case. Two things happen at the same time.

First, start a new branch and change `analyse_run.py`:

```powershell
git switch -c feature/max-temperature
```

In VS Code, open `analyse_run.py`. Add one line at the end of the `main` function, right after the line that prints the mean temperature. Keep the 4 spaces of indentation:

```python
    print(f"Max temperature: {max(temperatures):.1f} C")
```

Save, then run and commit:

```powershell
uv run python analyse_run.py
git add analyse_run.py
git commit -m "Print max temperature"
```

The script prints three lines. The last one is `Max temperature: 88.4 C`.

Second, imagine a colleague changed `main` in the meantime. Do it yourself:

```powershell
git switch main
Add-Content README.md "Run it with: uv run python analyse_run.py"
git add README.md
git commit -m "Explain how to run analyse_run.py"
git log --oneline --graph --all --decorate
```

Now the history has split in two. Both lines have a new commit:

```
* <hash> (feature/max-temperature) Print max temperature
| * <hash> (HEAD -> main) Explain how to run analyse_run.py
|/
* <hash> Add bar to kPa conversion
...
```

Merge:

```powershell
git merge feature/max-temperature --no-edit
```

`--no-edit` accepts the automatic merge message. Without it, Git opens an editor. If that ever happens, close the editor tab in VS Code (or type `:wq` in vim) and the merge is completed.

Expected:

```
Merge made by the 'ort' strategy.
 analyse_run.py | 1 +
 1 file changed, 1 insertion(+)
```

Look at the result:

```powershell
git log --oneline --graph --all --decorate
```

```
*   <hash> (HEAD -> main) Merge branch 'feature/max-temperature'
|\
| * <hash> (feature/max-temperature) Print max temperature
* | <hash> Explain how to run analyse_run.py
|/
* <hash> Add bar to kPa conversion
...
```

The merge commit has two parents. The two changes touched different files, so Git combined them without help.

Clean up:

```powershell
git branch -d feature/max-temperature
git status
```

### 5. Explain it

Answer in one or two sentences each, to your neighbour or in writing.

1. Git made a fast-forward the first time and a merge commit the second time. Why?
2. What do you gain by doing your work on a branch instead of directly on `main`? What does it cost you?

## Check yourself

Short questions to test yourself after class. The answers are in `solutions/git/README.md`.

1. What is the difference between `git switch main` and `git switch -c feature/x`?
2. What happens to the files on disk when you switch branches?
3. Why can you safely delete a branch after it is merged?

## Optional: if you have time

### A merge conflict (10 minutes)

A **merge conflict** happens when two branches changed the same lines. Git cannot decide which version is right, so it asks you. This is normal and not an emergency.

The branch `experiment/psi-precision` changes the same line as `main` did (`BAR_TO_PSI`). Try to merge it:

```powershell
git merge experiment/psi-precision
```

Expected:

```
Auto-merging conversions.py
CONFLICT (content): Merge conflict in conversions.py
Automatic merge failed; fix conflicts and then commit the result.
```

Git stopped halfway. Check:

```powershell
git status
```

It lists `conversions.py` under "Unmerged paths", "both modified". Open the file in VS Code. You see markers:

```
<<<<<<< HEAD
BAR_TO_PSI = 14.504  # psi per bar, rounded to 3 decimals
=======
BAR_TO_PSI = 14.5038  # psi per bar, more precise
>>>>>>> experiment/psi-precision
```

The part between `<<<<<<<` and `=======` is your version (`main`). The part between `=======` and `>>>>>>>` is the other branch.

If you want to try the "With Copilot" task at the end of this page, do it now, before you resolve the conflict.

VS Code shows buttons above the markers: **Accept Current Change**, **Accept Incoming Change**, **Accept Both Changes**, and **Compare Changes**. Choose **Accept Incoming Change** to keep `14.5038`. You can also click **Resolve in Merge Editor** at the bottom right for a three-pane view. Check that no `<<<<<<<`, `=======` or `>>>>>>>` lines are left. Save the file. Then:

```powershell
git add conversions.py
git commit -m "Merge experiment/psi-precision"
git log --oneline --graph --all --decorate
```

Because you saved a finished merge in a normal `git commit -m`, you are done.

If you get lost, you can always go back to before the merge:

```powershell
git merge --abort
```

This works as long as you have not committed the merge yet.

### With Copilot

Do this while the conflict above is still open (after `git merge experiment/psi-precision`, before you resolve it). Select the conflict in `conversions.py`, open Copilot Chat (`Ctrl+Alt+I`) and ask:

> This is a merge conflict between HEAD (`main`) and the branch `experiment/psi-precision`. Explain what each side changed and suggest which side to keep.

Do you agree with its suggestion? What did you check before you accepted it? Copilot can read both lines, but it does not know how precise your test-bench results must be. That is your call as the engineer. Finish with `git add` and `git commit` as described above.
