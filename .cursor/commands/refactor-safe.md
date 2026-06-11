# /refactor-safe

ARRR Refine — one safe refactor; contract unchanged.

## Trigger

User typed `/refactor-safe` with **no extra text**. Do not ask follow-up questions.

## Preconditions

- Branch: `refactor`.
- `/refactor-smell` P0 target identified (or infer top P0 from codebase).
- Budget: **max 3 files, 1 class, 3 methods** per session unless user expands.

## Steps

1. Apply **one** refactor (extract function, move constant to `constants.py`, etc.).
2. Run `python -m pytest tests/ -v` — all **PASS**; golden **matched** if applicable.
3. Summarize diff and smell resolved.

## Prohibited

- Behavior or public API change
- Refactor without green tests
- Large multi-smell rewrite in one step

## Next

`/refactor-smell` again or next RED bundle; `/export` at session end.
