---
layout: section
---

# Python on <span class="dm-accent">your laptop</span>

<!--
Now the practical part: making sure Python runs on your managed Windows laptop, and running a script from PowerShell.
-->

---
layout: default
label: 2 · Python on your laptop
---

# The <span class="dm-accent">interpreter</span> runs your file

<DmProcess class="mt-8">
<DmPhase label="hello.py" />
<DmPhase label="python.exe" />
<DmPhase label="Output" />
</DmProcess>

<p class="mt-8">Python is a program. Your <code>.py</code> file is just text it reads and executes.</p>

<!--
There is no compile step you need to manage. The interpreter, python.exe on Windows, reads your text file and runs it. If the interpreter is not found, or the wrong one is found, nothing runs. Most first-day problems are about which python.exe your terminal starts.
-->

---
layout: default
label: 2 · Python on your laptop
---

# Installing Python on a managed laptop with <span class="dm-accent">uv</span>

```powershell
uv python install 3.13
uv python list --only-installed
```

<v-clicks>

- No administrator rights needed: uv installs Python in your user profile
- Several Python versions can live side by side
- Each project chooses its version, uv picks the right one

</v-clicks>

<style>
.slidev-code { font-size: 17px !important; line-height: 1.5 !important; }
</style>

<!--
On a managed laptop you often cannot run a classic installer. uv downloads a Python build and keeps it in your own profile, so no admin rights are involved. You may already have done this in the setup manual, in which case the install command just confirms it. We use Python 3.13 throughout the training.
-->

---
layout: default
label: 2 · Python on your laptop
---

# What is the <span class="dm-accent">PATH</span>?

```powershell
$env:Path -split ';'
```

```text
C:\Users\you\.local\bin
C:\Windows\system32
C:\Windows
C:\Program Files\Git\cmd
...
```

<v-click>

Type a command, and Windows searches these folders, top to bottom, for a matching program.

</v-click>

<style>
.slidev-code { font-size: 17px !important; line-height: 1.5 !important; }
</style>

<!--
PATH is a list of folders. When you type uv or python in PowerShell, Windows looks through the folders in this list in order and runs the first match. Every person's list looks slightly different. The split command on the slide just prints the single long string one folder per line. If you know MATLAB, this is the same idea as the MATLAB search path for functions.
-->

---
layout: default
label: 2 · Python on your laptop
---

# Which Python am I <span class="dm-accent">running</span>?

```powershell
Get-Command python
```

```text
CommandType  Name        Source
-----------  ----        ------
Application  python.exe  C:\Users\you\AppData\Local\Microsoft\WindowsApps\python.exe
```

<v-click>

<DmBanner class="mt-4" tone="violet" icon="mdi:alert-outline" title="Watch out">
A <code>WindowsApps</code> path is the Microsoft Store shortcut, not a real Python. It opens the Store or does nothing useful.
</DmBanner>

</v-click>

<style>
.slidev-code { font-size: 17px !important; line-height: 1.5 !important; }
</style>

<!--
Get-Command shows which program a name resolves to. On many Windows machines, python.exe in WindowsApps is only a stub that points to the Microsoft Store. That is why a plain python command can behave strangely. This is the main reason we run Python through uv in this training: uv finds the correct interpreter for the project and you stop depending on PATH luck.
-->

---
layout: default
label: 2 · Python on your laptop
---

# Run a script from <span class="dm-accent">PowerShell</span>

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
label: 2 · Python on your laptop
---

# Try ideas in the <span class="dm-accent">REPL</span>

```powershell
uv run python
```

```python
>>> 7.5 * 14.5038
108.7785
>>> pressures = [6.8, 7.1, 7.5]
>>> max(pressures)
7.5
>>> exit()
```

<style>
.slidev-code { font-size: 17px !important; line-height: 1.5 !important; }
</style>

<!--
Without a file name, Python starts an interactive prompt. Every line runs immediately, which is perfect for testing a small idea, similar to the MATLAB command window. Nothing you type there is saved. Leave with exit() or Ctrl+Z followed by Enter on Windows.
-->

---
layout: default
label: 2 · Python on your laptop
---

# Running from <span class="dm-accent">VS Code</span>

<DmSteps class="mt-4">
<DmStep n="1" label="Open the folder">File, Open Folder, choose your project folder</DmStep>
<DmStep n="2" label="Select the interpreter">Command Palette, Python: Select Interpreter, pick the one in <code>.venv</code> or the uv Python 3.13</DmStep>
<DmStep n="3" label="Run">Play button at the top right, or <code>uv run python hello.py</code> in the integrated terminal</DmStep>
</DmSteps>

<!--
Open the folder, not just a single file, so VS Code knows the project. The integrated terminal, Ctrl+backtick, is the same PowerShell you used before and starts in the project folder. Both ways of running do the same thing, the play button is just a shortcut. If the interpreter is wrong, a yellow warning shows in the bottom bar.
-->

---
layout: statement
---

# Exercise 01: <span class="dm-accent">First script</span>

`exercises/python/01-first-script`

<!--
Everyone creates a script, runs it from PowerShell and from VS Code, and changes it. About 15 minutes. Oliver and I walk around, and any PATH or interpreter problem is exactly what we want to catch now.
-->
