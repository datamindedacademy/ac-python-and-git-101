# Solution notes - 05

## Notes

- `test_conversions.py` holds the provided tests, the test you wrote yourself (`test_psi_to_bar`) and one for the optional `classify`. Run them with `uv run pytest solutions/python/05-functions`.
- A function that prints cannot be checked with a simple `assert`, and a script cannot reuse its result. A function that returns can be tested and reused. That is why all conversions return.
- Run the tests of one folder at a time. The exercise folder and the solution folder both have a `conversions.py` and a `test_conversions.py`, and pytest cannot load two files with the same name in one run.

## Challenge

`convert` is in `conversions.py` and its tests are in `test_challenge_convert.py`. The lookup dict holds the size of each unit in bar. Converting is a division of two lookups, so a new unit is one new line in the dict. The folder now runs 10 tests.

## Open question

The default list is created once, when the `def` line runs, and every call that leaves out the argument shares it. The first call returns `[a]`, the second `[a, b]` and the third has three values. Python evaluates default values at definition time, not at call time. Use `readings=None` and create the list inside the function with `if readings is None: readings = []`.
