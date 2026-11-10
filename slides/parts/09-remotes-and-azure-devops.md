---
layout: section
---

# Remotes and <span class="dm-accent">Azure DevOps</span>

---
layout: default
label: 9 · Remotes and Azure DevOps
---

# <span class="dm-accent">Clone</span> a repository

```powershell
git clone https://dev.azure.com/<organisation>/<project>/_git/<training-repo>
cd <training-repo>
git remote -v
```

```text
origin  https://dev.azure.com/<organisation>/<project>/_git/<training-repo> (fetch)
```

- The first time, a browser window asks you to sign in (Git Credential Manager)
- `clone` creates the remote `origin`; the URL is on the **Clone** button in Azure DevOps

<style>
.slidev-code { font-size: 16px !important; line-height: 1.5 !important; }
</style>

<!--
Clone copies the whole repository, history included, into a new folder and sets up the remote for you. The sign-in popup is Git Credential Manager, which ships with Git for Windows and remembers the token afterwards. Origin is only the default nickname for the URL. Do not clone into a OneDrive or network folder; use a local path.
-->

---
layout: default
label: 9 · Remotes and Azure DevOps
---

# <span class="dm-accent">Push</span> and <span class="dm-accent">pull</span>

```powershell
git push -u origin feature/bar-to-psi   # first push of a new branch
git push                                 # later pushes
git pull                                 # fetch and merge new commits
git fetch                                # only download, change nothing
```

- `-u` links your local branch to the remote one, needed only once
- `pull` is `fetch` plus merge: commit or restore your edits first

<style>
.slidev-code { font-size: 16px !important; line-height: 1.5 !important; }
</style>

<!--
The first push of a new branch creates it on the server, and Azure DevOps prints a link in the output to create a pull request. Pull is what you type daily. Fetch is the careful variant when you want to see what is coming before it touches your files. If a pull produces a conflict, it is the same conflict you saw earlier.
-->

---
layout: statement
title: Exercise - Azure DevOps remote
---

# Exercise time: <span class="dm-accent">Azure DevOps remote</span>

<p class="mt-6 text-lg opacity-80"><code>exercises/git/04-azure-devops-remote</code></p>
<p class="mt-2 text-sm opacity-70">About 15 minutes: clone, branch, commit, push</p>

<!--
Participants clone the training repository from Azure DevOps, create a branch, commit a small change and push it. This is the first time they sign in, so expect a few authentication questions. Have the URL on screen.
-->

---
layout: default
label: 9 · Remotes and Azure DevOps
---

# The pull request <span class="dm-accent">flow</span>

<DmProcess class="mt-4">
<DmPhase label="Push" />
<DmPhase label="Create" />
<DmPhase label="Review" />
<DmPhase label="Approve" />
<DmPhase label="Complete" />
</DmProcess>

<div class="mt-8"></div>
<ul>
  <li>A pull request (PR) proposes merging your branch into <code>main</code>; colleagues read the diff first</li>
  <li><b>Complete</b>: pick the merge type (squash keeps <code>main</code> readable), tick <b>Delete source branch</b></li>
  <li>Afterwards update your laptop: <code>git switch main</code>, <code>git pull</code></li>
</ul>

<!--
Nobody commits straight to main; changes arrive through a PR that someone else reads. The PR is an Azure DevOps feature, not a Git one. Walk through the screens live if you can: the Files tab with the diff, comments, the Approve button and the Complete dialog. Squash merge turns a branch of ten messy commits into one clean one. After completing, pull on main so your laptop knows about the merge. On day 3 we make PRs mandatory with a branch policy.
-->

---
layout: statement
title: Exercise - pull request
---

# Exercise time: <span class="dm-accent">pull request</span>

<p class="mt-6 text-lg opacity-80"><code>exercises/git/05-pull-request</code></p>
<p class="mt-2 text-sm opacity-70">About 20 minutes: PR into main, review, complete, pull</p>

<!--
Participants open a pull request for the branch from the previous exercise, review a neighbour's PR, complete it and pull the result. Pair people up so everyone gets to review.
-->

---
layout: default
label: 9 · Remotes and Azure DevOps
---

# Keep files out: <span class="dm-accent">.gitignore</span>

```text
# .gitignore
.venv/
__pycache__/
data/raw/
```

- One pattern per line; commit the file itself so everyone shares it
- Never commit passwords, tokens or large raw data
- Day 2 uses it for data files and notebooks

<style>
.slidev-code { font-size: 16px !important; line-height: 1.5 !important; }
</style>

<!--
Some files do not belong in history: the virtual environment that uv creates, Python's cache folders, large measurement dumps, and anything secret. List them in a file called dot gitignore and Git will skip them. Ignoring only helps for files not yet committed. Tomorrow we add more patterns for data files.
-->

---
layout: default
label: 9 · Remotes and Azure DevOps
---

# Three ways to use <span class="dm-accent">Git</span>

<DmComparison
  class="mt-2"
  :rows="['Advantages', 'Disadvantages', 'Use it when']"
  :cols="['Command line', 'VS Code', 'SourceTree']"
>
  <template #r0c0>Every feature, same everywhere, easy to copy into notes</template>
  <template #r0c1>Already open, diff and conflict views built in</template>
  <template #r0c2>Clear graph of branches, point and click</template>

  <template #r1c0>Commands to learn, easy to mistype</template>
  <template #r1c1>Hides the commands, fewer rare features</template>
  <template #r1c2>Extra install, less common on managed laptops</template>

  <template #r2c0>You need full power, or help from a colleague or a doc</template>
  <template #r2c1>Daily edit, commit, push work next to the code</template>
  <template #r2c2>You want to browse a complex history visually</template>
</DmComparison>

<!--
No tool is wrong. All three drive the same Git, so you can switch between them in the same repository. We teach the command line first because it shows what Git actually does, and because every tutorial and error message uses it. Many people then settle on VS Code for daily work. Next is a short demo of the Source Control view.
-->

---
layout: statement
title: Demo - Git in VS Code
---

# Demo: <span class="dm-accent">Git in VS Code</span>

<p class="mt-6 text-lg opacity-80">Optional practice: <code>exercises/git/06-git-in-vscode</code></p>

<!--
Trainer demo of the same cycle in the Source Control view (control shift G): changed files, click for the diff, plus to stage, message and Commit, Sync Changes for push and pull, and the branch name at the bottom left. Show a .gitignore taking effect. Participants can do exercise 06 afterwards in their own time.
-->
