# 05 - Functions and modules

Time: about 25 minutes.

## Goal

Write your own functions, put them in a module, and import them from a script.

## Background

- A **function** is a named block of code you can run many times. You **define** it with `def` and **call** it with its name and brackets.
- **Parameters** are the inputs of a function. **Arguments** are the values you pass in.
- A **default value** makes a parameter optional: `def average(values, decimals=2)`.
- `return` sends a result back to the caller. A function without `return` gives back `None`.
- A **docstring** is a text in triple quotes on the first line of a function. It explains what the function does.
- A **module** is a `.py` file with functions. You `import` it to use its functions in another file.
- `if __name__ == "__main__":` is a block that runs only when you run the file directly. It does not run on import. Use it for quick tests.

```python
def bar_to_psi(pressure_bar):
    """Convert a pressure from bar to psi."""
    return pressure_bar * 14.5038
```

## Tasks

1. Open `exercises/python/05-functions/conversions.py`. Complete the four functions (TODO 1 to 4). Read the docstrings.
2. Run the file directly. It should print one line.

   ```powershell
   uv run python exercises/python/05-functions/conversions.py
   ```

3. Open `report.py`. Import the functions (TODO 5) and fill in the report. Run it:

   ```powershell
   uv run python exercises/python/05-functions/report.py
   ```

4. Back in `conversions.py`, add the self-test under `if __name__ == "__main__":` (TODO 6). Run `conversions.py` again, then run `report.py` again. Does the self-test also run when you import? It should not.
5. Call `average` with and without the `decimals` argument. Also try a **keyword argument**: `average(values, decimals=0)`.

## Check yourself

`report.py` should print:

```text
Average pressure (bar): 7.33
Average pressure (psi): 106.31
Temperature (K): 356.65
Flow (m3/h): 149.4
```

## Stretch

- Write `psi_to_bar` and check that `psi_to_bar(bar_to_psi(7.5))` gives 7.5 back (use `round`).
- Make a function `classify(pressure, limit=8.5)` that returns `"ALARM"` or `"OK"`. Use it from exercise 04.
