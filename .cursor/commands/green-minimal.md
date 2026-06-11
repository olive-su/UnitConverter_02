# /green-minimal

ARRR Respond — minimal implementation to pass current RED.

## Trigger

User typed `/green-minimal` with **no extra text**. Do not ask follow-up questions.

## Preconditions

- Branch: `green`.
- Failing RED test(s) exist from prior `red` branch work.
- Read failing test file(s) and [docs/PRD.md](../../docs/PRD.md).

## Steps

1. Implement the **smallest** change under `src/` to make the targeted test(s) pass.
2. No extra features beyond the current RED bundle.
3. Run `python -m pytest` for affected tests — expect **PASS**.
4. Do not refactor structure beyond what GREEN requires.

## Prohibited

- Implementing future RED bundles
- Changing test assertions to force pass
- Skip/xfail

## Next

Suggest `/golden-master` if output is serialized; else next RED or `/refactor-smell`.
