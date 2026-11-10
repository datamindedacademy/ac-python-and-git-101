# Git exercises: solutions

Expected command sequences and answers to the "check yourself" questions. Hashes are written as `<hash>`. Yours will differ unless noted.

Commands are for Windows PowerShell 5.1. Replace `anna` with your own name.

## Exercise 1: Your first commit

```powershell
uv run python exercises/git/setup_exercise.py 1
cd "<path printed by the script>"
git config user.name
git config user.email
git init -b main
git status
git add conversions.py
git status
git commit -m "Add bar to psi conversion"
git log
git log --oneline
# edit conversions.py: add celsius_to_kelvin
git status
git diff
git add conversions.py
git diff
git diff --staged
git commit -m "Add Celsius to Kelvin conversion"
git add measurements.csv
git commit -m "Add first measurements"
git status
```

Final `git log --oneline`:

```
<hash> Add first measurements
<hash> Add Celsius to Kelvin conversion
<hash> Add bar to psi conversion
```

Answers:

1. `git add` moves a change from the working tree to the staging area. `git commit` moves it from the staging area to the repository.
2. `git diff` compares the working tree with the staging area. After `git add` they are the same, so nothing shows. `git diff --staged` shows the staged change (staging area against the last commit).
3. Each commit should be one logical change with its own message. The function and the data file are unrelated.
4. Git sees the file in the folder, but it is not in any commit and not staged. Git does not follow it.
5. Without `-m`, Git opens a text editor to ask for the message. `-m` gives the message on the command line.

Stretch: `git log --stat` adds the list of changed files and the number of added and removed lines per commit. The `.git` folder is hidden. `ls -Force` shows it.

## Exercise 2: Explore the history

```powershell
uv run python exercises/git/setup_exercise.py 2
cd "<path printed by the script>"
git status
git log --oneline
git log
git show <hash-of-Fix-Kelvin-offset>
git diff <hash-of-first-commit> <hash-of-last-commit>
git diff HEAD~1 HEAD
git log -S 273.15
git log --oneline -- conversions.py
git log --oneline --author=Jan
git blame conversions.py
git switch --detach <hash-of-Add-measurements-and-analyse_run-script>
uv run python analyse_run.py
git switch main
uv run python analyse_run.py
# edit conversions.py: KELVIN_OFFSET = 0
git status
git diff
git restore conversions.py
git status
```

Output of `analyse_run.py` on the old commit (offset 273.0) and on `main` (offset 273.15):

```
Mean pressure: 7.50 bar (108.75 psi)
Mean temperature: 85.3 C (358.33 K)

Mean pressure: 7.50 bar (108.78 psi)
Mean temperature: 85.3 C (358.48 K)
```

Answers:

1. `git show <hash>`.
2. Sofie Claes, in the commit "Fix Kelvin offset" (5 March 2025). She changed `273.0` to `273.15`. `git log -S 273.15` and `git blame conversions.py` both show this. Jan Peeters made the last change to `BAR_TO_PSI`; Anna Verhoeven wrote the first version of the file.
3. It checks out an old commit without being on a branch (detached HEAD), so you can look around. Return with `git switch main`.
4. `git restore <file>` discards uncommitted edits in the working tree. `git restore --staged <file>` only takes the file out of the staging area and keeps your edit.
5. The edit was never committed, so Git has no copy of it.

Stretch answers: `git log --oneline -- analyse_run.py` gives "Add measurements and analyse_run script". `git log --stat` shows that the first commit changed the most files (3: `conversions.py`, `README.md` and `.gitignore`). `--reverse` prints the oldest commit first.

## Exercise 3: Branches and merging

```powershell
uv run python exercises/git/setup_exercise.py 3
cd "<path printed by the script>"
git status
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

# merge commit
git switch -c feature/max-temperature
# edit analyse_run.py: add the max temperature print line
uv run python analyse_run.py
git add analyse_run.py
git commit -m "Print max temperature"
git switch main
Add-Content README.md "Run it with: uv run python analyse_run.py"
git add README.md
git commit -m "Explain how to run analyse_run.py"
git merge feature/max-temperature --no-edit
git log --oneline --graph --all --decorate
git branch -d feature/max-temperature
git status
```

Answers:

1. `git switch main` goes to an existing branch. `git switch -c feature/x` creates the new branch at the current commit and goes to it.
2. In the first case `main` had no new commits, so Git only moved the `main` label. In the second case `main` and the feature branch each had a new commit, so Git needed a new commit with two parents to join them.
3. Git replaces the files in your folder with the version of the branch you switch to. Your uncommitted edits stay, as long as they do not clash with the files that change.
4. A branch is only a label. The commits are in `main` too, so nothing is lost. `git branch -d` also refuses if the branch is not merged.
5. `main` is the version others use and build on. If it only gets finished work, it always works.

### Stretch: the merge conflict

```powershell
git merge experiment/psi-precision
git status
# open conversions.py in VS Code, click "Accept Incoming Change" (or choose your own line)
# check that no <<<<<<<, ======= or >>>>>>> remains, save
git add conversions.py
git commit -m "Merge experiment/psi-precision"
git log --oneline --graph --all --decorate
```

There is no single correct result. Either value is acceptable, as long as the markers are gone, the file still runs (`uv run python analyse_run.py`) and the merge is committed. The line that survives is `BAR_TO_PSI = 14.504  # ...` (current) or `BAR_TO_PSI = 14.5038  # ...` (incoming). If someone is lost: `git merge --abort` returns to the state before the merge.

## Exercise 4: Clone from Azure DevOps and push a branch

```powershell
New-Item -ItemType Directory -Force "$HOME\git-exercises"
cd "$HOME\git-exercises"
git clone https://dev.azure.com/<organisation>/<project>/_git/<training-repo>
cd <training-repo>
git status
git log --oneline
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

Answers:

1. `git branch` lists only local branches. `git branch -a` also lists the remote-tracking branches (`remotes/origin/...`), which are your laptop's record of what the remote has.
2. `origin` is the default name Git gives to the remote you cloned from, here the Azure DevOps repository.
3. The branch exists only locally, so the remote needs to create it. `-u` also sets the upstream, so later `git push` and `git pull` need no arguments.
4. So that people do not change the same files and cause conflicts.
5. After the push the commit exists on your laptop and on Azure DevOps (in your branch). It does not exist in `main` yet.

Stretch: `git fetch` followed by `git branch -a` lists the branches other participants pushed. In the graph, `origin/main` is where the remote `main` was at the last fetch, and your branch is one commit ahead of it.

## Exercise 5: Pull request, review and merge

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

Answers:

1. A request to merge a branch into another one, with a place for description, review and discussion. `main` requires one so that every change gets looked at by a second person and `main` stays working.
2. The reviewer saw the changes of the PR in one view (Files tab) with fresh eyes. They could spot unclear text, mistakes or files that should not be there.
3. `git pull` is `git fetch` (download new commits) plus a merge of them into your current branch. `git fetch` only downloads and does not touch your files or branch.
4. Their PRs were merged into `main` on the server, and you pulled `main`.
5. It removes your local record of remote branches that were deleted on the server (here `origin/feature/anna-intro`).
6. When someone else merged a change into `main` that touches the same lines as your branch.

Branching models: trunk-based development uses short-lived branches into one `main` branch. GitFlow uses long-lived `develop`, `release/*` and `hotfix/*` branches next to `main`. The exercise followed the trunk-based style.

## Exercise 6: Git in VS Code

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

Answers:

1. The **+** (Stage Changes) button.
2. `U` is untracked (new file, not yet in Git). `M` is modified (a tracked file with changes).
3. `git push -u origin <branch>`: it creates the branch on the remote and links the local branch to it.
4. So that everyone who clones the repository gets the same ignore rules.
5. No. A file that is already tracked stays tracked and stays in the history. You would need `git rm --cached <file>` to stop tracking it (not covered in this training).
