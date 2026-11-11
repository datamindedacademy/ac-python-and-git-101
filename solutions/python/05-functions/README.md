# Solution notes - 05

## Notes

- `test_bench.py` holds the provided tests and the `classify` tests written in task 2. Run them with `uv run pytest solutions/python/05-functions`.
- Run the tests of one folder at a time. The exercise folder and the solution folder both have a `bench.py` and a `test_bench.py`, and pytest cannot load two files with the same name in one run.
- `report.py` has a `main()` that uses all four functions. The `if __name__ == "__main__":` guard keeps the import silent.
- `parse_reading` also accepts a decimal comma (`"7,5 bar"`), which the starter tests ask for.

## Task 3

`units.py` and `test_units.py`. The lookup dict maps each unit to `(family, factor, offset)`, with base value (bar or K) = `value * factor + offset`. Converting is to base and then from base: `(base - to_offset) / to_factor`. Only temperature has non-zero offsets, so a plain factor table (the pressure-only version) does not work for degC and degF. The family in the dict is what rejects `bar` to `K`. A new unit is one new line.

Common wrong turns: a dict of factors only (fails for degC and degF), one `if` branch per pair of units, and a round trip test that includes mixed families (those raise, by design).

## Open question

The default list is created once, when the `def` line runs, and every call that leaves out the argument shares it. The first call returns `[a]`, the second `[a, b]` and the third has three values. Python evaluates default values at definition time, not at call time. Use `readings=None` and create the list inside the function with `if readings is None: readings = []`.
