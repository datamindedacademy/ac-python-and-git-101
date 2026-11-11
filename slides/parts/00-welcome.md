---
layout: intro
role: Dataminded
---

# Jan <span class="dm-accent">Vanbuel</span>

<p class="mt-4">Your trainer today. Ask early, ask often: stuck for five minutes means wave at me.</p>

<!--
Introduce yourself briefly, then ask the room three questions with a show of hands: who has used MATLAB, who has written Excel macros or VBA, and who has written a little Python. That tells you how much to lean on the MATLAB analogies. Say clearly that Day 1 assumes some scripting experience and focuses on what is specific to Python. You are the only trainer today, so ask people to help their neighbour first while you walk around during the exercises.
-->

---
layout: default
label: Welcome
---

# Today covers three things you will use <span class="dm-accent">every week</span>

<div class="grid-3 mt-2">
  <DmIconBadge icon="i-mdi-laptop" label="Development environment" sub="Python, uv, VS Code, PowerShell" />
  <DmIconBadge icon="i-mdi-language-python" tone="dark" label="Programming fundamentals" sub="Types, loops, functions, files" />
  <DmIconBadge icon="i-mdi-source-branch" label="Version control" sub="Git and Azure DevOps" />
</div>

<p class="note">Some scripting experience assumed (MATLAB, VBA or a little Python). We focus on what is specific to Python.</p>

<!--
The three blocks of the day. The environment comes first because nothing else works without it. Fundamentals is the biggest block. Git gets the end of the day, when you are comfortable with files and the terminal. The day assumes some scripting experience, so we spend the time on what is specific to Python.
-->

---
layout: default
label: Welcome
---

# AI writes code, you <span class="dm-accent">ask, judge and choose</span>

<div class="grid-3 mt-2">
<DmInfoCard icon="i-mdi-chat-question-outline" title="Ask">

You have to ask in the specialist's **vocabulary**

</DmInfoCard>
<DmInfoCard icon="i-mdi-scale-balance" icon-tone="navy" title="Judge">

You have to read what comes back and decide if it is **right**

</DmInfoCard>
<DmInfoCard icon="i-mdi-call-split" title="Choose">

There are several approaches, and someone must own the **tradeoff**

</DmInfoCard>
</div>

<p class="note">"Loop over the CSV files in this folder and return a dict per run" beats "make it work for all my files".</p>

<!--
An assistant like Copilot can write a working script in seconds, so why spend a day on fundamentals? Because the quality of what you get depends on what you ask. Compare the two requests on the slide. Then you have to read the result and judge it: is it correct, does it handle the empty file, is it the simple version or the clever one? And there is nearly always more than one way, each with a cost, and the tool will pick one silently unless you say what you want. Today gives you the words and the tradeoffs. That is the part that stays yours.
-->

---
layout: default
label: Welcome
---

# This prompt will <span class="dm-accent">make sense</span> by 15:00

<p class="prompt">Write a function `summarize_run(path: Path) -> dict` that reads a CSV log with `csv.DictReader`, converts `pressure_bar` to float, skips and counts rows that raise `ValueError`, and returns the mean and max. Use a list comprehension where it fits. Standard library only, no classes. Add a pytest test using `pytest.approx`.</p>

<style>
.prompt { font-family: monospace; font-size: 19px; line-height: 1.6; background: var(--dm-surface); border-left: 4px solid var(--dm-connecting); border-radius: 8px; padding: 18px 22px; margin-top: 16px; }
</style>

<!--
This is what a specialist asks for. Every term in it is taught today: csv.DictReader, float conversion, ValueError and skipping bad rows, list comprehension, the standard library, pytest and pytest.approx, type hints and Path. Do not explain anything now. The same slide comes back in the wrap-up.
-->


---
layout: default
label: Welcome
---

# Use Copilot, keep only lines <span class="dm-accent">you understand</span>

<div class="grid-3 mt-2">
<DmInfoCard icon="i-mdi-alert-circle-outline" title="Explain errors">

Paste the error and ask what it means and where to look

</DmInfoCard>
<DmInfoCard icon="i-mdi-compare-horizontal" title="Ask for a second way">

Then compare the two and pick the simpler one

</DmInfoCard>
<DmInfoCard icon="i-mdi-account-check-outline" icon-tone="navy" title="Own the commit">

Your name is on it. Understand every line, or replace it

</DmInfoCard>
</div>

<!--
GitHub Copilot is allowed all day, starting now. The most valuable uses today are asking it to explain an error message or a piece of code, and asking for a second way to do the same thing so you can compare. The one habit I insist on: if you do not understand a line, ask Copilot to explain it or replace it with something you understand. Your name is on the commit, so the responsibility is yours. One more habit, from Oliver's Clean Code workshop: keep it simple. The simplest version that works is the one to keep, and assistants tend to over-build, so ask for less. Some of you may not have an activated licence yet: pair up with a neighbour who has one, the exercises all work without it too. Day 3 goes deeper into agents, skills and reviewing AI-written code.
-->

---
layout: default
label: Welcome
---

# Judge code in this order: <span class="dm-accent">correct, readable, fast</span>

<div class="grid-3 mt-2">
  <DmIconBadge icon="i-mdi-check-decagram" tone="dark" label="1 · Correct" sub="Does it do what it should?" />
  <DmIconBadge icon="i-mdi-book-open-variant" label="2 · Readable" sub="Will you understand it in two months?" />
  <DmIconBadge icon="i-mdi-speedometer" label="3 · Fast" sub="Is it fast enough? Ask this last." />
</div>

<!--
From Oliver's Clean Code workshop. This is the checklist for the Judge step, and the order matters. First check that the code is correct: run it, try an odd input, compare with a value you know. Then check that it is readable, because code is read far more often than it is written. Performance comes last, because correct and readable code can be made fast, while the reverse is much harder. Use these three questions on everything Copilot hands back today.
-->

---
layout: default
label: Welcome
---

# By 17:00 you can do <span class="dm-accent">six things</span> on your own laptop

<div class="grid-3 goals">
<v-clicks>
<DmInfoCard icon="i-mdi-console" title="Run a script">

Set up Python and run a script from PowerShell

</DmInfoCard>
<DmInfoCard icon="i-mdi-package-variant-closed" title="Manage a project">

A virtual environment per project, packages with uv

</DmInfoCard>
<DmInfoCard icon="i-mdi-code-braces" title="Write a program">

Functions, conditions, loops and imports, run from VS Code

</DmInfoCard>
<DmInfoCard icon="i-mdi-bug-outline" icon-tone="navy" title="Read an error">

Find the line a stack trace points to

</DmInfoCard>
<DmInfoCard icon="i-mdi-file-document-multiple-outline" icon-tone="navy" title="Automate files">

Read a folder of files and write a summary

</DmInfoCard>
<DmInfoCard icon="i-mdi-source-pull" icon-tone="navy" title="Work with Git">

Clone, commit on a branch, push and pull from Azure DevOps

</DmInfoCard>
</v-clicks>
</div>

<!--
These are the six things you should be able to do at the end of the day. We come back to this slide in the wrap-up and tick them off. Day 2 builds on this with data analysis, and day 3 covers CI/CD, code quality and agentic AI. Today is the foundation for both.
-->

---
layout: agenda
label: Agenda
---

# Agenda

1. 09:00 Setup check
2. 09:30 Python on your laptop, scripts and notebooks
3. 10:15 Language fundamentals, lunch at 12:30
4. 13:15 Files, the standard library and exceptions
5. 14:20 Projects with uv
6. 15:05 Version control and Git
7. 16:50 Wrap-up

<style>
li { padding-top: 5px !important; padding-bottom: 5px !important; }
</style>

<!--
This is the plan, not a contract. There are two 15 minute breaks, one around 11:00 inside the fundamentals block and one at about 14:50 after uv, and we move them when an exercise is in full flow. Lunch is at 12:30 and we restart at 13:15. Git gets the last stretch of the day because by then you are comfortable with files, folders and the terminal.
-->

---
layout: default
label: Welcome
---

# Four commands prove your laptop is <span class="dm-accent">ready</span>

<div class="split">

```powershell
uv --version
uv python list --only-installed
code --version
git --version
```

<div class="grid-2">
  <DmIconBadge icon="i-mdi-lightning-bolt" label="uv" sub="Python and packages" />
  <DmIconBadge icon="i-mdi-language-python" tone="dark" label="Python 3.13" sub="installed by uv" />
  <DmIconBadge icon="i-mdi-microsoft-visual-studio-code" tone="dark" label="VS Code" sub="the editor" />
  <DmIconBadge icon="i-mdi-git" label="Git" sub="version control" />
</div>

</div>

<DmBanner class="mt-4" icon="i-mdi-lifebuoy" title="Something fails?">
Do not debug alone. Wave at me: setup problems are normal on managed laptops.
</DmBanner>

<style>
.slidev-code { font-size: 17px !important; line-height: 1.5 !important; }
.split :deep(.dm-badge-circle) { width: 64px; height: 64px; }
.split :deep(.dm-badge-icon) { width: 30px; height: 30px; }
.split :deep(.dm-badge) { gap: 6px; }
</style>

<!--
Use these 30 minutes to get every laptop to the same state: uv installed, Python 3.13 available through uv, VS Code starting, Git available. The commands on the slide are the quick check. Managed laptops sometimes block downloads or need a proxy setting, and that is exactly what I am here to solve. Nobody should start the content blocks with a broken setup.
-->
