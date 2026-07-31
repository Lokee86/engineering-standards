# Engineering Standards Maintainer Map

Parent index: [Engineering Standards](INDEX.md)

## Purpose

This document routes maintainers to the canonical documentation and implementation boundary for common changes to shared engineering standards.

## Overview

Use this map when the owning standard or enforcement surface is unclear. It is a navigation aid, not a replacement for normative standard pages, checker implementation, templates, or repository-local decisions.

## Change-area routing

| Change area | Canonical documentation | Primary implementation boundary | Verification |
| --- | --- | --- | --- |
| Documentation taxonomy, required shapes, and ownership rules | [Documentation standard](documentation-standard.md) | `docs/documentation-standard.md` | Shared checker self-check |
| Repository-type documentation requirements and capabilities | [Repository profiles](profiles.md) | `docs/profiles.md`, `templates/docs-standard.json` | Shared checker self-check |
| Documentation workflow and agent behavior | [Documentation procedure](documentation-procedure.md) | `docs/documentation-procedure.md`, `skills/documentation/SKILL.md`, `templates/AGENTS-documentation.md` | Shared checker self-check |
| Documentation change-impact rules | [Change-impact rules](change-impact.md) | `docs/change-impact.md`, repository `docs-standard.json` mappings | Changed-from checker tests |
| Documentation completeness claims and legacy baselines | [Completeness and status claims](completeness.md) | `tools/docs_policy/baseline.py`, `tools/docs_policy/check.py` | `tools/docs_policy/tests/` |
| Documentation required paths, indexes, links, and coverage | [Adoption and enforcement](adoption.md) | `tools/docs_policy/`, `policies/pitlord/documentation-core.json` | `tools/docs_policy/tests/` and self-check |
| Vendored documentation-standard snapshots | [Adoption and enforcement](adoption.md) | `tools/sync_checker.py` | Isolated sync and repository check |
| Architecture principles and minimum evidence | [Architecture standard](architecture/architecture-standard.md) | `docs/architecture/architecture-standard.md` | Standards self-check and architectural review |
| Responsibility ownership and dependency direction | [Ownership and dependency direction](architecture/ownership-and-dependency.md) | `docs/architecture/ownership-and-dependency.md` | Architectural review |
| Packages, seams, interfaces, helpers, and abstractions | [Seams and abstractions](architecture/seams-and-abstractions.md) | `docs/architecture/seams-and-abstractions.md` | Architectural review |
| Mutable state, lifecycle, concurrency, and shutdown | [State, lifecycle, and concurrency](architecture/state-lifecycle-and-concurrency.md) | `docs/architecture/state-lifecycle-and-concurrency.md` | Architectural review and focused tests |
| Persistence, generated state, processes, protocols, and migration | [Data, processes, and protocols](architecture/data-processes-and-protocols.md) | `docs/architecture/data-processes-and-protocols.md` | Contract and migration review |
| Failures, degradation, observability, health, and recovery | [Resilience, observability, and operations](architecture/resilience-observability-and-operations.md) | `docs/architecture/resilience-observability-and-operations.md` | Operational and failure review |
| Package, service, monorepo, and umbrella-product boundaries | [Repository and component structure](architecture/repository-and-component-structure.md) | `docs/architecture/repository-and-component-structure.md` | Architectural review |
| Invariant tests, ADRs, exceptions, and architectural debt | [Testing, evolution, and decisions](architecture/testing-evolution-and-decisions.md) | `docs/architecture/testing-evolution-and-decisions.md` | Test, decision, and migration evidence |
| Architecture design and review workflow | [Architecture procedure](architecture/architecture-procedure.md) | `docs/architecture/architecture-procedure.md` | Review checklist |

## Boundaries

- Normative rules belong in `docs/`; enforcement mechanics belong in `tools/` and `policies/`.
- Templates illustrate compliant repository-local surfaces but do not override normative documents.
- Vendored `.standards/` directories are generated snapshots and are not edited directly.
- Repository-local policies and ADRs may specialize shared standards only through explicit documented decisions.
- Architecture standards currently define review guidance only; no automatic cross-repository architecture enforcement is owned here yet.

## Related docs

- [Documentation standard](documentation-standard.md)
- [Architecture standard](architecture/architecture-standard.md)
- [Documentation procedure](documentation-procedure.md)
- [Architecture procedure](architecture/architecture-procedure.md)
- [Adoption and enforcement](adoption.md)

## Notes

Use this map to find the owner first. Use the owning standard, implementation, tests, or repository-specific ADR for the detailed contract.
