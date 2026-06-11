"""U-IN-01: empty input — format error. Trace: FR-05."""

import pytest


def test_u_in_01_empty_input_format_error():
    raw_input = ""
    expected_message = "format error"

    pytest.fail(
        "RED: U-IN-01 — parse_input not implemented; "
        f'expected input "{raw_input}" -> {expected_message}'
    )
