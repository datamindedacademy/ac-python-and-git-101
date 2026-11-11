# Solution notes - 06

## Challenge

The first half is already in `summarize_runs.py`: it takes a runs folder and an output folder from `sys.argv`. `challenge.py` adds the second half. It takes only the runs folder and prints a warning for every run with a standard deviation above `LIMIT_STD_BAR` (0.18). With the three given runs only `run_01` (0.20 bar) gives a warning.

## Open question

Read the file row by row, which the `csv` reader already does, and keep only running totals: the count, the sum, the sum of squares and the maximum. The mean is sum divided by count, and the standard deviation follows from the three totals. Welford's method gives the same result with less rounding error, because it avoids subtracting two large, nearly equal numbers. Memory use stays constant, whatever the file size.
