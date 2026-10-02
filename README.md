---
generated: true
generator: opencat-research
projectId: gaudi2-practical-inference
objectiveId: gaudi2-practical-inference
acceptedRevision: 4
doNotEdit: true
---
# Gaudi 2 practical inference

Accepted research state published by [OpenCat Research](https://gaudi.clarion.run/projects/gaudi2-practical-inference). Revision **4** · generated 2026-10-02T00:02:06.675Z · [machine corpus](corpus/corpus.json) · [integrity manifest](MANIFEST.json).

## Objective

## Gaudi 2 practical inference

Make standalone Gaudi 2 hardware practical for high-performance LLM inference on ordinary Linux systems.

### Success criteria

- **Access:** A documented single-card PCIe-carrier configuration initializes cleanly and completes a fixed inference smoke workload.
- **Performance:** Pinned single-card workloads show repeatable TTFT, prefill, decode, capacity, correctness, and stability results with retained evidence.

## Brief

Brief as of 2026-10-01.

### Access — Partial

A documented single-card PCIe-carrier configuration initializes cleanly and completes a fixed inference smoke workload.

- Gaudi 2 has a maintained vLLM plugin path and documented installation, but its validated model coverage is narrower than Gaudi 3.
  - Cites: [Serving via the vLLM Hardware Plugin for Intel Gaudi, and the narrowing Gaudi 2 validation coverage](context/EVIDENCE.md#gaudi2-vllm-coverage), [Source installation is pin-locked to a validated upstream vLLM commit](context/EVIDENCE.md#install-pinned-source-build), [Validated model list is broad but Gaudi 3-centric, with a much smaller Gaudi 2 subset](context/EVIDENCE.md#validated-models-gaudi3-centric)
- OAM-to-PCIe operation is reported, while missing-UBB driver behavior, unwired scale-up links, and a complete repeatable host setup remain unresolved.
  - Cites: [Single Gaudi 2 runs on OAM-to-PCIe adapters, but scale-up SerDes/QSFP links are unwired](context/EVIDENCE.md#discord-gaudi2-oam-adapter-enablement)

Uncertain: none.

### Performance — Partial

Pinned single-card workloads show repeatable TTFT, prefill, decode, capacity, correctness, and stability results with retained evidence.

- Single-card measurements show plausible performance headroom, but the available results remain source-reported rather than independently reproduced here.
  - Cites: [Qwen3.8-27B-FP8: archived A800-vs-Gaudi2 record shows shorter TTFT at all tested concurrencies, but a 3.3% decode-throughput deficit at 32 concurrency](context/EVIDENCE.md#qwen38-fp8-a800-vs-gaudi2-record), [Hand-written MME/TPC kernel findings: 1.5 TB/s TPC aggregate, 300 GB/s MME, 40 tok/s Qwen 27B on TPCs alone](context/EVIDENCE.md#discord-gaudi2-handwritten-mme-tpc-kernels)
- The strongest retained throughput evidence is largely TP2 or TP2×PP2 and must not be generalized to a standalone carrier card.
  - Cites: [DeepSeek V4.1 unified full-acceleration run: 81.347 tokens/s mean with an in-repository evidence bundle and explicit lifecycle checks](context/EVIDENCE.md#deepseek-v41-full-accel-evidence-bundle), [Qwen TP2 gains came from fusing the AllReduce/residual/RMSNorm boundary, after a silent missing-collective bug in deferred reductions was fixed first](context/EVIDENCE.md#tp2-reduction-fusion-and-correctness), [Reported DSV4.1 at 73.5 tok/s token-generation at 1M context on 4 Gaudi 2](context/EVIDENCE.md#discord-cdna2-gaudi2-dsv41-1m-context)

Uncertain: [~3000 tok/s prefill on 4 Gaudi 2 (TP2xPP2) for DeepSeek V4.1 Flash - replication disputed](context/EVIDENCE.md#discord-gaudi2-dsv41-prefill-3000tps-disputed), [Independent attempt: 80 tok/s single-stream decode but batching and MTP broken, ~100 tok/s prefill](context/EVIDENCE.md#discord-gaudi2-1cat-dsv41-partial), [A 1Cat-affiliated Discord participant claimed “6.4k prefill,” but the model, topology, units, benchmark definition, and measurement evidence were not stated.](context/EVIDENCE.md#discord-gaudi2-prefill-6k4-claim)

## Direction

## Next

**[What is the reproducible single-card OAM-to-PCIe bring-up path?](context/EVIDENCE.md#question-direct-attach)**
- Work status: blocked; priority: 1
- Definition of done: A named single-card configuration enumerates cleanly, initializes the driver, passes health diagnostics, and completes a fixed inference workload with the full procedure retained.
- Next action: Run and document one complete carrier-to-inference bring-up on a named host and software version.
- Inputs: [Gaudi 2 hardware access for reproducible tests](context/EVIDENCE.md#need-gaudi2-host), [Documented carrier and driver bring-up run](context/EVIDENCE.md#need-carrier-bringup-run), [Proposed power and thermal characterization](context/EVIDENCE.md#need-power-thermal-characterization)

## Blocker

The next question is blocked.
Inputs: [Gaudi 2 hardware access for reproducible tests](context/EVIDENCE.md#need-gaudi2-host), [Documented carrier and driver bring-up run](context/EVIDENCE.md#need-carrier-bringup-run), [Proposed power and thermal characterization](context/EVIDENCE.md#need-power-thermal-characterization)

## Decisions

No steering decisions.

## Queue

- P1 · blocked: [What is the reproducible single-card OAM-to-PCIe bring-up path?](context/EVIDENCE.md#question-direct-attach)
- P2 · ready: [Where does warmed single-card decode time go: graph compilation, replay, host dispatch, or execution?](context/EVIDENCE.md#question-graph-dispatch)
- P3 · blocked: [Why do long-context prefill and batching results diverge so widely?](context/EVIDENCE.md#question-prefill-batching)
- P4 · ready: [Which quantization and model formats reliably execute on Gaudi 2 today?](context/EVIDENCE.md#question-quant-model)
- P5 · ready: [Which multi-card optimizations transfer to standalone single-card inference?](context/EVIDENCE.md#question-topology-transfer)

## Continue this research

Point an agentic harness at this repository. It must begin with [AGENTS.md](AGENTS.md), which loads the current context, shared research policy, and typed submission protocol. Anyone may research and submit candidate evidence; only OpenCat Research can reconcile, Apply, and publish accepted corpus changes.
