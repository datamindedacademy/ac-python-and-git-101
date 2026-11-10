---
layout: section
---

# Files and <span class="dm-accent">exceptions</span>

<!--
Scripts that automate work read files and write files, and things will go wrong. Here we learn to do both, and to read an error message without panic.
-->

---
layout: default
label: 5 · Files and exceptions
---

# Reading a text file

```python {all|1-2|4-5|7|all}
from pathlib import Path

with open("data/run_014.csv", encoding="utf-8") as f:
    for line in f:
        print(line.strip())

text = Path("data/run_014.csv").read_text(encoding="utf-8")
```

<v-click>

```text
t_s,pressure_bar,temperature_c
0,6.8,71.2
10,7.1,74.5
20,7.5,78.9
```

</v-click>

<style>
.slidev-code { font-size: 17px !important; line-height: 1.5 !important; }
</style>

<!--
open with the with keyword guarantees the file is closed when the block ends, even if an error happens in between. Looping over the file gives one line at a time, each still carrying its newline character, so strip removes it. For small files Path.read_text reads everything in one go. Always state the encoding, utf-8 is the safe choice.
-->

---
layout: default
label: 5 · Files and exceptions
---

# Writing and appending

```python {all|1-2|3-5|7-8|all}
lines = ["run,max_pressure_bar", "TB-014,7.9"]
with open("summary.txt", "w", encoding="utf-8") as f:
    for line in lines:
        f.write(line + "\n")

with open("summary.txt", "a", encoding="utf-8") as f:
    f.write("TB-015,8.2\n")
```

<DmBanner class="mt-2" tone="violet" icon="mdi:alert-outline">
Mode <code>"w"</code> replaces an existing file without asking. <code>"a"</code> adds at the end, <code>"r"</code> only reads.
</DmBanner>

<style>
.slidev-code { font-size: 17px !important; line-height: 1.5 !important; }
</style>

<!--
Three modes cover nearly everything: r to read, w to write from scratch, a to append. The dangerous one is w, because it silently wipes a file with that name. write does not add a newline, you add it yourself. When your script produces output, write to a new file rather than over your raw data.
-->

---
layout: default
label: 5 · Files and exceptions
---

# A <span class="dm-accent">traceback</span> is a map to the error

```text {all|1|2-3|4|all}
Traceback (most recent call last):
  File "convert.py", line 2, in <module>
    pressure_bar = float(text)
ValueError: could not convert string to float: 'seven'
```

<v-clicks>

- Line 1 is only a header, it says: read on
- The middle shows the file, the line number and the code that failed
- The last line names the error type and what went wrong. Read it first.

</v-clicks>

<style>
.slidev-code { font-size: 17px !important; line-height: 1.5 !important; }
</style>

<!--
When Python fails it prints a traceback. It looks scary and it is the most useful thing it gives you. Start at the bottom: the error type, here ValueError, and the message, which says what could not be converted. Then look one line up: file, line number and the exact code. That is usually all you need to find the problem.
-->

---
layout: default
label: 5 · Files and exceptions
---

# Tracebacks through <span class="dm-accent">several functions</span>

```text {all|7|5-6|2-3|all}
Traceback (most recent call last):
  File "analyse.py", line 5, in <module>
    print(mean(readings))
          ~~~~^^^^^^^^^^
  File "analyse.py", line 2, in mean
    return sum(values) / len(values)
           ~~~~~~~~~~~~^~~~~~~~~~~~~
ZeroDivisionError: division by zero
```

<v-click>

<p class="mt-2">Read bottom up: what failed, where it failed, then who called it.</p>

</v-click>

<style>
.slidev-code { font-size: 17px !important; line-height: 1.5 !important; }
</style>

<!--
When a function calls a function, the traceback lists every step, the oldest call on top and the place of the failure at the bottom. The tildes and carets point at the part of the line that failed. Here the empty list made len return zero. The fix may be in the calling code, not in the function, so follow the chain upward and decide which line is really wrong.
-->

---
layout: default
label: 5 · Files and exceptions
---

# Errors you will <span class="dm-accent">meet</span>

<DmComparison
  class="err mt-2"
  :rows="['FileNotFoundError', 'ValueError', 'TypeError', 'KeyError', 'IndexError', 'NameError']"
  :cols="['Typical cause']"
>
  <template #r0c0>Wrong path or wrong working folder</template>
  <template #r1c0>Right type, unusable value: <code>float("seven")</code></template>
  <template #r2c0>Mixing types: <code>"a" + 1</code></template>
  <template #r3c0>Dictionary key that does not exist, often a typo</template>
  <template #r4c0>List position beyond the end, often an off-by-one</template>
  <template #r5c0>Misspelled name, or used before it was created</template>
</DmComparison>

<style>
.err :deep(.dm-cmp-rowlabel) { font-size: 12px; padding: 4px; }
.err :deep(.dm-cmp-cell) { padding-top: 6px; padding-bottom: 6px; }
</style>

<!--
Six names cover most of what you meet in the first months. The name of the error already tells you which kind of mistake to look for. For example KeyError with a column name means a typo in that name or a changed header in the CSV. In exercise 07 you debug scripts that each contain a different one of these.
-->

---
layout: default
label: 5 · Files and exceptions
---

# Handling errors with <span class="dm-accent">try / except</span>

```python {all|2-3|4-6|all}
text = "seven"
try:
    pressure_bar = float(text)
except ValueError:
    pressure_bar = None
    print(f"Skipping bad value: {text!r}")
print(pressure_bar)
```

<v-click>

```text
Skipping bad value: 'seven'
None
```

</v-click>

<style>
.slidev-code { font-size: 17px !important; line-height: 1.5 !important; }
</style>

<!--
Sometimes an error is expected, for example one bad row in a long log. try runs the risky code, and if the named exception occurs, the except block runs instead of crashing the script. The script then carries on. Execution continues after the whole block either way.
-->

---
layout: default
label: 5 · Files and exceptions
---

# Catch <span class="dm-accent">specific</span> errors and raise your own

<DmColumns class="mt-2">
<DmColumn header="Do" tone="violet">

```python
try:
    text = path.read_text()
except FileNotFoundError:
    print(f"Missing: {path}")
```

</DmColumn>
<DmColumn header="Don't" tone="plain">

```python
try:
    text = path.read_text()
except:
    pass
```

</DmColumn>
</DmColumns>

```python
if not values:
    raise ValueError("mean() needs at least one value")
```

<style>
.slidev-code { font-size: 17px !important; line-height: 1.5 !important; }
</style>

<!--
Catch the one error you expect and say something useful. A bare except with pass swallows every problem, including your own typos, and the script appears to work while producing nothing. You can also raise an error yourself when your function receives something it cannot handle: fail early with a clear message, that is kinder than a ZeroDivisionError three lines later.
-->

---
layout: statement
---

# Exercise 07: <span class="dm-accent">Files and exceptions</span>

`exercises/python/07-files-and-exceptions`

<!--
Read and write files, handle a bad row, and then fix several broken scripts by reading their tracebacks. Start each time at the bottom line. About 30 minutes.
-->
