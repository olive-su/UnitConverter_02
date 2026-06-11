# UnitConverter_02 — 마스터 세션 프롬프트

English version: [MASTER_PROMPT.md](MASTER_PROMPT.md).

작업 세션 시작 시 붙여 넣거나 경로로 참조한다. 이슈·PR 텍스트는 영문, 작업 대화는 한국어 가능.

## 북극성 — C2C 추적성

모든 요구([guide/02_traceability-matrix.ko.md](../guide/02_traceability-matrix.ko.md)의 FR/NFR/EXT)는 테스트 ID와 파일 경로에 추적되어야 한다.

Dual-Track TDD를 ARRR로 실행하는 것이 추적성을 보장하는 유일한 승인된 방법:

- Ask = RED (`tests/`만)
- Respond = GREEN (최소 통과 구현)
- Refine = REFACTOR (구조, 계약 불변)
- Repeat = 다음 RED 묶음

ARRR과 "C2C x Dual-Track TDD"는 별도 방법론이 아니라 같은 사이클이다.

## 편집 전 읽기 순서

1. [WORK_PLAN.ko.md](../WORK_PLAN.ko.md) — 현재 phase 게이트
2. [AGENTS.ko.md](../AGENTS.ko.md) + `.cursor/rules/*`
3. `harness/sessions/INDEX.ko.md` + 최신 세션 로그
4. [guide/00_Guide.ko.md](../guide/00_Guide.ko.md) 및 해당 phase 가이드
5. `docs/PRD.ko.md` (Spec phase 이후)
6. 톤 참고: 동일 phase의 `MagicSquare_1004` Report/Prompting

## 저장소·브랜치 계약

- 원격: `olive-su/UnitConverter_02`
- 브랜치 흐름: `main` -> `spec` -> `red` -> `green` -> `refactor` -> (반복) -> `new_features`
- **현재 phase**: Phase 1 — Spec, 브랜치 `spec`

단계 전환 시: 브랜치 전환, 영문 이슈, 내가 요청할 때 커밋, 내가 확인한 뒤에만 푸시, 아래 리뷰어로 영문 PR.

| Phase | 브랜치 | 수정 범위 |
|-------|--------|-----------|
| Spec | `spec` | docs, `.cursor/`, `Report/`, `Prompting/`, harness |
| RED | `red` | `tests/`만 |
| GREEN | `green` | `src/` + 해당 tests |
| REFACTOR | `refactor` | 리팩터만 (계약 불변) |

### PR 리뷰어

`yhkwon0817`, `jhgomi`, `curiosus`, `okpym`

## 규칙 SSOT

- 프로젝트 규칙: `.cursor/rules/*.mdc`와 harness — 루트 `.cursorrules` **중복 생성 금지**.
- 이중 언어 문서: 가독 `*.md`는 `name.md` + `name.ko.md`.
- 커밋: 내가 요청할 때 영문 Conventional Commits.
- 명시적 확인 없이 푸시 금지.

## Phase 1 — Spec 산출물

WORK_PLAN에 명시되지 않으면 `src/` 구현·pytest 실행 **금지**.

### 1. Mom Test (에이전트 자체 시뮬레이션)

- **Role 1**: 인터뷰어 — Mom Test 규칙, 질문 1개, 솔루션 제안 금지.
- **Role 2**: 페르소나 — 6시간 AI 실습 Activities 수업생([README.md](../README.md))이며, ft/m 스펙·스프레드시트 재입력·잘못된 비율로 ~20분 손실 등 실무 단위 변환 고통도 겪는 사용자.
- Transcript에 3턴 인터뷰 후 산출:
  - 표면 문제 (솔루션 혼입 금지 문장)
  - 진짜 문제 (한 문장)
  - Mom Test 증거 (인용 3줄)
  - R-G-I-O 워크북 + 검증 방법이 있는 성공 기준 3개
- 산출물: `Report/01.REPORT.md`~`03`, `Prompting/01.Export-Transcript.md`~`03`

### 2. PRD

- Mom Test + guide/01 + guide/02로 `docs/PRD.md` + `docs/PRD.ko.md`
- 범위, Mom Test 근거 배제, 추적표, 인수 예시 포함

### 3. Cursor ARRR 하네스 (Spec — 파일만, 테스트 실행 없음)

슬래시 커맨드 생성 (이름만 — 추가 질문 금지):

- `red-test-plan`, `red-skeleton`, `green-minimal`, `golden-master`, `refactor-smell`, `refactor-safe`, `export-session`, `export`

스킬 생성:

- `unit-converter-tdd` — ARRR, Dual-Track, RED 규칙
- `unit-converter-docs` — Report/Prompting + `report-template.md`, `transcript-template.md`, `phase-checklist.md`

MagicSquare_1004 커맨드 톤 맞춤. SSOT: WORK_PLAN, guide/, AGENTS.md.

산출물: `Report/04.REPORT.md`, `Prompting/04.Export-Transcript.md` (Cursor 4그룹 가이드).

### 4. Phase 2 스캐폴딩 (같은 `spec` 브랜치, PR 전)

Phase 1 산출물 후: `pyproject.toml`, guide/04 기준 `src/`·`tests/` 골격 — RED/GREEN 본문 없음.

### 5. Spec PR 게이트 (단일 통합 PR)

`spec`에서 Phase 1 + Phase 2 완료 후:

- 이슈 제안: `spec: PRD, Mom Test evidence, ARRR harness, and project scaffolding`
- `main` 대상 PR, 위 리뷰어
- 내가 명시적으로 요청하지 않으면 푸시·커밋 금지

### 6. 세션 종료

- `/export`로 최신 Report + Prompting
- 해당 시 harness 세션 로그(en + ko) + INDEX 갱신

## RED 규칙 (이후 phase — 위반 금지)

- `red`에서 `src/` 변경 금지
- `pytest.fail("RED: ...")` 허용; skip/xfail 금지
- 1 RED 묶음 = 1 커밋
- Track B: `tests/entity/`, 도메인 목 금지
- Track A: `tests/boundary/`, 도메인 목 허용

## 첫 RED 묶음 (스캐폴딩 후)

Track B 우선: **D-CNV-01** (FR-02) — [guide/06_dualtrack-red-design.ko.md](../guide/06_dualtrack-red-design.ko.md).

## ARRR 사이클 슬래시 워크플로

```text
/red-test-plan -> /red-skeleton -> /green-minimal -> /golden-master -> /refactor-smell -> /refactor-safe -> /export
```

## 본 프롬프트에 고정된 결정

| 항목 | 결정 |
|------|------|
| Mom Test 페르소나 | README Activities 수업생 + ft/m 변환 구체적 고통 |
| Spec PR 범위 | Phase 1 + Phase 2 스캐폴딩 후 `spec`에서 단일 통합 PR |
| 규칙 위치 | `.cursor/rules/*.mdc`만; 루트 `.cursorrules` 없음 |
| REFACTOR 브랜치 | `refactor` |
