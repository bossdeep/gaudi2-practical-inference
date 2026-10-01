---
generated: true
generator: opencat-research
projectId: gaudi2-practical-inference
objectiveId: gaudi2-practical-inference
acceptedRevision: 3
doNotEdit: true
---
# OpenCat Research v0.5 Bauhaus Policy

Bauhaus means the smallest honest shape with one owner for each decision.

The system has three durable domains:

1. **Work log** — Threads, Messages, Runs, and Events.
2. **Corpus** — Objective, Sources, Entries, and the compact Brief.
3. **Proposal/revision boundary** — the only path from work into accepted corpus.

A Message is already raw contribution. A Run is already its processing envelope. A ChangeProposal is already the normalized candidate change. Do not add Contribution, Candidate, Inbox, Actor, CapabilityOffer, ThreadBrief, generic Relationship, or Commit records without a proven consumer and distinct authority.

## Corpus primitives

The accepted corpus has exactly four primitives: Objective, Source, Entry, and Brief. Evidence is Source provenance plus a claim citation and calibrated evidence level. An Entry is exactly one claim, question, or decision; an input is not a separate kind but a question referenced from another question's work plan.

A project’s research targets (the GitHub repositories and Discord channels it follows) and its connectors (the access mechanisms that retrieve from them) are owner configuration, not corpus and not a fifth domain. Retrieved or submitted material keeps its citation and provenance in the Work log; only one validated Proposal plus explicit owner Apply turns it into an accepted Source or Entry.

Direction is the primary work surface and a fresh projection, not a durable Inbox. Derive it from active unresolved question Entries with work metadata plus the active decision Entries. Input questions are the question Entries referenced by those work plans.

## Composition

- Derive public Evidence, Sources, Direction, and input questions directly from accepted corpus records.
- Keep only criterion progress in the Brief: each criterion's status, answer, and uncertainty. Direction is derived, never stored.
- Human UI, hosted OMP, external agents, CLI, and future clients converge on the same validated Proposal and Apply commands.
- Keep the Research Host authoritative and clients thin.
- Prefer fresh bounded projection over cache invalidation while the corpus remains small.
- Preserve one active model execution globally across Research Runs and transient project-creation turns, and one successful reconciliation per Run.

## Participation and access

- Design for crowd contribution: expose ranked work, definition of done, next action, required inputs, and an agent-ready brief.
- Preserve identical corpus and proposal semantics in public, gated, and private deployments.
- Keep deployment access separate from Source visibility. A permissive deployment never makes private provenance public.
- Contributor credentials and model entitlements remain with the contributor.

## Entropy control

Before adding a stage, table, service, queue, cache, or taxonomy, require evidence that it owns later-only information or a distinct decision. Otherwise consolidate it into Work log, Corpus, or Proposal/revision.
