# AGENTS.ko.md

이 저장소에서 작업하는 AI 에이전트의 진입점 문서.
English version: [AGENTS.md](AGENTS.md).

## 개요
- 에이전트 기반 개발을 위한 Cursor 네이티브 하네스.
- `revfactory/harness`(Claude Code)를 Cursor에 맞게 재설계.
- 목표: 긴 컨텍스트와 세션 교체에도 일관된 에이전트 작업 유지.

## 세션 시작 시 읽는 순서
1. `.cursor/rules/00-ground-rules.mdc` — 프로젝트 전반 규칙.
2. `harness/sessions/INDEX.ko.md` — 세션 히스토리.
3. 인덱스가 가리키는 최신 세션 로그.

## 핵심 규약
- 그라운드 룰: `.cursor/rules/00-ground-rules.mdc`.
- 세션 프로토콜: `.cursor/rules/10-session-history.mdc`.
- 커밋/푸쉬 정책: `.cursor/rules/20-commit-policy.mdc`.
- 문서 정책: `.cursor/rules/30-doc-policy.mdc`.
- 팀/패턴: `.cursor/rules/40-agent-team.mdc`.

## 빠른 규칙
- 커밋 메시지: 영문, Conventional Commits.
- 로컬 자동 커밋 허용. 사용자 확인 없이 push 금지.
- 모든 `*.md`는 `name.md`와 `name.ko.md` 두 버전 유지.
- 문서: 개조식·간결, 이모지 금지.

## 역할
- `harness/agents/` 참고: orchestrator, architect, builder, test-engineer, reviewer, doc-writer.

## 커맨드
- `.cursor/commands/`의 `/session-start`, `/session-save`, `/harness-commit`.

## 프로젝트 컨텍스트
- 대상 프로젝트: `UnitConverter` (Python).
- 요구사항: `README.md`, 설계 목표: `Ref/02-Goal.md`.
