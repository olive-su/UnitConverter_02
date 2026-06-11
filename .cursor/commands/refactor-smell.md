# /refactor-smell

ARRR Refine Ask — smell table only. No code edits.

## Trigger

User typed `/refactor-smell` with **no extra text**. Do not ask follow-up questions.

## Preconditions

- Branch: `refactor` (or about to switch).
- Tests are green for current scope.

## Steps

1. Scan `src/` for smells (duplication, long methods, magic numbers, SRP violations).
2. Output a table P0–P2:

| Priority | Smell | Location | Safe refactor candidate |
|----------|-------|----------|-------------------------|

3. Map smells to [guide/03_legacy-seed-analysis.md](../../guide/03_legacy-seed-analysis.md) where relevant.
4. Pick **one** P0 candidate for `/refactor-safe`.
5. **Do not edit files.**

## Prohibited

- Code changes in this step
- Contract-breaking API changes
