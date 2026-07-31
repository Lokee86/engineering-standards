# Laughing Skull Engineering Standards

This repository is the canonical source for shared engineering practices across Laughing Skull projects.

The governed standards currently cover documentation and architecture. Documentation standards define how repository knowledge is owned, structured, maintained, and verified. Architectural standards define how responsibility, state, dependencies, seams, processes, failure behavior, and evolution should be designed and reviewed.

## Documentation standards

- [Documentation standard](docs/documentation-standard.md)
- [Documentation procedure](docs/documentation-procedure.md)
- [Maintainer map](docs/maintainer-map.md)
- [Repository profiles](docs/profiles.md)
- [Change-impact rules](docs/change-impact.md)
- [Completeness and status claims](docs/completeness.md)
- [Adoption and enforcement](docs/adoption.md)

## Architecture standards

- [Architecture standards index](docs/architecture/INDEX.md)
- [Architecture standard](docs/architecture/architecture-standard.md)
- [Ownership and dependency direction](docs/architecture/ownership-and-dependency.md)
- [Seams and abstractions](docs/architecture/seams-and-abstractions.md)
- [State, lifecycle, and concurrency](docs/architecture/state-lifecycle-and-concurrency.md)
- [Data, processes, and protocols](docs/architecture/data-processes-and-protocols.md)
- [Resilience, observability, and operations](docs/architecture/resilience-observability-and-operations.md)
- [Repository and component structure](docs/architecture/repository-and-component-structure.md)
- [Testing, evolution, and decisions](docs/architecture/testing-evolution-and-decisions.md)
- [Architecture procedure](docs/architecture/architecture-procedure.md)

The architectural standard is currently normative design guidance only. It is not automatically propagated or enforced across adopted repositories.

## Documentation enforcement

Repositories adopt the documentation standard through `docs-standard.json`.

Run the shared checker from this repository:

```bash
python tools/docs_policy/check.py --repo /path/to/repository
```

For pull-request change-impact enforcement:

```bash
python tools/docs_policy/check.py --repo /path/to/repository --changed-from origin/main
```

For an explicitly tracked legacy rollout baseline:

```bash
python tools/docs_policy/check.py \
  --repo /path/to/repository \
  --write-baseline docs-standard.baseline.json
```

Demon Docs remains the preferred maintenance engine for indexes, links, frontmatter, moves, and managed documentation surfaces. Pitlord enforces repository-level required paths and required policy language through the reusable policies under `policies/pitlord/`.

## Authority

Repository-local policy may specialize shared standards, but it may not silently weaken an adopted standard. Exceptions must be explicit and documented in the repository that owns the affected architecture or documentation.
