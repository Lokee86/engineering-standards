# Architecture Standards

Parent index: [Engineering Standards](../INDEX.md)

## Purpose

This index is the entry point for shared architectural standards.

## Overview

These standards define how responsibilities, dependencies, state, seams, processes, failure handling, repository structure, and architectural evolution should be designed and reviewed across Laughing Skull projects.

They are currently normative design guidance. They are not yet an automatically enforced cross-repository compliance profile.

## Direct files

- [Architecture standard](architecture-standard.md) — Core architectural rules and the minimum evidence required for a sound design.
- [Ownership and dependency direction](ownership-and-dependency.md) — Responsibility ownership, non-ownership, public boundaries, and dependency flow.
- [Seams and abstractions](seams-and-abstractions.md) — When to add seams, packages, interfaces, helpers, wrappers, and extension boundaries.
- [State, lifecycle, and concurrency](state-lifecycle-and-concurrency.md) — State ownership, transitions, mutation, scheduling, shutdown, and recovery.
- [Data, processes, and protocols](data-processes-and-protocols.md) — Sources of truth, generated state, process boundaries, contracts, compatibility, and migration.
- [Resilience, observability, and operations](resilience-observability-and-operations.md) — Failure behavior, diagnostics, health, recovery, and operational visibility.
- [Repository and component structure](repository-and-component-structure.md) — Package, service, application, monorepo, and independently usable component boundaries.
- [Testing, evolution, and decisions](testing-evolution-and-decisions.md) — Architectural invariants, contract tests, migrations, ADRs, exceptions, and debt.
- [Architecture procedure](architecture-procedure.md) — Required reasoning and review workflow for architectural changes.

## Related docs

- [Engineering Standards Maintainer Map](../maintainer-map.md)
- [Documentation standard](../documentation-standard.md)
- [Documentation procedure](../documentation-procedure.md)

## Notes

Repository-specific architecture remains owned by each repository. These documents define how that architecture is judged, not what every product must contain.
