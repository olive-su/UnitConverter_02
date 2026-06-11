# /red-test-plan

ARRR Ask — RED design table only. No files under `tests/` or `src/`.

## Trigger

User typed `/red-test-plan` with **no extra text**. Do not ask follow-up questions.

## Preconditions

- Read [WORK_PLAN.md](../../WORK_PLAN.md), [guide/06_dualtrack-red-design.md](../../guide/06_dualtrack-red-design.md), [docs/PRD.md](../../docs/PRD.md).
- Branch should be `red` for implementation; on `spec`, design-only is allowed.

## Steps

1. Infer the **next RED bundle** from WORK_PLAN cycle order (Track B first unless user context names one).
2. Output a **4-block design table** in chat (do not create files):

| Block | Content |
|-------|---------|
| Meta | Phase `red`, Layer (`entity` or `boundary`), Track (Logic or UI), Test ID (`D-*` or `U-*`), FR/NFR trace |
| Given / Then | Concrete input and expected failure message or assertion target |
| Path | Target file e.g. `tests/entity/test_d_cnv_01.py` |
| Rules | No `src/` edit; `pytest.fail` or assert on missing impl allowed |

3. State **invariants**: ECB (entity no boundary import), Track B no domain mocks.
4. End with: next step is `/red-skeleton` on branch `red`.

## Prohibited

- Creating or editing `tests/` or `src/`
- `skip`, `xfail`, weakening asserts
- Asking the user which test to pick if WORK_PLAN order is clear
