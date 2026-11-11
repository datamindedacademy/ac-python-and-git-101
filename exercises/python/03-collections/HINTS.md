# Hints: 03 - Collections

Try the task first. Read a hint only when you are stuck.

## Hint for task 1

`sorted(..., reverse=True)` and a slice from the start give the top three. For the trimmed mean, sort from low to high and slice with `[1:-1]`. Round with `round(x, 3)`.

## Hint for task 2

`.append()` takes a new dict with the same three keys. Index twice for the pressure: `[-1]`, then the key. `set()` and `len()` count unique values. `latitude, longitude = position` unpacks the tuple.
