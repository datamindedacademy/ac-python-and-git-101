# Solution notes - 04

## Explain it: model answers

Your own words are fine. What matters is that you name the tradeoff.

**You used a `for` loop to go over the readings and a `while` loop to count the minutes to the alarm. Why does each loop fit its job? What happens to the `while` loop if the pressure never rises?**

`for` fits when you know what to go over: one iteration per reading, and it stops by itself. `while` fits when you do not know the number of iterations in advance and repeat until a condition changes. The risk of `while` is an infinite loop: if the pressure never rises above the limit, the condition stays true forever.

**In your `if/elif/else`, does the order of the conditions matter? What would the script print for 8.7 bar if you checked the warning limit first?**

Yes. Python takes the first branch whose condition is true and skips the rest. With the warning limit first, 8.7 bar is above 8.0, so the script prints WARNING and never reaches the alarm check. Check the strictest condition first.
