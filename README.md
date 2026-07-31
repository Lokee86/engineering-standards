# Laughing Skull Engineering Standards

This repository is the canonical source for shared engineering practices across Laughing Skull projects.

The governed standards cover documentation and architecture. Documentation standards define how repository knowledge is owned, structured, maintained, and verified. Architectural standards define how responsibility, state, dependencies, seams, processes, failure behavior, evolution, and deterministic enforcement should be designed.

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
- [Architectural enforcement with Pitlord](docs/architecture/enforcement.md)
- [Ownership and dependency direction](docs/architecture/ownership-and-dependency.md)
- [Seams and abstractions](docs/architecture/seams-and-abstractions.md)
- [State, lifecycle, and concurrency](docs/architecture/state-lifecycle-and-concurrency.md)
- [Data, processes, and protocols](docs/architecture/data-processes-and-protocols.md)
- [Resilience, observability, and operations](docs/architecture/resilience-observability-and-operations.md)
- [Repository and component structure](docs/architecture/repository-and-component-structure.md)
- [Testing, evolution, and decisions](docs/architecture/testing-evolution-and-decisions.md)
- [Architecture procedure](docs/architecture/architecture-procedure.md)

Pitlord is the expected deterministic architecture-enforcement mechanism. Repository-local policy defines actual ownership areas, dependency direction, forbidden coupling, and cycle rules. Focused tests and runtime scenarios retain behavioral, lifecycle, failure, recovery, and compatibility invariants that static evidence cannot prove.

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

Demon Docs remains the preferred maintenance engine for indexes, links, frontmatter, moves, and managed documentation surfaces. Pitlord enforces repository-level required paths and required policy language through reusable policies under `policies/pitlord/`.

## Architecture enforcement

Architecture-enforced repositories own a local `tools/pitlord/` policy and execution procedure. The expected gate validates policy, prepares current Lexicon and Arcana evidence, and runs Pitlord with a bounded timeout.

The reusable `policies/pitlord/architecture-core.json` policy establishes the required local enforcement surface. It does not replace repository-specific semantic rules; meaningful ownership areas and dependency invariants must be defined by the repository that owns the architecture.

Architecture rollout remains explicit per repository. This standard does not authorize automatic bulk policy propagation.

## Authority

Repository-local policy may specialize shared standards, but it may not silently weaken an adopted standard. Exceptions must be explicit and documented in the repository that owns the affected architecture or documentation.