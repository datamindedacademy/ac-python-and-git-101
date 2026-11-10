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
    assert "Pressure in psi: 108.7785" in out
    assert "Temperature in K: 355.15" in out
    assert "Unit CB-0042 runs at 7.50 bar and 82.0 C" in out
    assert "Alarm: False" in out


def test_02_ask():
    out = run_ok(SOLUTIONS / "02-variables-and-types" / "ask.py", stdin="7.5\n")
    assert "108.8 psi" in out


def test_03_collections():
    out = run_ok(SOLUTIONS / "03-collections" / "collections_intro.py")
    assert "Last: 7.5" in out
    assert "First three: [7.1, 7.3, 7.4]" in out
    assert "Number of readings: 7" in out
    assert "Mean: 7.414285714285714" in out
    assert "Temperature of second: 81.9" in out
    assert "Pressures: [7.1, 7.4, 7.6]" in out
    assert "Unique sensors: 4" in out


def test_04_control_flow():
    out = run_ok(SOLUTIONS / "04-control-flow" / "alarms.py")
    assert "8.1 bar -> WARNING" in out
    assert "8.7 bar -> ALARM" in out
    assert "7.3 bar -> OK" in out
    assert "Alarms: 2" in out
    assert "Minutes to alarm: 4" in out
    assert "First alarm reading: 8.7" in out


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


def test_06_stats():
    run_ok(SOLUTIONS / "06-standard-library" / "stats.py")
    path = SOLUTIONS / "06-standard-library" / "output" / "summary.json"
    with open(path) as file:
        summary = json.load(file)
    assert summary["rows"] == 10
    assert summary["pressure_mean_bar"] == pytest.approx(7.43)
    assert summary["pressure_std_bar"] == pytest.approx(0.21, abs=0.005)
    assert summary["temperature_max_c"] == pytest.approx(84.6)


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


def test_09_data_files_exist():
    data = EXERCISES / "09-automation-capstone" / "data"
    assert len(list(data.glob("*.csv"))) == 6


def test_09_generator_is_deterministic(tmp_path):
    # The committed CSV files must match what the generator makes.
    import importlib.util

    path = EXERCISES / "09-automation-capstone" / "generate_data.py"
    spec = importlib.util.spec_from_file_location("generate_data", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    rows = module.make_rows(1, module.RUNS["run_01"])
    with open(EXERCISES / "09-automation-capstone" / "data" / "run_01.csv", newline="") as file:
        committed = list(csv.reader(file))
    assert committed[0] == module.HEADER
    assert committed[1:] == rows


def test_09_capstone_summary(tmp_path):
    data = EXERCISES / "09-automation-capstone" / "data"
    out = run_ok(
        SOLUTIONS / "09-automation-capstone" / "summarize_runs.py", str(data), str(tmp_path)
    )
    assert "Summarised 5 runs, skipped 1 files." in out

    with open(tmp_path / "summary.csv", newline="") as file:
        rows = list(csv.DictReader(file))
    by_run = {row["run"]: row for row in rows}
    assert sorted(by_run) == ["run_01", "run_02", "run_03", "run_04", "run_05"]
    assert by_run["run_03"]["rows_skipped"] == "1"
    assert by_run["run_05"]["rows_skipped"] == "1"
    assert by_run["run_03"]["rows_used"] == "19"
    assert {name: int(row["alarm_count"]) for name, row in by_run.items()} == {
        "run_01": 0,
        "run_02": 3,
        "run_03": 0,
        "run_04": 1,
        "run_05": 0,
    }

    with open(tmp_path / "summary.json") as file:
        result = json.load(file)
    assert result["skipped_files"] == ["run_06.csv"]
    assert len(result["runs"]) == 5
    run_01 = result["runs"][0]
    assert run_01["pressure_min_bar"] <= run_01["pressure_mean_bar"] <= run_01["pressure_max_bar"]


def test_09_capstone_default_paths():
    out = run_ok(SOLUTIONS / "09-automation-capstone" / "summarize_runs.py")
    assert "Summarised 5 runs" in out
    assert (SOLUTIONS / "09-automation-capstone" / "output" / "summary.csv").exists()


@pytest.mark.parametrize(
    "script",
    [
        "01-first-script/hello.py",
        "02-variables-and-types/units.py",
        "03-collections/collections_intro.py",
        "04-control-flow/alarms.py",
        "05-functions/conversions.py",
        "05-functions/report.py",
        "06-standard-library/stats.py",
        "07-files-and-exceptions/files_and_exceptions.py",
        "08-uv-project/plot_pressure.py",
        "09-automation-capstone/summarize_runs.py",
    ],
)
def test_starters_do_not_crash(script, tmp_path):
    args = [str(tmp_path / "x.png")] if script.startswith("08") else []
    result = run(EXERCISES / script, *args)
    assert result.returncode == 0, result.stderr
