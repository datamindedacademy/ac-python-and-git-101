# Solution notes - 05

## Explain it: model answers

Your own words are fine. What matters is that you name the tradeoff.

**What do you gain by moving the conversions into `conversions.py`? What does it cost?**

You gain one place for each formula: every script imports the same tested function, and a fix reaches all of them. The cost is one more file to keep track of, an import that must be able to find it, and a change in the module can break scripts you forgot about.

**What is the difference between a function that prints its result and a function that returns it? Which of the two can `report.py` reuse?**

A function that prints only shows text on the screen and gives back `None`. A function that returns hands the value to the caller, who can store it, round it or pass it on. `report.py` can only reuse functions that return.
