"""Format conversion results as multi-line output. Trace: FR-02, EXT-03."""

import json


def format_output(converted: dict[str, float], *, output_format: str = "lines") -> str:
    """Return formatted conversion output (lines or json)."""
    if output_format == "json":
        return json.dumps(converted)
    order = ("meter", "feet", "yard")
    lines = [f"{unit}: {converted[unit]}" for unit in order if unit in converted]
    return "\n".join(lines)
