"""D-CNV-02: convert_all — 2.5 m -> 8.20210 ft (5 digits). Trace: FR-02."""

import pytest


def test_d_cnv_02_convert_all_meter_to_feet():
    source_unit = "meter"
    value = 2.5
    expected_feet = 8.20210
    epsilon = 1e-5

    pytest.fail(
        "RED: D-CNV-02 — convert_all not implemented; "
        f"expected {value} {source_unit} -> {expected_feet} ft (+/- {epsilon})"
    )
