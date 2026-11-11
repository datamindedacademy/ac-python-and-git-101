# 03 - Collections

**Words to use:** list, tuple, dict, key, value, index, slice, method.

## Goal

Store many values together with lists, tuples, dicts and sets. Pick items by index, slice and sort lists, change dicts, and count unique values, all without a loop.

## Why this matters

The structure you pick decides how the rest of the script reads. A CSV file becomes a list of dicts and a JSON file becomes dicts and lists. The data tables of day 2 build on the same ideas.

## Background

A **collection** holds several values in one variable.

| Type | Looks like | Ordered | Can change | Use it for |
|---|---|---|---|---|
| `list` | `[7.1, 7.3]` | yes | yes | a series of readings |
| `tuple` | `(52.01, 4.36)` | yes | no | a fixed group, like coordinates |
| `dict` | `{"pressure_bar": 7.5}` | yes | yes | named fields of one thing |
| `set` | `{"P1", "T1"}` | no | yes | unique values |

- An **index** is the position of an item. Python starts counting at **0**. `-1` is the last item, `-2` the one before it.
- A **slice** takes part of a list: `letters[1:4]` gives items 1, 2 and 3. The stop index is not included. Leave a side empty to go to that end: `letters[:2]` is the first two. Negative numbers count from the end, so a slice can drop both ends: `letters[1:-1]` for `["a", "b", "c", "d"]` gives `["b", "c"]`.
- A **method** is a function that belongs to a value. A list has `.append(x)` to add an item at the end.
- `len(x)`, `sum(x)`, `max(x)` and `min(x)` work on a whole list.
- `sorted(values)` gives a new list from low to high. `sorted(values, reverse=True)` goes from high to low. The original list does not change.
- A dict looks up a value by **key**: `measurement["pressure_bar"]`. Assigning to a key that does not exist adds it. Assigning to a key that exists changes it. A key that does not exist gives a `KeyError` when you read it.
- A list of dicts is indexed twice: first the position in the list, then the key. A negative index works here as well.
- `a, b = pair` **unpacks** a tuple or list with two items into two variables.
- A **set** keeps each value once. `set(values)` turns a list into a set, and `len()` of it counts the unique values. `"x" in collection` is `True` when `"x"` is one of the items.

## Tasks

Open `exercises/python/03-collections/collections_intro.py` and do TODO 1 to 11. Each TODO says which result to reach. Try it with the hint closed first. Open the hint only when you are stuck. You do not need a loop for any of them. Run after each step:

```powershell
uv run python exercises/python/03-collections/collections_intro.py
```

Tip: you can also try things quickly in the REPL with `uv run python`.

<details>
<summary>Hint for TODO 1</summary>

Use the index `-1`.

</details>

<details>
<summary>Hint for TODO 2</summary>

Use a slice. The stop index is not included.

</details>

<details>
<summary>Hint for TODO 3</summary>

Use the list method `.append()`, then `len()`.

</details>

<details>
<summary>Hint for TODO 4</summary>

Use `max()`, `min()`, `sum()` and `len()`. The mean is the sum divided by the count.

</details>

<details>
<summary>Hint for TODO 5</summary>

Sort with `sorted(..., reverse=True)`, then take a slice from the start.

</details>

<details>
<summary>Hint for TODO 6</summary>

Sort the list from low to high. A slice that starts at 1 and stops at -1 drops the lowest and the highest. Then take the mean of what is left and round it with `round(x, 3)`.

```python
middle = sorted(pressures_bar)[1:-1]
```

</details>

<details>
<summary>Hint for TODO 7</summary>

Write two names on the left of one `=`, separated by a comma.

</details>

<details>
<summary>Hint for TODO 8</summary>

Assign to a key with `measurement["key"] = value`. A new key is added, an existing key is changed. Then print `measurement`.

</details>

<details>
<summary>Hint for TODO 9</summary>

Index twice: the position in the list, then the key. The second measurement has index 1. The last one has index `-1`.

</details>

<details>
<summary>Hint for TODO 10</summary>

Use `.append()` with a new dict that has the same three keys as the others.

</details>

<details>
<summary>Hint for TODO 11</summary>

Use `set()` and `len()` for the count, and `in` for the second line.

</details>

## Check yourself

Among your other prints you should see:

```text
First: 7.1
Last: 7.5
First three: [7.1, 7.3, 7.4]
Number of readings: 7
Max: 7.8 Min: 7.1 Mean: 7.414285714285714
Top three: [7.8, 7.6, 7.5]
Trimmed mean: 7.4
Latitude: 52.01 Longitude: 4.36
Pressure: 7.5
{'timestamp': '2026-01-15 09:00:00', 'pressure_bar': 7.5, 'temperature_c': 83.5, 'flow_l_s': 41.5}
Temperature of second: 81.9
Pressure of last: 7.6
Number of measurements: 4
Unique sensors: 4
F1 present: True
```

## Optional: if you have time

1. Print every key and value of `measurement`, one per line. Loop over `measurement.items()`. Loops are the topic of exercise 04, so look at that exercise first, or ask Copilot to explain the loop.
2. Build a list with only the pressures from `measurements`. Start with an empty list `[]`, then loop and `.append()`.
3. Use `measurement.get("humidity", "unknown")`. How is it different from `measurement["humidity"]`?
4. In the REPL, try `position[0] = 0.0` and read the error. Why can a tuple not change?
5. Make a list of the pressures above 7.3 with a **list comprehension**: `[p for p in pressures_bar if p > 7.3]`. Exercise 04 covers comprehensions properly.

### With Copilot

Do optional task 2 first. Then select your `for` loop with `.append()` and ask Copilot Chat: *"Rewrite this loop as a list comprehension."* Run both versions and check that they give the same list. Which version would you rather find in a colleague's script, and why?

## Challenge

For those who finish early. There are no TODOs and no hints.

You have the list of dicts `measurements` in `collections_intro.py`. Build a new dict that maps each key (`timestamp`, `pressure_bar`, `temperature_c`) to the list of its values over all measurements, and print it. Expected output starts like this:

```text
{'timestamp': ['09:00', '09:01', '09:02', '09:03'], 'pressure_bar': [7.1, 7.4, 7.6, 7.3], ...}
```

Do not type the three key names in your code. It must also work for a measurement with more keys.

## Open question

This goes beyond today. Most people cannot answer it yet. Try it anyway, or bring it to the trainer.

Run `a = [1, 2, 3]`, then `b = a`, then `b.append(4)`, and print `a`. Why did `a` change? And why can a tuple be a key in a dict, while a list cannot?
