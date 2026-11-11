# Exercise 4: Clone from Azure DevOps and push a branch

Core tasks: 1 to 8. Everything under "Optional" is extra.

Words to use: remote, `origin`, clone, push, upstream branch, remote-tracking branch (`origin/main`), fetch.

## Goal

Get a copy of your group's training repository from Azure DevOps. Make a branch with a file in your own folder, and push it to Azure DevOps.

## Why this matters

A script that exists only on your laptop is gone when the laptop is. The remote is the backup, and the only way a colleague gets your work without an email attachment. You use it every day you work in a shared repository.

## Background

So far your repository lived only on your laptop. Real projects have a shared copy on a server. This shared copy is called a **remote**. In this training the remote is an **Azure DevOps Repos** repository. Atlas Copco hosts it, and your group has one.

Terms used in this exercise:

| Term | Meaning |
|---|---|
| **remote** | A copy of the repository on a server. Its default name is `origin`. |
| **clone** | Download a full copy of a remote repository, with its whole history. |
| **push** | Send your commits to the remote. |
| **pull** | Get new commits from the remote and bring them into your branch. |
| **upstream** | The remote branch that your local branch is linked to. |

Everyone in your group works in the same repository. To avoid getting in each other's way, each person only adds files in their own folder: `participants/<your-name>/`. Use your first name in lowercase, without spaces or special characters, for example `anna`.

You sign in with your Atlas Copco account through **Git Credential Manager**. The first time you clone or push, a browser window opens and asks you to sign in. After that, it remembers you.

## Before you start

Your trainer gives you the repository URL. It looks like this:

```
https://dev.azure.com/<organisation>/<project>/_git/<training-repo>
```

Replace the three placeholders with the real values from the trainer. You can also copy the URL in Azure DevOps: open the repository, go to **Repos > Files**, and click **Clone** at the top right.

## Core tasks

### 1. Clone the repository

Put your clone next to your other exercises, not inside the course repository.

```powershell
New-Item -ItemType Directory -Force "$HOME\git-exercises"
cd "$HOME\git-exercises"
git clone https://dev.azure.com/<organisation>/<project>/_git/<training-repo>
```

A sign-in window opens in your browser. Sign in with your work account. Then go back to PowerShell:

```
Cloning into '<training-repo>'...
remote: Azure Repos
remote: Found 8 objects to send. (3 ms)
Receiving objects: 100% (8/8), done.
```

The numbers will differ. Go into the new folder:

```powershell
cd <training-repo>
ls
```

You should see `README.md`, `check_setup.py`, `participants` and (hidden) `.gitignore`.

### 2. Look around

```powershell
git status
git remote -v
git branch
git branch -a
```

What you see:

- `git status` says `On branch main` and `Your branch is up to date with 'origin/main'`.
- `git remote -v` shows that `origin` points to the Azure DevOps URL, for fetch and for push.
- `git branch` lists local branches: only `main`.
- `git branch -a` lists local and remote branches. Remote branches look like `remotes/origin/main`. Other people's pushed branches will appear here too once you fetch.

```
* main
  remotes/origin/HEAD -> origin/main
  remotes/origin/main
```

### 3. Check that Git knows who you are

You did this in exercise 1. Run `git config user.name` and `git config user.email`. Both must print something.

### 4. Make a branch

Never work on `main`. Create a branch with your name in it:

```powershell
git switch -c feature/<your-name>-intro
```

For example `feature/anna-intro`. Branch names with a slash show up as folders in some tools. That is fine.

### 5. Add a file in your folder

Create your personal folder and a file in it. Replace `anna` with your own name everywhere:

```powershell
New-Item -ItemType Directory -Force participants/anna
Set-Content participants/anna/about.md "# Anna`n`nI work in FD. I use Python to analyse compressor test data."
ls participants/anna
cat participants/anna/about.md
```

In PowerShell, the backtick followed by `n` is a new line. If you prefer, open the folder in VS Code (`code .`), create the file there and type your text.

### 6. Commit

```powershell
git status
git add participants/anna/about.md
git commit -m "Add intro for Anna"
git log --oneline
```

Now you have a commit that exists only on your laptop.

### 7. Push your branch

The remote does not know your branch yet. Push it and link it to a remote branch in one go:

```powershell
git push -u origin feature/anna-intro
```

`-u` (short for `--set-upstream`) links your local branch to `origin/feature/anna-intro`. From now on `git push` and `git pull` on this branch need no extra arguments.

Expected output ends with:

```
 * [new branch]      feature/anna-intro -> feature/anna-intro
branch 'feature/anna-intro' set up to track 'origin/feature/anna-intro'.
```

Check:

```powershell
git status
git branch -a
```

`git status` says `Your branch is up to date with 'origin/feature/anna-intro'`. `git branch -a` now lists `remotes/origin/feature/anna-intro`.

### 8. See it in Azure DevOps

Open the repository in your browser. Go to **Repos > Branches**. Find your branch. Click it and open `participants/anna/about.md`. Go to **Repos > Commits** and find your commit with your name and message.

Azure DevOps may show a banner: "You updated feature/anna-intro just now. Create a pull request". Do not click it yet. That is the next exercise.

## Check yourself

Short questions to test yourself after class. The answers are in `solutions/git/README.md`.

1. What is the difference between `git branch` and `git branch -a`?
2. What is `origin`?
3. Why did the first `git push` need `-u origin <branch>`?
4. Why does everyone work in their own `participants/<name>` folder?

## Optional: if you have time

- Run the check script from the repository. It should print your Python version and say hello: `uv run python check_setup.py`.
- Run `git fetch` and then `git branch -a`. Do you see branches of other participants?
- Run `git log --oneline --graph --all --decorate`. Find `origin/main` and your branch.
- In the Azure DevOps web page of your file, click **History** and compare with `git log -- participants/anna/about.md`.

### With Copilot

Use Copilot to explain, then check its explanation against your own repository. Open Copilot Chat (`Ctrl+Alt+I`) and ask:

> What is the difference between `git fetch` and `git pull`? What happens to my remote-tracking branch `origin/main` and to my local branch `main` in each case?

Now run `git fetch`, then `git status` and `git branch -a`. Does what you see match what Copilot said? Which part of its answer could you verify, and which part did you have to take on trust?

## Open question

This goes beyond today. Most people cannot answer it yet. Try it anyway, or bring it to the trainer.

After `git fetch` your laptop holds commits that are in none of your own branches. Where are they? You can work a whole week without network: name two things you can do offline with Git, and one you cannot.
