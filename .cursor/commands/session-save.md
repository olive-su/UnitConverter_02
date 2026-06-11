# /session-save

Persist the current session so the next one can resume.

## Steps
1. Copy `harness/sessions/_template.md` to `harness/sessions/YYYY-MM-DD-NN-<slug>.md`.
2. Create the Korean version `...-<slug>.ko.md`.
3. Fill in: goal, key decisions, changes, commit hashes, open items, next steps.
4. Add a newest-first row to `harness/sessions/INDEX.md` and `INDEX.ko.md`.
5. Commit with `docs: add session log <slug>`.
6. Do not push unless the user confirms.
