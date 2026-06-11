"""Parse unit:value input strings. Trace: FR-01, FR-04, FR-05."""


class FormatError(Exception):
    """Raised when input format is invalid. Trace: FR-05."""


class NegativeValueError(Exception):
    """Raised when value is negative. Trace: FR-04."""


def parse_input(raw: str) -> tuple[str, float]:
    """Parse ``unit:value`` input; raise FormatError on invalid format."""
    if raw == "":
        raise FormatError("format error")
    if ":" not in raw:
        raise FormatError("format error")
    _unit, value_str = raw.split(":", 1)
    value = float(value_str)
    if value < 0:
        raise NegativeValueError("rejected")
