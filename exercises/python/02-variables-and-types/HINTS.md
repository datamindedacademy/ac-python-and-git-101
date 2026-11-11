# Hints: 02 - Variables and types

Try the task first. Read a hint only when you are stuck.

## Hint for task 1

`pressure_text.split()[0]` is the text `"7.5"`. Wrap it in `float()`. Psi is bar times `BAR_TO_PSI`. Kelvin is degrees Celsius plus `273.15`. In the f-string write `{pressure_bar:.2f}`.

## Hint for task 2

The last line says what went wrong: you added a `float` to a `str`. Convert one of them with `str()`, or use an f-string.
