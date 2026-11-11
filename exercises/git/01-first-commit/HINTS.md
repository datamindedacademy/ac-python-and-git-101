# Hints: Exercise 1: Your first commit

Try the task first. Read a hint only when you are stuck.

## Hint for task 1

```powershell
git config --global user.name "Your Name"
git config --global user.email "your.name@example.com"
git init -b main
git status
git add conversions.py
git commit -m "Add bar to psi conversion"
git add measurements.csv
git commit -m "Add first measurements"
git log --oneline
```

If `git log` fills the screen and shows `:` or `(END)`, press `q`.

## Hint for task 2

```powershell
git status
git diff
git add conversions.py
git diff --staged
git commit -m "Add Celsius to Kelvin conversion"
git add measurements.csv
git diff --staged
git commit -m "Add fourth measurement run"
```

`git diff` shows what is not staged yet. `git diff --staged` shows what is waiting in the staging area.
