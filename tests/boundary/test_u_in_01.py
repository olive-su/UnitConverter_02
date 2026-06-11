"""U-IN-01: empty input — format error. Trace: FR-05."""

import pytest

from src.boundary.input_parser import FormatError, parse_input


def test_u_in_01_empty_input_format_error():
    raw_input = ""
    expected_message = "format error"

    with pytest.raises(FormatError) as exc_info:
        parse_input(raw_input)

    assert expected_message in str(exc_info.value)
