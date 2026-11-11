"""Tests for bench.py.

Run them from the repo root:
    uv run pytest exercises/python/05-functions

A test is a function whose name starts with test_. It calls your code and
states with `assert` what the result must be. If the statement after `assert`
is false, the test fails.
"""

import bench
import pytest

# pytest.approx compares floats with a tiny tolerance, because floats can have
# small rounding errors (0.1 + 0.2 is not exactly 0.3).


def test_parse_reading():
    assert bench.parse_reading("7.5 bar") == (7.5, "bar")
    assert bench.parse_reading("760 kPa") == (760.0, "kPa")


def test_parse_reading_extra_spaces():
    assert bench.parse_reading("  108.8   psi ") == (108.8, "psi")


def test_parse_reading_decimal_comma():
    assert bench.parse_reading("7,5 bar") == (7.5, "bar")


def test_to_bar():
    # This function is already written, so this test passes.
    assert bench.to_bar(14.5038, "psi") == pytest.approx(1.0)
    assert bench.to_bar(760, "kPa") == pytest.approx(7.6)
    assert bench.to_bar(7.5, "bar") == 7.5


def test_to_bar_default_unit_is_bar():
    assert bench.to_bar(7.5) == 7.5


def test_summarize_odd_count():
    assert bench.summarize([7.4, 7.1, 7.2]) == {
        "count": 3,
        "min": 7.1,
        "max": 7.4,
        "mean": 7.23,
        "median": 7.2,
    }


def test_summarize_even_count():
    assert bench.summarize([7.0, 9.0, 8.0, 7.2]) == {
        "count": 4,
        "min": 7.0,
        "max": 9.0,
        "mean": 7.8,
        "median": 7.6,
    }


def test_summarize_decimals():
    result = bench.summarize([7.1, 7.3, 7.9], decimals=1)
    assert result == {"count": 3, "min": 7.1, "max": 7.9, "mean": 7.4, "median": 7.3}


def test_summarize_empty():
    assert bench.summarize([]) == {"count": 0}


# Task 2, part A: write your tests for classify here, BEFORE you write it.
# The function does not exist yet. Run the tests: they must fail first.
