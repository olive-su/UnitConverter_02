"""U-OUT-01: meter:2.5 — 3+ output lines. Trace: FR-02."""

from src.boundary.output_formatter import format_output
from src.entity.converter import convert_all


def test_u_out_01_meter_2_5_three_plus_output_lines():
    raw_input = "meter:2.5"
    min_output_lines = 3

    unit, _, value_str = raw_input.partition(":")
    converted = convert_all(unit, float(value_str))
    output = format_output(converted)
    lines = [line for line in output.splitlines() if line.strip()]

    assert len(lines) >= min_output_lines
