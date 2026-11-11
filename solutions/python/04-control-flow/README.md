# Solution notes - 04

## Challenge

`challenge.py` is the reference solution. It checks every window of three readings with `range(len(...) - 2)` and `all(...)`. It also runs the two extra test lists from the task.

## Open question

Round brackets make a generator expression, not a tuple. Printing it shows something like `<generator object ...>`. It produces one value at a time when asked, so it never holds ten million values in memory. The price is that you can walk through it only once. Wrap it in `list(...)` when you need the values again.
