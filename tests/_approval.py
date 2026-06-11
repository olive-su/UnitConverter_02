"""Golden Master harness. Set UPDATE_GOLDEN=1 to refresh baselines."""

import json
import os
from pathlib import Path
from typing import Any

GOLDEN_ROOT = Path(__file__).resolve().parent / "golden"


def golden_update_enabled() -> bool:
    return os.environ.get("UPDATE_GOLDEN", "").strip() == "1"


def golden_file_path(subdir: str, filename: str) -> Path:
    return GOLDEN_ROOT / subdir / filename


def _serialize(data: Any) -> str:
    return json.dumps(data, indent=2, sort_keys=True) + "\n"


def assert_golden_matches(subdir: str, filename: str, actual: Any) -> None:
    """Compare actual data to a golden JSON file; refresh when UPDATE_GOLDEN=1."""
    path = golden_file_path(subdir, filename)
    serialized = _serialize(actual)

    if golden_update_enabled():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(serialized, encoding="utf-8")
        return

    if not path.is_file():
        raise AssertionError(
            f"Missing golden file: {path}. "
            "Run with UPDATE_GOLDEN=1 to create the baseline."
        )

    expected = path.read_text(encoding="utf-8")
    assert serialized == expected, (
        f"Golden mismatch for {path.name}. "
        "Set UPDATE_GOLDEN=1 to refresh if the change is intentional."
    )
