"""Tests for convert() in units.py (reference solution)."""

import pytest
from units import UNITS, convert


def test_pressure():
    assert convert(7.5, "bar", "psi") == pytest.approx(108.7785)
    assert convert(100, "kPa", "bar") == pytest.approx(1.0)


def test_temperature():
    assert convert(100, "degC", "degF") == pytest.approx(212.0)
    assert convert(0, "K", "degC") == pytest.approx(-273.15)
    assert convert(32, "degF", "K") == pytest.approx(273.15)


def test_unknown_unit_raises():
    with pytest.raises(ValueError):
        convert(1, "bar", "atm")
    with pytest.raises(ValueError):
        convert(1, "atm", "bar")


def test_mixed_families_raise():
    with pytest.raises(ValueError):
        convert(1, "bar", "K")
    with pytest.raises(ValueError):
        convert(1, "degF", "psi")


def test_round_trip_every_pair():
    for a in UNITS:
        for b in UNITS:
            if UNITS[a][0] == UNITS[b][0]:
                assert convert(convert(12.5, a, b), b, a) == pytest.approx(12.5)
