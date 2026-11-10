# Solution notes - 02

## Explain it: model answers

Your own words are fine. What matters is that you name the tradeoff.

**`temperature_c = 82` is an `int` and `pressure_bar = 7.5` is a `float`. What is the difference? What type is `temperature_k` after you add 273.15, and why?**

An `int` is a whole number and is exact. A `float` has decimals and is stored with limited precision, so tiny rounding errors are normal. `temperature_k` is a `float`, because an `int` plus a `float` gives a `float`.

**Why call a variable `pressure_bar` and not just `p`? What does the longer name cost you, and what does it buy you?**

The name `pressure_bar` tells the reader what the value is and in which unit, so nobody mixes bar and psi. It costs more typing and longer lines. Code is read more often than it is written, so the clear name wins.
