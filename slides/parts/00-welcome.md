---
layout: intro
role: Platform engineer and Dataminded Academy lead
photo: /jan-vanbuel.jpg
---

# Jan <span class="dm-accent">Vanbuel</span>

<p class="mt-4">Your trainer today. I like Rust, playing the saxophone and triathlon.</p>

<!--
Introduce yourself briefly, then ask the room three questions with a show of hands: who has used MATLAB, who has written Excel macros or VBA, and who has written a little Python. That tells you how much to lean on the MATLAB analogies. Say clearly that Day 1 assumes some scripting experience and focuses on what is specific to Python. You are the only trainer today, so ask people to help their neighbour first while you walk around during the exercises.
-->

---
layout: default
label: Welcome
---

# Three days: <span class="dm-accent">write</span> it, <span class="dm-accent">analyse</span> with it, <span class="dm-accent">trust</span> it

<div class="days">
<div class="dcard d1"><div class="top"><div class="ico"><div class="i-mdi-code-braces" /></div><span class="num">Day 1</span><span class="today">today</span></div><b>Python and Git 101</b><span class="sub">Write a script and share it</span><ul><li>Python on your laptop, uv</li><li>The language, files, errors</li><li>Git: commit, branch, pull request</li></ul></div>
<div class="conn">→</div>
<div class="dcard d2"><div class="top"><div class="ico"><div class="i-mdi-chart-line" /></div><span class="num">Day 2</span></div><b>Data analysis</b><span class="sub">Turn measurements into answers</span><ul><li>pandas and NumPy</li><li>SciPy and scikit-learn</li><li>Plots with Matplotlib</li></ul></div>
<div class="conn">→</div>
<div class="dcard d3"><div class="top"><div class="ico"><div class="i-mdi-shield-check-outline" /></div><span class="num">Day 3</span></div><b>Code you can trust</b><span class="sub">Quality, automation and agents</span><ul><li>Tests, linting, type checking</li><li>Pipelines on Azure DevOps</li><li>Coding agents, and reviewing their work</li></ul></div>
</div>

<p class="bring"><b>Bring your own work.</b> A use case, an example or a question from your job is welcome in every session.</p>

<style>
.days { display: grid; grid-template-columns: 1fr 26px 1fr 26px 1fr; align-items: stretch; margin-top: 10px; }
.conn { display: flex; align-items: center; justify-content: center; font-size: 24px; font-weight: 700; color: var(--dm-connecting); }
.dcard { display: flex; flex-direction: column; gap: 4px; padding: 18px 18px 14px; border-radius: 12px; background: var(--dm-surface); border-top: 5px solid var(--dm-premium); }
.dcard.d1 { border-top-color: var(--dm-connecting); box-shadow: 0 0 0 2px var(--dm-connecting); }
.dcard .top { display: flex; align-items: center; gap: 10px; margin-bottom: 6px; }
.dcard .ico { width: 44px; height: 44px; border-radius: 10px; background: var(--dm-premium); color: #fff; display: flex; align-items: center; justify-content: center; font-size: 26px; }
.dcard.d1 .ico { background: var(--dm-connecting); }
.dcard .num { font-size: 14px; font-weight: 600; letter-spacing: 0.05em; text-transform: uppercase; color: var(--dm-premium); }
.dcard .today { margin-left: auto; font-size: 12px; font-weight: 600; color: #fff; background: var(--dm-connecting); border-radius: 999px; padding: 2px 10px; }
.dcard b { font-size: 20px; color: var(--dm-premium); }
.dcard .sub { font-size: 14.5px; color: var(--dm-premium); opacity: 0.8; }
.dcard ul { margin: 8px 0 0; padding-left: 18px; }
.dcard li { font-size: 14.5px; line-height: 1.45; margin: 3px 0; }
.bring { margin-top: 16px; padding: 10px 16px; border-left: 4px solid var(--dm-connecting); background: var(--dm-authentic); border-radius: 0 8px 8px 0; font-size: 15.5px; color: var(--dm-premium); }
</style>

<!--
This is the whole training in one picture. Today you learn to write a Python script and to share it with Git. Day 2 uses that for data analysis: tables with pandas, numbers with NumPy and SciPy, plots with Matplotlib, and a first model with scikit-learn. Day 3 is about code you can trust: tests, linting and type checking, pipelines on Azure DevOps, and coding agents and how to review what they write. Each day builds on the one before, so today is the foundation. Invite everyone to bring something from their own work to the next sessions: a script they want to write, a data file they struggle with, an error they could not solve, or just a question. Real cases make days 2 and 3 better. For today: setup check at 09:00, Python until lunch at 12:30, restart at 13:15 with files, errors and uv, Git from about 15:05, wrap-up at 16:50. There are two 15 minute breaks, around 11:00 and around 14:50, and we move them when an exercise is in full flow.
-->

---
layout: default
label: Welcome
---

# AI is a <span class="dm-accent">multiplier</span> of experience

<div class="eq">
  <span class="term">your experience</span><span class="op">×</span><span class="term ai">AI</span><span class="op">=</span><span class="term">what you get</span>
</div>

<p class="zero">Zero experience gives AI nothing to multiply.</p>

<div class="grid-3 mt-2">
<DmInfoCard icon="i-mdi-translate" title="Speak the language">

Know the words a specialist uses, so you can ask for exactly that

</DmInfoCard>
<DmInfoCard icon="i-mdi-scale-balance" icon-tone="navy" title="Understand the tradeoffs">

There are several ways to do it, each with a cost. You choose

</DmInfoCard>
<DmInfoCard icon="i-mdi-target" title="Ask specific questions">

A precise request gets code you can read and check

</DmInfoCard>
</div>

<style>
.eq { display: flex; align-items: center; justify-content: center; gap: 18px; margin-top: 8px; font-size: 26px; font-weight: 600; color: var(--dm-premium); }
.eq .term { padding: 8px 20px; border-radius: 10px; background: var(--dm-surface); }
.eq .ai { background: var(--dm-connecting); color: #fff; }
.eq .op { font-size: 30px; color: var(--dm-connecting); }
.zero { text-align: center; font-size: 19px; margin: 12px 0 6px; color: var(--dm-premium); }
</style>

<!--
This is how we see AI at Dataminded, and it is why this day exists. AI multiplies the experience you bring. With a lot of experience you get a lot back. With zero experience there is nothing to multiply: you get code you cannot read, cannot check and cannot fix. So today is not about typing code faster than an assistant. It builds the three things the assistant cannot bring for you. First the language: the words a Python or Git specialist uses, so your request says exactly what you want. Second the tradeoffs: script or notebook, list or dict, skip a bad row or stop, merge or rebase. The assistant picks one silently unless you say which. Third specific questions: the next slide shows what that looks like. Copilot is allowed all day, starting now. Use it to explain an error or a line you do not understand, and to show a second way so you can compare. Keep only lines you understand, your name is on the commit. Judge what comes back in this order: is it correct, is it readable, and only then is it fast enough. Assistants tend to over-build, so ask for less. If your licence is not active yet, pair up with someone who has one. The exercises all work without it. Day 3 goes deeper into agents and reviewing AI-written code.
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
This is what a specific question looks like: what a specialist asks for. Every term in it is taught today: csv.DictReader, float conversion, ValueError and skipping bad rows, list comprehension, the standard library, pytest and pytest.approx, type hints and Path. Do not explain anything now. The same slide comes back in the wrap-up.
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

Clone, commit on a branch, push and pull from a remote

</DmInfoCard>
</v-clicks>
</div>

<!--
These are the six things you should be able to do at the end of the day. We come back to this slide in the wrap-up and tick them off. Day 2 builds on this with data analysis, and day 3 covers CI/CD, code quality and agentic AI. Today is the foundation for both.
-->

---
layout: default
label: Welcome
---

# Check the tools, then <span class="dm-accent">clone the repository</span>

<div class="setup">
<div>
<p class="step">1 · The tools answer</p>

```powershell
uv --version
uv python list --only-installed
code --version
git --version
```

</div>
<div>
<p class="step">2 · The course material is on your laptop</p>

```powershell
cd $HOME\Documents
git clone https://github.com/datamindedacademy/ac-python-and-git-101
cd ac-python-and-git-101
uv sync
code .
```

</div>
</div>

<DmBanner class="mt-4" icon="i-mdi-lifebuoy" title="Something fails?">
Do not debug alone. Call me over: setup problems are normal on managed laptops.
</DmBanner>

<style>
.slidev-code { font-size: 13px !important; line-height: 1.6 !important; }
.setup { display: grid; grid-template-columns: 270px 1fr; gap: 24px; margin-top: 8px; }
.setup > * { min-width: 0; }
.step { font-weight: 600; font-size: 15px; color: var(--dm-connecting); margin: 0 0 6px; }
</style>

<!--
Use these 30 minutes to get every laptop to the same state. First the four tools: uv installed, Python 3.13 available through uv, VS Code starting, Git available. Then the course repository: clone it into Documents, run uv sync, and open the folder in VS Code. git clone copies the repository from the server, and we come back to it this afternoon. uv sync creates the folder .venv with the Python and the packages the exercises need. Every exercise today runs from this folder. Managed laptops sometimes block downloads or need a proxy setting, and that is exactly what I am here to solve. Nobody should start the content blocks with a broken setup.
-->
