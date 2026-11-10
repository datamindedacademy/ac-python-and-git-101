# 02 - Variables and types

Time: about 15 minutes.

## Goal

Store values in variables, know their types, convert between types and units, and print nice messages with f-strings.

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

Open `exercises/python/02-variables-and-types/units.py` and do the TODOs from 1 to 7. Run it after every step:

```powershell
uv run python exercises/python/02-variables-and-types/units.py
```

Then do task 8 in a new file `ask.py` in the same folder:

8. Ask the user for a pressure with `input()` and convert it. `input()` always returns text, so you must convert it with `float()`.

   ```python
   text = input("Pressure in bar: ")
   ```

   Print the pressure in psi. Run it with `uv run python exercises/python/02-variables-and-types/ask.py` and type `7.5` when it asks.

## Check yourself

The main script should print this (with your own TODO 1 and 5 output added):

```text
CB-0042 <class 'str'>
Pressure in psi: 108.7785
Temperature in K: 355.15
Unit CB-0042 runs at 7.50 bar and 82.0 C
Corrected: 8.0
Alarm: False
```

Hint: `82 + 273.15` may show tiny extra digits like `355.15`. That is normal for floats.

## Stretch

- Run `print(0.1 + 0.2)`. Why is it not exactly `0.3`? (Floats are stored in binary. Small rounding errors are normal. Use `round()` when printing.)
- Convert the temperature to degrees Fahrenheit: `c * 9 / 5 + 32`.
