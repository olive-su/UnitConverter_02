"""Golden Master harness. Set UPDATE_GOLDEN=1 to refresh baselines."""

import os


def golden_update_enabled() -> bool:
    return os.environ.get("UPDATE_GOLDEN", "").strip() == "1"
