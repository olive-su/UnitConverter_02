"""U-IN-02: no colon — format error. Trace: FR-05."""

import pytest

from src.boundary.input_parser import FormatError, parse_input


def test_u_in_02_no_colon_format_error():
    raw_input = "meter"
    expected_message = "format error"

    with pytest.raises(FormatError) as exc_info:
        parse_input(raw_input)

    assert expected_message in str(exc_info.value)
