# Git exercises

Day 1, part 3: version control with Git and a remote forge.

By the end you can: clone a remote repository, commit on a branch, push, open a pull request, and pull.

## Overview

| # | Folder | Topic | Why it matters |
|---|---|---|---|
| 1 | `01-first-commit` | `git init`, `status`, `add`, `commit`, `log`, `diff`, `diff --staged`. The three areas. Commits that say one thing. | A commit is the unit you undo and review. |
| 2 | `02-history` | Extra exercise (ahead, or after class): `log`, `show`, find who changed a value and when, `restore`. | Find out what changed, who did it and why. |
| 3 | `03-branches` | `switch -c`, `merge` (fast-forward, merge conflict), `rebase`, `branch -d`. | Try things safely, and solve conflicts calmly. |
| 4 | `04-remote` | `clone`, `remote`, `push -u` to the remote. | Your work is backed up and colleagues can get it. |
| 5 | `05-pull-request` | Pull request, review, merge, `pull`, clean up. | A second pair of eyes before it reaches `main`. |
| 6 | `06-git-in-vscode` | Trainer demo in class. Do it yourself afterwards. | Daily Git work, and keeping data out of history. |

Do the exercises in order. Exercise 2 is extra: do it when you are ahead, or after class. Exercise 6 is a trainer demo to repeat afterwards.

## How an exercise works

- **Words to use**: the terms of that exercise.
- **Tasks**: two or three per exercise. Each states a result to reach, not the commands. The last one is much harder. Most people will not finish it in class.
- **No hints**: find the commands in the slides, in the cheat sheet below, or with `git help <command>`.
- Answers are in `solutions/git/README.md`.
- **Open question**: goes beyond today. Most people cannot answer it yet. Try it, or bring it to the trainer.

## Using Copilot

You may use GitHub Copilot all day. No task needs it.

- Type the Git commands yourself today. You need the words to ask for the right thing later.
- Read `git diff` before every commit, whoever wrote the change.
- You are the author of what you commit and push.

## Setup scripts for exercises 1 to 3

Exercises 1 to 3 start from a prepared folder. Create it with the setup script. Run this from the root of the course repository (`ac-python-and-git-101`), in PowerShell:

```powershell
uv run python exercises/git/setup_exercise.py 1
```

Use `2` or `3` for the other exercises. The script creates `git-exercises\exercise_<n>` in your home folder, outside the course repository, and prints the `cd` command you need next. Add `--force` to start again, or `--target <folder>` to put it somewhere else.

Exercises 4 to 6 use the training repository on the forge and need no setup script. The trainer gives you its URL:

```
https://<forge>/<organisation>/<training-repo>.git
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
Forge: new pull request                 5. PR, review, approve, merge
git switch main ; git pull                6. update your laptop
git branch -d feature/<name>-<topic>      7. clean up
git fetch --prune
```
