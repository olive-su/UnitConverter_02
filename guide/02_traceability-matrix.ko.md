# 02. 추적표 — PRD에서 테스트로

English version: [02_traceability-matrix.md](02_traceability-matrix.md). 출처: `goinfre/02`.

모든 FR / NFR / EXT를 테스트 ID에 1:1로 매핑한다 — 개념(PRD)에서 코드(테스트)까지 추적 가능하게.

## 규칙

- 구현하는 모든 테스트는 아래 ID 하나를 정확히 인용한다.
- Track A = UI / 경계. Track B = 도메인 / 로직.

## 매트릭스

| ID | 요구 | Given | Then | Track | 대상 모듈 | P |
|----|------|-------|------|-------|-----------|---|
| FR-01 | `meter:2.5` 파싱 | 유효 문자열 | value=2.5, unit=meter | A/B | `app/input_parser.py` | P0 |
| FR-02 | 전 단위 출력 | meter 2.5 | feet~8.2021, yard~2.7340 | B | `domain/converter.py` | P0 |
| FR-03 | 미지 단위 | `cubit:1` (미등록) | 명확한 오류 | A/B | `domain/unit_registry.py` | P0 |
| FR-04 | 음수 | `meter:-1` | 거부 / 예외 | A | `app/input_parser.py` | P0 |
| FR-05 | 잘못된 형식 | `meter` / `abc` | 형식 오류 | A | `app/input_parser.py` | P0 |
| NFR-01 | OCP | `inch` 추가 | 변환기 코드 비수정 | B | `domain/unit_registry.py` | P0 |
| NFR-02 | SRP | - | Parser / Registry / Converter / Formatter 분리 | - | 패키지 구조 | P0 |
| EXT-01 | 설정 파일 | `units.json` | 비율 로드 | B | `infrastructure/config_loader.py` | P1 |
| EXT-02 | 동적 등록 | `1 cubit = 0.4572 m` | 즉시 변환 가능 | B | `domain/unit_registry.py` | P1 |
| EXT-03 | 출력 포맷 | `--format` | json / csv / table 검증 | A | `app/output_formatter.py` | P1 |

## 비고

- Track·대상 모듈 열은 원본 추적표에 더해 요구를 아키텍처에 연결한다 ([04 목표 아키텍처](04_target-architecture.ko.md)).
- RED 수준 테스트 ID(`D-*`, `U-*`)는 이로부터 도출되며 [06 Dual-Track RED 설계](06_dualtrack-red-design.ko.md)에서 설계한다.

## 다음

- 최초 실패 테스트 설계: [06 Dual-Track RED 설계](06_dualtrack-red-design.ko.md).
