"""Tests for exercises/git/setup_exercise.py (the sandbox repositories for the Git exercises)."""

import shutil
import subprocess
import sys
from pathlib import Path

import pytest

SCRIPT = Path(__file__).resolve().parent.parent / "exercises" / "git" / "setup_exercise.py"


@pytest.fixture
def env(tmp_path, monkeypatch):
    """A git environment with no identity, so tests pass on a machine without git config."""
    global_config = tmp_path / "gitconfig"
    global_config.write_text("")
    monkeypatch.setenv("GIT_CONFIG_GLOBAL", str(global_config))
    monkeypatch.setenv("GIT_CONFIG_NOSYSTEM", "1")
    monkeypatch.setenv("HOME", str(tmp_path / "home"))
    monkeypatch.setenv("USERPROFILE", str(tmp_path / "home"))
    for who in ("AUTHOR", "COMMITTER"):
        monkeypatch.setenv(f"GIT_{who}_NAME", "Test User")
        monkeypatch.setenv(f"GIT_{who}_EMAIL", "test@example.com")


def run_setup(n, target, *extra):
    return subprocess.run(
        [sys.executable, str(SCRIPT), str(n), "--target", str(target), *extra],
        capture_output=True,
        text=True,
    )


def git(repo, *args, check=True):
    result = subprocess.run(["git", *args], cwd=repo, capture_output=True, text=True)
    if check:
        assert result.returncode == 0, result.stderr
    return result


def commit_count(repo, ref="HEAD"):
    return int(git(repo, "rev-list", "--count", ref).stdout.strip())


def branches(repo):
    out = git(repo, "branch", "--format=%(refname:short)").stdout
    return set(out.split())


def test_exercise_1_has_files_but_no_repository(env, tmp_path):
    target = tmp_path / "ex1"
    result = run_setup(1, target)
    assert result.returncode == 0, result.stderr
    assert (target / "conversions.py").is_file()
    assert (target / "measurements.csv").is_file()
    assert not (target / ".git").exists()
    assert f'cd "{target}"' in result.stdout


def test_exercise_1_core_flow(env, tmp_path):
    """The three tasks of exercise 1, ending with six commits and a clean tree."""
    target = tmp_path / "ex1"
    run_setup(1, target)
    git(target, "init", "-b", "main")
    status = git(target, "status").stdout
    assert "No commits yet" in status
    assert "conversions.py" in status and "measurements.csv" in status

    # Task 1: two commits.
    git(target, "add", "conversions.py")
    git(target, "commit", "-m", "Add bar to psi conversion")
    assert commit_count(target) == 1
    assert git(target, "status", "--short").stdout.strip() == "?? measurements.csv"
    git(target, "add", "measurements.csv")
    git(target, "commit", "-m", "Add first measurements")

    # Task 2: two unrelated changes.
    with (target / "conversions.py").open("a") as file:
        file.write(
            "\n\ndef celsius_to_kelvin(temperature_c):\n"
            '    """Convert a temperature from degrees Celsius to Kelvin."""\n'
            "    return temperature_c + 273.15\n"
        )
    with (target / "measurements.csv").open("a") as file:
        file.write("4,8.5,91.2\n")
    assert git(target, "status", "--short").stdout.splitlines() == [
        " M conversions.py",
        " M measurements.csv",
    ]

    # Two commits. After staging, plain diff and staged diff show different files.
    git(target, "add", "conversions.py")
    assert "measurements.csv" in git(target, "diff").stdout
    assert "conversions.py" not in git(target, "diff").stdout
    assert "celsius_to_kelvin" in git(target, "diff", "--staged").stdout
    git(target, "commit", "-m", "Add Celsius to Kelvin conversion")
    git(target, "add", "measurements.csv")
    git(target, "commit", "-m", "Add fourth measurement run")
    assert commit_count(target) == 4
    assert git(target, "status", "--porcelain").stdout == ""

    # Task 3: two edits in one file, hunk by hunk, then fix the message of the earlier commit.
    path = target / "conversions.py"
    path.write_text(
        path.read_text().replace("test bench.", "test bench (pressure and temperature).", 1)
        + "\n\ndef kelvin_to_celsius(temperature_k):\n"
        '    """Convert a temperature from Kelvin to degrees Celsius."""\n'
        "    return temperature_k - 273.15\n"
    )

    def add_function_hunk():
        # Hunks come in file order: n for the docstring, y for the new function.
        result = subprocess.run(
            ["git", "add", "-p", "conversions.py"],
            cwd=target,
            input="n\ny\n",
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0, result.stderr

    add_function_hunk()
    assert "kelvin_to_celsius" in git(target, "diff", "--staged").stdout
    assert "pressure and temperature" not in git(target, "diff", "--staged").stdout
    git(target, "commit", "-m", "Add kelvin_to_celcius")
    git(target, "add", "conversions.py")
    git(target, "commit", "-m", "Reword the module docstring")
    git(target, "reset", "--soft", "HEAD~2")
    git(target, "reset")
    add_function_hunk()
    git(target, "commit", "-m", "Add kelvin_to_celsius")
    git(target, "add", "conversions.py")
    git(target, "commit", "-m", "Reword the module docstring")
    assert git(target, "log", "--format=%s", "-2").stdout.splitlines() == [
        "Reword the module docstring",
        "Add kelvin_to_celsius",
    ]
    assert commit_count(target) == 6
    assert "pressure and temperature" not in git(target, "show", "HEAD~1").stdout
    assert "kelvin_to_celsius" not in git(target, "show", "HEAD").stdout
    assert git(target, "status", "--porcelain").stdout == ""


def test_exercise_2_history(env, tmp_path):
    target = tmp_path / "ex2"
    result = run_setup(2, target)
    assert result.returncode == 0, result.stderr
    assert (target / ".git").is_dir()
    assert commit_count(target) == 5
    assert branches(target) == {"main"}
    assert git(target, "status", "--porcelain").stdout == ""
    messages = git(target, "log", "--format=%s").stdout.splitlines()
    assert messages[0] == "Use more precise bar to psi factor"
    assert messages[-1] == "Add bar to psi conversion"
    # Three different authors, as the exercise questions assume.
    authors = set(git(target, "log", "--format=%an").stdout.splitlines())
    assert authors == {"Anna Verhoeven", "Jan Peeters", "Sofie Claes"}
    # The Kelvin fix is the only commit that touched the value 273.15.
    found = git(target, "log", "-S", "273.15", "--format=%an|%s").stdout.splitlines()
    assert found == ["Sofie Claes|Fix Kelvin offset"]
    # A local identity was set because none was configured.
    assert git(target, "config", "--local", "user.name").stdout.strip()


def test_exercise_2_is_deterministic(env, tmp_path):
    run_setup(2, tmp_path / "a")
    run_setup(2, tmp_path / "b")
    head_a = git(tmp_path / "a", "rev-parse", "HEAD").stdout
    head_b = git(tmp_path / "b", "rev-parse", "HEAD").stdout
    assert head_a == head_b


def test_exercise_3_branches_and_conflict(env, tmp_path):
    target = tmp_path / "ex3"
    result = run_setup(3, target)
    assert result.returncode == 0, result.stderr
    assert branches(target) == {"main", "experiment/psi-precision", "feature/temperature-report"}
    assert git(target, "branch", "--show-current").stdout.strip() == "main"
    assert commit_count(target, "main") == 4
    assert commit_count(target, "experiment/psi-precision") == 4
    assert commit_count(target, "feature/temperature-report") == 6
    assert git(target, "status", "--porcelain").stdout == ""

    # Work on a copy so the sandbox stays untouched.
    copy = tmp_path / "ex3-copy"
    shutil.copytree(target, copy)
    merge = git(copy, "merge", "--no-edit", "experiment/psi-precision", check=False)
    assert merge.returncode != 0
    unmerged = git(copy, "diff", "--name-only", "--diff-filter=U").stdout.split()
    assert unmerged == ["conversions.py"]
    assert "<<<<<<<" in (copy / "conversions.py").read_text()


def _ff_merge_kpa(target):
    """Task 1: branch, commit, fast-forward merge, delete the branch."""
    git(target, "switch", "-c", "feature/pressure-kpa")
    with (target / "conversions.py").open("a") as file:
        file.write(
            '\n\ndef bar_to_kpa(pressure_bar):\n    """Convert a pressure from bar to kPa."""\n'
            "    return pressure_bar * 100\n"
        )
    git(target, "commit", "-am", "Add bar to kPa conversion")
    git(target, "switch", "main")
    assert "Fast-forward" in git(target, "merge", "feature/pressure-kpa").stdout
    git(target, "branch", "-d", "feature/pressure-kpa")


def _resolve_conflict(target):
    """Task 2: merge experiment/psi-precision, keep the incoming BAR_TO_PSI line."""
    merge = git(target, "merge", "experiment/psi-precision", check=False)
    assert merge.returncode != 0
    unmerged = git(target, "diff", "--name-only", "--diff-filter=U").stdout.split()
    assert unmerged == ["conversions.py"]
    text = (target / "conversions.py").read_text()
    assert "<<<<<<< HEAD" in text and ">>>>>>> experiment/psi-precision" in text
    # Accept the incoming line, as the README suggests.
    resolved = "BAR_TO_PSI = 14.5038  # psi per bar, more precise"
    lines = [
        resolved if line.startswith("BAR_TO_PSI = 14.504 ") else line
        for line in text.splitlines()
        if not line.startswith(("<<<<<<<", "=======", ">>>>>>>", "BAR_TO_PSI = 14.5038"))
    ]
    (target / "conversions.py").write_text("\n".join(lines) + "\n")
    git(target, "add", "conversions.py")
    git(target, "commit", "-m", "Merge experiment/psi-precision")
    parents = git(target, "rev-list", "--parents", "-n", "1", "HEAD").stdout.split()
    assert len(parents) == 3


def test_exercise_3_tasks_1_and_2_conflict_and_resolve(env, tmp_path):
    target = tmp_path / "ex3"
    run_setup(3, target)
    _ff_merge_kpa(target)
    _resolve_conflict(target)
    text = (target / "conversions.py").read_text()
    assert "BAR_TO_PSI = 14.5038" in text and "def bar_to_kpa" in text and "<<<<" not in text


def test_exercise_3_task_3_rebase_conflicts_and_continues(env, tmp_path):
    """Task 3, after tasks 1 and 2: dirty tree, rebase conflict, continue, fast-forward."""
    target = tmp_path / "ex3"
    run_setup(3, target)
    _ff_merge_kpa(target)
    _resolve_conflict(target)
    before = git(target, "rev-parse", "feature/temperature-report").stdout

    with (target / "README.md").open("a") as file:
        file.write("TODO: check the units\n")
    git(target, "switch", "feature/temperature-report")
    refused = git(target, "rebase", "main", check=False)
    assert refused.returncode != 0 and "unstaged changes" in refused.stderr
    git(target, "stash")
    stopped = git(target, "rebase", "main", check=False)
    assert stopped.returncode != 0 and "CONFLICT" in stopped.stdout
    text = (target / "conversions.py").read_text()
    assert "def bar_to_kpa" in text and "def celsius_to_fahrenheit" in text
    keep_both = [line for line in text.splitlines() if not line.startswith(("<<<<<<<", ">>>>>>>"))]
    (target / "conversions.py").write_text("\n".join(keep_both).replace("=======", "\n") + "\n")
    git(target, "add", "conversions.py")
    git(target, "-c", "core.editor=true", "rebase", "--continue")
    assert git(target, "rev-parse", "HEAD").stdout != before

    git(target, "switch", "main")
    assert "Fast-forward" in git(target, "merge", "feature/temperature-report").stdout
    git(target, "branch", "-d", "feature/temperature-report")
    git(target, "stash", "pop")
    assert git(target, "status", "--porcelain").stdout == " M README.md\n"
    subjects = git(target, "log", "--format=%s", "-3").stdout.splitlines()
    assert subjects == [
        "Print mean temperature in Fahrenheit",
        "Add Celsius to Fahrenheit conversion",
        "Print min temperature",
    ]
    # linear on top of the merge commit: no merge commit among the three
    assert git(target, "rev-list", "--merges", "HEAD~3..HEAD").stdout == ""
    run = subprocess.run(
        [sys.executable, "analyse_run.py"], cwd=target, capture_output=True, text=True
    )
    assert run.returncode == 0, run.stderr
    assert "Min temperature" in run.stdout and " F" in run.stdout


def test_exercise_2_revert_in_the_middle_conflicts(env, tmp_path):
    """Task 3 reverts "Fix Kelvin offset", which conflicts with the later psi commit."""
    target = tmp_path / "ex2"
    run_setup(2, target)
    sha = git(target, "log", "--grep=Fix Kelvin", "--format=%h").stdout.strip()
    result = git(target, "revert", "--no-edit", sha, check=False)
    assert result.returncode != 0
    assert git(target, "status", "--short").stdout.strip() == "UU conversions.py"
    path = target / "conversions.py"
    text = path.read_text()
    start = text.index("<<<<<<<")
    end = text.index("\n", text.index(">>>>>>>")) + 1
    path.write_text(text[:start] + "BAR_TO_PSI = 14.5038\nKELVIN_OFFSET = 273.0\n" + text[end:])
    git(target, "add", "conversions.py")
    git(target, "revert", "--continue", "--no-edit")
    assert commit_count(target) == 6
    assert git(target, "log", "--format=%s", "-1").stdout.strip() == 'Revert "Fix Kelvin offset"'
    assert "KELVIN_OFFSET = 273.0\n" in path.read_text()
    assert git(target, "status", "--porcelain").stdout == ""


@pytest.mark.parametrize("n", [1, 2, 3])
def test_rerun_without_force_fails_and_force_works(env, tmp_path, n):
    target = tmp_path / f"ex{n}"
    assert run_setup(n, target).returncode == 0
    marker = target / "my_work.txt"
    marker.write_text("do not delete me")

    again = run_setup(n, target)
    assert again.returncode != 0
    assert "--force" in again.stderr
    assert marker.exists()

    forced = run_setup(n, target, "--force")
    assert forced.returncode == 0, forced.stderr
    assert not marker.exists()


def test_refuses_target_inside_course_repo(env):
    inside = SCRIPT.parent / "sandbox-should-not-exist"
    result = run_setup(2, inside)
    assert result.returncode != 0
    assert not inside.exists()


@pytest.mark.parametrize("n", [4, 5, 6])
def test_remote_exercises_need_no_setup(env, tmp_path, n):
    target = tmp_path / f"ex{n}"
    result = run_setup(n, target)
    assert result.returncode == 0
    assert not target.exists()
