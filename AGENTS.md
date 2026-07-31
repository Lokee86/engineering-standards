# AGENTS.md

This repository owns shared engineering standards and their deterministic compliance tooling.

## Documentation work

Read these before changing the documentation standard or checker:

- `docs/documentation-standard.md`
- `docs/documentation-procedure.md`
- `docs/profiles.md`
- `docs/change-impact.md`
- `docs/completeness.md`
- `docs/adoption.md`

## Architecture work

Read these before changing the architectural standard:

- `docs/architecture/architecture-standard.md`
- `docs/architecture/ownership-and-dependency.md`
- `docs/architecture/seams-and-abstractions.md`
- `docs/architecture/state-lifecycle-and-concurrency.md`
- `docs/architecture/data-processes-and-protocols.md`
- `docs/architecture/resilience-observability-and-operations.md`
- `docs/architecture/repository-and-component-structure.md`
- `docs/architecture/testing-evolution-and-decisions.md`
- `docs/architecture/architecture-procedure.md`

## Rules

- Documentation is part of implementation, not optional follow-up work.
- Preserve the distinction between current behavior, plans, research, limits, and agent guidance.
- Keep repository profiles concrete; do not force game-specific or CLI-specific taxonomy on every project.
- Prefer one canonical owner for each fact and link across document types instead of duplicating prose.
- Architectural standards define ownership and judgment; repository-specific architecture remains in the owning repository.
- Prefer useful concrete seams early, but do not create vague abstraction layers without a real responsibility or invariant.
- Defer mechanics, not ownership.
- Keep state, lifecycle, concurrency, failure, recovery, and observability ownership explicit.
- Do not add or propagate cross-repository architecture enforcement unless the user explicitly approves a rollout.
- Keep the documentation checker deterministic, dependency-free, and safe to run in CI.
- Add or update tests when checker behavior changes.
- Do not claim a repository is documented, architecturally compliant, or otherwise compliant without the appropriate evidence and disclosed gaps.

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

Architectural-standard changes must also include:

```text
Architecture impact:
- Standards added or changed:
- Ownership or boundary impact:
- Enforcement impact:
- Known architectural gaps:
```
