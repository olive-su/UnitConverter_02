"""U-OUT-03: meter:2.5 — format=csv CSV output. Trace: EXT-03."""

from src.boundary.output_formatter import format_output
from src.entity.converter import convert_all


def test_u_out_03_meter_2_5_format_csv():
    raw_input = "meter:2.5"
    output_format = "csv"

    unit, _, value_str = raw_input.partition(":")
    converted = convert_all(unit, float(value_str))
    output = format_output(converted, output_format=output_format)
    lines = [line for line in output.strip().splitlines() if line.strip()]

    assert len(lines) >= 2
    assert lines[0] == "unit,value"
    assert all("," in line for line in lines[1:])
