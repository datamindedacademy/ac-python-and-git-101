"""Convert a value between units of the same family (pressure or temperature)."""

BAR_TO_PSI = 14.5038

# unit: (family, factor, offset). Base value (bar or K) = value * factor + offset.
UNITS = {
    "bar": ("pressure", 1.0, 0.0),
    "psi": ("pressure", 1 / BAR_TO_PSI, 0.0),
    "kPa": ("pressure", 0.01, 0.0),
    "K": ("temperature", 1.0, 0.0),
    "degC": ("temperature", 1.0, 273.15),
    "degF": ("temperature", 5 / 9, 273.15 - 32 * 5 / 9),
}


def convert(value, from_unit, to_unit):
    """Convert `value` from `from_unit` to `to_unit`."""
    for unit in (from_unit, to_unit):
        if unit not in UNITS:
            raise ValueError(f"Unknown unit: {unit!r}. Use one of {list(UNITS)}.")
    from_family, from_factor, from_offset = UNITS[from_unit]
    to_family, to_factor, to_offset = UNITS[to_unit]
    if from_family != to_family:
        raise ValueError(f"Cannot convert {from_family} ({from_unit}) to {to_family} ({to_unit}).")
    base = value * from_factor + from_offset
    return (base - to_offset) / to_factor


if __name__ == "__main__":
    print(round(convert(7.5, "bar", "psi"), 4))
    print(round(convert(100, "degC", "degF"), 4))
    print(round(convert(0, "K", "degC"), 4))
