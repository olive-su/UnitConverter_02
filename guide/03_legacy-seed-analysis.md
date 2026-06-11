# 03. Legacy Seed Analysis — What Is Wrong

Korean version: [03_legacy-seed-analysis.ko.md](03_legacy-seed-analysis.ko.md). Source: `goinfre/03`.

Diagnose the 37-line seed so the redesign targets concrete smells, not vague "clean code".

## Seed (`UnitConverter.py`)

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
        ...        # one branch per unit
    # hardcoded ratios, no validation, prints directly
```

## Smells and Resolutions

| Smell | Why it hurts | Motivates | Resolved by |
|-------|--------------|-----------|-------------|
| if/elif per unit | OCP violation — adding a unit edits `main()` | NFR-01 | `domain/unit_registry.py` (register + lookup) |
| Hardcoded ratio `3.28084` | Config cannot be externalized | EXT-01 | `infrastructure/config_loader.py` |
| Parse + convert + print in `main()` | SRP violation — untestable | NFR-02 | Parser / Registry / Converter / Formatter split |
| No negative / format checks | Invalid input passes silently | FR-04, FR-05 | `app/input_parser.py` validation |
| `split(':', 1)` alone | `meter:2.5:extra` boundary not handled | FR-01, FR-05 | parser with explicit boundary checks |
| `print` inside logic | Output coupled to logic | EXT-03 | `app/output_formatter.py` |

## Takeaway

- Each smell maps to a requirement ([02 Traceability Matrix](02_traceability-matrix.md)) and a target module ([04 Target Architecture](04_target-architecture.md)).
- RED tests fill the validation gaps before any implementation ([06 Dual-Track RED Design](06_dualtrack-red-design.md)).

## Next

- See the module layout that removes these smells: [04 Target Architecture](04_target-architecture.md).
