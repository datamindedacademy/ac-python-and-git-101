# Solution notes - 01

## Task 2

The kernel keeps every variable until it restarts, and a cell uses whatever the variables are at that moment. The solution notebook has a cell that does `pressures_bar.append(7.5)`. Run it, then run the average cell again: it shows 7.275. After Restart and Run All it shows 7.2333, because the average cell now runs before the append cell. Other ways to get there are deleting the cell that defines a variable after it ran, or running a cell twice when it changes a variable.

Rule of thumb: explore in a notebook, then move the stable code to a script or module. A script always runs from top to bottom. A notebook runs in the order you click.

## Open question

When you press Enter, the interpreter starts and imports a few modules it needs at startup. It then compiles your source to bytecode and runs that. Python saves the bytecode of modules you import in a `__pycache__` folder next to them, so the next start skips the compile step. The script you run directly is not cached, it is compiled every time.
