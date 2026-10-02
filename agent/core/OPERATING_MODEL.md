---
generated: true
generator: opencat-research
projectId: gaudi2-practical-inference
objectiveId: gaudi2-practical-inference
acceptedRevision: 4
doNotEdit: true
---
# OpenCat Research v0.5 Operating Model

The Research Host runs one loop:

1. pin the Objective, accepted corpus revision, Context Pack, thread context, authorized retrieval profile, and exact research-target scope;
2. inspect the pinned corpus, recent thread transcript, reusable retrieval handles, the Brief, and the top item in Direction;
3. choose the smallest call plan that can resolve that item’s evidence delta, batching corpus reads and avoiding overlapping discovery;
4. retrieve and fully read external candidates only when current or missing evidence is required;
5. apply the canonical epistemic policy to each candidate and its relationship to the pinned corpus;
6. capture the visible answer;
7. switch to the reconcile-only tool surface;
8. record `no_change` when nothing passes the retention threshold, `needs_input` when an honest bounded record is blocked, or one smallest coherent review-only mutation when candidates pass;
9. wait for explicit human review and Apply;
10. let public views, Direction, and future Runs derive from the new accepted revision.

The owner may also **Steer** — record a decision, retire a decision, or prioritize a question — which builds an owner-authored Proposal and applies it through the same Apply path without a model Run.

## Authority

The model may answer, compare, synthesize, identify missing inputs, and propose. It cannot alter the Objective, Steer, or publish. The host stamps private workspace provenance, validates the full resulting corpus, enforces one reconciliation per running Run, and applies only after owner action.

## Context

Every Run pins an immutable Context Pack, publication revision, corpus snapshot, tool/connector profile, and research-target scope (the project’s `sourceFocus` assignment). Connector definition and authorization use only that access snapshot. An active Run never rebases or gains scope from later changes to the project’s targets or connectors. Only one model execution is admitted globally so model execution and Apply cannot race.

The answer and reconciliation are separate RPC phases in one isolated OMP process. The answer phase exposes only read tools. The reconciliation phase exposes only `research_reconcile`.
