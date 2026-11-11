"""Tests for convert() in conversions.py (challenge, reference solution)."""

import conversions
import pytest


def test_convert_bar_to_psi():
    assert conversions.convert(7.5, "bar", "psi") == pytest.approx(108.7785)


def test_convert_kpa_to_bar_and_back():
    assert conversions.convert(100, "kPa", "bar") == pytest.approx(1.0)
    assert conversions.convert(1, "bar", "kPa") == pytest.approx(100.0)


def test_convert_unknown_unit_raises():
    with pytest.raises(ValueError):
        conversions.convert(1, "bar", "atm")
    with pytest.raises(ValueError):
        conversions.convert(1, "atm", "bar")
