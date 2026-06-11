"""U-IN-03: negative value — rejected. Trace: FR-04."""

import pytest


def test_u_in_03_negative_rejected():
    raw_input = "meter:-1"
    expected_message = "rejected"

    pytest.fail(
        "RED: U-IN-03 — parse_input not implemented; "
        f'expected input "{raw_input}" -> {expected_message}'
    )
