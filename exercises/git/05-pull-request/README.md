# Exercise 5: Pull request, review and merge

Words to use: pull request, reviewer, approve, merge, branch protection rule, merge commit, squash merge, pull.

## Goal

Get your branch into `main` the way teams do it: with a pull request that a colleague reviews. Then bring your laptop up to date and clean up.

## Why this matters

A pull request puts a second pair of eyes on a change before it reaches the version everyone uses, and it keeps the record of why. That matters more when part of the code was written by an assistant. You are still the one who answers for it.

## Background

Nobody pushes directly to `main` in a team project. In this training, `main` is **protected**: the forge refuses direct pushes (a branch protection rule on `main`). Changes get in through a **pull request** (PR).

A pull request says: "I have a branch. Please look at it, and merge it into `main`." It has:

- a title and a description that explain the change,
- a list of changed files, with the differences,
- a place for comments,
- a **reviewer** who can approve it.

This is how most teams check each other's work. It catches mistakes, spreads knowledge, and keeps `main` working. In this training, the rule requires a pull request with one approval before you can merge it.

## Before you start

You need your branch `feature/<your-name>-intro` from exercise 4, pushed to the remote. Sit next to a neighbour: you review each other's PR.

## Tasks

Stuck on a task? Look at the slides, the cheat sheet in `exercises/git/README.md`, or `git help <command>`.

### Task 1: Open a pull request and review one

On the forge, open a pull request from `feature/<your-name>-intro` into `main`, with a title, a short description of what and why, and your neighbour as reviewer. Look at the **Conversation**, **Commits** and **Files changed** tabs and at the checks at the bottom of the Conversation.

Then review your neighbour's pull request: read the **Files changed** tab, leave at least one comment on a line (hover over the line, click the blue **+**, then **Start a review**), and finish with **Review changes**, **Approve**, **Submit review**. A good review answers three things. Is the change what the description says? Does it do anything it should not? Is it clear?

Result: your PR is open with a reviewer, and your neighbour's PR has your approval and at least one line comment.

### Task 2: Merge and clean up

When your PR has its approval and the merge box is green, click **Merge pull request**. Keep the default **Create a merge commit**, confirm, then click **Delete branch**. If your neighbour left a comment that needs an answer, reply and click **Resolve conversation** first.

Then update your laptop: your local `main` gets the new commits, including your neighbours' folders, and your local copy of the branch is deleted. Your laptop also forgets the remote branch that was deleted.

End state:

```
*   267628c Merge pull request #1 from <organisation>/feature/anna-intro
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

This one is much harder.

`main` moves all the time, because everyone merges PRs into it. Reproduce the bad case. Two participants (or one participant with two branches) each change the same line of `README.md` in the training repository, each on their own branch, and each open a PR. Merge the first PR. The second PR now says **This branch has conflicts that must be resolved**.

1. Make the second PR mergeable again, from the command line, by bringing `main` into your branch with a merge. Resolve the conflict in the file and push.
2. Say what you would have done differently with a rebase of your branch on `origin/main`. Name the extra push option it needs and why.
3. The team has to pick one for its branch protection rule. Say which and give one reason.

Rules:

- Do not edit the file in the web page of the forge.
- Do not use `git push --force` for the merge route.
- Do not leave a real change in the shared `README.md`. The trainer may reset it.

The second PR updates itself when you push, and **Merge pull request** works again. A resolved conflict leaves one merge commit on your branch, with `main` as second parent.

## Open question

With a squash merge your change lands on `main` as one new commit. Afterwards `git branch -d` refuses to delete your branch, although everything in it is on `main`. Why does Git think the branch is not merged?
