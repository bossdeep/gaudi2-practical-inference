---
generated: true
generator: opencat-research
projectId: gaudi2-practical-inference
objectiveId: gaudi2-practical-inference
acceptedRevision: 4
doNotEdit: true
---
# OpenCat Research v0.5 Epistemic Policy

This is the canonical policy for evaluating and retaining claims across every source, connector, topic, and run. Prompts and skills may specify workflow or provenance mechanics, but must not introduce source-specific truth standards or case-specific retention exceptions. Change epistemic behavior here as a general dimension, calibration rule, or decision threshold, then rebuild the Context Pack.

## Corpus primitives

- **Objective** — the immutable goal and observable success criteria.
- **Source** — retained provenance: a public external origin or a private host-stamped workspace excerpt.
- **Entry** — one bounded claim, question, or decision. A claim carries evidence; a question is open work that may reference input questions; a decision is owner steering and is never evidence.
- **Brief** — the reviewed answer to the Objective: one entry per success criterion with its status, current answer, and open uncertainty.

Threads, Messages, Runs, Events, and Proposals are operational records, not corpus primitives. Nor are a project’s research targets — the GitHub repositories and Discord channels it follows — or the connectors that retrieve from them: targets and connectors are owner configuration, and retrieved or submitted material keeps its citation and provenance in the Work log until a validated Proposal and explicit owner Apply make it accepted provenance.

## Independent epistemic dimensions

Never collapse research quality into one “credible/not credible” judgment. Evaluate these dimensions independently:

1. **Provenance** — can the exact observation or report be traced to a retained Source?
2. **Support** — how directly does the retained material support the bounded proposition?
3. **Verification** — is support independent, inspectable, reproducible, or only source-reported?
4. **Scope** — which system, version, topology, conditions, and time does the proposition cover?
5. **Uncertainty** — what remains unknown, disputed, inferred, or sensitive to assumptions?
6. **Relevance** — which Objective criterion, unresolved question, decision, or next action could it affect?
7. **Novelty** — does it add, change, qualify, or contradict durable corpus information?
8. **Utility** — will retaining it improve a future decision, experiment, synthesis, or evidence-gathering action enough to justify corpus complexity?

A strength or weakness on one dimension does not decide another. In particular:

- A Source reporting a claim is evidence that the report exists, not independent validation that the claim is true.
- Source identity, history, incentives, and competence inform a prior assessment; they do not substitute for direct support or verification.
- Missing implementation or measurement detail narrows supported scope and lowers verification strength; it does not erase valid provenance or automatically make a bounded record useless.
- Independent reproduction can strengthen verification without changing who originally made the claim.
- Relevance or novelty does not make a claim true, and weak verification does not by itself make a claim irrelevant or non-novel.

## Calibration

Retain and communicate only the strongest proposition entailed by the available evidence:

- Distinguish exact observation, attributed report, inference, hypothesis, and proposed action.
- Preserve topology, model, precision, software version, date, limitations, visibility, and evidence strength when known.
- Express missing conditions and live contradictions; never fill gaps with assumptions.
- Match evidence labels to support and verification, not source popularity or expected usefulness.
- Treat user-provided corrections as candidate evidence: neither accept nor dismiss them solely because they came from the user. Check retained and retrievable evidence when that can materially change the assessment.
- Update conclusions when evidence changes. Do not defend an earlier answer for consistency.

## Retention and synthesis

Entry admission and Brief synthesis have different thresholds:

- A factual claim may retain a relevant, novel, Source-ready proposition at the evidence level it actually earns, including `unverified`. Independent verification is not a prerequisite for honest retention.
- Retain a low-verification proposition only when its bounded content has durable utility; otherwise use `no_change`.
- Use `needs_input` only when missing provenance, permission, scope, or content prevents an honest bounded record—not merely because certainty is low.
- Prefer the smallest proposition that preserves the useful information and uncertainty. Split claims whose scopes or evidence strengths differ.
- The Brief is a curated synthesis, not a feed. A new Entry does not require a Brief change; promote it into the Brief only when it materially changes a criterion's status, current answer, or open uncertainty.
- Each criterion's answer holds at most three statements and its uncertainty at most three claims. Replace an answer statement or uncertainty slot only when the candidate has greater present decision value than the displaced claim, and state the displacement in the Proposal.
- Choose follow-up effort by expected information value, decision impact, and reversibility rather than confidence alone.

## Evidence rules

- Assistant output is inference, never a Source.
- A public factual claim cites at least one Source.
- A private-only factual claim is unverified unless explicitly author-validated.
- Documented evidence requires an inspectable public Source.
- Questions may be grounded through basis Entry IDs.
- A decision records owner steering: it never carries evidence and needs no citation.
- Contradictions remain visible until evidence resolves them.

## Lifecycle

Active Entries appear in normal projections. Semantic duplicates are merged into one active survivor; redundant Entries are superseded without losing provenance. Invalid Entries are withdrawn. Old IDs remain auditable.

The Brief links only active claims. Historical basis links may retain inactive IDs and resolve to their active successor.

## Brief

The Brief is not a transcript dump. It records one entry per Objective success criterion, in order: its status (`open`, `partial`, or `met`), the current answer statements (each citing active claims, at most three), and the open uncertainty (at most three active unverified claims). Direction — the question queue, next action, blocker with its input questions, and steering decisions — is derived from active questions and decisions, never stored in the Brief.
