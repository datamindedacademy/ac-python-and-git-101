# 02 - Variables and types

**Words to use:** variable, assignment, type, int, float, str, method, f-string, constant, boolean, traceback.

## Goal

Take values that arrive as text, clean them with string methods, convert them to numbers, convert units, and print clear messages with f-strings.

## Why this matters

Measurement data almost always arrives as text. A value with the wrong type or the wrong unit gives a wrong number, often without any error message. A name that carries the unit, like `pressure_bar`, is the cheapest protection.

## Background

- A **variable** is a name that points to a value: `mass_kg = 12.5`. Use lower case and underscores (`snake_case`). Put the unit in the name.
- Every value has a **type**. The basic ones:
  - `int`: whole number, like `82`.
  - `float`: number with decimals, like `7.5`.
  - `str`: text, like `"CB-0042"`. Text goes between quotes.
  - `bool`: `True` or `False`.
- `type(x)` tells you the type of `x`.
- **Converting** means changing type: `float("3.2")` turns the text `"3.2"` into the number 3.2. `int(2.9)` and `str(2.9)` work the same way. Text that is not a number, like `float("abc")`, gives an error.
- A **method** is a function that belongs to a value. You call it with a dot. Text has many methods, and each one gives a **new** text. The original does not change:

  ```python
  "12 kg".removesuffix(" kg")  # '12', the text without the end
  "CB-0042".lower()  # 'cb-0042'
  ```

  The result is still text. Convert it with `float()` when you need a number.
- A method call gives a value, so you can call the next method on it: `"12 KG".lower().removesuffix(" kg")`.
- `help(str)` lists every method of text.
- A **comparison** like `a > b` gives a `bool`: `True` or `False`. Other comparisons: `<`, `>=`, `<=`, `==`, `!=`.
- An **f-string** puts values inside text: `f"Mass: {mass_kg} kg"`. Add `:.2f` after the name to show 2 decimals: `{mass_kg:.2f}`.
- A name in CAPITALS (like `BAR_TO_PSI`) is a convention for a **constant**: a value that never changes.
- A **traceback** is the report Python prints when a script crashes. The last line names the error. The lines above it show where it happened.

## Tasks

Open `exercises/python/02-variables-and-types/units.py`. There are three tasks. No task needs a loop or an `if`. Run with:

```powershell
uv run python exercises/python/02-variables-and-types/units.py
```

### Task 1: text to numbers

Turn `pressure_text` and `temperature_text` into numbers and print the two lines below. Keep the numbers in variables whose names carry the unit. Do not type the numbers in the print lines.

```text
Pressure: 7.50 bar = 108.78 psi
Temperature: 82.00 degC = 355.15 K
```

### Task 2: read an error

Add this line at the end of the file, after your task 1 code, and run the script:

```python
print("Pressure: " + pressure_bar)
```

It crashes on purpose. Read the traceback from the bottom up: which error is it, and on which line? Then change the line so the script prints `Pressure: 7.5 bar`, with the unit.

```text
Traceback (most recent call last):
  File "units.py", line 20, in <module>
    print("Pressure: " + pressure_bar)
          ~~~~~~~~~~~~~^~~~~~~~~~~~~~
TypeError: can only concatenate str (not "float") to str
```

(The file path and line number in your traceback differ.)

### Task 3: a messy reading

This one is much harder.

`raw_sensor`, `raw_pressure` and `raw_temperature` are three fields as a technician typed them into a log: extra spaces, mixed upper and lower case, and a decimal comma. The pressure is in psi and the temperature is in degrees Fahrenheit. Print the reading in bar and degrees Celsius, and say whether the pressure is above `ALARM_LIMIT_BAR`.

```text
Sensor P1
Pressure: 7.50 bar
Temperature: 82.00 degC
Above limit: True
```

Rules:

- No loop, no `if`, no `import`.
- No `split()` and no square brackets. Text methods are enough.
- Do not type the sensor name or any number from the three values. Do not edit the three values.
- Fahrenheit to Celsius is `(f - 32) * 5 / 9`.
- When `float()` refuses a text, read the last line of the traceback: it shows the exact text it got, with the quotes.

## Open question

`0.1 + 0.2 == 0.3` is `False`, but `0.5 + 0.25 == 0.75` is `True`. Why? What does that mean for a script that checks whether two measured pressures are equal?

A second one. Run this:

```python
import sys

print(sys.getsizeof(1), sys.getsizeof(1.0))
```

It prints `28 24`: the whole number 1 takes more bytes than the float 1.0. Why? Try `sys.getsizeof(2**100)` as well. What does that tell you about the largest `int` Python can hold?
