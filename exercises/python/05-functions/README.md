# 05 - Functions and modules

**Words to use:** function, parameter, argument, default value, return value, docstring, module, import, test, assertion, test-driven development.

## Goal

Write your own functions in a module, let tests tell you when they are correct, and import the module from a script.

## Why this matters

A function is the unit you can test, reuse and ask Copilot for. A test is how you accept code you did not write yourself: it states what correct means before the code exists.

## Background

- A **function** is a named block of code you can run many times. You **define** it with `def` and **call** it with its name and brackets.
- **Parameters** are the inputs of a function. **Arguments** are the values you pass in.
- A **default value** makes a parameter optional: `def average(values, decimals=2)`.
- `return` sends a result back to the caller. A function without `return` gives back `None`.
- A **docstring** is a text in triple quotes on the first line of a function. It explains what the function does.
- A **module** is a `.py` file with functions. You `import` it to use its functions in another file.
- A **test** is a small function that calls your code and states what the result must be. The statement is an **assertion**: `assert bar_to_psi(1) == 14.5038`. When the assertion is false, the test fails.
- **pytest** is the tool that finds the functions named `test_...` and runs them. A failing test is called **red**, a passing test **green**. You work in a loop: see a red test, write code until it is green, then go to the next one.
- **Test-driven development** means that you write the test first and the code second. The test says precisely what "correct" means, to you, to a colleague, or to Copilot.
- The tests compare floats with `pytest.approx(...)`, because floats have tiny rounding errors and `==` can fail on a correct result.

```python
def bar_to_psi(pressure_bar):
    """Convert a pressure from bar to psi."""
    return pressure_bar * 14.5038
```

## How to read a failed test

pytest prints a lot. You need four things. This is a real failure from this exercise, shortened:

```text
exercises/python/05-functions/test_conversions.py .FFFF                  [100%]

_______________________________ test_bar_to_psi ________________________________

    def test_bar_to_psi():
>       assert conversions.bar_to_psi(1) == pytest.approx(14.5038)
E       assert 0.0 == 14.5038 ± 1.5e-05
E         Obtained: 0.0
E         Expected: 14.5038 ± 1.5e-05

exercises/python/05-functions/test_conversions.py:24: AssertionError
========================= 4 failed, 1 passed in 0.05s ==========================
```

1. **Which test**: the name in the header line, `test_bar_to_psi`.
2. **Which line**: the line marked with `>`, and the file and line number below it (`test_conversions.py:24`).
3. **Expected versus actual**: the lines that start with `E`. The function gave `0.0`, the test expected `14.5038`.
4. **The score**: the last line. `.FFFF` at the top says the same: one dot per passed test, one `F` per failed test.

Read from the bottom up, like the tracebacks you will meet in exercise 07.

## Tasks

1. **Red.** Run the tests and read the output. Do not change any code yet.

   ```powershell
   uv run pytest exercises/python/05-functions
   ```

   Four tests fail and one passes. For `test_average`, find the line number, the expected value and the actual value. Open `test_conversions.py` and read that test.

2. **Green.** Open `conversions.py`. `l_s_to_m3_h` is already done as an example. Complete `bar_to_psi`, `celsius_to_kelvin` and `average` (TODO 1 to 3). Run the tests after each function, until you see `5 passed`.

3. **Test first.** You need a function `psi_to_bar`. It does not exist yet. Do TODO 4 in this order:
   1. In `test_conversions.py`, write `test_psi_to_bar`. Decide what the function must return for 14.5038 psi.
   2. Run the tests. Your new test must fail (red), with an `AttributeError`: the function is not there.
   3. Now write `psi_to_bar` in `conversions.py` and run the tests until you see `6 passed`.

4. **Use the module.** Open `report.py`. Import the functions (TODO 5) and fill in the report. Run it:

   ```powershell
   uv run python exercises/python/05-functions/report.py
   ```

## Check yourself

The tests end with:

```text
============================== 6 passed in 0.03s ===============================
```

`report.py` should print:

```text
Average pressure (bar): 7.33
Average pressure (psi): 106.31
Temperature (K): 356.65
Flow (m3/h): 149.4
```

## Optional: if you have time

1. Break `bar_to_psi` on purpose (multiply by 14 instead of `BAR_TO_PSI`) and run the tests. Which test catches it? Repair it again.
2. Call `average` with and without the `decimals` argument. Also try a **keyword argument**: `average(values, decimals=0)`.
3. What is the difference between a function that prints its result and a function that returns it? Which of the two can a test check?
4. Test first again: write a test for `classify(pressure, limit=8.5)`, which returns `"ALARM"` or `"OK"`. Then write the function.
5. Add this block at the end of `conversions.py` and run the file directly with `uv run python exercises/python/05-functions/conversions.py`. Then run `report.py`. The block runs only when you run the file itself, not when you import it.

   ```python
   if __name__ == "__main__":
       print(bar_to_psi(7.5))
   ```

### With Copilot

Do this with a function that does not exist yet, for example `kelvin_to_celsius`. Write the test yourself first. Then select the failing test and ask Copilot Chat: *"Write the function in `conversions.py` that makes this test pass."* Run the tests. Green? Now ask: *"Write a second test for this function that covers an edge case: a negative value, zero, or a string as argument."* Read that test before you run it. Does it describe behaviour you actually want? For example: must a temperature below 0 K raise an exception, or is that not the job of a conversion function? Keep the test only if you agree with what it demands.

## Challenge

For those who finish early. There are no TODOs and no hints.

Test first. In a new test file, write tests for a function `convert(value, from_unit, to_unit)`. Then write the function in `conversions.py`. It converts between the units `bar`, `psi` and `kPa`. For example, `convert(7.5, "bar", "psi")` gives `108.7785`.

- Use one lookup dict. No chain of `if`s.
- An unknown unit raises `ValueError`. Test that with `pytest.raises`.

## Open question

This goes beyond today. Most people cannot answer it yet. Try it anyway, or bring it to the trainer.

Write `def add_reading(value, readings=[]):` with a body that appends `value` to `readings` and returns `readings`. Call it three times with only the first argument. Explain the third result. What does this tell you about when Python evaluates a default value?
