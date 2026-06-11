"""Length conversion to meters (meter SSOT hub). Trace: FR-02."""

METER_TO_FEET = 3.28084
METER_TO_YARD = 1.09361


def to_meter(unit: str, value: float) -> float:
    """Convert a value in the given unit to meters."""
    if unit == "meter":
        return value
    if unit == "feet":
        return value / METER_TO_FEET
    raise ValueError(f"unknown unit: {unit}")


def convert_all(source_unit: str, value: float) -> dict[str, float]:
    """Convert a value to all registered units via meter SSOT."""
    meters = to_meter(source_unit, value)
    return {
        "meter": meters,
        "feet": meters * METER_TO_FEET,
        "yard": meters * METER_TO_YARD,
    }
