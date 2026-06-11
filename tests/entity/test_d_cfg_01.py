"""D-CFG-01: broken JSON file -> ConfigError. Trace: EXT-01."""

import pytest


def test_d_cfg_01_broken_json_raises_config_error(tmp_path):
    # Arrange: invalid JSON content (EXT-01 config load guard)
    broken_file = tmp_path / "broken_units.json"
    broken_file.write_text("{ not valid json", encoding="utf-8")
    expected_error = "ConfigError"

    # Act / Assert: RED skeleton — load_units_json deferred to GREEN
    pytest.fail(
        "RED: D-CFG-01 — load_units_json not implemented; "
        f"expected load({broken_file!s}) -> {expected_error}"
    )
