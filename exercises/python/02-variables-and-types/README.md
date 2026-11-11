# 02 - Variables and types

**Words to use:** variable, assignment, type, int, float, str, f-string, constant.

## Goal

Take values that arrive as text, convert them to numbers, convert units, and print clear messages with f-strings.

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
- `text.split()` cuts a text at the spaces and gives a **list** of the parts. Lists come in exercise 03. For now you only need to pick a part by its position. Counting starts at 0:

  ```python
  parts = "12 kg".split()  # ['12', 'kg']
  parts[0]  # '12', the first part
  parts[1]  # 'kg', the second part
  ```

  Both parts are still text. Convert the number part with `float()`.
- A **comparison** like `a > b` gives a `bool`: `True` or `False`. Other comparisons: `<`, `>=`, `<=`, `==`, `!=`.
- An **f-string** puts values inside text: `f"Mass: {mass_kg} kg"`. Add `:.2f` after the name to show 2 decimals: `{mass_kg:.2f}`.
- A name in CAPITALS (like `BAR_TO_PSI`) is a convention for a **constant**: a value that never changes.

## Tasks

Open `exercises/python/02-variables-and-types/units.py` and do TODO 1 to 6. Each TODO says which result to reach. Try it with the hint closed first. Open the hint only when you are stuck. Run the script after every step:

```powershell
uv run python exercises/python/02-variables-and-types/units.py
```

<details>
<summary>Hint for TODO 1</summary>

`print(a, type(a))` prints a value followed by its type.

</details>

<details>
<summary>Hint for TODO 2</summary>

Use `float()` on the text. Then add `273.15` to the number.

</details>

<details>
<summary>Hint for TODO 3</summary>

Use `.split()` on `pressure_text`. Take the first part with `[0]` and the second with `[1]`. Convert the first part with `float()`.

</details>

<details>
<summary>Hint for TODO 4</summary>

Multiply `pressure_bar` by `BAR_TO_PSI`.

</details>

<details>
<summary>Hint for TODO 5</summary>

Use an f-string with `{...}` for each variable. For two decimals write `{pressure_bar:.2f}`. Kelvin needs a variable too: keep the result of TODO 2 in `temperature_k`.

</details>

<details>
<summary>Hint for TODO 6</summary>

Compare with `>`. The result of a comparison is already a `bool`.

</details>

7. **Read an error.** Add this line at the end of `units.py` and run the script:

   ```python
   print(temperature_text + 1)
   ```

   It crashes on purpose. Read the traceback from the bottom up. Which exception is it, and on which line? Then remove the line.

## Check yourself

The script should print:

```text
CB-0042 <class 'str'>
7.5 bar <class 'str'>
82 <class 'str'>
Temperature in K: 355.15
7.5 <class 'float'>
bar <class 'str'>
Pressure in psi: 108.7785
Unit CB-0042 runs at 7.50 bar (108.78 psi) and 355.15 K
Alarm: False
```

Floats can show tiny extra digits. That is normal.

For task 7 the last line of the traceback names a `TypeError`.

## Optional: if you have time

1. In a new file `ask.py` in the same folder, ask the user for a pressure with `input()` and print it in psi. `input()` always returns text, so you must convert it with `float()`.

   ```python
   text = input("Pressure in bar: ")
   ```

   Run it with `uv run python exercises/python/02-variables-and-types/ask.py` and type `7.5` when it asks.

2. Run `print(0.1 + 0.2)`. Why is it not exactly `0.3`? (Floats are stored in binary. Small rounding errors are normal. Use `round()` when printing.)
3. Convert the temperature to degrees Fahrenheit: `c * 9 / 5 + 32`.
4. Print `int(7.9)` and `round(7.9)`. Is `int()` rounding?

### With Copilot

Ask Copilot Chat: *"Show two other ways to format a float with 2 decimals inside a Python string, besides an f-string."* You will probably get `str.format()` and the `%` operator. Run both. Which of the three would you rather read in a colleague's script, and why?

## Challenge

For those who finish early. There are no TODOs and no hints.

Write `parse.py`. It gets text such as `"7.5 bar"` or `"108.8 psi"`. Split it into a value and a unit, convert the value to the other unit, and print the result:

```text
7.5 bar = 108.78 psi
```

Text with an unknown unit, such as `"3 atm"`, prints a clear message instead of crashing.

## Open question

`0.1 + 0.2 == 0.3` is `False`, but `0.5 + 0.25 == 0.75` is `True`. Why? What does that mean for a script that checks whether two measured pressures are equal?

A second one. Run this:

```python
import sys

print(sys.getsizeof(1), sys.getsizeof(1.0))
```

It prints `28 24`: the whole number 1 takes more bytes than the float 1.0. Why? Try `sys.getsizeof(2**100)` as well. What does that tell you about the largest `int` Python can hold?
