---
generated: true
generator: opencat-research
projectId: gaudi2-practical-inference
objectiveId: gaudi2-practical-inference
acceptedRevision: 2
doNotEdit: true
---
# Gaudi 2 practical inference

Accepted research state published by [OpenCat Research](https://gaudi.clarion.run). Revision **2** · generated 2026-09-26T16:52:33.255Z · [machine corpus](corpus/corpus.json) · [integrity manifest](MANIFEST.json).

## Objective

Make standalone Gaudi 2 hardware practical for high-performance LLM inference on ordinary Linux systems.

### Success criteria

- **Access:** A documented single-card PCIe-carrier configuration initializes cleanly and completes a fixed inference smoke workload.
- **Performance:** Pinned single-card workloads show repeatable TTFT, prefill, decode, capacity, correctness, and stability results with retained evidence.

## TLDR

- Gaudi 2 has a maintained vLLM plugin path and documented installation, but its validated model coverage is narrower than Gaudi 3.
- Single-card measurements show plausible performance headroom, but the available results remain source-reported rather than independently reproduced here.
- The strongest retained throughput evidence is largely TP2 or TP2×PP2 and must not be generalized to a standalone carrier card.
- OAM-to-PCIe operation is reported, while missing-UBB driver behavior, unwired scale-up links, and a complete repeatable host setup remain unresolved.

## Primary blocker

No retained standalone configuration joins carrier bring-up, pinned software, health checks, and a fixed inference baseline.

## Next action

Document one single-card configuration, then profile the same fixed workload so access and performance work share one baseline.

## Current priorities

- **P1 · blocked:** [What is the reproducible single-card OAM-to-PCIe bring-up path?](context/FRONTIER.md#question-direct-attach)
  - Next: Run and document one complete carrier-to-inference bring-up on a named host and software version.
- **P2 · ready:** [Where does warmed single-card decode time go: graph compilation, replay, host dispatch, or execution?](context/FRONTIER.md#question-graph-dispatch)
  - Next: Capture a warmed trace and compare ordinary submission with the largest supported replay region.
- **P3 · blocked:** [Why do long-context prefill and batching results diverge so widely?](context/FRONTIER.md#question-prefill-batching)
  - Next: Run the same prompt/concurrency sweep on one pinned stack and retain raw timings and configuration.
- **P4 · ready:** [Which quantization and model formats reliably execute on Gaudi 2 today?](context/FRONTIER.md#question-quant-model)
  - Next: Select representative BF16, FP8, and INT4 checkpoints and record load, correctness, memory, and throughput outcomes.
- **P5 · ready:** [Which multi-card optimizations transfer to standalone single-card inference?](context/FRONTIER.md#question-topology-transfer)
  - Next: Re-run one kernel/runtime optimization on TP1 and compare against its multi-card baseline.

## Known

- [Gaudi 2 hardware architecture and headline specifications](context/EVIDENCE.md#gaudi2-arch-specs)
- [Source installation is pin-locked to a validated upstream vLLM commit](context/EVIDENCE.md#install-pinned-source-build)
- [Compatibility matrix pins one plugin release to one vLLM version and one Gaudi software version](context/EVIDENCE.md#version-compatibility-matrix)

## Uncertain

- [~3000 tok/s prefill on 4 Gaudi 2 (TP2xPP2) for DeepSeek V4.1 Flash - replication disputed](context/EVIDENCE.md#discord-gaudi2-dsv41-prefill-3000tps-disputed)
- [Independent attempt: 80 tok/s single-stream decode but batching and MTP broken, ~100 tok/s prefill](context/EVIDENCE.md#discord-gaudi2-1cat-dsv41-partial)
- [A 1Cat-affiliated Discord participant claimed “6.4k prefill,” but the model, topology, units, benchmark definition, and measurement evidence were not stated.](context/EVIDENCE.md#discord-gaudi2-prefill-6k4-claim)

## Continue this research

Point an agentic harness at this repository. It must begin with [AGENTS.md](AGENTS.md), which loads the current context, shared research policy, and typed submission protocol. Anyone may research and submit candidate evidence; only OpenCat Research can reconcile, Apply, and publish accepted corpus changes.
