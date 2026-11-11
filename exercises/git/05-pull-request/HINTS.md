# Hints: Exercise 5: Pull request, review and merge

Try the task first. Read a hint only when you are stuck.

## Hint for task 1

**Repos > Pull requests > New pull request**. Check the branches at the top, fill in title and description, add the reviewer, click **Create**. Your neighbour's PR is under "Assigned to me" or "Active". The **Approve** button is at the top right, and plain **Approve** is the one to use here.

## Hint for task 2

```powershell
git switch main
git pull
git log --oneline --graph -10
git branch -d feature/anna-intro
git fetch --prune
git branch -a
```

`git pull` fetches new commits and merges them into your current branch. `--prune` removes your record of remote branches that no longer exist. If `git branch -d` says "not fully merged" and the PR was completed with **Squash**, see the open question.
