# Commit Convention

Korean version: [commit-convention.ko.md](commit-convention.ko.md).

## Overview
- English Conventional Commits for all commits.
- Auto local commits allowed; push only after user confirmation.

## When to Commit
- A logical unit is complete (feature, fix, refactor, test, docs).
- The change grows large; split into small cohesive commits.
- A session log is saved.

## Format
- `type: subject` in imperative mood, <= 72 chars.
- Optional body explains why, not what.

## Types
- `feat`: new feature.
- `fix`: bug fix.
- `refactor`: no behavior change.
- `test`: tests only.
- `docs`: docs only.
- `chore`: tooling or config.

## Examples
- `feat: add unit registry for dynamic units`
- `fix: reject negative input values`
- `refactor: extract converter from cli`
- `test: cover unknown unit error path`
- `docs: add session log 2026-06-11-01`

## Pre-Commit
- Run tests and linter; do not commit on failure.
- Do not commit secrets.

## Push
- Never push without explicit user confirmation.
- No force-push or direct push to `main` unless requested.
