# 01. PRD 요약 — 무엇을 만드는가

English version: [01_prd-summary.md](01_prd-summary.md). 출처: `goinfre/01`.

길이 단위 변환 CLI를 PRD에서 테스트까지 추적 가능하게 재구현한다.

## 문제

- 레거시 `UnitConverter.py`는 비율 하드코딩, 단위별 분기, 검증 누락.
- 목표: 동일 동작이되 확장 가능(OCP), 분리(SRP), 검증 포함.

## 핵심 요구

- 입력: `unit:value` 파싱 (예: `meter:2.5`).
- 기본 단위: meter, feet, yard.
- 비율: `1 m = 3.28084 ft = 1.09361 yd`. feet<->yard는 meter 경유 계산.
- 품질: OCP, SRP, 입력 검증 (음수, 잘못된 형식, 미지 단위).

## P1 확장

1. 설정 파일: `units.json` / YAML에서 비율 로드.
2. 동적 등록: `1 cubit = 0.4572 meter` 등록 후 즉시 변환.
3. 출력 포맷: `--format json | csv | table`.

## 예상 출력

```text
$ python -m unit_converter "meter:2.5"
2.5 meter = 8.2021 feet
2.5 meter = 2.7340 yard
...
```

## 인수 예시

| 입력 | 기대 |
|------|------|
| `meter:2.5` | meter 2.5, feet ~8.2021, yard ~2.7340 |
| `feet:1` | meter 0.3048 (비율 경유) |
| `cubit:1` (미등록) | 명확한 미지 단위 오류 |
| `meter:-1` | 거부 (음수) |
| `meter` / `abc` | 형식 오류 |

## 다음

- 각 요구를 테스트 ID에 고정: [02 추적표](02_traceability-matrix.ko.md).
- 이 설계가 제거하는 스멜: [03 레거시 시드 분석](03_legacy-seed-analysis.ko.md).
