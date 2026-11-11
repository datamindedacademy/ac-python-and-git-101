---
layout: section
---

# Python on <span class="dm-accent">your laptop</span>

<!--
We start with the practical part: making sure Python runs on your managed Windows laptop, and running a script from PowerShell. Then we look at the two forms your code can take, scripts and notebooks, and do the first exercise.
-->

---
layout: default
label: 1 · Python on your laptop
---

# <span class="dm-accent">Python</span> is open source and runs on CPython

<div class="grid-3">
  <DmIconBadge icon="i-mdi-calendar-star" label="1991" sub="by Guido van Rossum, named after Monty Python" />
  <DmIconBadge icon="i-mdi-account-group-outline" label="Open source" sub="steered by the PSF" />
  <DmIconBadge icon="i-mdi-language-c" tone="dark" label="CPython 3.13" sub="the interpreter, written in C" />
</div>

<DmProcess class="mt-8">
<DmPhase label="Your .py file" />
<DmPhase label="Compiled to bytecode" />
<DmPhase label="CPython runs it" />
</DmProcess>

<!--
A minute of background. Python is more than thirty years old and is developed in the open, with no single vendor behind it. If you come from MATLAB you know one vendor and one runtime. Here the language is a specification, and CPython is the implementation almost everyone uses: a program written in C that reads your text file, compiles it to bytecode and executes it. That is why uv python install downloads CPython. Other implementations exist, PyPy is one, but you will rarely meet them. We use Python 3.13 in this training.
-->

---
layout: default
label: 1 · Python on your laptop
---

# Check <span class="dm-accent">which Python</span> a command really runs

```powershell
Get-Command python
```

```text
CommandType  Name        Source
-----------  ----        ------
Application  python.exe  C:\Users\you\AppData\Local\Microsoft\WindowsApps\python.exe
```

<v-click>

<DmBanner class="mt-4" tone="violet" icon="i-mdi-alert-outline" title="Watch out">
A <code>WindowsApps</code> path is the Microsoft Store shortcut, not a real Python. It opens the Store or does nothing useful.
</DmBanner>

</v-click>

<style>
.slidev-code { font-size: 17px !important; line-height: 1.5 !important; }
</style>

<!--
Get-Command shows which program a name resolves to. On many Windows machines, python.exe in WindowsApps is only a stub that points to the Microsoft Store. That is why a plain python command can behave strangely. PATH is the list of folders Windows searches, top to bottom, when you type a command; you can print it with $env:Path -split ';'. This is the main reason we run Python through uv: the command uv python install 3.13 puts a real interpreter in your user profile without admin rights, and uv run finds it so you stop depending on PATH luck.
-->

---
layout: default
label: 1 · Python on your laptop
---

# Go to the folder, then <span class="dm-accent">uv run</span> the script

```python
# hello.py
print("Compressor test bench online")
```

```powershell
cd C:\Users\you\training
uv run python hello.py
```

```text
Compressor test bench online
```

<style>
.slidev-code { font-size: 17px !important; line-height: 1.5 !important; }
</style>

<!--
Two steps: move to the folder that contains the file, then tell uv to run Python on it. The most common mistake is running the command from the wrong folder, which gives the error "can't open file". Use Get-Location to see where you are and dir to list the files. uv run takes care of finding the right interpreter.
-->

---
layout: default
label: 1 · Python on your laptop
---

# <span class="dm-accent">VS Code</span> runs the same script in three steps

<DmSteps class="mt-4">
<DmStep n="1" label="Open the folder">File, Open Folder, choose your project folder</DmStep>
<DmStep n="2" label="Select the interpreter">Command Palette, Python: Select Interpreter, pick the one in <code>.venv</code> or the uv Python 3.13</DmStep>
<DmStep n="3" label="Run">Play button at the top right, or <code>uv run python hello.py</code> in the integrated terminal</DmStep>
</DmSteps>

<!--
Open the folder, not just a single file, so VS Code knows the project. The integrated terminal, Ctrl+backtick, is the same PowerShell you used before and starts in the project folder. Both ways of running do the same thing, the play button is just a shortcut. If the interpreter is wrong, a yellow warning shows in the bottom bar.
-->

