# UnitConverter_02 — Master Session Prompt

Korean version: [MASTER_PROMPT.ko.md](MASTER_PROMPT.ko.md).

Paste this at the start of a work session (or reference by path). Issue and PR text stay English; working dialogue may use Korean.

## North Star — C2C Traceability

Every requirement (FR/NFR/EXT in [guide/02_traceability-matrix.md](../guide/02_traceability-matrix.md)) must trace to a test ID and a file path.

Dual-Track TDD executed as ARRR is the only approved way to preserve that trace:

- Ask = RED (tests only)
- Respond = GREEN (minimal pass)
- Refine = REFACTOR (structure, contract unchanged)
- Repeat = next RED bundle

ARRR and "C2C x Dual-Track TDD" are the same cycle, not separate methodologies.

## Read Order (before any edit)

1. [WORK_PLAN.md](../WORK_PLAN.md) — current phase gate
2. [AGENTS.md](../AGENTS.md) + `.cursor/rules/*`
3. `harness/sessions/INDEX.md` + latest session log
4. [guide/00_Guide.md](../guide/00_Guide.md) and the guide for this phase
5. `docs/PRD.md` (after Spec phase)
6. Tone reference: `MagicSquare_1004` Report/Prompting for the same phase

## Repo and Branch Contract

- Remote: `olive-su/UnitConverter_02`
- Branch flow: `main` -> `spec` -> `red` -> `green` -> `refactor` -> (repeat) -> `new_features`
- **Current phase**: Phase 1 — Spec on branch `spec`

On phase transition: switch branch, English issue, commit when I ask, push only after I confirm, English PR with reviewers below.

| Phase | Branch | Edit scope |
|-------|--------|------------|
| Spec | `spec` | docs, `.cursor/`, `Report/`, `Prompting/`, harness |
| RED | `red` | `tests/` only |
| GREEN | `green` | `src/` + matching tests |
| REFACTOR | `refactor` | refactor only (contract unchanged) |

### PR reviewers

`yhkwon0817`, `jhgomi`, `curiosus`, `okpym`

## Rules SSOT

- Project rules: `.cursor/rules/*.mdc` and harness — **do not** add a duplicate root `.cursorrules`.
- Bilingual docs: `name.md` + `name.ko.md` for human-readable markdown.
- Commits: English Conventional Commits when I request.
- Never push without my explicit confirmation.

## Phase 1 — Spec Deliverables

Do **not** write `src/` implementation or run pytest unless WORK_PLAN explicitly scopes it.

### 1. Mom Test (agent self-simulation)

- **Role 1**: interviewer — Mom Test rules, one question at a time, no solution pitching.
- **Role 2**: persona — student in the 6-hour AI activities lab ([README.md](../README.md)) who also hits real conversion pain: spec sheets in ft vs m, spreadsheet re-entry, wrong ratio costing ~20 minutes.
- Run 3 interview turns in the transcript; then produce:
  - Surface problem (forbidden solution-mixed sentences)
  - Real problem (one sentence)
  - Mom Test evidence (3 quoted lines)
  - R-G-I-O workbook + 3 success criteria with verification method
- Artifacts: `Report/01.REPORT.md` through `Report/03.REPORT.md`, `Prompting/01.Export-Transcript.md` through `Prompting/03.Export-Transcript.md`

### 2. PRD

- `docs/PRD.md` + `docs/PRD.ko.md` from Mom Test + guide/01 + guide/02
- Include: scope, out-of-scope with Mom Test rationale, traceability table, acceptance examples

### 3. Cursor ARRR harness (Spec — files only, no test run)

Create slash commands (name only — no follow-up questions):

- `red-test-plan`, `red-skeleton`, `green-minimal`, `golden-master`, `refactor-smell`, `refactor-safe`, `export-session`, `export`

Create skills:

- `unit-converter-tdd` — ARRR, Dual-Track, RED rules
- `unit-converter-docs` — Report/Prompting + `report-template.md`, `transcript-template.md`, `phase-checklist.md`

Match MagicSquare_1004 command tone. SSOT: WORK_PLAN, guide/, AGENTS.md.

Artifacts: `Report/04.REPORT.md`, `Prompting/04.Export-Transcript.md` (Cursor 4-group guide).

### 4. Phase 2 scaffolding (same `spec` branch, before PR)

After Phase 1 artifacts: `pyproject.toml`, `src/` and `tests/` skeleton per guide/04 — no RED/GREEN bodies.

### 5. Spec PR gate (single combined PR)

After Phase 1 + Phase 2 on `spec`:

- Propose issue: `spec: PRD, Mom Test evidence, ARRR harness, and project scaffolding`
- PR to `main` with reviewers above
- Do not push or commit unless I explicitly ask

### 6. Session close

- `/export` for latest Report + Prompting
- Harness session log (en + ko) + INDEX update when applicable

## RED Rules (later phases — do not violate)

- No `src/` changes on `red`
- `pytest.fail("RED: ...")` allowed; no skip/xfail
- One RED bundle = one commit
- Track B: `tests/entity/`, no domain mocks
- Track A: `tests/boundary/`, domain mocks allowed

## First RED bundle (after scaffolding)

Track B priority: **D-CNV-01** (FR-02) — see [guide/06_dualtrack-red-design.md](../guide/06_dualtrack-red-design.md).

## Slash workflow per ARRR cycle

```text
/red-test-plan -> /red-skeleton -> /green-minimal -> /golden-master -> /refactor-smell -> /refactor-safe -> /export
```

## Decisions locked in this prompt

| Topic | Decision |
|-------|----------|
| Mom Test persona | Lab student (README Activities) + concrete ft/m conversion pain |
| Spec PR scope | Single PR after Phase 1 + Phase 2 scaffolding on `spec` |
| Rules location | `.cursor/rules/*.mdc` only; no root `.cursorrules` |
| REFACTOR branch | `refactor` |
