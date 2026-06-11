"""D-CNV-03: convert_all — feet->yard via meter SSOT. Trace: FR-02."""

from src.entity.converter import convert_all

METER_TO_FEET = 3.28084
METER_TO_YARD = 1.09361


def test_d_cnv_03_convert_all_feet_to_yard_via_meter():
    source_unit = "feet"
    value = 3.28084
    meters_via_feet = value / METER_TO_FEET
    expected_yard = meters_via_feet * METER_TO_YARD
    epsilon = 1e-5

    result = convert_all(source_unit, value)

    assert abs(result["yard"] - expected_yard) < epsilon
