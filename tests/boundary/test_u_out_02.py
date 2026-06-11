"""U-OUT-02: meter:2.5 — format=json JSON output. Trace: EXT-03."""

import json

from src.boundary.output_formatter import format_output
from src.entity.converter import convert_all


def test_u_out_02_meter_2_5_format_json():
    raw_input = "meter:2.5"
    output_format = "json"
    expected_keys = ("meter", "feet", "yard")

    unit, _, value_str = raw_input.partition(":")
    converted = convert_all(unit, float(value_str))
    output = format_output(converted, output_format=output_format)
    parsed = json.loads(output)

    for key in expected_keys:
        assert key in parsed
