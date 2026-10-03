---
generated: true
generator: opencat-research
projectId: gaudi2-practical-inference
objectiveId: gaudi2-practical-inference
acceptedRevision: 6
doNotEdit: true
---
# Frontier

Active unfinished questions, ordered by accepted priority.

## question-direct-attach

What is the reproducible single-card OAM-to-PCIe bring-up path?

Define the carrier, missing-UBB driver behavior, host and firmware compatibility, power delivery, thermal setup, health checks, and inference smoke workload.
- Work status: blocked; priority: 1
- Definition of done: A named single-card configuration enumerates cleanly, initializes the driver, passes health diagnostics, and completes a fixed inference workload with the full procedure retained.
- Next action: Run and document one complete carrier-to-inference bring-up on a named host and software version.
- Inputs: [need-gaudi2-host](context/EVIDENCE.md#need-gaudi2-host), [need-carrier-bringup-run](context/EVIDENCE.md#need-carrier-bringup-run), [need-power-thermal-characterization](context/EVIDENCE.md#need-power-thermal-characterization)
- Evidence basis: [discord-gaudi2-oam-adapter-enablement](context/EVIDENCE.md#discord-gaudi2-oam-adapter-enablement), [gaudi2-install-prereqs](context/EVIDENCE.md#gaudi2-install-prereqs), [gaudi2-arch-specs](context/EVIDENCE.md#gaudi2-arch-specs)

## question-graph-dispatch

Where does warmed single-card decode time go: graph compilation, replay, host dispatch, or execution?

Separate the costs on one fixed model and shape; success is a trace-backed latency budget that identifies the dominant controllable component.
- Work status: ready; priority: 2
- Definition of done: A repeatable warmed per-token latency breakdown identifies the dominant controllable component with graph compilation excluded from steady state.
- Next action: Capture a warmed trace and compare ordinary submission with the largest supported replay region.
- Inputs: [need-gaudi2-host](context/EVIDENCE.md#need-gaudi2-host), [need-profiler-trace](context/EVIDENCE.md#need-profiler-trace)
- Evidence basis: [gaudi2-exec-modes](context/EVIDENCE.md#gaudi2-exec-modes), [warmup-graph-cache-cost](context/EVIDENCE.md#warmup-graph-cache-cost), [discord-gaudi2-dispatch-overhead-resident-graphs](context/EVIDENCE.md#discord-gaudi2-dispatch-overhead-resident-graphs)

## question-prefill-batching

Why do long-context prefill and batching results diverge so widely?

Reconcile the disputed ~3000 tok/s TP2×PP2 report with the independent ~100 tok/s report under fixed model, prompt, precision, topology, and measurement definitions.
- Work status: blocked; priority: 3
- Definition of done: A retained benchmark matrix under fixed model, prompt, precision, topology, and timing definitions explains the reported prefill discrepancy.
- Next action: Run the same prompt/concurrency sweep on one pinned stack and retain raw timings and configuration.
- Inputs: [need-gaudi2-host](context/EVIDENCE.md#need-gaudi2-host), [need-profiler-trace](context/EVIDENCE.md#need-profiler-trace)
- Evidence basis: [discord-gaudi2-dsv41-prefill-3000tps-disputed](context/EVIDENCE.md#discord-gaudi2-dsv41-prefill-3000tps-disputed), [discord-gaudi2-1cat-dsv41-partial](context/EVIDENCE.md#discord-gaudi2-1cat-dsv41-partial), [qwen38-fp8-a800-vs-gaudi2-record](context/EVIDENCE.md#qwen38-fp8-a800-vs-gaudi2-record)

## question-quant-model

Which quantization and model formats reliably execute on Gaudi 2 today?

Map supported checkpoint formats, device-bound calibration, fallback paths, and validated models without conflating hardware dtype support with end-to-end quantized inference.
- Work status: ready; priority: 4
- Definition of done: A tested compatibility matrix records load, correctness, memory, calibration, and throughput outcomes for representative BF16, FP8, and INT4 checkpoints.
- Next action: Select representative BF16, FP8, and INT4 checkpoints and record load, correctness, memory, and throughput outcomes.
- Inputs: [need-gaudi2-host](context/EVIDENCE.md#need-gaudi2-host)
- Evidence basis: [gaudi2-datatypes](context/EVIDENCE.md#gaudi2-datatypes), [quantization-backends-and-calibration](context/EVIDENCE.md#quantization-backends-and-calibration), [discord-gaudi2-quantization-gaps](context/EVIDENCE.md#discord-gaudi2-quantization-gaps)

## question-topology-transfer

Which multi-card optimizations transfer to standalone single-card inference?

Separate MME/TPC/data-movement techniques from HCCL, TP, PP, and scale-up fabric effects before using multi-card results to guide desktop work.
- Work status: ready; priority: 5
- Definition of done: An explicit set of multi-card techniques is tested on one card and separated from HCCL, tensor-parallel, pipeline-parallel, and scale-up-fabric effects.
- Next action: Re-run one kernel/runtime optimization on TP1 and compare against its multi-card baseline.
- Inputs: [need-gaudi2-host](context/EVIDENCE.md#need-gaudi2-host), [need-profiler-trace](context/EVIDENCE.md#need-profiler-trace)
- Evidence basis: [gaudi2-roce-network](context/EVIDENCE.md#gaudi2-roce-network), [tp2-reduction-fusion-and-correctness](context/EVIDENCE.md#tp2-reduction-fusion-and-correctness), [discord-gaudi2-oam-adapter-enablement](context/EVIDENCE.md#discord-gaudi2-oam-adapter-enablement)
