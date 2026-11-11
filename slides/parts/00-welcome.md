---
layout: default
label: Welcome
---

# Welcome to <span class="dm-accent">Day 1</span>

<DmColumns class="mt-6">
<DmColumn header="Your trainers" tone="navy">

- **Jan Vanbuel**, Dataminded
- **Oliver Willekens**, Dataminded, assisting in the room

</DmColumn>
<DmColumn header="Today" tone="violet">

- Development environment
- Programming fundamentals
- Version control with Git

</DmColumn>
<DmColumn header="Ground rules" tone="plain">

- Ask early, ask often
- Stuck for 5 minutes? Wave at us
- No programming experience assumed

</DmColumn>
</DmColumns>

<!--
Introduce yourselves briefly and ask who has used MATLAB, who has used Excel macros or VBA, and who has never programmed. That tells you how much to lean on the MATLAB analogies. Say clearly that Day 1 assumes no programming experience and that nobody is behind. Oliver walks around during the exercises.
-->

---
layout: default
label: Welcome
---

# Why learn this if <span class="dm-accent">AI</span> can write the code?

<DmColumns class="mt-6">
<DmColumn header="Ask" tone="navy">

You have to ask in the specialist's **vocabulary**

</DmColumn>
<DmColumn header="Judge" tone="violet">

You have to read what comes back and decide if it is **right**

</DmColumn>
<DmColumn header="Choose" tone="navy">

There are several approaches, and someone must own the **tradeoff**

</DmColumn>
</DmColumns>

<!--
An assistant like Copilot can write a working script in seconds, so why spend a day on fundamentals? Because the quality of what you get depends on what you ask. "Loop over the CSV files in this folder and return a dict per run" gets a far better answer than "make it work for all my files". Then you have to read the result and judge it: is it correct, does it handle the empty file, is it the simple version or the clever one? And there is nearly always more than one way, each with a cost, and the tool will pick one silently unless you say what you want. Today gives you the words and the tradeoffs. That is the part that stays yours.
-->

---
layout: default
label: Welcome
---

# Copilot today: <span class="dm-accent">how to use it</span>

<div class="rules">

- Use it freely, in every exercise
- Ask it to explain errors and unfamiliar code
- Ask for a second approach, then compare the two
- Keep only lines you can explain to your neighbour
- You are the author of what you commit, Copilot is not

</div>

<style>
.rules li { margin-bottom: 10px; font-size: 1.05em; }
</style>

<!--
GitHub Copilot is allowed all day, starting now. The most valuable uses for a beginner are asking it to explain an error message or a piece of code, and asking for a second way to do the same thing so you can compare. The one habit we insist on: if you cannot explain a line to the person next to you, ask Copilot to explain it or replace it with something you understand. Your name is on the commit, so the responsibility is yours. One more habit, from Oliver's Clean Code workshop: keep it simple. The simplest version that works is the one to keep, and assistants tend to over-build, so ask for less. Some of you may not have an activated licence yet: pair up with a neighbour who has one, the exercises all work without it too. Day 3 goes deeper into agents, skills and reviewing AI-written code.
-->

---
layout: default
label: Welcome
---

# Judging code: <span class="dm-accent">three questions</span>, in this order

<DmSteps class="mt-4">
<DmStep n="1" label="Correct">Does it do what it is supposed to do?</DmStep>
<DmStep n="2" label="Readable">Will a colleague, or you in two months, understand it?</DmStep>
<DmStep n="3" label="Performant">Is it fast enough? Ask this last.</DmStep>
</DmSteps>

<!--
From Oliver's Clean Code workshop. This is the checklist for the Judge step, and the order matters. First check that the code is correct: run it, try an odd input, compare with a value you know. Then check that it is readable, because code is read far more often than it is written. Performance comes last, because correct and readable code can be made fast, while the reverse is much harder. Use these three questions on everything Copilot hands back today.
-->

---
layout: default
label: Welcome
---

# What you can do <span class="dm-accent">by 17:00</span>

<div class="goals">

<v-clicks>

- Set up a Python environment and run a script from PowerShell
- Create a virtual environment per project and install packages with uv
- Write a script with functions, conditionals and loops, import a package into it, and run it from VS Code
- Read a stack trace and find the error it points to
- Automate a repetitive task with a script that reads and writes files
- Clone an Azure DevOps repository, commit on a branch, push and pull

</v-clicks>

</div>

<style>
.goals li { margin-bottom: 10px; font-size: 1.05em; }
</style>

<!--
These are the six things you should be able to do at the end of the day. We come back to this slide in the wrap-up and tick them off. Day 2 builds on this with data analysis, and day 3 covers CI/CD, code quality and agentic AI. Today is the foundation for both.
-->

---
layout: agenda
label: Agenda
---

# Agenda

1. 09:00 Setup check
2. 09:30 Scripts, notebooks and running Python
3. 10:15 Language fundamentals, lunch at 12:30
4. 13:15 Standard library, files and exceptions
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

# Setup check: <span class="dm-accent">30 minutes</span>

```powershell
uv --version
uv python list --only-installed
code --version
git --version
```

<DmBanner class="mt-6" icon="mdi:lifebuoy" title="Something fails?">
Do not debug alone. Call a trainer, setup problems are normal on managed laptops.
</DmBanner>

<style>
.slidev-code { font-size: 17px !important; line-height: 1.5 !important; }
</style>

<!--
Use these 30 minutes to get every laptop to the same state: uv installed, Python 3.13 available through uv, VS Code starting, Git available. The commands on the slide are the quick check. Managed laptops sometimes block downloads or need a proxy setting, and that is exactly what we are here to solve. Nobody should start the content blocks with a broken setup.
-->
