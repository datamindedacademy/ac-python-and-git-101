# Read logs and stop on bad data, or skip it.
# Run from the repo root:
#   uv run python exercises/python/07-files-and-exceptions/check_logs.py

from pathlib import Path

MAX_BAD_SHARE = 0.2  # a file with a larger share of bad rows stops the script
logs_folder = Path(__file__).parent / "logs"

# --- Task 3: stop or skip ---
# See the README. No hints for this one.
