# 03. 레거시 시드 분석 — 무엇이 문제인가

English version: [03_legacy-seed-analysis.md](03_legacy-seed-analysis.md). 출처: `goinfre/03`.

37줄 시드를 진단해 재설계가 막연한 "클린 코드"가 아니라 구체적 스멜을 겨냥하게 한다.

## 시드 (`UnitConverter.py`)

```python
def main():
    s = input("...meter:2.5...")
    unit, value = s.split(':', 1)
    value = float(value)
    if unit == "meter":
        print(value * 3.28084)
    elif unit == "feet":
        print(value / 3.28084)
    elif unit == "yard":
        ...        # 단위마다 분기 증가
    # 하드코딩 비율, 검증 없음, print 직접 출력
```

## 스멜과 해소

| 스멜 | 왜 문제인가 | 동기 요구 | 해소 |
|------|-------------|-----------|------|
| 단위별 if/elif | OCP 위반 — 단위 추가 시 `main()` 수정 | NFR-01 | `domain/unit_registry.py` (등록 + 조회) |
| 비율 `3.28084` 하드코딩 | 설정 외부화 불가 | EXT-01 | `infrastructure/config_loader.py` |
| `main()`에 파싱+변환+출력 혼재 | SRP 위반 — 테스트 불가 | NFR-02 | Parser / Registry / Converter / Formatter 분리 |
| 음수/형식 검증 없음 | 잘못된 입력이 조용히 통과 | FR-04, FR-05 | `app/input_parser.py` 검증 |
| `split(':', 1)` 단독 | `meter:2.5:extra` 경계 미처리 | FR-01, FR-05 | 명시적 경계 검사 파서 |
| 로직 내부 `print` | 출력이 로직에 결합 | EXT-03 | `app/output_formatter.py` |

## 시사점

- 각 스멜은 요구([02 추적표](02_traceability-matrix.ko.md))와 대상 모듈([04 목표 아키텍처](04_target-architecture.ko.md))에 매핑된다.
- RED 테스트가 구현 이전에 검증 갭을 메운다 ([06 Dual-Track RED 설계](06_dualtrack-red-design.ko.md)).

## 다음

- 스멜을 제거하는 모듈 구조: [04 목표 아키텍처](04_target-architecture.ko.md).
