---
layout: default
label: Wrap-up
---

# You can now do <span class="dm-accent">all six things</span>

<div class="grid-3">
<DmInfoCard icon="i-mdi-check-bold" title="Run a script">

From PowerShell and VS Code

</DmInfoCard>
<DmInfoCard icon="i-mdi-check-bold" title="Manage a project">

A .venv per project with uv

</DmInfoCard>
<DmInfoCard icon="i-mdi-check-bold" title="Write a program">

Functions, loops, imports

</DmInfoCard>
<DmInfoCard icon="i-mdi-check-bold" icon-tone="navy" title="Read an error">

Find the line in a stack trace

</DmInfoCard>
<DmInfoCard icon="i-mdi-check-bold" icon-tone="navy" title="Automate files">

Read files, write a summary

</DmInfoCard>
<DmInfoCard icon="i-mdi-check-bold" icon-tone="navy" title="Work with Git">

Branch, commit, push, PR, pull

</DmInfoCard>
</div>

<p class="note">Today: the <b>vocabulary</b> and the tradeoffs. Day 3: you use them to direct and review Copilot and coding agents.</p>

<!--
Go through the list and ask for a show of hands for each item. This is the end level promised for the day. If a point gets few hands, note it for the homework. Close the loop with the opening question: AI can write the code, but you now have the words to ask for the right thing and the understanding to judge what comes back. Offer to stay a few minutes for anyone whose sign-in or pull request did not work.
-->

---
layout: default
label: Wrap-up
---

# Eight commands cover <span class="dm-accent">daily Git</span>

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

# Before <span class="dm-accent">day 2</span>: one full cycle with a PR

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
- Day 3, going deeper: tests, linting, pipelines, coding agents and reviewing their work

</DmColumn>
</DmColumns>

<!--
Day 2 builds on the first column: packages install through uv, the exercises assume you can write a loop and read a file, and we store the work in Git, using .gitignore for data files and nbstripout for notebooks. Learn Git Branching is a good evening activity. Day 3 adds the safety net around it: tests, linting, type checking, pipelines and the branch policy that protects main. Copilot is allowed from today; day 3 goes deeper into coding agents and how to review their work.
-->

---
layout: thanks
---

# Thank <span class="dm-accent">you</span>

See you on day 2

<!--
Thank the group, remind them of the homework, and tell them where to find the slides and exercises.
-->
