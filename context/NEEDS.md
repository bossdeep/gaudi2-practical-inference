---
generated: true
generator: opencat-research
projectId: gaudi2-practical-inference
objectiveId: gaudi2-practical-inference
acceptedRevision: 2
doNotEdit: true
---
# Inputs needed

Derived from active work-item input references.

## need-gaudi2-host

Gaudi 2 hardware access for reproducible tests

A contributor needs access to a working Gaudi 2 host so fixed single-card workloads and bring-up procedures can be reproduced.

- Evidence: proposed
- Area: hardware
- Basis: `discord-gaudi2-research-roadmap-thread`, `discord-gaudi2-oam-adapter-enablement`

## need-carrier-bringup-run

Documented carrier and driver bring-up run

Retain carrier identity, host platform, firmware, driver changes, health output, and a completed inference smoke workload.

- Evidence: proposed
- Area: hardware
- Basis: `discord-gaudi2-oam-adapter-enablement`, `gaudi2-install-prereqs`

## need-power-thermal-characterization

Proposed power and thermal characterization

The documented accelerator envelope reaches 600 W; a standalone carrier path needs measured power delivery and thermal behavior before it can be called reproducible.

- Evidence: proposed
- Area: hardware
- Basis: `gaudi2-arch-specs`, `gaudi2-reliability-observability`

## need-profiler-trace

Profiler trace from one fixed inference workload

Capture one warmed workload with enough MME, TPC, DMA, graph, and host-dispatch timing to separate execution from submission overhead.

- Evidence: proposed
- Area: performance
- Basis: `discord-gaudi2-handwritten-mme-tpc-kernels`, `discord-gaudi2-dispatch-overhead-resident-graphs`
