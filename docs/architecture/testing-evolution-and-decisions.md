# Testing, Evolution, and Decisions

Parent index: [Architecture Standards](INDEX.md)

## Purpose

This document defines how architectural invariants are verified, how systems evolve, and how consequential decisions, exceptions, and debt are recorded.

## Overview

Architecture must survive implementation change. Tests and deterministic gates protect the contracts that must remain true; architectural decision records explain why consequential tradeoffs were accepted; migration plans control changes that cannot occur atomically.

## Architectural invariants

An architectural invariant is a property that must remain true across many local implementation changes.

Examples include:

- only one component mutates authoritative state;
- one dependency direction remains acyclic;
- a protocol response is deterministic for the same snapshot;
- publication is atomic from a reader's perspective;
- a cache cannot become the source of truth;
- adapters emit normalized facts but cannot publish snapshots;
- clients cannot bypass server authority;
- generated state is excluded from authored-source traversal.

Each critical invariant should have a focused protecting test, static rule, contract fixture, integration scenario, or release gate.

## Test layers

Use the narrowest test that can protect the invariant:

- unit tests for local validation and transition rules;
- package or component tests for ownership and lifecycle behavior;
- contract tests for independently evolving consumers and providers;
- persistence fixtures for format and migration compatibility;
- integration tests for process, storage, and failure boundaries;
- runtime scenarios for multi-component behavior and recovery;
- static or policy checks for dependency direction and forbidden coupling;
- release gates for packaging, installation, upgrade, and rollback.

End-to-end tests do not replace focused owner tests. Focused tests do not replace cross-boundary contract tests.

## Behavioral-contract mapping

Complex or stateful systems should maintain a behavioral-contract matrix mapping important invariants to:

```text
Canonical architecture owner
Implementation boundary
Protecting test or gate
Failure meaning
Release significance
Known coverage gap
```

The matrix is a navigation and assurance artifact. It does not replace the tests or architecture documents it links.

## Safe evolution

Architectural change should preserve a coherent system at each intermediate step.

Prefer:

- additive seams before caller migration;
- compatibility adapters with explicit removal criteria;
- immutable or generation-based publication;
- shadow reads or writes for bounded comparison;
- backfills with repeatable checkpoints;
- strangler replacement around one authoritative boundary;
- feature flags that preserve one owner rather than fork policy;
- measurable cutover criteria.

Avoid:

- indefinite dual writes;
- two active sources of truth;
- migration fallbacks with no removal owner;
- branching old and new policy in every caller;
- format changes without old-data fixtures;
- architecture rewrites that cannot be verified incrementally.

## Architectural decision records

Create an ADR when a decision is:

- difficult or expensive to reverse;
- cross-cutting across components or repositories;
- surprising to a future maintainer;
- a deliberate exception to a shared standard;
- a selection among materially different tradeoffs;
- a migration that temporarily violates the desired steady state;
- a public compatibility or persistence commitment.

A useful ADR contains:

```text
Title and status
Context and problem
Decision
Ownership and dependency consequences
State, lifecycle, failure, and operational consequences
Alternatives considered
Compatibility and migration impact
Verification and acceptance evidence
Known risks and debt
Superseding or removal conditions
```

An ADR records why. Canonical architecture documentation records what is currently true. When a decision ships, update both.

## Exceptions

An exception must be:

- explicit and narrow;
- owned by a named component or team;
- justified against the specific rule;
- bounded by scope and duration where possible;
- paired with compensating verification or operational controls;
- visible in current architecture or limits documentation;
- reviewed when surrounding assumptions change.

"Legacy," "temporary," and "faster" are not sufficient explanations without a concrete constraint and exit condition.

## Architectural debt

Architectural debt includes known ambiguous ownership, cycles, migration residue, missing recovery, unversioned contracts, duplicated policy, and abstractions that no longer match responsibility.

Debt should record:

```text
Current risk
Affected owner and consumers
Why it remains
What change would remove it
Blocking dependency
Detection or mitigation
Review trigger
```

Debt must not be hidden as an undocumented fallback or permanent TODO.

## Review evidence

Before accepting a significant architectural change, reviewers should see:

- the owner and non-owner boundaries;
- the before and after dependency direction;
- state and lifecycle flow;
- failure and recovery behavior;
- migration stages and authority;
- protecting tests or new gates;
- documentation impact;
- ADR or exception when required.

## Related docs

- [Architecture standard](architecture-standard.md)
- [Architecture procedure](architecture-procedure.md)
- [Data, processes, and protocols](data-processes-and-protocols.md)
- [Resilience, observability, and operations](resilience-observability-and-operations.md)

## Notes

A passing test suite is not proof of sound architecture, but architecture that cannot be protected by focused tests or deterministic evidence is too implicit.
