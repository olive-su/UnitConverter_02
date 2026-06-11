# UnitConverter_02

English version: [README.md](README.md).

| 항목 | 값 |
|------|-----|
| 브랜치 | `spec` |
| 단계 | **Spec** — RED 이전 요구사항·스캐폴딩 |
| 원격 | [olive-su/UnitConverter_02](https://github.com/olive-su/UnitConverter_02) |
| PR | [#2 spec → main](https://github.com/olive-su/UnitConverter_02/pull/2) |
| 최신 커밋 | `cb868da` — Mom Test, PRD, ARRR 하네스, 프로젝트 스캐폴딩 |

---

## 이 브랜치의 역할

ARRR(Analyze → Red → Green → Refactor) 워크플로의 **Spec** 브랜치입니다. 제품 요구사항, 아키텍처 가이드, Cursor 하네스, 빈 `src/` / `tests/` 스캐폴딩을 담습니다. **기능 테스트는 아직 없습니다** — 구현은 `red`·`green`에서 진행합니다.

## 제품 목표

레거시 길이 변환기(`UnitConverter.py`)를 추적 가능한 테스트 우선 CLI로 재구현:

- 입력: `단위:값` (예: `meter:2.5`)
- 출력: 등록된 모든 단위로 변환 (meter, feet, yard)
- 기준 비율: `1 m = 3.28084 ft = 1.09361 yd` (meter SSOT)
- 품질: OCP, SRP, 입력 검증, 설정·동적 단위·출력 포맷(P1) 확장

## `spec`에서 완료된 항목

| 영역 | 상태 |
|------|------|
| Mom Test 근거 | `Report/01`–`05` |
| PRD | `docs/PRD.md` (+ `.ko.md`) |
| 마스터 프롬프트 | `docs/MASTER_PROMPT.md` (+ `.ko.md`) |
| Phase 0 가이드 | `guide/00`–`06` (추적성, 아키텍처, ARRR, Dual-Track RED) |
| 작업 계획 (SSOT) | `WORK_PLAN.md` (+ `.ko.md`) |
| Cursor 하네스 | `AGENTS.md`, `.cursor/rules`, `.cursor/commands`, `harness/` |
| 프로젝트 레이아웃 | `pyproject.toml`, 빈 `src/entity`, `src/boundary`, `tests/` 트리 |
| 레거시 시드 | `UnitConverter.py` (참고용) |

## 브랜치 맵 (ARRR)

```text
main          ← 머지 대상
  ↑
spec          ← 현재 위치 (요구사항 + 하네스)
  ↓
red           ← 실패 테스트만 (src 구현 없음)
  ↓
green         ← 테스트 통과 최소 코드 (Cycle 1–4 완료)
  ↓
refactor      ← 구조 정리, 공개 계약 동일
```

사이클·추적 ID: `guide/05_arrr-7steps.md`, `guide/06_dualtrack-red-design.md`.

## 빠른 시작

### 사전 요구

- Python 3.11+
- 선택: `pip install -e ".[dev]"` (pytest; `spec`에서는 수집 테스트 없음)

### 에이전트·기여자 읽기 순서

1. [AGENTS.ko.md](AGENTS.ko.md) — 하네스 진입점
2. [WORK_PLAN.ko.md](WORK_PLAN.ko.md) — 빌드 순서·추적성
3. [docs/PRD.ko.md](docs/PRD.ko.md) — 제품 요구사항
4. [guide/00_Guide.ko.md](guide/00_Guide.ko.md) — 가이드 목차

### 이 브랜치 확인

```bash
python -m pytest --collect-only -q
# 기대: no tests collected (스캐폴딩만)
```

### 레거시 CLI (참고)

```bash
python UnitConverter.py
# 예: meter:2.5 입력 — 리팩터 전 단일 파일, 목표 아키텍처 아님
```

## 프로젝트 레이아웃

```text
UnitConverter_02/
├── docs/              PRD, MASTER_PROMPT
├── guide/             Phase 0 아키텍처·ARRR 문서
├── harness/           세션 로그, 에이전트 역할, 패턴
├── Report/, Prompting/ Mom Test 및 단계 export
├── src/               빈 패키지 스텁 (entity, boundary)
├── tests/             conftest만 — 기능 테스트 없음
├── .cursor/           규칙, 명령, 스킬
├── UnitConverter.py   레거시 시드
└── pyproject.toml
```

## 추적성 (미리보기)

| ID | 요구사항 | 트랙 |
|----|----------|------|
| FR-01–05 | 파싱, 출력, 오류 | A/B |
| NFR-01–02 | OCP, SRP 모듈 분리 | B |
| EXT-01–03 | 설정, 동적 단위, 출력 포맷 | B / A |

전체 매트릭스: `guide/02_traceability-matrix.ko.md`.

## 다음 단계 (머지 또는 체크아웃 후)

1. **`red`** — Dual-Track 번들별 실패 테스트 스켈레톤 (`D-CNV-*`, `U-IN-*`, …).
2. **`green`** — pytest 통과까지 최소 구현.
3. **`refactor`** — 테스트 계약 유지하며 구조 개선.

## 라이선스·기여자

강의/팀 프로젝트. 리뷰어·단계 체크리스트: `WORK_PLAN.ko.md` 9절.
