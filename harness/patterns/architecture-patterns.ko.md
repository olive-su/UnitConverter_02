# 아키텍처 패턴 (Architecture Patterns)

English version: [architecture-patterns.md](architecture-patterns.md).

## 개요
- `revfactory/harness`의 6개 팀 패턴을 Cursor에 매핑.
- Cursor에는 Agent Teams 런타임이 없음. 서브에이전트(Task)로 위임.
- 작업에 맞는 가장 작은 패턴 선택.

## 패턴

### 파이프라인 (Pipeline)
- 용도: 순차·의존 단계.
- Cursor: 한 세션에서 순서대로 실행.
- 예: 분석, 설계, 구현, 테스트, 문서화.

### 팬아웃/팬인 (Fan-out / Fan-in)
- 용도: 독립·병렬 하위 작업.
- Cursor: 병렬 서브에이전트(Task) 실행 후 결과 취합.
- 예: 여러 모듈 동시 조사.

### 전문가 풀 (Expert Pool)
- 용도: 상황별 선택.
- Cursor: 상황에 맞는 역할 문서 적용.
- 예: 설계는 아키텍트, 코드는 빌더.

### 생산자-리뷰어 (Producer-Reviewer)
- 용도: 생성 + 품질 게이트.
- Cursor: 빌더 생산, 리뷰어 서브에이전트 검증.
- 예: 기능 구현 후 diff 리뷰.

### 슈퍼바이저 (Supervisor)
- 용도: 동적 작업 분배.
- Cursor: 오케스트레이터가 Task로 분할·배정.
- 예: 빌드와 테스트를 병렬 조율.

### 계층적 위임 (Hierarchical Delegation)
- 용도: 재귀적 분해가 필요한 큰 작업.
- Cursor: 서브에이전트가 하위 서브에이전트 생성(제한적 깊이).
- 예: 최상위 작업을 모듈 단위로 분할.

## 선택 가이드
- 작은 작업: 단일 오케스트레이션 세션 (파이프라인).
- 독립 부분: 팬아웃/팬인.
- 품질 중요: 생산자-리뷰어.
- 요소 많음: 슈퍼바이저 또는 계층적 위임.
