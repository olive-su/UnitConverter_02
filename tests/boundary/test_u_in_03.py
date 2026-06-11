"""U-IN-03: negative value — rejected. Trace: FR-04."""

import pytest

from src.boundary.input_parser import NegativeValueError, parse_input


def test_u_in_03_negative_rejected():
    raw_input = "meter:-1"
    expected_message = "rejected"

    with pytest.raises(NegativeValueError) as exc_info:
        parse_input(raw_input)

    assert expected_message in str(exc_info.value)
