# Reference solution for exercise 05.
from bench import classify, parse_reading, summarize, to_bar


def main():
    readings = ["7.1 bar", "108.8 psi", "760 kPa", "7.2 bar", "126.2 psi"]
    values_bar = []
    for text in readings:
        value, unit = parse_reading(text)
        values_bar.append(to_bar(value, unit))
    stats = summarize(values_bar)
    print(f"Readings: {stats['count']}")
    print(f"Min: {stats['min']} bar")
    print(f"Max: {stats['max']} bar")
    print(f"Mean: {stats['mean']} bar")
    print(f"Median: {stats['median']} bar")
    print(f"Status: {classify(stats['max'])}")


if __name__ == "__main__":
    main()
