# 04 - Control flow

**Words to use:** condition, comparison operator, branch, for loop, iteration, indentation, enumerate, list comprehension.

## Goal

Make decisions with `if`, repeat work with `for` (and `while`), count readings that are outside the limits, and build a list of them with a loop and with a list comprehension.

## Why this matters

A loop with a condition is the core of nearly every automation script: go over all readings, files or runs and act on some of them. List comprehensions are what you will meet most in code from colleagues and from Copilot, so you need to read them fluently.

## Background

- **Control flow** is how your program decides what to run and how often.
- `if`, `elif` and `else` choose one path. Python checks the conditions from top to bottom and runs the first one that is true.
- **Comparison** operators: `>`, `<`, `>=`, `<=`, `==` (equal), `!=` (not equal). Combine with `and`, `or` and `not`.
- A `for` loop takes the items of a collection one by one:

  ```python
  for name in names:
      print("Hello", name)
  ```

  `range(10, 13)` gives 10, 11, 12 (the stop number is not included). `enumerate(names)` gives the position and the item together, and `enumerate(names, start=1)` starts counting at 1.
- A `while` loop repeats as long as a condition is true. Take care: if the condition never becomes false, the loop never ends. Press `Ctrl+C` to stop it.
- **Indentation** (4 spaces) is part of the syntax. Everything indented under `if` or `for` belongs to it.
- `break` leaves a loop. `continue` jumps to the next item.
- A **list comprehension** builds a list in one line. `[t for t in temperatures_c if t > 90]` gives the same list as this loop:

  ```python
  hot = []
  for t in temperatures_c:
      if t > 90:
          hot.append(t)
  ```

  The rule: one `for`, one `if`. Anything more, write the loop.

## Tasks

Open `exercises/python/04-control-flow/alarms.py` and do TODO 1, 2, 4, 5 and 8. Each TODO says which result to reach. Try it with the hint closed first. Open the hint only when you are stuck. Run it often:

```powershell
uv run python exercises/python/04-control-flow/alarms.py
```

<details>
<summary>Hint for TODO 1</summary>

Use `if`, `elif` and `else`. Check the highest limit first. Print one word in each branch.

</details>

<details>
<summary>Hint for TODO 2</summary>

Use a `for` loop over `pressures_bar`, with the `if/elif/else` from TODO 1 inside it. Build the line with an f-string.

```python
for pressure in pressures_bar:
    ...
```

</details>

<details>
<summary>Hint for TODO 4</summary>

`enumerate()` gives the number and the value together. It can start counting at 1 with `start=1`.

```python
for number, pressure in enumerate(pressures_bar, start=1):
    ...
```

</details>

<details>
<summary>Hint for TODO 5</summary>

Loop over the readings, test each one with `if`, and add 1 to `alarm_count` when it is above the limit. `x += 1` adds 1 to `x`.

</details>

<details>
<summary>Hint for TODO 8</summary>

For the loop version, start from the empty list and use `.append()` inside an `if`. The one-line version has the pattern `[... for p in pressures_bar if ...]`.

</details>

## Check yourself

With TODO 1, 2, 4, 5 and 8 done, you should see these results among your prints. TODO 1 prints `WARNING` for 8.1:

```text
WARNING
8.1 bar -> WARNING
8.7 bar -> ALARM
7.3 bar -> OK
Reading 1: 7.1
Reading 8: 7.3
Alarms: 2
Alarm readings (loop): [8.7, 8.6]
Alarm readings (comprehension): [8.7, 8.6]
```

The loop of TODO 2 prints eight lines, one per reading. The loop of TODO 4 prints eight lines too.

## Optional: if you have time

1. TODO 3 (numbers 1 to 5), TODO 6 (`while`) and TODO 7 (`break` and `continue`) in `alarms.py`. Expected: the numbers 1 to 5 on separate lines, `Minutes to alarm: 4` and `First alarm reading: 8.7`.

   <details>
   <summary>Hint for TODO 3</summary>

   `range(1, 6)` gives 1, 2, 3, 4, 5. The stop number is not included.

   </details>

   <details>
   <summary>Hint for TODO 6</summary>

   `while condition:` repeats its block as long as the condition is true. Make sure something inside the block changes the condition, or the loop never ends. `Ctrl+C` stops it.

   </details>

   <details>
   <summary>Hint for TODO 7</summary>

   `continue` jumps to the next reading. `break` leaves the loop.

   </details>

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
