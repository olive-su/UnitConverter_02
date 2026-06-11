# 06. Dual-Track RED 설계

English version: [06_dualtrack-red-design.md](06_dualtrack-red-design.md). 출처: `goinfre/06`.

구현 이전에 두 트랙에서 최초 실패 테스트를 설계한다.

## Track A — UI / 경계

| Test ID | Given | Then (기대 RED) | 추적 | 경로 |
|---------|-------|-----------------|------|------|
| U-IN-01 | `""` (빈 입력) | 형식 오류 메시지 | FR-05 | `tests/boundary/test_u_in_01.py` |
| U-IN-02 | `meter` (콜론 없음) | 형식 오류 | FR-05 | `tests/boundary/test_u_in_02.py` |
| U-IN-03 | `meter:-1` | 음수 거부 | FR-04 | `tests/boundary/test_u_in_03.py` |
| U-OUT-01 | `meter:2.5` | 3줄 이상 출력 (스켈레톤) | FR-02 | `tests/boundary/test_u_out_01.py` |

## Track B — 도메인 / 로직

| Test ID | 함수 | Given / Then | 추적 | 경로 |
|---------|------|--------------|------|------|
| D-CNV-01 | `to_meter` | 1 feet -> 0.3048 m (+/- eps) | FR-02 | `tests/entity/test_d_cnv_01.py` |
| D-CNV-02 | `convert_all` | 2.5 m -> 8.20210 ft (5자리) | FR-02 | `tests/entity/test_d_cnv_02.py` |
| D-CNV-03 | `convert_all` | feet->yard, meter 경유 경로와 일치 | FR-02 | `tests/entity/test_d_cnv_03.py` |
| D-REG-01 | `register` | cubit 0.4572 -> 변환 가능 | EXT-02, NFR-01 | `tests/entity/test_d_reg_01.py` |
| D-CFG-01 | `load json` | 깨진 파일 -> ConfigError | EXT-01 | `tests/entity/test_d_cfg_01.py` |

## RED 규칙

- RED 단계에서 구현 코드 작성 금지.
- `pytest.fail("RED: ...")` 허용.
- `skip` / `xfail` 금지.
- 1 RED 묶음 = 1 커밋.

## 사용법

- 각 행은 추적 ID에 연결된다 ([02 추적표](02_traceability-matrix.ko.md)).
- Track B 테스트는 도메인 목 금지; Track A 테스트는 도메인 목 허용.
- 한 트랙의 RED 묶음이 실패하면 최소 GREEN을 구현한다 ([05 ARRR 7단계](05_arrr-7steps.ko.md)).

## 다음

- 인덱스로 복귀: [00 가이드](00_Guide.ko.md).
- [WORK_PLAN.ko.md](../WORK_PLAN.ko.md) Phase 1 / Phase 2에 따라 구현 시작.
