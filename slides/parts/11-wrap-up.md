---
layout: section
---

# <span class="dm-accent">Wrap-up</span>

---
layout: default
label: Wrap-up
---

# What you can do <span class="dm-accent">now</span>: Python

<DmColumns class="mt-4">
<DmColumn header="Python" tone="navy">

- Run a script from PowerShell
- Keep a virtual environment per project with uv
- Use functions, conditionals and loops
- Import a package and run it from VS Code

</DmColumn>
<DmColumn header="Working with code" tone="violet" divider>

- Read a stack trace and find the failing line
- Automate a task that reads and writes files

</DmColumn>
</DmColumns>

<!--
Go through the list and ask for a show of hands for each item. This is the end level promised for the Python half. If a point gets few hands, note it for the homework slide.
-->

---
layout: default
label: Wrap-up
---

# What you can do <span class="dm-accent">now</span>: Git

<DmProcess class="mt-6">
<DmPhase label="Clone" />
<DmPhase label="Commit" />
<DmPhase label="Push" />
<DmPhase label="PR" />
<DmPhase label="Pull" />
</DmProcess>

<p class="mt-12 text-center">Clone an Azure DevOps repository, commit on a branch, push, merge through a PR and pull the result. Plus: read the history, undo a change, and recognise a merge conflict.</p>

<!--
This is the end level of the Git half. Ask who feels confident with each step and who wants another go at it. Offer to stay a few minutes for anyone whose sign-in or pull request did not work.
-->

---
layout: default
label: Wrap-up
---

# Git <span class="dm-accent">cheat sheet</span>

<DmColumns class="mt-2">
<DmColumn header="Local" tone="navy">

```powershell
git status
git add <file>
git commit -m "message"
git log --oneline
git diff
git restore <file>
git switch -c <branch>
git merge <branch>
```

</DmColumn>
<DmColumn header="Remote" tone="violet" divider>

```powershell
git clone <url>
git remote -v
git pull
git push -u origin <branch>
git fetch
git branch -d <branch>
git merge --abort
```

</DmColumn>
</DmColumns>

<!--
Point out that this will be in the handout. Eight commands cover almost everything in daily use. Status is the one to run when in doubt.
-->

---
layout: default
label: Wrap-up
---

# Before <span class="dm-accent">day 2</span>

<DmSteps dir="vertical">
<DmStep n="1" label="Working uv environment">Create a project, add a package, run a script from PowerShell and from VS Code.</DmStep>
<DmStep n="2" label="Language fundamentals">Redo the exercises you found hard: functions, loops, files, exceptions.</DmStep>
<DmStep n="3" label="Clone, commit, push, pull">Do one full cycle on Azure DevOps, including a pull request.</DmStep>
</DmSteps>

<!--
Day 2 builds on all three. Pandas and NumPy install through uv, so the environment must work. The data analysis exercises assume you can write a loop and read a file. And we will store the exercises in Git, so the cycle must feel familiar. Ask people to message the trainers if any of the three fails.
-->

---
layout: default
label: Wrap-up
---

# Further <span class="dm-accent">reading</span>

- **Pro Git**, free book: `git-scm.com/book`
- **Learn Git Branching**, interactive visual game: `learngitbranching.js.org`
- **The Python Tutorial**, official: `docs.python.org/3/tutorial`
- **uv documentation**: `docs.astral.sh/uv`
- Azure DevOps Repos documentation: `learn.microsoft.com/azure/devops/repos`

<!--
Pro Git is the reference for everything we skipped, including rebase and stash. Learn Git Branching is a good evening activity: it shows branches as pictures and teaches merge and rebase in small levels. The Python tutorial and uv docs are the ones to bookmark.
-->

---
layout: default
label: Wrap-up
---

# <span class="dm-accent">Day 2</span> and day 3

<DmColumns class="mt-4">
<DmColumn header="Day 2: data analysis" tone="navy">

- pandas and NumPy
- SciPy and Matplotlib
- scikit-learn
- `.gitignore` for data files, nbstripout for notebooks

</DmColumn>
<DmColumn header="Day 3: quality and automation" tone="violet" divider>

- pytest, ruff, type checking
- pre-commit
- Azure DevOps pipelines and branch policies
- GitHub Copilot and coding agents

</DmColumn>
</DmColumns>

<!--
Tomorrow we use what you learned today on real measurement data. The Git habits from this afternoon carry over: you commit your analyses on a branch. Day 3 adds the safety net around it: tests, linting, pipelines and the branch policy that protects main.
-->

---
layout: thanks
---

# Thank <span class="dm-accent">you</span>

See you on day 2

<!--
Thank the group, remind them of the homework, and tell them where to find the slides and exercises.
-->
