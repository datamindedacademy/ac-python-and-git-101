# Trainer guide: Git exercises

What to prepare on GitHub before the training, how to run the Git part, and what can go wrong.

## 1. Prepare GitHub (about 30 minutes, a few days before)

### Repositories

1. Use your GitHub **organisation** for the training (for example `python-training`).
2. Create **one private repository per group** (for example `training-repo-group-a`). Keep groups to about 10 to 15 people so the Pull requests list stays readable.
3. When you create each repository, leave **Add a README file**, `.gitignore` and licence on "None". An empty repository is easiest to seed.
4. The default branch must be `main`. The first push below creates it.

### Access

Participants need a GitHub account. Ask them to send you the username beforehand.

1. In each repository, open **Settings > Collaborators** (or **Settings > Collaborators and teams**) and invite every participant with the **Write** role. A team with Write access on the repository does the same job.
2. Participants must **accept the invitation** (email or github.com/notifications) before class. Check on the Collaborators page that nobody is still "Pending".
3. Do not give anyone Admin: admins can bypass the protection rule.

Participants must be able to sign in to GitHub in the browser pop-up of Git Credential Manager.

### Branch protection for `main`

Do this after the seed content is pushed (section 2), or the first push is blocked.

Go to **Settings > Branches > Add branch protection rule** (or **Settings > Rules > Rulesets**), target `main`:

1. **Require a pull request before merging**: on.
   - **Require approvals**: on, **1**. The author cannot approve their own pull request, so participants must ask a neighbour.
   - **Dismiss stale pull request approvals when new commits are pushed**: your choice. Off is simpler.
2. **Require conversation resolution**: off (or on, if you want to show it).
3. Leave status checks off. Leave **Do not allow bypassing the above settings** off, so you can still fix things as owner.
4. Leave force pushes and deletions blocked.
5. Under **Settings > General > Pull Requests**, allow **Squash merging** and **Merge commits**.

Test it: with a participant-level account (not an admin), try `git push origin main` after a local change. It must be refused. Then open a PR and check that **Merge pull request** stays disabled until a second person approves.

## 2. Seed content for the training repository

The folder `exercises/git/training-repo-seed/` in this course repository holds the starting content:

| File | Purpose |
|---|---|
| `README.md` | Rules and a map of the repository. |
| `participants/.gitkeep` | Makes Git keep the empty `participants` folder. |
| `.gitignore` | Ignores `.venv/`, `__pycache__/`, `*.pyc`. |
| `check_setup.py` | Tiny script to check that Python runs in the clone. |

Push it to the empty GitHub repository. Work **outside** the course repository, so you do not nest repositories. In PowerShell, from the root of the course repository:

```powershell
Copy-Item -Recurse -Force exercises/git/training-repo-seed "$HOME\seed-upload"
cd "$HOME\seed-upload"
git init -b main
git add --all
git commit -m "Add seed content for the training repository"
git remote add origin https://github.com/<organisation>/<training-repo>.git
git push -u origin main
```

A browser window asks you to sign in on the first push. Afterwards, open the repository page and check that you see `README.md`, `check_setup.py`, `.gitignore` and `participants/`.

For every other group repository, run these two commands in the same folder:

```powershell
git remote set-url origin https://github.com/<organisation>/<training-repo-group-b>.git
git push -u origin main
```

Then set the branch protection rule (section 1) on every repository.

Finally, write down the real URL per group:

```
https://github.com/<organisation>/<training-repo>.git
```

Hand it to participants at the start of exercise 4, for example on the whiteboard or in the chat. The placeholders `<organisation>` and `<training-repo>` in all exercise texts refer to this URL.

## 3. Check the laptops (day before, or first minutes of the day)

On one managed laptop, in PowerShell:

```powershell
git --version
uv --version
git config --global --list
git clone https://github.com/<organisation>/<training-repo>.git "$HOME\git-exercises\test-clone"
```

- Git for Windows is installed and on the PATH.
- Git Credential Manager pops up and signs in (it is part of Git for Windows). If a corporate proxy or conditional access blocks the pop-up, find out now.
- The setup script runs: `uv run python exercises/git/setup_exercise.py 2`.
- `code .` opens VS Code from the terminal.
- The execution policy is `Restricted`. Nothing in these exercises needs `.ps1` files.

Fallback if the laptops cannot reach GitHub: use the devcontainer. Exercises 1 to 3 work offline. For 4 to 6 you can create a local "remote": `git init --bare $HOME\git-exercises\remote.git`, then clone it. Pull requests are not possible then; demonstrate them on your screen.

## 4. Running the session (15:05 to 16:50)

The block is 105 minutes: 30 minutes of instruction and demo, and 75 minutes of exercises.

| Time | Content |
|---|---|
| 15:05 | Slides (about 20 min): why version control, repository, commit, three areas, branch, merge, remote, pull request, GitFlow versus trunk-based in two minutes. |
| 15:25 | Exercise 1 (20 min). Draw the three areas on the whiteboard first. Task 2 is about staging: walk around and ask for the prediction before people run `git status`. |
| 15:45 | Exercise 3 (20 min). The merge conflict is task 2. |
| 16:05 | Hand out the repository URL. Short instruction on remotes and GitHub (about 8 min, live clone). |
| 16:13 | Exercise 4 (15 min). Expect sign-in problems: see below. |
| 16:28 | Exercise 5 (20 min). Pair up neighbours before they start. |
| 16:48 | Demo of exercise 6 in VS Code (about 2 min: the Source Control view only). Point to the README for doing it alone. |
| 16:50 | End. |

Exercise 2 (history) is not done in class. It is for early finishers and for homework. Exercises 3 to 5 do not depend on it. Exercises 1, 3, 4 and 5 add up to 75 minutes. Exercise 6 is a demo only.

Each exercise has two or three tasks. Each task states a result. There are no hints: participants find the commands in the slides, the cheat sheet in `exercises/git/README.md` or `git help`. The full command sequences are in `solutions/git/README.md`. Point a stuck participant to the right slide before you give a command. The last task of each exercise is much harder and has no hint. The times above cover the tasks before it. Most participants will not finish the last task in class, and nothing later depends on it.

**If the day runs late:**

1. Do the merge conflict of exercise 3 (task 2) as a trainer demo on your screen instead of hands-on. Keep task 1 (branch, commit, fast-forward merge) as an exercise.
2. Never drop exercises 4 and 5: they reach the end goal (clone, branch, commit, push, pull request).

Exercise 2 as a whole is for participants who finish early, while you help the others. Mention only briefly: GitFlow versus trunk-based development, cherry-pick, stash, tags. Rebase has a slide and is task 3 of exercise 3.

### Copilot and checking understanding

- Participants may use GitHub Copilot (inline completions and Copilot Chat in VS Code) all day, including in the Git block. The ground rules are in `exercises/git/README.md` under "Using Copilot". No task needs Copilot.
- Not every participant may have an activated Copilot licence yet. Pair those people with a neighbour who has one. Do not spend class time on licence problems.
- Ask participants to type the Git commands themselves. Copilot is for explaining messages and for changing code, which they then inspect with `git diff`.
- To check understanding, walk around, pick two or three people per exercise and ask them to say what they just did. Listen for the terms in the "Words to use" line.
- Every exercise ends with an "Open question" that goes beyond the day. Nobody has to answer it. Answers are in `solutions/git/README.md`.
- The message to repeat: an assistant can write the code, but you must know the words to ask for the right thing, read the diff to judge the result, and own what you commit.

## 5. Common problems

| Problem | Fix |
|---|---|
| Sign-in window does not appear | Run `git credential-manager --version`. Try a fresh `git clone`. Make sure the browser is not blocking pop-ups. |
| `fatal: Authentication failed` after a password change or switch of account | Windows Credential Manager (Control Panel) > Windows Credentials > remove `git:https://github.com`. |
| "Repository not found" or a 403 | URL typo, or the invitation is not accepted yet. Check Settings > Collaborators. |
| `Author identity unknown` on commit | Participant did not do the `git config` step (task 1) of exercise 1. |
| Push to `main` rejected | That is the protection rule working. Participant should make a branch (`git switch -c ...`) and push that. |
| Participant committed on `main` locally | `git switch -c feature/<name>-intro` creates a branch at the current commit. Then in `main`: `git fetch` and `git reset --hard origin/main`. This is outside the exercises, so do it for them. |
| `git pull` says "divergent branches" | Run `git config --global pull.rebase false`, then `git pull` again. This keeps the merge behaviour explained in the exercises. |
| `git branch -d` says "not fully merged" after the PR | The PR was squashed. Use `git branch -D <branch>` once the PR shows Merged. |
| Two participants have the same first name | Add the last initial: `anna-v`. |
| The setup script says the folder exists | Use `--force`. |

## 6. After the training

- Optionally keep the repositories read-only as examples (archive them under **Settings > General > Danger Zone**).
- Delete the repositories when they are no longer needed, and remove the collaborators. Ask Atlas Copco which retention they prefer.
- Nothing in these repositories is secret, but remind participants not to commit real measurement data or credentials in any repository.

## Checking the material

From the repository root:

```powershell
uv run pytest         # checks the solutions and the Git setup script
uv run ruff check .   # lint
```

The slide commands are in [`slides/README.md`](../../slides/README.md).
