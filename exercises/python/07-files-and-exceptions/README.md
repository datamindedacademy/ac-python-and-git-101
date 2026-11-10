# 07 - Files, exceptions and tracebacks

Time: about 25 minutes.

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

## Part A: files and try/except

1. Look at `pressures.txt`. Can you spot the bad lines?
2. Open `files_and_exceptions.py`, do TODO 1 to 5.
3. Run it:

   ```powershell
   uv run python exercises/python/07-files-and-exceptions/files_and_exceptions.py
   ```

## Part B: read the traceback

Three scripts are broken on purpose. For each one:

1. Run it and read the traceback from the bottom up.
2. Write down: the **exception type**, the **file line number**, and **what it means** in your own words.
3. Fix the script and run it again.

```powershell
uv run python exercises/python/07-files-and-exceptions/broken_1.py
uv run python exercises/python/07-files-and-exceptions/broken_2.py
uv run python exercises/python/07-files-and-exceptions/broken_3.py
```

| Script | Exception type | Line | Your explanation | Your fix |
|---|---|---|---|---|
| `broken_1.py` | | | | |
| `broken_2.py` | | | | |
| `broken_3.py` | | | | |

For `broken_3.py`, also write down the names of all the functions in the traceback, in the order they were called. Which one is the place where the error actually happens? Is that also the place where you want to fix it?

## Check yourself

Part A should print something like:

```text
Lines read: 6
Good values: [7.1, 7.4, 7.2, 7.5]
Bad lines: ['7,6', 'abc']
File not found: does_not_exist.txt
```

Part B: after your fixes, `broken_1.py` prints a highest pressure, `broken_2.py` prints the message and the limit text, and `broken_3.py` prints `Average pressure: 7.33 bar`.

## Stretch

- In `broken_3.py`, make `parse_pressure` accept a decimal comma by replacing `","` with `"."` before converting.
- Write a function `read_pressures(path)` that returns the good values and prints a warning for every bad line.
