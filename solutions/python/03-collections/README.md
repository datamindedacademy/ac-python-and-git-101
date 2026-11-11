# Solution notes - 03

## Challenge

`challenge.py` is the reference solution. It loops over the keys of the first dict and uses a comprehension for each list. It has its own copy of the four measurements.

## Open question

`b = a` does not copy the list. It gives the same list object a second name, so `b.append(4)` changes what `a` sees too. Use `a.copy()` when you want a separate list. A dict key must be hashable and must stay the same while it is in the dict. A list can change, so it is not hashable. A tuple cannot change, so it can be a key.
