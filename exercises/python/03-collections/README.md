# 03 - Collections

Core time: 15 minutes. Optional tasks at the end if you have time.

## Goal

Store many values together with lists, tuples, dicts and sets. Pick items by index, slice lists, and use common methods.

## Background

A **collection** holds several values in one variable.

| Type | Looks like | Ordered | Can change | Use it for |
|---|---|---|---|---|
| `list` | `[7.1, 7.3]` | yes | yes | a series of readings |
| `tuple` | `(52.01, 4.36)` | yes | no | a fixed group, like coordinates |
| `dict` | `{"pressure_bar": 7.5}` | yes | yes | named fields of one thing |
| `set` | `{"P1", "T1"}` | no | yes | unique values |

- An **index** is the position of an item. Python starts counting at **0**. `-1` is the last item.
- A **slice** takes part of a list: `readings[1:4]` gives items 1, 2 and 3.
- A **method** is a function that belongs to a value, like `readings.append(7.8)`.
- A dict looks up a value by **key**: `measurement["pressure_bar"]`. A key that does not exist gives a `KeyError`.

## Tasks

Open `exercises/python/03-collections/collections_intro.py` and do TODO 1 to 9. Run after each step:

```powershell
uv run python exercises/python/03-collections/collections_intro.py
```

Tip: you can also try things quickly in the REPL with `uv run python`.

## Check yourself

With TODO 1 to 9 done, you should see (among your other prints):

```text
First: 7.1
Last: 7.5
First three: [7.1, 7.3, 7.4]
Number of readings: 7
Max: 7.8 Min: 7.1 Mean: 7.414285714285714
```

The dict part prints every key and value of `measurement`.

## Optional: if you have time

1. TODO 10 to 12 in `collections_intro.py`: a list of dicts and a set. Expected: `Temperature of second: 81.9`, a list of three pressures `[7.1, 7.4, 7.6]`, and `4` unique sensors.
2. Use `measurement.get("humidity", "unknown")`. How is it different from `measurement["humidity"]`?
3. Make a list of the pressures above 7.3 with a **list comprehension**: `[p for p in pressures_bar if p > 7.3]`.
