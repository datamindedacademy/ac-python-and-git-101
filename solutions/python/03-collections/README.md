# Solution notes - 03

## Explain it: model answers

Your own words are fine. What matters is that you name the tradeoff.

**You stored one measurement as a dict and the series of pressures as a list. Why not the other way round?**

A measurement has a fixed set of named fields, so a dict with keys fits: you ask for `"pressure_bar"` by name. A series is many values of the same kind in order, so a list fits: you index, slice and loop over it. A list for one measurement would force you to remember that position 1 is the pressure. A dict for the series would need invented keys.

**The position of the test hall is a tuple, not a list. What does a tuple promise that a list does not? When is that useful?**

A tuple cannot change after you create it. That is a promise to the reader: these values belong together and stay as they are. The cost is that you cannot append or replace items, so use a list when the data grows.
