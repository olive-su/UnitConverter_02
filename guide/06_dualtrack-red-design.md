# 06. Dual-Track RED Design

Korean version: [06_dualtrack-red-design.ko.md](06_dualtrack-red-design.ko.md). Source: `goinfre/06`.

Design the first failing tests on two tracks before any implementation.

## Track A — UI / Boundary

| Test ID | Given | Then (expected RED) | Trace | Path |
|---------|-------|---------------------|-------|------|
| U-IN-01 | `""` (empty input) | format error message | FR-05 | `tests/boundary/test_u_in_01.py` |
| U-IN-02 | `meter` (no colon) | format error | FR-05 | `tests/boundary/test_u_in_02.py` |
| U-IN-03 | `meter:-1` | negative rejected | FR-04 | `tests/boundary/test_u_in_03.py` |
| U-OUT-01 | `meter:2.5` | 3+ output lines (skeleton) | FR-02 | `tests/boundary/test_u_out_01.py` |

## Track B — Domain / Logic

| Test ID | Function | Given / Then | Trace | Path |
|---------|----------|--------------|-------|------|
| D-CNV-01 | `to_meter` | 1 feet -> 0.3048 m (+/- eps) | FR-02 | `tests/entity/test_d_cnv_01.py` |
| D-CNV-02 | `convert_all` | 2.5 m -> 8.20210 ft (5 digits) | FR-02 | `tests/entity/test_d_cnv_02.py` |
| D-CNV-03 | `convert_all` | feet->yard matches via-meter path | FR-02 | `tests/entity/test_d_cnv_03.py` |
| D-REG-01 | `register` | cubit 0.4572 -> convertible | EXT-02, NFR-01 | `tests/entity/test_d_reg_01.py` |
| D-CFG-01 | `load json` | broken file -> ConfigError | EXT-01 | `tests/entity/test_d_cfg_01.py` |

## RED Rules

- No implementation code during RED.
- `pytest.fail("RED: ...")` is allowed.
- No `skip` / `xfail`.
- One RED bundle = one commit.

## How to Use

- Each row binds to a traceability ID ([02 Traceability Matrix](02_traceability-matrix.md)).
- Track B tests use no domain mocks; Track A tests may mock the domain.
- After a track's RED bundle fails, implement the minimal GREEN ([05 ARRR 7 Steps](05_arrr-7steps.md)).

## Next

- Return to the index: [00 Guide](00_Guide.md).
- Begin implementation per [WORK_PLAN.md](../WORK_PLAN.md) Phase 1 / Phase 2.
