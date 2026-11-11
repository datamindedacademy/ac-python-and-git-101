# Trainer guide: Git exercises

What to prepare in Azure DevOps before the training, how to run the Git part, and what can go wrong.

## 1. Prepare Azure DevOps (about 30 minutes, a few days before)

### Project and repositories

1. Atlas Copco provides an Azure DevOps **project** for the training (for example `python-training`).
2. Create **one Git repository per group** (for example `training-repo-group-a`). Keep groups to about 10 to 15 people so the Pull requests list stays readable.
3. When you create each repository, **untick** "Add a README" and leave the `.gitignore` option at "None". An empty repository is easiest to seed.
4. Check the default branch name. For new repositories it follows **Organization settings > Repos > Repositories > Settings > Default branch name**. It must be `main`. If that setting is not available to you, the first push below creates `main` anyway.

### Permissions

For every participant (use a group such as the project's **Contributors** group, or a dedicated "Python training" group):

| Permission (Repos > Security) | Setting |
|---|---|
| Read | Allow |
| Contribute | Allow |
| Create branch | Allow |
| Contribute to pull requests | Allow |
| Force push (rewrite history and delete branches) | **Deny** |
| Bypass policies when pushing | **Deny** |
| Bypass policies when completing pull requests | **Deny** |

Participants need at least **Basic** access level in the organisation. Ask Atlas Copco IT to confirm this beforehand. Participants must be able to sign in with their work account on the browser pop-up of Git Credential Manager.

You as trainer need rights to set policies. Note that members of **Project Administrators** can bypass policies by default. That is fine for you, but do not add participants to that group.

### Branch policy for `main`

Do this after the seed content is pushed (section 2), or the first push is blocked.

Go to **Repos > Branches**, open the **...** menu next to `main`, and choose **Branch policies**:

1. **Require a minimum number of reviewers**: on, minimum **1**.
   - **Allow requestors to approve their own changes**: off. This forces participants to ask a neighbour.
   - **Reset all approval votes** when new changes are pushed: your choice. Off is simpler.
2. **Check for linked work items**: off.
3. **Check for comment resolution**: off (or on, if you want to show it).
4. **Limit merge types**: allow **Merge (no fast-forward)** and **Squash merge**. Do not allow only **Rebase** or **Semi-linear**: those force participants to update their branch first, and rebasing a pushed branch is not practised in the exercises.
5. Build validation and automatic reviewers: none.

Test it: with your own account (not an admin), try `git push origin main` after a local change. It must be refused. Then create a PR with a second person's account and see that it cannot complete without an approval.

## 2. Seed content for the training repository

The folder `exercises/git/training-repo-seed/` in this course repository holds the starting content:

| File | Purpose |
|---|---|
| `README.md` | Rules and a map of the repository. |
| `participants/.gitkeep` | Makes Git keep the empty `participants` folder. |
| `.gitignore` | Ignores `.venv/`, `__pycache__/`, `*.pyc`. |
| `check_setup.py` | Tiny script participants run in exercise 4. |

Push it to the empty Azure DevOps repository. Work **outside** the course repository, so you do not nest repositories. In PowerShell, from the root of the course repository:

```powershell
Copy-Item -Recurse -Force exercises/git/training-repo-seed "$HOME\seed-upload"
cd "$HOME\seed-upload"
git init -b main
git add --all
git commit -m "Add seed content for the training repository"
git remote add origin https://dev.azure.com/<organisation>/<project>/_git/<training-repo>
git push -u origin main
```

A browser window asks you to sign in on the first push. Afterwards, open **Repos > Files** and check that you see `README.md`, `check_setup.py`, `.gitignore` and `participants/`.

For every other group repository, run these two commands in the same folder:

```powershell
git remote set-url origin https://dev.azure.com/<organisation>/<project>/_git/<training-repo-group-b>
git push -u origin main
```

Alternatively, in each new repository choose **Import a repository** and use the first repository's URL.

Then set the branch policy (section 1) on every repository.

Finally, write down the real URL per group:

```
https://dev.azure.com/<organisation>/<project>/_git/<training-repo>
```

Hand it to participants at the start of exercise 4, for example on the whiteboard or in the chat. The placeholders `<organisation>`, `<project>` and `<training-repo>` in all exercise texts refer to this URL.

## 3. Check the laptops (day before, or first minutes of the day)

On one managed laptop, in PowerShell:

```powershell
git --version
uv --version
git config --global --list
git clone https://dev.azure.com/<organisation>/<project>/_git/<training-repo> "$HOME\git-exercises\test-clone"
```

- Git for Windows is installed and on the PATH.
- Git Credential Manager pops up and signs in (it is part of Git for Windows). If a corporate proxy or conditional access blocks the pop-up, find out now.
- The setup script runs: `uv run python exercises/git/setup_exercise.py 2`.
- `code .` opens VS Code from the terminal.
- The execution policy is `Restricted`. Nothing in these exercises needs `.ps1` files.

Fallback if the laptops cannot reach Azure DevOps: use the devcontainer. Exercises 1 to 3 work offline. For 4 to 6 you can create a local "remote": `git init --bare $HOME\git-exercises\remote.git`, then clone it. Pull requests are not possible then; demonstrate them on your screen.

## 4. Running the session (15:05 to 16:50)

The block is 105 minutes: about 30 minutes of instruction and 75 minutes of core exercises.

| Time | Content |
|---|---|
| 15:05 | Slides (about 20 min): why version control, repository, commit, three areas, branch, merge, remote, pull request, GitFlow versus trunk-based in two minutes. |
| 15:25 | Exercise 1 (10 min). Draw the three areas on the whiteboard first. |
| 15:35 | Exercise 2 (10 min). |
| 15:45 | Exercise 3 (20 min). The merge conflict is a core task. |
| 16:05 | Hand out the repository URL. Short instruction on remotes and Azure DevOps (about 8 min, live clone). |
| 16:13 | Exercise 4 (15 min). Expect sign-in problems: see below. |
| 16:28 | Exercise 5 (20 min). Pair up neighbours before they start. |
| 16:48 | Demo of exercise 6 in VS Code (about 2 min: the Source Control view only). Point to the README for doing it alone. |
| 16:50 | End. |

Exercise 3 grew from 15 to 20 minutes because the merge conflict is now core. The 5 extra minutes come from the remote instruction (10 to 8 minutes) and the exercise 6 demo (5 to 2 minutes). The block stays at 105 minutes. Times add up to roughly 30 minutes of instruction and 75 minutes of exercises. Exercise 6 is a demo only.

**If the day runs late, drop in this order:**

1. Exercise 2 (history). Show `git log --oneline` and `git show` in one minute during the slides instead.
2. Do the merge conflict of exercise 3 (task 4) as a trainer demo on your screen instead of hands-on. Keep the branch, commit and fast-forward merge as exercises.
3. Never drop exercises 4 and 5: they reach the end goal (clone, branch, commit, push, pull request).

Everything under "Optional: if you have time" in the READMEs is never done in class. The **Challenge** tasks at the end of exercises 1, 2, 3 and 5 are for participants who finish early, while you help the others. Mention only briefly: GitFlow versus trunk-based development, cherry-pick, stash, tags. Rebase has a slide and an optional task in exercise 3.

### Copilot and checking understanding

- Participants may use GitHub Copilot (inline completions and Copilot Chat in VS Code) all day, including in the Git block. The ground rules are in `exercises/git/README.md` under "Using Copilot". No core task needs Copilot.
- Not every participant may have an activated Copilot licence yet. Pair those people with a neighbour who has one for the optional "With Copilot" tasks. Do not spend class time on licence problems.
- Ask participants to type the Git commands themselves. Copilot is for explaining messages and for changing code, which they then inspect with `git diff`.
- To check understanding, walk around, pick two or three people per exercise and ask a "Check yourself" question out loud. Listen for the terms in the "Words to use" line. Model answers are in `solutions/git/README.md`.
- Every exercise ends with an "Open question" that goes beyond the day. Nobody has to answer it. Answers are in `solutions/git/README.md`.
- The message to repeat: an assistant can write the code, but you must know the words to ask for the right thing, read the diff to judge the result, and own what you commit.

## 5. Common problems

| Problem | Fix |
|---|---|
| Sign-in window does not appear | Run `git credential-manager --version`. Try a fresh `git clone`. Make sure the browser is not blocking pop-ups. |
| `fatal: Authentication failed` after a password change or switch of account | Windows Credential Manager (Control Panel) > Windows Credentials > remove `git:https://dev.azure.com`. |
| `TF401019` or "repository does not exist or you do not have permission" | URL typo, or the person is not in the permission group. Check Repos > Security. |
| `Author identity unknown` on commit | Participant did not do the `git config` step of exercise 1. |
| Push to `main` rejected | That is the policy working. Participant should make a branch (`git switch -c ...`) and push that. |
| Participant committed on `main` locally | `git switch -c feature/<name>-intro` creates a branch at the current commit. Then in `main`: `git fetch` and `git reset --hard origin/main`. This is outside the exercises, so do it for them. |
| `git pull` says "divergent branches" | Run `git config --global pull.rebase false`, then `git pull` again. This keeps the merge behaviour explained in the exercises. |
| `git branch -d` says "not fully merged" after the PR | The PR was squashed. Use `git branch -D <branch>` once the PR shows Completed. |
| Two participants have the same first name | Add the last initial: `anna-v`. |
| The setup script says the folder exists | Use `--force`. |

## 6. After the training

- Optionally keep the repositories read-only as examples (set **Contribute** to Deny for the group).
- Delete the repositories when they are no longer needed. Ask Atlas Copco which retention they prefer.
- Nothing in these repositories is secret, but remind participants not to commit real measurement data or credentials in any repository.

## Checking the material

From the repository root:

```powershell
uv run pytest         # checks the solutions and the Git setup script
uv run ruff check .   # lint
```

The slide commands are in [`slides/README.md`](../../slides/README.md).
