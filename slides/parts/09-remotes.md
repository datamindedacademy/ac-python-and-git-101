---
layout: section
---

# Remotes and <span class="dm-accent">pull requests</span>

---
layout: default
label: 9 · Remotes
---

# <span class="dm-accent">Clone</span> copies the repository and its history

```powershell
git clone https://<forge>/<organisation>/<training-repo>.git
cd <training-repo>
git remote -v
```

```text
origin  https://<forge>/<organisation>/<training-repo>.git (fetch)
```

- The first time, a browser window asks you to sign in (Git Credential Manager)
- `clone` creates the remote `origin`; the URL is on the repository page of the forge

<style>
.slidev-code { font-size: 16px !important; line-height: 1.5 !important; }
</style>

<!--
Clone copies the whole repository, history included, into a new folder and sets up the remote for you. The sign-in popup is Git Credential Manager, which ships with Git for Windows and remembers the token afterwards. Origin is only the default nickname for the URL. Atlas Copco uses Azure DevOps, which comes on day 3, and the Git commands are identical; only the web pages differ. Do not clone into a OneDrive or network folder; use a local path.
-->

---
layout: default
label: 9 · Remotes
---

# <span class="dm-accent">Push</span> uploads commits, <span class="dm-accent">pull</span> downloads them

```powershell
git push -u origin feature/bar-to-psi   # first push of a new branch
git push                                 # later pushes
git pull                                 # fetch and merge new commits
git fetch                                # only download, change nothing
```

- `-u` sets the upstream: it links your local branch to the remote one, needed only once
- `origin/main` is a **remote-tracking branch**: your laptop's last known copy of `main` on the server, updated by `fetch` and `pull`
- `pull` is `fetch` plus merge: commit or restore your edits first

<p class="ask" v-click><b>Question</b>Your laptop is stolen on the train. Which work is gone?</p>

<style>
.slidev-code { font-size: 16px !important; line-height: 1.5 !important; }
</style>

<!--
The first push of a new branch creates it on the server, and the forge prints a link in the output to open a pull request. On the repository page it also shows a **Compare & pull request** button. Pull is what you type daily. Fetch is the careful variant when you want to see what is coming before it touches your files. The upstream is the remote branch your local branch follows, so later push and pull need no arguments. Origin slash main is a remote-tracking branch: your laptop's memory of main on the server, which only changes when you fetch or pull. If a pull produces a conflict, it is the same conflict you saw earlier. Question on the slide: every commit you did not push, and every change you did not commit. What is on the server is safe. Push at the end of every working session.
-->

---
layout: statement
title: Exercise - remote
---

# Exercise time: <span class="dm-accent">the remote</span>

<p class="mt-6 text-lg opacity-80"><code>exercises/git/04-remote</code></p>
<p class="mt-2 text-sm opacity-70">About 15 minutes: clone, branch, commit, push</p>

<!--
Participants clone the training repository from the forge, create a branch, commit a small change and push it. This is the first time they sign in, so expect a few authentication questions. Have the URL on screen.
-->

---
layout: default
label: 9 · Remotes
---

# A <span class="dm-accent">pull request</span> lets a colleague review first

<DmProcess class="mt-4">
<DmPhase label="Push" />
<DmPhase label="Open" />
<DmPhase label="Review" />
<DmPhase label="Approve" />
<DmPhase label="Merge" />
</DmProcess>

<div class="grid-3 mt-8">
<DmInfoCard icon="i-mdi-source-pull" title="Propose">

A pull request (PR) proposes merging your branch into `main`. Colleagues read the diff first.

</DmInfoCard>
<DmInfoCard icon="i-mdi-check-all" title="Merge">

Click **Merge pull request** (squash keeps `main` readable), then **Delete branch**.

</DmInfoCard>
<DmInfoCard icon="i-mdi-laptop" icon-tone="navy" title="Update your laptop">

`git switch main`, then `git pull`

</DmInfoCard>
</div>

<p class="note">A <b>branch protection rule</b> on <code>main</code> can require a pull request with an approval before it can be merged.</p>

<!--
Nobody commits straight to main; changes arrive through a PR that someone else reads. The PR is a feature of the forge, not a Git one. Walk through the screens live if you can: the Files tab with the diff, comments, the Approve option in Review changes and the Merge pull request button. Squash merge turns a branch of ten messy commits into one clean one. After merging, pull on main so your laptop knows about the merge. On day 3 we make PRs mandatory with a branch protection rule.
-->

---
layout: statement
title: Exercise - pull request
---

# Exercise time: <span class="dm-accent">pull request</span>

<p class="mt-6 text-lg opacity-80"><code>exercises/git/05-pull-request</code></p>
<p class="mt-2 text-sm opacity-70">About 20 minutes: PR into main, review, merge, pull</p>

<!--
Participants open a pull request for the branch from the previous exercise, review a neighbour's PR, merge it and pull the result. Pair people up so everyone gets to review.
-->

---
layout: default
label: 9 · Remotes
---

# <span class="dm-accent">.gitignore</span> keeps files out of history

```text
# .gitignore
.venv/
__pycache__/
data/raw/
```

- One pattern per line; commit the file itself so everyone shares it
- Never commit passwords, tokens or large raw data
- Day 2 uses it for data files and notebooks

<p class="note">A <b>tracked</b> file is one Git already follows. <code>.gitignore</code> only works on files that are not tracked yet: they become <b>ignored</b>.</p>

<style>
.slidev-code { font-size: 16px !important; line-height: 1.5 !important; }
</style>

<!--
Some files do not belong in history: the virtual environment that uv creates, Python's cache folders, large measurement dumps, and anything secret. List them in a file called dot gitignore and Git will skip them. Ignoring only helps for files not yet committed. Tomorrow we add more patterns for data files.
-->

---
layout: statement
title: Demo - Git in VS Code
---

# Demo: <span class="dm-accent">Git in VS Code</span>

<p class="mt-6 text-lg opacity-80">Optional practice: <code>exercises/git/06-git-in-vscode</code></p>

<p class="mt-4 text-sm opacity-80">In the <b>Source Control view</b>: + stages, Commit commits, <b>Publish Branch</b> is the first push, <b>Sync Changes</b> pulls and then pushes.</p>

<p class="words"><b>Words you can now use</b> clone · origin · push · pull · fetch · upstream · origin/main · pull request · review</p>

<style>
.words { font-size: 15px; opacity: 0.9; margin-top: 40px; }
.words b { margin-right: 8px; }
</style>

<!--
Trainer demo of the same cycle in the Source Control view (control shift G): changed files, click for the diff, plus to stage, message and Commit, Sync Changes for push and pull, and the branch name at the bottom left. Show a .gitignore taking effect. Participants can do exercise 06 afterwards in their own time.
-->

---
layout: statement
title: Questions - remotes
---

# Questions?

<p class="mt-6 text-lg opacity-80">remotes</p>

<!--
Pause here. Ask for questions on clone, push, pull, pull requests and .gitignore. Wait a few seconds longer than feels comfortable. If nobody asks, ask one person what was least clear.
-->
