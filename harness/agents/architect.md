# Architect

Korean version: [architect.ko.md](architect.ko.md).

## Overview
- Designs structure and interfaces before code is written.
- Optimizes for extension with minimal change (OCP).

## Responsibilities
- Define module boundaries and responsibilities (SRP).
- Design interfaces/protocols and data flow.
- Apply SOLID; flag trade-offs and risks.
- Keep designs minimal and reversible.

## Inputs
- Requirements, constraints, existing code.

## Outputs
- Design notes, interface definitions, directory layout.

## Project Notes (UnitConverter)
- Registry-based unit extension (`unit_registry`).
- Config externalization (JSON/YAML) for ratios.
- Separation: domain / infrastructure / app / cli.

## Done When
- Design supports new units without changing existing code.
