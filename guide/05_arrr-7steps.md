# 05. ARRR 7 Steps — Methodology

Korean version: [05_arrr-7steps.ko.md](05_arrr-7steps.ko.md). Source: `goinfre/05`, enriched with best practices.

How we build: short TDD cycles mapped to a 7-step plan and a branch strategy.

## TDD Cycle

- RED: write the test first, confirm it fails.
- GREEN: minimal implementation that passes.
- REFACTOR: improve structure safely, contract unchanged.

## 7 Steps

1. Topic: make length conversion a testable module.
2. R-G-I-O: Role=developer, Goal=concept-to-code, Input=`unit:val`, Output=all units.
3. Ask: write `test_converter.py` RED skeleton.
4. Respond: minimal Registry + Converter (GREEN).
5. Refine: split Parser / Formatter, add Golden Master.
6. Repeat: add each new requirement as a new RED bundle.
7. Extend: dynamic unit registration + 3 output formats.

## ARRR Mapping

| ARRR | Activity | Mode |
|------|----------|------|
| A — Ask | RED design + skeleton | Ask -> Agent |
| R — Respond | GREEN + Golden | Agent |
| R — Refine | REFACTOR | Ask -> Agent |
| R — Repeat | document + export | Agent |

## Branch Strategy (from MagicSquare_1004)

```text
main -> spec -> red -> green -> refactor -> (repeat cycles) -> new_features
```

| Branch | ARRR | Edit scope |
|--------|------|------------|
| `spec` | prep | docs, `.cursor/`, harness, `Report/`, `Prompting/` |
| `red` | Ask=RED | `tests/` only |
| `green` | Respond | `src/` + matching tests |
| `refactor` | Refine | structure only (contract unchanged) |

## Best Practices

- One RED bundle = one commit; never mix RED and GREEN in a commit.
- Keep tests behavior-focused; assert on contract, not implementation details.
- Use Golden Master for stable serialized output; refresh deliberately, not silently.
- Triangulate: add cases that force generalization (e.g. feet->yard via meter).
- Keep the domain pure and dependency-free so tests need no mocks.

## References

- Kent Beck, "Test-Driven Development: By Example".
- Martin Fowler, "Refactoring" — smell catalog and safe steps.
- Rob Fitzpatrick, "The Mom Test" — validating the real problem.
- Approval Tests / Golden Master — `approvaltests.com`.

## Next

- Write the first failing tests: [06 Dual-Track RED Design](06_dualtrack-red-design.md).
