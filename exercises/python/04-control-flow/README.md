# 04 - Control flow

Core time: 15 minutes. Optional tasks at the end if you have time.

**Words to use:** condition, comparison operator, branch, for loop, while loop, iteration, indentation, enumerate.

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

Open `exercises/python/04-control-flow/alarms.py`, do TODO 1 to 6 and run it often. Skip TODO 3, it is optional:

```powershell
uv run python exercises/python/04-control-flow/alarms.py
```

## Explain it

This is the last core task. Answer each question in one or two sentences, to your neighbour or in writing. You do not need to write code.

1. You used a `for` loop to go over the readings and a `while` loop to count the minutes to the alarm. Why does each loop fit its job? What happens to the `while` loop if the pressure never rises?
2. In your `if/elif/else`, does the order of the conditions matter? What would the script print for 8.7 bar if you checked the warning limit first?

## Check yourself

With TODO 1 to 6 done, you should see these results among your prints:

```text
8.1 bar -> WARNING
Alarms: 2
Minutes to alarm: 4
```

Check the loop in TODO 2: 8.7 bar -> ALARM and 7.3 bar -> OK.

## Optional: if you have time

1. TODO 3 (`range`) and TODO 7 (`break` and `continue`) in `alarms.py`. Expected: `First alarm reading: 8.7`.
2. Make the list of alarm readings with a list comprehension: `[p for p in pressures_bar if p > PRESSURE_ALARM_BAR]`.
3. Print the share of readings in alarm as a percentage with one decimal.

### With Copilot

Select your counting loop from TODO 5 and ask Copilot Chat: *"Count the alarms without an explicit for loop, using `sum()` with a generator expression."* Check that the result is still 2. Which version is easier to verify by reading it? Which one would you choose in a script that a new colleague must maintain?
