# UnitConverter_02 — PRD (제품 요구사항 문서)

English version: [PRD.md](PRD.md).

| 항목 | 내용 |
|------|------|
| 프로젝트 | UnitConverter_02 |
| 버전 | 0.1 (Spec) |
| 생성일 | 2026-06-11 |
| 근거 | Mom Test — [Report/01.REPORT.md](../Report/01.REPORT.md), [Report/02.REPORT.md](../Report/02.REPORT.md), [Report/03.REPORT.md](../Report/03.REPORT.md) |
| 단계 | Spec — RED 구현 전 요구사항 |

---

## 1. 개요

### 1.1 배경

실습생·초급 개발자는 보고서·과제에서 **meter, feet, yard**를 동시에 맞춰야 한다. `3.28` 같은 **근사 비율**은 **전 단위 불일치**와 **10~20분** 재작업을 만든다.

**Mom Test 증거 (시뮬레이션 — [Report/02.REPORT.md](../Report/02.REPORT.md)):**

- **3.28** → **8.2** feet, 정답 **8.2021**
- feet·yard **각각 따로** 근사 계산
- 엑셀 **4~5회**, **약 12분**; 레거시 `UnitConverter.py` 신뢰 불가

### 1.2 진짜 문제

> `unit:value` **한 입력**으로 **전 단위**를 **meter SSOT 비율**로 일관 출력해야 할 때, **수동·근사·단위별 따로 계산**으로 일관성이 깨지고 **10~20분** 교정에 쓰이며, **검증 없는 레거시 코드**를 믿지 못한다.

### 1.3 이번 릴리스 목표 (P0)

- `unit:value` 파싱
- **등록된 전 단위** meter 기준 일관 변환 출력
- 음수·형식·미지 단위 **명시적 거부**
- **추적 가능한 테스트 루프** (Dual-Track TDD)

**의도적 보류:** P1 설정 파일·동적 등록·출력 포맷 — Mom Test: 일관성·신뢰 먼저.

### 1.4 주제 (1문장)

> **한 `unit:value` 입력으로 meter SSOT 비율로 전 길이 단위를 일관 변환하고, 잘못된 입력은 명확히 거부하는 CLI와 Dual-Track TDD 테스트 루프를 만든다.**

---

## 2. 사용자 및 시나리오

### 2.1 R-G-I-O

| | 내용 |
|---|---|
| **R** | `unit:value`로 전 단위를 맞춰야 하는 실습생·개발자 |
| **G** | **한 입력 → 전 단위 일관**; 잘못된 입력 → **명확 오류** |
| **I** | `unit:value` 문자열 |
| **O** | 전 단위 출력(기본 table) 또는 오류 메시지 |

### 2.2 페르소나

AI 실습 수업생 + 부품 스펙(m/ft) 정리 맥락. 도메인: meter, feet, yard; feet↔yard는 meter 경유.

### 2.3 핵심 시나리오

1. CLI에 `meter:2.5` 입력.
2. 파싱 → 레지스트리·변환기(meter 허브).
3. meter, feet, yard 출력.
4. `meter:-1`, `meter`, 미등록 `cubit:1` → 명확 오류.
5. 테스트로 성공·실패 재현 (RED→GREEN→REFACTOR).

---

## 3. 도메인 규칙

| 규칙 | 설명 |
|------|------|
| 입력 | `unit:value` |
| P0 단위 | meter, feet, yard |
| 비율 | `1m = 3.28084ft`, `1m = 1.09361yd` |
| 교차 변환 | feet↔yard **meter 경유** |

---

## 4. 기능 요구 (추적표)

| ID | 요구 | Given | Then | Track | 우선순위 |
|----|------|-------|------|-------|----------|
| FR-01 | 파싱 | `meter:2.5` | value=2.5, unit=meter | A/B | P0 |
| FR-02 | 전 단위 출력 | meter 2.5 | feet~8.2021, yard~2.7340 | B | P0 |
| FR-03 | 미지 단위 | `cubit:1` | 명확 오류 | A/B | P0 |
| FR-04 | 음수 | `meter:-1` | 거부 | A | P0 |
| FR-05 | 형식 오류 | `meter` | 형식 오류 | A | P0 |
| NFR-01 | OCP | 단위 추가 | 변환기 비수정 | B | P0 |
| NFR-02 | SRP | 구조 | Parser/Registry/Converter/Formatter 분리 | - | P0 |
| EXT-01 | 설정 파일 | `units.json` | 비율 로드 | B | P1 |
| EXT-02 | 동적 등록 | cubit | 변환 가능 | B | P1 |
| EXT-03 | 출력 포맷 | `--format` | json/csv/table | A | P1 |

출처: [guide/02_traceability-matrix.ko.md](../guide/02_traceability-matrix.ko.md). RED ID: [guide/06](../guide/06_dualtrack-red-design.ko.md).

---

## 5. 인수 예시

| 입력 | 기대 |
|------|------|
| `meter:2.5` | meter 2.5, feet ~8.2021, yard ~2.7340 |
| `feet:1` | meter ~0.3048 |
| `cubit:1` | 미지 단위 오류 |
| `meter:-1` | 거부 |
| `meter` | 형식 오류 |

---

## 6. 범위 밖 (P0) — Mom Test

| 제외 | 이유 |
|------|------|
| P1 확장 먼저 | 표면 솔루션 |
| 레거시 if/elif만 확장 | OCP/SRP 스멜 |
| 테스트 없는 설계만 | 추적성·신뢰 회복 불가 |

---

## 7. 아키텍처 (목표)

`src/entity/`, `src/boundary/`; `tests/entity/`, `tests/boundary/`; Golden Master. [guide/04](../guide/04_target-architecture.ko.md).

---

## 8. 성공 기준

| # | 기준 | 검증 |
|---|------|------|
| 1 | `meter:2.5` SSOT 비율 | pytest Track B |
| 2 | RED→GREEN 루프 | `pytest tests/ -v` |
| 3 | 잘못된 입력 명확 오류 | Track A |

---

## 9. 관련 문서

[Report/02](../Report/02.REPORT.md), [Report/03](../Report/03.REPORT.md), [WORK_PLAN.ko.md](../WORK_PLAN.ko.md), [MASTER_PROMPT.ko.md](MASTER_PROMPT.ko.md).

---

*PRD v0.1 — Spec. 구현은 `red` / `green` / `refactor` 브랜치 ARRR.*
