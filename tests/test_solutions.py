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
    assert "7.5 bar <class 'str'>" in out
    assert "82 <class 'str'>" in out
    assert "Temperature in K: 355.15" in out
    assert "7.5 <class 'float'>" in out
    assert "Pressure in psi: 108.7785" in out
    assert "Unit CB-0042 runs at 7.50 bar (108.78 psi) and 355.15 K" in out
    assert "Alarm: False" in out


def test_02_ask():
    out = run_ok(SOLUTIONS / "02-variables-and-types" / "ask.py", stdin="7.5\n")
    assert "108.8 psi" in out


def test_02_challenge_parse():
    out = run_ok(SOLUTIONS / "02-variables-and-types" / "parse.py")
    assert "7.5 bar = 108.78 psi" in out
    assert "Unknown unit 'atm'" in out


def test_03_challenge():
    out = run_ok(SOLUTIONS / "03-collections" / "challenge.py")
    assert "'pressure_bar': [7.1, 7.4, 7.6, 7.3]" in out


def test_03_collections():
    out = run_ok(SOLUTIONS / "03-collections" / "collections_intro.py")
    assert "Last: 7.5" in out
    assert "First three: [7.1, 7.3, 7.4]" in out
    assert "Number of readings: 7" in out
    assert "Max: 7.8 Min: 7.1 Mean: 7.414285714285714" in out
    assert "Top three: [7.8, 7.6, 7.5]" in out
    assert "Trimmed mean: 7.4" in out
    assert "Latitude: 52.01 Longitude: 4.36" in out
    assert "'temperature_c': 83.5, 'flow_l_s': 41.5}" in out
    assert "Temperature of second: 81.9" in out
    assert "Pressure of last: 7.6" in out
    assert "Number of measurements: 4" in out
    assert "Unique sensors: 4" in out
    assert "F1 present: True" in out


def test_04_control_flow():
    out = run_ok(SOLUTIONS / "04-control-flow" / "alarms.py")
    assert "8.1 bar -> WARNING" in out
    assert "8.7 bar -> ALARM" in out
    assert "7.3 bar -> OK" in out
    assert "Alarms: 2" in out
    assert "Minutes to alarm: 4" in out
    assert "First alarm reading: 8.7" in out
    assert "Alarm readings (loop): [8.7, 8.6]" in out
    assert "Alarm readings (comprehension): [8.7, 8.6]" in out


def test_04_challenge():
    out = run_ok(SOLUTIONS / "04-control-flow" / "challenge.py")
    assert "start at reading 3" in out
    assert "No three readings in a row above 8.0 bar" in out


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
    assert "10 passed" in result.stdout
    assert "failed" not in result.stdout


def test_05_challenge_convert_tests_pass():
    result = run_pytest(SOLUTIONS / "05-functions" / "test_challenge_convert.py")
    assert result.returncode == 0, result.stdout
    assert "3 passed" in result.stdout


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


def test_06_summarize_runs(tmp_path):
    runs = EXERCISES / "06-standard-library" / "runs"
    assert len(list(runs.glob("*.csv"))) == 3
    out = run_ok(SOLUTIONS / "06-standard-library" / "summarize_runs.py", str(runs), str(tmp_path))
    assert "run_01.csv: 8 rows, mean pressure 7.25 bar" in out
    with open(tmp_path / "summary.json") as file:
        summaries = json.load(file)
    assert [item["run"] for item in summaries] == ["run_01", "run_02", "run_03"]
    assert summaries[0]["rows"] == 8
    assert summaries[0]["pressure_mean_bar"] == pytest.approx(7.25)
    assert summaries[0]["temperature_max_c"] == pytest.approx(82.7)
    with open(tmp_path / "summary.csv", newline="") as file:
        assert len(list(csv.DictReader(file))) == 3


def test_06_solution_runs_match_exercise_runs():
    for path in (EXERCISES / "06-standard-library" / "runs").glob("*.csv"):
        other = SOLUTIONS / "06-standard-library" / "runs" / path.name
        assert other.read_text() == path.read_text()


def test_06_default_paths():
    out = run_ok(SOLUTIONS / "06-standard-library" / "summarize_runs.py")
    assert "run_03.csv" in out
    assert (SOLUTIONS / "06-standard-library" / "output" / "summary.json").exists()


def test_07_summarize_logs_survives_bad_value():
    out = run_ok(SOLUTIONS / "07-files-and-exceptions" / "summarize_logs.py")
    assert "run_02: mean 7.71 bar, 1 rows skipped" in out
    assert "run_01: mean 7.25 bar, 0 rows skipped" in out


def test_06_challenge_warns_on_high_std():
    out = run_ok(
        SOLUTIONS / "06-standard-library" / "challenge.py",
        str(EXERCISES / "06-standard-library" / "runs"),
    )
    assert "Warning: run_01 has a pressure standard deviation of 0.2 bar" in out
    assert "Warning: run_02" not in out


def test_07_challenge_stops_or_skips():
    script = SOLUTIONS / "07-files-and-exceptions" / "challenge.py"
    result = run(script)
    assert result.returncode != 0
    assert result.stderr.strip().splitlines()[-1] == (
        "ValueError: run_02.csv line 4: cannot convert 'ERR'"
    )
    assert "run_02: mean 7.71 bar, 1 rows skipped" in run_ok(script, "--skip")


def test_07_files_and_exceptions():
    out = run_ok(SOLUTIONS / "07-files-and-exceptions" / "files_and_exceptions.py")
    assert "Good values: [7.1, 7.4, 7.2, 7.5]" in out
    assert "Bad lines: ['7,6', 'abc']" in out
    assert "File not found: does_not_exist.txt" in out
    report = SOLUTIONS / "07-files-and-exceptions" / "output" / "report.txt"
    assert report.read_text().splitlines()[-1] == "Bad lines: 2"


@pytest.mark.parametrize(
    ("script", "exception"),
    [
        ("broken_1.py", "NameError"),
        ("broken_2.py", "TypeError"),
        ("broken_3.py", "ValueError"),
    ],
)
def test_07_broken_scripts_fail_as_intended(script, exception):
    result = run(EXERCISES / "07-files-and-exceptions" / script)
    assert result.returncode != 0
    last_line = result.stderr.strip().splitlines()[-1]
    assert last_line.startswith(exception + ":")


def test_07_broken_3_has_multi_frame_traceback():
    result = run(EXERCISES / "07-files-and-exceptions" / "broken_3.py")
    assert result.stderr.count('File "') >= 4


@pytest.mark.parametrize(
    ("script", "expected"),
    [
        ("broken_1_fixed.py", "Highest pressure: 7.6"),
        ("broken_2_fixed.py", "Unit CB-0042 runs at 7.5 bar"),
        ("broken_3_fixed.py", "Average pressure: 7.33 bar"),
    ],
)
def test_07_fixed_scripts_work(script, expected):
    out = run_ok(SOLUTIONS / "07-files-and-exceptions" / script)
    assert expected in out


def test_08_plot(tmp_path):
    target = tmp_path / "pressure.png"
    run_ok(SOLUTIONS / "08-uv-project" / "plot_pressure.py", str(target))
    assert target.exists()
    assert target.read_bytes()[:8] == b"\x89PNG\r\n\x1a\n"


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
        "07-files-and-exceptions/files_and_exceptions.py",
        "08-uv-project/plot_pressure.py",
        "07-files-and-exceptions/summarize_logs.py",
    ],
)
def test_starters_do_not_crash(script, tmp_path):
    args = [str(tmp_path / "x.png")] if script.startswith("08") else []
    result = run(EXERCISES / script, *args)
    assert result.returncode == 0, result.stderr
