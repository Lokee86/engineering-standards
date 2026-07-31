# <Repository> Maintainer Map

Parent index: [<Documentation index>](../INDEX.md)

## Purpose

This document routes maintainers to the canonical documentation and primary implementation boundary for common changes in <repository>.

## Overview

Use this map when the owner of a change is unclear. It is not a repository inventory and does not replace focused architecture, reference, operations, development, or code-map sections.

## Change-area routing

| Change area | Canonical documentation | Primary implementation boundary | Verification |
| --- | --- | --- | --- |
| <Maintainer intent or subsystem> | [<Canonical owner>](<relative-link>) | `<implementation/root/>` | `<test or verification owner>` |

## Component maintainer maps

- Add links here when independently maintained components require their own maps.
- Remove this section when no component-local maps are needed.

## Boundaries

- State the most important ownership and non-ownership boundaries that prevent maintainers from choosing the wrong component.
- Keep detailed behavior in the canonical owning documents.

## Related docs

- [Documentation coverage](../development/documentation-coverage.md)
- Add the principal architecture or repository-layout owner.

## Notes

Route by change intent rather than reproducing the directory tree.
