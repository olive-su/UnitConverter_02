"""U-OUT-04: meter:2.5 — format=table table text output. Trace: EXT-03."""

from src.boundary.output_formatter import format_output
from src.entity.converter import convert_all


def test_u_out_04_meter_2_5_format_table():
    raw_input = "meter:2.5"
    output_format = "table"
    expected_header_tokens = ("unit", "value")
    expected_units = ("meter", "feet", "yard")

    unit, _, value_str = raw_input.partition(":")
    converted = convert_all(unit, float(value_str))
    output = format_output(converted, output_format=output_format)
    lower = output.lower()

    for token in expected_header_tokens:
        assert token in lower
    for unit_name in expected_units:
        assert unit_name in lower
