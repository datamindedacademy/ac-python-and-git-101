# Hints: 04 - Control flow

Try the task first. Read a hint only when you are stuck.

## Hint for task 1

`for number, pressure in enumerate(pressures_bar, start=1):` gives the number and the value. Inside, check the alarm limit first with `if`, then `elif` for the warning limit, then `else`. Add 1 to a counter in the alarm branch.

## Hint for task 2

The first list has the pattern `[p for p in pressures_bar if ...]`. The second has no `if`, and puts the calculation in front of `for`: `[round(p * 14.5038, 1) for p in pressures_bar]`.
