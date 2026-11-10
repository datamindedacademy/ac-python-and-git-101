# Solution notes - 07

## Traceback answers

| Script | Exception type | Line | Meaning | Fix |
|---|---|---|---|---|
| `broken_1.py` | `NameError` | 12 | The name `maximum_bar` was used but never assigned. | Create it first: `maximum_bar = max(pressures_bar)`. Check for typos in names. |
| `broken_2.py` | `TypeError` | 8 | `+` cannot join a `str` and a `float`. | Use an f-string: `f"Unit {serial_number} runs at {pressure_bar} bar"`. |
| `broken_3.py` | `ValueError` | 10 | `float("7,6")` fails because Python expects a decimal point. | Replace the comma: `float(text.replace(",", "."))`. |

## broken_3.py: the chain of calls (optional task)

Read from the top: `<module>` calls `main` (line 25). `main` calls `average_pressure` (line 21). `average_pressure` calls `parse_pressure` (line 16). The failing line is line 10, inside `parse_pressure`. The error is raised in `parse_pressure`, the bottom frame. That is where Python noticed the problem. The real cause is the input `"7,6"`, so cleaning the text in `parse_pressure` is the right place to fix it.

## Habits

- Read the last line first, then go up until you reach your own file.
- The line number is where Python noticed the problem. The cause can be a bit earlier.
- Copy the last line into a search engine if you do not know the exception.

## Optional folder script

`summarize_logs.py` wraps `float()` in `try/except ValueError`, counts the skipped rows and keeps going. Expected last lines: `run_02: mean 7.71 bar, 1 rows skipped`.

## Explain it: model answers

Your own words are fine. What matters is that you name the tradeoff.

**Why do you catch `ValueError` and not every exception with a bare `except:`?**

`ValueError` is the one failure you expect and know how to handle: text that is not a number. A bare `except:` also swallows typos (`NameError`), wrong types and even `Ctrl+C`, so real bugs stay hidden and the script reports wrong results without a warning. Catching narrowly costs a little thought about what can go wrong.

**A traceback gives you a line number. Is that always the line you must change? Use `broken_1.py` as your example.**

No. The line number is where Python noticed the problem, not always where the cause is. In `broken_1.py` the traceback points at line 12, where `maximum_bar` is used, but the fix is to add a line above it that creates the variable.
