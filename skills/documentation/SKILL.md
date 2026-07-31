# Documentation Skill

Use this skill when implementation, documentation ownership, public behavior, state, operations, planning, research, or limitations change.

## Workflow

1. Read `docs-standard.json` and the repository documentation policy.
2. Identify the changed responsibility, not merely the changed files.
3. Use the maintainer map to route the change when the canonical owner or implementation boundary is unclear.
4. Locate the canonical guide, reference, architecture, operations, design/domain, data/protocol, development, planning, research, limits, and agent owners that apply.
5. Update current documentation in the same change as implementation.
6. Update maintainer maps, indexes, links, implementation coverage, focused code maps, and behavioral contracts when affected.
7. Graduate implemented facts out of planning; retain research evidence without treating it as product reference.
8. Run the configured documentation checks.
9. Report documentation impact and known gaps explicitly.

## Constraints

- Do not create a new document when an existing canonical owner fits.
- Do not use the root README as the complete manual.
- Do not treat a maintainer map, code map, generated index, or coverage-table row as sufficient explanation.
- Do not turn a maintainer map into a file-by-file inventory; route by change intent and ownership.
- Do not leave current behavior owned only by planning or research.
- Do not claim complete, current, or compliant documentation without the required evidence.
