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
    assert branches(target) == {"main", "experiment/psi-precision"}
    assert git(target, "branch", "--show-current").stdout.strip() == "main"
    assert commit_count(target, "main") == 4
    assert commit_count(target, "experiment/psi-precision") == 4
    assert git(target, "status", "--porcelain").stdout == ""

    # Work on a copy so the sandbox stays untouched.
    copy = tmp_path / "ex3-copy"
    shutil.copytree(target, copy)
    merge = git(copy, "merge", "--no-edit", "experiment/psi-precision", check=False)
    assert merge.returncode != 0
    unmerged = git(copy, "diff", "--name-only", "--diff-filter=U").stdout.split()
    assert unmerged == ["conversions.py"]
    assert "<<<<<<<" in (copy / "conversions.py").read_text()


def test_exercise_3_ff_and_merge_commit_paths_work(env, tmp_path):
    """The commands in the README for exercise 3 must not conflict with the prepared branch."""
    target = tmp_path / "ex3"
    run_setup(3, target)
    git(target, "switch", "-c", "feature/pressure-kpa")
    with (target / "conversions.py").open("a") as file:
        file.write("\n\ndef bar_to_kpa(pressure_bar):\n    return pressure_bar * 100\n")
    git(target, "add", "conversions.py")
    git(target, "commit", "-m", "Add bar to kPa conversion")
    git(target, "switch", "main")
    assert "Fast-forward" in git(target, "merge", "feature/pressure-kpa").stdout

    git(target, "switch", "-c", "feature/max-temperature")
    with (target / "analyse_run.py").open("a") as file:
        file.write("\n# max temperature\n")
    git(target, "commit", "-am", "Print max temperature")
    git(target, "switch", "main")
    with (target / "README.md").open("a") as file:
        file.write("More notes.\n")
    git(target, "commit", "-am", "Explain how to run analyse_run.py")
    git(target, "merge", "feature/max-temperature", "--no-edit")
    parents = git(target, "rev-list", "--parents", "-n", "1", "HEAD").stdout.split()
    assert len(parents) == 3  # the commit itself plus two parents


def _ff_merge_kpa(target):
    """The fast-forward merge of core task 3."""
    git(target, "switch", "-c", "feature/pressure-kpa")
    with (target / "conversions.py").open("a") as file:
        file.write("\n\ndef bar_to_kpa(pressure_bar):\n    return pressure_bar * 100\n")
    git(target, "commit", "-am", "Add bar to kPa conversion")
    git(target, "switch", "main")
    git(target, "merge", "feature/pressure-kpa")
    git(target, "branch", "-d", "feature/pressure-kpa")


def test_exercise_3_conflict_after_fast_forward_and_resolve(env, tmp_path):
    """Core task 4: after task 3, merging experiment/psi-precision conflicts and can be resolved."""
    target = tmp_path / "ex3"
    run_setup(3, target)
    _ff_merge_kpa(target)
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


def test_exercise_3_rebase_flow_after_core_tasks(env, tmp_path):
    """Optional rebase task, started after the conflict merge of core task 4."""
    target = tmp_path / "ex3"
    run_setup(3, target)
    _ff_merge_kpa(target)
    git(target, "merge", "experiment/psi-precision", check=False)
    git(target, "checkout", "--theirs", "conversions.py")
    git(target, "commit", "-am", "Merge experiment/psi-precision")

    git(target, "switch", "-c", "feature/min-temperature")
    path = target / "analyse_run.py"
    path.write_text(
        path.read_text().replace(
            "K)\")\n",
            "K)\")\n    print(f\"Min temperature: {min(temperatures):.1f} C\")\n",
        )
    )
    git(target, "commit", "-am", "Print min temperature")
    before = git(target, "rev-parse", "HEAD").stdout
    git(target, "switch", "main")
    with (target / "README.md").open("a") as file:
        file.write("Output: mean pressure and temperature.\n")
    git(target, "commit", "-am", "Describe the output in the README")
    git(target, "switch", "feature/min-temperature")
    git(target, "rebase", "main")
    assert git(target, "rev-parse", "HEAD").stdout != before
    git(target, "switch", "main")
    assert "Fast-forward" in git(target, "merge", "feature/min-temperature").stdout
    git(target, "branch", "-d", "feature/min-temperature")
    assert git(target, "status", "--porcelain").stdout == ""


def test_exercise_3_stash_challenge(env, tmp_path):
    target = tmp_path / "ex3"
    run_setup(3, target)
    (target / "conversions.py").write_text("# half finished\n")
    git(target, "switch", "experiment/psi-precision", check=False)  # refused: would be overwritten
    git(target, "stash")
    assert git(target, "status", "--porcelain").stdout == ""
    git(target, "switch", "experiment/psi-precision")
    git(target, "switch", "main")
    git(target, "stash", "pop")
    assert (target / "conversions.py").read_text() == "# half finished\n"


def test_exercise_2_revert_challenge_applies_cleanly(env, tmp_path):
    """The challenge reverts the newest commit by its message."""
    target = tmp_path / "ex2"
    run_setup(2, target)
    sha = git(target, "log", "--grep=Use more precise", "--format=%h").stdout.strip()
    git(target, "revert", "--no-edit", sha)
    assert commit_count(target) == 6
    assert "BAR_TO_PSI = 14.5\n" in (target / "conversions.py").read_text()


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
