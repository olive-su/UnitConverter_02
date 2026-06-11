"""D-REG-01: register cubit 0.4572 m then convertible. Trace: EXT-02, NFR-01."""

import pytest


def test_d_reg_01_register_cubit_then_convertible():
    # Arrange: dynamic registration — 1 cubit = 0.4572 meter (EXT-02, NFR-01 OCP)
    unit_name = "cubit"
    meters_per_unit = 0.4572
    value = 1.0
    expected_meters = 0.4572
    epsilon = 1e-4

    # Act / Assert: RED skeleton — register + to_meter deferred to GREEN
    pytest.fail(
        "RED: D-REG-01 — register not implemented; "
        f"expected register({unit_name!r}, {meters_per_unit}) then "
        f"to_meter({unit_name!r}, {value}) -> {expected_meters} m (+/- {epsilon})"
    )
