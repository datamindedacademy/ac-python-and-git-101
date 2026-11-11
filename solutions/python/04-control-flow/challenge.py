# Reference solution for the challenge in exercise 04.

PRESSURE_WARNING_BAR = 8.0

pressures_bar = [7.1, 7.6, 8.1, 8.4, 8.7, 7.9, 8.6, 7.3]


def first_run_of_three(readings):
    """Return the number (from 1) of the first of three readings in a row above the limit."""
    for start in range(len(readings) - 2):
        if all(p > PRESSURE_WARNING_BAR for p in readings[start : start + 3]):
            return start + 1
    return None


def report(readings):
    number = first_run_of_three(readings)
    if number is None:
        print(f"No three readings in a row above {PRESSURE_WARNING_BAR} bar")
    else:
        print(f"Three readings in a row above {PRESSURE_WARNING_BAR} bar start at reading {number}")


report(pressures_bar)
# More tests: never, and a run at the very end.
report([7.1, 8.1, 7.0, 8.2, 8.3, 7.0])
report([7.1, 7.0, 8.1, 8.2, 8.3])
