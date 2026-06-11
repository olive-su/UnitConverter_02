"""Length conversion to meters (meter SSOT hub). Trace: FR-02."""

METER_TO_FEET = 3.28084


def to_meter(unit: str, value: float) -> float:
    """Convert a value in the given unit to meters."""
    if unit == "meter":
        return value
    if unit == "feet":
        return value / METER_TO_FEET
    raise ValueError(f"unknown unit: {unit}")
