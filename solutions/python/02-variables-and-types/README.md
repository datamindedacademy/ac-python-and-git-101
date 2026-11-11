# Solution notes - 02

## Challenge

`parse.py` is the reference solution. It splits the text with `.split()` and converts with a dict of factors.

## Open question

Floats are stored as binary fractions. 0.5, 0.25 and 0.75 are sums of powers of two, so they are exact. 0.1, 0.2 and 0.3 have no exact binary form, so each one is stored slightly off and the sum lands on a different float than 0.3. Never compare measured floats with `==`. Use `math.isclose(a, b, rel_tol=1e-6)` or compare the difference with a tolerance that fits the sensor.
