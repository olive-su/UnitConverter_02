# /export-session

ARRR Repeat — export Report and Prompting for this session.

## Trigger

User typed `/export-session` with **no extra text**. Do not ask follow-up questions.

## Steps

1. List `Report/` and `Prompting/`; find max `NN` in `NN.REPORT.md` and `NN.Export-Transcript.md`.
2. Next number = max + 1 (2-digit: `01`, `02`, …).
3. Create `Report/NN.REPORT.md` — summary table, decisions, changed files, pytest result if any, next steps, related links. Follow [unit-converter-docs skill](../skills/unit-converter-docs/report-template.md).
4. Create `Prompting/NN.Export-Transcript.md` — User/Cursor dialogue from **this chat**. Follow transcript template.
5. Do not overwrite existing numbered files.

## Auto-extract from chat (no user prompts)

- Session topic and phase
- Files created or modified
- Key commands used (`/red-test-plan`, etc.)

## Prohibited

- Asking user for report number or title
- Skipping Prompting transcript

## Alias

Same behavior as `/export` ([export.md](export.md)).
