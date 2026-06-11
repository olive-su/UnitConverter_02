"""Dynamic unit registration (OCP). Trace: EXT-02, NFR-01."""

_REGISTRY: dict[str, float] = {}


def register(name: str, meters_per_unit: float) -> None:
    """Register a unit by meters per one unit (e.g. 1 cubit = 0.4572 m)."""
    _REGISTRY[name] = meters_per_unit


def lookup(name: str) -> float | None:
    """Return meters-per-unit ratio for a registered name, or None."""
    return _REGISTRY.get(name)
