# Hints: 07 - Files, exceptions and tracebacks

Try the task first. Read a hint only when you are stuck.

## Hint for task 1

The last line of the traceback names the problem. A name can only be used after you have assigned a value to it.

## Hint for task 2

Wrap `float(row["pressure_bar"])` in `try:` and add the number to `pressures_bar` there. In the `except ValueError:` branch, add 1 to `skipped`. The mean is `round(sum(pressures_bar) / len(pressures_bar), 2)`.
