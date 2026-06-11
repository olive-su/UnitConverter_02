# unit-converter-tdd

Use when executing ARRR / Dual-Track TDD on UnitConverter_02.

## SSOT

- [WORK_PLAN.md](../../../WORK_PLAN.md)
- [guide/05_arrr-7steps.md](../../../guide/05_arrr-7steps.md)
- [guide/06_dualtrack-red-design.md](../../../guide/06_dualtrack-red-design.md)
- [docs/PRD.md](../../../docs/PRD.md)

## ARRR = Dual-Track TDD

| ARRR | Branch | Scope |
|------|--------|-------|
| Ask RED | `red` | `tests/` only |
| Respond GREEN | `green` | `src/` + tests |
| Refine REFACTOR | `refactor` | structure, contract fixed |
| Repeat | any | `/export`, next RED |

## Dual-Track

| Track | Layer | Path | Domain mocks |
|-------|-------|------|--------------|
| B Logic | entity | `tests/entity/`, `src/entity/` | Forbidden |
| A UI/boundary | boundary | `tests/boundary/`, `src/boundary/` | Allowed |

## RED rules

- One RED bundle = one commit
- `pytest.fail("RED: ...")` OK
- No `skip` / `xfail`
- No `src/` on `red`

## Commands

`/red-test-plan` → `/red-skeleton` → `/green-minimal` → `/golden-master` → `/refactor-smell` → `/refactor-safe` → `/export`

## First P0 bundle

D-CNV-01 (`to_meter`, 1 feet → 0.3048 m) — Track B.

## Ratios SSOT

- `1 meter = 3.28084 feet`
- `1 meter = 1.09361 yard`
- feet ↔ yard via meter
