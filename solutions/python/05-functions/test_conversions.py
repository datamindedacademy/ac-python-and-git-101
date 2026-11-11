"""Tests for conversions.py (reference solution).

Run them from the repo root:
    uv run pytest solutions/python/05-functions
"""

import conversions
import pytest


def test_l_s_to_m3_h():
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


# Task 2: the test you write before the function exists.
def test_psi_to_bar():
    assert conversions.psi_to_bar(14.5038) == pytest.approx(1.0)
    assert conversions.psi_to_bar(0) == 0
    # Converting there and back gives the value you started with.
    assert conversions.psi_to_bar(conversions.bar_to_psi(7.5)) == pytest.approx(7.5)
