"""D-REG-01: register cubit 0.4572 m then convertible. Trace: EXT-02, NFR-01."""

from src.entity.converter import to_meter
from src.entity.unit_registry import register


def test_d_reg_01_register_cubit_then_convertible():
    unit_name = "cubit"
    meters_per_unit = 0.4572
    value = 1.0
    expected_meters = 0.4572
    epsilon = 1e-4

    register(unit_name, meters_per_unit)

    result = to_meter(unit_name, value)

    assert abs(result - expected_meters) < epsilon
