# UnitConverter Guide Set

Korean version: [00_Guide.ko.md](00_Guide.ko.md).

Foundation guides for the UnitConverter project. They take the project from problem statement to a test-first, OCP/SRP-clean implementation. Read this index first, then follow the order below.

## Purpose

- Define what to build (PRD) and prove it is traceable to tests.
- Diagnose the legacy seed and set the target architecture.
- Drive implementation with ARRR / Dual-Track TDD.

## Guides at a Glance

| # | Guide | Role in flow | Source |
|---|-------|--------------|--------|
| 01 | [PRD Summary](01_prd-summary.md) | What we build (requirements, ratios, P1 extras) | goinfre/01 |
| 02 | [Traceability Matrix](02_traceability-matrix.md) | Map every requirement to a test ID | goinfre/02 |
| 03 | [Legacy Seed Analysis](03_legacy-seed-analysis.md) | Why the current code is a problem | goinfre/03 |
| 04 | [Target Architecture](04_target-architecture.md) | Module layout (OCP/SRP) | goinfre/04 |
| 05 | [ARRR 7 Steps](05_arrr-7steps.md) | Methodology (RED-GREEN-REFACTOR) | goinfre/05 |
| 06 | [Dual-Track RED Design](06_dualtrack-red-design.md) | First failing tests (Track A/B) | goinfre/06 |

## Flow

```mermaid
flowchart LR
  PRD[01 PRD summary] --> TRACE[02 Traceability]
  TRACE --> LEGACY[03 Legacy analysis]
  LEGACY --> ARCH[04 Architecture]
  ARCH --> ARRR[05 ARRR 7 steps]
  ARRR --> RED[06 Dual-Track RED]
  RED --> impl["Implement: RED -> GREEN -> REFACTOR"]
```

## Read Order

1. 01 PRD Summary — understand the product and acceptance.
2. 02 Traceability Matrix — anchor each requirement to a test ID.
3. 03 Legacy Seed Analysis — see the smells the design must remove.
4. 04 Target Architecture — learn the module split before coding.
5. 05 ARRR 7 Steps — adopt the workflow and branch strategy.
6. 06 Dual-Track RED Design — write the first failing tests.

## When to Revisit

- Before any new requirement: 02 to assign a test ID, 06 to design the RED bundle.
- Before any new module: 04 to keep boundaries (entity/boundary/control) clean.
- Before each commit: 05 for the RED-GREEN-REFACTOR cadence and commit rules.

## Related Documents

- [WORK_PLAN.md](../WORK_PLAN.md) — phased project roadmap.
- `docs/PRD.md` — formal PRD (produced in Phase 1).
- [AGENTS.md](../AGENTS.md) — agent behavior contract.

## Conventions

- Each guide is bilingual: `name.md` (English) + `name.ko.md` (Korean), kept in sync.
- Terse bullet style, no emojis, one goal per page.
