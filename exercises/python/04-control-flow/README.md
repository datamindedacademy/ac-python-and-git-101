# 04 - Control flow

Core time: 15 minutes. Optional tasks at the end if you have time.

## Goal

Make decisions with `if`, repeat work with `for` and `while`, and count readings that are outside the limits.

## Background

- **Control flow** is how your program decides what to run and how often.
- `if`, `elif` and `else` choose one path. Python checks the conditions from top to bottom and runs the first one that is true.
- **Comparison** operators: `>`, `<`, `>=`, `<=`, `==` (equal), `!=` (not equal). Combine with `and`, `or` and `not`.
- A `for` loop takes the items of a collection one by one. `range(1, 6)` gives 1, 2, 3, 4, 5.
- A `while` loop repeats as long as a condition is true. Take care: if the condition never becomes false, the loop never ends. Press `Ctrl+C` to stop it.
- **Indentation** (4 spaces) is part of the syntax. Everything indented under `if` or `for` belongs to it.
- `break` leaves a loop. `continue` jumps to the next item.

## Tasks

Open `exercises/python/04-control-flow/alarms.py`, do TODO 1 to 6 and run it often:

```powershell
uv run python exercises/python/04-control-flow/alarms.py
```

## Check yourself

With TODO 1 to 6 done, you should see these results among your prints:

```text
8.1 bar -> WARNING
Alarms: 2
Minutes to alarm: 4
```

Check the loop in TODO 2: 8.7 bar -> ALARM and 7.3 bar -> OK.

## Optional: if you have time

1. TODO 7 in `alarms.py`: `break` and `continue`. Expected: `First alarm reading: 8.7`.
2. Make the list of alarm readings with a list comprehension: `[p for p in pressures_bar if p > PRESSURE_ALARM_BAR]`.
3. Print the share of readings in alarm as a percentage with one decimal.
