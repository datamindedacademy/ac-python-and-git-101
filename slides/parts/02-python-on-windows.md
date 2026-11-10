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
Get-Command shows which program a name resolves to. On many Windows machines, python.exe in WindowsApps is only a stub that points to the Microsoft Store. That is why a plain python command can behave strangely. PATH is the list of folders Windows searches, top to bottom, when you type a command; you can print it with $env:Path -split ';'. This is the main reason we run Python through uv: the command uv python install 3.13 puts a real interpreter in your user profile without admin rights, and uv run finds it so you stop depending on PATH luck.
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
