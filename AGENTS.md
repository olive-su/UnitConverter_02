# AGENTS.md

Entry point for AI agents working in this repository.
Korean version: [AGENTS.ko.md](AGENTS.ko.md).

## What This Is
- A Cursor-native harness for agent-based development.
- Adapted from `revfactory/harness` (Claude Code) for Cursor.
- Goal: consistent agent work across long contexts and session swaps.

## Read Order (Every Session)
1. `.cursor/rules/00-ground-rules.mdc` — project-wide rules.
2. `harness/sessions/INDEX.md` — session history.
3. The latest session log referenced in the index.

## Core Contracts
- Ground rules: `.cursor/rules/00-ground-rules.mdc`.
- Session protocol: `.cursor/rules/10-session-history.mdc`.
- Commit/push policy: `.cursor/rules/20-commit-policy.mdc`.
- Documentation policy: `.cursor/rules/30-doc-policy.mdc`.
- Team and patterns: `.cursor/rules/40-agent-team.mdc`.

## Quick Rules
- Commit messages: English, Conventional Commits.
- Auto local commits allowed; never push without user confirmation.
- Every `*.md` doc has both `name.md` and `name.ko.md`.
- Docs: terse, bullet-point, no emojis.

## Roles
- See `harness/agents/` for orchestrator, architect, builder, test-engineer, reviewer, doc-writer.

## Commands
- `/session-start`, `/session-save`, `/harness-commit` in `.cursor/commands/`.

## Project Context
- Target project: `UnitConverter` (Python).
- Requirements: `README.md`, design goal: `Ref/02-Goal.md`.
