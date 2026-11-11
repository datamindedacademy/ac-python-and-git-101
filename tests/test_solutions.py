"""Check that the reference solutions run and give the right results."""

import csv
import json
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).parent.parent
EXERCISES = ROOT / "exercises" / "python"
SOLUTIONS = ROOT / "solutions" / "python"


def run(script, *args, stdin="", cwd=ROOT):
    """Run a script with the current Python and return the finished process."""
    return subprocess.run(
        [sys.executable, str(script), *args],
        input=stdin,
        capture_output=True,
        text=True,
        cwd=cwd,
        timeout=60,
    )


def run_ok(script, *args, stdin=""):
    result = run(script, *args, stdin=stdin)
    assert result.returncode == 0, result.stderr
    return result.stdout


def test_01_hello():
    out = run_ok(SOLUTIONS / "01-first-script" / "hello.py")
    assert "Compressor: CB-0042" in out
    assert "Average pressure in bar: 7.23" in out
    assert "Python version: 3." in out
    assert "Python runs from:" in out


def test_01_notebooks_are_valid():
    for folder in (EXERCISES, SOLUTIONS):
        path = folder / "01-first-script" / "first_notebook.ipynb"
        with open(path) as file:
            notebook = json.load(file)
        assert notebook["nbformat"] == 4
        assert len(notebook["cells"]) >= 3
        for cell in notebook["cells"]:
            if cell["cell_type"] == "code":
                assert cell["outputs"] == []


def test_01_solution_notebook_code_runs():
    with open(SOLUTIONS / "01-first-script" / "first_notebook.ipynb") as file:
        notebook = json.load(file)
    code = "\n".join("".join(c["source"]) for c in notebook["cells"] if c["cell_type"] == "code")
    namespace = {}
    exec(code, namespace)
    assert namespace["average_bar"] == pytest.approx(7.2333, abs=1e-3)


def test_02_units():
    out = run_ok(SOLUTIONS / "02-variables-and-types" / "units.py")
    assert "Pressure: 7.50 bar = 108.78 psi" in out
    assert "Temperature: 82.00 degC = 355.15 K" in out
    assert "Pressure: 7.5 bar\n" in out
    assert "Sensor P1 at 09:00:00 on 2026-01-15" in out
    assert "Pressure: 7.50 bar\n" in out
    assert "Temperature: 82.00 degC\n" in out
    assert "Above limit: True" in out


def test_03_collections():
    out = run_ok(SOLUTIONS / "03-collections" / "collections_intro.py")
    assert "Last: 7.5" in out
    assert "Top three: [7.6, 7.5, 7.4]" in out
    assert "Trimmed mean: 7.35" in out
    assert "Measurements: 4" in out
    assert "Pressure of last: 7.3" in out
    assert "Unique sensors: 4" in out
    assert "Hall: 52.01 N, 4.36 E" in out
    assert "Median of all six: 7.35" in out
    assert "Median of first five: 7.3\n" in out
    assert "Peak: 7.6 bar at 09:04" in out


def test_04_control_flow():
    out = run_ok(SOLUTIONS / "04-control-flow" / "alarms.py")
    assert "Reading 3: 8.1 bar -> WARNING" in out
    assert "Reading 5: 8.7 bar -> ALARM" in out
    assert "Reading 8: 7.3 bar -> OK" in out
    assert "Alarms: 2" in out
    assert "Alarm readings: [8.7, 8.6]" in out
    assert "In psi: [103.0, 110.2, 117.5, 121.8, 126.2, 114.6, 124.7, 105.9]" in out
    assert "Episode 1: readings 2 to 4, length 3, peak 8.3" in out
    assert "Episode 2: readings 6 to 6, length 1, peak 8.4" in out
    assert "Episode 3: readings 8 to 11, length 4, peak 8.9" in out
    assert "Episode 4: readings 13 to 14, length 2, peak 8.5" in out
    assert "Longest: readings 8 to 11, 4 readings" in out


def test_05_import_has_no_side_effects():
    folder = SOLUTIONS / "05-functions"
    result = subprocess.run(
        [sys.executable, "-c", "import conversions; print(conversions.psi_to_bar(14.5038))"],
        capture_output=True,
        text=True,
        cwd=folder,
    )
    assert result.returncode == 0, result.stderr
    assert result.stdout.strip() == "1.0"


def test_05_report():
    out = run_ok(SOLUTIONS / "05-functions" / "report.py")
    assert "Average pressure (bar): 7.33" in out
    assert "Average pressure (psi): 106.31" in out
    assert "Temperature (K): 356.65" in out
    assert "Flow (m3/h): 149.4" in out
    direct = run_ok(SOLUTIONS / "05-functions" / "conversions.py")
    assert direct.strip() == "108.7785"


def run_pytest(folder):
    """Run pytest on one folder in its own process.

    Each folder gets its own process, so the two `conversions.py` and
    `test_conversions.py` files (starter and solution) never meet in one run.
    """
    return subprocess.run(
        [sys.executable, "-m", "pytest", str(folder), "-q", "-p", "no:cacheprovider"],
        capture_output=True,
        text=True,
        cwd=ROOT,
        timeout=120,
    )


def test_05_solution_tests_pass():
    result = run_pytest(SOLUTIONS / "05-functions")
    assert result.returncode == 0, result.stdout
    assert "11 passed" in result.stdout
    assert "failed" not in result.stdout


def test_05_units():
    out = run_ok(SOLUTIONS / "05-functions" / "units.py")
    assert out.split() == ["108.7785", "212.0", "-273.15"]


def test_05_starter_tests_are_red():
    result = run_pytest(EXERCISES / "05-functions")
    assert result.returncode == 1, result.stdout
    assert "4 failed, 1 passed" in result.stdout
    for name in ("test_bar_to_psi", "test_celsius_to_kelvin", "test_average"):
        assert f"FAILED exercises/python/05-functions/test_conversions.py::{name}" in (
            result.stdout.replace("\\", "/")
        )
    # Failures must be failed assertions, not import or collection errors.
    assert "error" not in result.stdout.lower().replace("assertionerror", "")


def test_05_starter_has_no_psi_to_bar_yet():
    source = (EXERCISES / "05-functions" / "conversions.py").read_text()
    assert "def psi_to_bar" not in source


def test_06_summarize_runs():
    runs = EXERCISES / "06-standard-library" / "runs"
    assert len(list(runs.glob("*.csv"))) == 3
    script = SOLUTIONS / "06-standard-library" / "summarize_runs.py"
    out = run_ok(script, str(runs))
    assert "Rows: 8\nMean pressure: 7.25 bar\nMax pressure: 7.5 bar" in out
    output = SOLUTIONS / "06-standard-library" / "output"
    with open(output / "summary.json") as file:
        summaries = json.load(file)
    assert [item["run"] for item in summaries] == ["run_01", "run_02", "run_03"]
    assert summaries[0]["rows"] == 8
    assert summaries[0]["pressure_mean_bar"] == pytest.approx(7.25)
    assert summaries[0]["pressure_max_bar"] == pytest.approx(7.5)
    with open(output / "outliers.csv", newline="") as file:
        rows = list(csv.DictReader(file))
    assert [row["run"] for row in rows] == ["run_01", "run_02", "run_03"]
    assert [row["flagged"] for row in rows] == ["True", "False", "False"]
    assert float(rows[0]["deviation_std"]) == pytest.approx(-1.85)
    assert "Flagged: run_01 (-1.85 standard deviations, limit 1.8)" in out
    assert "Flagged: run_02" not in out
    assert "Flagged: run_02" in run_ok(script, str(runs), "1.5")


def test_06_solution_runs_match_exercise_runs():
    for path in (EXERCISES / "06-standard-library" / "runs").glob("*.csv"):
        other = SOLUTIONS / "06-standard-library" / "runs" / path.name
        assert other.read_text() == path.read_text()


def test_06_default_paths():
    out = run_ok(SOLUTIONS / "06-standard-library" / "summarize_runs.py")
    assert "Flagged: run_01" in out
    assert (SOLUTIONS / "06-standard-library" / "output" / "summary.json").exists()


def test_07_summarize_logs_skips_and_counts():
    out = run_ok(SOLUTIONS / "07-files-and-exceptions" / "summarize_logs.py")
    assert "run_01: mean 7.25 bar, 0 rows skipped" in out
    assert "run_02: mean 7.71 bar, 1 rows skipped" in out
    assert "run_04: mean 7.37 bar, 4 rows skipped" in out


def test_07_check_logs_strict_stops_at_first_bad_row():
    script = SOLUTIONS / "07-files-and-exceptions" / "check_logs.py"
    result = run(script, "--strict")
    assert result.returncode == 1
    assert result.stderr.strip() == "Error: run_02.csv line 4: cannot convert 'ERR'"
    assert "run_01: mean 7.25 bar" in result.stdout
    assert "run_03" not in result.stdout


def test_07_check_logs_skips_until_too_many_bad_rows():
    script = SOLUTIONS / "07-files-and-exceptions" / "check_logs.py"
    result = run(script)
    assert result.returncode == 1
    assert "run_02: mean 7.71 bar, 1 rows skipped" in result.stdout
    assert "run_03: mean 7.49 bar, 0 rows skipped" in result.stdout
    assert result.stderr.strip() == (
        "Error: run_04.csv: 4 of 8 rows are bad, the limit is 20%"
    )
    run_02 = SOLUTIONS / "07-files-and-exceptions" / "logs" / "run_02.csv"
    assert run_ok(script, str(run_02)).endswith("1 rows skipped\n")


def test_07_check_logs_missing_file():
    result = run(SOLUTIONS / "07-files-and-exceptions" / "check_logs.py", "nope.csv")
    assert result.returncode == 1
    assert result.stderr.strip() == "File not found: nope.csv"


def test_07_broken_1_fails_as_intended():
    result = run(EXERCISES / "07-files-and-exceptions" / "broken_1.py")
    assert result.returncode != 0
    assert result.stderr.strip().splitlines()[-1].startswith("NameError:")


def test_07_broken_1_fixed_works():
    out = run_ok(SOLUTIONS / "07-files-and-exceptions" / "broken_1_fixed.py")
    assert "Highest pressure: 7.6" in out


def test_08_plot(tmp_path):
    target = tmp_path / "pressure.png"
    run_ok(SOLUTIONS / "08-uv-project" / "plot_pressure.py", str(target))
    assert target.exists()
    assert target.read_bytes()[:8] == b"\x89PNG\r\n\x1a\n"
    header = (SOLUTIONS / "08-uv-project" / "plot_pressure.py").read_text()
    assert header.startswith("# /// script\n")
    assert '"matplotlib' in header.split("# ///")[1]


@pytest.mark.parametrize(
    "script",
    [
        "01-first-script/hello.py",
        "02-variables-and-types/units.py",
        "03-collections/collections_intro.py",
        "04-control-flow/alarms.py",
        "05-functions/conversions.py",
        "05-functions/report.py",
        "06-standard-library/summarize_runs.py",
        "08-uv-project/plot_pressure.py",
        "07-files-and-exceptions/summarize_logs.py",
        "07-files-and-exceptions/check_logs.py",
    ],
)
def test_starters_do_not_crash(script, tmp_path):
    args = [str(tmp_path / "x.png")] if script.startswith("08") else []
    result = run(EXERCISES / script, *args)
    assert result.returncode == 0, result.stderr
