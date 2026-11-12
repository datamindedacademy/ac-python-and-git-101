# 05 - Functions and modules

**Words to use:** function, parameter, argument, keyword argument, default value, return value, type hint, docstring, module, import, test, assertion, test-driven development.

## Goal

Write functions in a module until given tests pass, write tests before a function exists, and import the module from a script.

## Why this matters

A function is the unit you can test, reuse and ask Copilot for. A test is how you accept code you did not write yourself.

## Background

- A **function** is a named block of code. You **define** it with `def` and **call** it with its name and brackets.
- **Parameters** are the inputs of a function. **Arguments** are the values you pass in.
- A **default value** makes a parameter optional: `def shorten(text, length=10)`. A call with one argument uses 10.
- A **keyword argument** names the parameter in the call: `shorten(text, length=5)`. It changes one default and leaves the others.
- `return` sends a result back to the caller. A function without `return` gives back `None`. A function can return a tuple: `return 7.5, "bar"`. The caller unpacks it: `value, unit = f(text)`.
- A **type hint** says what a parameter or result should be: `def shorten(text: str, length: int = 10) -> str:`. Python does not check it, readers and Copilot do.
- A **docstring** is a text in triple quotes on the first line of a function. It says what the function does.
- A **module** is a `.py` file with functions. You `import` it in another file.
- A **test** is a small function that calls your code and states what the result must be: `assert kg_to_lb(1) == 2.2046`. This statement is an **assertion**. When it is false, the test fails.
- **pytest** finds the functions named `test_...` and runs them. A failing test is **red**, a passing test **green**. See a red test, write code until it is green, go to the next one.
- **Test-driven development** means you write the test first and the code second. The test says what "correct" means, to you, to a colleague, or to Copilot.
- Compare floats with `pytest.approx(...)`, because `==` can fail on a correct float.
- A function can refuse an input it cannot handle. `raise ValueError("Unknown unit: atm")` stops the function with that error, the same kind of error `float("abc")` gives. A test states that a call must fail like this:

  ```python
  with pytest.raises(ValueError):
      kg_to_lb("heavy")
  ```

  The test passes when the indented line raises a `ValueError`, and fails when it does not.

```python
def kg_to_lb(mass_kg: float) -> float:
    """Convert a mass from kilogram to pound."""
    return mass_kg * 2.2046
```

## How to read a failed test

This is a real failure from this exercise, shortened:

```text
>       assert bench.parse_reading("7.5 bar") == (7.5, "bar")
E       AssertionError: assert (0.0, '') == (7.5, 'bar')
E         At index 0 diff: 0.0 != 7.5

exercises/python/05-functions/test_bench.py:19: AssertionError
========================= 7 failed, 2 passed in 0.03s ==========================
```

The `>` line is the failing assertion. The `E` lines give actual versus expected. The last line is the score. Read from the bottom up, like the tracebacks of exercise 07.

## Tasks

Tasks 1 and 2 use the files in `exercises/python/05-functions`. Task 3 uses new files in the same folder.

### Task 1: red to green

Run the tests and read the failures:

```powershell
uv run pytest exercises/python/05-functions
```

Then complete `parse_reading` and `summarize` in `bench.py`. `to_bar` is done as an example. The tests are the specification. Run them until they all pass.

```text
============================== 9 passed in 0.03s ===============================
```

### Task 2: test first, then a script that uses the module

**Part A.** A function `classify(pressure_bar, warning_bar=8.0, alarm_bar=8.5)` does not exist yet. It returns `"OK"`, `"WARNING"` or `"ALARM"`. A pressure at or above a limit counts as that level.

In `test_bench.py`, write at least four tests for it first. Cover both boundaries and one call with a keyword argument that changes a limit. See them fail. Then write `classify` in `bench.py` until they pass.

**Part B.** Open `report.py`. Write a `main()` that uses all four functions of `bench.py` on `readings`: parse each reading, convert it to bar, summarize the values, classify the highest one. Import the functions, do not copy them. Importing `report` must print nothing. Run it:

```powershell
uv run python exercises/python/05-functions/report.py
```

```text
Readings: 5
Min: 7.1 bar
Max: 8.7 bar
Mean: 7.62 bar
Median: 7.5 bar
Status: ALARM
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
