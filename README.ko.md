# UnitConverter_02

English version: [README.md](README.md).

| 항목 | 값 |
|------|-----|
| 브랜치 | `green` |
| 단계 | **Green** — 최소 구현, 범위 내 테스트 전부 통과 |
| 원격 | [olive-su/UnitConverter_02](https://github.com/olive-su/UnitConverter_02) |
| PR | [#6 green → main](https://github.com/olive-su/UnitConverter_02/pull/6) |
| 최신 커밋 | `c189a95` — U-OUT-04 table 출력 (Track A) |

---

## 이 브랜치의 역할

**Green** 브랜치: Cycle 1–4 RED 계약을 만족하는 최소 프로덕션 코드. **테스트 15개 통과** (entity 5, boundary 7, golden 3). 구조는 `guide/04_target-architecture.ko.md`의 SRP/OCP를 따릅니다.

## 빠른 시작

```bash
pip install -e ".[dev]"
python -m pytest -q
# 기대: 15 passed
```

## 구현 맵

### Entity (`src/entity/`)

| 모듈 | 추적 | 역할 |
|------|------|------|
| `converter.py` | D-CNV-01–03 / FR-02 | `to_meter`, `convert_all` (meter SSOT) |
| `unit_registry.py` | D-REG-01 / EXT-02 | 동적 단위 등록 |

### Infrastructure (`src/infrastructure/`)

| 모듈 | 추적 | 역할 |
|------|------|------|
| `config_loader.py` | D-CFG-01 / EXT-01 | JSON 비율 로드·오류 검증 |

### Boundary (`src/boundary/`)

| 모듈 | 추적 | 역할 |
|------|------|------|
| `input_parser.py` | U-IN-01–03 / FR-04–05 | `unit:value` 파싱·검증 |
| `output_formatter.py` | U-OUT-01–04 / FR-02, EXT-03 | `lines`, `json`, `csv`, `table` |

## 테스트 요약

| 영역 | 개수 | 파일 |
|------|------|------|
| Entity | 5 | `test_d_cnv_*`, `test_d_reg_01`, `test_d_cfg_01` |
| Boundary | 7 | `test_u_in_*`, `test_u_out_*` (U-OUT-03 csv 포함) |
| Golden | 3 | `test_golden_cycle1_track_b.py` + JSON 베이스라인 |

변환 비율 (meter 허브):

- `1 meter = 3.28084 feet`
- `1 meter = 1.09361 yard`

## 사이클 진행 (RED + GREEN 완료)

| 사이클 | 트랙 | 번들 |
|--------|------|------|
| 1 | B | D-CNV-01, D-CNV-02, D-CNV-03 + golden master |
| 2 | A | U-IN-01, U-IN-02, U-IN-03 |
| 3 | B | D-REG-01, D-CFG-01 |
| 4 | A | U-OUT-01, U-OUT-02, U-OUT-03, U-OUT-04 |

## 사용 예 (라이브러리)

```python
from src.entity.converter import convert_all
from src.boundary.output_formatter import format_output

result = convert_all("meter", 2.5)
print(format_output(result, output_format="json"))
```

## 브랜치 맵

```text
spec  → 요구사항
red   → 실패 테스트 11개 (src 없음)
green → 현재 위치 (15 통과, Cycle 1–4 전체)
refactor → Cycle 1 구조 정리 (부분; green 먼저 머지)
```

## 프로젝트 레이아웃

```text
src/
├── entity/converter.py, unit_registry.py
├── boundary/input_parser.py, output_formatter.py
└── infrastructure/config_loader.py
tests/
├── entity/, boundary/
└── golden/cycle1_track_b/
```

## 문서·워크플로

- 빌드 순서 SSOT: `WORK_PLAN.ko.md`
- 요구사항: `docs/PRD.ko.md`
- 에이전트 하네스: `AGENTS.ko.md`
- 리포트: `Report/` (단계 export)

## 다음 단계

- PR #6을 `main`에 머지
- 선택: `green` 머지 후 `refactor`에서 `/refactor-smell`
- 선택: golden master 범위 확대

## 레거시

`UnitConverter.py`는 원본 시드; 새 CLI는 `src/` 모듈 사용.
