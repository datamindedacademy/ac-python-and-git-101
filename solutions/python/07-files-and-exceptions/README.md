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

## Challenge

`challenge.py` is the reference solution. It uses `reader.line_num`, which counts lines in the file including the header, so `ERR` in `run_02.csv` is on line 4. Run it with `--skip` to skip bad rows. Without the switch it stops with `ValueError: run_02.csv line 4: cannot convert 'ERR'`.

Default for a nightly script: stopping is the safer default. A silent skip changes the mean without anybody noticing. If the night run must always finish, skip but make the warning visible (a log or a mail) and count the skipped rows in the result.

## Open question

The file holds a partial document, which is not valid JSON, so the next reader fails. Write the new content to a temporary file in the same folder and then rename it over the real one with `os.replace` (or `Path.replace`). A rename on the same disk either happens or does not, so a reader sees the old file or the new one. The temporary file must be on the same disk, otherwise the rename becomes a copy.
