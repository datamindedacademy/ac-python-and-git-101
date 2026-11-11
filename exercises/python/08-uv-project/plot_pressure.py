# Plot pressure over time to a PNG file.
# Copy this file into your own uv project (see the README), then run:
#   uv run python plot_pressure.py

import sys

import matplotlib

matplotlib.use("Agg")  # draw to a file, no window needed
import matplotlib.pyplot as plt  # noqa: E402

minutes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
pressures_bar = [7.1, 7.3, 7.4, 7.2, 7.6, 7.5, 7.8, 7.7, 7.4, 7.3]
alarm_limit_bar = 8.5

output_file = sys.argv[1] if len(sys.argv) > 1 else "pressure.png"

# TODO: draw this picture and save it to output_file:
#   - pressure against time, as a line with round markers
#   - the alarm limit as a red dashed horizontal line
#   - axis labels with units: "Time (min)" and "Pressure (bar)"
#   - the title "Test run CB-0042"
#   - a legend that names both lines
#   - saved to output_file at 150 dpi
# Matplotlib is a day 2 topic. See the README for hints.

# This line only reports. It prints even when nothing was saved.
print("Saved", output_file)
