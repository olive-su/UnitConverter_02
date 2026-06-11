"""D-CFG-01: broken JSON file -> ConfigError. Trace: EXT-01."""

import pytest

from src.infrastructure.config_loader import ConfigError, load_units_json


def test_d_cfg_01_broken_json_raises_config_error(tmp_path):
    broken_file = tmp_path / "broken_units.json"
    broken_file.write_text("{ not valid json", encoding="utf-8")

    with pytest.raises(ConfigError):
        load_units_json(broken_file)
