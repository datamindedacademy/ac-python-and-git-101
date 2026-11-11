# Exercise 5: Pull request, review and merge

Words to use: pull request, reviewer, approve, complete, branch policy, merge commit, squash merge, pull.

## Goal

Get your branch into `main` the way teams do it: with a pull request that a colleague reviews. Then bring your laptop up to date and clean up.

## Why this matters

A pull request puts a second pair of eyes on a change before it reaches the version everyone uses, and it keeps the record of why. That matters more when part of the code was written by an assistant. You are still the one who answers for it.

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

Stuck on a task? The hints are in `HINTS.md` in this folder.

### Task 1: Open a pull request and review one

In Azure DevOps, open a pull request from `feature/<your-name>-intro` into `main`, with a title, a short description of what and why, and your neighbour as reviewer. Look at the **Files** and **Commits** tabs and at the policies on the right.

Then review your neighbour's pull request: read the **Files** tab, leave at least one comment on a line (hover over the line number and click the comment icon), and click **Approve**. A good review answers three things. Is the change what the description says? Does it do anything it should not? Is it clear?

Result: your PR is open with a reviewer, and your neighbour's PR has your approval and at least one line comment.

### Task 2: Complete and clean up

When your PR has its approval and the policy shows a green check, complete it. Keep the default merge type **Merge (no fast-forward)** and tick **Delete feature/<your-name>-intro after merging**. If your neighbour left a comment that needs an answer, reply and click **Resolve** first.

Then update your laptop: your local `main` gets the new commits, including your neighbours' folders, and your local copy of the branch is deleted. Your laptop also forgets the remote branch that Azure DevOps deleted.

End state:

```
*   267628c Merged PR 1: Add intro for Anna
|\
| * abca709 Add intro for Anna
|/
* 0575ff7 Initial commit
```

The hashes and the number of commits will differ. `git branch -a` shows only:

```
* main
  remotes/origin/HEAD -> origin/main
  remotes/origin/main
```

### Task 3: A pull request that conflicts with main

This one is much harder. There is no hint.

`main` moves all the time, because everyone completes PRs into it. Reproduce the bad case. Two participants (or one participant with two branches) each change the same line of `README.md` in the training repository, each on their own branch, and each open a PR. Complete the first PR. The second PR now shows **Conflicts**.

1. Make the second PR mergeable again, from the command line, by bringing `main` into your branch with a merge. Resolve the conflict in the file and push.
2. Say what you would have done differently with a rebase of your branch on `origin/main`. Name the extra push option it needs and why.
3. The team has to pick one for its branch policy. Say which and give one reason.

Rules:

- Do not edit the file in the Azure DevOps web page.
- Do not use `git push --force` for the merge route.
- Do not leave a real change in the shared `README.md`. The trainer may reset it.

The second PR updates itself when you push, and **Complete** works again. A resolved conflict leaves one merge commit on your branch, with `main` as second parent.

## Open question

With a squash merge your change lands on `main` as one new commit. Afterwards `git branch -d` refuses to delete your branch, although everything in it is on `main`. Why does Git think the branch is not merged?
