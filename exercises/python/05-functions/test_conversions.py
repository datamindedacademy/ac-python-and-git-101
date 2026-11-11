"""Tests for conversions.py.

Run them from the repo root:
    uv run pytest exercises/python/05-functions

A test is a function whose name starts with test_. It calls your code and
states with `assert` what the result must be. If the statement after `assert`
is false, the test fails.
"""

import conversions
import pytest

# pytest.approx compares floats with a tiny tolerance, because floats can have
# small rounding errors (0.1 + 0.2 is not exactly 0.3).


def test_l_s_to_m3_h():
    # This function is already written, so this test passes.
    assert conversions.l_s_to_m3_h(10) == pytest.approx(36.0)


def test_bar_to_psi():
    assert conversions.bar_to_psi(1) == pytest.approx(14.5038)
    assert conversions.bar_to_psi(7.5) == pytest.approx(108.7785)


def test_celsius_to_kelvin():
    assert conversions.celsius_to_kelvin(0) == pytest.approx(273.15)
    assert conversions.celsius_to_kelvin(82) == pytest.approx(355.15)


def test_average():
    assert conversions.average([7.0, 8.0]) == 7.5


def test_average_rounds_to_decimals():
    values = [7.1, 7.2, 7.4]
    assert conversions.average(values) == 7.23
    assert conversions.average(values, decimals=1) == 7.2


# TODO 4: write your own test here, BEFORE you write the function.
# The function psi_to_bar does not exist yet. Name your test test_psi_to_bar.
# Decide what the function must return. One known value: 14.5038 psi is 1 bar.
# Run the tests: your new test must fail before you write the function.
