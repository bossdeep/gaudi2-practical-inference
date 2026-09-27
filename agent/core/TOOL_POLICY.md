---
generated: true
generator: opencat-research
projectId: gaudi2-practical-inference
objectiveId: gaudi2-practical-inference
acceptedRevision: 2
doNotEdit: true
---
# OpenCat Research v0.3 Tool Policy

The Research Host exposes two phase-specific tool surfaces in one isolated OMP Run. Each Run captures an immutable profile, connector inventory, and exact tool-name allowlist at admission.

## Answer phase

- `research_overview` — pinned Objective, State, What’s Next, counts, and publication revision.
- `research_search` — bounded search over pinned Entries and Sources, including work status.
- `research_read` — exact pinned State, What’s Next, Entry, Source, or Context Pack reads. Entry/Source batches retain valid records and report `missingIds` instead of failing the entire call.
- `web_search` / `web_read` — OMP public-web discovery followed by SSRF-protected HTTPS retrieval.
- `github_search` / `github_read` — unauthenticated public GitHub search and canonical public resource retrieval. These tools provide research evidence only; they cannot use the OpenCat GitHub App, identify or synchronize the private platform repository, mutate the canonical public project repository, clone, fetch, pull, commit, push, or deploy.
- `discord_search` / `discord_review` / `discord_read` — UI-only search, incremental channel review, and exact context reads through the dedicated authenticated profile, limited to the project allowlist.

The OpenCat GitHub App is a separate host control plane. App credentials and installation tokens never enter a Run. Contributor OAuth tokens are discarded after GitHub identity resolution; the trusted login and submission transport may be attached to an untrusted work-log Message as provenance. Repository publication and pull-request ingestion are host effects, never model tools.

All answer tools are read-only. External calls retain invocation and retrieval lineage. Corpus search results include typed `readRequest` values; copy them exactly because Entry and Source IDs occupy different namespaces. Search results are discovery only: read a candidate, then search/read the pinned corpus records needed to check novelty, duplication, and contradiction before relying on or reconciling it.

The efficient default is one overview, one token-ranked corpus search, one batched corpus read, and at most one focused discovery search per necessary external connector followed by exact reads. The overview exposes reusable retrieval handles from earlier Runs in the same thread; follow-ups should read those handles rather than rediscovering the same resource. Duplicate or overlapping searches, repeated overviews, and one-ID-at-a-time corpus reads waste calls without increasing evidence quality. Refinement is justified only when the first result set is materially ambiguous.

Discord access never uses private APIs, user tokens, direct messages, or unlisted servers/channels. The profile is checked on use, one process owns it at a time, and all Discord retrieval content remains owner-authenticated. Per-channel review checkpoints advance only after a complete interval; bounded partial scans retain a continuation and leave the complete cursor unchanged. Search history is never treated as channel-review coverage.

## Reconcile phase

- `research_reconcile` — records exactly one successful `no_change`, `needs_input`, or draft Proposal receipt.

The host resolves workspace anchors only from exact quotes in named user-role Messages in the same thread. It resolves public retrieved Sources only from fully read web/GitHub retrievals in the same Run; direct model-authored public Sources are rejected. It resolves Discord Sources only from an exact target-message quote in a `discord_read` context retrieval, then stamps private provenance. It validates the full resulting corpus, stores Proposal plus receipt atomically, and never publishes.

Reconciliation evaluates the strongest bounded proposition supported by each fully read candidate. It assesses provenance, support, verification, scope, uncertainty, relevance, novelty, and utility independently, then applies separate thresholds for Entry retention and State synthesis. A candidate that is goal-relevant, durably useful, novel or corrective, and Source-ready becomes the smallest coherent proposal at the evidence level it earns; retrieval alone does not force mutation, and independent verification is not required for honest `unverified` retention. The provider-compatible tool schema describes one conditional contract, and the host enforces it: `no_change` and `needs_input` cannot mutate; `proposal` requires impact fields and 1–20 operation-specific objects; `needs_input` requires a concrete requested input. Unused non-mutating metadata is ignored. `reason` is valid only for supersede/withdraw operations.

The model cannot alter the Objective. Apply remains an authenticated human action with whole-revision compare-and-swap. Apply durably stages one exact candidate revision, the isolated OpenCat GitHub App publishes and verifies that complete privacy-filtered project repository snapshot, and only then does the host commit the identical accepted overlay and mark the Proposal applied. Publication failure leaves the Proposal pending for exact retry. The model cannot initiate, shape, credential, or observe that write. Platform source commits, pull, build, and deployment remain separate explicit owner actions.

Never replace a failed validated path with shell, filesystem, SQL, ambient browser/network access, or other OMP capabilities.
