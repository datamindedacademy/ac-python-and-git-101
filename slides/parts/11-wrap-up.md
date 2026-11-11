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

# Read these two prompts <span class="dm-accent">again</span>

<DmColumns class="mt-2">
<DmColumn header="Git" tone="navy">

<p class="prompt">Fetch and rebase `feature/max-temperature` onto `origin/main`. If a commit conflicts, stop and show me both sides. Then stage only `analyse_run.py` and commit it as a conventional commit, type `fix`, scope `analysis`. Do not commit `output/`. Push with `--force-with-lease` and draft the pull request description from `git diff origin/main`.</p>

</DmColumn>
<DmColumn header="Python" tone="violet" divider>

<p class="prompt">Write a function `summarize_run(path: Path) -> dict` that reads a CSV log with `csv.DictReader`, converts `pressure_bar` to float, skips and counts rows that raise `ValueError`, and returns the mean and max. Use a list comprehension where it fits. Standard library only, no classes. Add a pytest test using `pytest.approx`.</p>

</DmColumn>
</DmColumns>

<style>
.prompt { font-family: monospace; font-size: 14px; line-height: 1.55; background: var(--dm-surface); border-left: 4px solid var(--dm-connecting); border-radius: 8px; padding: 14px 16px; }
</style>

<!--
Ask the room which terms they could not explain this morning and can now. Any term that is still unclear is a question for now, while we are all here. The Python prompt is the one from the start of the day, the Git prompt is the one from the start of this afternoon.
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
# open the PR, merge it, repeat
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
- **Bring your own work**: a use case, an example or a question

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
Invite everyone to bring something from their own work to the next sessions: a script they want to write, a data file they struggle with, an error they could not solve, or just a question. Real cases make days 2 and 3 better, and we will make time for them. Day 2 builds on the first column: packages install through uv, the exercises assume you can write a loop and read a file, and we store the work in Git, using .gitignore for data files and nbstripout for notebooks. Learn Git Branching is a good evening activity. Day 3 adds the safety net around it: tests, linting, type checking, pipelines and the branch protection rule that protects main. Copilot is allowed from today; day 3 goes deeper into coding agents and how to review their work.
-->

---
layout: default
label: Wrap-up
---

# More from <span class="dm-accent">Dataminded Academy</span>

<div class="grid-3 mt-2 more">
<DmInfoCard icon="i-mdi-docker" title="Containerization with Docker">

Pack a script with its Python and packages, so it runs the same anywhere

<a href="https://github.com/datamindedacademy/containerization_with_docker">github.com/datamindedacademy/<br/>containerization_with_docker</a>

</DmInfoCard>
<DmInfoCard icon="i-mdi-calendar-clock" icon-tone="navy" title="Orchestration with Airflow">

Run scripts on a schedule, in order, with retries and alerts

<a href="https://github.com/datamindedacademy/workflows_with_airflow">github.com/datamindedacademy/<br/>workflows_with_airflow</a>

</DmInfoCard>
<DmInfoCard icon="i-mdi-table-large" title="Polars and PySpark">

Data frames for large logs: Polars on one machine, PySpark on a cluster

<a href="https://github.com/datamindedacademy/dataframe-of-mind">github.com/datamindedacademy/<br/>dataframe-of-mind</a>

</DmInfoCard>
</div>

<style>
.more a { font-family: monospace; font-size: 11.5px; color: var(--dm-connecting); line-height: 1.5; }
</style>

<!--
For after the three days. These are other Dataminded Academy courses, and the material is in public repositories you can work through on your own. Docker is the next step after uv: a container packs the script, the Python version and the packages into one thing that runs the same on a server as on your laptop. Airflow is for when a script has to run every night, after another one, with a retry and an alert when it fails. Polars and PySpark are both for data frames, the tables you meet on day 2 with pandas: Polars when the data still fits on one machine but pandas gets slow, PySpark when it needs a cluster. One repository, dataframe-of-mind, covers the two side by side.
-->

---
layout: thanks
---

# Thank <span class="dm-accent">you</span>

See you on day 2

<!--
Thank the group, remind them of the homework, and tell them where to find the slides and exercises.
-->
