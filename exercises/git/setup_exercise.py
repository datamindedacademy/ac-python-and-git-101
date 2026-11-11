"""Create a sandbox repository for one of the Git exercises.

Usage (from the root of the course repository):

    uv run python exercises/git/setup_exercise.py <n> [--target FOLDER] [--force]

The sandbox is created OUTSIDE the course repository (default:
~/git-exercises/exercise_<n>) so that Git repositories are never nested.
Only the Python standard library is used, so it runs in Windows PowerShell
with the execution policy set to Restricted, and on Linux.
"""

from __future__ import annotations

import argparse
import os
import shutil
import stat
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
TEMPLATES = HERE / "templates"
COURSE_ROOT = HERE.parent.parent

LOCAL_EXERCISES = (1, 2, 3)
REMOTE_EXERCISES = (4, 5, 6)

DEFAULT_NAME = "Training Participant"
DEFAULT_EMAIL = "participant@example.com"

ANNA = ("Anna Verhoeven", "anna.verhoeven@example.com")
JAN = ("Jan Peeters", "jan.peeters@example.com")
SOFIE = ("Sofie Claes", "sofie.claes@example.com")


class SetupError(Exception):
    """A problem the participant can understand and fix."""


# ---------------------------------------------------------------- git helpers


def git(repo: Path, *args: str, env: dict[str, str] | None = None) -> str:
    """Run a git command in `repo` and return its output. Raise SetupError on failure."""
    full_env = {**os.environ, **(env or {})}
    try:
        result = subprocess.run(
            ["git", *args],
            cwd=repo,
            env=full_env,
            capture_output=True,
            text=True,
            encoding="utf-8",
        )
    except FileNotFoundError:
        raise SetupError(
            "Could not find git. Close and reopen PowerShell, then run `git --version`."
        ) from None
    if result.returncode != 0:
        raise SetupError(f"git {' '.join(args)} failed:\n{result.stderr.strip()}")
    return result.stdout


def init_repo(repo: Path) -> None:
    """Create a repository with the branch `main`, regardless of the user's settings."""
    git(repo, "init", "-b", "main")
    # Only set a local identity when there is none, so the participant's own wins.
    if not git_config_value(repo, "user.name"):
        git(repo, "config", "user.name", DEFAULT_NAME)
    if not git_config_value(repo, "user.email"):
        git(repo, "config", "user.email", DEFAULT_EMAIL)


def git_config_value(repo: Path, key: str) -> str:
    result = subprocess.run(
        ["git", "config", "--get", key], cwd=repo, capture_output=True, text=True
    )
    return result.stdout.strip()


def overlay(template: str, repo: Path) -> None:
    """Copy a template folder over the repository, normalising line endings to LF."""
    source = TEMPLATES / template
    for path in sorted(source.rglob("*")):
        if not path.is_file():
            continue
        destination = repo / path.relative_to(source)
        destination.parent.mkdir(parents=True, exist_ok=True)
        text = path.read_bytes().replace(b"\r\n", b"\n")
        destination.write_bytes(text)


def commit(repo: Path, message: str, author: tuple[str, str], date: str) -> None:
    """Stage everything and commit with a fixed author and date."""
    name, email = author
    env = {
        "GIT_AUTHOR_NAME": name,
        "GIT_AUTHOR_EMAIL": email,
        "GIT_AUTHOR_DATE": date,
        "GIT_COMMITTER_NAME": name,
        "GIT_COMMITTER_EMAIL": email,
        "GIT_COMMITTER_DATE": date,
    }
    git(repo, "add", "--all")
    git(repo, "-c", "commit.gpgsign=false", "commit", "-m", message, env=env)


# ------------------------------------------------------------------ exercises


def setup_1(repo: Path) -> None:
    """Two loose files, no repository. The participant runs `git init`."""
    overlay("ex1", repo)


def setup_2(repo: Path) -> None:
    """A repository with five commits by three authors."""
    init_repo(repo)
    steps = [
        ("step1", "Add bar to psi conversion", ANNA, "2025-03-03T09:15:00+01:00"),
        ("step2", "Add Celsius to Kelvin conversion", ANNA, "2025-03-03T11:40:00+01:00"),
        ("step3", "Add measurements and analyse_run script", JAN, "2025-03-04T10:05:00+01:00"),
        ("step4", "Fix Kelvin offset", SOFIE, "2025-03-05T14:20:00+01:00"),
        ("step5", "Use more precise bar to psi factor", JAN, "2025-03-06T08:55:00+01:00"),
    ]
    for step, message, author, date in steps:
        overlay(f"ex2/{step}", repo)
        commit(repo, message, author, date)


def setup_3(repo: Path) -> None:
    """Four commits on main plus two prepared side branches."""
    init_repo(repo)
    steps = [
        ("step1", "Add unit conversions", ANNA, "2025-03-03T09:15:00+01:00"),
        ("step2", "Add measurements and analyse_run script", ANNA, "2025-03-03T11:40:00+01:00"),
        ("step3", "Add README", JAN, "2025-03-04T10:05:00+01:00"),
    ]
    for step, message, author, date in steps:
        overlay(f"ex3/{step}", repo)
        commit(repo, message, author, date)

    # A branch with three commits, for the rebase task. Its second commit appends to
    # conversions.py, where the participant also appends on main, so the rebase conflicts.
    git(repo, "switch", "-c", "feature/temperature-report")
    for step, message, date in [
        ("feature1", "Print min temperature", "2025-03-04T14:00:00+01:00"),
        ("feature2", "Add Celsius to Fahrenheit conversion", "2025-03-04T15:30:00+01:00"),
        ("feature3", "Print mean temperature in Fahrenheit", "2025-03-04T16:45:00+01:00"),
    ]:
        overlay(f"ex3/{step}", repo)
        commit(repo, message, SOFIE, date)

    # A side branch that changes the same line as main will change later.
    git(repo, "switch", "main")
    git(repo, "switch", "-c", "experiment/psi-precision")
    overlay("ex3/branch", repo)
    commit(repo, "Try a more precise psi factor", SOFIE, "2025-03-05T09:30:00+01:00")

    git(repo, "switch", "main")
    overlay("ex3/main4", repo)
    commit(repo, "Round psi factor to 3 decimals", JAN, "2025-03-05T15:10:00+01:00")


SETUPS = {1: setup_1, 2: setup_2, 3: setup_3}

INTRO = {
    1: "Exercise 1: two files, no repository yet. You create the repository.",
    2: "Exercise 2: a repository with 5 commits to explore.",
    3: "Exercise 3: a repository with 4 commits on main and two prepared side branches.",
}


# ------------------------------------------------------------------- plumbing


def remove_tree(path: Path) -> None:
    """Delete a folder, including read-only files (needed for .git on Windows)."""

    def on_error(func, failed_path, _exc):
        os.chmod(failed_path, stat.S_IWRITE)
        func(failed_path)

    shutil.rmtree(path, onexc=on_error)


def check_target(target: Path) -> None:
    home = Path.home().resolve()
    if target == home or target == Path(target.anchor):
        raise SetupError(f"Refusing to use {target} as an exercise folder.")
    if target == COURSE_ROOT or COURSE_ROOT in target.parents:
        raise SetupError(
            f"{target} is inside the course repository.\n"
            "Do not nest Git repositories. Use the default folder or pick one outside."
        )
    if target in COURSE_ROOT.parents:
        raise SetupError(f"Refusing to use {target}: it contains the course repository.")
    if target == Path.cwd().resolve():
        raise SetupError(f"Refusing to use {target}: it is the folder you are in.")


def parse_args(argv: list[str] | None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create a sandbox repository for a Git exercise.",
    )
    parser.add_argument("exercise", type=int, choices=range(1, 7), metavar="n", help="1 to 6")
    parser.add_argument(
        "--target",
        type=Path,
        help="folder to create (default: ~/git-exercises/exercise_<n>)",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="delete the folder first if it already exists",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    n = args.exercise

    if n in REMOTE_EXERCISES:
        print(f"Exercise {n} does not need a setup script.")
        print("You work in your clone of the training repository on the forge.")
        print("Follow the README of the exercise.")
        return 0

    target = args.target or Path.home() / "git-exercises" / f"exercise_{n}"
    target = target.expanduser().resolve()

    try:
        check_target(target)
        if target.exists() and any(target.iterdir()):
            if not args.force:
                raise SetupError(
                    f"The folder {target} already exists.\n"
                    "Use --force to delete it and start again."
                )
            remove_tree(target)
        target.mkdir(parents=True, exist_ok=True)
        SETUPS[n](target)
    except SetupError as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1

    print(INTRO[n])
    print(f"Created: {target}")
    print()
    print("Next, run this command:")
    print(f'  cd "{target}"')
    return 0


if __name__ == "__main__":
    sys.exit(main())
