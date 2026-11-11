# Exercise 3: Branches and merging

Core tasks: 1 to 4. Everything under "Optional" is extra.

Words to use: branch, HEAD, switch, merge, fast-forward, merge commit, merge conflict, rebase.

## Goal

Work on a change in a separate branch, then merge it back into `main`. See both kinds of merge: fast-forward and merge commit. Resolve a merge conflict.

## Why this matters

A branch lets you try something without breaking the version that works. Conflicts are normal as soon as two people touch the same script. Solving one calmly is a skill you need in the first week of working together.

## Background

A **branch** is a separate line of work. You make a branch to try something without disturbing `main`. When the work is good, you **merge** it back.

`main` is the branch that holds the "official" version of the project. A common rule: never work directly on `main`. Do your work on a branch, then merge.

A branch is only a label that points to a commit. Making one costs nothing. `HEAD` tells you which branch you are on.

There are two kinds of merge:

- **Fast-forward**: `main` did not change while you worked. Git just moves the `main` label forward. No new commit.
- **Merge commit**: `main` moved on while you worked. Git combines both lines in a new commit with two parents. If both lines changed the same lines, you decide first: a **merge conflict**.

## Setup

From the root of the course repository:

```powershell
uv run python exercises/git/setup_exercise.py 3
```

Run the `cd` command it prints. The repository contains a `.gitignore` file that hides Python cache folders (`__pycache__/`), so they do not clutter `git status`. Exercise 6 explains `.gitignore`. You get a repository with 4 commits on `main`, and a second branch called `experiment/psi-precision`. Leave that branch alone until task 4.

## Core tasks

Try each task with the hint closed. Open it when you are stuck.

### 1. Look at where you are

Question: which branches exist, which one are you on, and which commit does each branch point to? Show all branches in one graph.

<details>
<summary>Hint</summary>

```powershell
git branch
git log --oneline --graph --all --decorate
```

</details>

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

Result: a new branch `feature/pressure-kpa` with one commit on it. Branch names are free text. A common habit is `feature/<what-it-does>` or `fix/<what-it-fixes>`.

Open the folder in VS Code (`code .`). Add this function at the end of `conversions.py` and save:

```python


def bar_to_kpa(pressure_bar):
    """Convert a pressure from bar to kPa."""
    return pressure_bar * 100
```

Check: the graph shows your commit on top, on the branch `feature/pressure-kpa`, as a straight line on top of `main`:

```
* <hash> (HEAD -> feature/pressure-kpa) Add bar to kPa conversion
* <hash> (main) Round psi factor to 3 decimals
| * <hash> (experiment/psi-precision) Try a more precise psi factor
|/
* <hash> Add README
...
```

<details>
<summary>Hint</summary>

Create a branch and switch to it in one step. Expected: `Switched to a new branch 'feature/pressure-kpa'`.

```powershell
git switch -c feature/pressure-kpa
```

After you edited and saved the file:

```powershell
git status
git add conversions.py
git commit -m "Add bar to kPa conversion"
git log --oneline --graph --all --decorate
```

</details>

### 3. Merge: the fast-forward

Result: `main` contains the kPa function, and the branch `feature/pressure-kpa` is deleted.

Before you merge, go to `main` and look at `conversions.py` in VS Code. The new function is gone. It lives only on your branch. Switching branches changes the files on disk.

Check: the merge output says `Fast-forward`:

```
Updating <hash>..<hash>
Fast-forward
 conversions.py | 5 +++++
 1 file changed, 5 insertions(+)
```

"Fast-forward" means `main` had no new commits, so Git only moved the label. Check the file again: the function is back, now on `main`.

Delete the branch once it is merged. The commits are safe. The delete command refuses to delete a branch that is not merged yet. That is a safety net.

<details>
<summary>Hint</summary>

```powershell
git switch main
git merge feature/pressure-kpa
git branch -d feature/pressure-kpa
git log --oneline --graph --all --decorate
```

</details>

### 4. Merge: a conflict

Now `main` and the branch `experiment/psi-precision` changed the same line (`BAR_TO_PSI`). Git cannot decide which version is right, so it asks you. This is a **merge conflict**. It is normal and not an emergency.

Result: `experiment/psi-precision` is merged into `main`, with `BAR_TO_PSI = 14.5038` and no conflict markers left in the file.

Steps:

1. Make sure you are on `main`, then merge `experiment/psi-precision` into it. Expected:

```
Auto-merging conversions.py
CONFLICT (content): Merge conflict in conversions.py
Automatic merge failed; fix conflicts and then commit the result.
```

2. Git stopped halfway. `git status` lists `conversions.py` under "Unmerged paths", "both modified".

3. Open `conversions.py` in VS Code. You see markers:

```
<<<<<<< HEAD
BAR_TO_PSI = 14.504  # psi per bar, rounded to 3 decimals
=======
BAR_TO_PSI = 14.5038  # psi per bar, more precise
>>>>>>> experiment/psi-precision
```

The part between `<<<<<<<` and `=======` is your version (`main`). The part between `=======` and `>>>>>>>` is the other branch.

4. VS Code shows buttons above the markers: **Accept Current Change**, **Accept Incoming Change**, **Accept Both Changes**, and **Compare Changes**. Choose **Accept Incoming Change** to keep `14.5038`. You can also click **Resolve in Merge Editor** at the bottom right for a three-pane view. Check that no `<<<<<<<`, `=======` or `>>>>>>>` lines are left. Save the file.

5. Finish the merge: mark the file as resolved and make the merge commit with the message `Merge experiment/psi-precision`. Look at the graph. The merge commit has two parents. Because you saved a finished merge with a normal `git commit -m`, you are done.

<details>
<summary>Hint</summary>

Steps 1 and 2:

```powershell
git switch main
git merge experiment/psi-precision
git status
```

Step 5:

```powershell
git add conversions.py
git commit -m "Merge experiment/psi-precision"
git log --oneline --graph --all --decorate
```

</details>

If you get lost, you can always go back to before the merge:

```powershell
git merge --abort
```

This works as long as you have not committed the merge yet.

## Check yourself

Short questions to test yourself after class. The answers are in `solutions/git/README.md`.

1. What is the difference between `git switch main` and `git switch -c feature/x`?
2. What happens to the files on disk when you switch branches?
3. Why can you safely delete a branch after it is merged?

## Optional: if you have time

### 5. A merge commit without a conflict

When both lines changed but not the same lines, Git joins them for you. Make a branch with a change in `analyse_run.py`, commit it, then switch to `main` and commit a change in `README.md`:

```powershell
git switch -c feature/max-temperature
# edit analyse_run.py, then:
git commit -am "Print max temperature"
git switch main
Add-Content README.md "Run it with: uv run python analyse_run.py"
git commit -am "Explain how to run analyse_run.py"
git merge feature/max-temperature --no-edit
git log --oneline --graph --all --decorate
git branch -d feature/max-temperature
```

`--no-edit` accepts the automatic merge message. Without it, Git opens an editor. If that happens, close the editor tab in VS Code (or type `:wq` in vim) and the merge is completed. The merge commit has two parents, and no help from you was needed.

Task 6 solves the same situation in a different way.

### 6. Rebase instead of merge

Same situation as task 5: `main` moved while you worked on a branch. A **rebase** replays your commits on top of the latest `main`, so the history stays a straight line. Start on `main`, with a clean `git status`.

1. Make a branch and commit a change on it. In `analyse_run.py`, add this line at the end of the `main` function, after the line that prints the mean temperature (keep the 4 spaces):

```python
    print(f"Min temperature: {min(temperatures):.1f} C")
```

```powershell
git switch -c feature/min-temperature
git commit -am "Print min temperature"
git log --oneline -1
```

Write down the hash of your commit.

2. Let `main` move on:

```powershell
git switch main
Add-Content README.md "Output: mean pressure and temperature."
git commit -am "Describe the output in the README"
git log --oneline --graph --all --decorate
```

The graph shows two lines: your branch and `main` both have a new commit.

3. Go back to your branch and rebase it on `main`:

```powershell
git switch feature/min-temperature
git rebase main
git log --oneline --graph --all --decorate
```

Expected: `Successfully rebased and updated refs/heads/feature/min-temperature.` The graph is now one straight line, with your commit on top. Compare its hash with the one you wrote down.

4. Merge. This is a fast-forward, because your branch is already ahead of `main`:

```powershell
git switch main
git merge feature/min-temperature
git branch -d feature/min-temperature
git log --oneline --graph --all --decorate
```

If a rebase hits a conflict, fix the file, then `git add <file>` and `git rebase --continue`. To give up: `git rebase --abort`.

Questions:

1. Compare the hash of your commit before and after the rebase. Why did it change?
2. Why is it safe to rebase here, and when would it not be?

### With Copilot

Do this during core task 4: after `git merge experiment/psi-precision`, before you resolve the conflict. Select the conflict in `conversions.py`, open Copilot Chat (`Ctrl+Alt+I`) and ask:

> This is a merge conflict between HEAD (`main`) and the branch `experiment/psi-precision`. Explain what each side changed and suggest which side to keep.

Do you agree with its suggestion? What did you check before you accepted it? Copilot can read both lines, but it does not know how precise your test-bench results must be. That is your call as the engineer. Finish with `git add` and `git commit` as in task 4.

## Challenge

For those who finish early. No commands given: find them with `git help <command>` or Copilot, and check the result with `git log` and `git status`.

Make a new branch and edit `conversions.py` on it, but do not commit. Now you must look at `main` to check something. Switch to `main` without committing half-finished work and without losing it. Then come back and carry on with your edits where you left them.

## Open question

Git does not record on which branch a commit was made. So how can `git log --graph` draw the lines? And what is a branch, physically, inside the `.git` folder?
