# /golden-master

ARRR Respond — Golden Master / approval baseline for stable output.

## Trigger

User typed `/golden-master` with **no extra text**. Do not ask follow-up questions.

## Preconditions

- Branch: `green`.
- Target test already **PASS** on minimal GREEN.
- Harness: `tests/_approval.py`, `tests/golden/`.

## Steps

1. Add or extend approval test using project golden harness.
2. Capture expected output to `tests/golden/` (or document refresh via `UPDATE_GOLDEN=1`).
3. Run full affected suite — all **PASS**.
4. Note golden file paths in session summary.

## Prohibited

- Silently overwriting golden without stating `UPDATE_GOLDEN=1` workflow
- Changing contract to match wrong golden

## Next

`/refactor-smell` on branch `refactor`, or next RED bundle.
