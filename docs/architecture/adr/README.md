# Architecture Decision Records

This directory contains Architecture Decision Records (ADRs) for the TextCollector project.

## What are ADRs?

ADRs are documents that capture important architectural decisions made during the development of the project. Each ADR describes:

- The context and problem that led to the decision
- The decision itself
- The status of the decision
- The consequences of the decision

## ADR Format

Each ADR follows this format:

```
# ADR-NNNN: Title

## Status
[Proposed | Accepted | Deprecated | Superseded by ADR-XXXX]

## Context
[Description of the problem and context]

## Decision
[Description of the decision made]

## Consequences
[Description of the consequences of the decision]

## Alternatives Considered
[Description of alternatives that were considered]

## References
[Links to related resources]
```

## ADR Workflow

1. **Creation**: When a significant architectural decision is needed, create a new ADR
2. **Review**: Share the ADR for discussion and feedback
3. **Acceptance**: Once consensus is reached, update the status to "Accepted"
4. **Implementation**: Reference the ADR during implementation
5. **Evolution**: If a decision is later changed, create a new ADR and reference the old one

## ADR Index

- [ADR-0001: Metadata Schema Design](./adr-0001-metadata-schema-design.md) [Pending]