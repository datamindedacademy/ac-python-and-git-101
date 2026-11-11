# Hints: 05 - Functions and modules

Try the task first. Read a hint only when you are stuck.

## Hint for task 1

`bar_to_psi` multiplies by the constant `BAR_TO_PSI`. `celsius_to_kelvin` adds 273.15. `average` divides `sum(values)` by `len(values)` and passes the result to `round()` with `decimals` as second argument.

## Hint for task 2

A test is a function whose name starts with `test_`. Its body is an `assert` that compares the function result with the expected number, using `pytest.approx(...)`. One known value: 14.5038 psi is 1 bar. In `report.py`, `from conversions import name_one, name_two` makes functions from the module available. The psi value starts from the average in bar.
