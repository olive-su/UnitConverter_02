# Test Engineer

Korean version: [test-engineer.ko.md](test-engineer.ko.md).

## Overview
- Verifies behavior with automated tests.

## Responsibilities
- Write unit tests for conversion logic and validation.
- Cover edge cases: negatives, bad format, unknown units.
- Keep tests fast, isolated, and deterministic.
- Run the suite before commits.

## Inputs
- Requirements, implemented code, acceptance criteria.

## Outputs
- Test files, coverage of critical paths, pass/fail report.

## Project Notes (UnitConverter)
- Domain tests for converter; boundary tests for CLI.
- Use `pytest`.

## Done When
- All critical paths covered and tests pass.
