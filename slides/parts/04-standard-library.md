---
layout: section
---

# The standard <span class="dm-accent">library</span>

<!--
Python ships with a large collection of ready-made modules. This block covers the four that you need for almost any automation job: math, pathlib, csv and json.
-->

---
layout: default
label: 4 · The standard library
---

# <span class="dm-accent">import</span> gives you ready-made tools like math

```python {all|1|3-6|8|all}
import math

diameter_m = 0.05
area_m2 = math.pi * (diameter_m / 2) ** 2
flow_m3_s = 18.4 / 1000
print(round(flow_m3_s / area_m2, 2))

print(math.isclose(0.1 + 0.2, 0.3))
```

<v-click>

```text
9.37
True
```

</v-click>

<style>
.slidev-code { font-size: 17px !important; line-height: 1.5 !important; }
</style>

<!--
import makes a module available, and you reach its contents with a dot. Here we compute the flow velocity in a 50 mm pipe: 18.4 litres per second is 9.37 metres per second. Floats are binary approximations, so 0.1 + 0.2 is not exactly 0.3 and you should never compare floats with equality. math.isclose is the safe way. The standard library is like the toolboxes that come with MATLAB, only free and already installed. Other useful names are math.sqrt, math.log, math.floor and math.ceil.
-->

---
layout: default
label: 4 · The standard library
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
Path wraps a file or folder path. The slash operator joins parts correctly with the Windows separator, so you never glue strings together by hand. You get the name, suffix and stem for free, you can test existence, and glob finds all files matching a pattern. The loop over glob is the key pattern for exercises 06 and 07: one script that processes every log in a folder. On Windows the backslash in a normal string starts an escape sequence, so write paths with Path and forward slashes, not by gluing strings.
-->

---
layout: default
label: 4 · The standard library
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

<style>
.slidev-code { font-size: 15px !important; line-height: 1.5 !important; }
</style>

<!--
DictReader turns every row into a dictionary keyed by the header names, so you get exactly the list of dicts from the fundamentals block. The with block opens the file and closes it again, we look at that properly in the next block. One thing to remember: every value comes back as a string, so convert with float before calculating. Writing rows works the same way with csv.DictWriter, and the exercise shows it.
-->

---
layout: default
label: 4 · The standard library
---

# <span class="dm-accent">json</span> stores settings and nested data

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

<p class="words"><b>Words you can now use</b> standard library · module · import · path · glob · CSV · JSON</p>

<style>
.words { font-size: 15px; opacity: 0.9; margin-top: 14px; }
.words b { margin-right: 8px; }
</style>

<!--
Use math, pathlib, csv and json on a small set of fictional bench logs. About 25 minutes.
-->
