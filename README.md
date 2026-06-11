# UnitConverter_02

Korean version: [README.ko.md](README.ko.md).

| Field | Value |
|-------|-------|
| Branch | `green` |
| Phase | **Green** — minimal implementation, all scoped tests passing |
| Remote | [olive-su/UnitConverter_02](https://github.com/olive-su/UnitConverter_02) |
| PR | [#6 green → main](https://github.com/olive-su/UnitConverter_02/pull/6) |
| Latest commit | `c189a95` — U-OUT-04 table output (Track A) |

---

## What this branch is

This is the **Green** branch: the smallest production code that satisfies Cycle 1–4 RED contracts. **15 tests pass** (entity 5, boundary 7, golden 3). Structure follows SRP/OCP from `guide/04_target-architecture.md`.

## Quick start

```bash
pip install -e ".[dev]"
python -m pytest -q
# Expected: 15 passed
```

## Implementation map

### Entity (`src/entity/`)

| Module | Trace | Role |
|--------|-------|------|
| `converter.py` | D-CNV-01–03 / FR-02 | `to_meter`, `convert_all` via meter SSOT |
| `unit_registry.py` | D-REG-01 / EXT-02 | dynamic unit registration |

### Infrastructure (`src/infrastructure/`)

| Module | Trace | Role |
|--------|-------|------|
| `config_loader.py` | D-CFG-01 / EXT-01 | load ratios from JSON; validate errors |

### Boundary (`src/boundary/`)

| Module | Trace | Role |
|--------|-------|------|
| `input_parser.py` | U-IN-01–03 / FR-04–05 | parse and validate `unit:value` |
| `output_formatter.py` | U-OUT-01–04 / FR-02, EXT-03 | `lines`, `json`, `csv`, `table` formats |

## Test summary

| Area | Count | Files |
|------|-------|-------|
| Entity | 5 | `test_d_cnv_*`, `test_d_reg_01`, `test_d_cfg_01` |
| Boundary | 7 | `test_u_in_*`, `test_u_out_*` (incl. U-OUT-03 csv) |
| Golden | 3 | `test_golden_cycle1_track_b.py` + JSON baselines |

Conversion ratios (meter hub):

- `1 meter = 3.28084 feet`
- `1 meter = 1.09361 yard`

## Cycle progress (RED + GREEN complete)

| Cycle | Track | Bundles |
|-------|-------|---------|
| 1 | B | D-CNV-01, D-CNV-02, D-CNV-03 + golden master |
| 2 | A | U-IN-01, U-IN-02, U-IN-03 |
| 3 | B | D-REG-01, D-CFG-01 |
| 4 | A | U-OUT-01, U-OUT-02, U-OUT-03, U-OUT-04 |

## Example usage (library)

```python
from src.entity.converter import convert_all
from src.boundary.output_formatter import format_output

result = convert_all("meter", 2.5)
print(format_output(result, output_format="json"))
```

## Branch map

```text
spec  → requirements
red   → 11 failing tests (no src)
green → you are here (15 passing, full Cycle 1–4)
refactor → Cycle 1 structure cleanup (partial; merge green first)
```

## Project layout

```text
src/
├── entity/converter.py, unit_registry.py
├── boundary/input_parser.py, output_formatter.py
└── infrastructure/config_loader.py
tests/
├── entity/, boundary/
└── golden/cycle1_track_b/
```

## Docs and workflow

- SSOT build order: `WORK_PLAN.md`
- Requirements: `docs/PRD.md`
- Agent harness: `AGENTS.md`
- Reports: `Report/` (phase exports)

## Next steps

- Open PR #6 merge to `main`
- Optional: `/refactor-smell` on `refactor` after merging `green`
- Optional: expand golden master coverage

## Legacy

`UnitConverter.py` remains as the original seed; new CLI should use `src/` modules.
