"""Format conversion results as multi-line output. Trace: FR-02, EXT-03."""

import json


def format_output(converted: dict[str, float], *, output_format: str = "lines") -> str:
    """Return formatted conversion output (lines, json, csv, or table)."""
    order = ("meter", "feet", "yard")
    if output_format == "json":
        return json.dumps(converted)
    if output_format == "csv":
        lines = ["unit,value"]
        for unit in order:
            if unit in converted:
                lines.append(f"{unit},{converted[unit]}")
        return "\n".join(lines)
    if output_format == "table":
        lines = ["unit | value", "----- | -----"]
        for unit in order:
            if unit in converted:
                lines.append(f"{unit} | {converted[unit]}")
        return "\n".join(lines)
    lines = [f"{unit}: {converted[unit]}" for unit in order if unit in converted]
    return "\n".join(lines)
