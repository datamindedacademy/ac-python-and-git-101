# Hints: Exercise 4: Clone from the remote and push a branch

Try the task first. Read a hint only when you are stuck.

## Hint for task 1

```powershell
git remote -v
git branch -a
git log -1
```

## Hint for task 2

```powershell
git switch -c feature/anna-intro
New-Item -ItemType Directory -Force participants/anna
Set-Content participants/anna/about.md "# Anna`n`nI work at Atlas Copco. I use Python to analyse compressor test data."
git add participants/anna/about.md
git commit -m "Add intro for Anna"
git push -u origin feature/anna-intro
```

`-u` (short for `--set-upstream`) links your local branch to `origin/feature/anna-intro`. In PowerShell, the backtick followed by `n` is a new line. You can also create the file in VS Code.
