# Architecture Patterns

Korean version: [architecture-patterns.ko.md](architecture-patterns.ko.md).

## Overview
- Six team patterns from `revfactory/harness`, mapped to Cursor.
- Cursor has no Agent Teams runtime; delegate via subagents (Task).
- Pick the smallest pattern that fits the task.

## Patterns

### Pipeline
- Use for: sequential, dependent steps.
- Cursor: run steps in order within one session.
- Example: analyze, design, build, test, document.

### Fan-out / Fan-in
- Use for: independent, parallel subtasks.
- Cursor: launch parallel subagents (Task), then merge results.
- Example: parallel research on multiple modules.

### Expert Pool
- Use for: context-dependent selection.
- Cursor: apply the role doc that fits the current need.
- Example: pick Architect for design, Builder for code.

### Producer-Reviewer
- Use for: generation plus quality gate.
- Cursor: Builder produces; Reviewer subagent verifies.
- Example: implement feature, then review diff.

### Supervisor
- Use for: dynamic task distribution.
- Cursor: Orchestrator splits and assigns via Task.
- Example: orchestrator coordinates build and test in parallel.

### Hierarchical Delegation
- Use for: large tasks needing recursive breakdown.
- Cursor: subagents spawn sub-subagents (limited depth).
- Example: top task split into module-level subtasks.

## Selection Guide
- Small task: single orchestrated session (Pipeline).
- Independent parts: Fan-out / Fan-in.
- Quality-critical: Producer-Reviewer.
- Many moving parts: Supervisor or Hierarchical.
