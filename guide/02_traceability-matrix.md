# 02. Traceability Matrix — PRD to Tests

Korean version: [02_traceability-matrix.ko.md](02_traceability-matrix.ko.md). Source: `goinfre/02`.

Map every FR / NFR / EXT to a test ID, 1:1, so concept (PRD) stays traceable to code (test).

## Rule

- Every implemented test cites exactly one ID below.
- Track A = UI / boundary. Track B = domain / logic.

## Matrix

| ID | Requirement | Given | Then | Track | Target module | P |
|----|-------------|-------|------|-------|---------------|---|
| FR-01 | Parse `meter:2.5` | valid string | value=2.5, unit=meter | A/B | `app/input_parser.py` | P0 |
| FR-02 | Output all units | meter 2.5 | feet~8.2021, yard~2.7340 | B | `domain/converter.py` | P0 |
| FR-03 | Unknown unit | `cubit:1` (unregistered) | clear error | A/B | `domain/unit_registry.py` | P0 |
| FR-04 | Negative | `meter:-1` | reject / raise | A | `app/input_parser.py` | P0 |
| FR-05 | Malformed | `meter` / `abc` | format error | A | `app/input_parser.py` | P0 |
| NFR-01 | OCP | add `inch` | no edit to converter code | B | `domain/unit_registry.py` | P0 |
| NFR-02 | SRP | - | Parser / Registry / Converter / Formatter split | - | package layout | P0 |
| EXT-01 | Config file | `units.json` | ratios loaded | B | `infrastructure/config_loader.py` | P1 |
| EXT-02 | Dynamic registration | `1 cubit = 0.4572 m` | convertible immediately | B | `domain/unit_registry.py` | P1 |
| EXT-03 | Output format | `--format` | json / csv / table verified | A | `app/output_formatter.py` | P1 |

## Notes

- Track and target-module columns are added on top of the source matrix to bind requirements to the architecture ([04 Target Architecture](04_target-architecture.md)).
- RED-level test IDs (`D-*`, `U-*`) derive from these and are designed in [06 Dual-Track RED Design](06_dualtrack-red-design.md).

## Next

- Design the first failing tests: [06 Dual-Track RED Design](06_dualtrack-red-design.md).
