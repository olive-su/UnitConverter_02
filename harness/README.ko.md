# Cursor 에이전트 하네스 (Cursor Agent Harness)

English version: [README.md](README.md).

## 개요
- 에이전트 기반 개발을 위한 Cursor 네이티브 하네스.
- `revfactory/harness`(Claude Code)를 Cursor에 맞게 재설계.
- 긴 컨텍스트와 세션 교체에도 에이전트 작업을 일관되게 유지.

## 필요성
- 긴 작업은 세션 교체를 유발. 그라운드 룰로 일관성 유지.
- 세션 로그로 컨텍스트 유실 방지.
- 클린코드 커밋으로 히스토리 가독성 유지.
- 이중언어 문서로 한국어·영어 독자 모두 지원.

## 구조
- `.cursor/rules/` — 운영 규칙 (영문, 머신 설정).
- `.cursor/commands/` — 슬래시 커맨드: session-start, session-save, harness-commit.
- `AGENTS.md` / `AGENTS.ko.md` — 진입점과 행동 규약.
- `harness/agents/` — 6개 역할 정의 (이중언어).
- `harness/patterns/` — Cursor에 매핑한 6개 아키텍처 패턴.
- `harness/guides/` — 문서·커밋 컨벤션.
- `harness/sessions/` — 세션 인덱스, 템플릿, 로그.

## 사용법
1. 세션 시작: `/session-start` 실행.
2. 계획: 오케스트레이터가 패턴과 역할 선택.
3. 구현·테스트·리뷰: 역할 문서에 따라 진행.
4. 커밋: `/harness-commit` 실행 (영문 Conventional Commits).
5. 저장: 컨텍스트가 길어지기 전에 `/session-save` 실행.

## 컨벤션
- 커밋: 영문 Conventional Commits. 사용자 확인 후에만 push.
- 문서: 모든 `*.md`는 `name.md`와 `name.ko.md` 보유. 개조식·간결·이모지 금지.

## 역할
- 오케스트레이터, 아키텍트, 빌더, 테스트 엔지니어, 리뷰어, 문서 작성자.
- `harness/agents/` 참고.
