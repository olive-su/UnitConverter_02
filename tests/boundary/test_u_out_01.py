"""U-OUT-01: meter:2.5 — 3+ output lines. Trace: FR-02."""

import pytest


def test_u_out_01_meter_2_5_three_plus_output_lines():
    raw_input = "meter:2.5"
    min_output_lines = 3

    pytest.fail(
        "RED: U-OUT-01 — format_output not implemented; "
        f'expected input "{raw_input}" -> at least {min_output_lines} output lines'
    )
