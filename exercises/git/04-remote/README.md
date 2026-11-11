# Exercise 4: Clone from the remote and push a branch

Words to use: remote, `origin`, clone, push, upstream branch, remote-tracking branch (`origin/main`), fetch, pull.

## Goal

Get a copy of your group's training repository from the remote. Make a branch with a file in your own folder, and push it.

## Why this matters

A script that exists only on your laptop is gone when the laptop is. The remote is the backup, and the only way a colleague gets your work without an email attachment. You use it every day you work in a shared repository.

## Background

So far your repository lived only on your laptop. Real projects have a shared copy on a server. This shared copy is called a **remote**. It lives on a **forge**: a website that hosts repositories and adds sign-in and pull requests. Your group has one repository there. The Git commands are the same on every forge.

Terms used in this exercise:

| Term | Meaning |
|---|---|
| **remote** | A copy of the repository on a server. Its default name is `origin`. |
| **clone** | Download a full copy of a remote repository, with its whole history. |
| **push** | Send your commits to the remote. |
| **pull** | Get new commits from the remote and bring them into your branch. |
| **upstream** | The remote branch that your local branch is linked to. |

Everyone in your group works in the same repository. To avoid getting in each other's way, each person only adds files in their own folder: `participants/<your-name>/`. Use your first name in lowercase, without spaces or special characters, for example `anna`.

You sign in to the forge through **Git Credential Manager**, which comes with Git for Windows. The first time you clone or push, a browser window opens and asks you to sign in. After that, it remembers you.

## Before you start

Your trainer gives you the repository URL. It looks like this:

```
https://<forge>/<organisation>/<training-repo>.git
```

The trainer gives you the real URL. You can also copy it from the repository page on the forge.

## Tasks

Stuck on a task? Look at the slides, the cheat sheet in `exercises/git/README.md`, or `git help <command>`.

### Task 1: Clone and look around

Clone the training repository into a folder next to your other exercises, not inside the course repository. A sign-in window opens in your browser the first time. Sign in to the forge.

```powershell
New-Item -ItemType Directory -Force "$HOME\git-exercises"
cd "$HOME\git-exercises"
git clone https://<forge>/<organisation>/<training-repo>.git
cd <training-repo>
```

```
Cloning into '<training-repo>'...
remote: Enumerating objects: 8, done.
Receiving objects: 100% (8/8), done.
```

The numbers will differ. Then answer three questions from inside the clone, using Git and not the web page: what is the remote called and where does it point, which branches exist on the remote, and who made the last commit.

`git branch -a` shows something like this for a fresh clone. Other people's pushed branches appear here after a `git fetch`.

```
* main
  remotes/origin/HEAD -> origin/main
  remotes/origin/main
```

### Task 2: Push a branch

Everyone in your group works in the same repository, each in their own folder `participants/<your-name>/`. Use your first name in lowercase, for example `anna`.

Never work on `main`. Make a branch named `feature/<your-name>-intro`. On it, add the file `participants/<your-name>/about.md` with a few lines about yourself, and commit it as the only change. Push the branch to the remote so that your local branch is linked to it, and later `git push` and `git pull` need no extra arguments. Then find your branch and your commit on the forge: the branch dropdown on the **Code** tab, and the **Commits** link.

Exercise 5 starts from this branch, so finish this task.

Expected output of the push ends with:

```
 * [new branch]      feature/anna-intro -> feature/anna-intro
branch 'feature/anna-intro' set up to track 'origin/feature/anna-intro'.
```

`git status` says `Your branch is up to date with 'origin/feature/anna-intro'`, and `git branch -a` lists `remotes/origin/feature/anna-intro`.

The forge may show a **Compare & pull request** button, and `git push` prints a `https://<forge>/.../pull/new/feature/anna-intro` link. Do not use them yet.

### Task 3: The remote moved while you were committing

This one is much harder.

A colleague pushes a commit to your branch on the remote while you have a new local commit that is not pushed yet. Do this with a neighbour who has access to your branch (they clone it, add a commit and push), or alone with a second clone of the repository in another folder, which plays the colleague.

1. Make a local commit on your branch, but do not push it yet.
2. Let the colleague push their commit to the same branch first.
3. Before you run `git push`, write down what you expect it to say. Then run it and compare.
4. Get both commits on the remote branch.
5. Explain in your own words how `git fetch` differs from `git pull`, using what you saw in `git log --oneline --graph --all` before and after the fetch.

Rules:

- No `git push --force`, and no `--force-with-lease`.
- Do not delete or recreate the branch.

The push is refused, and Git tells you why:

```
 ! [rejected]        feature/anna-intro -> feature/anna-intro (fetch first)
error: failed to push some refs to '...'
hint: Updates were rejected because the remote contains work that you do not
hint: have locally.
```

After the fetch, `git status -sb` says `[ahead 1, behind 1]`, and the graph has two lines that split from your first commit.

## Open question

After `git fetch` your laptop holds commits that are in none of your own branches. Where are they? You can work a whole week without network: name two things you can do offline with Git, and one you cannot.
