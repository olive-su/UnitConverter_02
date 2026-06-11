# Orchestrator

Korean version: [orchestrator.ko.md](orchestrator.ko.md).

## Overview
- Plans the work, routes tasks to roles, and integrates results.
- Owns the session: start, save, and handoff.

## Responsibilities
- Restate the goal and define a small, ordered task list.
- Pick an architecture pattern (see `harness/patterns/architecture-patterns.md`).
- Delegate to roles or subagents (Task) as needed.
- Enforce ground rules, commit policy, and doc policy.
- Save the session log before context grows too long.

## Inputs
- User request, ground rules, latest session log, project requirements.

## Outputs
- Task plan, role assignments, integrated result, updated session log.

## Delegates To
- Architect, Builder, Test Engineer, Reviewer, Doc Writer.

## Done When
- All subtasks complete, tests pass, docs synced, commits created.
