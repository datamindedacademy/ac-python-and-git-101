# Solution notes - 07

## Traceback answers

| Script | Exception type | Line | Meaning | Fix |
|---|---|---|---|---|
| `broken_1.py` | `NameError` | 12 | The name `maximum_bar` was used but never assigned. | Create it first: `maximum_bar = max(pressures_bar)`. Check for typos in names. |
| `broken_2.py` | `TypeError` | 8 | `+` cannot join a `str` and a `float`. | Use an f-string: `f"Unit {serial_number} runs at {pressure_bar} bar"`. |
| `broken_3.py` | `ValueError` | 10 | `float("7,6")` fails because Python expects a decimal point. | Replace the comma: `float(text.replace(",", "."))`. |

## broken_3.py: the chain of calls

Read from the top: `<module>` calls `main` (line 25). `main` calls `average_pressure` (line 21). `average_pressure` calls `parse_pressure` (line 16). The failing line is line 10, inside `parse_pressure`. The error is raised in `parse_pressure`, the bottom frame. That is where Python noticed the problem. The real cause is the input `"7,6"`, so cleaning the text in `parse_pressure` is the right place to fix it.

## Habits

- Read the last line first, then go up until you reach your own file.
- The line number is where Python noticed the problem. The cause can be a bit earlier.
- Copy the last line into a search engine if you do not know the exception.
