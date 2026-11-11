# 05 - Functions and modules

**Words to use:** function, parameter, argument, default value, return value, docstring, module, import, test, assertion, test-driven development.

## Goal

Write your own functions in a module, let tests tell you when they are correct, and import the module from a script.

## Why this matters

A function is the unit you can test, reuse and ask Copilot for. A test is how you accept code you did not write yourself: it states what correct means before the code exists.

## Background

- A **function** is a named block of code you can run many times. You **define** it with `def` and **call** it with its name and brackets.
- **Parameters** are the inputs of a function. **Arguments** are the values you pass in.
- A **default value** makes a parameter optional: `def shorten(text, length=10)`. A call with one argument uses 10.
- `return` sends a result back to the caller. A function without `return` gives back `None`.
- A **docstring** is a text in triple quotes on the first line of a function. It explains what the function does.
- A **module** is a `.py` file with functions. You `import` it to use its functions in another file.
- A **test** is a small function that calls your code and states what the result must be. The statement is an **assertion**: `assert kg_to_lb(1) == 2.2046`. When the assertion is false, the test fails.
- **pytest** is the tool that finds the functions named `test_...` and runs them. A failing test is called **red**, a passing test **green**. You work in a loop: see a red test, write code until it is green, then go to the next one.
- **Test-driven development** means that you write the test first and the code second. The test says precisely what "correct" means, to you, to a colleague, or to Copilot.
- The tests compare floats with `pytest.approx(...)`, because floats have tiny rounding errors and `==` can fail on a correct result.

```python
def kg_to_lb(mass_kg):
    """Convert a mass from kilogram to pound."""
    return mass_kg * 2.2046
```

## How to read a failed test

This is a real failure from this exercise, shortened:

```text
>       assert conversions.bar_to_psi(1) == pytest.approx(14.5038)
E       assert 0.0 == 14.5038 ± 1.5e-05
E         Obtained: 0.0
E         Expected: 14.5038 ± 1.5e-05

exercises/python/05-functions/test_conversions.py:24: AssertionError
========================= 4 failed, 1 passed in 0.05s ==========================
```

The header line above it names the test. The line marked `>` is the failing assertion, with its file and line number below. The `E` lines give expected versus actual. The last line is the score. Read from the bottom up, like the tracebacks of exercise 07.

## Tasks

Everything for tasks 1 and 2 is in `exercises/python/05-functions`. Task 3 uses new files in the same folder.

### Task 1: red to green

Run the tests and read the failures.

```powershell
uv run pytest exercises/python/05-functions
```

Then complete `bar_to_psi`, `celsius_to_kelvin` and `average` in `conversions.py`. `l_s_to_m3_h` is done as an example. The tests say what is expected. Run them until they all pass.

```text
============================== 5 passed in 0.03s ===============================
```

### Task 2: test first, then use the module

You need a function `psi_to_bar`. It does not exist yet. In `test_conversions.py`, write `test_psi_to_bar` first and see it fail. Then write the function in `conversions.py` until all 6 tests pass.

```text
============================== 6 passed in 0.03s ==============================
```

Then open `report.py`. Import the functions from `conversions` and fill in the four prints. Run it:

```powershell
uv run python exercises/python/05-functions/report.py
```

```text
Average pressure (bar): 7.33
Average pressure (psi): 106.31
Temperature (K): 356.65
Flow (m3/h): 149.4
```

### Task 3: one convert function

This one is much harder.

Write a function `convert(value, from_unit, to_unit)` in a new file `units.py`, with its tests in a new file `test_units.py`, both in `exercises/python/05-functions`. Write the tests first. Run them with:

```powershell
uv run pytest exercises/python/05-functions/test_units.py
```

The units are `bar`, `psi` and `kPa` (pressure) and `degC`, `K` and `degF` (temperature). Running `units.py` itself must print:

```text
108.7785
212.0
-273.15
```

Those are `convert(7.5, "bar", "psi")`, `convert(100, "degC", "degF")` and `convert(0, "K", "degC")`, each rounded to 4 decimals.

Rules:

- One lookup dict for all units. No chain of `if`s over unit names.
- An unknown unit raises `ValueError`. Converting between a pressure unit and a temperature unit raises `ValueError` too. Test both with `pytest.raises`.
- Write a round trip test: `convert(convert(x, a, b), b, a)` gives `x` with `pytest.approx`, for every pair of units of the same family.

## Open question

Write `def add_reading(value, readings=[]):` with a body that appends `value` to `readings` and returns `readings`. Call it three times with only the first argument. Explain the third result. What does this tell you about when Python evaluates a default value?
