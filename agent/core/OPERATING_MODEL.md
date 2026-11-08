---
generated: true
generator: opencat-research
projectId: gaudi2-practical-inference
objectiveId: gaudi2-practical-inference
acceptedRevision: 16
doNotEdit: true
---
# OpenCat Research v0.6 Operating Model

The Research Host runs one loop:

1. pin the Objective, accepted corpus revision, Context Pack, thread context, authorized retrieval profile, and exact research-target scope;
2. inspect the pinned corpus, recent thread transcript, reusable retrieval handles, the Brief, and the top item in Direction;
3. choose the smallest call plan that can resolve that item’s evidence delta, batching corpus reads and avoiding overlapping discovery;
4. retrieve and fully read external candidates only when current or missing evidence is required;
5. answer the owner’s actual question, reading this Run’s own thread history when the bounded transcript omits earlier discussion;
6. if — and only if — the turn warrants a change (a justified candidate or an explicit owner update request), call `research_request_reconciliation`; the host saves the answer first;
7. for a requested Run, switch to the reconcile-only tool surface and record `no_change`, `needs_input`, or one smallest coherent review-only mutation; an ordinary answer completes without this phase;
8. wait for explicit human review and Apply;
9. let public views, Direction, and future Runs derive from the new accepted revision.

The owner may also **Steer** — record a decision, retire a decision, or prioritize a question — which builds an owner-authored Proposal and applies it through the same Apply path without a model Run.

## Authority

The model may answer, compare, synthesize, identify missing inputs, and propose. It cannot alter the Objective, Steer, or publish. The host stamps private workspace provenance, validates the full resulting corpus, enforces at most one reconciliation per running Run, and applies only after owner action.

## Context

Every Run pins an immutable Context Pack, publication revision, corpus snapshot, tool/connector profile, and research-target scope (the project’s `sourceFocus` assignment). Connector definition and authorization use only that access snapshot. An active Run never rebases or gains scope from later changes to the project’s targets or connectors. Only one model execution is admitted globally so model execution and Apply cannot race.

The answer and reconciliation phases are separate RPC phases in one isolated OMP process. The answer phase exposes the pinned read tools plus one bounded control request (`research_request_reconciliation`), which changes no Run, corpus, or Proposal state. The reconciliation phase, reached only when the Run requested it, exposes only `research_reconcile`.
