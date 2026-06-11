# UnitConverter_02

Korean version: [README.ko.md](README.ko.md).

| Field | Value |
|-------|-------|
| Branch | `refactor` |
| Phase | **Refactor** — structure cleanup, same test contract |
| Remote | [olive-su/UnitConverter_02](https://github.com/olive-su/UnitConverter_02) |
| Latest commit | `6219a81` — extract unit ratio map (contract unchanged) |
| Scope | **Cycle 1 Track B only** (D-CNV + golden) |

---

## What this branch is

This is the **Refactor** branch: improve internal structure **without changing observable behavior**. The first refactor commit extracts hard-coded ratios into `src/entity/constants.py` and drives `converter.py` from map lookups instead of inline `if` branches.

**6 tests pass** — Cycle 1 entity tests (3) plus golden master (3). Track A (parser/formatter) and Cycle 3–4 (registry, config, output formats) exist only on `green`; merge `green` before extending refactor here.

## Quick start

```bash
pip install -e ".[dev]"
python -m pytest -q
# Expected: 6 passed
```

## Refactor delta (vs Cycle 1 green)

| Before | After |
|--------|-------|
| Ratios and branches inside `converter.py` | `constants.py`: `UNIT_TO_METER`, `METER_TO_UNIT` |
| `if unit == "meter"` / `if unit == "feet"` | `dict.get` + dict comprehension in `convert_all` |

Public functions unchanged:

- `to_meter(unit, value) -> float`
- `convert_all(source_unit, value) -> dict[str, float]`

## Source layout (this branch)

```text
src/entity/
├── constants.py   # ratio maps (new)
└── converter.py     # map-driven conversion
tests/entity/
├── test_d_cnv_01.py
├── test_d_cnv_02.py
└── test_d_cnv_03.py
tests/golden/cycle1_track_b/   # JSON baselines
```

No `src/boundary/`, `src/infrastructure/`, or `unit_registry.py` on this branch yet.

## Test inventory

| Test | Trace | Golden baseline |
|------|-------|-----------------|
| `test_d_cnv_01` | D-CNV-01 | `d_cnv_01_to_meter_one_feet.json` |
| `test_d_cnv_02` | D-CNV-02 | `d_cnv_02_convert_all_meter_to_feet.json` |
| `test_d_cnv_03` | D-CNV-03 | `d_cnv_03_convert_all_feet_to_yard.json` |

## Branch map

```text
green     → full Cycle 1–4 (15 tests) — merge source of truth
refactor  → you are here (Cycle 1 refactor only, 6 tests)
```

Recommended flow:

1. Merge `green` → `main` (or into `refactor`).
2. Rebase `refactor` onto latest `green`.
3. Re-apply or extend refactors (`/refactor-smell`) while keeping all 15 tests green.

## Refactor rules

- No test changes unless the contract was wrong (fix on `red` first).
- One refactor theme per commit; run full scoped pytest before commit.
- Prefer extract-class/module over behavior change.

References: `guide/05_arrr-7steps.md`, `WORK_PLAN.md` section 5.

## Docs

- Architecture target: `guide/04_target-architecture.md`
- Legacy smells addressed: `guide/03_legacy-seed-analysis.md`
- Agent harness: `AGENTS.md`

## Next steps

- Merge `green` into `refactor` to align with full implementation.
- Continue refactor-smell passes (parser/formatter/registry) with tests green.
- Open PR to `main` after full test suite passes on this branch.
