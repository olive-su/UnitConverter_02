# UnitConverter_02

Korean version: [README.ko.md](README.ko.md).

| Field | Value |
|-------|-------|
| Branch | `red` |
| Phase | **Red** — failing tests only, no production implementation |
| Remote | [olive-su/UnitConverter_02](https://github.com/olive-su/UnitConverter_02) |
| PR | [#4 red → main](https://github.com/olive-su/UnitConverter_02/pull/4) |
| Latest commit | `e9db033` — U-OUT-04 failing skeleton (Track A) |

---

## What this branch is

This is the **Red** branch in ARRR / Dual-Track TDD. It contains **11 intentional failing tests** that define the contract for Cycle 1–4 bundles. `src/` has only empty package stubs — **no converter, parser, or formatter code**. GREEN work happens on `green`.

## Expected test result

```bash
pip install -e ".[dev]"
python -m pytest -q
# Expected: 11 failed (all RED — this is correct)
```

## Test inventory (all RED)

### Track B — Entity / domain

| Test file | Trace ID | Requirement |
|-----------|----------|-------------|
| `tests/entity/test_d_cnv_01.py` | D-CNV-01 / FR-02 | `to_meter` — one feet → meter |
| `tests/entity/test_d_cnv_02.py` | D-CNV-02 / FR-02 | `convert_all` — meter → all units |
| `tests/entity/test_d_cnv_03.py` | D-CNV-03 / FR-02 | feet → yard via meter SSOT |
| `tests/entity/test_d_reg_01.py` | D-REG-01 / EXT-02 | dynamic unit registration (cubit) |
| `tests/entity/test_d_cfg_01.py` | D-CFG-01 / EXT-01 | broken JSON config raises error |

### Track A — Boundary / CLI

| Test file | Trace ID | Requirement |
|-----------|----------|-------------|
| `tests/boundary/test_u_in_01.py` | U-IN-01 / FR-05 | empty input → format error |
| `tests/boundary/test_u_in_02.py` | U-IN-02 / FR-05 | missing colon → format error |
| `tests/boundary/test_u_in_03.py` | U-IN-03 / FR-04 | negative value rejected |
| `tests/boundary/test_u_out_01.py` | U-OUT-01 / FR-02 | lines output for `meter:2.5` |
| `tests/boundary/test_u_out_02.py` | U-OUT-02 / EXT-03 | JSON output format |
| `tests/boundary/test_u_out_04.py` | U-OUT-04 / EXT-03 | table output format |

Note: U-OUT-03 (CSV) was added directly on `green` (GREEN-only bundle).

## What is **not** on `red`

- No `src/entity/converter.py`, `unit_registry.py`, `constants.py`
- No `src/boundary/input_parser.py`, `output_formatter.py`
- No `src/infrastructure/config_loader.py`
- No golden master baselines under `tests/golden/`

## Branch map

```text
spec  → requirements and harness
red   → you are here (11 failing tests, stubs only)
green → minimal implementation (15 passing tests)
refactor → Cycle 1 structure cleanup
```

## Workflow for builders

1. Pick one RED bundle (one test file = one commit on `red`).
2. Checkout `green`, implement the **smallest** code to pass that test.
3. Commit on `green` with `green: minimal … for <ID>`.
4. Do not fix tests on `red` — tests are the specification.

References: `guide/06_dualtrack-red-design.md`, `WORK_PLAN.md` sections 5–8.

## Project docs

- Requirements: `docs/PRD.md`
- Trace matrix: `guide/02_traceability-matrix.md`
- Target modules: `guide/04_target-architecture.md`
- Agent entry: `AGENTS.md`

## Legacy reference

`UnitConverter.py` remains as the pre-refactor seed; new code must not copy its if/elif structure.

## Next step

Merge or rebase from `green` when reviewing the full passing stack, or continue RED→GREEN cycles per `WORK_PLAN.md`.
