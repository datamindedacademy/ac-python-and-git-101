# Solution notes - 02

## Task 3

Each field needs a chain of text methods before `float()` accepts it. `strip()` removes the spaces at both ends. It has to come before `removesuffix()`, because with spaces after it the unit is not at the end of the text. `replace(",", ".")` turns the decimal comma into a point: `float("108,8")` gives a `ValueError`, and its last line shows the text it got. `upper()` turns `p1` into `P1`. Psi to bar is a division by `BAR_TO_PSI`. The last line is the comparison `reading_bar > ALARM_LIMIT_BAR`, which is already a `bool`.

`help(str)` is where to find these methods. `removesuffix()` only removes the exact text you give it, so `" psi"` does not match `" PSI"`. Either remove `" PSI"`, or call `lower()` first and then remove `" psi"`.

## Open question

Floats are stored as binary fractions. 0.5, 0.25 and 0.75 are sums of powers of two, so they are exact. 0.1, 0.2 and 0.3 have no exact binary form, so each one is stored slightly off and the sum lands on a different float than 0.3. Never compare measured floats with `==`. Use `math.isclose(a, b, rel_tol=1e-6)` or compare the difference with a tolerance that fits the sensor.

The second question. Every Python value is an object with a header of 16 bytes: a reference count and a pointer to its type. A float adds one 8-byte double, which gives 24. An `int` has no fixed width. It stores a length field of 8 bytes and then as many 4-byte digits as the number needs, which gives 28 for small numbers. `sys.getsizeof(2**100)` is 40, because a bigger number gets more digits. So an `int` never overflows, it only uses more memory. A float always has 64 bits, so it has a largest value and limited precision. This is also why a list of a million numbers takes far more memory in plain Python than in NumPy on day 2.
