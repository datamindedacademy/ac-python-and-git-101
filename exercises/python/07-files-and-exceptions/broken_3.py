# This script is broken on purpose. Run it, read the traceback and fix it.
# This one has a traceback with more than one step. Read it from the bottom up.
#   uv run python exercises/python/07-files-and-exceptions/broken_3.py

# Pressures typed by a colleague with a European keyboard.
raw_pressures = ["7.1", "7.4", "7,6", "7.2"]


def parse_pressure(text):
    return float(text)


def average_pressure(texts):
    values = []
    for text in texts:
        values.append(parse_pressure(text))
    return sum(values) / len(values)


def main():
    average_bar = average_pressure(raw_pressures)
    print(f"Average pressure: {average_bar:.2f} bar")


main()
