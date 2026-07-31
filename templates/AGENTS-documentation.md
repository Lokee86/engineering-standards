## Documentation

Documentation is part of the implementation.

Before completing a change:

1. Identify affected public contracts, ownership, flows, state, operations, invariants, and extension seams.
2. Update every affected canonical current document in the same change.
3. Keep implemented behavior, planning, research, limitations, and agent guidance separate.
4. Update implementation coverage and behavioral-contract mappings when ownership or invariants change.
5. Run the configured documentation compliance checks.
6. Never report documentation as complete or current unless the required checks and semantic review support that claim.

Completion reports include:

```text
Documentation impact:
- Inspected:
- Updated:
- Not affected:
- Compliance check:
- Known documentation gaps:
```
