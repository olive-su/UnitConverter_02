# UnitConverter_02

Korean version: [README.ko.md](README.ko.md).

Traceable length-unit CLI re-implemented with ARRR / Dual-Track TDD. Converts a single `unit:value` input into all registered units using **meter as the single source of truth (SSOT)**.

| Field | Value |
|-------|-------|
| Branch | `main` (stable delivery) |
| Remote | [olive-su/UnitConverter_02](https://github.com/olive-su/UnitConverter_02) |
| Python | 3.11+ |
| Status | Cycle 1–4 complete — **15 tests passing** |

---

## Overview

Students and developers enter one length value (e.g. `meter:2.5`) and receive consistent conversions to **meter, feet, and yard** — plus dynamically registered units and configurable ratios. The legacy monolith `UnitConverter.py` is preserved as reference only; runtime logic lives under `src/`.

**Conversion ratios (meter hub):**

- `1 meter = 3.28084 feet`
- `1 meter = 1.09361 yard`
- feet ↔ yard always via meter (no direct ratio)

## Quick start

```bash
# Clone and enter the repo
git clone https://github.com/olive-su/UnitConverter_02.git
cd UnitConverter_02

# Virtual environment (recommended)
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # macOS / Linux

# Install with dev dependencies
pip install -e ".[dev]"

# Run the full test suite
python -m pytest -q
# Expected: 15 passed
```

## Features

| Area | Capability | Trace IDs |
|------|------------|-----------|
| Parsing | `unit:value` format, empty/invalid/negative rejection | FR-01, FR-04, FR-05 / U-IN-* |
| Conversion | All units from one input via meter SSOT | FR-02 / D-CNV-* |
| Errors | Unknown unit handling | FR-03 |
| Config | Load ratios from JSON file | EXT-01 / D-CFG-01 |
| Registry | Register custom units at runtime (e.g. cubit) | EXT-02 / D-REG-01 |
| Output | `lines`, `json`, `csv`, `table` formats | EXT-03 / U-OUT-* |
| Quality | OCP-friendly registry; SRP module split | NFR-01, NFR-02 |

## Architecture

Layered layout per `guide/04_target-architecture.md`:

```text
src/
├── entity/
│   ├── constants.py      # UNIT_TO_METER / METER_TO_UNIT maps (refactored)
│   ├── converter.py      # to_meter, convert_all
│   └── unit_registry.py  # dynamic unit registration
├── boundary/
│   ├── input_parser.py   # parse and validate input
│   └── output_formatter.py
└── infrastructure/
    └── config_loader.py  # external JSON ratios

tests/
├── entity/               # domain tests (5)
├── boundary/             # parser / formatter tests (7)
└── golden/cycle1_track_b/  # regression baselines (3)
```

**Design principles:**

- **SRP** — parser, converter, registry, formatter, and config loader are separate modules.
- **OCP** — new units via registry or config without editing converter branches.
- **Traceability** — every test cites a requirement ID from `guide/02_traceability-matrix.md`.

## Usage examples

### Library

```python
from src.boundary.input_parser import parse_input
from src.entity.converter import convert_all
from src.boundary.output_formatter import format_output

unit, value = parse_input("meter:2.5")
result = convert_all(unit, value)
print(format_output(result, output_format="lines"))
print(format_output(result, output_format="json"))
```

### Config file

Sample ratios: `units.json` at repo root. Load via `src/infrastructure/config_loader.py` (see tests in `tests/entity/test_d_cfg_01.py`).

### Legacy CLI (reference)

```bash
python UnitConverter.py
```

Pre-refactor seed — not the target architecture. Use `src/` modules for new work.

## Test suite

| Layer | Tests | Purpose |
|-------|-------|---------|
| Entity | 5 | conversion, registry, config |
| Boundary | 7 | input validation, output formats |
| Golden | 3 | Cycle 1 Track B regression JSON baselines |

```bash
python -m pytest -v              # verbose
python -m pytest tests/entity/   # domain only
python -m pytest tests/golden/   # golden master only
```

## How this was built (ARRR)

Development followed Analyze → Red → Green → Refactor on feature branches; `main` integrates the result after review.

| Phase | Branch | Delivered |
|-------|--------|-----------|
| Spec | `spec` | PRD, guides, harness, scaffolding |
| Red | `red` | Failing test contracts (11 bundles) |
| Green | `green` | Minimal passing implementation |
| Refactor | `refactor` | `constants.py` map extraction, contract unchanged |

Merged path (assumed): `spec` → `red` → `green` → `refactor` → **`main`**.

Build order and trace matrix: [WORK_PLAN.md](WORK_PLAN.md).

## Documentation

| Document | Role |
|----------|------|
| [docs/PRD.md](docs/PRD.md) | Product requirements |
| [docs/MASTER_PROMPT.md](docs/MASTER_PROMPT.md) | Agent session entry prompt |
| [guide/00_Guide.md](guide/00_Guide.md) | Guide index |
| [AGENTS.md](AGENTS.md) | Cursor harness contract |
| [WORK_PLAN.md](WORK_PLAN.md) | SSOT build plan |

All human-readable docs ship in English and Korean (`name.md` + `name.ko.md`).

## Project layout

```text
UnitConverter_02/
├── src/                 # production code
├── tests/               # pytest suites + golden baselines
├── docs/                # PRD, master prompt
├── guide/               # architecture and ARRR guides
├── harness/             # session logs, agent roles
├── Report/, Prompting/  # phase evidence exports
├── .cursor/             # rules, commands, skills
├── UnitConverter.py     # legacy seed (reference)
├── units.json           # sample config
└── pyproject.toml
```

## Contributing

1. Read [AGENTS.md](AGENTS.md) and the latest session in `harness/sessions/`.
2. Follow ARRR: add or adjust tests on `red`, implement on `green`, refactor on `refactor`.
3. Commits: English, [Conventional Commits](https://www.conventionalcommits.org/).
4. Run `python -m pytest` before opening a PR.
5. Update bilingual docs when behavior or structure changes.

## License

Course / team educational project. See repository maintainers in `WORK_PLAN.md` section 9.
