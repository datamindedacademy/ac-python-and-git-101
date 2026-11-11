# 07 - Files, exceptions and tracebacks

**Words to use:** exception, exception type, traceback (stack trace), raise, catch, try/except, bubble up.

## Goal

Read a **traceback** to find what went wrong, handle a bad value without crashing, and decide where in a script an error should be caught and where it should stop the script.

## Why this matters

Real logs contain bad rows. A script that crashes on file 37 of 200 and a script that silently skips rows are both a problem, so you choose the behaviour on purpose. Reading a traceback is the fastest way to find a fault, in your code and in Copilot's.

## Background

- An **exception** is an error that stops your program. Each has a type, like `ValueError` or `FileNotFoundError`.
- `try` / `except` catches an exception, so you can deal with it:

  ```python
  try:
      value = float(text)
  except ValueError:
      print("Not a number:", text)
  ```

- Only catch the exception types you expect. Never write a bare `except:`, it hides real bugs.
- A **traceback** (also called stack trace) is the message Python prints when the program crashes. Start at the **bottom**. The last line has the **exception type** and a message. The line above it shows the file, **line number** and the code that failed. Steps above that show the calls that led to it.

  ```text
  Traceback (most recent call last):
    File "x.py", line 9, in <module>
      main()
    File "x.py", line 6, in main
      print(1 / 0)
  ZeroDivisionError: division by zero
  ```

- `csv.DictReader` has a `line_num` attribute: the number of the line it read last, counting the header. `reader = csv.DictReader(file)`, then `reader.line_num` inside the loop.
- `sys.argv` is the list of words typed after the script name. `sys.exit("message")` prints the message to the error output and stops the script with exit code 1.
- `raise NewError("text") from err` raises a new error and keeps the original one as its **cause**.

## Tasks

Stuck on a task? The hints are in `HINTS.md` in this folder.

Run each script from the repo root in PowerShell.

### Task 1: read a traceback

`exercises/python/07-files-and-exceptions/broken_1.py` crashes on purpose. Run it, read the traceback from the bottom line up, and find the exception type and the line number. Fix the script so that it prints both lines.

```powershell
uv run python exercises/python/07-files-and-exceptions/broken_1.py
```

```text
Average pressure: 7.325
Highest pressure: 7.6
```

### Task 2: skip and count

Open `exercises/python/07-files-and-exceptions/summarize_logs.py`. The logs in `logs/` contain values that are not a number, like `ERR`. Make the script survive them: skip such a row, count it, and print the count. Catch `ValueError` only. A bare `except:` or `except Exception: pass` does not count.

```powershell
uv run python exercises/python/07-files-and-exceptions/summarize_logs.py
```

```text
run_01: mean 7.25 bar, 0 rows skipped
run_02: mean 7.71 bar, 1 rows skipped
run_03: mean 7.49 bar, 0 rows skipped
run_04: mean 7.37 bar, 4 rows skipped
```

### Task 3: stop or skip

This one is much harder. There is no hint.

Open `exercises/python/07-files-and-exceptions/check_logs.py`. Write a script that reads the logs and has two modes:

- With `--strict`, the first bad value stops the script. Without it, bad rows are skipped, with a warning for each.
- Either way, a file where more than `MAX_BAD_SHARE` of the rows are bad stops the script.

A stop prints one line and exits with code 1. Any other argument is the name of a file to read. With no file names, read all of `logs/`.

```powershell
uv run python exercises/python/07-files-and-exceptions/check_logs.py
uv run python exercises/python/07-files-and-exceptions/check_logs.py --strict
uv run python exercises/python/07-files-and-exceptions/check_logs.py does_not_exist.csv
```

```text
run_01: mean 7.25 bar, 0 rows skipped
Warning: run_02.csv line 4: cannot convert 'ERR'
run_02: mean 7.71 bar, 1 rows skipped
run_03: mean 7.49 bar, 0 rows skipped
Warning: run_04.csv line 3: cannot convert 'ERR'
Warning: run_04.csv line 5: cannot convert ''
Warning: run_04.csv line 6: cannot convert 'n/a'
Warning: run_04.csv line 8: cannot convert 'ERR'
Error: run_04.csv: 4 of 8 rows are bad, the limit is 20%
```

```text
run_01: mean 7.25 bar, 0 rows skipped
Error: run_02.csv line 4: cannot convert 'ERR'
```

```text
File not found: does_not_exist.csv
```

Rules:

- A function `read_pressures(path, strict)` does the reading. You decide what it returns.
- In strict mode, a bad value makes the function raise a new `ValueError` that names the file and the line number in the file, and keeps the original error as its cause (`raise ... from err`).
- The function may print warnings. It must not print the `Error:` or `File not found:` line and must not call `sys.exit`. Only the code that calls it does that.
- `FileNotFoundError` gets its own message, as shown above.
- No bare `except:`.

## Open question

Your script is writing `summary.json` and the laptop loses power halfway. What is in the file now? How would you write the file so that a reader always finds either the complete old version or the complete new one, never half of one?
