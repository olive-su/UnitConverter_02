"""Format conversion results as multi-line output. Trace: FR-02."""


def format_output(converted: dict[str, float]) -> str:
    """Return one line per unit in meter, feet, yard order."""
    order = ("meter", "feet", "yard")
    lines = [f"{unit}: {converted[unit]}" for unit in order if unit in converted]
    return "\n".join(lines)
