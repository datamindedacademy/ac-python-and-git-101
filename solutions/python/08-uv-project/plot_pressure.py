# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "matplotlib>=3.10",
# ]
# ///

# Reference solution for exercise 08, task 2: the script carries its own dependencies.

import sys

import matplotlib

matplotlib.use("Agg")  # draw to a file, no window needed
import matplotlib.pyplot as plt  # noqa: E402

minutes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
pressures_bar = [7.1, 7.3, 7.4, 7.2, 7.6, 7.5, 7.8, 7.7, 7.4, 7.3]
alarm_limit_bar = 8.5

plt.plot(minutes, pressures_bar, marker="o", label="Pressure")
plt.axhline(alarm_limit_bar, color="red", linestyle="--", label="Alarm limit")
plt.xlabel("Time (min)")
plt.ylabel("Pressure (bar)")
plt.title("Test run CB-0042")
plt.legend()

output_file = sys.argv[1] if len(sys.argv) > 1 else "pressure.png"
plt.savefig(output_file, dpi=150)
print("Saved", output_file)
