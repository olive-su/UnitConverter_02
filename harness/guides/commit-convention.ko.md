# 커밋 컨벤션 (Commit Convention)

English version: [commit-convention.md](commit-convention.md).

## 개요
- 모든 커밋은 영문 Conventional Commits.
- 로컬 자동 커밋 허용. 사용자 확인 후에만 push.

## 커밋 시점
- 논리 단위 완료 (기능, 수정, 리팩터, 테스트, 문서).
- 변경이 커지면 작고 응집된 커밋으로 분할.
- 세션 로그 저장 시.

## 형식
- `type: subject` 명령형, 72자 이하.
- 본문(선택)은 무엇이 아니라 왜를 설명.

## 타입
- `feat`: 새 기능.
- `fix`: 버그 수정.
- `refactor`: 동작 변경 없음.
- `test`: 테스트만.
- `docs`: 문서만.
- `chore`: 도구·설정.

## 예시
- `feat: add unit registry for dynamic units`
- `fix: reject negative input values`
- `refactor: extract converter from cli`
- `test: cover unknown unit error path`
- `docs: add session log 2026-06-11-01`

## 커밋 전
- 테스트와 린터 실행. 실패 시 커밋 금지.
- 시크릿 커밋 금지.

## 푸쉬
- 사용자 확인 없이 push 금지.
- 요청 없이 force-push 또는 `main` 직접 push 금지.
