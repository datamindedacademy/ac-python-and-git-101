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

# Python fills the gap between <span class="dm-accent">shell scripts and C</span>

<div class="grid-3 mt-2">
<DmInfoCard icon="i-mdi-console" title="Shell scripts">

Quick to write. Painful once you need real logic, numbers or data structures

</DmInfoCard>
<DmInfoCard icon="i-mdi-language-python" icon-tone="navy" title="Python">

Reads like a script, with lists, dicts, functions and a large library built in

</DmInfoCard>
<DmInfoCard icon="i-mdi-language-c" title="C">

Can do everything. Slow to write, and easy to get wrong

</DmInfoCard>
</div>

<div class="guido">
<figure>
<img src="/guido-van-rossum.jpg" alt="Portrait of Guido van Rossum" />
<figcaption>Photo: Daniel Stroud, CC BY-SA 4.0</figcaption>
</figure>
<p class="note">Guido van Rossum started it in 1989 at CWI in Amsterdam, for system administration work that was too much for a shell script and not worth a C program. First release in 1991.</p>
</div>

<style>
.guido { display: grid; grid-template-columns: 230px 1fr; gap: 24px; align-items: center; margin-top: 18px; }
.guido figure { margin: 0; }
.guido img { width: 230px; height: 153px; object-fit: cover; border-radius: 10px; display: block; }
.guido figcaption { font-size: 10px; opacity: 0.6; margin-top: 4px; }
.guido .note { margin-top: 0 !important; }
</style>

<!--
Why does Python exist? Guido van Rossum worked at CWI in Amsterdam on an operating system called Amoeba. The administration tasks were too complex for Unix shell scripts, and writing each of them in C took too long. He wanted something in between: as quick to write as a shell script, with the data structures and error handling of a real language. That is still the reason people pick it today, and it is the same gap you may know between a batch file and a compiled program, or between an Excel macro and a full application. The name comes from Monty Python, not the snake. Python is open source and has no vendor: the Python Software Foundation owns the trademark and the core developers steer the language. If you come from MATLAB, that is the big difference: no licence, no single company.
-->

---
layout: default
label: 1 · Python on your laptop
---

# Python is the language, <span class="dm-accent">CPython</span> runs it

<DmProcess class="mt-2">
<DmPhase label="Your .py file" />
<DmPhase label="Compiled to bytecode" />
<DmPhase label="Run by the virtual machine" />
</DmProcess>

<p class="note">The <b>interpreter</b> is the program that does the last two steps: <code>python.exe</code>.<br/>To view the bytecode of a script: <code>uv run python -m dis &lt;script.py&gt;</code></p>

<DmComparison
  class="mt-4"
  :rows="['What it is', 'When you meet it']"
  :cols="['CPython', 'PyPy', 'MicroPython']"
>
  <template #r0c0>The reference implementation, written in C</template>
  <template #r0c1>Compiles hot loops to machine code while running</template>
  <template #r0c2>A small Python for microcontrollers</template>

  <template #r1c0>Always: it is what uv installs</template>
  <template #r1c1>Long pure-Python calculations</template>
  <template #r1c2>Sensors and embedded boards</template>
</DmComparison>

<!--
Two things carry the name Python, and it helps to keep them apart. The language is a specification: a document that says what a for loop or a list must do. An implementation is a program that follows that specification and runs your code. CPython is the reference implementation, written in C by the core developers, and it is what almost everyone uses and what uv python install downloads. How does it run your file? It first compiles the text to bytecode, a compact list of simple instructions. Then a virtual machine executes those instructions one by one. You can look at the bytecode with the dis module: run it on hello.py and you see instructions such as LOAD_NAME and CALL. Both steps happen inside one program, the interpreter, every time you run a script, which is why there is no separate build step as in C. The virtual machine is also why the same script runs unchanged on Windows and Linux: the bytecode is the same, only the interpreter differs per platform. It is also why plain Python loops are slower than C. Other implementations exist. PyPy adds a just-in-time compiler and can be much faster on long loops. MicroPython fits on a microcontroller. You will rarely need them, but when someone says Python is slow or Python cannot run there, the answer depends on which implementation. We use CPython 3.13 in this training.
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

# Go to the repository, then <span class="dm-accent">uv run</span> the script

```python
# exercises/python/01-first-script/hello.py
print("Hello, test engineer!")
```

```powershell
cd $HOME\Documents\ac-python-and-git-101
uv run python exercises/python/01-first-script/hello.py
```

```text
Hello, test engineer!
```

<style>
.slidev-code { font-size: 17px !important; line-height: 1.5 !important; }
</style>

<!--
Two steps: move to the repository you cloned during the setup check, then tell uv to run Python on a file in it. We always run from the root of the repository and give the path to the script. The script prints two more lines, left out here. The most common mistake is running the command from the wrong folder, which gives the error "can't open file". Use Get-Location to see where you are and dir to list the files. uv run takes care of finding the right interpreter.
-->

---
layout: default
label: 1 · Python on your laptop
---

# <span class="dm-accent">VS Code</span> runs the same script in three steps

<DmSteps class="mt-4">
<DmStep n="1" label="Open the folder">File, Open Folder, choose <code>ac-python-and-git-101</code></DmStep>
<DmStep n="2" label="Select the interpreter">Command Palette, Python: Select Interpreter, pick the one in <code>.venv</code> or the uv Python 3.13</DmStep>
<DmStep n="3" label="Run">Play button at the top right, or the same <code>uv run python</code> command in the integrated terminal</DmStep>
</DmSteps>

<!--
Open the folder, not just a single file, so VS Code knows the project. The integrated terminal, Ctrl+backtick, is the same PowerShell you used before and starts in the project folder. Both ways of running do the same thing, the play button is just a shortcut. If the interpreter is wrong, a yellow warning shows in the bottom bar.
-->

