# Git exercises

Day 1, part 3: version control with Git and Azure DevOps.

By the end you can: clone an Azure DevOps repository, commit on a branch, push, open a pull request, and pull.

## Overview

| # | Folder | Topic | Why it matters |
|---|---|---|---|
| 1 | `01-first-commit` | `git init`, `status`, `add`, `commit`, `log`, `diff`. The three areas. | A commit is the unit you undo and review. |
| 2 | `02-history` | `log`, `show`, find who changed a value and when, `restore`. | Find out what changed, who did it and why. |
| 3 | `03-branches` | `switch -c`, `merge` (fast-forward, merge conflict), `branch -d`. | Try things safely, and solve conflicts calmly. |
| 4 | `04-azure-devops-remote` | `clone`, `remote`, `push -u` to Azure DevOps. | Your work is backed up and colleagues can get it. |
| 5 | `05-pull-request` | Pull request, review, complete, `pull`, clean up. | A second pair of eyes before it reaches `main`. |
| 6 | `06-git-in-vscode` | Trainer demo in class. Do it yourself afterwards. | Daily Git work, and keeping data out of history. |

Every README starts with the core tasks and a "Words to use" list: the terms that exercise introduces. Each README has a **Why this matters** section and ends with an **Open question** that goes beyond the day. Each optional part has one **With Copilot** task. Everything under the heading **Optional: if you have time** at the end of a README is not needed to follow the training. Do it when you finish early or at home.

Exercises 1, 2, 3 and 5 end with a **Challenge** after the optional part. It is for those who finish early. It describes a result to reach and gives no commands: find them with `git help <command>` or Copilot, and check the result with `git log` and `git status`. The answers are in `solutions/git/README.md`. Exercises 4 and 6 have no challenge.

What moved to optional:

- Exercise 1: committing the data file (task 9) and the extras.
- Exercise 2: comparing two commits, `git log -S`, `git blame`, visiting an old version (detached HEAD), `git restore --staged`.
- Exercise 3: a merge commit without a conflict, rebase instead of merge.
- Exercise 4: running `check_setup.py` and the extras.
- Exercise 5: details on "main moved meanwhile", the GitFlow versus trunk-based table and the extras.

Do the exercises in order. Open each `README.md` in VS Code (right-click, **Open Preview**) or read it on screen.

## Using Copilot

You may use GitHub Copilot (inline completions and Copilot Chat in VS Code) during the whole training. No core task needs it. For the Git exercises, these ground rules get the most out of it:

- Use it freely. Ask it to explain a Git message or a command you do not understand.
- Type the Git commands yourself today. The commands are the vocabulary. You need the words to ask for the right thing later, and to judge what comes back.
- Read `git diff` before every commit, whoever wrote the change. Git shows you exactly what changed, so you can keep what is good and undo the rest.
- Keep commits small and pull requests reviewed. That matters more when an assistant writes code, not less.
- You are the author of what you commit and push. Your name is on it.

## Setup scripts for exercises 1 to 3

Exercises 1 to 3 start from a prepared folder. Create it with the setup script. Run this from the root of the course repository (`ac-python-and-git-101`), in PowerShell:

```powershell
uv run python exercises/git/setup_exercise.py 1
```

Use `2` or `3` for the other exercises. The script:

- creates the folder `git-exercises\exercise_<n>` in your home folder, **outside** the course repository (never put one Git repository inside another),
- prints the `cd` command you need next,
- refuses to overwrite an existing folder. Add `--force` to delete it and start again,
- accepts `--target <folder>` if you want it somewhere else.

```powershell
uv run python exercises/git/setup_exercise.py 2 --force
uv run python exercises/git/setup_exercise.py 3 --target D:\temp\ex3
```

Exercises 4 to 6 use the training repository on Azure DevOps and need no setup script. The trainer gives you its URL:

```
https://dev.azure.com/<organisation>/<project>/_git/<training-repo>
```

## If you get stuck

- Stuck in a screen with `:` or `(END)` at the bottom? You are in a pager. Press `q`.
- Stuck in a text editor after a commit or merge? Close the tab in VS Code. In vim, press `Esc`, type `:q!` and press Enter. Next time use `git commit -m "message"`.
- Not sure where you are? Run `pwd`, then `git status`.
- Raise your hand. Nothing in these exercises can destroy your work, except `git restore <file>` on uncommitted edits, and that one is marked in the text.

## Cheat sheet

All commands work in Windows PowerShell. Use `<...>` for a value you fill in.

### Set up (once per laptop)

```powershell
git config --global user.name "Your Name"
git config --global user.email "your.name@example.com"
git config user.name                  # check
```

### Start

```powershell
git init -b main                      # make a new repository in this folder
git clone <url>                       # copy a remote repository to your laptop
```

### The daily cycle

```powershell
git status                            # what is changed, staged, untracked?
git diff                              # unstaged changes
git diff --staged                     # staged changes
git add <file>                        # stage a file
git commit -m "Add ..."               # save a snapshot (always use -m)
git push                              # send commits to the remote
git pull                              # get commits from the remote
```

### Branches

```powershell
git branch                            # list local branches
git branch -a                         # also list remote branches
git switch <branch>                   # go to a branch
git switch -c <new-branch>            # create a branch and go to it
git merge <branch>                    # merge <branch> into the current branch
git rebase main                       # replay this branch on top of main (unpushed commits only)
git branch -d <branch>                # delete a merged branch
git push -u origin <branch>           # first push of a new branch
git fetch --prune                     # update remote info, forget deleted remote branches
```

### History

```powershell
git log --oneline                     # one line per commit (q to quit)
git log --oneline --graph --all --decorate   # picture of all branches
git show <hash>                       # one commit in detail
git diff <hash1> <hash2>              # compare two commits
git log -S <text>                     # commits that added or removed <text>
git blame <file>                      # who last changed each line
git switch --detach <hash>            # look at an old version
git switch main                       # come back
```

### Undo

```powershell
git restore <file>                    # throw away uncommitted edits (cannot be undone)
git restore --staged <file>           # unstage, keep the edit
git merge --abort                     # leave a merge that went wrong
git rebase --abort                    # leave a rebase that went wrong
```

### The three areas

```
working tree  --git add-->  staging area  --git commit-->  repository  --git push-->  remote
                                                           repository  <--git pull--  remote
```

### The pull request flow

```
git switch -c feature/<name>-<topic>      1. branch
(edit files)                              2. work
git add <file> ; git commit -m "..."      3. commit (in PowerShell 5.1 use ; instead of &&)
git push -u origin feature/<name>-<topic> 4. push
Azure DevOps: New pull request            5. PR, review, approve, complete
git switch main ; git pull                6. update your laptop
git branch -d feature/<name>-<topic>      7. clean up
git fetch --prune
```

In PowerShell 5.1, `&&` does not work. Run commands on separate lines, or join them with `;`.
