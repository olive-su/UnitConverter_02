"""D-CNV-03: convert_all — feet->yard via meter SSOT. Trace: FR-02."""

import pytest

METER_TO_FEET = 3.28084
METER_TO_YARD = 1.09361


def test_d_cnv_03_convert_all_feet_to_yard_via_meter():
    # Arrange: 3.28084 ft == 1 m; yard must come from meter path, not direct ft-yd ratio
    source_unit = "feet"
    value = 3.28084
    meters_via_feet = value / METER_TO_FEET
    expected_yard = meters_via_feet * METER_TO_YARD
    epsilon = 1e-5

    # Act / Assert: RED skeleton — yard in convert_all deferred to GREEN
    pytest.fail(
        "RED: D-CNV-03 — convert_all yard missing or feet->yard not via meter SSOT; "
        f"expected {value} {source_unit} -> yard {expected_yard} (+/- {epsilon})"
    )
