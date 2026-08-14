# Architecture Audit: <repository or scope>

Date: YYYY-MM-DD
Auditor: <person or tool>
Revision: <commit, branch, or working-tree state>
Scope: <included and excluded repositories, components, or paths>
Standard revision: <engineering-standards revision>

## Result

Overall classification: Aligned | Minor gaps | Material gaps | Provisional | Not auditable

State whether files were changed. Identify incomplete evidence, active migrations, dirty working trees, unavailable repositories, or other limits that make the result provisional.

## Evidence reviewed

- Canonical architecture and operations documentation
- Maintainer map and behavioral-contract matrix
- ADRs, migrations, limits, and compatibility owners
- Pitlord policy and static evidence
- Focused tests, contract fixtures, CI, and release gates
- Repository layout, generated-state boundaries, and large ownership concentrations

## Findings

### Strengths

- <supported strength and evidence owner>

### Gaps

| Severity | Finding | Canonical owner | Evidence | Required remediation |
| --- | --- | --- | --- | --- |
| Critical | <finding> | <document or component> | <path, rule, or test> | <bounded action> |

## Remediation order

1. <highest-risk ownership, authority, generated-state, or recovery issue>
2. <next issue>

## Exclusions and unavailable evidence

| Scope | Reason | Effect on conclusion |
| --- | --- | --- |
| <scope> | <reason> | <effect> |

## Verification after remediation

- <Pitlord command or policy gate>
- <focused tests or contract fixtures>
- <documentation and link check>
- <working-tree and generated-state check>

## Decision and debt follow-up

List ADRs, explicit exceptions, migration exit criteria, or debt records that must be created or updated.
