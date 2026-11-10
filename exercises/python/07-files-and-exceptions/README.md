# 07 - Files, exceptions and tracebacks

Core time: 20 minutes. Optional tasks at the end if you have time.

**Words to use:** exception, exception type, traceback (stack trace), raise, catch, try/except, file mode.

## Goal

Read and write text files, handle errors without crashing, and learn to read a **traceback** to find what went wrong.

## Background

- `with open(path) as file:` opens a file and closes it again at the end of the block. Always use `with`.
- File **modes**: `"r"` read (default), `"w"` write (replaces the file), `"a"` append (adds at the end).
- An **exception** is an error that stops your program. Each has a type, like `ValueError` or `FileNotFoundError`.
- `try` / `except` catches an exception, so you can deal with it:

  ```python
  try:
      value = float(text)
  except ValueError:
      print("Not a number:", text)
  ```

- Only catch the exception types you expect. Never write a bare `except:`, it hides real bugs.
- A **traceback** (also called stack trace) is the message Python prints when the program crashes. How to read it:
  1. Start at the **bottom**. The last line has the **exception type** and a message.
  2. The line above it shows the file, **line number** and the code that failed.
  3. If there are more steps above, they show the chain of function calls that led to it. The top step is where the program started, the bottom step is where it failed.

  ```text
  Traceback (most recent call last):
    File "x.py", line 9, in <module>
      main()
    File "x.py", line 6, in main
      print(1 / 0)
  ZeroDivisionError: division by zero
  ```

  Here the error is a `ZeroDivisionError` on line 6 in the function `main`, called from line 9.

## Core tasks

### Part A: files and try/except (about 10 minutes)

1. Look at `pressures.txt`. Can you spot the bad lines?
2. Open `files_and_exceptions.py`, do TODO 1 to 4.
3. Run it:

   ```powershell
   uv run python exercises/python/07-files-and-exceptions/files_and_exceptions.py
   ```

### Part B: read the traceback (about 10 minutes)

Two scripts are broken on purpose. For each one:

1. Run it and read the traceback from the bottom up.
2. Write down the **exception type** and the **line number**.
3. Fix the script and run it again.

```powershell
uv run python exercises/python/07-files-and-exceptions/broken_1.py
uv run python exercises/python/07-files-and-exceptions/broken_2.py
```

| Script | Exception type | Line |
|---|---|---|
| `broken_1.py` | | |
| `broken_2.py` | | |

## Explain it

This is the last core task. Answer each question in one or two sentences, to your neighbour or in writing. You do not need to write code.

1. Why do you catch `ValueError` and not every exception with a bare `except:`?
2. A traceback gives you a line number. Is that always the line you must change? Use `broken_1.py` as your example.

## Check yourself

Part A should print something like:

```text
Lines read: 6
Good values: [7.1, 7.4, 7.2, 7.5]
Bad lines: ['7,6', 'abc']
File not found: does_not_exist.txt
```

Part B: after your fixes, `broken_1.py` prints a highest pressure and `broken_2.py` prints the message and the limit text.

## Optional: if you have time

1. **A traceback with more than one step.** Run `broken_3.py`. Read it from the bottom up. Write down the names of all the functions in the traceback, in the order they were called. Which one is the place where the error actually happens? Is that also the place where you want to fix it? Then fix it. After the fix it prints `Average pressure: 7.33 bar`.

   ```powershell
   uv run python exercises/python/07-files-and-exceptions/broken_3.py
   ```

2. **Append to a file.** Do TODO 5 in `files_and_exceptions.py`.
3. **Folder script that survives bad data.** In exercise 06 you summarised a folder of logs. Here the folder `logs/` has one log with a bad value (`ERR`). Open `summarize_logs.py` and do TODO 1 to 3 so the script skips the bad row, counts it and keeps going:

   ```powershell
   uv run python exercises/python/07-files-and-exceptions/summarize_logs.py
   ```

   You should see a warning, and the line `run_02: mean 7.71 bar, 1 rows skipped`.
4. In `broken_3.py`, make `parse_pressure` accept a decimal comma by replacing `","` with `"."` before converting.
5. Write a function `read_pressures(path)` that returns the good values and prints a warning for every bad line.

### With Copilot

Run `broken_2.py` again (use the original, or undo your fix) and paste the full traceback into Copilot Chat. Ask: *"What is the cause of this exception, and which line raises it?"* Was it right? Which line of the traceback told you the same thing? Did Copilot propose the same fix as you, or a different one (for example `str()` instead of an f-string)? Which do you prefer?
