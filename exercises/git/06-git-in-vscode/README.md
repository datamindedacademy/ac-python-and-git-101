# Exercise 6: Git in VS Code

**Demo in class, do it yourself afterwards.**

The trainer shows this exercise on the screen in class. It is not part of the hands-on block. Do it yourself after the training, or whenever you have time. You can do all of it alone.

Words to use: Source Control view, stage, commit, publish branch, sync, `.gitignore`, tracked file, ignored file.

## Goal

Repeat the whole daily cycle with the **Source Control** view in VS Code instead of the command line: branch, edit, stage, commit, push, pull request, pull. Then learn how to keep files out of Git with `.gitignore`.

## Why this matters

Most daily Git work happens in the editor. `.gitignore` keeps measurement data, output files and secrets out of a history that cannot easily forget them. A file that was committed once stays in the history, even after you delete it.

## Background

VS Code has Git built in. The buttons run the same Git commands you typed in exercises 1 to 5. Nothing is different underneath, so you can mix both: do one step in the terminal and the next in VS Code.

Other graphical Git programs exist, for example **SourceTree**, GitKraken or the Git view in PyCharm. They look different but offer the same actions.

## Tasks

Replace `anna` with your own name.

### 1. Open your clone in VS Code

Make sure you start from an up-to-date `main` (end of exercise 5, or just after cloning). Then open the clone from PowerShell:

```powershell
cd "$HOME\git-exercises\<training-repo>"
git switch main
git pull
code .
```

If `code` is not recognised, use **File > Open Folder** in VS Code and choose the folder.

Open the Source Control view: click the branch icon in the left bar, or press `Ctrl+Shift+G`. It is empty because nothing has changed.

### 2. Create a branch

Look at the bottom-left corner of VS Code. It shows `main`. Click it. In the menu at the top, choose **Create new branch...** and type `feature/anna-vscode`. Press Enter.

The bottom-left corner now shows `feature/anna-vscode`.

### 3. Edit files

Create a new file in your folder: in the Explorer, right-click the folder `participants/anna`, choose **New File**, and name it `bench_notes.md`. Write two lines about a test-bench measurement. Save with `Ctrl+S`.

In the Source Control view, you see:

- the file under **Changes**, with a `U` next to it (untracked, new).

Open `participants/anna/about.md`, change a word and save. It appears under Changes with an `M` (modified). Click a file to see the difference side by side. This is `git diff` with colours.

### 4. Stage and commit

Hover over `bench_notes.md` and click the **+** (Stage Changes). The file moves to **Staged Changes**. This is `git add`.

Type a message in the box at the top, for example `Add bench notes for Anna`. Click **Commit**.

If you commit without staging anything, VS Code asks if you want to stage all changes and commit directly. That is fine for small changes. Click **Yes**.

The `about.md` change is still not committed. Stage it with **+** and commit it with the message `Update intro`. Two small commits are better than one mixed commit.

Check in the terminal (menu **Terminal > New Terminal**):

```powershell
git log --oneline
```

You see both commits.

### 5. Push

The Source Control view shows a **Publish Branch** button. Click it. It does `git push -u origin feature/anna-vscode`. If VS Code asks whether to run `git fetch` periodically, answer as you like.

Open GitHub. The branch is there.

### 6. Pull request (optional, needs a second person)

On GitHub, open a PR as in exercise 5. The branch protection rule needs an approval, and you cannot approve your own PR. If you work alone, skip tasks 6 and 7. Just leave the pushed branch as it is, and go on with task 8. If a colleague or the trainer is around, ask them to approve, then merge the PR.

### 7. Pull the result (only after the PR is merged)

In VS Code, click the branch name in the bottom-left and choose `main`. Then open the **...** menu in the Source Control view and choose **Pull**. Or click the **Sync Changes** button in the status bar.

To delete the finished branch: press `Ctrl+Shift+P`, type `Git: Delete Branch...`, and choose `feature/anna-vscode`. To remove the deleted remote branch from your list, run `git fetch --prune` in the terminal.

If you skipped the PR, just switch back to `main` in the bottom-left corner.

### 8. Keep files out of Git with `.gitignore`

Not every file belongs in Git. Examples: virtual environments (`.venv/`), Python caches (`__pycache__/`), and large output files that your script can recreate. A file called `.gitignore` lists patterns that Git should ignore.

Make sure you are on `main` (bottom-left corner). Start a new branch from `main`: `feature/anna-ignore` (bottom-left corner, as before).

Open the terminal in VS Code and create some output files in your folder:

```powershell
New-Item -ItemType Directory -Force participants/anna/output
Set-Content participants/anna/output/summary.csv "run,mean_bar"
Set-Content participants/anna/output/plot.png "not a real picture"
```

Look at the Source Control view. The `output` folder shows up as a new file. You do not want to commit generated files.

The repository already has a `.gitignore` in its root that covers `.venv/` and `__pycache__/`. Open it and read it. For your own output folder, create a `.gitignore` in your own folder:

```powershell
Set-Content participants/anna/.gitignore "output/`n*.png`n.venv/`n__pycache__/"
cat participants/anna/.gitignore
```

Expected:

```
output/
*.png
.venv/
__pycache__/
```

Look at the Source Control view again. The `output` folder is gone from the list. Only `.gitignore` is new. Git ignores files that match the patterns.

Commit the `.gitignore` itself, so everyone who clones gets the same rules:

```powershell
git add participants/anna/.gitignore
git commit -m "Add .gitignore for Anna's folder"
git status
```

`git status` says working tree clean, even though `output/` exists on disk.

A `.gitignore` only affects files that Git does not follow yet. If you already committed a file, ignoring it later does not remove it from the history.

Push the branch and open a PR if you want, or leave it local.

## Command line, VS Code and SourceTree

| Action | Command line | VS Code | SourceTree |
|---|---|---|---|
| See what changed | `git status`, `git diff` | Source Control view, click a file | File status pane, diff pane |
| Stage | `git add <file>` | **+** next to the file | Tick the file (Stage) |
| Commit | `git commit -m "..."` | Message box and **Commit** | Message box and **Commit** |
| New branch | `git switch -c <name>` | Branch name bottom-left, **Create new branch...** | **Branch** button |
| Switch branch | `git switch <name>` | Click branch name bottom-left | Double-click the branch |
| Push | `git push` | **Publish Branch** or **Sync Changes** | **Push** button |
| Pull | `git pull` | **...** > **Pull**, or **Sync Changes** | **Pull** button |
| History graph | `git log --oneline --graph --all` | Extension such as Git Graph, or the Timeline view | Built-in graph (very good) |
| Resolve a conflict | Edit file, `git add`, `git commit` | Merge editor with buttons | External merge tool |
| Strength | Exact, same everywhere, scriptable | Close to your code, no extra program | Good overview of branches |

Rule of thumb: use what is fast for you. Know the command line for when something goes wrong, and to read documentation, which is always written in commands.

## Check yourself

Short questions to test yourself after class. The answers are in `solutions/git/README.md`.

1. Which button in VS Code does the same as `git add`?
2. What do `U` and `M` next to a file name mean?
3. What does **Publish Branch** do on the command line?
4. If you ignore a file that is already committed, is it removed from Git?

## Optional: if you have time

### With Copilot

VS Code can let Copilot write the commit message. Change a line in your `about.md` and stage it. In the Source Control view, click the sparkle icon in the commit message box (**Generate Commit Message**). Read the result before you click **Commit**. Does it say what changed? Does it say why? Copilot only sees the diff, so add the reason yourself when it matters.

### More

- Install the **Git Graph** extension and look at the history of the training repository.
- Open the **Timeline** view at the bottom of the Explorer for `about.md`. It shows the commits that changed it.

## Open question

You commit a 200 MB data file by mistake and delete it again in the next commit. How big is the repository now? Why does adding the file to `.gitignore` afterwards not help, and what would you have to do instead?
