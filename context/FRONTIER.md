---
generated: true
generator: opencat-research
projectId: gaudi2-practical-inference
objectiveId: gaudi2-practical-inference
acceptedRevision: 12
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

Separate costs on one fixed model and shape; success remains a device-measured, trace-backed latency budget identifying the dominant controllable component. Prepare a single-card TP1/PP1 experiment manifest and timing/log schema with all outcomes marked not tested. Gate the comparison on source/code verification that the pinned stack supports ordinary submission and graph replay within the same execution mode; otherwise mark replay unavailable, and treat any execution-mode comparison as a separate experiment. Compare cold versus recipe-cache-reused startup separately from warmed ordinary submission versus supported replay, holding model, precision, inputs, batch, context, decode length and buckets fixed. Record compilation/capture, recipe loading and warm-up as distinct observable stages; exclude them from steady state and flag later compilation or cache misses. Define CPU submission entry/exit separately from replay events and device kernel/DMA timestamps; host-call duration is not device completion. Define end-to-end token latency from ready decode state to token availability, including required waits, sampling and output handling; separate prefill/TTFT. Specify only synchronization mechanisms verified for the pinned stack: isolated-step diagnostics bracket the region with completion boundaries, while representative steady-state runs retain natural synchronization to avoid changing scheduling. Correlate host/device traces and graph identifiers, preserve overlap rather than summing overlapping durations, and do not infer device time by subtracting host time from end-to-end latency. Retain exact plugin/upstream SHAs, driver/runtime, PyTorch/bridge/profiler/dependency versions, host/carrier/device identity, model/tokenizer revisions and artifact hashes, token inputs, decoding configuration, mode/compile/replay flags, buckets, cache provenance, warm-up and memory settings. Retain startup/compiler/cache and capture logs, graph counts per token, raw token timestamps, synchronization locations, correlated CPU/device traces, memory observations, exceptions and correctness checks. Plan repeated profiled and unprofiled runs and latency distributions. Community dispatch bottleneck reports motivate attribution but are not established single-card outcomes.
- Work status: ready; priority: 2
- Definition of done: A repeatable warmed per-token latency breakdown identifies the dominant controllable component with graph compilation excluded from steady state.
- Next action: Prepare a software-only TP1/PP1 fixed-shape decode manifest and timing/log schema; verify the pinned stack's actual same-mode submission/replay controls and synchronization mechanisms before naming APIs. Record all outcomes as not tested. Once hardware is available, capture repeated warmed ordinary-submission versus supported-replay runs with correlated host/device traces and unprofiled controls, retaining cold compilation/capture and warm-up separately.
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

Map supported checkpoint formats, device-bound calibration, fallback paths, and validated models without conflating hardware dtype support with end-to-end quantized inference. Prepare a configuration matrix with BF16/unquantized and existing FP8 quant_method=fp8 artifacts: BF16 with omitted quantization/unset QUANT_CONFIG; BF16 with inc/valid Gaudi-2 calibration JSON; FP8 with omitted quantization/unset QUANT_CONFIG; FP8 with inc/unset QUANT_CONFIG; FP8 with inc/valid JSON; repeat the latter with explicit CPU load device; and FP8 with omitted quantization/present-empty QUANT_CONFIG as a diagnostic negative control. Other rows use unspecified load device. Record checkpoint revisions, configuration, tensor layout/dtypes and artifact hashes; explicit arguments, environment state, requested and resolved method/load device; exact plugin/upstream commits and Gaudi software, PyTorch, INC and Transformers versions. Later capture configuration validation, model construction, weight loading, INC preparation/conversion if reached, HPU transfer/initialization, warm-up and fixed inference as separate stages with exceptions/tracebacks and correctness, memory, calibration and warmed throughput outcomes. Full checkpoint FP8 versus explicit inc override/rejection and converter registration/invocation remain unresolved. Preserve representative INT4 coverage in the final tested matrix; preparation is not execution evidence.
- Work status: ready; priority: 4
- Definition of done: A tested compatibility matrix records load, correctness, memory, calibration, and throughput outcomes for representative BF16, FP8, and INT4 checkpoints.
- Next action: Prepare the artifact/configuration matrix without claiming runtime outcomes; resolve the matching upstream vLLM SHA and readable INC registration/conversion caller plus FP8-versus-explicit-inc override/rejection branch. When Gaudi 2 access is available, execute the matrix and retain stage-specific failures and load, correctness, memory, calibration and warmed throughput results.
- Inputs: [need-gaudi2-host](context/EVIDENCE.md#need-gaudi2-host)
- Evidence basis: [gaudi2-datatypes](context/EVIDENCE.md#gaudi2-datatypes), [quantization-backends-and-calibration](context/EVIDENCE.md#quantization-backends-and-calibration), [discord-gaudi2-quantization-gaps](context/EVIDENCE.md#discord-gaudi2-quantization-gaps), [install-pinned-source-build](context/EVIDENCE.md#install-pinned-source-build), [gaudi2-vllm-coverage](context/EVIDENCE.md#gaudi2-vllm-coverage), [gaudi-inc-quant-config-presence-checks](context/EVIDENCE.md#gaudi-inc-quant-config-presence-checks)

## question-topology-transfer

Which multi-card optimizations transfer to standalone single-card inference?

Separate MME/TPC/data-movement techniques from HCCL, TP, PP, and scale-up fabric effects before using multi-card results to guide desktop work.
- Work status: ready; priority: 5
- Definition of done: An explicit set of multi-card techniques is tested on one card and separated from HCCL, tensor-parallel, pipeline-parallel, and scale-up-fabric effects.
- Next action: Re-run one kernel/runtime optimization on TP1 and compare against its multi-card baseline.
- Inputs: [need-gaudi2-host](context/EVIDENCE.md#need-gaudi2-host), [need-profiler-trace](context/EVIDENCE.md#need-profiler-trace)
- Evidence basis: [gaudi2-roce-network](context/EVIDENCE.md#gaudi2-roce-network), [tp2-reduction-fusion-and-correctness](context/EVIDENCE.md#tp2-reduction-fusion-and-correctness), [discord-gaudi2-oam-adapter-enablement](context/EVIDENCE.md#discord-gaudi2-oam-adapter-enablement)
