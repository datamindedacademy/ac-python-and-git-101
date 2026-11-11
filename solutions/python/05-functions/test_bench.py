"""Tests for bench.py (reference solution).

Run them from the repo root:
    uv run pytest solutions/python/05-functions
"""

import bench
import pytest


def test_parse_reading():
    assert bench.parse_reading("7.5 bar") == (7.5, "bar")
    assert bench.parse_reading("760 kPa") == (760.0, "kPa")


def test_parse_reading_extra_spaces():
    assert bench.parse_reading("  108.8   psi ") == (108.8, "psi")


def test_parse_reading_decimal_comma():
    assert bench.parse_reading("7,5 bar") == (7.5, "bar")


def test_to_bar():
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


# Task 2, part A: the tests you write before the function exists.
def test_classify_ok():
    assert bench.classify(7.2) == "OK"


def test_classify_warning_boundary():
    assert bench.classify(8.0) == "WARNING"
    assert bench.classify(7.99) == "OK"


def test_classify_alarm_boundary():
    assert bench.classify(8.5) == "ALARM"
    assert bench.classify(8.49) == "WARNING"


def test_classify_keyword_limits():
    assert bench.classify(7.2, warning_bar=7.0) == "WARNING"
    assert bench.classify(8.2, alarm_bar=8.0) == "ALARM"
