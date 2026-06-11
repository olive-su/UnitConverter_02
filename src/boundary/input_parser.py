"""Parse unit:value input strings. Trace: FR-01, FR-04, FR-05."""


class FormatError(Exception):
    """Raised when input format is invalid. Trace: FR-05."""


def parse_input(raw: str) -> tuple[str, float]:
    """Parse ``unit:value`` input; raise FormatError on invalid format."""
    if raw == "":
        raise FormatError("format error")
