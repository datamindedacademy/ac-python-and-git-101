# 03 - Collections

**Words to use:** list, tuple, dict, set, key, value, index, slice, split, unpack, method.

## Goal

Store many values together with lists, tuples, dicts and sets. Pick items by index, slice and sort lists, cut a line of text into a list, change dicts, and count unique values, all without a loop.

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
- `round(x, 3)` rounds a number to 3 decimals.
- `sorted(values)` gives a new list from low to high. `sorted(values, reverse=True)` goes from high to low. The original list does not change.
- A dict looks up a value by **key**: `measurement["pressure_bar"]`. Assigning to a key that does not exist adds it. Assigning to a key that exists changes it. A key that does not exist gives a `KeyError` when you read it.
- `7 // 2` is integer division: it gives `3`, without the remainder.
- A list of dicts is indexed twice: first the position in the list, then the key. A negative index works here as well.
- `a, b = pair` **unpacks** a tuple or list with two items into two variables. It works for any number of items, as long as the number of names is the same.
- `text.split()` cuts a text at the spaces and gives a list of the parts: `"12 kg".split()` is `["12", "kg"]`. Every part is still text. `text.split(",")` cuts at each comma instead.
- A **set** keeps each value once. `set(values)` turns a list into a set, and `len()` of it counts the unique values. `"x" in collection` is `True` when `"x"` is one of the items.

## Tasks

Open `exercises/python/03-collections/collections_intro.py`. There are three tasks. Each one states the output to reach. No task needs a loop or an `if`. Run with:

```powershell
uv run python exercises/python/03-collections/collections_intro.py
```

### Task 1: lists

From `pressures_bar`, print the last reading, the three highest readings (highest first) and the trimmed mean: the mean without the single highest and the single lowest reading, rounded to 3 decimals. The code must still be right when the list gets longer.

```text
Last: 7.5
Top three: [7.6, 7.5, 7.4]
Trimmed mean: 7.35
```

### Task 2: dicts, tuples and sets

`reading_line` is one line from a sensor log, with the fields separated by `;`. Add it to `measurements` as a fourth measurement, with the same keys and the same types as the other three. Do not type its values, take them from `reading_line`. Then print the number of measurements, the pressure of the last one, the number of unique values in `sensor_ids`, and the position of the hall.

```text
Measurements: 4
Pressure of last: 7.3
Unique sensors: 4
Hall: 52.01 N, 4.36 E
```

### Task 3: median and peak

This one is much harder.

`timestamps` and `pressures_bar` belong together: item 0 of one goes with item 0 of the other. Print the median of all six readings, the median of the first five, and the highest reading with its timestamp.

```text
Median of all six: 7.35
Median of first five: 7.3
Peak: 7.6 bar at 09:04
```

Rules:

- No loop, no `if`, no `import`.
- Both medians use the same expression. It must be right for an odd and for an even number of readings. For an even number, the median is the mean of the two middle readings.
- Do not type `"09:04"` or the index 4. Find it from the data.

## Open question

Run `a = [1, 2, 3]`, then `b = a`, then `b.append(4)`, and print `a`. Why did `a` change? And why can a tuple be a key in a dict, while a list cannot?
