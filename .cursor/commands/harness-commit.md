# /harness-commit

Create a clean-code commit following the commit policy.

## Steps
1. Run tests and linter; stop on failure.
2. Review the diff for single responsibility and clean code.
3. Stage only related files; split unrelated changes.
4. Write an English Conventional Commit message (`type: subject`).
5. Commit locally. Do not push unless the user confirms.

## Reference
- `.cursor/rules/20-commit-policy.mdc`
- `harness/guides/commit-convention.md`
