---
generated: true
generator: opencat-research
projectId: gaudi2-practical-inference
objectiveId: gaudi2-practical-inference
acceptedRevision: 2
doNotEdit: true
---
# Current State

As of 2026-09-27; accepted revision 2.

## TLDR

1. Gaudi 2 has a maintained vLLM plugin path and documented installation, but its validated model coverage is narrower than Gaudi 3.
   - Basis: `gaudi2-vllm-coverage`, `install-pinned-source-build`, `validated-models-gaudi3-centric`
2. Single-card measurements show plausible performance headroom, but the available results remain source-reported rather than independently reproduced here.
   - Basis: `qwen38-fp8-a800-vs-gaudi2-record`, `discord-gaudi2-handwritten-mme-tpc-kernels`
3. The strongest retained throughput evidence is largely TP2 or TP2×PP2 and must not be generalized to a standalone carrier card.
   - Basis: `deepseek-v41-full-accel-evidence-bundle`, `tp2-reduction-fusion-and-correctness`, `discord-cdna2-gaudi2-dsv41-1m-context`
4. OAM-to-PCIe operation is reported, while missing-UBB driver behavior, unwired scale-up links, and a complete repeatable host setup remain unresolved.
   - Basis: `discord-gaudi2-oam-adapter-enablement`, `question-direct-attach`

## Primary blocker

No retained standalone configuration joins carrier bring-up, pinned software, health checks, and a fixed inference baseline.

- **[Single Gaudi 2 runs on OAM-to-PCIe adapters, but scale-up SerDes/QSFP links are unwired](context/EVIDENCE.md#discord-gaudi2-oam-adapter-enablement)** — `discord-gaudi2-oam-adapter-enablement`
- **[What is the reproducible single-card OAM-to-PCIe bring-up path?](context/EVIDENCE.md#question-direct-attach)** — `question-direct-attach`
- **[Documented carrier and driver bring-up run](context/EVIDENCE.md#need-carrier-bringup-run)** — `need-carrier-bringup-run`

## Next action

Document one single-card configuration, then profile the same fixed workload so access and performance work share one baseline.

- **[What is the reproducible single-card OAM-to-PCIe bring-up path?](context/EVIDENCE.md#question-direct-attach)** — `question-direct-attach`
- **[Where does warmed single-card decode time go: graph compilation, replay, host dispatch, or execution?](context/EVIDENCE.md#question-graph-dispatch)** — `question-graph-dispatch`
- **[Profiler trace from one fixed inference workload](context/EVIDENCE.md#need-profiler-trace)** — `need-profiler-trace`

## Known

- **[Gaudi 2 hardware architecture and headline specifications](context/EVIDENCE.md#gaudi2-arch-specs)** — `gaudi2-arch-specs`
- **[Source installation is pin-locked to a validated upstream vLLM commit](context/EVIDENCE.md#install-pinned-source-build)** — `install-pinned-source-build`
- **[Compatibility matrix pins one plugin release to one vLLM version and one Gaudi software version](context/EVIDENCE.md#version-compatibility-matrix)** — `version-compatibility-matrix`

## Uncertain

- **[~3000 tok/s prefill on 4 Gaudi 2 (TP2xPP2) for DeepSeek V4.1 Flash - replication disputed](context/EVIDENCE.md#discord-gaudi2-dsv41-prefill-3000tps-disputed)** — `discord-gaudi2-dsv41-prefill-3000tps-disputed`
- **[Independent attempt: 80 tok/s single-stream decode but batching and MTP broken, ~100 tok/s prefill](context/EVIDENCE.md#discord-gaudi2-1cat-dsv41-partial)** — `discord-gaudi2-1cat-dsv41-partial`
- **[A 1Cat-affiliated Discord participant claimed “6.4k prefill,” but the model, topology, units, benchmark definition, and measurement evidence were not stated.](context/EVIDENCE.md#discord-gaudi2-prefill-6k4-claim)** — `discord-gaudi2-prefill-6k4-claim`
