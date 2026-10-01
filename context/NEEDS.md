---
generated: true
generator: opencat-research
projectId: gaudi2-practical-inference
objectiveId: gaudi2-practical-inference
acceptedRevision: 3
doNotEdit: true
---
# Inputs needed

Input questions referenced by open work.

## need-gaudi2-host

Gaudi 2 hardware access for reproducible tests

A contributor needs access to a working Gaudi 2 host so fixed single-card workloads and bring-up procedures can be reproduced.

- Area: hardware
- Needed by: [What is the reproducible single-card OAM-to-PCIe bring-up path?](context/EVIDENCE.md#question-direct-attach), [Where does warmed single-card decode time go: graph compilation, replay, host dispatch, or execution?](context/EVIDENCE.md#question-graph-dispatch), [Why do long-context prefill and batching results diverge so widely?](context/EVIDENCE.md#question-prefill-batching), [Which quantization and model formats reliably execute on Gaudi 2 today?](context/EVIDENCE.md#question-quant-model), [Which multi-card optimizations transfer to standalone single-card inference?](context/EVIDENCE.md#question-topology-transfer)

## need-carrier-bringup-run

Documented carrier and driver bring-up run

Retain carrier identity, host platform, firmware, driver changes, health output, and a completed inference smoke workload.

- Area: hardware
- Needed by: [What is the reproducible single-card OAM-to-PCIe bring-up path?](context/EVIDENCE.md#question-direct-attach)

## need-power-thermal-characterization

Proposed power and thermal characterization

The documented accelerator envelope reaches 600 W; a standalone carrier path needs measured power delivery and thermal behavior before it can be called reproducible.

- Area: hardware
- Needed by: [What is the reproducible single-card OAM-to-PCIe bring-up path?](context/EVIDENCE.md#question-direct-attach)

## need-profiler-trace

Profiler trace from one fixed inference workload

Capture one warmed workload with enough MME, TPC, DMA, graph, and host-dispatch timing to separate execution from submission overhead.

- Area: performance
- Needed by: [Where does warmed single-card decode time go: graph compilation, replay, host dispatch, or execution?](context/EVIDENCE.md#question-graph-dispatch), [Why do long-context prefill and batching results diverge so widely?](context/EVIDENCE.md#question-prefill-batching), [Which multi-card optimizations transfer to standalone single-card inference?](context/EVIDENCE.md#question-topology-transfer)
