# 04 - Control flow

**Words to use:** condition, comparison operator, branch, for loop, while loop, iteration, indentation, enumerate, list comprehension.

## Goal

Make decisions with `if`, repeat work with `for` and `while`, count readings that are outside the limits, and build a list of them with a loop and with a list comprehension.

## Why this matters

A loop with a condition is the core of nearly every automation script: go over all readings, files or runs and act on some of them. List comprehensions are what you will meet most in code from colleagues and from Copilot, so you need to read them fluently.

## Background

- **Control flow** is how your program decides what to run and how often.
- `if`, `elif` and `else` choose one path. Python checks the conditions from top to bottom and runs the first one that is true.
- **Comparison** operators: `>`, `<`, `>=`, `<=`, `==` (equal), `!=` (not equal). Combine with `and`, `or` and `not`.
- A `for` loop takes the items of a collection one by one. `range(1, 6)` gives 1, 2, 3, 4, 5.
- A `while` loop repeats as long as a condition is true. Take care: if the condition never becomes false, the loop never ends. Press `Ctrl+C` to stop it.
- **Indentation** (4 spaces) is part of the syntax. Everything indented under `if` or `for` belongs to it.
- `break` leaves a loop. `continue` jumps to the next item.
- A **list comprehension** builds a list in one line. `[p for p in pressures_bar if p > 8.5]` gives the same list as this loop:

  ```python
  high = []
  for p in pressures_bar:
      if p > 8.5:
          high.append(p)
  ```

  The rule: one `for`, one `if`. Anything more, write the loop.

## Tasks

Open `exercises/python/04-control-flow/alarms.py`, do TODO 1 to 6 and TODO 8, and run it often. Skip TODO 3, it is optional:

```powershell
uv run python exercises/python/04-control-flow/alarms.py
```

## Check yourself

With TODO 1 to 6 and 8 done, you should see these results among your prints:

```text
8.1 bar -> WARNING
Alarms: 2
Minutes to alarm: 4
Alarm readings (loop): [8.7, 8.6]
Alarm readings (comprehension): [8.7, 8.6]
```

Check the loop in TODO 2: 8.7 bar -> ALARM and 7.3 bar -> OK.

## Optional: if you have time

1. TODO 3 (`range`) and TODO 7 (`break` and `continue`) in `alarms.py`. Expected: `First alarm reading: 8.7`.
2. Print the share of readings in alarm as a percentage with one decimal.

### With Copilot

Select your counting loop from TODO 5 and ask Copilot Chat: *"Count the alarms without an explicit for loop, using `sum()` with a generator expression."* Check that the result is still 2. Which version is easier to verify by reading it? Which one would you choose in a script that a new colleague must maintain?

## Challenge

For those who finish early. There are no TODOs and no hints.

Find the first position in `pressures_bar` where three readings in a row are all above `PRESSURE_WARNING_BAR`. Print the number of the first of the three readings (counting from 1), or a message when it never happens. With the list in `alarms.py` the expected output is:

```text
Three readings in a row above 8.0 bar start at reading 3
```

Also test it with a list of your own where the answer is "never", and with one where the run is at the very end.

## Open question

This goes beyond today. Most people cannot answer it yet. Try it anyway, or bring it to the trainer.

Take your list comprehension and replace the square brackets with round ones. Print the result. What did you get? Why would that difference matter for a log with ten million rows?
