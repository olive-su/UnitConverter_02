"""Golden Master — Cycle 1 Track B (D-CNV-01~03). Trace: FR-02."""

from src.entity.converter import convert_all, to_meter
from tests._approval import assert_golden_matches

GOLDEN_SUBDIR = "cycle1_track_b"


def test_golden_d_cnv_01_to_meter_one_feet():
    actual = {
        "test_id": "D-CNV-01",
        "input": {"unit": "feet", "value": 1.0},
        "output": {"meters": to_meter("feet", 1.0)},
    }
    assert_golden_matches(GOLDEN_SUBDIR, "d_cnv_01_to_meter_one_feet.json", actual)


def test_golden_d_cnv_02_convert_all_meter_to_feet():
    actual = {
        "test_id": "D-CNV-02",
        "input": {"source_unit": "meter", "value": 2.5},
        "output": convert_all("meter", 2.5),
    }
    assert_golden_matches(GOLDEN_SUBDIR, "d_cnv_02_convert_all_meter_to_feet.json", actual)


def test_golden_d_cnv_03_convert_all_feet_to_yard_via_meter():
    actual = {
        "test_id": "D-CNV-03",
        "input": {"source_unit": "feet", "value": 3.28084},
        "output": convert_all("feet", 3.28084),
    }
    assert_golden_matches(GOLDEN_SUBDIR, "d_cnv_03_convert_all_feet_to_yard.json", actual)
