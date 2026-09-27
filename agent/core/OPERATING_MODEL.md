---
generated: true
generator: opencat-research
projectId: gaudi2-practical-inference
objectiveId: gaudi2-practical-inference
acceptedRevision: 2
doNotEdit: true
---
# OpenCat Research v0.3 Operating Model

The Research Host runs one loop:

1. pin the Objective, accepted corpus revision, Context Pack, thread context, and authorized retrieval profile;
2. inspect the pinned corpus, recent thread transcript, reusable retrieval handles, and highest-priority relevant item in What’s Next;
3. choose the smallest call plan that can resolve that item’s evidence delta, batching corpus reads and avoiding overlapping discovery;
4. retrieve and fully read external candidates only when current or missing evidence is required;
5. apply the canonical epistemic policy to each candidate and its relationship to the pinned corpus;
6. capture the visible answer;
7. switch to the reconcile-only tool surface;
8. record `no_change` when nothing passes the retention threshold, `needs_input` when an honest bounded record is blocked, or one smallest coherent review-only mutation when candidates pass;
9. wait for explicit human review and Apply;
10. let public views, What’s Next, and future Runs derive from the new accepted revision.

## Authority

The model may answer, compare, synthesize, identify missing inputs, and propose. It cannot alter the Objective or publish. The host stamps private workspace provenance, validates the full resulting corpus, enforces one reconciliation per running Run, and applies only after owner action.

## Context

Every Run pins an immutable Context Pack, publication revision, and corpus snapshot. An active Run never rebases. Only one Run is admitted globally so model execution and Apply cannot race.

The answer and reconciliation are separate RPC phases in one isolated OMP process. The answer phase exposes only read tools. The reconciliation phase exposes only `research_reconcile`.
