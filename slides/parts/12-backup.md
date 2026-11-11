---
layout: section
title: Backup - More Python
---

# Backup: more <span class="dm-accent">Python</span>

<!--
Backup slides, not part of the day. Each one stands alone: use it when a participant asks about the topic, or when Copilot writes it in someone's exercise. Every title names the problem the tool solves. The first half is language: classes, dataclasses, pydantic, generators, decorators, context managers and asyncio. The second half is for scripts that grow: logging, command-line arguments, the debugger and dates. The last slide is a reading aid for short syntax that generated code uses.
-->

---
layout: default
label: Backup · More Python
---

# Same values passed to every function? Use a <span class="dm-accent">class</span>

```python
class Compressor:
    def __init__(self, name, limit_bar):     # runs when you create one
        self.name = name
        self.limit_bar = limit_bar
        self.pressures_bar = []

    def add(self, pressure_bar):             # a method: a function of the object
        self.pressures_bar.append(pressure_bar)

    def is_over_limit(self):
        return max(self.pressures_bar) > self.limit_bar

c101 = Compressor("C-101", limit_bar=9.0)    # an object, or instance
c101.add(9.4)
print(c101.name, c101.is_over_limit())       # C-101 True
```

<p class="note">You used objects all day: <code>readings.append(7.5)</code> calls a method of a list. A class lets you define your own type.</p>

<style>
.slidev-code { font-size: 14.5px !important; line-height: 1.45 !important; }
</style>

<!--
A class is a blueprint, an object is one thing built from it. The object carries its own data, the attributes, and the functions that work on that data, the methods. self is the object itself: Python passes it in for you, so c101.add(7.5) arrives as add(c101, 7.5). __init__ runs once, when you create the object. Everyone has used objects all day without writing a class: a list, a string and a Path are objects with methods. When is a class worth it? When several functions keep passing the same group of values around, or when you have many things of the same kind that each keep their own state. A dict and a few functions are fine for most scripts, so do not start with a class. MATLAB users: this is classdef, with less ceremony.
-->

---
layout: default
label: Backup · More Python
---

# A <span class="dm-accent">dataclass</span> catches the typo a dict lets through

```python
from dataclasses import dataclass

@dataclass
class Reading:
    t_s: int
    pressure_bar: float
    temperature_c: float

reading = Reading(t_s=10, pressure_bar=7.1, temperature_c=74.5)
print(reading)                             # Reading(t_s=10, pressure_bar=7.1, temperature_c=74.5)
print(reading.pressure_bar)                # 7.1, and the editor completes the name
print(reading == Reading(10, 7.1, 74.5))   # True
```

<p class="note">A dict accepts any key, so a typo gives a new key. A dataclass has fixed fields, so a typo is an error.</p>

<p class="ask"><b>Question</b>The field says <code>float</code>. What does <code>Reading(10, "7.1", 74.5)</code> give?</p>

<style>
.slidev-code { font-size: 14.5px !important; line-height: 1.45 !important; }
</style>

<!--
A dataclass is a class that mostly holds data. You list the fields with their types, and the decorator writes the rest for you: __init__, a readable print, and comparison by value. It is still a normal class, so you can add methods to it. Compare it with the dict from this morning: reading["presure_bar"] = 7.1 silently creates a new key, reading.presure_bar on a dataclass is flagged by the editor before you run. It is the modern replacement for a MATLAB struct with a fixed set of fields. Add frozen=True between brackets after dataclass to make the record read-only. The line with the at sign is a decorator, there is a slide on those further on. Question on the slide: it works, and the pressure is the text "7.1". As with type hints on functions, a dataclass does not check the types when the script runs. That is the job of pydantic, on the next slide.
-->

---
layout: default
label: Backup · More Python
---

# <span class="dm-accent">pydantic</span> rejects bad data before it spreads

```python
from pydantic import BaseModel, Field

class Reading(BaseModel):
    t_s: int
    pressure_bar: float = Field(gt=0, lt=20)   # a rule: between 0 and 20
    temperature_c: float

row = {"t_s": "10", "pressure_bar": "7.1", "temperature_c": "74.5"}   # from csv.DictReader
Reading(**row)        # Reading(t_s=10, pressure_bar=7.1, temperature_c=74.5)

Reading(t_s=20, pressure_bar=-1, temperature_c="hot")
```

```text
ValidationError: 2 validation errors for Reading
pressure_bar
  Input should be greater than 0 [type=greater_than, input_value=-1, input_type=int]
temperature_c
  Input should be a valid number, unable to parse string as a number [input_value='hot']
```

<p class="note">Not in the standard library: <code>uv add pydantic</code>. Validate at the edge (files, APIs, user input), then trust the data inside.</p>

<style>
.slidev-code { font-size: 13.5px !important; line-height: 1.4 !important; }
</style>

<!--
pydantic looks like a dataclass, but it enforces the types when the script runs. It converts where that is safe, so the strings from a CSV row become an int and two floats, and it raises a ValidationError that names every bad field at once, with the value it got. Field adds rules on top of the type, here a pressure between 0 and 20 bar. The two stars unpack the dict into keyword arguments. The idea to take away is where to validate: at the edge of your program, where data comes in from a file, an API or a person. After that point the rest of the code can trust that a Reading is a Reading. Without it, a bad value travels on and fails three functions later, or does not fail at all and ends up in a report. The error text on the slide is shortened. pydantic also reads and writes JSON, which makes it common for settings files and web APIs. For whole tables, day 2 has pandas, and pandera does this job for data frames.
-->

---
layout: default
label: Backup · More Python
---

# A <span class="dm-accent">generator</span> reads a file too big for memory

<DmColumns class="mt-2">
<DmColumn header="A list: everything in memory" tone="plain">

```python
def read_pressures(path):
    pressures = []
    with open(path, newline="") as f:
        for row in csv.DictReader(f):
            pressures.append(
                float(row["pressure_bar"]))
    return pressures
```

</DmColumn>
<DmColumn header="A generator: one row at a time" tone="violet">

```python
def read_pressures(path):
    with open(path, newline="") as f:
        for row in csv.DictReader(f):
            yield float(row["pressure_bar"])
```

</DmColumn>
</DmColumns>

```python
print(max(read_pressures("data/run_014.csv")))    # 7.5, also for ten million rows
for pressure_bar in read_pressures("data/run_014.csv"):
    ...
```

<p class="note">A generator runs <b>once</b>. Loop over it a second time and it is empty. Need the values twice? Make a list.</p>

<style>
.slidev-code { font-size: 14px !important; line-height: 1.45 !important; }
</style>

<!--
A function with yield is a generator. Calling it runs nothing yet: it gives back an object that produces the next value each time the loop asks for one, and pauses in between. The caller sees no difference in the for loop, but only one row is in memory at a time, so the ten million row log from the csv slide is no longer a problem. You met the short form this morning: the sum over a comprehension without brackets is a generator expression. Many things in Python work this way: an open file gives lines one at a time, and so do csv.DictReader, Path.glob, zip and enumerate. The trap is in the note: a generator is used up after one pass. max of it works, a second max of the same object fails on an empty sequence. If you print a generator you see "generator object", not the values; wrap it in list to look inside.
-->

---
layout: default
label: Backup · More Python
---

# Time or cache any function with a <span class="dm-accent">decorator</span>

<DmColumns class="mt-2">
<DmColumn header="Using one" tone="violet">

```python
@timed
def summarize_run(path):
    return max(read_pressures(path))

summarize_run("data/run_014.csv")
```

```text
summarize_run: 0.42 s
```

The `@` line means:<br/>`summarize_run = timed(summarize_run)`

</DmColumn>
<DmColumn header="Writing one" tone="plain" divider>

```python
import functools, time

def timed(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        took = time.perf_counter() - start
        print(f"{func.__name__}: {took:.2f} s")
        return result
    return wrapper
```

</DmColumn>
</DmColumns>

<p class="note">You will mostly <b>use</b> them: <code>@dataclass</code>, <code>@functools.cache</code>, <code>@pytest.fixture</code>, <code>@app.get("/runs")</code>.</p>

<style>
.slidev-code { font-size: 13.5px !important; line-height: 1.45 !important; }
</style>

<!--
A decorator is a function that takes a function and returns a new one. The at sign is only a shorter way to write the reassignment shown on the left. The new function, here called wrapper, does something before and after and calls the original in between: timing, logging, caching, retrying, checking permissions. The body of summarize_run stays about one thing. On the right, star args and double star kwargs mean "whatever arguments the caller gave", so the wrapper fits any function. functools.wraps copies the name and the docstring of the original onto the wrapper. Read the left column first and treat the right one as optional: in practice you use decorators that a library wrote, far more often than you write one. functools.cache is a useful one to know: it remembers the result per set of arguments, so a slow function runs only once for the same input.
-->

---
layout: default
label: Backup · More Python
---

# A <span class="dm-accent">context manager</span> never forgets to clean up

<DmColumns class="mt-2">
<DmColumn header="with, as you know it" tone="plain">

```python
with open(path) as f:
    text = f.read()
# the file is closed here,
# also when read() raised
```

The same pattern for a database connection, a lock, a temporary folder, a serial port

</DmColumn>
<DmColumn header="Your own" tone="violet" divider>

```python
import time
from contextlib import contextmanager

@contextmanager
def timer(label):
    start = time.perf_counter()  # set up
    try:
        yield                    # the block runs
    finally:                     # clean up
        took = time.perf_counter() - start
        print(f"{label}: {took:.2f} s")

with timer("read logs"):
    rows = read_all_logs()
```

</DmColumn>
</DmColumns>

<p class="note"><code>try / finally</code> is the long form: the <code>finally</code> block runs whether the code above it failed or not.</p>

<style>
.slidev-code { font-size: 13.5px !important; line-height: 1.4 !important; }
</style>

<!--
A context manager pairs a set-up step with a clean-up step and guarantees the clean-up, also when the block in between raises an exception. You have used one since the files slide: with open closes the file for you. The pattern fits anything you must give back: a connection to a database or a measuring instrument, a lock, a temporary folder. The right column shows the shortest way to write your own. It combines the two previous slides: a decorator from contextlib on a generator function. Everything before yield is the set-up, the with block runs at the yield, and the finally part is the clean-up. finally is new today: it belongs to try, like except, and it always runs. If the yield gives a value, with timer("x") as t receives it. The other way to write a context manager is a class with the methods __enter__ and __exit__; you will see that in library code.
-->

---
layout: default
label: Backup · More Python
---

# <span class="dm-accent">asyncio</span> waits for many slow things at once

<DmColumns class="mt-2">
<DmColumn header="One after the other: 3 s" tone="plain">

```python
import time

def read_pressure(name):
    time.sleep(1)    # a slow network request
    return name, 7.5

def main():
    names = ["C-101", "C-102", "C-103"]
    readings = [read_pressure(name)
                for name in names]
    print(readings)

main()
```

</DmColumn>
<DmColumn header="All at once: 1 s" tone="violet" divider>

```python
import asyncio

async def read_pressure(name):
    await asyncio.sleep(1)
    return name, 7.5

async def main():
    names = ["C-101", "C-102", "C-103"]
    readings = await asyncio.gather(
        *(read_pressure(name) for name in names))
    print(readings)

asyncio.run(main())
```

</DmColumn>
</DmColumns>

<p class="note">It speeds up <b>waiting</b> (network, databases, instruments), not <b>calculating</b>. For heavy maths: NumPy, or several processes.</p>

<style>
.slidev-code { font-size: 13.5px !important; line-height: 1.4 !important; }
</style>

<!--
The problem: a script that asks fifty compressors, or fifty web pages, for a value spends almost all its time waiting for answers, one after the other. asyncio lets one script wait for all of them at the same time. The sleep of one second stands for a slow request. On the left the three requests take three seconds, on the right one second, and with fifty it is still about one second. Two new words. async def defines a coroutine: a function that can pause. await marks the point where it pauses, and while it waits Python runs the other coroutines. gather starts them together and collects the results in order, and asyncio.run starts the whole thing from normal code. It is still one thread doing one thing at a time, it only never sits idle while waiting. That is why it does not help with calculation: a loop that computes for a second keeps everything else waiting. For that, use NumPy, or several processes with concurrent.futures. Two practical points. Async spreads: a function that awaits must itself be async, so you choose it for a whole program, not for one function. And you need libraries that support it, such as httpx for web requests, because a normal time.sleep or requests call inside async code blocks everything. If generated code is full of async and await and your script only reads a few files, ask for the plain version.
-->

---
layout: default
label: Backup · More Python
---

# <span class="dm-accent">logging</span> shows what an unattended script did

```python
import logging

logging.basicConfig(
    level=logging.INFO,                                  # the switch: show INFO and above
    format="%(asctime)s %(levelname)s %(message)s",
)
log = logging.getLogger(__name__)

log.debug("Row %d: %s", number, row)                     # hidden at level INFO
log.info("Read %d rows from %s", len(rows), path)
log.warning("Skipped %d rows without a pressure", skipped)
```

```text
2025-03-05 14:30:02,118 INFO Read 3 rows from data/run_014.csv
2025-03-05 14:30:02,118 WARNING Skipped 2 rows without a pressure
```

<p class="note">Five levels: <code>DEBUG</code>, <code>INFO</code>, <code>WARNING</code>, <code>ERROR</code>, <code>CRITICAL</code>. Add <code>filename="run.log"</code> to <code>basicConfig</code> to write to a file.</p>

<style>
.slidev-code { font-size: 14px !important; line-height: 1.45 !important; }
</style>

<!--
print is fine while you write a script. Once it runs every night without you, you want to know when something happened and how serious it was, and you want the detail off by default and on when you investigate. That is logging. Every message has a level. basicConfig sets, once, at the start of the script, which levels are shown and what a line looks like. Change INFO to DEBUG and the debug lines appear, without touching the rest of the code. The percent placeholders are the logging style: pass the values as extra arguments and the text is only built when the message is shown. getLogger with __name__ gives the logger the name of the module, so in a larger project you see which file a line came from. Keep print for the actual result of the script, and use logging for what happened along the way. log.exception inside an except block logs the message with the full traceback.
-->

---
layout: default
label: Backup · More Python
---

# <span class="dm-accent">argparse</span> changes the input without editing the script

```python
import argparse
from pathlib import Path

parser = argparse.ArgumentParser(description="Summarise one test bench run.")
parser.add_argument("log", type=Path, help="CSV file of the run")
parser.add_argument("--limit-bar", type=float, default=9.0, help="alarm limit")
args = parser.parse_args()

print(args.log, args.limit_bar)
```

```powershell
uv run python summarize_run.py data\run_014.csv --limit-bar 8.5
uv run python summarize_run.py --help
```

<p class="note">No more editing the script to change a file name. You get <code>--help</code>, type conversion and a clear error for free.</p>

<style>
.slidev-code { font-size: 14.5px !important; line-height: 1.45 !important; }
</style>

<!--
The step from a script for yourself to a tool for a colleague: the input is no longer a path typed into the code, but an argument on the command line. An argument without dashes is positional and required. One with two dashes is an option, here with a default. type converts the text from the command line, so args.log is a Path and args.limit_bar is a float, and a value that is not a number gives a clear message instead of a traceback. The dash in limit-bar becomes an underscore in args.limit_bar. The help text is generated from the description and the help strings. This also makes a script easy to schedule or to call from another program. sys.argv is the raw list underneath, and the packages typer and click do the same job with less code.
-->

---
layout: default
label: Backup · More Python
---

# The <span class="dm-accent">debugger</span> finds the bug without ten print lines

<DmSteps class="mt-4">
<DmStep n="1" label="Set a breakpoint">Click left of a line number, a red dot appears. The script will pause <b>before</b> that line.</DmStep>
<DmStep n="2" label="Start debugging">Press <code>F5</code>, or the arrow next to the play button, <b>Python Debugger: Debug Python File</b></DmStep>
<DmStep n="3" label="Look">Hover over a name, or read the <b>Variables</b> panel. Type any expression in the <b>Debug Console</b>.</DmStep>
<DmStep n="4" label="Step">Next line: <code>F10</code>. Into a function: <code>F11</code>. Out of it: <code>Shift+F11</code>. Continue: <code>F5</code>.</DmStep>
</DmSteps>

<p class="note">Right-click a breakpoint to add a condition, such as <code>pressure_bar > 9</code>: stop only at the row that matters.</p>

<!--
The alternative to adding print lines, running, and adding more print lines. A breakpoint pauses the script on a line of your choice, with all variables as they are at that moment. From there you step one line at a time and watch the values change, which is the fastest way to find where your idea of the program and the program itself differ. Step over runs the line, step into follows a function call into its body. The Debug Console is a Python prompt inside the paused script: try len(rows), or the expression you suspect. A conditional breakpoint is what you want in a loop over a thousand rows where only one goes wrong. The Call Stack panel is the traceback, live: click a level to see the variables of the function that called this one. If VS Code asks for a debug configuration, choose Python File. This is worth a five minute live demo on one of the broken scripts from exercise 07 if there is time.
-->

---
layout: default
label: Backup · More Python
---

# <span class="dm-accent">datetime</span> gets durations and date formats right

```python
from datetime import datetime, timedelta

start = datetime.fromisoformat("2025-03-05 14:30:00")       # text to datetime
end = start + timedelta(minutes=45)                         # 2025-03-05 15:15:00

print((end - start).total_seconds())                        # 2700.0
print(start < end)                                          # True
print(start.strftime("%d/%m/%Y %H:%M"))                     # 05/03/2025 14:30
print(datetime.strptime("05/03/2025 14:30", "%d/%m/%Y %H:%M"))   # and back
```

- **datetime**: a moment. **timedelta**: a duration, the difference between two moments
- **strftime** writes text, **strptime** reads it, with a format you choose

<p class="note">Store and exchange timestamps as ISO 8601 text (<code>2025-03-05T14:30:00</code>). <code>05/03/2025</code> is March in Belgium and May in the US.</p>

<style>
.slidev-code { font-size: 14px !important; line-height: 1.45 !important; }
</style>

<!--
Timestamps in a log are text until you convert them, the same lesson as with numbers this morning. A datetime is a moment, and subtracting two of them gives a timedelta, a duration. Python handles month lengths and leap years, so never do this arithmetic on strings or on separate hour and minute numbers. fromisoformat reads the international format directly. For any other layout, strptime parses text with a format string and strftime writes it: p for parse, f for format. The note is the practical advice: use ISO 8601 in files and file names. It is unambiguous and it sorts correctly as plain text. Time zones exist too: a datetime without one is called naive, and for data from several sites or across a daylight saving change you add one with zoneinfo. On day 2, pandas reads a whole timestamp column in one call.
-->

---
layout: default
label: Backup · More Python
---

# Decode the short syntax in <span class="dm-accent">generated code</span>

| You read | It means |
| --- | --- |
| `sorted(runs, key=lambda run: run["pressure_bar"])` | **lambda**: a small function without a name, here "sort by pressure" |
| `for p, t in zip(pressures_bar, temperatures_c):` | **zip**: walk through two lists side by side |
| `status = "high" if pressure_bar > 9.0 else "ok"` | An **if** inside one expression |
| `def plot(*args, **kwargs):` | Accept any positional and any named arguments |
| `summarize(**settings)` | Unpack a dict into named arguments |
| `limit_bar: float \| None = None` | A float or nothing, and nothing is the default |
| `if (n := len(rows)) > 100:` | **Walrus**: assign and use the value in one go |
| `match command:` with `case "start":` | Pick a branch by the shape of a value, like `switch` |

<p class="note">You do not have to write these. If a line is too dense to review, ask for the plain version.</p>

<style>
table { font-size: 14.5px; }
td, th { padding: 6px 12px !important; }
td:first-child { white-space: nowrap; }
</style>

<!--
A reading aid, not a list of things to learn. Each row is a piece of syntax that Copilot and library documentation use freely. lambda defines a one-expression function on the spot, almost always as the key of sorted, min or max. zip pairs up elements, and stops at the shortest list. The one-line if is called a conditional expression. One star collects extra positional arguments into a tuple, two stars collect named ones into a dict; at a call, two stars do the opposite and spread a dict out. The bar means "or" between types, so float or None. The walrus operator saves one line and costs some readability. match is Python's version of switch, with pattern matching on top. The note is the point of the slide: you review the code, so you set the level. Asking the agent to rewrite a dense line as a loop and an if is a normal request.
-->
