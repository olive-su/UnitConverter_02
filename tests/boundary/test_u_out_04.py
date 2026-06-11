"""U-OUT-04: meter:2.5 — format=table table text output. Trace: EXT-03."""

import pytest


def test_u_out_04_meter_2_5_format_table():
    # Arrange: meter:2.5 conversion with table output format (EXT-03)
    raw_input = "meter:2.5"
    output_format = "table"
    expected_header_tokens = ("unit", "value")

    # Act / Assert: RED skeleton — format_output(table) deferred to GREEN
    pytest.fail(
        "RED: U-OUT-04 — format_output(table) not implemented; "
        f'expected input "{raw_input}" with format={output_format!r} '
        f"-> table text with header containing {expected_header_tokens}"
    )
