# Phase transition checklist

## Spec (`spec`)

- [ ] Mom Test Report 01–03, Prompting 01–03
- [ ] `docs/PRD.md` + `.ko.md`
- [ ] `.cursor/` commands + skills
- [ ] Scaffolding skeleton (no RED/GREEN bodies)
- [ ] Report/Prompting for session
- [ ] Issue + PR (English) when user requests

## RED (`red`)

- [ ] `/red-test-plan` design in chat or Report
- [ ] `/red-skeleton` — tests only, FAIL
- [ ] One bundle = one commit
- [ ] `/export`

## GREEN (`green`)

- [ ] `/green-minimal` — PASS
- [ ] `/golden-master` if serialized output
- [ ] `/export`

## REFACTOR (`refactor`)

- [ ] `/refactor-smell` — table only
- [ ] `/refactor-safe` — one smell, tests green
- [ ] `/export`

## Git (user confirms push)

- [ ] `gh issue create` (English)
- [ ] `gh pr create --reviewer yhkwon0817,jhgomi,curiosus,okpym`
