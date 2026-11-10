# Exercise 5: Pull request, review and merge

Time: about 25 minutes.

## Goal

Get your branch into `main` the way teams do it: with a pull request that a colleague reviews. Then bring your laptop up to date and clean up.

## Background

Nobody pushes directly to `main` in a team project. In this training, `main` is **protected**: Azure DevOps refuses direct pushes. Changes get in through a **pull request** (PR).

A pull request says: "I have a branch. Please look at it, and merge it into `main`." It has:

- a title and a description that explain the change,
- a list of changed files, with the differences,
- a place for comments,
- a **reviewer** who can approve it.

This is how most teams check each other's work. It catches mistakes, spreads knowledge, and keeps `main` working. In this training, the branch policy requires at least one approval before you can complete a PR.

## Before you start

You need your branch `feature/<your-name>-intro` from exercise 4, pushed to Azure DevOps. Sit next to a neighbour: you review each other's PR.

## Tasks

### 1. Create the pull request

In Azure DevOps, open your repository and go to **Repos > Pull requests**. Click **New pull request**.

1. Check the branches at the top: from `feature/<your-name>-intro` into `main`.
2. Write a **title**, for example `Add intro for Anna`.
3. Write a **description**: one or two sentences about what and why. For example: "Adds my personal folder with a short intro. First pull request of the training."
4. Under **Reviewers**, add your neighbour (search by name).
5. Click **Create**.

Look around the PR page. The **Files** tab shows the changes. The **Commits** tab lists your commits. The right side shows the required policies, such as "At least 1 reviewer must approve".

### 2. Review your neighbour's pull request

Ask your neighbour for the PR name. Open it from **Repos > Pull requests**, under "Assigned to me" or "Active".

1. Open the **Files** tab and read the change.
2. Add a comment on a line: hover over a line number and click the comment icon. Write something friendly, for example "Nice intro".
3. Click **Approve** at the top right. The menu next to it has "Approve with suggestions" and "Wait for author". Use plain **Approve** here.

A good review answers: Is the change what the description says? Does it do anything it should not? Is it clear?

### 3. Complete the pull request

Back in your own PR, you should see the approval and a comment. If your neighbour left a comment that needs an answer, reply and click **Resolve**.

When the policy shows a green check, click **Complete**. A dialog opens:

- **Merge type**: keep the default, **Merge (no fast-forward)**. This creates a merge commit.
- Tick **Delete feature/<your-name>-intro after merging**.
- Leave "Complete associated work items" alone.

Click **Complete merge**. The PR status changes to **Completed**.

### 4. Update your laptop

The merge happened on the server. Your laptop does not know yet. Switch to `main` and pull:

```powershell
git switch main
git pull
```

`git pull` downloads new commits from the remote and merges them into your current branch. Expected:

```
Updating <hash>..<hash>
Fast-forward
 participants/anna/about.md | 3 +++
 ...
```

You now also get the files of your neighbours that were merged. Look:

```powershell
ls participants
git log --oneline --graph -10
```

You see your commit and the merge commit that Azure DevOps made.

### 5. Clean up

Your branch is done. Delete the local copy:

```powershell
git branch -d feature/anna-intro
git fetch --prune
git branch -a
```

- `git branch -d` deletes the local branch. It only works if the branch was merged.
- `git fetch` downloads information about the remote without changing your files.
- `--prune` removes your local record of remote branches that no longer exist. Azure DevOps deleted `origin/feature/anna-intro` when you completed the PR.

`git branch -a` should now show only `main` and `remotes/origin/main`.

If `git branch -d` says "not fully merged" and your PR was completed with **Squash**, use `git branch -D feature/anna-intro` after you checked that the PR is completed.

### 6. What if `main` moved while my PR was open?

This happens all the time, because everyone merges PRs into the same `main`.

- If the other changes touch **different files or lines**, Azure DevOps merges your PR without a problem. You do nothing.
- If both changes touch **the same lines**, the PR shows **Conflicts**, and Complete is disabled. You fix it on your laptop:

```powershell
git switch feature/anna-intro
git pull origin main
```

`git pull origin main` brings the new `main` into your branch. If Git reports a conflict, open the file in VS Code, choose the right version (see the stretch of exercise 3), then:

```powershell
git add <file>
git commit -m "Merge main into feature/anna-intro"
git push
```

The PR updates itself. Pushing more commits to a branch with an open PR adds them to the PR.

Because everyone has their own folder in this training, you probably will not see conflicts. In a real project you will meet them. Do not panic: read the markers, choose, commit.

## Background: branching models

The way you worked in this exercise is close to **trunk-based development**: short-lived branches, small changes, PR into `main`, and `main` is always in a working state.

| | Trunk-based development | GitFlow |
|---|---|---|
| Main idea | One main branch. Short branches (hours to days). | Several long-lived branches: `main`, `develop`, plus `feature/*`, `release/*`, `hotfix/*`. |
| Merging | Small PRs into `main`, often. | Features go into `develop`. Releases go from `develop` to `main`. |
| Good for | Teams that release often. Scripts, data analysis, internal tools. | Software with planned versions and several supported releases. |
| Cost | Needs discipline and a quick review. | More branches, more merging, more overhead. |

For analysis scripts and small tools, start simple: trunk-based with PRs. You can add structure later if you need it.

## Check yourself

1. What is a pull request, and why does `main` require one?
2. What did the reviewer see that you could not easily see yourself?
3. What does `git pull` do? How is `git fetch` different?
4. Why do you see your neighbours' folders after the pull?
5. Why did we run `git fetch --prune` after the merge?
6. In which situation does a PR show conflicts?

## Stretch

- Create a second small change (for example edit your `about.md`) on a new branch, push it, and open a second PR. Add a second commit to the branch while the PR is open and see it appear in the PR.
- Open a PR **Overview** and read the "Policies" section. Which rules protect `main`?
