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

# Today: from a <span class="dm-accent">first script</span> to a pull request

<div class="day">
<div class="lane"><span class="lane-title">Morning · Python</span><div class="stops">
<div class="stop "><span class="time">09:00</span><div class="ico"><div class="i-mdi-laptop" /></div><b>Setup check</b><span class="txt">Tools answer, repository cloned</span></div>
<div class="stop "><span class="time">09:30</span><div class="ico"><div class="i-mdi-console" /></div><b>Run a script</b><span class="txt">Python, uv, script or notebook</span></div>
<div class="stop "><span class="time">10:15</span><div class="ico"><div class="i-mdi-code-braces" /></div><b>The language</b><span class="txt">Variables, collections, loops, functions, tests</span></div>
<div class="stop rest"><span class="time">12:30</span><div class="ico"><div class="i-mdi-silverware-fork-knife" /></div><b>Lunch</b><span class="txt">Back at 13:15</span></div>
</div></div>
<div class="lane"><span class="lane-title">Afternoon · Files, projects and Git</span><div class="stops">
<div class="stop navy"><span class="time">13:15</span><div class="ico"><div class="i-mdi-file-document-multiple-outline" /></div><b>Files and errors</b><span class="txt">Read a folder of logs, survive bad rows</span></div>
<div class="stop navy"><span class="time">14:20</span><div class="ico"><div class="i-mdi-package-variant-closed" /></div><b>Projects with uv</b><span class="txt">Packages, lock file, one-file scripts</span></div>
<div class="stop navy"><span class="time">15:05</span><div class="ico"><div class="i-mdi-source-branch" /></div><b>Git</b><span class="txt">Commit, branch, merge, rebase, pull request</span></div>
<div class="stop rest"><span class="time">16:50</span><div class="ico"><div class="i-mdi-flag-checkered" /></div><b>Wrap-up</b><span class="txt">Done at 17:00</span></div>
</div></div>
</div>

<div class="how">
<span><div class="i-mdi-presentation" /> Short theory</span>
<span class="arrow">→</span>
<span><div class="i-mdi-keyboard-outline" /> Exercise: 2 or 3 tasks, the last one is hard</span>
<span class="arrow">→</span>
<span><div class="i-mdi-help-circle-outline" /> Questions</span>
</div>

<style>
.day { display: flex; flex-direction: column; gap: 14px; margin-top: 6px; }
.lane-title { font-size: 13px; font-weight: 600; letter-spacing: 0.04em; text-transform: uppercase; color: var(--dm-connecting); }
.stops { display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; margin-top: 6px; position: relative; }
.stops::before { content: ""; position: absolute; left: 20px; right: 20px; top: 39px; height: 3px; background: var(--dm-connecting); opacity: 0.35; }
.stop { position: relative; display: flex; flex-direction: column; align-items: flex-start; gap: 2px; }
.stop .time { font-family: monospace; font-size: 12px; color: var(--dm-premium); opacity: 0.75; }
.stop .ico { width: 40px; height: 40px; border-radius: 50%; background: var(--dm-connecting); color: #fff; display: flex; align-items: center; justify-content: center; font-size: 22px; margin: 2px 0 4px; }
.stop.navy .ico { background: var(--dm-premium); }
.stop.rest .ico { background: #fff; color: var(--dm-connecting); border: 2px solid var(--dm-connecting); }
.stop b { font-size: 17px; color: var(--dm-premium); }
.stop .txt { font-size: 13.5px; line-height: 1.35; color: var(--dm-premium); opacity: 0.85; }
.how { display: flex; align-items: center; gap: 14px; margin-top: 18px; padding: 10px 16px; background: var(--dm-surface); border-radius: 8px; font-size: 15px; color: var(--dm-premium); }
.how span { display: inline-flex; align-items: center; gap: 6px; }
.how .arrow { color: var(--dm-connecting); font-weight: 700; }
.how div { font-size: 19px; color: var(--dm-connecting); }
</style>

<!--
This is the day in one picture. The morning is Python: we check every laptop, run a first script, and then work through the language itself, which is the biggest block. After lunch we read and write files, handle errors, and set up a project with uv. The last stretch is Git: commits, branches, and a pull request on a shared repository. Every block has the same rhythm: a short piece of theory, then an exercise with two or three tasks, then room for questions. The last task of each exercise is hard on purpose. Most of you will not finish it in class, and nothing later depends on it. This is the plan, not a contract. There are two 15 minute breaks, one around 11:00 and one at about 14:50, and we move them when an exercise is in full flow.
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
