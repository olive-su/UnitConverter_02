# UnitConverter_02

English version: [README.md](README.md).

| 항목 | 값 |
|------|-----|
| 브랜치 | `red` |
| 단계 | **Red** — 실패 테스트만, 프로덕션 구현 없음 |
| 원격 | [olive-su/UnitConverter_02](https://github.com/olive-su/UnitConverter_02) |
| PR | [#4 red → main](https://github.com/olive-su/UnitConverter_02/pull/4) |
| 최신 커밋 | `e9db033` — U-OUT-04 실패 스켈레톤 (Track A) |

---

## 이 브랜치의 역할

ARRR / Dual-Track TDD의 **Red** 브랜치입니다. Cycle 1–4 번들에 대한 **의도적 실패 테스트 11개**가 계약을 정의합니다. `src/`는 빈 패키지 스텁만 있으며 **변환·파서·포매터 코드는 없습니다**. GREEN 작업은 `green`에서 합니다.

## 기대 테스트 결과

```bash
pip install -e ".[dev]"
python -m pytest -q
# 기대: 11 failed (모두 RED — 정상)
```

## 테스트 목록 (전부 RED)

### Track B — Entity / 도메인

| 테스트 파일 | 추적 ID | 요구사항 |
|-------------|---------|----------|
| `tests/entity/test_d_cnv_01.py` | D-CNV-01 / FR-02 | `to_meter` — 1 feet → meter |
| `tests/entity/test_d_cnv_02.py` | D-CNV-02 / FR-02 | `convert_all` — meter → 전 단위 |
| `tests/entity/test_d_cnv_03.py` | D-CNV-03 / FR-02 | feet → yard (meter SSOT) |
| `tests/entity/test_d_reg_01.py` | D-REG-01 / EXT-02 | 동적 단위 등록 (cubit) |
| `tests/entity/test_d_cfg_01.py` | D-CFG-01 / EXT-01 | 깨진 JSON 설정 → 오류 |

### Track A — Boundary / CLI

| 테스트 파일 | 추적 ID | 요구사항 |
|-------------|---------|----------|
| `tests/boundary/test_u_in_01.py` | U-IN-01 / FR-05 | 빈 입력 → 형식 오류 |
| `tests/boundary/test_u_in_02.py` | U-IN-02 / FR-05 | 콜론 없음 → 형식 오류 |
| `tests/boundary/test_u_in_03.py` | U-IN-03 / FR-04 | 음수 거부 |
| `tests/boundary/test_u_out_01.py` | U-OUT-01 / FR-02 | `meter:2.5` 줄 단위 출력 |
| `tests/boundary/test_u_out_02.py` | U-OUT-02 / EXT-03 | JSON 출력 |
| `tests/boundary/test_u_out_04.py` | U-OUT-04 / EXT-03 | table 출력 |

참고: U-OUT-03(CSV)은 `green`에만 추가(GREEN 전용 번들).

## `red`에 **없는** 것

- `src/entity/converter.py`, `unit_registry.py`, `constants.py` 없음
- `src/boundary/input_parser.py`, `output_formatter.py` 없음
- `src/infrastructure/config_loader.py` 없음
- `tests/golden/` 골든 마스터 베이스라인 없음

## 브랜치 맵

```text
spec  → 요구사항·하네스
red   → 현재 위치 (실패 테스트 11개, 스텁만)
green → 최소 구현 (통과 테스트 15개)
refactor → Cycle 1 구조 정리
```

## 빌더 워크플로

1. RED 번들 하나 선택 (`red`에서 테스트 파일 1개 = 커밋 1개).
2. `green` 체크아웃 후 해당 테스트를 통과하는 **최소** 코드 구현.
3. `green`에 `green: minimal … for <ID>` 형식으로 커밋.
4. `red`의 테스트는 수정하지 않음 — 테스트가 명세입니다.

참고: `guide/06_dualtrack-red-design.ko.md`, `WORK_PLAN.ko.md` 5–8절.

## 프로젝트 문서

- 요구사항: `docs/PRD.ko.md`
- 추적 매트릭스: `guide/02_traceability-matrix.ko.md`
- 목표 모듈: `guide/04_target-architecture.ko.md`
- 에이전트 진입: `AGENTS.ko.md`

## 레거시 참고

`UnitConverter.py`는 리팩터 전 시드로 유지; 새 코드는 if/elif 구조를 복사하지 않습니다.

## 다음 단계

전체 통과 스택 검토 시 `green`에서 merge/rebase, 또는 `WORK_PLAN.ko.md`에 따라 RED→GREEN 사이클 계속.
