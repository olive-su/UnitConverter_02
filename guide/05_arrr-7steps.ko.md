# 05. ARRR 7단계 — 방법론

English version: [05_arrr-7steps.md](05_arrr-7steps.md). 출처: `goinfre/05`, 베스트 프랙티스로 보강.

빌드 방식: 짧은 TDD 사이클을 7단계 계획과 브랜치 전략에 매핑.

## TDD 사이클

- RED: 테스트 먼저, 실패 확인.
- GREEN: 통과하는 최소 구현.
- REFACTOR: 계약 불변으로 안전하게 구조 개선.

## 7단계

1. 주제: 길이 변환을 테스트 가능한 모듈로.
2. R-G-I-O: Role=개발자, Goal=개념에서 코드로, Input=`unit:val`, Output=전 단위.
3. Ask: `test_converter.py` RED 스켈레톤 작성.
4. Respond: Registry + Converter 최소 구현 (GREEN).
5. Refine: Parser / Formatter 분리, 골든 마스터 추가.
6. Repeat: 새 요구를 1개씩 새 RED 묶음으로 추가.
7. 확장: 동적 단위 등록 + 출력 3포맷.

## ARRR 매핑

| ARRR | 활동 | 모드 |
|------|------|------|
| A — Ask | RED 설계 + 스켈레톤 | Ask -> Agent |
| R — Respond | GREEN + 골든 | Agent |
| R — Refine | REFACTOR | Ask -> Agent |
| R — Repeat | 문서화 + 익스포트 | Agent |

## 브랜치 전략 (MagicSquare_1004 기반)

```text
main -> spec -> red -> green -> refactor -> (사이클 반복) -> new_features
```

| 브랜치 | ARRR | 수정 범위 |
|--------|------|-----------|
| `spec` | 준비 | docs, `.cursor/`, 하네스, `Report/`, `Prompting/` |
| `red` | Ask=RED | `tests/`만 |
| `green` | Respond | `src/` + 해당 tests |
| `refactor` | Refine | 구조만 (계약 불변) |

## 베스트 프랙티스

- 1 RED 묶음 = 1 커밋; 한 커밋에 RED와 GREEN 혼합 금지.
- 테스트는 동작 중심; 구현 세부가 아닌 계약을 단언.
- 안정적 직렬화 출력에 골든 마스터 사용; 갱신은 의도적으로, 조용히 금지.
- 삼각측량: 일반화를 강제하는 케이스 추가 (예: feet->yard meter 경유).
- 도메인을 순수·무의존으로 유지해 테스트에 목이 필요 없게.

## 참고

- Kent Beck, "Test-Driven Development: By Example".
- Martin Fowler, "Refactoring" — 스멜 카탈로그와 안전한 단계.
- Rob Fitzpatrick, "The Mom Test" — 진짜 문제 검증.
- Approval Tests / Golden Master — `approvaltests.com`.

## 다음

- 최초 실패 테스트 작성: [06 Dual-Track RED 설계](06_dualtrack-red-design.ko.md).
