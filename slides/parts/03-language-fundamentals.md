---
layout: section
---

# Language <span class="dm-accent">fundamentals</span>

<!--
The biggest block of the day. Variables, types, collections, control flow and functions, each followed by an exercise. All examples use compressor test-bench data, and all numbers are made up.
-->

---
layout: default
label: 3 · Language fundamentals
---

# Variables are <span class="dm-accent">names</span> for values

```python {all|1-3|5|6-7|all}
pressure_bar = 7.5
temperature_c = 82.3
run_id = "TB-014"

pressure_bar = 8.0
print(pressure_bar)
print(temperature_c)
```

<v-click>

```text
8.0
82.3
```

</v-click>

<style>
.slidev-code { font-size: 17px !important; line-height: 1.5 !important; }
</style>

<!--
The equals sign does not mean mathematical equality, it means: give this value this name. No declaration, no type, no semicolon, no end keyword. Assigning again to the same name simply points it at a new value. Compared with MATLAB, there is no output echo: nothing prints unless you call print.
-->

---
layout: default
label: 3 · Language fundamentals
---

# The basic <span class="dm-accent">data types</span>

```python
run_id = "TB-014"       # str: text
cycles = 12             # int: whole number
flow_l_s = 18.4         # float: decimal number
is_stable = True        # bool: True or False
operator = None         # None: no value (yet)

print(type(flow_l_s))
```

```text
<class 'float'>
```

<style>
.slidev-code { font-size: 17px !important; line-height: 1.5 !important; }
</style>

<!--
Every value has a type, and the type decides what you can do with it. Text is str, whole numbers int, decimals float, and truth values bool. None is the explicit "nothing here yet". Python works out the type from the value, so you do not declare it. In MATLAB nearly everything is a double matrix, here the distinction matters from the start.
-->

---
layout: default
label: 3 · Language fundamentals
---

# Converting <span class="dm-accent">between</span> types

```python {all|1-3|5-6|all}
text = "7.5"
pressure_bar = float(text)
print(pressure_bar + 1)        # 8.5

count = 3
print("Cycles: " + count)
```

<v-click>

```text
TypeError: can only concatenate str (not "int") to str
```

</v-click>

<style>
.slidev-code { font-size: 17px !important; line-height: 1.5 !important; }
</style>

<!--
Text read from a file or typed by a user is always a string, even if it looks like a number. Use float, int and str to convert. Python does not convert silently: adding text and a number is an error, and that is a feature. Here is our first error message, notice that it tells you the kind of error and what went wrong. We read these properly after lunch.
-->

---
layout: default
label: 3 · Language fundamentals
---

# Strings and <span class="dm-accent">f-strings</span>

```python {all|3|4|all}
run_id = "TB-014"
pressure_bar = 7.5
print(f"Run {run_id}: {pressure_bar:.1f} bar")
print(f"{pressure_bar * 14.5038:.0f} psi")
print("TB" in run_id, run_id.lower())
```

<v-click>

```text
Run TB-014: 7.5 bar
109 psi
True tb-014
```

</v-click>

<style>
.slidev-code { font-size: 17px !important; line-height: 1.5 !important; }
</style>

<!--
Put an f before the quote and you can place any expression inside curly braces. After the colon you control the format: .1f means one decimal place, .0f none. Strings also have methods such as lower, upper, strip, split and replace, called with a dot. Both single and double quotes work, pick one style and stay with it.
-->

---
layout: default
label: 3 · Language fundamentals
---

# Names are <span class="dm-accent">signposts</span>

<DmColumns class="mt-2">
<DmColumn header="Written fast" tone="plain">

```python
p = 7.5
t = 82
calc(p, t)
```

</DmColumn>
<DmColumn header="Read easily" tone="violet">

```python
pressure_bar = 7.5
temperature_c = 82
to_kelvin(temperature_c)
```

</DmColumn>
</DmColumns>

<p class="mt-4">Put the unit in the name. Constants in capitals: <code>ALARM_LIMIT_BAR = 8.5</code></p>

<style>
.slidev-code { font-size: 17px !important; line-height: 1.5 !important; }
</style>

<!--
From Oliver's Clean Code workshop. Code is read more often than it is written, and single-letter names optimise for writing, not for reading. A good name answers the question before it is asked: which quantity, in which unit. Python style is lowercase with underscores, and capitals for values that never change. There is a bonus today: Copilot follows the naming it sees, so good names also improve the code it generates for you.
-->

---
layout: statement
---

# Exercise 02: <span class="dm-accent">Variables and types</span>

`exercises/python/02-variables-and-types`

<p class="words"><b>Words you can now use</b> variable · assignment · type · string · float · f-string · convert</p>

<style>
.words { font-size: 15px; opacity: 0.9; margin-top: 14px; }
.words b { margin-right: 8px; }
</style>

<!--
Variables, types, f-strings and one deliberate type error to fix. About 15 minutes.
-->

---
layout: default
label: 3 · Language fundamentals
---

# Lists: an <span class="dm-accent">ordered</span> collection

```python {all|1|2|3|4-5|all}
pressures_bar = [6.8, 7.1, 7.5, 7.4, 7.9]
print(pressures_bar[0])
print(len(pressures_bar))
pressures_bar.append(8.2)
print(max(pressures_bar))
```

<v-click>

```text
6.8
5
8.2
```

</v-click>

<style>
.slidev-code { font-size: 17px !important; line-height: 1.5 !important; }
</style>

<!--
A list holds many values in order, written in square brackets. It can mix types and it grows with append. Careful if you come from MATLAB: this is not a numeric matrix, you cannot multiply a list by two and expect element-wise results. Numeric arrays arrive with NumPy on day 2. Indexing is with square brackets, and it starts at zero.
-->

---
layout: default
label: 3 · Language fundamentals
---

# Indexing starts at <span class="dm-accent">zero</span>

<table class="idx"><tbody>
<tr><th>index</th><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td></tr>
<tr><th>value</th><td>6.8</td><td>7.1</td><td>7.5</td><td>7.4</td><td>7.9</td></tr>
<tr><th>negative</th><td>-5</td><td>-4</td><td>-3</td><td>-2</td><td>-1</td></tr>
</tbody></table>

```python
p = [6.8, 7.1, 7.5, 7.4, 7.9]
print(p[1:3], p[:2], p[-2:])
```

```text
[7.1, 7.5] [6.8, 7.1] [7.4, 7.9]
```

<style>
.slidev-code { font-size: 17px !important; line-height: 1.5 !important; }
.idx { margin: 0 auto 12px; border-collapse: collapse; font-size: 0.95em; }
.idx td, .idx th { border: 1px solid #c9c4dd; padding: 4px 18px; text-align: center; }
.idx th { background: var(--dm-surface); font-weight: 600; }
</style>

<!--
This is the one that bites MATLAB users. The first element is index 0, not 1, and the slice 1:3 is MATLAB 2:3: the end of a slice is excluded. Negative indexes count from the end, so -1 is the last element, no end keyword needed. Slices give you a new list. If a script is off by one, suspect this first.
-->

---
layout: default
label: 3 · Language fundamentals
---

# Dictionaries: <span class="dm-accent">key to value</span>

```python {all|1|2|3-4|5|all}
reading = {"run": "TB-014", "pressure_bar": 7.5}
print(reading["pressure_bar"])
reading["flow_l_s"] = 18.4
print(reading.get("power_kw"))
print(reading)
```

<v-click>

```text
7.5
None
{'run': 'TB-014', 'pressure_bar': 7.5, 'flow_l_s': 18.4}
```

</v-click>

<style>
.slidev-code { font-size: 17px !important; line-height: 1.5 !important; }
</style>

<!--
A dictionary looks things up by name instead of by position. It is like a MATLAB struct, but you use square brackets and quoted keys. A missing key with square brackets is a KeyError, while get returns None, or a default you pass. A dict is the natural way to describe one measurement record with several fields. A list of such dicts is a small table, and that is exactly what the csv module hands you in the next block.
-->

---
layout: default
label: 3 · Language fundamentals
---

# A choice: <span class="dm-accent">list</span> or <span class="dm-accent">dict</span>?

<DmComparison
  class="mt-2"
  :rows="['Find by', 'Fits', 'Example']"
  :cols="['list', 'dict']"
>
  <template #r0c0>Position, in order</template>
  <template #r0c1>Name, the key</template>

  <template #r1c0>A series of the same kind of value</template>
  <template #r1c1>One record with different fields</template>

  <template #r2c0><code>pressures_bar[2]</code></template>
  <template #r2c1><code>reading["pressure_bar"]</code></template>
</DmComparison>

<p class="mt-4">Copilot will pick one for you unless you say which you want.</p>

<!--
Both can hold the same measurements, and the choice shapes all the code that follows. A list is right for a time series: many values of one kind, where order matters and you loop over all of them. A dict is right for one record with named fields, where you want to ask for the pressure by name and not remember that it was column two. The cost of a list is that positions are easy to mix up, the cost of a dict is that a mistyped key fails. When you ask Copilot for code, say it: "return a list of floats" or "return a dict with these keys". If you do not, it chooses, and you inherit the choice.
-->

---
layout: statement
---

# Exercise 03: <span class="dm-accent">Collections</span>

`exercises/python/03-collections`

<p class="words"><b>Words you can now use</b> list · index · slice · dict · key · value</p>

<style>
.words { font-size: 15px; opacity: 0.9; margin-top: 14px; }
.words b { margin-right: 8px; }
</style>

<!--
Lists, slicing, a dictionary and a list of dictionaries. Watch for the off-by-one in slices. About 20 minutes.
-->

---
layout: default
label: 3 · Language fundamentals
---

# Decisions with <span class="dm-accent">if</span>, elif, else

```python {all|2|4|6|all}
pressure_bar = 9.4
if pressure_bar > 9.0:
    print("ALARM: over limit")
elif pressure_bar < 5.0:
    print("Warning: low pressure")
else:
    print("OK")
```

<v-click>

```text
ALARM: over limit
```

</v-click>

<style>
.slidev-code { font-size: 17px !important; line-height: 1.5 !important; }
</style>

<!--
Python checks the conditions top to bottom and runs the first block whose condition is true. Each of those blocks is called a branch. Note the colon at the end of each header line, and note that there is no end keyword and no parentheses needed around the condition. MATLAB has elseif as one word, Python has elif.
-->

---
layout: default
label: 3 · Language fundamentals
---

# Repeating with <span class="dm-accent">for</span>

```python {all|2|1,3|all}
pressures_bar = [6.8, 7.1, 9.4]
for p in pressures_bar:
    print(f"{p:.1f} bar")

for i in range(3):
    print(i)
```

<v-click>

```text
6.8 bar
7.1 bar
9.4 bar
0
1
2
```

</v-click>

<style>
.slidev-code { font-size: 17px !important; line-height: 1.5 !important; }
</style>

<!--
A for loop takes each element of a collection in turn and runs the indented block with it. This is the power of the for loop, and the rule from Oliver's Clean Code workshop is do not repeat yourself: if you copy and paste a line and change one value, you want a loop or a function. The specialist's word is iterate: we iterate over the list. Loop over the values directly, you rarely need an index. When you need a count, range gives 0, 1, 2 and stops before the end value, the same exclusive end as slices. There is no end keyword, the indentation closes the loop.
-->

---
layout: default
label: 3 · Language fundamentals
---

# Loop pattern: <span class="dm-accent">filter and summarise</span>

```python {all|2-3|5-8|10|all}
pressures_bar = [6.8, 7.1, 9.4, 7.4, 9.1]
high = []
total = 0.0

for p in pressures_bar:
    total += p
    if p > 9.0:
        high.append(p)

print(high, round(total / len(pressures_bar), 2))
```

<v-click>

```text
[9.4, 9.1] 7.96
```

</v-click>

<style>
.slidev-code { font-size: 17px !important; line-height: 1.5 !important; }
</style>

<!--
This is the shape of most automation scripts: start with an empty list and a running total, loop over the data, decide with an if, and report at the end. Say it out loud: initialise, loop, test, collect. This pattern is the core of the file exercises after lunch. Put the if inside the loop, the indentation shows which one is nested in which.
-->

---
layout: statement
---

# Exercise 04: <span class="dm-accent">Control flow</span>

`exercises/python/04-control-flow`

<p class="words"><b>Words you can now use</b> condition · branch · loop · iterate · block · indentation</p>

<style>
.words { font-size: 15px; opacity: 0.9; margin-top: 14px; }
.words b { margin-right: 8px; }
</style>

<!--
Conditions, for loops and a while loop on bench readings. About 20 minutes. Break time after this exercise if the room is ready for it.
-->

---
layout: default
label: 3 · Language fundamentals
---

# Functions: <span class="dm-accent">name</span> a piece of logic

```python {all|1-2|4|all}
def to_psi(pressure_bar):
    return round(pressure_bar * 14.5038, 1)

print(to_psi(7.5))
print(to_psi(10))
```

<v-click>

```text
108.8
145.0
```

</v-click>

<style>
.slidev-code { font-size: 17px !important; line-height: 1.5 !important; }
</style>

<!--
def defines a function, followed by the name, parameters in parentheses, a colon and an indented body. return hands a value back to the caller. In MATLAB you needed one function per file, in Python you define as many as you like in the same script, and there is no end keyword.
-->

---
layout: default
label: 3 · Language fundamentals
---

# <span class="dm-accent">return</span> is not print

```python {all|1-2|4-5|all}
def double_and_print(x):
    print(x * 2)

result = double_and_print(4)
print(result)
```

<v-click>

```text
8
None
```

</v-click>

<p class="mt-2">A function without <code>return</code> gives back <code>None</code>. Use <code>print</code> to show, <code>return</code> to pass on.</p>

<style>
.slidev-code { font-size: 17px !important; line-height: 1.5 !important; }
</style>

<!--
The most frequent beginner confusion. print shows something on screen for a human, return gives the value to the code that called the function. If you want to use the result in a calculation, the function must return it. The 8 appears because the function printed it, the None is what the function returned.
-->

---
layout: default
label: 3 · Language fundamentals
---

# A small <span class="dm-accent">program</span> made of functions

```python {all|1-3|5-6|8-11|13-14|all}
def mean(values):
    """Return the arithmetic mean of a list of numbers."""
    return sum(values) / len(values)

def summarise(values):
    return {"min": min(values), "max": max(values), "mean": mean(values)}

def main():
    pressures_bar = [6.8, 7.1, 9.4, 7.4]
    print(summarise(pressures_bar))

if __name__ == "__main__":
    main()
```

<style>
.slidev-code { font-size: 17px !important; line-height: 1.5 !important; }
</style>

<!--
Real scripts are small functions that call each other, plus a main function that does the work. The string right under def is a docstring: the function's documentation, shown by help() and by VS Code on hover, like the help text at the top of a MATLAB function. On comments in general: a comment explains why, the code says what. Delete commented-out code, Git remembers it for you, and Git comes this afternoon. The last two lines mean: run main only when this file is started directly, not when another script imports it. You will see this phrase in most generated code; it is optional in small scripts, including exercise 05. The output is a dictionary with min 6.8, max 9.4 and mean 7.675.
-->

---
layout: default
label: 3 · Language fundamentals
---

# Type hints: <span class="dm-accent">reading</span> a signature

```python
def to_psi(pressure_bar: float, decimals: int = 1) -> float:
    return round(pressure_bar * 14.5038, decimals)
```

<div class="hints">

- `pressure_bar: float` the parameter and the type it expects
- `decimals: int = 1` a type and a default value
- `-> float` the type of the return value

</div>

<p class="mt-4">Hints are documentation that the editor and tools can check. Python does not enforce them when the script runs.</p>

<style>
.slidev-code { font-size: 17px !important; line-height: 1.5 !important; }
.hints li { margin-bottom: 6px; }
</style>

<!--
Copilot writes type hints all the time, so you need to be able to read them today. Writing them, and checking them with a type checker, is a day 3 topic. A hint after a colon says which type a parameter expects, the arrow says what comes back. They are promises, not guards: calling to_psi with the text "7.5" is accepted at the call and only fails inside, at the multiplication, with a TypeError. The value for you is that the signature alone tells you how to call the function. We do not use hints in the other examples today, to keep them short.
-->

---
layout: default
label: 3 · Language fundamentals
---

# A choice: <span class="dm-accent">script</span>, <span class="dm-accent">function</span> or <span class="dm-accent">module</span>?

<DmComparison
  class="mt-2"
  :rows="['Lines in the script', 'A function', 'A module']"
  :cols="['Use it when', 'The cost']"
>
  <template #r0c0>You do it once, in a few lines</template>
  <template #r0c1>Copy and paste when you need it again</template>

  <template #r1c0>You repeat it, or it deserves a name</template>
  <template #r1c1>A little structure to read through</template>

  <template #r2c0>Several scripts need the same functions</template>
  <template #r2c1>One more file, and an <code>import</code></template>
</DmComparison>

<p class="mt-4">Copilot will pick one for you unless you say which you want.</p>

<!--
Three places the same logic can live. Straight in the script is fine for a one-off. Once you repeat something, or a block of lines needs a comment to explain it, give it a name: a function. When a second script needs the same function, move it to its own .py file, a module, and import it, exactly like you import math after lunch. Do not start with modules: move code outward only when the need shows up. Keep it simple: the simplest version that works is the one to keep. Assistants tend to go to one extreme, either one long script or many small files, so tell Copilot which level you want: "keep it in one file, with a function per step".
-->

---
layout: default
label: 3 · Language fundamentals
---

# A test says what <span class="dm-accent">correct</span> means

```python
import pytest
import conversions

def test_bar_to_psi():
    assert conversions.bar_to_psi(1) == pytest.approx(14.5038)
```

<DmProcess class="mt-6">
<DmPhase label="Red: run, read the failure" />
<DmPhase label="Green: make it pass" />
<DmPhase label="Test first: write the next test" />
</DmProcess>

<p class="mt-6">This loop is <b>test-driven development</b>.</p>

<style>
.slidev-code { font-size: 17px !important; line-height: 1.5 !important; }
</style>

<!--
This ties back to the first question for judging code: is it correct? A test is a small function whose name starts with test and that contains an assertion: a statement that must be true. Here: 1 bar is 14.5038 psi, and pytest.approx compares floats with a tiny tolerance, because floats carry small rounding errors. Red: run the tests and read the failure. Green: write the function until the test passes. Test first: write the next test, test_psi_to_bar, before psi_to_bar exists. A test is the most precise way to tell a colleague or Copilot what you want, and the way to check what comes back. In exercise 05 you run uv run pytest on the exercise folder and write one test yourself before the function exists. Day 3 teaches pytest properly: fixtures, parametrize and running tests in the pipeline.
-->

---
layout: statement
---

# Exercise 05: <span class="dm-accent">Functions</span>

`exercises/python/05-functions`

<p class="words"><b>Words you can now use</b> function · argument · return value · type hint · test · assertion · test-driven development</p>

<style>
.words { font-size: 15px; opacity: 0.9; margin-top: 14px; }
.words b { margin-right: 8px; }
</style>

<!--
Write, call and combine small functions, test first: run the given tests, see them fail, and make them pass. This is the building block for everything after lunch. About 25 minutes.
-->
