---
layout: default
label: Wrap-up
---

# What you can do <span class="dm-accent">now</span>

<DmColumns class="mt-2">
<DmColumn header="Python" tone="navy">

- Run a script from PowerShell and from VS Code
- A virtual environment per project with uv
- Functions, conditionals, loops, importing a package
- Read a stack trace
- Read a folder of files and write a summary

</DmColumn>
<DmColumn header="Git" tone="violet" divider>

- Clone an Azure DevOps repository
- Commit on a branch
- Push, merge through a PR and pull
- Read history, undo a change, recognise a conflict

</DmColumn>
</DmColumns>

<!--
Go through the list and ask for a show of hands for each item. This is the end level promised for the day. If a point gets few hands, note it for the homework. Offer to stay a few minutes for anyone whose sign-in or pull request did not work.
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
git switch main
git pull
git switch -c feature/x
git push -u origin feature/x
# open the PR, complete it, repeat
```

</DmColumn>
</DmColumns>

<style>
.slidev-code { font-size: 14px !important; line-height: 1.5 !important; }
</style>

<!--
Point out that this will be in the handout. Eight commands cover almost everything in daily use, and the right column is the daily cycle: update main, branch, commit, push, pull request, then back to the start. Status is the one to run when in doubt.
-->

---
layout: default
label: Wrap-up
---

# Before <span class="dm-accent">day 2</span>, and beyond

<DmColumns class="mt-2">
<DmColumn header="Before day 2" tone="navy">

- A working uv environment
- Redo the fundamentals you found hard
- One full clone, commit, push, pull cycle with a PR

</DmColumn>
<DmColumn header="Read more" tone="plain" divider>

- Pro Git book (`git-scm.com/book`)
- Learn Git Branching (`learngitbranching.js.org`)
- Python tutorial (`docs.python.org/3/tutorial`)
- uv docs (`docs.astral.sh/uv`)

</DmColumn>
<DmColumn header="Next days" tone="violet" divider>

- Day 2: pandas, NumPy, SciPy, Matplotlib, scikit-learn
- Day 3: pytest, ruff, pre-commit, pipelines, Copilot

</DmColumn>
</DmColumns>

<!--
Day 2 builds on the first column: packages install through uv, the exercises assume you can write a loop and read a file, and we store the work in Git, using .gitignore for data files and nbstripout for notebooks. Learn Git Branching is a good evening activity. Day 3 adds the safety net around it: tests, linting, type checking, pipelines and the branch policy that protects main, plus GitHub Copilot and coding agents.
-->

---
layout: thanks
---

# Thank <span class="dm-accent">you</span>

See you on day 2

<!--
Thank the group, remind them of the homework, and tell them where to find the slides and exercises.
-->
