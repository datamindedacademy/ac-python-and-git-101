# Hints: Exercise 2: Explore the history

Try the task first. Read a hint only when you are stuck.

## Hint for task 1

```powershell
git log --oneline
git show --stat <hash>
```

`git show <hash>` without `--stat` also prints every changed line. Lines that start with `-` were removed and lines that start with `+` were added. If the screen shows `:` or `(END)`, press `q`.

## Hint for task 2

`git log -S<text>` lists the commits that added or removed that text. `git blame conversions.py` shows the commit and author of each line. To throw away the edit:

```powershell
git diff
git restore conversions.py
git status
```

`git restore` on a file permanently throws away uncommitted changes. Git cannot get them back, because they were never committed.
