# Solution notes - 06

## Task 3

`summarize_runs.py` holds all three tasks. For each run, `others` is the list of all readings of the other runs. The standard deviation is the population one, so the numbers match the README. With the three given runs and the default threshold of 1.8, only `run_01` is flagged (-1.85). `run_02` is close (1.74), so a threshold of 1.7 or lower flags two runs. A sample standard deviation (divide by n - 1) moves the numbers slightly, and the result can differ near the threshold.

`rows.sort(key=lambda row: abs(row["deviation_std"]), reverse=True)` sorts by size of the deviation, ignoring the sign. `sys.argv` holds text, so the threshold needs `float()`. The defaults come from `len(sys.argv) > 1` and `> 2`.

## Open question

Read the file row by row, which the `csv` reader already does, and keep only running totals: the count, the sum, the sum of squares and the maximum. The mean is sum divided by count, and the standard deviation follows from the three totals. Welford's method gives the same result with less rounding error, because it avoids subtracting two large, nearly equal numbers. Memory use stays constant, whatever the file size.
