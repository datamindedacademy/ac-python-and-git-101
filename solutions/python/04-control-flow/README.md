# Solution notes - 04

## Task 3

Keep a variable `start` that is `None` while no episode is open. A reading above the limit opens an episode when `start` is `None`, and updates the peak. A reading at or below the limit closes the open episode and stores `(start, end, length, peak)`. The loop ends without a closing reading when the last reading is above the limit, so after the loop, check `start` once more and store the open episode. Keep the longest while printing: compare each length with the best so far.

## Open question

Round brackets make a generator expression, not a tuple. Printing it shows something like `<generator object ...>`. It produces one value at a time when asked, so it never holds ten million values in memory. The price is that you can walk through it only once. Wrap it in `list(...)` when you need the values again.
