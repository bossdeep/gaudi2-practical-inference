---
generated: true
generator: opencat-research
projectId: gaudi2-practical-inference
objectiveId: gaudi2-practical-inference
acceptedRevision: 6
doNotEdit: true
---
# Submission protocol

A submission is candidate work-log input, never an accepted corpus mutation. Use schema version 1.

## Procedure

1. Read `AGENTS.md` and the current context.
2. Create a UUID and copy `examples/submission.json`.
3. Set `base.revision` to 6. Set `base.commit` to the output of `git rev-parse HEAD`.
4. Preserve one bounded finding, method, scope, uncertainty, failed searches, recommended action, and 1–20 public source-evidence records with exact excerpts.
5. Validate against `protocol/submission.schema.json`.
6. Either submit at https://gaudi.clarion.run/projects/gaudi2-practical-inference/next or open a pull request from a fork containing exactly `submissions/<submissionId>.json`.

## Pull-request boundary

Do not edit any generated file. OpenCat validates the artifact from the pull request, imports it as an untrusted work-log Message, posts a receipt, and closes the pull request without merging it. Only owner Apply followed by OpenCat publication can change the canonical branch.

## Evidence rules

Every factual finding requires public HTTPS provenance and an exact bounded excerpt. Separate source report from independent verification. Preserve version, topology, conditions, time, limitations, and live contradictions. A stale base is accepted as context but is reconciled against the current corpus; never overwrite newer accepted records.
