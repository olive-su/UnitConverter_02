# UnitConverter_02

English version: [README.md](README.md).

| 항목 | 값 |
|------|-----|
| 브랜치 | `refactor` |
| 단계 | **Refactor** — 구조 정리, 테스트 계약 동일 |
| 원격 | [olive-su/UnitConverter_02](https://github.com/olive-su/UnitConverter_02) |
| 최신 커밋 | `6219a81` — 단위 비율 맵 추출 (계약 불변) |
| 범위 | **Cycle 1 Track B만** (D-CNV + golden) |

---

## 이 브랜치의 역할

**Refactor** 브랜치: **관측 가능한 동작은 바꾸지 않고** 내부 구조를 개선합니다. 첫 리팩터 커밋은 하드코딩 비율을 `src/entity/constants.py`로 분리하고, `converter.py`를 맵 조회 기반으로 전환합니다.

**테스트 6개 통과** — Cycle 1 entity(3) + golden master(3). Track A(파서/포매터)와 Cycle 3–4(레지스트리, 설정, 출력 포맷)는 `green`에만 있음; 여기서 리팩터를 확장하려면 `green`을 먼저 머지하세요.

## 빠른 시작

```bash
pip install -e ".[dev]"
python -m pytest -q
# 기대: 6 passed
```

## 리팩터 변경 (Cycle 1 green 대비)

| 이전 | 이후 |
|------|------|
| `converter.py` 안에 비율·분기 | `constants.py`: `UNIT_TO_METER`, `METER_TO_UNIT` |
| `if unit == "meter"` / `if unit == "feet"` | `dict.get` + `convert_all`에서 dict comprehension |

공개 함수는 동일:

- `to_meter(unit, value) -> float`
- `convert_all(source_unit, value) -> dict[str, float]`

## 소스 레이아웃 (이 브랜치)

```text
src/entity/
├── constants.py   # 비율 맵 (신규)
└── converter.py     # 맵 기반 변환
tests/entity/
├── test_d_cnv_01.py
├── test_d_cnv_02.py
└── test_d_cnv_03.py
tests/golden/cycle1_track_b/   # JSON 베이스라인
```

이 브랜치에는 아직 `src/boundary/`, `src/infrastructure/`, `unit_registry.py` 없음.

## 테스트 목록

| 테스트 | 추적 | Golden 베이스라인 |
|--------|------|-------------------|
| `test_d_cnv_01` | D-CNV-01 | `d_cnv_01_to_meter_one_feet.json` |
| `test_d_cnv_02` | D-CNV-02 | `d_cnv_02_convert_all_meter_to_feet.json` |
| `test_d_cnv_03` | D-CNV-03 | `d_cnv_03_convert_all_feet_to_yard.json` |

## 브랜치 맵

```text
green     → Cycle 1–4 전체 (15 테스트) — 머지 기준
refactor  → 현재 위치 (Cycle 1 리팩터만, 6 테스트)
```

권장 흐름:

1. `green` → `main` 머지 (또는 `refactor`로).
2. `refactor`를 최신 `green` 위에 rebase.
3. 리팩터 확장 (`/refactor-smell`) 시 15개 테스트 모두 green 유지.

## 리팩터 규칙

- 계약이 틀린 경우가 아니면 테스트 수정 금지 (수정은 `red`에서).
- 커밋당 리팩터 테마 하나; 커밋 전 범위 내 pytest 실행.
- 동작 변경보다 클래스/모듈 추출 우선.

참고: `guide/05_arrr-7steps.ko.md`, `WORK_PLAN.ko.md` 5절.

## 문서

- 아키텍처 목표: `guide/04_target-architecture.ko.md`
- 해결한 레거시 스멜: `guide/03_legacy-seed-analysis.ko.md`
- 에이전트 하네스: `AGENTS.ko.md`

## 다음 단계

- `green`을 `refactor`에 머지해 전체 구현과 맞추기.
- 테스트 green 유지하며 refactor-smell 계속 (parser/formatter/registry).
- 이 브랜치에서 전체 테스트 통과 후 `main`으로 PR.
