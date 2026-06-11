"""Load unit ratios from JSON config. Trace: EXT-01."""

import json
from pathlib import Path


class ConfigError(Exception):
    """Raised when config file cannot be loaded or parsed. Trace: EXT-01."""


def load_units_json(path: Path) -> dict:
    """Load unit ratios from a JSON file; raise ConfigError on failure."""
    try:
        text = path.read_text(encoding="utf-8")
        return json.loads(text)
    except (OSError, json.JSONDecodeError) as exc:
        raise ConfigError("invalid config") from exc
