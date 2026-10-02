---
generated: true
generator: opencat-research
projectId: gaudi2-practical-inference
objectiveId: gaudi2-practical-inference
acceptedRevision: 4
doNotEdit: true
---
---
name: evidence-review
description: Review an active or historical Entry against retained Sources, scope, contradictions, and lifecycle before reconciliation.
---

# Evidence Review

1. Express the candidate as the smallest bounded proposition the retained material directly supports.
2. Resolve exact public/private Sources, scope, date, and historical basis.
3. Assess provenance, support, verification, scope, uncertainty, relevance, novelty, and utility independently. Never use one as a proxy for another.
4. Search active Entries for support, contradiction, duplication, or narrower applicability. Copy typed corpus `readRequest` values exactly; never move IDs between Entry and Source namespaces.
5. Separate observation, attributed report, inference, hypothesis, and proposed action; preserve every material unknown.
6. Assign evidence no stronger than retained provenance and verification permit. Low verification may still support a useful, explicitly bounded Entry.
7. Apply the retention threshold independently from the Brief threshold: retain only durable useful information, and change the Brief only when a criterion's status, current answer, or open uncertainty materially changes.
8. Merge duplicates by preserving unique provenance and superseding the redundant Entry.
9. Withdraw invalid content; keep unresolved contradictions visible.
10. Finish with `no_change`, `needs_input`, or the smallest reviewable Proposal. Never Apply.
