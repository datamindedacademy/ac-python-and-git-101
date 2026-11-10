# Solution notes - 06

## Explain it: model answers

Your own words are fine. What matters is that you name the tradeoff.

**Why use `csv.DictReader` and not split each line on commas yourself?**

`csv.DictReader` handles the header, quoted fields that contain commas, and line endings, and gives every row as a dict so you read columns by name. Splitting on commas yourself is shorter to start with but breaks on the first quoted value and depends on the column order. The cost of `DictReader` is one import and knowing that every value is still text.

**The script finds its input with `Path(__file__).parent` and `glob("*.csv")` instead of three file names typed in the code. What do you gain? What could surprise you one day?**

The script works from any folder and on any laptop, and a new log file is picked up without a code change. The surprise is the other side of that: every file that matches the glob pattern is processed, also a wrong or half-finished CSV that somebody dropped in the folder.
