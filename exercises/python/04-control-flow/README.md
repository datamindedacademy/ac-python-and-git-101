# 04 - Control flow

**Words to use:** condition, comparison operator, branch, for loop, iteration, indentation, enumerate, list comprehension.

## Goal

Make decisions with `if`, repeat work with `for`, count readings that are outside the limits, and build lists with list comprehensions.

## Why this matters

A loop with a condition is the core of nearly every automation script: go over all readings, files or runs and act on some of them. List comprehensions are what you will meet most in code from colleagues and from Copilot, so you need to read them fluently.

## Background

- `if`, `elif` and `else` choose one path. Python checks the conditions from top to bottom and runs the first one that is true.
- **Comparison** operators: `>`, `<`, `>=`, `<=`, `==` (equal), `!=` (not equal). Combine with `and`, `or` and `not`.
- A `for` loop takes the items of a collection one by one:

  ```python
  for name in names:
      print("Hello", name)
  ```

  `enumerate(names)` gives the position and the item together, and `enumerate(names, start=1)` starts counting at 1.
- **Indentation** (4 spaces) is part of the syntax. Everything indented under `if` or `for` belongs to it.
- A **list comprehension** builds a list in one line. `[t for t in temperatures_c if t > 90]` gives the same list as this loop:

  ```python
  hot = []
  for t in temperatures_c:
      if t > 90:
          hot.append(t)
  ```

  Without the `if` part it converts every item: `[t * 2 for t in temperatures_c]`.

## Tasks

Open `exercises/python/04-control-flow/alarms.py`. There are three tasks. Each one states the output to reach. Run with:

```powershell
uv run python exercises/python/04-control-flow/alarms.py
```

### Task 1: classify every reading

Go over `pressures_bar`. For each reading print its number (counting from 1), the value and its class: ALARM above `PRESSURE_ALARM_BAR`, WARNING above `PRESSURE_WARNING_BAR`, OK otherwise. After the loop print the number of alarms.

```text
Reading 1: 7.1 bar -> OK
Reading 2: 7.6 bar -> OK
Reading 3: 8.1 bar -> WARNING
Reading 4: 8.4 bar -> WARNING
Reading 5: 8.7 bar -> ALARM
Reading 6: 7.9 bar -> OK
Reading 7: 8.6 bar -> ALARM
Reading 8: 7.3 bar -> OK
Alarms: 2
```

### Task 2: list comprehensions

Build two lists, each with one list comprehension: the readings above `PRESSURE_ALARM_BAR`, and all readings converted from bar to psi (1 bar is 14.5038 psi), rounded to 1 decimal.

```text
Alarm readings: [8.7, 8.6]
In psi: [103.0, 110.2, 117.5, 121.8, 126.2, 114.6, 124.7, 105.9]
```

### Task 3: alarm episodes

This one is much harder.

`trend_bar` holds 14 readings. An **episode** is a run of consecutive readings above `PRESSURE_WARNING_BAR`. Print every episode with the numbers of its first and last reading (counting from 1), its length and its highest value. Then print the longest episode.

```text
Episode 1: readings 2 to 4, length 3, peak 8.3
Episode 2: readings 6 to 6, length 1, peak 8.4
Episode 3: readings 8 to 11, length 4, peak 8.9
Episode 4: readings 13 to 14, length 2, peak 8.5
Longest: readings 8 to 11, 4 readings
```

Rules:

- Find the episodes in one `for` loop over the readings, with `enumerate`. No `import`.
- It must also work when the last reading is above the limit.
- For a list of your own with no episode at all, it prints `No episodes` and nothing else.

## Open question

Take your list comprehension and replace the square brackets with round ones. Print the result. What did you get? Why would that difference matter for a log with ten million rows?
