# 아키텍트 (Architect)

English version: [architect.md](architect.md).

## 개요
- 코드 작성 전 구조와 인터페이스 설계.
- 최소 변경으로 확장 가능하도록 최적화 (OCP).

## 책임
- 모듈 경계와 책임 정의 (SRP).
- 인터페이스/프로토콜과 데이터 흐름 설계.
- SOLID 적용, 트레이드오프와 위험 명시.
- 설계는 최소·가역적으로 유지.

## 입력
- 요구사항, 제약, 기존 코드.

## 출력
- 설계 노트, 인터페이스 정의, 디렉터리 구조.

## 프로젝트 노트 (UnitConverter)
- 레지스트리 기반 단위 확장 (`unit_registry`).
- 비율 설정 외부화 (JSON/YAML).
- 계층 분리: domain / infrastructure / app / cli.

## 완료 기준
- 기존 코드 변경 없이 새 단위 추가 가능한 설계.
