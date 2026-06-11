# UnitConverter_02

English version: [README.md](README.md).

ARRR / Dual-Track TDD로 재구현한 추적 가능한 길이 단위 CLI. 단일 `단위:값` 입력을 **meter SSOT(단일 진실 공급원)** 기준으로 등록된 모든 단위로 변환합니다.

| 항목 | 값 |
|------|-----|
| 브랜치 | `main` (안정 배포) |
| 원격 | [olive-su/UnitConverter_02](https://github.com/olive-su/UnitConverter_02) |
| Python | 3.11+ |
| 상태 | Cycle 1–4 완료 — **테스트 15개 통과** |

---

## 개요

학생·개발자가 길이 값 하나(예: `meter:2.5`)를 입력하면 **meter, feet, yard** 및 동적 등록 단위로 일관되게 변환합니다. 레거시 단일 파일 `UnitConverter.py`는 참고용으로만 유지하며, 실행 로직은 `src/`에 있습니다.

**변환 비율 (meter 허브):**

- `1 meter = 3.28084 feet`
- `1 meter = 1.09361 yard`
- feet ↔ yard는 항상 meter 경유 (직접 비율 없음)

## 빠른 시작

```bash
# 저장소 클론
git clone https://github.com/olive-su/UnitConverter_02.git
cd UnitConverter_02

# 가상환경 (권장)
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # macOS / Linux

# 개발 의존성 포함 설치
pip install -e ".[dev]"

# 전체 테스트
python -m pytest -q
# 기대: 15 passed
```

## 기능

| 영역 | 기능 | 추적 ID |
|------|------|---------|
| 파싱 | `unit:value` 형식, 빈/잘못된/음수 입력 거부 | FR-01, FR-04, FR-05 / U-IN-* |
| 변환 | meter SSOT로 한 입력 → 전 단위 | FR-02 / D-CNV-* |
| 오류 | 알 수 없는 단위 처리 | FR-03 |
| 설정 | JSON 파일에서 비율 로드 | EXT-01 / D-CFG-01 |
| 레지스트리 | 런타임 사용자 단위 등록 (예: cubit) | EXT-02 / D-REG-01 |
| 출력 | `lines`, `json`, `csv`, `table` | EXT-03 / U-OUT-* |
| 품질 | OCP 레지스트리; SRP 모듈 분리 | NFR-01, NFR-02 |

## 아키텍처

`guide/04_target-architecture.ko.md` 레이어 구조:

```text
src/
├── entity/
│   ├── constants.py      # UNIT_TO_METER / METER_TO_UNIT 맵 (리팩터)
│   ├── converter.py      # to_meter, convert_all
│   └── unit_registry.py  # 동적 단위 등록
├── boundary/
│   ├── input_parser.py   # 입력 파싱·검증
│   └── output_formatter.py
└── infrastructure/
    └── config_loader.py  # 외부 JSON 비율

tests/
├── entity/               # 도메인 테스트 (5)
├── boundary/             # 파서·포매터 테스트 (7)
└── golden/cycle1_track_b/  # 회귀 베이스라인 (3)
```

**설계 원칙:**

- **SRP** — 파서, 변환기, 레지스트리, 포매터, 설정 로더 분리.
- **OCP** — converter 분기 수정 없이 레지스트리·설정으로 단위 확장.
- **추적성** — 모든 테스트는 `guide/02_traceability-matrix.ko.md` 요구 ID 인용.

## 사용 예

### 라이브러리

```python
from src.boundary.input_parser import parse_input
from src.entity.converter import convert_all
from src.boundary.output_formatter import format_output

unit, value = parse_input("meter:2.5")
result = convert_all(unit, value)
print(format_output(result, output_format="lines"))
print(format_output(result, output_format="json"))
```

### 설정 파일

샘플 비율: 저장소 루트 `units.json`. `src/infrastructure/config_loader.py`로 로드 (`tests/entity/test_d_cfg_01.py` 참고).

### 레거시 CLI (참고)

```bash
python UnitConverter.py
```

리팩터 전 시드 — 목표 아키텍처 아님. 신규 작업은 `src/` 모듈 사용.

## 테스트 스위트

| 계층 | 테스트 | 목적 |
|------|--------|------|
| Entity | 5 | 변환, 레지스트리, 설정 |
| Boundary | 7 | 입력 검증, 출력 포맷 |
| Golden | 3 | Cycle 1 Track B JSON 회귀 |

```bash
python -m pytest -v              # 상세
python -m pytest tests/entity/   # 도메인만
python -m pytest tests/golden/   # golden master만
```

## 구축 방식 (ARRR)

Analyze → Red → Green → Refactor를 기능 브랜치에서 진행하고, 리뷰 후 `main`에 통합합니다.

| 단계 | 브랜치 | 산출물 |
|------|--------|--------|
| Spec | `spec` | PRD, 가이드, 하네스, 스캐폴딩 |
| Red | `red` | 실패 테스트 계약 (11번들) |
| Green | `green` | 최소 통과 구현 |
| Refactor | `refactor` | `constants.py` 맵 추출, 계약 불변 |

머지 경로 (가정): `spec` → `red` → `green` → `refactor` → **`main`**.

빌드 순서·추적 매트릭스: [WORK_PLAN.ko.md](WORK_PLAN.ko.md).

## 문서

| 문서 | 역할 |
|------|------|
| [docs/PRD.ko.md](docs/PRD.ko.md) | 제품 요구사항 |
| [docs/MASTER_PROMPT.ko.md](docs/MASTER_PROMPT.ko.md) | 에이전트 세션 진입 프롬프트 |
| [guide/00_Guide.ko.md](guide/00_Guide.ko.md) | 가이드 목차 |
| [AGENTS.ko.md](AGENTS.ko.md) | Cursor 하네스 계약 |
| [WORK_PLAN.ko.md](WORK_PLAN.ko.md) | SSOT 작업 계획 |

사람이 읽는 문서는 영문·한글 쌍(`name.md` + `name.ko.md`)으로 제공합니다.

## 프로젝트 레이아웃

```text
UnitConverter_02/
├── src/                 # 프로덕션 코드
├── tests/               # pytest + golden 베이스라인
├── docs/                # PRD, 마스터 프롬프트
├── guide/               # 아키텍처·ARRR 가이드
├── harness/             # 세션 로그, 에이전트 역할
├── Report/, Prompting/  # 단계 근거 export
├── .cursor/             # 규칙, 명령, 스킬
├── UnitConverter.py     # 레거시 시드 (참고)
├── units.json           # 샘플 설정
└── pyproject.toml
```

## 기여

1. [AGENTS.ko.md](AGENTS.ko.md)와 `harness/sessions/` 최신 세션 확인.
2. ARRR 준수: `red`에서 테스트, `green`에서 구현, `refactor`에서 구조 정리.
3. 커밋: 영문 [Conventional Commits](https://www.conventionalcommits.org/).
4. PR 전 `python -m pytest` 실행.
5. 동작·구조 변경 시 이중 언어 문서 갱신.

## 라이선스

강의/팀 교육용 프로젝트. 관리자 목록: `WORK_PLAN.ko.md` 9절.
