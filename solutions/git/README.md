# Git exercises: solutions

Expected command sequences and answers to the "check yourself" questions. Each exercise has the core part first and then the optional part. Hashes are written as `<hash>`. Yours will differ unless noted.

Commands are for Windows PowerShell 5.1. Replace `anna` with your own name.

## Exercise 1: Your first commit

### Core

```powershell
uv run python exercises/git/setup_exercise.py 1
cd "<path printed by the script>"
# task 1
git config user.name
git config user.email
# task 2
git init -b main
git status
# task 3
git add conversions.py
git status
git commit -m "Add bar to psi conversion"
git log --oneline
git status
# task 4
git add measurements.csv
git commit -m "Add first measurements"
git log --oneline
# task 5: add celsius_to_kelvin to conversions.py, add the line 4,8.5,91.2 to measurements.csv
git status
git diff
# task 6
git add conversions.py
git diff
git diff --staged
git commit -m "Add Celsius to Kelvin conversion"
git add measurements.csv
git commit -m "Add fourth measurement run"
git log --oneline
git status
# task 7: edit the docstring of bar_to_psi, then
git add conversions.py
# change BAR_TO_PSI to 14.5038, do not stage
git status
git diff --staged
git diff
git commit -m "Clarify the bar_to_psi docstring"
git add conversions.py
git commit -m "Use a more precise psi factor"
git log --oneline
```

Final `git log --oneline` has six commits, newest first: "Use a more precise psi factor", "Clarify the bar_to_psi docstring", "Add fourth measurement run", "Add Celsius to Kelvin conversion", "Add first measurements", "Add bar to psi conversion". `git status` says "nothing to commit, working tree clean".

Task 3, why keep a file out of a commit: a commit should say one thing. A file can be unfinished, unrelated to this change, generated, or private (data, credentials). Left out, it does not end up in a review or in history, and it is easy to commit later on its own.

Task 6, the diffs after staging `conversions.py`: plain `git diff` shows only what is still unstaged, so the `measurements.csv` change and nothing of `conversions.py`. `git diff --staged` shows what is waiting in the staging area, the `celsius_to_kelvin` function.

Task 7: `git status` lists `conversions.py` twice, once under "Changes to be committed" (the docstring) and once under "Changes not staged for commit" (the `BAR_TO_PSI` edit). Staging records the content of the file at the moment of `git add`. An edit made after it is a new change against the staged version. `git diff --staged` shows the docstring, `git diff` shows the constant. The first commit takes only what was staged. A second `git add` stages the rest.

Check yourself:

1. `git diff` shows the changes that are not staged yet (working tree against staging area). `git diff --staged` shows the staged changes (staging area against the last commit).
2. "Untracked" means Git sees the file in the folder, but it is not in any commit and not staged.
3. Without `-m`, Git opens a text editor to ask for the message. `-m` gives the message on the command line.
4. You staged the file, then edited it again. The staged version and the newer working-tree version differ, so the file has a staged change and an unstaged change at the same time.

### Optional

Challenge (two commits from one editing session, both edits saved in one file before staging):

```powershell
git add -p conversions.py
# answer y for the hunk of the first edit, n for the other
git commit -m "Add kelvin_to_celsius"
git add conversions.py
git commit -m "Reword the module docstring"
git log --oneline
```

`git add -p` goes through the changes hunk by hunk and stages only the ones you accept, so one file can go into two commits. Check with `git diff --staged` before each commit. The two edits must be far enough apart to be separate hunks (`s` splits a hunk further).

More: `git log --stat` adds the list of changed files and the number of added and removed lines per commit. The `.git` folder is hidden. `ls -Force` shows it.

### Open question

About 50 MB, once (less if the content compresses). Git stores the content of a file under the hash of that content, and the file name is not part of it. The names live in the snapshot, which points twice at the same stored content. The two commits do not get the same hash. The hash of a commit covers the snapshot, the parent, the author, the committer, the dates and the message. Your names and the times differ, so the hashes differ, although both commits point at the same snapshot.

## Exercise 2: Explore the history

### Core

```powershell
uv run python exercises/git/setup_exercise.py 2
cd "<path printed by the script>"
git status
git log --oneline
git show <hash-of-Fix-Kelvin-offset>
git log conversions.py
# edit conversions.py: KELVIN_OFFSET = 0
git status
git diff
git restore conversions.py
git status
```

Check yourself:

1. `git show <hash>`.
2. Sofie Claes, in the commit "Fix Kelvin offset" (5 March 2025). She changed `273.0` to `273.15`. Jan Peeters made the last change to `BAR_TO_PSI`; Anna Verhoeven wrote the first version of the file.
3. `git log conversions.py` lists only the commits that touched that file: 4 commits instead of 5. "Add measurements and analyse_run script" is left out because it did not change `conversions.py`.

### Optional

```powershell
git diff <hash-of-first-commit> <hash-of-last-commit>
git diff HEAD~1 HEAD
git log -S 273.15
git log --oneline --author=Jan
git blame conversions.py
git switch --detach <hash-of-Add-measurements-and-analyse_run-script>
uv run python analyse_run.py
git switch main
uv run python analyse_run.py
# edit README.md, add a line
git add README.md
git restore --staged README.md
git restore README.md
```

`git log -S 273.15` and `git blame conversions.py` both point to Sofie Claes and the commit "Fix Kelvin offset".

Output of `analyse_run.py` on the old commit (offset 273.0) and on `main` (offset 273.15):

```
Mean pressure: 7.50 bar (108.75 psi)
Mean temperature: 85.3 C (358.33 K)

Mean pressure: 7.50 bar (108.78 psi)
Mean temperature: 85.3 C (358.48 K)
```

Answers:

1. `git switch --detach <hash>` checks out an old commit without being on a branch (detached HEAD), so you can look around. Return with `git switch main`.
2. `git restore <file>` discards uncommitted edits in the working tree. `git restore --staged <file>` only takes the file out of the staging area and keeps your edit.

More: `git log --oneline -- analyse_run.py` gives "Add measurements and analyse_run script". `git log --stat` shows that the first commit changed the most files (3: `conversions.py`, `README.md` and `.gitignore`). `--reverse` prints the oldest commit first.

### Challenge: undo one commit, keep the history

```powershell
git log --oneline
git revert <hash-of-Use-more-precise-bar-to-psi-factor> --no-edit
git log --oneline
git show HEAD
```

`git revert` makes a new commit that does the opposite of the chosen commit. The original stays in the log, followed by `Revert "Use more precise bar to psi factor"`, and `BAR_TO_PSI` is `14.5` again. It applies without a conflict because it is the newest commit and no later commit touches that line. (Checked with the setup script history.)

### Open question

`git reflog` lists where HEAD has been, including commits that no branch points to. Find the hash there, then `git switch -c rescue <hash>` gives the commit a branch again. Git removes unreferenced commits only after a period, 30 or 90 days by default, so there is time to find them. This does not help for edits that were never committed.

## Exercise 3: Branches and merging

### Core

```powershell
uv run python exercises/git/setup_exercise.py 3
cd "<path printed by the script>"
git branch
git log --oneline --graph --all --decorate

# fast-forward merge
git switch -c feature/pressure-kpa
# edit conversions.py: add bar_to_kpa at the end
git add conversions.py
git commit -m "Add bar to kPa conversion"
git log --oneline --graph --all --decorate
git switch main
git merge feature/pressure-kpa
git branch -d feature/pressure-kpa

# merge conflict
git merge experiment/psi-precision
git status
# open conversions.py in VS Code, click "Accept Incoming Change" (or choose your own line)
# check that no <<<<<<<, ======= or >>>>>>> remains, save
git add conversions.py
git commit -m "Merge experiment/psi-precision"
git log --oneline --graph --all --decorate
```

There is no single correct result. Either value is acceptable, as long as the markers are gone, the file still runs (`uv run python analyse_run.py`) and the merge is committed. The line that survives is `BAR_TO_PSI = 14.504  # ...` (current) or `BAR_TO_PSI = 14.5038  # ...` (incoming). If someone is lost: `git merge --abort` returns to the state before the merge. The new `bar_to_kpa` function from task 3 is not part of the conflict.

Check yourself:

1. `git switch main` goes to an existing branch. `git switch -c feature/x` creates the new branch at the current commit and goes to it.
2. Git replaces the files in your folder with the version of the branch you switch to. Your uncommitted edits stay, as long as they do not clash with the files that change.
3. A branch is only a label. The commits are in `main` too, so nothing is lost. `git branch -d` also refuses if the branch is not merged.

### Optional

Merge commit without a conflict (task 5):

```powershell
git switch -c feature/max-temperature
# edit analyse_run.py: add the max temperature print line
git commit -am "Print max temperature"
git switch main
Add-Content README.md "Run it with: uv run python analyse_run.py"
git commit -am "Explain how to run analyse_run.py"
git merge feature/max-temperature --no-edit
git log --oneline --graph --all --decorate
git branch -d feature/max-temperature
```

Rebase instead of merge (task 6):

```powershell
git switch -c feature/min-temperature
# edit analyse_run.py: add the min temperature print line
git commit -am "Print min temperature"
git log --oneline -1
git switch main
Add-Content README.md "Output: mean pressure and temperature."
git commit -am "Describe the output in the README"
git log --oneline --graph --all --decorate
git switch feature/min-temperature
git rebase main
git log --oneline --graph --all --decorate
git switch main
git merge feature/min-temperature
git branch -d feature/min-temperature
```

Answers:

1. A commit's hash covers its content, its parent and its metadata. After the rebase the commit has a different parent (the new tip of `main`), so Git has made a new commit with the same change and a new hash. The old one is no longer on the branch.
2. It is safe here because the branch was never pushed: nobody else has the old commits. It is not safe for commits that are already pushed and used by others. They hold the old commits, and after your rewrite and a force push they get duplicates and a confusing history. If you must, use `git push --force-with-lease`, and rebase before the first push instead.

Both tasks solve the same situation. Merge records what happened. Rebase tidies the branch before it is shared and leaves a straight history.

The "With Copilot" part is covered at the end of this file.

### Challenge: park half-finished work

```powershell
# you have uncommitted edits in conversions.py
git stash
git switch main
# look around, run what you need
git switch <your-branch>
git stash pop
```

`git stash` saves the uncommitted edits and gives you a clean working tree, so the switch works. `git stash pop` puts the edits back and removes the stash. `git stash list` shows what is parked.

### Open question

Each commit stores the hash of its parent, or of both parents for a merge commit. `git log --graph` draws the lines from those links, not from branch names. A branch is a small text file under `.git/refs/heads/` that contains one commit hash (or a line in `.git/packed-refs`). Creating a branch writes that file, which is why it costs nothing.

## Exercise 4: Clone from Azure DevOps and push a branch

### Core

```powershell
New-Item -ItemType Directory -Force "$HOME\git-exercises"
cd "$HOME\git-exercises"
git clone https://dev.azure.com/<organisation>/<project>/_git/<training-repo>
cd <training-repo>
git status
git remote -v
git branch
git branch -a
uv run python check_setup.py
git switch -c feature/anna-intro
New-Item -ItemType Directory -Force participants/anna
Set-Content participants/anna/about.md "# Anna`n`nI work in FD. I use Python to analyse compressor test data."
git add participants/anna/about.md
git commit -m "Add intro for Anna"
git push -u origin feature/anna-intro
git status
git branch -a
```

Check yourself:

1. `git branch` lists only local branches. `git branch -a` also lists the remote-tracking branches (`remotes/origin/...`), which are your laptop's record of what the remote has.
2. `origin` is the default name Git gives to the remote you cloned from, here the Azure DevOps repository.
3. The branch exists only locally, so the remote needs to create it. `-u` also sets the upstream, so later `git push` and `git pull` need no arguments.
4. So that people do not change the same files and cause conflicts.

Stretch: `git fetch` followed by `git branch -a` lists the branches other participants pushed. In the graph, `origin/main` is where the remote `main` was at the last fetch, and your branch is one commit ahead of it.

### Open question

They sit under the remote-tracking branches such as `origin/main` and `origin/<other branches>`. `git branch -a` lists them. Offline you can commit, branch, merge, read the history and diff. You cannot push, pull, fetch or open a pull request, because those need the remote.

## Exercise 5: Pull request, review and merge

### Core

Web steps in Azure DevOps: **Repos > Pull requests > New pull request**, from `feature/anna-intro` into `main`, title, description, reviewer, **Create**. The reviewer opens the PR, reads **Files**, comments, **Approve**. The author clicks **Complete**, keeps "Merge (no fast-forward)", ticks "Delete feature/anna-intro after merging", **Complete merge**.

```powershell
git switch main
git pull
ls participants
git log --oneline --graph -10
git branch -d feature/anna-intro
git fetch --prune
git branch -a
```

Final `git branch -a`:

```
* main
  remotes/origin/HEAD -> origin/main
  remotes/origin/main
```

If `main` moved and the PR shows conflicts:

```powershell
git switch feature/anna-intro
git pull origin main
# fix the conflict in VS Code
git add <file>
git commit -m "Merge main into feature/anna-intro"
git push
```

Check yourself:

1. The reviewer saw the changes of the PR in one view (Files tab) with fresh eyes. They could spot unclear text, mistakes or files that should not be there.
2. `git pull` is `git fetch` (download new commits) plus a merge of them into your current branch. `git fetch` only downloads and does not touch your files or branch.
3. Their PRs were merged into `main` on the server, and you pulled `main`.
4. It removes your local record of remote branches that were deleted on the server (here `origin/feature/anna-intro`).

A PR shows conflicts when someone else merged a change into `main` that touches the same lines as your branch.

Challenge (a conflict between two pull requests):

```powershell
git switch main
git pull
git switch -c feature/anna-conflict
# change the same line of README.md as your neighbour does, save
git add README.md
git commit -m "Change the README intro"
git push -u origin feature/anna-conflict
# open the PR, complete the first PR of the two (needs an approval)
# the second PR now shows Conflicts: fix it on your laptop
git switch feature/anna-conflict
git pull origin main
# fix README.md in VS Code, keep the line you want
git add README.md
git commit -m "Merge main into feature/anna-conflict"
git push
# the PR updates itself: complete it
```

The second PR conflicts because `main` now holds a different version of the same line. Merging `main` into your branch moves the decision to your laptop, where you can see both sides. Do not leave real changes in the shared README afterwards; the trainer may reset it.

Branching models: trunk-based development uses short-lived branches into one `main` branch. GitFlow uses long-lived `develop`, `release/*` and `hotfix/*` branches next to `main`. The exercise followed the trunk-based style.

### Open question

A squash merge makes one new commit on `main` with a new hash and a single parent. The commits on your branch are not ancestors of `main`, and `git branch -d` checks ancestry, not content. So Git sees commits on the branch that `main` does not contain, although the same changes are there. `git branch -D` deletes the branch anyway. Use it once the pull request shows Completed.

## Exercise 6: Git in VS Code

Trainer demo in class. Participants repeat it alone afterwards. Everything here is optional.

Equivalent commands for the VS Code clicks:

| VS Code | Command line |
|---|---|
| Bottom-left branch name, **Create new branch...** | `git switch -c feature/anna-vscode` |
| **+** next to a file | `git add <file>` |
| **Commit** | `git commit -m "..."` |
| **Publish Branch** | `git push -u origin feature/anna-vscode` |
| **...** > **Pull** | `git pull` |
| `Git: Delete Branch...` | `git branch -d feature/anna-vscode` |

The `.gitignore` part:

```powershell
git switch main
git switch -c feature/anna-ignore
New-Item -ItemType Directory -Force participants/anna/output
Set-Content participants/anna/output/summary.csv "run,mean_bar"
Set-Content participants/anna/output/plot.png "not a real picture"
Set-Content participants/anna/.gitignore "output/`n*.png`n.venv/`n__pycache__/"
git status
git add participants/anna/.gitignore
git commit -m "Add .gitignore for Anna's folder"
git status
```

Before the `.gitignore` exists, `git status` lists `participants/anna/output/`. Afterwards it lists only `participants/anna/.gitignore` as new. After the commit: "nothing to commit, working tree clean".

Check yourself:

1. The **+** (Stage Changes) button.
2. `U` is untracked (new file, not yet in Git). `M` is modified (a tracked file with changes).
3. `git push -u origin <branch>`: it creates the branch on the remote and links the local branch to it.
4. No. A file that is already tracked stays tracked and stays in the history. You would need `git rm --cached <file>` to stop tracking it (not covered in this training).

### Open question

The repository is about 200 MB larger (less if the data compresses well), because the file is still in the history. `.gitignore` only affects files that Git does not track yet, so it does nothing for a file that is already committed. Removing it needs a history rewrite, for example with `git filter-repo`, and a forced push. Everyone then has to clone again. It is cheaper to ignore data files from the start.

## The "With Copilot" tasks

These optional tasks have no single right answer. What matters is the judgement:

- Exercise 1: a good result is a diff with only the new `kelvin_to_celsius` function (`temperature_k - 273.15`). Anything else in the diff (renamed functions, reformatting, new comments) was not asked for and should be questioned.
- Exercise 2: the vague prompt usually gives a large diff (type hints, docstrings, validation, renames) that is hard to review. The precise prompt gives a few added lines. The difference is the precision of the request, in the vocabulary of the code.
- Exercise 3: Copilot can explain both sides, but which precision the test bench needs is a domain decision. A good check: read both lines, run `uv run python analyse_run.py` after resolving, and look at `git diff --staged`.
- Exercise 4: you can verify what `git fetch` did to `origin/main` and that your files did not change. You cannot verify claims about cases you did not try.
- Exercise 5: the draft usually describes what changed. It cannot know why, how you tested it, or what the reviewer should look at. Those are the parts to add.
- Exercise 6: generated commit messages describe the diff. Add the reason when it is not obvious.
