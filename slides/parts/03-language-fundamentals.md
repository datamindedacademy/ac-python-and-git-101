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

# Arithmetic, and a <span class="dm-accent">float</span> surprise

```python
print(7 / 2)       # 3.5   true division
print(7 // 2)      # 3     whole part only
print(7 % 2)       # 1     remainder
print(2 ** 10)     # 1024  power, not ^
print(0.1 + 0.2)   # 0.30000000000000004
```

<v-click>

<DmBanner class="mt-4" tone="violet" icon="mdi:calculator-variant-outline">
Floats are binary approximations. Never test two floats for exact equality.
</DmBanner>

</v-click>

<style>
.slidev-code { font-size: 17px !important; line-height: 1.5 !important; }
</style>

<!--
Power is double star, because the caret means something else in Python. The last line looks wrong but is correct: computers store decimals in binary, and 0.1 has no exact binary form. MATLAB does exactly the same, you may have seen it there. Later we use math.isclose to compare floats safely.
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

# Name things so the <span class="dm-accent">unit</span> is visible

<DmColumns class="mt-4">
<DmColumn header="Hard to read" tone="plain">

```python
p = 7.5
t = 82.3
q = 18.4
x1 = p * q
```

</DmColumn>
<DmColumn header="Clear" tone="violet">

```python
pressure_bar = 7.5
temperature_c = 82.3
flow_l_s = 18.4
power_kw = 37.5
```

</DmColumn>
</DmColumns>

<p class="mt-4">Lowercase with underscores (<code>snake_case</code>), and the unit as a suffix.</p>

<style>
.slidev-code { font-size: 17px !important; line-height: 1.5 !important; }
</style>

<!--
Names cost nothing and save hours. Python style is lowercase with underscores, and engineers benefit from putting the unit in the name, because unit confusion is a classic source of real errors. Names cannot start with a digit or contain spaces or dashes, and they are case sensitive. Avoid names like list or max, which already exist in Python.
-->

---
layout: statement
---

# Exercise 02: <span class="dm-accent">Variables and types</span>

`exercises/python/02-variables-and-types`

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

# Everyday <span class="dm-accent">list</span> operations

```python
p = [7.5, 6.8, 7.9, 7.1]
print(sum(p) / len(p))
print(sorted(p))
print(7.9 in p)
p.remove(6.8)
print(p)
```

```text
7.325
[6.8, 7.1, 7.5, 7.9]
True
[7.5, 7.9, 7.1]
```

<style>
.slidev-code { font-size: 17px !important; line-height: 1.5 !important; }
</style>

<!--
Built-in functions like sum, len, min, max and sorted work on any list. sorted returns a new list, while methods like append, remove and sort change the list in place. The keyword in checks membership. You will use these constantly before you ever need a library.
-->

---
layout: default
label: 3 · Language fundamentals
---

# Tuples and <span class="dm-accent">sets</span>

<DmColumns class="mt-4">
<DmColumn header="Tuple: fixed" tone="navy">

```python
limits = (5.0, 9.0)
low, high = limits
print(low, high)
limits[0] = 4.0
```

```text
TypeError: 'tuple' object does not
support item assignment
```

</DmColumn>
<DmColumn header="Set: unique" tone="violet">

```python
runs = {"TB-014", "TB-015", "TB-014"}
print(len(runs))
print("TB-015" in runs)
```

```text
2
True
```

</DmColumn>
</DmColumns>

<style>
.slidev-code { font-size: 17px !important; line-height: 1.5 !important; }
</style>

<!--
A tuple is a list that cannot change, used for small fixed groups like a lower and upper limit, and unpacking splits it into names. A set keeps each value once and has no order, handy for removing duplicates. Both are less common than lists and dicts, so just know they exist.
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
A dictionary looks things up by name instead of by position. It is like a MATLAB struct, but you use square brackets and quoted keys. A missing key with square brackets is a KeyError, while get returns None, or a default you pass. A dict is the natural way to describe one measurement record with several fields.
-->

---
layout: default
label: 3 · Language fundamentals
---

# A table of readings: a <span class="dm-accent">list of dicts</span>

```python {all|1-5|6-7|all}
readings = [
    {"t_s": 0, "pressure_bar": 6.8},
    {"t_s": 10, "pressure_bar": 7.1},
    {"t_s": 20, "pressure_bar": 7.5},
]
print(readings[2]["pressure_bar"])
print(len(readings))
```

<v-click>

```text
7.5
3
```

</v-click>

<p class="mt-2">One dict per row. This is exactly the shape you get when you read a CSV file.</p>

<style>
.slidev-code { font-size: 17px !important; line-height: 1.5 !important; }
</style>

<!--
Collections nest. A list of dicts is a small table, each dict a row. First pick the row with a number, then pick the field with its name. Keep this picture in mind, because the csv module in the next block hands you rows in exactly this form.
-->

---
layout: statement
---

# Exercise 03: <span class="dm-accent">Collections</span>

`exercises/python/03-collections`

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
Python checks the conditions top to bottom and runs the first block whose condition is true. Note the colon at the end of each header line, and note that there is no end keyword and no parentheses needed around the condition. MATLAB has elseif as one word, Python has elif.
-->

---
layout: default
label: 3 · Language fundamentals
---

# Comparisons and <span class="dm-accent">logic</span>

```python
pressure_bar = 7.5
run_id = "TB-014"
print(pressure_bar == 7.5, pressure_bar != 7.5)
print(5.0 <= pressure_bar <= 9.0)
print(pressure_bar > 9.0 or run_id == "TB-014")
print(not run_id.startswith("TB"))
```

```text
True False
True
True
False
```

<style>
.slidev-code { font-size: 17px !important; line-height: 1.5 !important; }
</style>

<!--
Comparison operators are the usual ones, with double equals for comparing and single equals for assigning, a classic slip. Python allows chained comparisons like 5 <= p <= 9, which reads like the engineering note. Combine conditions with the words and, or and not, not with the ampersand or the exclamation mark as in MATLAB or C.
-->

---
layout: default
label: 3 · Language fundamentals
---

# <span class="dm-accent">Indentation</span> is the syntax

<DmColumns class="mt-2">
<DmColumn header="Works" tone="violet">

```python
if pressure_bar > 9.0:
    print("ALARM")
    print("Stop the test")
print("Checked")
```

</DmColumn>
<DmColumn header="Fails" tone="plain">

```python
if pressure_bar > 9.0:
print("ALARM")
```

```text
IndentationError: expected an
indented block after 'if' statement
on line 1
```

</DmColumn>
</DmColumns>

<style>
.slidev-code { font-size: 17px !important; line-height: 1.5 !important; }
</style>

<!--
Python uses indentation, four spaces, to show which lines belong to a block. The block ends when the indentation goes back. This replaces MATLAB's end and the braces of other languages. The two ALARM lines run only when the condition is true, the last line always runs. VS Code inserts four spaces when you press Tab.
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
A for loop takes each element of a collection in turn and runs the indented block with it. Loop over the values directly, you rarely need an index. When you need a count, range gives 0, 1, 2 and stops before the end value, the same exclusive end as slices. There is no end keyword, the indentation closes the loop.
-->

---
layout: default
label: 3 · Language fundamentals
---

# Looping until a condition: <span class="dm-accent">while</span>

```python {all|3-4|all}
pressure_bar = 1.0
steps = 0
while pressure_bar < 7.0:
    pressure_bar *= 1.5
    steps += 1
print(steps, round(pressure_bar, 2))
```

<v-click>

```text
5 7.59
```

</v-click>

<p class="mt-2">If the condition never becomes false, the loop never ends. Stop it with <code>Ctrl+C</code>.</p>

<style>
.slidev-code { font-size: 17px !important; line-height: 1.5 !important; }
</style>

<!--
Use while when you do not know in advance how many rounds are needed, such as ramping up until a target is reached. Something inside the loop must change the condition, otherwise you get an infinite loop. If that happens, Ctrl+C in the terminal interrupts the script. The operators *= and += are shorthand for updating a variable in place.
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
This is the shape of most automation scripts: start with an empty list and a running total, loop over the data, decide with an if, and report at the end. Say it out loud: initialise, loop, test, collect. If you can write this pattern, you can write the capstone. Put the if inside the loop, the indentation shows which one is nested in which.
-->

---
layout: statement
---

# Exercise 04: <span class="dm-accent">Control flow</span>

`exercises/python/04-control-flow`

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

# Default values and <span class="dm-accent">keyword</span> arguments

```python {all|1|4|5|all}
def is_over_limit(pressure_bar, limit_bar=9.0):
    return pressure_bar > limit_bar

print(is_over_limit(9.4))
print(is_over_limit(9.4, limit_bar=10.0))
```

<v-click>

```text
True
False
```

</v-click>

<style>
.slidev-code { font-size: 17px !important; line-height: 1.5 !important; }
</style>

<!--
A parameter with an equals sign has a default and can be left out. When you call, writing the name, limit_bar=10.0, makes the call self-explaining. Prefer keyword arguments whenever a call has more than two or three values, so you do not mix up the order.
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

# Variables inside a function stay <span class="dm-accent">inside</span>

```python {all|1-3|5-6|all}
def mean(values):
    total = sum(values)
    return total / len(values)

print(round(mean([6.8, 7.1, 7.5]), 2))
print(total)
```

<v-click>

```text
7.13
NameError: name 'total' is not defined
```

</v-click>

<style>
.slidev-code { font-size: 17px !important; line-height: 1.5 !important; }
</style>

<!--
Names created inside a function exist only while the function runs. This is a good thing, it means functions cannot accidentally overwrite each other's variables. Everything a function needs goes in through parameters, everything it produces comes out through return. The NameError is another message you will meet often.
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
Real scripts are small functions that call each other, plus a main function that does the work. The string right under def is a docstring: the function's documentation, shown by help() and by VS Code on hover, like the help text at the top of a MATLAB function. The last two lines mean: run main only when this file is started directly, not when another script imports it. Treat that as a fixed phrase for now. The output is a dictionary with min 6.8, max 9.4 and mean 7.675.
-->

---
layout: statement
---

# Exercise 05: <span class="dm-accent">Functions</span>

`exercises/python/05-functions`

<!--
Write, call and combine small functions. This is the building block for everything after lunch. About 25 minutes.
-->
