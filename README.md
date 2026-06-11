# UnitConverter_02

Korean version: [README.ko.md](README.ko.md).

| Field | Value |
|-------|-------|
| Branch | `spec` |
| Phase | **Spec** — requirements and scaffolding before RED |
| Remote | [olive-su/UnitConverter_02](https://github.com/olive-su/UnitConverter_02) |
| PR | [#2 spec → main](https://github.com/olive-su/UnitConverter_02/pull/2) |
| Latest commit | `cb868da` — Mom Test, PRD, ARRR harness, project scaffolding |

---

## What this branch is

This is the **Spec** branch in the ARRR (Analyze → Red → Green → Refactor) workflow. It holds product requirements, architecture guides, Cursor harness, and empty `src/` / `tests/` scaffolding. **No failing or passing feature tests yet** — implementation starts on `red` and `green`.

## Product goal

Re-implement the legacy length converter (`UnitConverter.py`) as a traceable, test-first CLI:

- Input: `unit:value` (e.g. `meter:2.5`)
- Output: the value in all registered units (meter, feet, yard)
- Base ratios: `1 m = 3.28084 ft = 1.09361 yd` (meter as SSOT)
- Quality: OCP, SRP, input validation, optional config / dynamic units / output formats (P1)

## What is done on `spec`

| Area | Status |
|------|--------|
| Mom Test evidence | `Report/01`–`05` |
| PRD | `docs/PRD.md` (+ `.ko.md`) |
| Master prompt | `docs/MASTER_PROMPT.md` (+ `.ko.md`) |
| Phase 0 guides | `guide/00`–`06` (traceability, architecture, ARRR, Dual-Track RED) |
| Work plan (SSOT) | `WORK_PLAN.md` (+ `.ko.md`) |
| Cursor harness | `AGENTS.md`, `.cursor/rules`, `.cursor/commands`, `harness/` |
| Project layout | `pyproject.toml`, empty `src/entity`, `src/boundary`, `tests/` tree |
| Legacy seed | `UnitConverter.py` (reference only) |

## Branch map (ARRR)

```text
main          ← merge target
  ↑
spec          ← you are here (requirements + harness)
  ↓
red           ← failing tests only (no src implementation)
  ↓
green         ← minimal code to pass tests (Cycle 1–4 complete)
  ↓
refactor      ← structure cleanup, same public contract
```

See `guide/05_arrr-7steps.md` and `guide/06_dualtrack-red-design.md` for cycle and trace IDs.

## Quick start

### Prerequisites

- Python 3.11+
- Optional: `pip install -e ".[dev]"` for pytest (no tests collected on `spec` yet)

### Read order for agents and contributors

1. [AGENTS.md](AGENTS.md) — harness entry point
2. [WORK_PLAN.md](WORK_PLAN.md) — build order and traceability
3. [docs/PRD.md](docs/PRD.md) — product requirements
4. [guide/00_Guide.md](guide/00_Guide.md) — guide index

### Verify this branch

```bash
python -m pytest --collect-only -q
# Expected: no tests collected (scaffolding only)
```

### Legacy CLI (reference)

```bash
python UnitConverter.py
# Enter e.g. meter:2.5 — pre-refactor monolith, not the target architecture
```

## Project layout

```text
UnitConverter_02/
├── docs/              PRD, MASTER_PROMPT
├── guide/             Phase 0 architecture and ARRR docs
├── harness/           Session logs, agent roles, patterns
├── Report/, Prompting/ Mom Test and phase exports
├── src/               Empty package stubs (entity, boundary)
├── tests/             conftest only — no feature tests yet
├── .cursor/           Rules, commands, skills
├── UnitConverter.py   Legacy seed
└── pyproject.toml
```

## Traceability (preview)

| ID | Requirement | Track |
|----|-------------|-------|
| FR-01–05 | Parse, output, errors | A/B |
| NFR-01–02 | OCP, SRP module split | B |
| EXT-01–03 | Config, dynamic units, output formats | B / A |

Full matrix: `guide/02_traceability-matrix.md`.

## Next steps (after merge or checkout)

1. **`red`** — add failing test skeletons per Dual-Track bundles (`D-CNV-*`, `U-IN-*`, …).
2. **`green`** — minimal implementation until pytest passes.
3. **`refactor`** — improve structure without changing test contracts.

## License and contributors

Course / team project. Reviewers and phase checklist: `WORK_PLAN.md` section 9.
