---
generated: true
generator: opencat-research
projectId: gaudi2-practical-inference
objectiveId: gaudi2-practical-inference
acceptedRevision: 16
doNotEdit: true
---
# Accepted changes

Git history is the complete publication history. This projection lists current public records under the accepted revision that last changed them.

## Revision 16

Applied 2026-11-08T00:09:43.324Z.

- Accepted Entry: `discord-fixed-slot-kv-cache-capacity-tradeoff` — A contributor reported an early KV-cache design using fixed-size HBM pools per slot and host eviction, with high HBM use when request lengths varied.
- Accepted Entry: `tpc-clang-scalar-splat-shift-report` — A public issue reports that tpc-clang 2.7.33 can emit a left shift instead of a scalar-splat right shift when compiling for Gaudi 2 at optimization level O1 or higher.
- Source added: `tpc-llvm-issue-7-scalar-shift` — tpc-clang 2.7.33: scalar-splat right shift compiles as LEFT shift · Issue #7 · HabanaAI/tpc_llvm · GitHub

## Revision 15

Applied 2026-11-07T17:08:17.633Z.

- Accepted Entry: `vllm-gaudi-v0260-inc-conditional-cpu-loading` — Plugin v0.26.0 defaults INC weight loading to CPU only when the load device is unspecified; nonempty QUANT_CONFIG also triggers this default.
- Source added: `vllm-gaudi-v0260-platform-inc-cpu-default` — platform.py
- Source added: `vllm-gaudi-v0260-tag-commit` — d75619aed862d4ec3c37dd681beef1adbbaab98e

## Revision 14

Applied 2026-11-07T17:08:10.418Z.

- Accepted Entry: `vllm-gaudi-b059f9c-vllm-stable-commit-sha` — Plugin commit b059f9c declares upstream vLLM commit 568afb3a13806beb53bb2e6bd518269357b237c0 in VLLM_STABLE_COMMIT
- Source added: `vllm-gaudi-vllm-stable-commit-b059f9c` — VLLM_STABLE_COMMIT

## Revision 13

Applied 2026-11-07T17:08:03.706Z.

- Accepted Entry: `discord-gaudi2-sp3-waterblock-compatibility` — Community reports indicate AMD Socket SP3 liquid cooling blocks fit Gaudi 2 OAM modules for benchtop thermal management

## Revision 12

Applied 2026-11-07T17:07:50.612Z.

- Updated Entry: `quantization-backends-and-calibration` — Quantization support is INC FP8 plus INT4 AWQ/GPTQ, with device-bound calibration and MoE unification caveats
- Source added: `inc-weight-loading-guide-2026-10-03` — Intel® Neural Compressor - vLLM Hardware Plugin for Intel® Gaudi®

## Revision 11

Applied 2026-11-07T17:07:41.317Z.

- Accepted Entry: `discord-llamacpp-kv-size-graph-recompilation` — A community contributor reported graph recompilation at every KV size in a real workload using a llama.cpp backend under development.

## Revision 10

Applied 2026-11-07T17:07:34.329Z.

- Accepted Entry: `discord-wright-chunked-prefill-decode-tradeoff` — A contributor reported that Wright 0.2.0's interleaved chunked prefill reduced decode stalls in a Qwen3.8-27B workload, with a throughput and first-token tradeoff.

## Revision 9

Applied 2026-11-07T17:07:23.686Z.

- Accepted Entry: `discord-llamacpp-layer-split-quant-handling` — A contributor reported an in-development llama.cpp backend with layer or tensor splitting and on-read dequantization of sub-FP8 weights.

## Revision 8

Applied 2026-11-07T15:56:31.793Z.

- Accepted Entry: `gaudi-inc-quant-config-presence-checks` — At plugin commit b059f9c, an empty but present QUANT_CONFIG satisfies has_quant_config and selects the runner's INC finalize_calibration import branch.
- Updated Entry: `question-quant-model` — Which quantization and model formats reliably execute on Gaudi 2 today?
- Source added: `gaudi-b059-runner-inc-import-presence` — hpu_model_runner.py
- Source added: `gaudi-b059-utils-quant-config-presence` — utils.py

## Revision 7

Applied 2026-11-07T15:56:07.752Z.

- Updated Entry: `question-graph-dispatch` — Where does warmed single-card decode time go: graph compilation, replay, host dispatch, or execution?

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
