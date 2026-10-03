---
generated: true
generator: opencat-research
projectId: gaudi2-practical-inference
objectiveId: gaudi2-practical-inference
acceptedRevision: 6
doNotEdit: true
---
# Accepted changes

Git history is the complete publication history. This projection lists current public records under the accepted revision that last changed them.

## Revision 6

Applied 2026-10-03T06:40:16.205Z.

- Accepted Entry: `gaudi-plugin-serialized-fp8-branch` — The pinned Gaudi plugin defines a distinct non-block processing branch for already-serialized FP8 weights.
- Accepted Entry: `upstream-quantization-mismatch-guard` — Upstream vLLM ModelConfig enforces a quantization mismatch guard that raises ValueError if explicit CLI quantization differs from checkpoint quant_method unless reconciled by an override hook.
- Source added: `vllm-gaudi-hpu-fp8-ops` — hpu_fp8.py
- Source added: `vllm-upstream-verify-quantization` — model.py

## Revision 5

Applied 2026-10-03T01:28:11.554Z.

- Accepted Entry: `experimental-triton-gaudi2-backend-pr11545` — Experimental Triton backend for Gaudi 2 lowers TTIR to TPC-C for SynapseAI 1.24.1, but remains unmerged upstream
- Source added: `github-pr-triton-11545` — Add experimental Gaudi2 backend support by yangzhuxinyzx · Pull Request #11545 · triton-lang/triton · GitHub

## Revision 4

Applied 2026-10-02T00:02:06.675Z.

- Accepted Entry: `discord-gaudi2-graph-break-tensor-clone-dispatch` — Per-token HPU graph breaks in communication ops can add 35–55 ms dispatch latency, reducible below 1 ms via tensor cloning

## Revision 3

Applied 2026-10-01T23:51:08.250Z.

- State: current State revised

## Revision 2

Applied 2026-09-26T16:52:33.255Z.

- Accepted Entry: `discord-gaudi2-prefill-6k4-claim` — A 1Cat-affiliated Discord participant claimed “6.4k prefill,” but the model, topology, units, benchmark definition, and measurement evidence were not stated.

## Revision 1

Applied 2026-09-26T16:48:39.018Z.

- Accepted Entry: `deepseek-v41-pr40-code-not-throughput-recipe` — Merged 1Cat PR #40 supplies an optimized DeepSeek V4.1 TP2×PP2 prefill implementation and correctness-qualified serving path, but it does not provide a reproducible throughput result or confirm 6.4k prefill tokens/s.
- Source added: `github-1cat-pr40-prefill-qualification` — [HPU] Integrate general V4.1 prefill optimizations by yangzhuxinyzx · Pull Request #40 · 1CatAI/1Cat-vLLM-Gaudi · GitHub
