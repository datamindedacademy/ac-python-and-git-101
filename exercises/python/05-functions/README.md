# 05 - Functions and modules

Core time: 20 minutes. Optional tasks at the end if you have time.

**Words to use:** function, parameter, argument, default value, return value, docstring, module, import.

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

1. Open `exercises/python/05-functions/conversions.py`. Complete three functions (TODO 1, 2 and 4). `l_s_to_m3_h` is already done as an example. Read the docstrings.
2. Run the file directly. It should print one line.

   ```powershell
   uv run python exercises/python/05-functions/conversions.py
   ```

3. Open `report.py`. Import the functions (TODO 5) and fill in the report. Run it:

   ```powershell
   uv run python exercises/python/05-functions/report.py
   ```

4. Back in `conversions.py`, add the self-test under `if __name__ == "__main__":` (TODO 6). Run `conversions.py` again, then run `report.py` again. Does the self-test also run when you import? It should not.

## Explain it

This is the last core task. Answer each question in one or two sentences, to your neighbour or in writing. You do not need to write code.

1. What do you gain by moving the conversions into `conversions.py`? What does it cost?
2. What is the difference between a function that prints its result and a function that returns it? Which of the two can `report.py` reuse?

## Check yourself

`report.py` should print:

```text
Average pressure (bar): 7.33
Average pressure (psi): 106.31
Temperature (K): 356.65
Flow (m3/h): 149.4
```

## Optional: if you have time

1. Call `average` with and without the `decimals` argument. Also try a **keyword argument**: `average(values, decimals=0)`.
2. Write `psi_to_bar` and check that `psi_to_bar(bar_to_psi(7.5))` gives 7.5 back (use `round`).
3. Make a function `classify(pressure, limit=8.5)` that returns `"ALARM"` or `"OK"`. Use it from exercise 04.

### With Copilot

Ask Copilot Chat: *"What happens when `average` is called with an empty list? Suggest two ways to handle that case."* You will probably get "return a default value such as `None`" and "raise an exception". Which one would you choose for test bench data, and why? Think about which mistake is easier to notice later.
