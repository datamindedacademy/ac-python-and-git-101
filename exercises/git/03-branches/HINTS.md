# Hints: Exercise 3: Branches and merging

Try the task first. Read a hint only when you are stuck.

## Hint for task 1

```powershell
git switch -c feature/pressure-kpa
git add conversions.py
git commit -m "Add bar to kPa conversion"
git switch main
git merge feature/pressure-kpa
git branch -d feature/pressure-kpa
```

## Hint for task 2

The merge stops halfway and `git status` shows `conversions.py` as "both modified". In VS Code, the buttons above the markers (**Accept Current Change**, **Accept Incoming Change**) resolve it. Save the file, then:

```powershell
git switch main
git merge experiment/psi-precision
git add conversions.py
git commit -m "Merge experiment/psi-precision"
```

To go back to before the merge: `git merge --abort`.
