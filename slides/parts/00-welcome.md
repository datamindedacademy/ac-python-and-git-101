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

Clone, commit on a branch, push and pull from GitHub

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
