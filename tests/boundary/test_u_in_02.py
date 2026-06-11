"""U-IN-02: no colon — format error. Trace: FR-05."""

import pytest


def test_u_in_02_no_colon_format_error():
    raw_input = "meter"
    expected_message = "format error"

    pytest.fail(
        "RED: U-IN-02 — parse_input not implemented; "
        f'expected input "{raw_input}" -> {expected_message}'
    )
