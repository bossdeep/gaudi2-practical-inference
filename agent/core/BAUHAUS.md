---
generated: true
generator: opencat-research
projectId: gaudi2-practical-inference
objectiveId: gaudi2-practical-inference
acceptedRevision: 2
doNotEdit: true
---
# OpenCat Research v0.3 Bauhaus Policy

Bauhaus means the smallest honest shape with one owner for each decision.

The system has three durable domains:

1. **Work log** — Threads, Messages, Runs, and Events.
2. **Corpus** — Objective, Sources, Entries, and compact State.
3. **Proposal/revision boundary** — the only path from work into accepted corpus.

A Message is already raw contribution. A Run is already its processing envelope. A ChangeProposal is already the normalized candidate change. Do not add Contribution, Candidate, Inbox, Actor, CapabilityOffer, ThreadBrief, generic Relationship, or Commit records without a proven consumer and distinct authority.

## Corpus primitives

The accepted corpus has exactly four primitives: Objective, Source, Entry, and State. Evidence is Source provenance plus an Entry citation and calibrated evidence level. A Question or Need is an Entry, not another domain.

What’s Next is the primary work surface and a fresh projection, not a durable Inbox. Derive it from active unresolved Question Entries with work metadata. Derive Inputs needed from those Questions’ active `need` Entry references.

## Composition

- Derive public Evidence, Sources, What’s Next, and Inputs needed directly from accepted corpus records.
- Keep only interpretive salience in State: TLDR, blocker, next action, Known, and Uncertain.
- Human UI, hosted OMP, external agents, CLI, and future clients converge on the same validated Proposal and Apply commands.
- Keep the Research Host authoritative and clients thin.
- Prefer fresh bounded projection over cache invalidation while the corpus remains small.
- Preserve one active Run and one successful reconciliation per Run.

## Participation and access

- Design for crowd contribution: expose ranked work, definition of done, next action, required inputs, and an agent-ready brief.
- Preserve identical corpus and proposal semantics in public, gated, and private deployments.
- Keep deployment access separate from Source visibility. A permissive deployment never makes private provenance public.
- Contributor credentials and model entitlements remain with the contributor.

## Entropy control

Before adding a stage, table, service, queue, cache, or taxonomy, require evidence that it owns later-only information or a distinct decision. Otherwise consolidate it into Work log, Corpus, or Proposal/revision.
