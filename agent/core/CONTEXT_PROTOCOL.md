---
generated: true
generator: opencat-research
projectId: gaudi2-practical-inference
objectiveId: gaudi2-practical-inference
acceptedRevision: 4
doNotEdit: true
---
# OpenCat Research v0.5 Context and project-pack protocol

A Run Context Pack is an immutable, content-addressed projection of one accepted corpus revision. The canonical public project repository is a complete shareable projection of that revision plus portable policy and submission protocol. Neither is a mutation surface.

## Tiers

- **Sticky:** identity, rules, Bauhaus policy, Objective, success criteria, schema version, deployment access mode, and actual publication revision.
- **Session:** operating model, epistemic/tool policy, the current Brief, and the top item in Direction.
- **On demand:** full Direction queue, referenced input questions, skill bodies, Sources, claims (evidence), and historical records.

## Invariants

- Required checked-in policy and skill files exist and are non-empty.
- Every generated file has a SHA-256 hash in `MANIFEST.json`.
- The pack digest derives from normalized file names and contents, not wall-clock time.
- Publication, corpus, or harness-policy change creates a new digest.
- Existing Runs remain pinned to their original digest, publication revision, and host-generated corpus snapshot.
- Every new Run pins its exact connector/tool profile and research-target scope (`sourceFocus`); later target or connector settings never rebase an existing Run.
- Loading verifies every hash.
- Generated Markdown is marked `doNotEdit`.
- Run-only prompts and corpus snapshots live outside content-addressed pack directories.
- Private provenance may exist in authenticated Run context but must never leak into public site projections.

## Canonical public project repository

- The default branch is an exact OpenCat-generated snapshot with one `MANIFEST.json`; every projected file is hashed and the complete tree is verified after publication.
- `corpus/corpus.json` is the sole machine-readable shareable accepted corpus. Context Markdown, portable policy, the Brief and derived Direction, public Sources, and Evidence derive from it.
- Private provenance identifiers and payloads, work logs, Runs, Events, Proposals, sessions, credentials, connector state, and run-only prompts never enter the public repository.
- Contributors do not edit generated content. They submit one schema-valid `submissions/<uuid>.json` artifact through the site or a fork pull request; OpenCat imports it into the work log and closes the pull request without merge.
- Only explicit owner Apply can authorize semantic change. OpenCat commits the accepted overlay first, then best-effort publishes that exact candidate repository revision; a failed publication is reported and never gates acceptance.
