"""Length unit ratios relative to meter (SSOT hub). Trace: FR-02."""

METER_TO_FEET = 3.28084
METER_TO_YARD = 1.09361

UNIT_TO_METER: dict[str, float] = {
    "meter": 1.0,
    "feet": 1.0 / METER_TO_FEET,
}

METER_TO_UNIT: dict[str, float] = {
    "meter": 1.0,
    "feet": METER_TO_FEET,
    "yard": METER_TO_YARD,
}
