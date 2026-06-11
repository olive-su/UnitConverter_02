"""Length conversion to meters (meter SSOT hub). Trace: FR-02."""

from src.entity.constants import METER_TO_UNIT, UNIT_TO_METER


def to_meter(unit: str, value: float) -> float:
    """Convert a value in the given unit to meters."""
    factor = UNIT_TO_METER.get(unit)
    if factor is None:
        raise ValueError(f"unknown unit: {unit}")
    return value * factor


def convert_all(source_unit: str, value: float) -> dict[str, float]:
    """Convert a value to all registered units via meter SSOT."""
    meters = to_meter(source_unit, value)
    return {unit: meters * factor for unit, factor in METER_TO_UNIT.items()}
