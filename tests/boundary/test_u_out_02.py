"""U-OUT-02: meter:2.5 — format=json JSON output. Trace: EXT-03."""

import pytest


def test_u_out_02_meter_2_5_format_json():
    # Arrange: meter:2.5 conversion with JSON output format (EXT-03)
    raw_input = "meter:2.5"
    output_format = "json"
    expected_keys = ("meter", "feet", "yard")

    # Act / Assert: RED skeleton — format_output(json) deferred to GREEN
    pytest.fail(
        "RED: U-OUT-02 — format_output(json) not implemented; "
        f'expected input "{raw_input}" with format={output_format!r} '
        f"-> parseable JSON with keys {expected_keys}"
    )
