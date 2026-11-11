# Solution notes - 03

## Task 3

Sort the readings and call the count `n`. The indexes `(n - 1) // 2` and `n // 2` are the same item when `n` is odd, and the two middle items when `n` is even. The mean of those two items is the median in both cases, so no `if` is needed.

For the peak, `pressures_bar.index(max(pressures_bar))` gives the position of the highest reading. The same position in `timestamps` is its time.

## Open question

`b = a` does not copy the list. It gives the same list object a second name, so `b.append(4)` changes what `a` sees too. Use `a.copy()` when you want a separate list. A dict key must be hashable and must stay the same while it is in the dict. A list can change, so it is not hashable. A tuple cannot change, so it can be a key.
