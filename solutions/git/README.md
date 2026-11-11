# Git exercises: solutions

Expected command sequences and answers, per exercise and per task. Hashes are written as `<hash>`. Yours will differ unless noted.

Commands are for Windows PowerShell 5.1. Replace `anna` with your own name.

## Exercise 1: Your first commit

### Task 3: two edits in one file, and a typo in history

```powershell
git add -p conversions.py
# hunks come in file order: n for the docstring hunk, y for the new function
git diff --staged
git commit -m "Add kelvin_to_celcius"
git add conversions.py
git commit -m "Reword the module docstring"
git log --oneline
# the typo is in the commit before the last: take both commits apart, keep the edits
git reset --soft HEAD~2
git reset
git add -p conversions.py
# n for the docstring hunk, y for the new function
git commit -m "Add kelvin_to_celsius"
git add conversions.py
git commit -m "Reword the module docstring"
git log --oneline
git status
```

`git add -p` goes through the changes hunk by hunk and stages only the ones you accept, so one file can go into two commits. The two edits must be far enough apart to be separate hunks (`s` splits a hunk further).

`git reset --soft HEAD~2` moves the branch back two commits and keeps all their changes staged. `git reset` then unstages them, so the file is changed in the working tree and nothing is lost. The edits are still in the file, so the two commits can be made again with the right message. `git log --oneline` then shows six commits and `git status` is clean. Other routes that work: `git reset --soft HEAD~1`, `git stash`, `git commit --amend -m "..."` on the earlier commit, `git stash pop`, then commit again. If a commit seems lost, `git reflog` still lists it.

### Open question

About 50 MB, once (less if the content compresses). Git stores the content of a file under the hash of that content, and the file name is not part of it. The names live in the snapshot, which points twice at the same stored content. The two commits do not get the same hash. The hash of a commit covers the snapshot, the parent, the author, the committer, the dates and the message. Your names and the times differ, so the hashes differ, although both commits point at the same snapshot.

## Exercise 2: Explore the history

### Task 3: undo one old commit, keep the later ones

```powershell
git log --oneline
git revert <hash-of-Fix-Kelvin-offset>
# Git stops: CONFLICT in conversions.py
git status
# in conversions.py keep BAR_TO_PSI = 14.5038 and KELVIN_OFFSET = 273.0, delete the marker lines
git add conversions.py
git revert --continue
git log --oneline
uv run python analyse_run.py
```

`git revert` makes a new commit that does the opposite of the chosen commit, so the original stays in the log, followed by `Revert "Fix Kelvin offset"`. Here it conflicts: the revert wants `KELVIN_OFFSET = 273.0` and `BAR_TO_PSI = 14.5`, but the later commit "Use more precise bar to psi factor" changed the line next to it, and Git does not guess when changes touch neighbouring lines. The conflict shows both versions between `<<<<<<< HEAD` and `>>>>>>>`. The result to keep is the later `BAR_TO_PSI = 14.5038` plus the reverted `KELVIN_OFFSET = 273.0`. `git revert --continue` opens an editor for the message (save and close, or use `git revert --continue --no-edit`). `git revert --abort` goes back to before the revert. `analyse_run.py` then prints 108.78 psi and 358.33 K. (Checked with the setup script history.)

### Open question

`git reflog` lists where HEAD has been, including commits that no branch points to. Find the hash there, then `git switch -c rescue <hash>` gives the commit a branch again. Git removes unreferenced commits only after a period, 30 or 90 days by default, so there is time to find them. This does not help for edits that were never committed.

## Exercise 3: Branches and merging

### Tasks 1 and 2

```powershell
uv run python exercises/git/setup_exercise.py 3
cd "<path printed by the script>"

# task 1
git switch -c feature/pressure-kpa
# edit conversions.py: add bar_to_kpa at the end
git add conversions.py
git commit -m "Add bar to kPa conversion"
git switch main
git merge feature/pressure-kpa
git branch -d feature/pressure-kpa

# task 2
git merge experiment/psi-precision
# open conversions.py in VS Code, click "Accept Incoming Change"
# check that no <<<<<<<, ======= or >>>>>>> remains, save
git add conversions.py
git commit -m "Merge experiment/psi-precision"
git log --oneline --graph --all --decorate
```

### Task 3

```powershell
Add-Content README.md "TODO: check the units"
git switch feature/temperature-report
git rebase main
# error: cannot rebase: You have unstaged changes.
git stash
git rebase main
# CONFLICT in conversions.py on "Add Celsius to Fahrenheit conversion"
# edit conversions.py: keep both functions (bar_to_kpa first, then celsius_to_fahrenheit), no markers
git add conversions.py
git rebase --continue
# the editor opens for the commit message: save and close it
# Successfully rebased and updated refs/heads/feature/temperature-report.
git switch main
git merge feature/temperature-report
git branch -d feature/temperature-report
git stash pop
git log --oneline --graph --all --decorate
git status --short
uv run python analyse_run.py
```

Notes:

- Git refuses to rebase with uncommitted changes. `git stash` parks the README line, `git stash pop` brings it back. `git rebase --autostash main` does both in one go.
- The conflict comes in the second commit, because `main` and the branch both appended to the end of `conversions.py`. The rebase stops there. After `git add` and `git rebase --continue` the third commit is replayed without trouble. `git rebase --abort` returns to before the rebase.
- Expected: the graph in the README, ` M README.md` from `git status --short`, and four lines from `analyse_run.py`: mean pressure, mean temperature, min temperature and mean temperature in Fahrenheit. Checked with the setup script.
- Why the hashes changed: a commit's hash covers its content, its parent and its metadata. After the rebase each commit has a different parent (the first sits on the new tip of `main`, the others on the commit before them), so Git made new commits with the same changes and new hashes. The old ones are no longer on the branch. That is also why rebasing commits that are already pushed and used by others is a bad idea: they still have the old ones.

### Open question

Each commit stores the hash of its parent, or of both parents for a merge commit. `git log --graph` draws the lines from those links, not from branch names. A branch is a small text file under `.git/refs/heads/` that contains one commit hash (or a line in `.git/packed-refs`). Creating a branch writes that file, which is why it costs nothing.

## Exercise 4: Clone from the remote and push a branch

### Tasks 1 and 2

```powershell
New-Item -ItemType Directory -Force "$HOME\git-exercises"
cd "$HOME\git-exercises"
git clone https://<forge>/<organisation>/<training-repo>.git
cd <training-repo>
git remote -v
git branch -a
git log -1
git switch -c feature/anna-intro
New-Item -ItemType Directory -Force participants/anna
Set-Content participants/anna/about.md "# Anna`n`nI work at Atlas Copco. I use Python to analyse compressor test data."
git add participants/anna/about.md
git commit -m "Add intro for Anna"
git push -u origin feature/anna-intro
git status
git branch -a
```

`origin` is the default name Git gives to the remote you cloned from. `git branch -a` also lists the remote-tracking branches (`remotes/origin/...`), which are your laptop's record of what the remote had at the last fetch. `-u` sets the upstream, so later `git push` and `git pull` need no arguments.

### Task 3

The second clone `..\other` plays the colleague (a neighbour does the same from their laptop).

```powershell
# in your clone: a local commit, not pushed
Set-Content participants/anna/mine.md "my change"
git add participants/anna/mine.md
git commit -m "My commit"

# in the other clone: switch to the branch, commit, push
git switch feature/anna-intro
Set-Content participants/anna/theirs.md "colleague change"
git add participants/anna/theirs.md
git commit -m "Colleague commit"
git push

# back in your clone: the push is rejected
git push
git fetch
git status -sb
git log --oneline --graph --all
git pull --no-rebase
git push
```

Expected: `git push` ends with `! [rejected] ... (fetch first)`. After `git fetch`, `git status -sb` shows `[ahead 1, behind 1]` and the graph shows `My commit` and `Colleague commit` as two lines from the same parent. `git pull --no-rebase` makes a merge commit (`Merge branch 'feature/anna-intro' of ...`) and the following `git push` is accepted. Also fine: `git fetch` then `git merge origin/feature/anna-intro`, or `git pull --rebase` (this rewrites only the unpushed local commit, so no force is needed).

`--no-rebase` is there because a plain `git pull` on diverged branches stops with `fatal: Need to specify how to reconcile divergent branches` unless `pull.rebase` is configured.

`git fetch` downloads the new commits and moves `origin/feature/anna-intro`. It does not touch your branch or your files. `git pull` is `git fetch` followed by a merge (or rebase) of the fetched commits into your current branch.

### Open question

They sit under the remote-tracking branches such as `origin/main` and `origin/<other branches>`. `git branch -a` lists them. Offline you can commit, branch, merge, read the history and diff. You cannot push, pull, fetch or open a pull request, because those need the remote.

## Exercise 5: Pull request, review and merge

### Tasks 1 and 2

Web steps on the forge: **Compare & pull request** (or **Pull requests > New pull request**), from `feature/anna-intro` into `main`, title, description, reviewer, **Create pull request**. The reviewer opens the PR, reads **Files changed**, comments on a line (blue **+**, **Start a review**), then **Review changes**, **Approve**, **Submit review**. The author clicks **Merge pull request**, keeps "Create a merge commit", confirms, then **Delete branch**.

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

### Task 3

```powershell
git switch main
git pull
git switch -c feature/anna-conflict
# change the same line of README.md as your neighbour does, save
git add README.md
git commit -m "Change the README intro"
git push -u origin feature/anna-conflict
# open the PR, merge the first PR of the two (needs an approval)
# the second PR now says "This branch has conflicts that must be resolved": fix it on your laptop
git fetch
git merge origin/main
```

The merge stops with `CONFLICT (content): Merge conflict in README.md`, and `git status` shows `UU README.md`. Open the file, keep the line you want, remove the markers, then:

```powershell
git add README.md
git commit -m "Merge main into feature/anna-conflict"
git push
# the PR updates itself: merge it
```

`git fetch` plus `git merge origin/main` is used instead of `git pull origin main` because on a branch that has diverged from `main`, a plain `git pull` can stop with `fatal: Need to specify how to reconcile divergent branches`.

The second PR conflicts because `main` now holds a different version of the same line. Merging `main` into your branch moves the decision to your laptop, where you can see both sides. The result is one merge commit with `main` as second parent, and the plain `git push` works because the branch only grew.

The rebase route:

```powershell
git fetch
git rebase origin/main
# fix README.md, then
git add README.md
git rebase --continue
git push --force-with-lease
```

The rebase replays your commit on top of `origin/main`, so the commit gets a new hash. The remote branch still holds the old one, so a plain `git push` is rejected as non-fast-forward. `--force-with-lease` overwrites the remote branch only if it is still where your last fetch saw it, so it does not wipe a colleague's push that you have not seen. A plain `--force` would.

Which one for the branch protection rule: either answer is fine if the reason is given. Merge is the safer default for a team that is new to Git: it never rewrites pushed commits, a reviewer's comments stay attached to the same commits, and nobody needs a force push. Rebase gives a straight history, but it needs the force option and everyone sharing the branch must know to expect it. Do not leave real changes in the shared README afterwards; the trainer may reset it.

### Open question

A squash merge makes one new commit on `main` with a new hash and a single parent. The commits on your branch are not ancestors of `main`, and `git branch -d` checks ancestry, not content. So Git sees commits on the branch that `main` does not contain, although the same changes are there. `git branch -D` deletes the branch anyway. Use it once the pull request shows Merged.

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

## The "With Copilot" task of exercise 6

Generated commit messages describe the diff. Add the reason when it is not obvious.
