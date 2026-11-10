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
git status
```

```text
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

- The first time, a browser window asks you to sign in (Git Credential Manager)
- The URL is on the **Clone** button of the repository in Azure DevOps

<!--
Clone copies the whole repository, history included, into a new folder, and sets up the remote for you. The sign-in popup is Git Credential Manager, which ships with Git for Windows and remembers the token afterwards. Do not clone into a OneDrive or network folder; use a local path.
-->

---
layout: default
label: 9 · Remotes and Azure DevOps
---

# The remote is called <span class="dm-accent">origin</span>

```powershell
git remote -v
```

```text
origin  https://dev.azure.com/<organisation>/<project>/_git/<training-repo> (fetch)
origin  https://dev.azure.com/<organisation>/<project>/_git/<training-repo> (push)
```

- `clone` created the remote named `origin` for you
- `origin/main` is your laptop's memory of where `main` was on the server
- A local repository made with `git init` has no remote until you add one

<!--
Origin is only a default name, a nickname for the URL. The branch origin/main is a bookmark that your laptop updates whenever it talks to the server. That explains why status can say you are ahead or behind: it compares your main with that bookmark.
-->

---
layout: default
label: 9 · Remotes and Azure DevOps
---

# Share a branch: <span class="dm-accent">push -u</span>

```powershell
git switch -c feature/bar-to-psi
git add conversions.py
git commit -m "Add bar to psi conversion"
git push -u origin feature/bar-to-psi
```

```text
To https://dev.azure.com/<organisation>/<project>/_git/<training-repo>
 * [new branch]      feature/bar-to-psi -> feature/bar-to-psi
branch 'feature/bar-to-psi' set up to track 'origin/feature/bar-to-psi'.
```

- `-u` is needed only the first time; later a plain `git push` is enough

<!--
The first push of a new branch creates it on the server. Dash u links your local branch to the remote one, so later push and pull know where to go. Azure DevOps also prints a link in the push output to create a pull request, which is handy.
-->

---
layout: default
label: 9 · Remotes and Azure DevOps
---

# <span class="dm-accent">Fetch</span> or <span class="dm-accent">pull</span>

<DmColumns class="mt-4">
<DmColumn header="git fetch" tone="navy">

- Downloads new commits from the server
- Does not change your files or branches
- Safe at any time
- Then look: `git log origin/main`

</DmColumn>
<DmColumn header="git pull" tone="violet" divider>

- Fetch, then merge into your current branch
- Updates your files
- Do it on `main` before you start new work
- Commit or restore your edits first

</DmColumn>
</DmColumns>

<!--
Pull is fetch plus merge. For daily use, pull is what you type. Fetch is the careful variant when you want to see what is coming before it touches your files. If a pull produces a conflict, it is the same conflict you saw earlier.
-->

---
layout: statement
title: Exercise - Azure DevOps remote
---

# Exercise time: <span class="dm-accent">Azure DevOps remote</span>

<p class="mt-6 text-lg opacity-80"><code>exercises/git/04-azure-devops-remote</code></p>

<!--
Participants clone the training repository from Azure DevOps, create a branch, commit a small change and push it. This is the first time they sign in, so expect a few authentication questions. Allow about twenty minutes, and have the URL on screen.
-->

---
layout: default
label: 9 · Remotes and Azure DevOps
---

# The pull request <span class="dm-accent">flow</span>

<DmProcess class="mt-6">
<DmPhase label="Push" />
<DmPhase label="Create" />
<DmPhase label="Review" />
<DmPhase label="Approve" />
<DmPhase label="Complete" />
</DmProcess>

<ul class="mt-12">
  <li>A pull request (PR) proposes merging a branch into <code>main</code></li>
  <li>Colleagues read the diff and comment before anything changes on <code>main</code></li>
  <li>It is a feature of Azure DevOps, not of Git</li>
</ul>

<!--
This is the heart of teamwork on the platform. Nobody commits straight to main; changes arrive through a PR that someone else reads. Even if you work alone, the PR gives you a moment to look at your own diff. On day 3 we make this mandatory with a branch policy.
-->

---
layout: default
label: 9 · Remotes and Azure DevOps
---

# In Azure DevOps: <span class="dm-accent">Repos, Pull requests</span>

<DmSteps dir="vertical">
<DmStep n="1" label="Create">New pull request: source <code>feature/...</code>, target <code>main</code>, add a title and description.</DmStep>
<DmStep n="2" label="Review">Reviewers read the Files tab and comment on lines.</DmStep>
<DmStep n="3" label="Approve">A reviewer approves, or waits for changes.</DmStep>
<DmStep n="4" label="Complete">Choose the merge type, tick <b>Delete source branch</b>, confirm.</DmStep>
</DmSteps>

<!--
Walk through the screens live if you have a demo repository. Point out the Files tab with the diff, the comments with resolve buttons, and the Complete dialog. Stress deleting the source branch: branches are disposable once merged.
-->

---
layout: default
label: 9 · Remotes and Azure DevOps
---

# Merge types when you <span class="dm-accent">complete</span>

| Merge type | Result on `main` |
| --- | --- |
| Merge (no fast-forward) | All commits kept, plus a merge commit |
| Squash merge | One single commit for the whole PR |
| Rebase and fast-forward | Commits replayed, straight line |
| Semi-linear merge | Rebase, then a merge commit |

<div class="mt-4"></div>

- For small feature branches, squash merge keeps `main` readable
- Use what the team agrees on; it can be set per repository

<!--
Do not go deep. The first option is what you did locally with git merge. Squash is popular because it turns a branch with ten messy commits into one clean one. Rebase comes back on the exists-not-today slide in the next section, so just name it. The team lead can fix the allowed types in repository settings.
-->

---
layout: default
label: 9 · Remotes and Azure DevOps
---

# After the merge: <span class="dm-accent">update local</span>

```powershell
git switch main
git pull
git branch -d feature/bar-to-psi
```

```text
Updating 9b221ad..5c0e1fa
Fast-forward
 conversions.py | 3 +++
 1 file changed, 3 insertions(+)
Deleted branch feature/bar-to-psi (was 1cd9279).
```

- Your laptop does not know about the merge until you pull

<!--
The merge happened on the server, so your local main is behind. Switch to main, pull, and delete the local feature branch. After this you are ready to start the next piece of work from an up to date main. If branch dash d refuses, the branch is not merged in the way Git can see, for example after a squash; ask the trainer.
-->

---
layout: statement
title: Exercise - pull request
---

# Exercise time: <span class="dm-accent">pull request</span>

<p class="mt-6 text-lg opacity-80"><code>exercises/git/05-pull-request</code></p>

<!--
Participants open a pull request for the branch from the previous exercise, review a neighbour's PR, complete it and pull the result. Pair people up so everyone gets to review. About twenty minutes.
-->

---
layout: default
label: 9 · Remotes and Azure DevOps
---

# The daily <span class="dm-accent">cycle</span>

<DmProcess class="mt-2">
<DmPhase label="Update" />
<DmPhase label="Branch" />
<DmPhase label="Commit" />
<DmPhase label="Push" />
<DmPhase label="PR" />
</DmProcess>

```powershell
git switch main; git pull
git switch -c feature/x
git add <file>; git commit -m "message"
git push -u origin feature/x
# create, review and complete the PR in Azure DevOps, then repeat
```


<!--
This is the whole day on one slide. Repeat it out loud. If they can do these five steps without looking, they have reached the end level of the day. Everything else, such as history and conflicts, is support for this loop.
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
.ipynb_checkpoints/
data/raw/
```

```powershell
git add .gitignore
git commit -m "Ignore virtual environment and raw data"
```

- One pattern per line; commit the file itself so everyone shares it
- Never commit passwords, tokens or large raw data
- Day 2 uses it for data files and notebooks

<!--
Some files do not belong in history: the virtual environment that uv creates, Python's cache folders, large measurement dumps, and anything secret. List them in a file called dot gitignore and Git will skip them. Note that ignoring only helps for files not yet committed. Tomorrow we add more patterns for data files.
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
  <template #r0c0>Every feature, same everywhere, easy to copy into notes and scripts</template>
  <template #r0c1>Already open, diff and conflict views built in</template>
  <template #r0c2>Clear graph of branches, point and click</template>

  <template #r1c0>Commands to learn, easy to mistype</template>
  <template #r1c1>Hides the commands, fewer rare features</template>
  <template #r1c2>Extra install, less common on managed laptops</template>

  <template #r2c0>You need the full power, or help from a colleague or a doc</template>
  <template #r2c1>Daily edit, commit, push work next to the code</template>
  <template #r2c2>You want to browse a complex history visually</template>
</DmComparison>

<!--
No tool is wrong. All three drive the same Git, so you can switch between them in the same repository. We teach the command line first because it shows what Git actually does, and because every tutorial and error message uses it. Many people then settle on VS Code for daily work and use the terminal for the rest.
-->

---
layout: default
label: 9 · Remotes and Azure DevOps
---

# The same cycle in <span class="dm-accent">VS Code</span>

| Command line | Source Control view |
| --- | --- |
| `git status` | List of changed files |
| `git diff` | Click a file to see the diff |
| `git add` | Plus icon next to a file |
| `git commit -m "..."` | Type a message, press Commit |
| `git switch -c` | Branch name at the bottom left |
| `git push` / `git pull` | Sync Changes and the three-dot menu |

<!--
Open the Source Control view with control shift G. Every command we have used has a button. Show one complete round trip: edit a file, stage it, write the message, commit and sync. The status bar shows the current branch and lets you create or switch branches.
-->

---
layout: statement
title: Exercise - Git in VS Code
---

# Exercise time: <span class="dm-accent">Git in VS Code</span>

<p class="mt-6 text-lg opacity-80"><code>exercises/git/06-git-in-vscode</code></p>

<!--
The same cycle through the Source Control view, plus a .gitignore. Participants who prefer the terminal may mix both, since they act on the same repository. About fifteen minutes.
-->
