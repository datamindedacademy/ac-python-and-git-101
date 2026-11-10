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

# Batteries included: <span class="dm-accent">import</span> and math

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
import makes a module available, and you reach its contents with a dot. Here we compute the flow velocity in a 50 mm pipe: 18.4 litres per second is 9.37 metres per second. math.isclose is the safe way to compare floats, as promised earlier. The standard library is like the toolboxes that come with MATLAB, only free and already installed. Other useful names are math.sqrt, math.log, math.floor and math.ceil.
-->

---
layout: default
label: 4 · The standard library
---

# <span class="dm-accent">pathlib</span>: paths as objects

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
Path wraps a file or folder path. The slash operator joins parts correctly with the Windows separator, so you never glue strings together by hand. You get the name, suffix and stem for free, you can test existence, and glob finds all files matching a pattern. The csv files in the loop are what we process in the capstone: one script, many logs.
-->

---
layout: default
label: 4 · The standard library
---

# Windows paths and the <span class="dm-accent">backslash</span> trap

```python {all|1|2|all}
print("C:\new\table.csv")
print(r"C:\new\table.csv")
```

<v-click>

```text
C:
ew	able.csv
C:\new\table.csv
```

</v-click>

<v-click>

<DmBanner class="mt-4" tone="violet" icon="mdi:lightbulb-outline">
In a normal string, <code>\n</code> is a newline and <code>\t</code> is a tab. Use <code>Path(...)</code>, forward slashes, or a raw string with <code>r"..."</code>.
</DmBanner>

</v-click>

<style>
.slidev-code { font-size: 17px !important; line-height: 1.5 !important; }
</style>

<!--
The backslash starts an escape sequence in Python strings, and Windows paths are full of backslashes. The first line prints a path broken by a newline and a tab. A raw string, with the r in front, turns that off. Even better, build paths with pathlib and forward slashes, which Python on Windows accepts everywhere.
-->

---
layout: default
label: 4 · The standard library
---

# <span class="dm-accent">csv</span>: reading rows

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
DictReader turns every row into a dictionary keyed by the header names, so you get exactly the list of dicts we built by hand earlier. The with block opens the file and closes it again, we look at that properly in the next block. One thing to remember: every value comes back as a string, so convert with float before calculating.
-->

---
layout: default
label: 4 · The standard library
---

# <span class="dm-accent">csv</span>: writing rows

```python {all|2|3-5|all}
import csv
rows = [{"t_s": 0, "pressure_bar": 6.8}, {"t_s": 10, "pressure_bar": 7.1}]
with open("out.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["t_s", "pressure_bar"])
    writer.writeheader()
    writer.writerows(rows)
```

<v-click>

```text
t_s,pressure_bar
0,6.8
10,7.1
```

</v-click>

<style>
.slidev-code { font-size: 17px !important; line-height: 1.5 !important; }
</style>

<!--
Writing mirrors reading: DictWriter with the column names, a header line, then the rows. The mode "w" creates the file, and overwrites it if it exists. Always pass newline="" on Windows, otherwise you may get empty lines between the rows. Passing encoding="utf-8" avoids surprises with special characters.
-->

---
layout: default
label: 4 · The standard library
---

# <span class="dm-accent">json</span>: settings and nested data

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
layout: default
label: 4 · The standard library
---

# More <span class="dm-accent">built-in</span> modules worth knowing

<DmColumns class="mt-4">
<DmColumn>

- `statistics`: mean, median, stdev
- `datetime`: dates, times, durations
- `shutil`: copy and move files

</DmColumn>
<DmColumn divider>

- `argparse`: command-line options for scripts
- `collections`: Counter, defaultdict
- `random`: random numbers for simulations

</DmColumn>
</DmColumns>

<p class="mt-4">Outside the standard library: packages you install, which is what uv is for.</p>

<!--
The documentation at docs.python.org lists everything. A rule worth following: before you install a package or write something yourself, check whether the standard library already does it. Day 2 brings pandas and NumPy, which are not in the standard library, and need the installation tooling we meet next.
-->

---
layout: statement
---

# Exercise 06: <span class="dm-accent">Standard library</span>

`exercises/python/06-standard-library`

<!--
Use math, pathlib, csv and json on a small set of fictional bench logs. About 25 minutes.
-->
