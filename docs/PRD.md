# UnitConverter_02 — PRD (Product Requirements Document)

Korean version: [PRD.ko.md](PRD.ko.md).

| Field | Value |
|-------|-------|
| Project | UnitConverter_02 |
| Version | 0.1 (Spec) |
| Date | 2026-06-11 |
| Evidence | Mom Test — [Report/01.REPORT.md](../Report/01.REPORT.md), [Report/02.REPORT.md](../Report/02.REPORT.md), [Report/03.REPORT.md](../Report/03.REPORT.md) |
| Phase | Spec — requirements before RED implementation |

---

## 1. Overview

### 1.1 Background

Students and junior developers must convert a single length value across **meter, feet, and yard** for lab reports and assignments. Manual or rounded ratios (e.g. `3.28` instead of `3.28084`) produce **inconsistent multi-unit output** and **10–20 minutes** of rework.

**Mom Test evidence (simulation — [Report/02.REPORT.md](../Report/02.REPORT.md)):**

- Used **3.28** → **8.2** feet; required **8.2021**
- Computed **feet and yard separately** with different approximations
- **4–5** spreadsheet iterations, **~12 minutes**; legacy `UnitConverter.py` not trusted

### 1.2 Real problem

> When one `unit:value` must yield **all units consistently** via a **meter-based SSOT**, **manual per-unit math and wrong ratios** break consistency and cost **10–20 minutes** of correction; unvalidated legacy code is not trusted.

### 1.3 Release goal (P0)

Provide a **traceable CLI** and **test loop** that:

- Parses `unit:value`
- Outputs **all registered units** with correct ratios
- Rejects negative, malformed, and unknown-unit input **explicitly**

**Intentional deferral:** P1 config file, dynamic registration, output formats — surface extensions after P0 traceability (Mom Test: fix consistency and trust first).

### 1.4 Topic (one sentence)

> **From one `unit:value` input, convert to all length units via meter SSOT ratios and reject bad input with clear errors, protected by Dual-Track TDD.**

---

## 2. Users and scenarios

### 2.1 R-G-I-O

| | Content |
|---|---------|
| **R** | Lab student / developer converting meter, feet, yard for assignments and specs |
| **G** | One input → **all units** consistent; bad input → **clear error** (not silent wrong numbers) |
| **I** | String `unit:value` (e.g. `meter:2.5`) |
| **O** | All unit lines (default table) or explicit error |

### 2.2 Persona

| Field | Content |
|-------|---------|
| Role | Python AI lab student + occasional hardware spec conversion |
| Behavior | Calculator, spreadsheet, legacy `UnitConverter.py` |
| Domain | meter, feet, yard; `1m = 3.28084ft`, `1m = 1.09361yd`; feet↔yard via meter |

### 2.3 Core scenario

1. User runs CLI with `meter:2.5`.
2. System parses unit and value, converts via registry + converter (meter hub).
3. Prints meter, feet, yard (and future units) with SSOT ratios.
4. Invalid cases (`meter:-1`, `meter`, `cubit:1` unregistered) return clear errors.
5. **Test loop** reproduces success and failure (RED → GREEN → REFACTOR).

---

## 3. Domain rules

| Rule | Description |
|------|-------------|
| Input format | `unit:value` — colon-separated, one pair |
| Base units (P0) | meter, feet, yard |
| Ratios | `1 meter = 3.28084 feet`, `1 meter = 1.09361 yard` |
| Cross conversion | feet ↔ yard **via meter** (no direct feet-yard ratio in converter) |
| Precision | Display ~4–5 significant digits (see acceptance examples) |

---

## 4. Functional requirements (traceability)

| ID | Requirement | Given | Then | Track | Priority |
|----|-------------|-------|------|-------|----------|
| FR-01 | Parse input | `meter:2.5` | value=2.5, unit=meter | A/B | P0 |
| FR-02 | Output all units | meter 2.5 | feet~8.2021, yard~2.7340 | B | P0 |
| FR-03 | Unknown unit | `cubit:1` (unregistered) | clear error | A/B | P0 |
| FR-04 | Negative | `meter:-1` | reject | A | P0 |
| FR-05 | Malformed | `meter` / `abc` | format error | A | P0 |
| NFR-01 | OCP | add unit | no converter code change | B | P0 |
| NFR-02 | SRP | layout | Parser / Registry / Converter / Formatter split | - | P0 |
| EXT-01 | Config file | `units.json` | ratios loaded | B | P1 |
| EXT-02 | Dynamic register | cubit ratio | convertible | B | P1 |
| EXT-03 | Output format | `--format` | json / csv / table | A | P1 |

Source matrix: [guide/02_traceability-matrix.md](../guide/02_traceability-matrix.md).

RED test IDs (`D-*`, `U-*`): [guide/06_dualtrack-red-design.md](../guide/06_dualtrack-red-design.md).

---

## 5. Acceptance examples

| Input | Expected |
|-------|----------|
| `meter:2.5` | meter 2.5, feet ~8.2021, yard ~2.7340 |
| `feet:1` | meter ~0.3048 |
| `cubit:1` (unregistered) | unknown-unit error |
| `meter:-1` | rejected |
| `meter` / `abc` | format error |

---

## 6. Out of scope (P0) — Mom Test rationale

| Excluded | Reason |
|----------|--------|
| P1 JSON/YAML, dynamic units, `--format` **first** | Surface solution; P0 = one input, all units, trust |
| Extending legacy `if/elif` only | OCP/SRP smells — [guide/03](../guide/03_legacy-seed-analysis.md) |
| Architecture docs without tests | No test loop → no traceability or trust recovery |

---

## 7. Architecture (target)

- Layers: `src/entity/` (domain), `src/boundary/` (CLI, parser, formatter)
- Tests: `tests/entity/` (Track B, no domain mocks), `tests/boundary/` (Track A)
- Golden Master: `tests/_approval.py`, `tests/golden/`
- Details: [guide/04_target-architecture.md](../guide/04_target-architecture.md)

---

## 8. Success criteria (from Mom Test workbook)

| # | Criterion | Verification |
|---|-----------|--------------|
| 1 | `meter:2.5` → correct feet/yard (SSOT ratios) | pytest Track B + CLI |
| 2 | RED→GREEN test loop | `pytest tests/ -v` |
| 3 | Invalid input → explicit error | Track A tests |

---

## 9. Related documents

| Document | Description |
|----------|-------------|
| [Report/02.REPORT.md](../Report/02.REPORT.md) | Mom Test SSOT |
| [Report/03.REPORT.md](../Report/03.REPORT.md) | R-G-I-O workbook |
| [WORK_PLAN.md](../WORK_PLAN.md) | Phase roadmap |
| [MASTER_PROMPT.md](MASTER_PROMPT.md) | Session entry |

---

*PRD v0.1 — Spec phase. Implementation follows ARRR on branches `red` / `green` / `refactor`.*
