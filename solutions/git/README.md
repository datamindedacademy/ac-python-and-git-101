# Git exercises: solutions

Expected command sequences and answers to the "check yourself" questions. Each exercise has the core part first (the timed tasks) and then the optional part. Hashes are written as `<hash>`. Yours will differ unless noted.

Commands are for Windows PowerShell 5.1. Replace `anna` with your own name.

## Exercise 1: Your first commit

### Core (10 min)

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
git log --oneline
```

Final `git log --oneline`:

```
<hash> Add Celsius to Kelvin conversion
<hash> Add bar to psi conversion
```

Explain it (model answers):

1. The working tree is the folder with the files you edit. The staging area is the list of changes you selected for the next commit. The repository is the saved history of commits in `.git`. After `git add` the change is in the staging area; after `git commit` it is in the repository.
2. You decide what belongs together. You can put one logical change in a commit and leave unfinished or unrelated edits out, which keeps each commit small, easy to describe and easy to review or undo. The cost is one extra step (`git add`) and the risk of forgetting to stage a file.

Check yourself:

1. `git diff` compares the working tree with the staging area. After `git add` they are the same, so nothing shows. `git diff --staged` shows the staged change (staging area against the last commit).
2. "Untracked" means Git sees the file in the folder, but it is not in any commit and not staged.
3. Without `-m`, Git opens a text editor to ask for the message. `-m` gives the message on the command line.

### Optional

```powershell
git add measurements.csv
git commit -m "Add first measurements"
git status
```

Final `git log --oneline` has a third commit, "Add first measurements", and `git status` says "nothing to commit, working tree clean".

More: `git log --stat` adds the list of changed files and the number of added and removed lines per commit. The `.git` folder is hidden. `ls -Force` shows it.

## Exercise 2: Explore the history

### Core (10 min)

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

Explain it (model answers):

1. The diff of a commit shows what changed, the author and date show who and when, and the commit message is the only place that says why. Git records the first three for you; the message is yours to write. A message like "Fix Kelvin offset" lets a colleague find the commit in seconds, while "update" does not.
2. Git can only bring back what was committed. Uncommitted edits exist in one place, your working tree, and `git restore` or a mistake can remove them for good. So commit small and often: every commit is a point you can return to.

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

## Exercise 3: Branches and merging

### Core (15 min)

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

Explain it (model answers):

1. The first time `main` had no new commits since the branch started, so Git only moved the `main` label forward to the branch's commit: a fast-forward. The second time both `main` and the branch had a new commit, so the history had split. Git joined the two lines with a new merge commit that has two parents.
2. On a branch you can commit unfinished work without breaking `main`, drop the work if the idea fails, and have it reviewed before it lands. `main` stays in a working state for everyone else. The cost is a merge at the end, and the longer a branch lives, the larger the chance of a merge conflict.

Check yourself:

1. `git switch main` goes to an existing branch. `git switch -c feature/x` creates the new branch at the current commit and goes to it.
2. Git replaces the files in your folder with the version of the branch you switch to. Your uncommitted edits stay, as long as they do not clash with the files that change.
3. A branch is only a label. The commits are in `main` too, so nothing is lost. `git branch -d` also refuses if the branch is not merged.

### Optional: the merge conflict

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

### Core (15 min)

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

Explain it (model answers):

1. `origin/main` is a remote-tracking branch: your laptop's memory of where `main` was on the server the last time you talked to it. Right now it shows the state at your clone. It does not update by itself; it changes only when you run `git fetch`, `git pull` or `git push`. Colleagues may have pushed since then without you seeing it.
2. The commit exists in your local repository and, after the push, on Azure DevOps in your branch `feature/<your-name>-intro`. It is not in `main` yet, neither on the server nor on your laptop, and not on your colleagues' laptops until they fetch.

Check yourself:

1. `git branch` lists only local branches. `git branch -a` also lists the remote-tracking branches (`remotes/origin/...`), which are your laptop's record of what the remote has.
2. `origin` is the default name Git gives to the remote you cloned from, here the Azure DevOps repository.
3. The branch exists only locally, so the remote needs to create it. `-u` also sets the upstream, so later `git push` and `git pull` need no arguments.
4. So that people do not change the same files and cause conflicts.

Stretch: `git fetch` followed by `git branch -a` lists the branches other participants pushed. In the graph, `origin/main` is where the remote `main` was at the last fetch, and your branch is one commit ahead of it.

## Exercise 5: Pull request, review and merge

### Core (20 min)

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

Explain it (model answers):

1. A pull request puts a second pair of eyes on every change before it reaches `main`, and it records what was changed, why, and who approved it. That catches mistakes early and keeps `main` working for everyone. The cost is waiting time and effort from a colleague, which is why pull requests should be small.
2. You are. The author of a commit stays responsible for it; the reviewer shares responsibility for letting it in. It makes no difference whether you typed the code or Copilot generated it: you read the diff, you committed it, and your name is on it.

Check yourself:

1. The reviewer saw the changes of the PR in one view (Files tab) with fresh eyes. They could spot unclear text, mistakes or files that should not be there.
2. `git pull` is `git fetch` (download new commits) plus a merge of them into your current branch. `git fetch` only downloads and does not touch your files or branch.
3. Their PRs were merged into `main` on the server, and you pulled `main`.
4. It removes your local record of remote branches that were deleted on the server (here `origin/feature/anna-intro`).

A PR shows conflicts when someone else merged a change into `main` that touches the same lines as your branch.

Branching models: trunk-based development uses short-lived branches into one `main` branch. GitFlow uses long-lived `develop`, `release/*` and `hotfix/*` branches next to `main`. The exercise followed the trunk-based style.

## Exercise 6: Git in VS Code

Trainer demo in class. Participants repeat it alone afterwards (20 min). Everything here is optional for the timed block.

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

Explain it (model answers):

1. In the repository: what a person wrote and what others need to reproduce your work, such as scripts, small configuration files, documentation and the `.gitignore` itself. Not in the repository: what can be regenerated or is specific to your laptop (`.venv/`, `__pycache__/`, plots and output files), large raw data, and anything secret such as passwords. Generated files bloat the history and cause needless conflicts.
2. The Source Control view is fast for the daily cycle and shows diffs side by side, next to your code. The command line is exact, works the same on every machine and server, and is what documentation and error messages refer to, so it is the tool for anything unusual. Both run the same Git underneath, so you can mix them.

Check yourself:

1. The **+** (Stage Changes) button.
2. `U` is untracked (new file, not yet in Git). `M` is modified (a tracked file with changes).
3. `git push -u origin <branch>`: it creates the branch on the remote and links the local branch to it.
4. No. A file that is already tracked stays tracked and stays in the history. You would need `git rm --cached <file>` to stop tracking it (not covered in this training).

## The "With Copilot" tasks

These optional tasks have no single right answer. What matters is the judgement:

- Exercise 1: a good result is a diff with only the new `kelvin_to_celsius` function (`temperature_k - 273.15`). Anything else in the diff (renamed functions, reformatting, new comments) was not asked for and should be questioned.
- Exercise 2: the vague prompt usually gives a large diff (type hints, docstrings, validation, renames) that is hard to review. The precise prompt gives a few added lines. The difference is the precision of the request, in the vocabulary of the code.
- Exercise 3: Copilot can explain both sides, but which precision the test bench needs is a domain decision. A good check: read both lines, run `uv run python analyse_run.py` after resolving, and look at `git diff --staged`.
- Exercise 4: you can verify what `git fetch` did to `origin/main` and that your files did not change. You cannot verify claims about cases you did not try.
- Exercise 5: the draft usually describes what changed. It cannot know why, how you tested it, or what the reviewer should look at. Those are the parts to add.
- Exercise 6: generated commit messages describe the diff. Add the reason when it is not obvious.
