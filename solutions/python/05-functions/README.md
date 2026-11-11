# Solution notes - 05

## Explain it: model answers

Your own words are fine. What matters is that you name the tradeoff.

**What do you gain by moving the conversions into `conversions.py`? What does it cost?**

You gain one place for each formula: every script imports the same tested function, and a fix reaches all of them. The cost is one more file to keep track of, an import that must be able to find it, and a change in the module can break scripts you forgot about.

**You wrote the test for `psi_to_bar` before the function. What did the test force you to decide before you wrote any code?**

The name of the function, its argument and its unit, and the exact result for a known input (14.5038 psi must give 1 bar). Those are decisions about what "correct" means, and you made them before any code could bend them. The cost is a few minutes up front, and a wrong expectation in the test gives you a wrong function that still passes.

## Notes

- `test_conversions.py` holds the provided tests, the test you wrote yourself (`test_psi_to_bar`) and one for the optional `classify`. Run them with `uv run pytest solutions/python/05-functions`.
- A function that prints cannot be checked with a simple `assert`, and a script cannot reuse its result. A function that returns can be tested and reused. That is why all conversions return.
- Run the tests of one folder at a time. The exercise folder and the solution folder both have a `conversions.py` and a `test_conversions.py`, and pytest cannot load two files with the same name in one run.
