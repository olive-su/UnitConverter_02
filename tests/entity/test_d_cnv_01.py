"""D-CNV-01: to_meter — 1 feet -> 0.3048 m (+/- eps). Trace: FR-02."""

import pytest


def test_d_cnv_01_to_meter_one_feet():
    # Arrange: 1 feet input (domain unit + value)
    unit = "feet"
    value = 1.0
    expected_meters = 0.3048
    epsilon = 1e-4

    # Act / Assert: RED skeleton — implementation deferred to GREEN
    pytest.fail(
        "RED: D-CNV-01 — to_meter not implemented; "
        f"expected {value} {unit} -> {expected_meters} m (+/- {epsilon})"
    )
