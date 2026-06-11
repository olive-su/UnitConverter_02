"""D-CNV-01: to_meter — 1 feet -> 0.3048 m (+/- eps). Trace: FR-02."""

from src.entity.converter import to_meter


def test_d_cnv_01_to_meter_one_feet():
    unit = "feet"
    value = 1.0
    expected_meters = 0.3048
    epsilon = 1e-4

    result = to_meter(unit, value)

    assert abs(result - expected_meters) < epsilon
