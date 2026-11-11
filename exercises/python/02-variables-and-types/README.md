# 02 - Variables and types

**Words to use:** variable, assignment, type, int, float, str, f-string, constant.

## Goal

Store values in variables, know their types, convert between types and units, and print nice messages with f-strings.

## Why this matters

Measurement data almost always arrives as text. A value with the wrong type or the wrong unit gives a wrong number, often without any error message. A name that carries the unit, like `pressure_bar`, is the cheapest protection.

## Background

- A **variable** is a name that points to a value: `pressure_bar = 7.5`. Use lower case and underscores (`snake_case`). Put the unit in the name.
- Every value has a **type**. The basic ones:
  - `int`: whole number, like `82`.
  - `float`: number with decimals, like `7.5`.
  - `str`: text, like `"CB-0042"`. Text goes between quotes.
  - `bool`: `True` or `False`.
- `type(x)` tells you the type of `x`.
- **Converting** means changing type: `float("7.8")`, `int(7.9)`, `str(7.9)`.
- An **f-string** puts values inside text: `f"Pressure: {pressure_bar} bar"`. Add `:.2f` to show 2 decimals.
- A name in CAPITALS (like `BAR_TO_PSI`) is a convention for a **constant**: a value that never changes.

## Tasks

Open `exercises/python/02-variables-and-types/units.py` and do TODO 1 to 4. Run it after every step:

```powershell
uv run python exercises/python/02-variables-and-types/units.py
```

## Check yourself

The main script should print this (with your own TODO 1 output added). Output for TODO 5 to 7 appears only after you do the optional tasks:

```text
CB-0042 <class 'str'>
Pressure in psi: 108.7785
Temperature in K: 355.15
Unit CB-0042 runs at 7.50 bar and 82.0 C
```

Hint: floats can show tiny extra digits. That is normal.

## Optional: if you have time

1. TODO 5 to 7 in `units.py`: string methods, convert text to a number, and make a boolean. Expected: `Corrected: 8.0` and `Alarm: False`.
2. In a new file `ask.py` in the same folder, ask the user for a pressure with `input()` and convert it. `input()` always returns text, so you must convert it with `float()`.

   ```python
   text = input("Pressure in bar: ")
   ```

   Print the pressure in psi. Run it with `uv run python exercises/python/02-variables-and-types/ask.py` and type `7.5` when it asks.

3. Run `print(0.1 + 0.2)`. Why is it not exactly `0.3`? (Floats are stored in binary. Small rounding errors are normal. Use `round()` when printing.)
4. Convert the temperature to degrees Fahrenheit: `c * 9 / 5 + 32`.

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

This goes beyond today. Most people cannot answer it yet. Try it anyway, or bring it to the trainer.

`0.1 + 0.2 == 0.3` is `False`, but `0.5 + 0.25 == 0.75` is `True`. Why? What does that mean for a script that checks whether two measured pressures are equal?
