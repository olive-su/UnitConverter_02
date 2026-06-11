# /red-skeleton

ARRR Ask — RED skeleton test file. `tests/` only.

## Trigger

User typed `/red-skeleton` with **no extra text**. Do not ask follow-up questions.

## Preconditions

- Latest `/red-test-plan` output or [guide/06_dualtrack-red-design.md](../../guide/06_dualtrack-red-design.md).
- Branch: `red`. **Do not modify `src/`.**

## Steps

1. Create the test file from the design table path.
2. Use AAA structure; cite trace ID in docstring or comment (`FR-02`, `D-CNV-01`).
3. Body: `pytest.fail("RED: <Test-ID> — ...")` or import that will fail until GREEN.
4. Run `python -m pytest <path> -v` — expect **FAIL**.
5. One RED bundle = one commit when user requests commit.

## Track rules

| Track | Path | Mocks |
|-------|------|-------|
| B | `tests/entity/` | Domain mocks **forbidden** |
| A | `tests/boundary/` | Domain mocks **allowed** |

## Prohibited

- Any change under `src/`
- `skip`, `xfail`, empty tests that pass
- GREEN implementation
