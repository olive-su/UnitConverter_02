# Cursor Agent Harness

Korean version: [README.ko.md](README.ko.md).

## Overview
- A Cursor-native harness for agent-based development.
- Adapted from `revfactory/harness` (Claude Code) for Cursor.
- Keeps agent work consistent across long contexts and session swaps.

## Why
- Long tasks force session swaps; ground rules keep work consistent.
- Session logs prevent context loss.
- Clean-code commits keep history readable.
- Bilingual docs serve Korean and English readers.

## Structure
- `.cursor/rules/` — operational rules (English, machine config).
- `.cursor/commands/` — slash commands: session-start, session-save, harness-commit.
- `AGENTS.md` / `AGENTS.ko.md` — entry point and behavior contract.
- `harness/agents/` — six role definitions (bilingual).
- `harness/patterns/` — six architecture patterns mapped to Cursor.
- `harness/guides/` — documentation and commit conventions.
- `harness/sessions/` — session index, template, and logs.

## How to Use
1. Start a session: run `/session-start`.
2. Plan: orchestrator picks a pattern and role(s).
3. Build, test, review per role docs.
4. Commit: run `/harness-commit` (English Conventional Commits).
5. Save: run `/session-save` before context grows long.

## Conventions
- Commits: English Conventional Commits; push only after user confirmation.
- Docs: every `*.md` has `name.md` and `name.ko.md`; terse, bullet-point, no emojis.

## Roles
- Orchestrator, Architect, Builder, Test Engineer, Reviewer, Doc Writer.
- See `harness/agents/`.
