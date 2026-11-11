# Solution notes - 07

## Task 1

`broken_1_fixed.py` is `broken_1.py` with the fix. The comment at the top names the error.

## Task 3

`check_logs.py` is the reference solution. The decisions:

- `read_pressures` catches `ValueError` per row, because it is the only place that knows the file and the line (`reader.line_num` counts the header, so `ERR` in `run_02.csv` is on line 4). In strict mode it raises a new `ValueError` with that context `from err`. Otherwise it counts the row and warns.
- The share check is at the end of the function, when the row counts are known. It raises a `ValueError` too.
- Only the top of the script catches. There the plan is the same for every error: print one line and exit with code 1 (`sys.exit("...")`). `FileNotFoundError` is caught first, so it gets its own message.
- Strict mode stops at `run_02.csv`. Without it the script reads `run_02.csv` and `run_03.csv`, then stops at `run_04.csv`, where 4 of 8 rows are bad.

Stop or skip for a nightly script: stopping is the safer default, because a silent skip changes the mean without anybody noticing. Skip only if the warning stays visible.

Common mistakes: catching inside the function and printing there, so the caller cannot decide; `except Exception`, which also hides typos; checking the share per row instead of per file.

## Open question

The file holds a partial document, which is not valid JSON, so the next reader fails. Write the new content to a temporary file in the same folder and then rename it over the real one with `os.replace` (or `Path.replace`). A rename on the same disk either happens or does not, so a reader sees the old file or the new one. The temporary file must be on the same disk, otherwise the rename becomes a copy.
