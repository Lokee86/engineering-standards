# AGENTS.md

This repository owns shared engineering standards and their deterministic compliance tooling.

## Documentation work

Read these before changing the documentation standard or checker:

- `docs/documentation-standard.md`
- `docs/documentation-procedure.md`
- `docs/profiles.md`
- `docs/change-impact.md`
- `docs/completeness.md`

## Rules

- Documentation is part of implementation, not optional follow-up work.
- Preserve the distinction between current behavior, plans, research, limits, and agent guidance.
- Keep repository profiles concrete; do not force game-specific or CLI-specific taxonomy on every project.
- Prefer one canonical owner for each fact and link across document types instead of duplicating prose.
- Keep the checker deterministic, dependency-free, and safe to run in CI.
- Add or update tests when checker behavior changes.
- Do not claim a repository is documented or compliant unless the checker passes and known semantic gaps are disclosed.

## Completion report

Every implementation report must include:

```text
Documentation impact:
- Inspected:
- Updated:
- Not affected:
- Compliance check:
- Known documentation gaps:
```
