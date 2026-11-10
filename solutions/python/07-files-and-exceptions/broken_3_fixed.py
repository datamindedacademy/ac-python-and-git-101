# Fixed version of broken_3.py.
# Error: ValueError: could not convert string to float: '7,6' (line 10 of the broken file).
# The chain is: <module> -> main -> average_pressure -> parse_pressure.
# The error happens in parse_pressure, but the cause is the data: a decimal comma.
# We fix it where the text is converted, so every caller benefits.

raw_pressures = ["7.1", "7.4", "7,6", "7.2"]


def parse_pressure(text):
    return float(text.replace(",", "."))


def average_pressure(texts):
    values = []
    for text in texts:
        values.append(parse_pressure(text))
    return sum(values) / len(values)


def main():
    average_bar = average_pressure(raw_pressures)
    print(f"Average pressure: {average_bar:.2f} bar")


main()
