# Laughing Skull Engineering Standards

This repository is the canonical source for shared engineering practices across Laughing Skull projects.

The first governed practice is documentation. It combines the ownership-focused taxonomy used by Space Rocks with the guide/reference/architecture/operations separation, coverage mapping, behavioral-contract discipline used by Demon Docs, and intent-driven maintainer maps proven in Grimoire.

## Documentation standard

- [Documentation index](docs/INDEX.md)
- [Documentation standard](docs/documentation-standard.md)
- [Documentation procedure](docs/documentation-procedure.md)
- [Maintainer map](docs/maintainer-map.md)
- [Repository profiles](docs/profiles.md)
- [Change-impact rules](docs/change-impact.md)
- [Completeness and status claims](docs/completeness.md)
- [Adoption and enforcement](docs/adoption.md)

## Enforcement

Repositories adopt the standard through `docs-standard.json`.

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

Repository-local policy may specialize the shared standard, but it may not silently weaken it. Every exception must be explicit in `docs-standard.json` and documented in the repository's documentation policy.
