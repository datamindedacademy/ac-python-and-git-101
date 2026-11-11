---
layout: section
---

# Files and the standard <span class="dm-accent">library</span>

<!--
Scripts that automate work read and write files. Python ships with a large collection of ready-made modules for that. This block covers pathlib, reading and writing files with open, csv and json. You met import with math this morning.
-->

---
layout: default
label: 4 · Files and the standard library
---

# <span class="dm-accent">pathlib</span> builds paths and finds files

```python {all|2-3|5-6|8|all}
from pathlib import Path

data_dir = Path("data")
log_file = data_dir / "run_014.csv"

print(log_file.name, log_file.suffix, log_file.stem)
print(log_file.exists())

for f in sorted(data_dir.glob("*.csv")):
    print(f)
```

<v-click>

```text
run_014.csv .csv run_014
True
data\run_014.csv
data\run_015.csv
```

</v-click>

<style>
.slidev-code { font-size: 15px !important; line-height: 1.5 !important; }
</style>

<!--
Path wraps a file or folder path. This is the second form of import from this morning: from pathlib import Path. The slash operator joins parts correctly with the Windows separator, so you never glue strings together by hand. You get the name, suffix and stem for free, you can test existence, and glob finds all files matching a pattern. The loop over glob is the key pattern for exercises 06 and 07: one script that processes every log in a folder. On Windows the backslash in a normal string starts an escape sequence, so write paths with Path and forward slashes, not by gluing strings.
-->

---
layout: default
label: 4 · Files and the standard library
---

# <span class="dm-accent">with open</span> reads a file and closes it again

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

<p class="note"><code>f</code> is the <b>file handle</b>. State the <b>encoding</b>, or Windows picks its own.</p>

<style>
.slidev-code { font-size: 17px !important; line-height: 1.5 !important; }
</style>

<!--
open with the with keyword guarantees the file is closed when the block ends, even if an error happens in between. The name f is the file handle: your grip on the open file. Looping over the file gives one line at a time, each still carrying its newline character, so strip removes it. For small files Path.read_text reads everything in one go. Always state the encoding, utf-8 is the safe choice.
-->

---
layout: default
label: 4 · Files and the standard library
---

# Mode <span class="dm-accent">w</span> overwrites, mode <span class="dm-accent">a</span> appends

```python {all|1-2|3-5|7-8|all}
lines = ["run,max_pressure_bar", "TB-014,7.9"]
with open("summary.txt", "w", encoding="utf-8") as f:
    for line in lines:
        f.write(line + "\n")

with open("summary.txt", "a", encoding="utf-8") as f:
    f.write("TB-015,8.2\n")
```

<DmBanner class="mt-2" tone="violet" icon="i-mdi-alert-outline">
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
label: 4 · Files and the standard library
---

# <span class="dm-accent">csv</span> turns each row into a dict of strings

```text
t_s,pressure_bar,temperature_c
0,6.8,71.2
10,7.1,74.5
20,7.5,78.9
```

```python {all|2|3|4-5|all}
import csv
with open("data/run_014.csv", newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))
print(rows[0])
print(float(rows[1]["pressure_bar"]) + 1)
```

<v-click>

```text
{'t_s': '0', 'pressure_bar': '6.8', 'temperature_c': '71.2'}
8.1
```

</v-click>

<p class="note">The first row is the <b>header</b>. Its names become the keys of every row.</p>

<p class="ask" v-click><b>Question</b>The log has ten million rows. What does <code>list(...)</code> on line 3 do?</p>

<style>
.slidev-code { font-size: 15px !important; line-height: 1.5 !important; }
</style>

<!--
DictReader turns every row into a dictionary keyed by the header names, so you get exactly the list of dicts from the fundamentals block. The with block opens the file and closes it again, as on the earlier slide. One thing to remember: every value comes back as a string, so convert with float before calculating. Writing rows works the same way with csv.DictWriter, and the exercise shows it. Question on the slide: it reads every row into memory at once, each as a dict of strings, which takes several gigabytes. Without list you can loop over the reader and handle one row at a time.
-->

---
layout: default
label: 4 · Files and the standard library
---

# <span class="dm-accent">json</span> stores settings and nested data

<p class="why"><b>Why</b>CSV holds one flat table. Settings, limits and nested results need a format with names and levels.</p>

```python {all|2|3-4|5-6|all}
import json
config = {"limit_bar": 9.0, "channels": ["pressure", "flow"], "operator": None}
text = json.dumps(config)
print(text)
back = json.loads(text)
print(back["channels"][0], back["operator"])
```

<v-click>

```text
{"limit_bar": 9.0, "channels": ["pressure", "flow"], "operator": null}
pressure None
```

</v-click>

<style>
.slidev-code { font-size: 17px !important; line-height: 1.5 !important; }
</style>

<!--
JSON is the usual format for settings and for data exchanged between programs. Python dicts, lists, strings, numbers and None map directly onto it, with None becoming null. dumps turns Python into text, loads turns text back into Python. Add indent=2 to dumps for a readable layout with line breaks. For files there are json.dump and json.load. Use JSON for nested data and CSV for flat tables.
-->

---
layout: statement
---

# Exercise 06: <span class="dm-accent">Standard library</span>

`exercises/python/06-standard-library`

<p class="words"><b>Words you can now use</b> standard library · path · glob · file handle · encoding · CSV · JSON</p>

<style>
.words { font-size: 15px; opacity: 0.9; margin-top: 14px; }
.words b { margin-right: 8px; }
</style>

<!--
Use math, pathlib, with open, csv and json on a small set of fictional bench logs. The starter keeps its structure, the answers are in the collapsed hints. About 30 minutes.
-->
