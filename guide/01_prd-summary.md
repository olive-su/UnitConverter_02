# 01. PRD Summary — What We Build

Korean version: [01_prd-summary.ko.md](01_prd-summary.ko.md). Source: `goinfre/01`.

Re-implement a length-unit conversion CLI so it is traceable from PRD to tests.

## Problem

- Legacy `UnitConverter.py` hardcodes ratios, branches per unit, and skips validation.
- Goal: same behavior, but extensible (OCP), separated (SRP), and validated.

## Core Requirements

- Input: parse `unit:value` (e.g. `meter:2.5`).
- Base units: meter, feet, yard.
- Ratios: `1 m = 3.28084 ft = 1.09361 yd`. feet<->yard computed via meter.
- Quality: OCP, SRP, input validation (negative, malformed format, unknown unit).

## P1 Extensions

1. Config file: load ratios from `units.json` / YAML.
2. Dynamic registration: register `1 cubit = 0.4572 meter` and convert immediately.
3. Output format: `--format json | csv | table`.

## Expected Output

```text
$ python -m unit_converter "meter:2.5"
2.5 meter = 8.2021 feet
2.5 meter = 2.7340 yard
...
```

## Acceptance Examples

| Input | Expected |
|-------|----------|
| `meter:2.5` | meter 2.5, feet ~8.2021, yard ~2.7340 |
| `feet:1` | meter 0.3048 (via ratio) |
| `cubit:1` (unregistered) | clear unknown-unit error |
| `meter:-1` | rejected (negative) |
| `meter` / `abc` | format error |

## Next

- Anchor each requirement to a test ID: [02 Traceability Matrix](02_traceability-matrix.md).
- See the smells this design removes: [03 Legacy Seed Analysis](03_legacy-seed-analysis.md).
