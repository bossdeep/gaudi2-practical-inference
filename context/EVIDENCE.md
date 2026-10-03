---
generated: true
generator: opencat-research
projectId: gaudi2-practical-inference
objectiveId: gaudi2-practical-inference
acceptedRevision: 5
doNotEdit: true
---
# Evidence

Every accepted Entry, including inactive history. Claims carry an evidence badge; questions and decisions do not. Public citations retain the exact bounded support note used by the corpus.

## gaudi2-arch-specs

**Gaudi 2 hardware architecture and headline specifications**

Documented: 7nm process (down from 16nm on Gaudi 1); 24 AI-customized Tensor Processor Cores (4th-generation TPC, up from 8) plus a Matrix Multiplication Engine; heterogeneous MME+TPC design intended to overlap GEMM and non-GEMM execution; 96 GB HBM2e in-package memory at 2.45 TB/s (up from 32 GB), 48 MB on-die SRAM sized so MME, TPC, DMAs and RDMA NICs run in parallel; integrated media decoders (HEVC, H.264, VP9, JPEG) with post-decode transforms for vision pre-processing. Form factor: OCP OAM 1.1 mezzanine card (HL-225H, Intel product-brief record dated 2023-07-28), PCIe Gen4 x16 host interface, 48x 56Gb PAM4 SerDes links, up to 600 W power with passive cooling; 8-card HLBA-225 baseboard (585x417x4.6 mm) and the 8-card HLS-Gaudi2 server (dual Xeon Ice Lake, 2 PCIe switches, 4x (3+1) 4 kW PSU). Launch context: introduced 2022-05-10 at Intel Vision;

- Kind: Claim
- Status: active
- Evidence: Documented
- Area: hardware
- Document date: 2022-05-10
- Retrieved: 2026-09-25
- Scope: not separately stated
- Topics: architecture, tpc, mme, hbm2e, hl-225h, oam-1-1, hls-gaudi2
- Basis Entries: none
- Omitted private support records: 0

### Citations

- **Intel Gaudi 2 AI Accelerators white paper v2.0 (Oct 2023)** (`intel-gaudi-2-ai-accelerators-white-paper-8057b8a`)
  - Locator: https://cdrdv2-public.intel.com/839363/Intel-Gaudi2-AI-Accelerators-whitepaper.pdf
  - Support: Sections II/VIII/IX/X give 96 GB HBM2E @2.45 TB/s + 48 MB SRAM, 7nm-implied TPC lineage, OAM 1.1 mezzanine up to 600 W with PCIe Gen4 x16 and 48x 56Gb PAM4 SerDes (24x100GbE), HLBA-225 baseboard and HLS-Gaudi2 server configuration.
- **Gaudi Architecture (docs.habana.ai 1.24.0)** (`gaudi-architecture-docs-habana-ai-1-24-0-549cda7`)
  - Locator: https://docs.habana.ai/en/latest/Gaudi_Overview/Gaudi_Architecture.html
  - Support: "Gaudi 2 offers 2.4 Terabits of networking bandwidth with the native integration on-chip of 24 x 100 Gbps RoCE V2 RDMA NICs... The Gaudi 2 memory subsystem includes 96 GB of HBM2E memories delivering 2.45 TB/sec bandwidth, in addition to a 48 MB of local SRAM..." plus FP8/FP16/BF16/FP32/TF32 datatype list and media-decoder formats.

## gaudi2-roce-network

**On-chip RoCEv2 fabric: 24x 100 GbE ports, 21 scale-up + 3 scale-out, and derived per-card bandwidth**

Documented: each Gaudi 2 integrates 24x 100 Gbps RoCEv2 RDMA NICs on-die for 2.4 Tb/s aggregate. 21 ports are hardwired to the other seven accelerators in the 8-card box in a non-blocking all-to-all arrangement (3 ports per peer); the remaining 3 ports per card are scale-out to standard Ethernet switches, routed on the HLBA-225 baseboard to six QSFP-DD connectors (8x3 = 2.4 TbE). Intel's network-configuration docs give the arithmetic: per-Gaudi-2 scale-up 21x100 Gbps = 262.5 GB/s unidirectional (525 GB/s bidirectional), per-card scale-out 3x100 Gbps = 37.5 GB/s each direction, and HLS-2 box scale-out 300 GB/s unidirectional (600 GB/s bidirectional). Those GB/s values are derived from link count x line rate, not measured collectives. Docs state Gaudi 2's network architecture is the same shape as Gaudi 3 with 100 Gbps links instead of 200 Gbps. Host-side bring-up note:

- Kind: Claim
- Status: active
- Evidence: Documented
- Area: distributed
- Document date: 2023-07-28
- Retrieved: 2026-09-25
- Scope: not separately stated
- Topics: rocev2, scale-up, scale-out, hccl, hls-gaudi2, hlba-225
- Basis Entries: none
- Omitted private support records: 0

### Citations

- **Gaudi Architecture (docs.habana.ai 1.24.0)** (`gaudi-architecture-docs-habana-ai-1-24-0-549cda7`)
  - Locator: https://docs.habana.ai/en/latest/Gaudi_Overview/Gaudi_Architecture.html
  - Support: "Gaudi architecture is the first DL training processor that has integrated RDMA over Converged Ethernet (RoCE v2) engines on-chip... These can be connected directly between Gaudi processors, or through any number of standard Ethernet switches."
- **Intel Gaudi Network Configuration (docs.habana.ai 1.24.0)** (`intel-gaudi-network-configuration-docs-hab-191f4e6`)
  - Locator: https://docs.habana.ai/en/latest/Management_and_Monitoring/Network_Configuration/index.html
  - Support: "Gaudi 2 network architecture is similar to Gaudi 3 except that the network links operate at 100Gbps. The theoretical peak of scale-up bandwidth from each Gaudi 2 is 21*100Gbps = 262.5 GB/s unidirectional... The scale-out bandwidth from each Gaudi 2 is 3*100Gbps = 37.5 GB/s in each direction... scale-out bandwidth of an HLS-2 box consisting of 8 Gaudi 2s is 3*8*100Gbps = 300 GB/s unidirectional."

## gaudi2-datatypes

**Supported data types and precisions (and why INT8 dtype support is not INT8 quantized inference)**

Documented: Gaudi 2 supports FP32, TF32, BF16, FP16 and FP8 (both E4M3 and E5M2); all MME datatypes accumulate into an FP32 accumulator; the TPC additionally handles INT32/INT16/INT8. FP8 was the headline new datatype versus Gaudi 1. On the framework side, the PyTorch integration exposes Int8/Int16/Int32/Int64/Float8/Float16/Float32/BFloat16 tensors (Int8/16/32 with limited operator coverage), but the same support matrix lists only 'FP8 quantization: Yes' and 'Int8/16/32 quantization: No', 'Int4 quantization: No' - i.e. datatype availability in ops does not imply a supported quantized-inference path. Inference:

- Kind: Claim
- Status: active
- Evidence: Documented
- Area: quantization
- Document date: 2023-10-01
- Retrieved: 2026-09-25
- Scope: not separately stated
- Topics: precision, bf16, fp16, fp8, int8, tf32, fp32-accumulate
- Basis Entries: none
- Omitted private support records: 0

### Citations

- **Gaudi Architecture (docs.habana.ai 1.24.0)** (`gaudi-architecture-docs-habana-ai-1-24-0-549cda7`)
  - Locator: https://docs.habana.ai/en/latest/Gaudi_Overview/Gaudi_Architecture.html
  - Support: "Gaudi 2 supports all popular data types required for deep learning: FP32, TF32, BF16, FP16 & FP8 (both E4M3 and E5M2). In the MME, all data types are accumulated into an FP32 accumulator."
- **Intel Gaudi 2 AI Accelerators white paper v2.0 (Oct 2023)** (`intel-gaudi-2-ai-accelerators-white-paper-8057b8a`)
  - Locator: https://cdrdv2-public.intel.com/839363/Intel-Gaudi2-AI-Accelerators-whitepaper.pdf
  - Support: TPC is "a general purpose VLIW processor which is 256B SIMD wide and supports FP32, BF16, FP16 & FP8 (Both E4M3 and E5M2), in addition to INT32, INT16 & INT8 data types."

## gaudi2-fp8-inference

**How FP8 inference is enabled on Gaudi 2 - and the Gaudi-2-specific FP8 scale limits**

Documented enablement path: FP8 inference uses Intel Neural Compressor (INC) with an explicit measure-then-quantize flow - htcore.hpu_set_env(), FP8Config.from_json_file, prepare (MEASURE mode) then convert (QUANTIZE mode), htcore.hpu_initialize(model, mark_scales=True), finalize_calibration to dump stats; scale methods include maxabs_hw, maxabs_pow2 and per-channel variants; PT_HPU_WEIGHT_SHARING=0 is needed to free BF16 weights so only FP8 weights remain resident. Gaudi-2-specific constraint (device_for_scales="GAUDI2"): only 4 E4M3 exponent-bias values exist (3, 7, 11, 15; default 7), whereas "In Gaudi 3, the exponent-bias range is expanded to (0, 63)" - so Gaudi 2 quantized scales are coarser and recompile-driven than on Gaudi 3.

- Kind: Claim
- Status: active
- Evidence: Documented
- Area: quantization
- Document date: 2026-01-01
- Retrieved: 2026-09-25
- Scope: not separately stated
- Topics: fp8, e4m3, e5m2, inc, exponent-bias, kv-cache, quantization-workflow
- Basis Entries: none
- Omitted private support records: 0

### Citations

- **Run Inference Using FP8 (docs.habana.ai 1.24.0)** (`run-inference-using-fp8-docs-habana-ai-1-2-6a4e13c`)
  - Locator: https://docs.habana.ai/en/latest/PyTorch/Inference_on_PyTorch/Quantization/Inference_Using_FP8.html
  - Support: "This guide provides the steps required to enable FP8 inference on your Intel Gaudi 2 and Intel Gaudi 3 AI accelerator"; device_for_scales table: "GAUDI2 - In Gaudi 2 there are 4 possible exponent-bias values (3, 7, 11, 15), where 7 is the default exponent bias" vs "GAUDI3 - exponent-bias range is expanded to (0, 63)"; dynamic_quantization "only applies to linear layers"; PT_HPU_WEIGHT_SHARING=0 requirement; unify_measurements flow to run FP8 on fewer cards.
- **Gaudi Release Notes (1.24.x)** (`gaudi-release-notes-1-24-x-2da618f`)
  - Locator: https://docs.habana.ai/en/latest/Release_Notes/GAUDI_Release_Notes.html
  - Support: "Sporadic numerical instability may occur when training with FP8 precision."; vLLM plugin notes flag FP8/KV-cache quantization as "not fully supported with torch.compile execution mode".

## gaudi-sw-suite-scope

**Intel Gaudi software suite (ex-SynapseAI): components, and PyTorch-only framework scope after TensorFlow removal**

Documented: the suite comprises the graph compiler and runtime (operator fusion, layout management, parallelization/pipelining, memory management, recipe caching), the TPC kernel library, firmware and drivers, the TPC SDK (LLVM-based TPC-C compiler, simulator, debugger), the profiler, management/monitoring tooling (HLML, hl-smi, hl_qual), and HCCL for collectives. Multi-stream execution (compute, networking, DMA) is exposed to the framework. Scope caveat: framework integration is now PyTorch-only - TensorFlow support and all TensorFlow reference models were removed in release 1.15.0 (the last TensorFlow-enabled release was 1.14.x with TF 2.13.1), so any TensorFlow-based Gaudi 2 plan implies a frozen 1.14-era stack. Naming: the SynapseAI brand was renamed to "Intel Gaudi software" at 1.15.0 with code unchanged (hence Synapse references persist in the codebase). Inference:

- Kind: Claim
- Status: active
- Evidence: Documented
- Area: software-stack
- Document date: 2026-01-01
- Retrieved: 2026-09-25
- Scope: not separately stated
- Topics: synapseai, graph-compiler, tpc-sdk, hccl, tensorflow-removed, brand-rename
- Basis Entries: none
- Omitted private support records: 0

### Citations

- **Intel Gaudi Software Suite (docs.habana.ai 1.24.0)** (`intel-gaudi-software-suite-docs-habana-ai-19c9d84`)
  - Locator: https://docs.habana.ai/en/latest/Gaudi_Overview/Intel_Gaudi_Software_Suite.html
  - Support: Lists graph compiler and runtime, TPC kernel library, TPC SDK components, HCCL ("Intel Gaudi's implementation of standard collective communication routines with NCCL-compatible APIs... uses Gaudi integrated NICs for both scale-up and scale-out"), and states the software "is integrated with PyTorch".
- **Gaudi Release Notes v1.15** (`gaudi-release-notes-v1-15-2109790`)
  - Locator: https://docs.habana.ai/en/latest/Release_Notes/Release%20Notes%20v1.15.0.html
  - Support: "TensorFlow is no longer supported. Removed all TensorFlow models from Model References GitHub repository." and "With the acquisition of Habana Labs by Intel, the SynapseAI brand has changed to Intel Gaudi software... no code has changed."

## gaudi2-exec-modes

**Execution modes, compilation model and deprecated paths on Gaudi 2 today**

Documented (docs 1.24.0): Eager mode + torch.compile(backend="hpu_backend") is the default path since v1.21.0 and is Intel's recommendation; plain Eager mode is slower because graphs are not optimized; Lazy mode is "a legacy fallback that is no longer developed and will be deprecated", enabled with PT_HPU_LAZY_MODE=1. HPU Graphs exist only in Lazy mode; dynamic shapes are supported in Eager/torch.compile (PT_HPU_ENABLE_REFINE_DYNAMIC_SHAPES, off by default) and in Lazy. Public (non-fork) PyTorch 2.11 is supported in preview: Eager + torch.compile only, no dedicated Docker image, and Lazy is fork-only. Deprecated/EOL paths relevant to a Gaudi 2 deployment: PyTorch Lightning (last supported 2.5.1, tested with v1.21.x), Slurm support to be deprecated in the next release, HabanaAI/vllm-fork end-of-life (superseded by vllm-project/vllm-gaudi), and Model-References LLM training migrating to HabanaAI/Megatron-LM.

- Kind: Claim
- Status: active
- Evidence: Documented
- Area: software-stack
- Document date: 2026-01-01
- Retrieved: 2026-09-25
- Scope: not separately stated
- Topics: eager, lazy, torch-compile, hpu-backend, hpu-graphs, deprecations
- Basis Entries: none
- Omitted private support records: 0

### Citations

- **PyTorch Gaudi Theory of Operations (docs.habana.ai 1.24.0)** (`pytorch-gaudi-theory-of-operations-docs-ha-cb112af`)
  - Locator: https://docs.habana.ai/en/latest/PyTorch/Reference/PyTorch_Gaudi_Theory_of_Operations.html
  - Support: "Eager mode with torch.compile (if enabled), is the default execution path, while Lazy mode is a legacy fallback that is no longer developed and will be deprecated"; table shows Lazy mode "Not supported" with public PyTorch and that public PyTorch support "is currently in preview mode, limited to Eager mode with torch.compile, and does not include a dedicated Docker image".
- **PyTorch Support Matrix (docs.habana.ai 1.24.0)** (`pytorch-support-matrix-docs-habana-ai-1-24-63feaf9`)
  - Locator: https://docs.habana.ai/en/latest/PyTorch/Reference/PyTorch_Support_Matrix.html
  - Support: HPU Graphs = Yes only in Lazy; torch.jit/TorchScript and ONNX = No; Pipeline Parallel/Distributed Elastic = No; Gloo/NCCL backends = No (HCCL used); torch.compile(backend="inductor") = No; Triton custom ops = No.

## gaudi2-install-prereqs

**Driver/software installation and host prerequisites for a Gaudi 2 node**

Documented: the recommended install path is habanalabs-installer.sh (vault.habana.ai/artifactory/gaudi-installer/<ver>/) with `install --type base`; a custom per-package path exists for fine-grained control, and the kernel must be updated before running the installer. The DKMS package installs habanalabs, habanalabs_cn, habanalabs_en (Ethernet), habanalabs_compat and habanalabs_ib. habanalabs-container-runtime (Docker and Kubernetes) and habanalabs-qual-workloads (qualification/stress, e.g. ResNet-50 stress plugin) are not installed automatically; habanalabs-tools is needed for TPC kernel authoring. Host preparation specifics: huge pages are configured automatically by the installer; IOMMU passthrough (iommu=pt intel_iommu=on) is required only for Ubuntu 24.04.2/22.04.5 on kernel 6.8; CPU governor must be set to performance on bare metal before starting containers;

- Kind: Claim
- Status: active
- Evidence: Documented
- Area: software-stack
- Document date: 2026-01-01
- Retrieved: 2026-09-25
- Scope: not separately stated
- Topics: driver, dkms, habanalabs-installer, container-runtime, huge-pages, iommu, nic-bring-up
- Basis Entries: none
- Omitted private support records: 0

### Citations

- **Driver and Software Installation (docs.habana.ai 1.24.0)** (`driver-and-software-installation-docs-haba-16261db`)
  - Locator: https://docs.habana.ai/en/latest/Installation_Guide/Driver_Installation.html
  - Support: Installer command `wget .../gaudi-installer/1.24.1/habanalabs-installer.sh` + `install --type base`; "habanalabs-container-runtime and habanalabs-qual-workloads are not automatically installed"; IOMMU passthrough only for Ubuntu 24.04.2/22.04.5 with kernel 6.8; manage_network_ifs.sh --up/--status with example output showing 3 ports up per accel device; env-var list and `source /etc/profile.d/habanalabs*.sh`.
- **Installation Guide and On-Premise System Update (docs.habana.ai 1.24.0)** (`installation-guide-and-on-premise-system-u-927100a`)
  - Locator: https://docs.habana.ai/en/latest/Installation_Guide/index.html
  - Support: Links hardware/network requirements, driver/software install, firmware upgrade, additional install per environment (bare metal, Docker, Kubernetes, OpenShift), system verification, and network configuration; notes driver install is not required when using the Intel Gaudi Base Operator.

## gaudi2-support-matrix-1241

**Gaudi 2 supported configuration in software release 1.24.1**

Documented (Support Matrix, Intel Gaudi Software 1.24.1 / build 1.24.1-482): Gaudi 2 is a first-class supported platform - Ubuntu 22.04.5 (Python 3.10) and 24.04.2 (3.12), RHEL 9.6 (3.12), TencentOS 3.1 (3.10), Navix 9.4 and 9.6 (3.12); kernels 5.15+ (Ubuntu 22.04), 6.8.0 (24.04.2) and 5.14.x (RHEL/TencentOS/Navix). Stack versions: Docker 29.1.5, PyTorch 2.11, lightning-habana 1.7.0, Ray 2.32.0, DeepSpeed fork of 0.14.4, Megatron-LM fork core_r0.11.0 (Gaudi 3 has core_r0.13.0), Intel Neural Compressor v3.8.1, OpenMPI 5.0.8, libfabric 1.16.1+/1.20.0 for Gaudi Direct with Verbs, Optimum for Intel Gaudi 1.21.0 with Transformers 4.55.4, Text Generation Inference 3.3.2, and vLLM Hardware Plugin for Intel Gaudi 0.24.0/0.26.0. On-prem component table: HL-225H SPI firmware and FIT 1.24.0-fw-62.6.2, CPLD 0x10, eROM >= 1.12.1-fw-46.0.5; HLBA-225 PCIe retimer 2.2 and SerDes retimer 0xD00A; HLS-Gaudi 2 BMC/PCIe-switch versions.

- Kind: Claim
- Status: active
- Evidence: Documented
- Area: software-stack
- Document date: 2026-01-01
- Retrieved: 2026-09-25
- Scope: not separately stated
- Topics: support-matrix, 1-24-1, os-support, pytorch-2-11, firmware, validation-policy
- Basis Entries: none
- Omitted private support records: 0

### Citations

- **Support Matrix (docs.habana.ai 1.24.x)** (`support-matrix-docs-habana-ai-1-24-x-19aeae0`)
  - Locator: https://docs.habana.ai/en/latest/Support_Matrix/Support_Matrix.html
  - Support: Gaudi 2 table: Intel Gaudi Software 1.24.1, Ubuntu 22.04.5/24.04.2 (Python 3.10/3.12), RHEL9 9.6 (3.12), TencentOS 3.1, Navix 9.4/9.6; Kubernetes 1.33-1.35; PyTorch 2.11; Ray 2.32.0; INC v3.8.1; Optimum for Intel Gaudi 1.21.0; TGI 3.3.2; vLLM Hardware Plugin 0.24.0, 0.26.0; "We perform validation only on the latest version and the two preceding versions."
- **Gaudi Release Notes (1.24.x)** (`gaudi-release-notes-1-24-x-2da618f`)
  - Locator: https://docs.habana.ai/en/latest/Release_Notes/GAUDI_Release_Notes.html
  - Support: v1.24.1 adds OCP 4.22/RHEL 9.8, drops RHEL 9.4, announces Slurm deprecation; v1.24.0 lists dropped OS support per accelerator (e.g. "OpenCloudOS on Intel Gaudi 3 and Intel Gaudi 2") and the Gaudi-2-only firmware note: "For Gaudi 2 only, firmware SPI version v1.21.2 and later are not compatible with Boot FIT v1.20.1 and earlier."

## gaudi2-vllm-coverage

**Serving via the vLLM Hardware Plugin for Intel Gaudi, and the narrowing Gaudi 2 validation coverage**

Documented: serving on Gaudi 2 is done through the community-maintained Apache-2.0 vLLM Hardware Plugin for Intel Gaudi (vllm-project/vllm-gaudi), built on vLLM's hardware-pluggable RFC; 0.26.0 pairs with upstream vLLM 0.26.0 and Intel Gaudi software 1.24.1 with PyTorch 2.11; 0.24.0 with 1.24.1/PyTorch 2.11; 0.19.0 with 1.24.0/PyTorch 2.10. Operational specifics: installation pins a saved "last good commit" of upstream vLLM because of recurring API drift; multi-card serving uses vLLM's `mp` backend when TP*PP*DP>1 and the platform forces VLLM_WORKER_MULTIPROC_METHOD=spawn because forking after HPU driver init can hang on exit. Validation scope:

- Kind: Claim
- Status: active
- Evidence: Documented
- Area: serving
- Document date: 2026-08-01
- Retrieved: 2026-09-25
- Scope: topology: not-stated
- Topics: vllm, validated-models, tensor-parallel, serving, upstream-drift
- Basis Entries: none
- Omitted private support records: 0

### Citations

- **Validated Models - vLLM Hardware Plugin for Intel Gaudi** (`validated-models-vllm-hardware-plugin-for-b3bb318`)
  - Locator: https://docs.vllm.ai/projects/gaudi/en/latest/getting_started/validated_models.html
  - Support: Table of validated configurations with per-row "Validated AI accelerator"; Gaudi 2 appears in 8 rows (Granite-20B-code, Meta-Llama-3.1-8B/-8B-Instruct, Meta-Llama-3.1-70B/-70B-Instruct, Mistral-Large-Instruct-2407, Mixtral-8x7B-Instruct-v0.1, Qwen2-72B-Instruct) while Meta-Llama-3.3-70B-Instruct, Meta-Llama-3.1-405B, gpt-oss and Qwen3-VL rows are Gaudi 3 only.
- **vllm-project/vllm-gaudi README** (`vllm-project-vllm-gaudi-readme-9453bcc`)
  - Locator: https://github.com/vllm-project/vllm-gaudi
  - Support: Release history: 0.26.0 on vLLM 0.26.0 + Intel Gaudi v1.24.1/PyTorch 2.11 (2026/08); 0.24.0 on vLLM 0.24.0 + v1.24.1/PyTorch 2.11; 0.19.0 on vLLM 0.19.0 + v1.24.0/PyTorch 2.10; installation via saved VLLM_STABLE_COMMIT; multi-card path uses vLLM `mp` backend and HPU overrides VLLM_WORKER_MULTIPROC_METHOD to spawn ("forking after HPU driver initialization leaves driver state in child processes and can cause hangs on exit").

## gaudi2-reliability-observability

**Reliability and observability surface on Gaudi 2 (hl-smi, ECC, row replacement, throttling) plus known hardware/firmware constraints**

Documented: hl-smi / HLML is the management surface. Per-device queryable fields include ECC counters (uncorrected and corrected, aggregate since driver load and volatile since fd open, DRAM/uncorrected-HBM counts, hbm-sram-critical), ECC mode current/pending, address-level row replacement with cause (e.g. "Single Bit ECC", "Double Bit ECC") plus a pending flag, power/thermal throttling violation durations, power draw vs cap (with the caveat that -Q power.draw reflects only the 54 V rail while the summary Pwr figure combines 54 V and 12 V), power-limit setting, device reset (-r, requires root and -i), NIC port inventory and link/stat state (internal vs external ports), temperature from four SoC sensors, utilization and memory used/free/total, plus row-replacement and TPM attestation queries; hl-smi topo reports CPU and NUMA affinity, and hl_qual provides platform qualification/stress tooling (habanalabs-qual-workloads).

- Kind: Claim
- Status: active
- Evidence: Documented
- Area: reliability
- Document date: 2026-01-01
- Retrieved: 2026-09-25
- Scope: not separately stated
- Topics: ecc, row-replacement, throttling, hl-smi, hl-qual, firmware-compatibility
- Basis Entries: none
- Omitted private support records: 0

### Citations

- **System Management Interface Tool (hl-smi) - docs.habana.ai 1.24.0** (`system-management-interface-tool-hl-smi-do-d69bb54`)
  - Locator: https://docs.habana.ai/en/latest/Management_and_Monitoring/Embedded_System_Tools_Guide/System_Management_Interface_Tool.html
  - Support: Query list includes ecc.errors.uncorrected/corrected aggregate+volatile, ecc.errors.dram*, ecc.errors.hbm.sram.critical, ecc.mode.current/pending, stats.violation.power/thermal, power.draw, --reset-aip, -n/--nic ports|link|stats, and --query-row-replacement with replaced_rows.address/cause; row-replacement example shows causes "Single Bit ECC" and "Double Bit ECC"; note that -Q power.draw covers the 54 V rail only while hl-smi Pwr combines 54 V and 12 V.
- **Gaudi Release Notes (1.24.x)** (`gaudi-release-notes-1-24-x-2da618f`)
  - Locator: https://docs.habana.ai/en/latest/Release_Notes/GAUDI_Release_Notes.html
  - Support: Known issues: "For Gaudi 2 only, firmware SPI version v1.21.2 and later are not compatible with Boot FIT v1.20.1 and earlier"; "Running functional test in high power mode experiences a performance failure with an 8.5% degradation"; Ubuntu kernel 6.8 IOMMU-passthrough requirement; "Model checkpointing for ResNet50 in torch.compile mode is broken"; "To bypass a performance issue in Linux kernel version >= 5.9... the intel_idle driver must be disabled by adding intel_idle.max_cstate=0".

## gaudi2-history-lifecycle

**Provenance and current lifecycle status: Habana acquisition, launch dates, and evidence that Gaudi 2 is maintained but no longer the enablement frontier**

Documented history: Habana Labs (founded 2016 per Intel's launch material) announced the first-gen Gaudi AI training processor on 2019-06-17; Intel acquired Habana Labs on 2019-12-12 for total consideration of $1.7 billion (Intel FY2019 Form 10-K); Gaudi 2 was launched 2022-05-10 at Intel Vision with 7nm/24 TPC/96 GB HBM2e and 24x100 GbE, demonstrated ~2x A100-80GB training throughput on ResNet-50 and BERT per Intel's own material, and was later stated to have started shipping in volume and on the Intel Developer Cloud in June 2023; Gaudi 3 was introduced 2024-04-09 at Intel Vision (available to OEMs Q2 2024) with the claim of "4x more AI compute for BF16 and a 1.5x increase in memory bandwidth over its predecessor".

- Kind: Claim
- Status: active
- Evidence: Documented
- Area: software-stack
- Document date: 2024-04-09
- Retrieved: 2026-09-25
- Scope: not separately stated
- Topics: history, habana-acquisition, launch-timeline, lifecycle, synapseai-core-archived, roadmap
- Basis Entries: none
- Omitted private support records: 0

### Citations

- **Habana Labs Launches Gaudi2 Deep Learning Training Processor (fact sheet, 2022-05-10)** (`habana-labs-launches-gaudi2-deep-learning-26d6679`)
  - Locator: https://download.intel.com/newsroom/2022/corporate/vision/Habana-Gaudi2-Launch-Fact-Sheet.pdf
  - Support: "May 10, 2022 - Today at the Intel Vision conference, Habana Labs, an Intel company, launched the Gaudi2 processor, its second-generation Gaudi processor for training"; "Habana Labs... is a leading AI Processor company founded in 2016"; "one thousand HLS-Gaudi2s have been deployed in the Habana Gaudi2 data centers in Israel".
- **Gaudi Release Notes (1.24.x)** (`gaudi-release-notes-1-24-x-2da618f`)
  - Locator: https://docs.habana.ai/en/latest/Release_Notes/GAUDI_Release_Notes.html
  - Support: 1.24.1 shipped 2026 with security fixes and a stated plan for 1.24.2; still lists Gaudi 2 OS support changes (drops RHEL 9.4; keeps TencentOS on Gaudi 2) - evidence the platform is maintained but on a legacy-skewed track.

## install-pinned-source-build

**Source installation is pin-locked to a validated upstream vLLM commit**

Documented install flow requires three coupled steps: (1) read the validated upstream commit from the `vllm/last-good-commit-for-vllm-gaudi` branch (`VLLM_STABLE_COMMIT`), (2) build upstream vLLM for the empty platform (`VLLM_TARGET_DEVICE=empty pip install --no-build-isolation -e .`) so the existing Habana PyTorch build is reused, and (3) `pip install -e .` the plugin. torchaudio must be installed separately with `--no-deps` from the PyTorch CPU index to avoid pulling a CUDA torch, because some upstream models (Qwen3.5) need it. Requirements are Python 3.10, Gaudi 2 or 3, and a matching Gaudi software version. The pin exists because the plugin tracks upstream vLLM commits and upstream API drift routinely breaks it.

- Kind: Claim
- Status: active
- Evidence: Documented
- Area: software-stack
- Document date: 2026-08-06
- Retrieved: 2026-09-25
- Scope: not separately stated
- Topics: installation, build-from-source, version-pinning, upstream-compatibility, torchaudio
- Basis Entries: none
- Omitted private support records: 0

### Citations

- **README – Getting Started** (`readme-getting-started-dafee48`)
  - Locator: https://github.com/vllm-project/vllm-gaudi/blob/main/README.md
  - Support: Steps export VLLM_COMMIT_HASH from the last-good-commit branch, build vLLM with VLLM_TARGET_DEVICE=empty, then pip install -e . the plugin; documents the torchaudio --no-deps CPU-wheel workaround.
- **update-stable-commit workflow** (`update-stable-commit-workflow-7cb0fbc`)
  - Locator: https://github.com/vllm-project/vllm-gaudi/blob/main/.github/workflows/update-stable-commit.yaml
  - Support: Automation that maintains the VLLM_STABLE_COMMIT value consumed by the documented install flow.

## version-compatibility-matrix

**Compatibility matrix pins one plugin release to one vLLM version and one Gaudi software version**

Documented support is a strict pairing, not a range: the latest validated release is vLLM v0.26.0 on Intel Gaudi software v1.24.1 (PyTorch 2.11); vLLM 0.24.0 also maps to 1.24.1, 0.19.x/0.21.0 map to 1.24.0, 0.13.0–0.16.0 map to 1.23.0, and 0.10.1 was Beta on 1.22.1. Branch names encode the same policy (`vllm/last-good-commit-for-vllm-gaudi`, `releases/v0.x.y`), so upgrades require moving both the plugin and the Gaudi software stack together.

- Kind: Claim
- Status: active
- Evidence: Documented
- Area: software-stack
- Document date: 2026-08-06
- Retrieved: 2026-09-25
- Scope: not separately stated
- Topics: compatibility, release-cadence, gaudi-software, pytorch, upgrade-path
- Basis Entries: none
- Omitted private support records: 0

### Citations

- **Compatibility Matrix** (`compatibility-matrix-5fad2ba`)
  - Locator: https://docs.vllm.ai/projects/gaudi/en/latest/getting_started/compatibility_matrix.html
  - Support: Table maps each vLLM version to exactly one supported Gaudi software version and states the latest validated pair as vLLM v0.26.0 / Gaudi 1.24.1.
- **v0.26.0 release notes** (`v0-26-0-release-notes-ffa3b49`)
  - Locator: https://docs.vllm.ai/projects/gaudi/en/latest/release_notes_v0.26.0.html
  - Support: Confirms the release is based on upstream vLLM v0.26.0 and supports Gaudi Software v1.24.1 with PyTorch 2.11.

## validated-models-gaudi3-centric

**Validated model list is broad but Gaudi 3-centric, with a much smaller Gaudi 2 subset**

The validated list contains ~55 model/TP/dtype/accelerator rows covering Llama 3.1/3.3, Mistral, Mixtral, Qwen2.5/3/3.5/3.6, Gemma-4, GPT-OSS (20B/120B), Granite 3.x/4.0-h, MiniMax-M2/M3, DeepSeek-R1-Distill and VL models. Most rows are Gaudi 3 with BF16, and FP8 rows are paired with specific TP sizes. Only a small minority of rows are marked valid on Gaudi 2 — approximately Granite-20B-code (BF16/FP8), Meta-Llama-3.1-8B/-Instruct (BF16/FP8), Meta-Llama-3.1-70B/-Instruct (2/4/8 HPU, BF16/FP8), Mistral-Large-Instruct-2407, Mixtral-8x7B (FP8/BF16), Qwen2-72B-Instruct, and Qwen3-30B-A3B-Instruct-2507. The docs explicitly warn unlisted configurations may work but are untested.

- Kind: Claim
- Status: active
- Evidence: Documented
- Area: model-support
- Document date: 2026-08-06
- Retrieved: 2026-09-25
- Scope: not separately stated
- Topics: validated-models, gaudi-2, gaudi-3, tensor-parallelism, bf16, fp8
- Basis Entries: none
- Omitted private support records: 0

### Citations

- **README – Getting Started** (`readme-getting-started-dafee48`)
  - Locator: https://github.com/vllm-project/vllm-gaudi/blob/main/README.md
  - Support: Adds MiniMax-M3, Gemma-4 family, Kimi-K2.5 vision tower, and Qwen3-Coder-Next as newly supported models in v0.26.0.
- **Validated Models - vLLM Hardware Plugin for Intel Gaudi** (`validated-models-vllm-hardware-plugin-for-b3bb318`)
  - Locator: https://docs.vllm.ai/projects/gaudi/en/latest/getting_started/validated_models.html
  - Support: Table of model, TP size, datatype, and validated accelerator; Gaudi 2 appears only on a small subset of rows while Gaudi 3 dominates.

## supported-and-experimental-features

**Feature surface is wide, but several headline capabilities are explicitly experimental or planned**

Documented as supported: offline/online OpenAI-compatible serving, HPU autodetection, custom paged attention/operators, tensor parallel inference, HPU Graphs, `torch.compile` (default), INC/AWQ/GPTQ quantization, LoRA/MultiLoRA, automatic prefix caching (on by default), multiprocessing backend, multimodal, guided decoding, data parallel, configurable bucketing (exp/lin/pad), and row-parallel chunking. Experimental: runtime scale patching (up to 90% FP8 warm-up reduction but 5–20% throughput cost, Llama-only, no MoE), trivial-scales optimization, dynamic MatMul/KV quantization, and single-process model swap (requires VLLM_SERVER_DEV_MODE and insecure serialization). Explicitly planned: sliding window attention, P/D disaggregate support, in-place weight update, multinode support, and pipeline parallel inference. Multi-step scheduling and delayed sampling are discontinued in favor of async scheduling.

- Kind: Claim
- Status: active
- Evidence: Documented
- Area: software-stack
- Document date: 2026-08-06
- Retrieved: 2026-09-25
- Scope: not separately stated
- Topics: feature-matrix, experimental-features, planned-features, async-scheduling, prefix-caching
- Basis Entries: none
- Omitted private support records: 0

### Citations

- **Supported Features** (`supported-features-b1973ea`)
  - Locator: https://docs.vllm.ai/projects/gaudi/en/latest/features/supported_features.html
  - Support: Contains the supported/experimental/planned/discontinued tables; notes INC quantization is not fully supported under torch.compile and multimodal is not fully supported under t.compile, and lists expected 5–10% speedup for the fully async executor.
- **Single-Process Model Swap architecture** (`single-process-model-swap-architecture-f33eda2`)
  - Locator: https://docs.vllm.ai/projects/gaudi/en/latest/design/single_process_model_swap_arch_overview.html
  - Support: Documents the multi-model server entrypoint, drain-and-reconfigure switch flow, and the cloudpickle-based in-process config transfer requiring VLLM_ALLOW_INSECURE_SERIALIZATION=1.

## bucketing-and-continuous-batching

**Continuous batching is expressed through shape bucketing over batch/query/context-block dimensions**

Gaudi graph compilation is sensitive to input shapes, so the plugin pads forward passes into pre-warmed buckets across three dimensions — batch size, query length, and context length in blocks — generated separately for prompt and decode phases. Default strategy is exponential (`VLLM_BUCKETING_STRATEGY=exp`, min/step/max/limit); `lin` and `pad` (with PAD_MAX/PAD_PERCENT) trade warm-up cost against runtime padding. Bucketing is transparent: sequence-length padding is never returned to users and batch padding does not create requests. Requests exceeding an upper bucket boundary are executed unpadded and can force graph compilation, causing large latency spikes — the docs explicitly warn to raise bucket maxima for long-context workloads.

- Kind: Claim
- Status: active
- Evidence: Documented
- Area: performance
- Document date: 2026-08-06
- Retrieved: 2026-09-25
- Scope: topology: not-stated
- Topics: continuous-batching, bucketing, padding, graph-recompilation, latency
- Basis Entries: none
- Omitted private support records: 0

### Citations

- **Bucketing Mechanism** (`bucketing-mechanism-abe7712`)
  - Locator: https://docs.vllm.ai/projects/gaudi/en/latest/features/bucketing_mechanism.html
  - Support: Defines the three bucketing dimensions, the exp/lin/pad strategies with worked examples, and the warning that exceeding the maximum bucket size may require a graph compilation that significantly increases end-to-end latency.
- **Warm-up – HPU Graph Capture** (`warm-up-hpu-graph-capture-90e83ee`)
  - Locator: https://docs.vllm.ai/projects/gaudi/en/latest/features/warmup.html
  - Support: Describes the scheduler filling maximum decode batch size and scheduling prefill iterations from the waiting queue to restore batch size when requests complete, making large-batch decode graphs critical to capture.

## warmup-graph-cache-cost

**Warm-up and graph capture dominate startup time and compete with KV cache for device memory**

Warm-up runs a forward pass per bucket before the server listens; warm-up time can reach hours depending on bucket count and dtype. HPU graph recipes can be cached with PT_HPU_RECIPE_CACHE_CONFIG: documented measurements for Llama 3.1 8B show BF16 dropping from 66 s to 23 s (~65% faster) and FP8 from 504 s to 34 s (~93% faster). Memory is a shared pool between KV cache and HPU graphs; `gpu_memory_utilization` applies only to memory free after weight load plus a profiling pass, and `VLLM_GRAPH_RESERVED_MEM` (default 0.1) reserves part of that for graph capture. FP8 models need higher engine/RPC timeouts because of long compile times, and `VLLM_SKIP_WARMUP=true` is documented as development-only because it defers compilation to first real requests.

- Kind: Claim
- Status: active
- Evidence: Documented
- Area: performance
- Document date: 2026-08-06
- Retrieved: 2026-09-25
- Scope: topology: not-stated
- Topics: warm-up, hpu-graphs, recipe-cache, kv-cache-memory, gpu-memory-utilization
- Basis Entries: none
- Omitted private support records: 0

### Citations

- **Managing and Reducing Warm-up Time** (`managing-and-reducing-warm-up-time-8b71886`)
  - Locator: https://docs.vllm.ai/projects/gaudi/en/latest/configuration/warm-up/managing_warm-up.html
  - Support: Provides the PT_HPU_RECIPE_CACHE_CONFIG format and the BF16 66→23 s / FP8 504→34 s reduction table, plus cache-invalidation conditions (container/Gaudi version, platform, TP or dtype change).
- **Warm-up – HPU Graph Capture** (`warm-up-hpu-graph-capture-90e83ee`)
  - Locator: https://docs.vllm.ai/projects/gaudi/en/latest/features/warmup.html
  - Support: Explains that graph capture shares the usable-memory pool with KV cache and documents the gpu_memory_utilization/VLLM_GRAPH_RESERVED_MEM interaction with sample startup logs.

## quantization-backends-and-calibration

**Quantization support is INC FP8 plus INT4 AWQ/GPTQ, with device-bound calibration and MoE unification caveats**

Three backends are documented: Intel Neural Compressor (FP8 weights and activations plus fp8_inc KV cache, requires prior calibration producing a QUANT_CONFIG JSON), AutoAWQ, and GPTQModel (INT4/INT8). Key operational constraints: FP8 inference requires calibration on the same device type as inference because scale measurements are device-dependent (Gaudi 2 scales cannot be reused on Gaudi 3 and vice versa); the INC guide states quantization is currently validated only on Llama models; FP8 compile time can cause server/RPC timeouts that must be raised; and when calibrating MoE models with expert parallelism, each rank only measures its local experts, so `-u` must be paired with `-r` to unify scales or FP8 accuracy degrades. Runtime scale patching can cut FP8 warm-up by up to 90% but costs 5–20% throughput and is unsupported for MoE/convolution.

- Kind: Claim
- Status: active
- Evidence: Documented
- Area: quantization
- Document date: 2026-08-06
- Retrieved: 2026-09-25
- Scope: not separately stated
- Topics: fp8, inc, calibration, awq, gptq, moe, kv-cache-quantization
- Basis Entries: none
- Omitted private support records: 0

### Citations

- **Quantization and Inference (overview)** (`quantization-and-inference-overview-ed22838`)
  - Locator: https://docs.vllm.ai/projects/gaudi/en/latest/configuration/quantization/quantization.html
  - Support: Lists the three supported backends: Intel Neural Compressor, Auto_Awq, and Gptqmodel.
- **Intel Neural Compressor guide** (`intel-neural-compressor-guide-5db0d37`)
  - Locator: https://docs.vllm.ai/projects/gaudi/en/latest/configuration/quantization/inc.html
  - Support: States FP8 weight/activation quantization on Gaudi 2 and 3, that quantization is validated only on Llama models today, the device-dependence of measurements, and the compile-timeout environment variables.

## distributed-backends-and-multinode-limits

**Single-node multi-card serving is the validated distributed path; Ray multi-node is explicitly unvalidated and PP is not fully supported**

On HPU the auto-selected backends are `uni` at world_size 1 and `mp` for TP*PP*DP > 1; `mp` is documented as the recommended production backend for single-node multi-card serving, and the worker start method is force-overridden from `fork` to `spawn` because forking after HPU driver initialization can hang on exit. The env-variable reference states plainly that 'Multi-node serving with Ray on Gaudi has not yet been validated by the Gaudi software product engineering team.' The pipeline-parallelism page says full support is coming in an upcoming release, and the supported-features page still lists both 'Multinode support' and 'Pipeline parallel inference' as planned. A separate multi-node page gives a Ray procedure but opens with 'This feature will be introduced in a future release' and points at the legacy HabanaAI vllm-fork / vllm-hpu-extension calibration docs.

- Kind: Claim
- Status: active
- Evidence: Documented
- Area: distributed
- Document date: 2026-08-06
- Retrieved: 2026-09-25
- Scope: not separately stated
- Topics: distributed-inference, tensor-parallelism, pipeline-parallelism, ray, multiprocessing, spawn
- Basis Entries: none
- Omitted private support records: 0

### Citations

- **README – Getting Started** (`readme-getting-started-dafee48`)
  - Locator: https://github.com/vllm-project/vllm-gaudi/blob/main/README.md
  - Support: Documents mp default for world_size>1, uni for world_size==1, and the automatic fork→spawn override with its HPU-driver rationale.
- **Configuration – Distributed Executor Backend on HPU** (`configuration-distributed-executor-backend-a6a76d2`)
  - Locator: https://docs.vllm.ai/projects/gaudi/en/latest/configuration/env_variables.html
  - Support: Describes mp/uni/external_launcher/ray, the forced spawn override, and states Ray multi-node on Gaudi 'has not yet been validated'; recommends mp for production.

## sparse-attention-and-hybrid-gdn-limits

**Known hard edges: sparse attention is unsupported, hybrid GDN long-context is fragile, and low-batch MoE decode is slow**

Three documented/reported limitations recur in the issue tracker. (1) Sparse attention is not implemented on HPU — loading GLM-5.x DSA models raises 'NotImplementedError: Sparse Attention is not supported on HPU'; the working path is a dense-MLA fallback (PR #1664), which changes the intended sparse execution model. (2) Hybrid GDN (GatedDeltaNet) + FullAttention models are unreliable at 262K context: issue #1734 reports a Synapse graph-compilation failure (synStatus 26) on the first request in v0.26.0 that does not occur in v0.24.0, and issue #1736 reports warm-up memory miscalculation where GDN state scales with block count and leaves ~18 GiB for 300+ warm-up buckets that need ~20–30 GiB peak. (3) MoE decode at low batch size is slow on Gaudi 2 — roughly 20 tok/s for several Qwen3.5/3.6 MoE and MiniMax M2.7-class models at BS=1.

- Kind: Claim
- Status: active
- Evidence: Unverified
- Area: reliability
- Document date: 2026-08-13
- Retrieved: 2026-09-25
- Scope: not separately stated
- Topics: sparse-attention, dsa, gated-deltanet, hybrid-models, oom, graph-compilation, moe, low-batch-decode
- Basis Entries: none
- Omitted private support records: 0

### Citations

- **Issue #1549 – GLM-5 sparse attention failure** (`issue-1549-glm-5-sparse-attention-failure-d96481b`)
  - Locator: https://github.com/vllm-project/vllm-gaudi/issues/1549
  - Support: User reports GLM-5.2 failing on vllm-gaudi 0.21 with 'NotImplementedError: Sparse Attention is not supported on HPU', and a later comment documents the dense-MLA workaround and its throughput.
- **Issue #1734 – Synapse graph compilation failure with hybrid GDN on v0.26.0** (`issue-1734-synapse-graph-compilation-failu-3dabd80`)
  - Locator: https://github.com/vllm-project/vllm-gaudi/issues/1734
  - Support: Repro with ThinkingCap-Qwen3.6-27B-FP8, TP=4, 262144 context, fp8_inc KV: synStatus 26 graph compile failure on first request on v0.26.0 while the same config works on v0.24.0.

## active-research-moe-gather-and-serving

**Active research: low-batch FP8 MoE gather-combine, single-process model swap, and experimental disaggregated serving**

The most concrete active optimization is a custom gathered-expert FP8 MoE combine for silu + per-channel FP8 weights, exposed as experimental env vars (VLLM_HPU_MOE_GATHER off by default, VLLM_HPU_MOE_GATHER_RATIO default 0.4 derived from a Qwen 3.5 MoE crossover sweep, VLLM_HPU_MOE_GATHER_VERIFY for in-memory ULP comparison). It is credited with roughly 2x Qwen 3.6 35B-A3B BS=1 decode, ~2x Qwen3.5-122B and ~1.5x Qwen3.5-397B, derived from the earlier MiniMax-M3 gather work in #1673. Other in-flight directions: single-process model swap for sequential multi-model serving (documented architecture, requires dev-mode/insecure serialization), GDN compact state and Mamba/hybrid prefix caching, TPC custom kernels, MLA variants (qk_rope_head_dim == 0), Nemotron-H WNA16, and RoPE numerical fixes for very long contexts.

- Kind: Claim
- Status: active
- Evidence: Author-validated
- Area: distributed
- Document date: 2026-09-25
- Retrieved: 2026-09-25
- Scope: not separately stated
- Topics: moe-gather, fp8, single-process-model-swap, disaggregated-serving, nixl, lmcache, gdn, tpc-kernels
- Basis Entries: none
- Omitted private support records: 0

### Citations

- **PR #1731 – custom gathered-expert MoE combine for silu/FP8** (`pr-1731-custom-gathered-expert-moe-combine-35e7317`)
  - Locator: https://github.com/vllm-project/vllm-gaudi/pull/1731
  - Support: Reports ~2x at BS=1 for Qwen 3.6 35B-A3B, nearly 2x for Qwen3.5-122B, 1.5x for 397B, with diminishing gains up to BS≈8; based on PR #1673 for MiniMax M3.
- **LMCache examples README** (`lmcache-examples-readme-84542c6`)
  - Locator: https://github.com/vllm-project/vllm-gaudi/blob/main/examples/lmcache/README.md
  - Support: Documents disaggregated prefill (LMCache server or external Redis) and KV-cache sharing examples, requiring at least 2 HPU cards; launcher script itself prints that LMCache disaggregated prefill for vLLM v1 is experimental.

## gaudi2-repo-scope-and-baseline

**1CatAI/1Cat-vLLM-Gaudi is a Gaudi2-focused engineering branch of the vLLM-Gaudi plugin, with a frozen documented baseline commit**

Repository metadata: created 2026-08-29, Apache-2.0, not a GitHub-declared fork (no parent, isFork=false), 26 stars / 7 forks, 1,687 tracked paths, main tip f65d92227e43da2c2f98910420cb9ac98cf7c4c0 (committed 2026-09-25). README describes the project as 1CatAI's engineering branch of the vLLM-Gaudi hardware plugin ('vLLM-Gaudi 硬件插件工程分支'), requiring a matching vLLM engine, with Gaudi2 as the primary optimization target; inherited AGENTS.md still documents vllm_gaudi as a vLLM plugin package rather than a vLLM fork. The README pins the merged source baseline to 5fa3e08302716d458a82aa7d95d107e201b51d8c (PR #34, merged 2026-09-20) and states that no hardware tests were re-run for the README merge (README footer: '本次未运行硬件测试'). Declared scope lines: Qwen (GDN, DFlash2), DeepSeek V4 / V4.1 (incl. DSpark), MiniMax M3 model registration and MiniMax H3 omni; 167 C TPC kernel sources exist under csrc/deepseek_v4/kernels (README claims '100 余个').

- Kind: Claim
- Status: active
- Evidence: Documented
- Area: hardware
- Document date: 2026-09-25
- Retrieved: 2026-09-25
- Scope: not separately stated
- Topics: repository-scope, vllm-gaudi, gaudi2, baseline-commit, license, release-status
- Basis Entries: none
- Omitted private support records: 0

### Citations

- **README.md (main tip f65d9222)** (`readme-md-main-tip-f65d9222-a7dd966`)
  - Locator: https://github.com/1CatAI/1Cat-vLLM-Gaudi/blob/f65d92227e43da2c2f98910420cb9ac98cf7c4c0/README.md
  - Support: States 1CatAI maintains this as a vLLM-Gaudi hardware-plugin engineering branch requiring a matching vLLM engine; targets Gaudi2; footer pins baseline 5fa3e08302716d458a82aa7d95d107e201b51d8c (main / PR #34), merge date 2026-09-21, and says no hardware tests were run for this merge.
- **AGENTS.md (main)** (`agents-md-main-4fd2060`)
  - Locator: https://github.com/1CatAI/1Cat-vLLM-Gaudi/blob/main/AGENTS.md
  - Support: Documents the package as 'vllm-gaudi - the vLLM Hardware Plugin for Intel Gaudi AI accelerators. It is a plugin package (not a fork)' integrating HPUs via the vLLM plugin architecture; lists subsystem layout (vllm_gaudi/ops, models, attention, extension, v1, distributed).

## qwen38-fp8-a800-vs-gaudi2-record

**Qwen3.8-27B-FP8: archived A800-vs-Gaudi2 record shows shorter TTFT at all tested concurrencies, but a 3.3% decode-throughput deficit at 32 concurrency**

The repository transcribes an existing measurement record (screenshot-sourced, not re-run) for Qwen3.8-27B-FP8 with 2,048 input tokens per request at concurrency 1/8/16/32. Gaudi2 (TP1) TTFT: 0.4036 / 2.9354 / 5.8028 / 11.6282 s versus A800 0.7739 / 5.7206 / 9.8716 / 16.5182 s, i.e. 47.8% / 48.7% / 41.2% / 29.6% shorter first-token latency. Decode total throughput: Gaudi2 57.17 / 380.25 / 644.21 / 958.44 tokens/s versus A800 48.64 / 342.11 / 614.62 / 991.44 tokens/s, i.e. +17.5% / +11.1% / +4.8% / -3.3%. The page states explicitly that derived 'inferred prefill' (2,048 x concurrency / TTFT) is an input-rate estimate, that the two sides' TTFT statistic definitions are not fully aligned, that output length, sampling, Decode timing window, full software versions and measurement date are all unprovided, and that the differences must not be attributed to GDN, DFlash2, or any specific kernel.

- Kind: Claim
- Status: active
- Evidence: Unverified
- Area: performance
- Document date: 2026-09-15
- Retrieved: 2026-09-25
- Scope: topology: single-card; model: Qwen3.8-27B; precision: FP8
- Topics: qwen3-8, 27b, fp8, ttft, decode-throughput, a800-comparison, benchmark-provenance
- Basis Entries: none
- Omitted private support records: 0

### Citations

- **docs/benchmarks/qwen38-a800-gaudi2.md** (`docs-benchmarks-qwen38-a800-gaudi2-md-dacc38d`)
  - Locator: https://github.com/1CatAI/1Cat-vLLM-Gaudi/blob/5fa3e08302716d458a82aa7d95d107e201b51d8c/docs/benchmarks/qwen38-a800-gaudi2.md
  - Support: Raw and derived tables with the eight TTFT/decode pairs, the derivation formulas, the condition table marking versions, output length, sampling, Decode window and measurement date as '未提供', and the reading guidance that inferred prefill is only an input-rate estimate and must not be attributed to specific optimizations.
- **docs/benchmarks/qwen38-a800-gaudi2.json** (`docs-benchmarks-qwen38-a800-gaudi2-json-24f3cfd`)
  - Locator: https://github.com/1CatAI/1Cat-vLLM-Gaudi/blob/5fa3e08302716d458a82aa7d95d107e201b51d8c/docs/benchmarks/qwen38-a800-gaudi2.json
  - Support: Structured record referenced by the markdown; the doc states it stores the source screenshot's SHA-256 so the source file can be checked for modification.

## deepseek-v41-full-accel-evidence-bundle

**DeepSeek V4.1 unified full-acceleration run: 81.347 tokens/s mean with an in-repository evidence bundle and explicit lifecycle checks**

PR #36 and its archived evidence directory record the strongest performance figure in the repository with retained data: 4xGaudi2, TP2xPP2, DSpark off, max model length 1,048,576, max batched tokens 8,192, max sequences 32, KV block size 128, 8,193 blocks, 2,048 input + 256 output tokens, greedy, first ten ITLs discarded. Three rounds measured 12.276568 / 12.300522 / 12.301963 ms/token; mean 12.293018 ms/token (81.347 tokens/s); a post-repair B1 confirmation measured 12.307399 ms/token. The same bundle records 8/8 generation smoke cases with natural EOS, a 1,237-token long generation without repetition or invalid Unicode, 2/2 B2 concurrent requests after restricting V2 asynchronous continuation to single-request scheduler steps, a streaming-cancellation-then-recovery request, and public-gateway model discovery/non-streaming/streaming/B2 checks with backend health HTTP 200.

- Kind: Claim
- Status: active
- Evidence: Author-validated
- Area: performance
- Document date: 2026-09-21
- Retrieved: 2026-09-25
- Scope: topology: tp2-pp2; model: DeepSeek V4.1
- Topics: deepseek-v4-1, serving, itl, throughput, evidence-bundle, b2-concurrency, gateway
- Basis Entries: none
- Omitted private support records: 0

### Citations

- **evidence/20260921_dsv41-unified-full-accel-e2e/REPORT.md** (`evidence-20260921-dsv41-unified-full-accel-067d5c1`)
  - Locator: https://github.com/1CatAI/1Cat-vLLM-Gaudi/blob/d0266b69960c87e23fd20a74edf970a61e8fc1dd/evidence/20260921_dsv41-unified-full-accel-e2e/REPORT.md
  - Support: Dated 2026-09-21, hardware 4 x Gaudi2 TP2xPP2 DSpark off, full service configuration, the four timing values plus mean, functional/lifecycle checklist, and the two fixes made during unified validation (V2 async completion only for single-request steps; gateway port/SSE/client-disconnect handling).
- **Pull request #36** (`pull-request-36-83aa20d`)
  - Locator: https://github.com/1CatAI/1Cat-vLLM-Gaudi/pull/36
  - Support: Promotes the validated V4.1 full-acceleration bundle to the dedicated entrypoint and reports the same 12.293018 ms/token mean (81.347 tokens/s), 62 tests passed / 3 skipped, 8/8 generation smoke cases, 1,237-token long generation, B2 concurrency and cancellation-recovery results, and points to the raw records under evidence/20260921_dsv41-unified-full-accel-e2e/.

## flashinfer-gaudi-qwen-stack

**FlashInfer-Gaudi package, Qwen GDN acceleration, DFlash2 speculative decoding and a Qwen3.5 FP8 quality repair form the Qwen execution stack on Gaudi2**

The repository ships an independently namespaced flashinfer_gaudi package whose public surface follows FlashInfer 0.6.18 for chunk_gated_delta_rule, gated_delta_rule_decode_pretranspose, gated_delta_rule_decode, gated_delta_rule_mtp and gdn_fused_decode_step, with Gaudi extensions (GDN prefill/decode, fused decode, activation/quant/norm fusion, block-FP8 linear). The prefill tactic is shape-gated to BF16 Hq=Hk=16/Hv=48 (TP1) or rank-local 8/24 (TP2), K=V=128, chunk 128, one uniform sequence, and keeps FP32 recurrent state; the prefill graph stays FP32 with BF16 bulk math described as still-research. Measured results attributed to this route on Qwen3.8-27B-FP8, one Gaudi2, TP1 (PR #4, vs the previous vLLM-Gaudi GDN route): GDN prefill operator throughput 2.3-2.8x, single-request TTFT 1.34-1.47x, steady decode 1.25-1.92x, full-request throughput 1.27-1.55x, plus roughly 0.4-0.8% more from the fused decode step.

- Kind: Claim
- Status: active
- Evidence: Author-validated
- Area: software-stack
- Document date: 2026-09-14
- Retrieved: 2026-09-25
- Scope: not separately stated
- Topics: flashinfer-gaudi, gdn, qwen3-8, qwen3-5, dflash2, speculative-decoding, fp8-quality
- Basis Entries: none
- Omitted private support records: 0

### Citations

- **docs/features/flashinfer_gaudi.md** (`docs-features-flashinfer-gaudi-md-af3b8f2`)
  - Locator: https://github.com/1CatAI/1Cat-vLLM-Gaudi/blob/5fa3e08302716d458a82aa7d95d107e201b51d8c/docs/features/flashinfer_gaudi.md
  - Support: Declares the FlashInfer 0.6.18-aligned public surface, the GDN prefill shape gates and TP2 opt-in, native/public/bridge strict policies that reject partial native prototypes, the FP32 prefill graph, the decode-sized dynamic FP8 quantization cap (32 rows default, VLLM_HPU_CGUID_DYNAMIC_QUANT_MAX_ROWS) and the fused direct-state buckets 1/2/4/8/16/32.
- **Pull request #4** (`pull-request-4-ab68028`)
  - Locator: https://github.com/1CatAI/1Cat-vLLM-Gaudi/pull/4
  - Support: Reports the operator/TTFT/decode/full-request multipliers on Qwen3.8-27B-FP8 TP1 single Gaudi2, the 187 passed / 1 expected-failure test list, the five-run same-card A/B, and discloses that a reverse-order control was lost to a driver-level device-acquisition failure with no partial result used.

## tp2-reduction-fusion-and-correctness

**Qwen TP2 gains came from fusing the AllReduce/residual/RMSNorm boundary, after a silent missing-collective bug in deferred reductions was fixed first**

PR #5 fuses the dense Qwen3 TP2 all-reduce, residual add and RMSNorm into one graph-native collective boundary while keeping stock HCCL as the transport, deferring row-parallel and vocabulary-embedding reductions to the following normalized boundary, and enabling grouped decode compilation on the guarded path. It reports about 30% lower steady decode latency on the validated Qwen3.8 FP8 TP2 single-request workload, and about 45% when combined with eight-layer regional graphs relative to the original TP2 path, with identical output hashes across accepted repeated runs; the change is opt-in behind VLLM_HPU_TP2_FUSED_AR_NORM and only for a two-rank TP-only dense Qwen3 topology, and a fresh hardware rerun on the combined mainline was pending because the node had a driver-level device-acquisition stall. PR #10 then fixed a correctness defect:

- Kind: Claim
- Status: active
- Evidence: Author-validated
- Area: distributed
- Document date: 2026-09-05
- Retrieved: 2026-09-25
- Scope: topology: tp2; model: Qwen
- Topics: tensor-parallel, allreduce, rmsnorm, hccl, gemma-rmsnorm, collective-correctness, qwen3-8, qwen3-5
- Basis Entries: none
- Omitted private support records: 0

### Citations

- **Pull request #5** (`pull-request-5-cdf67f1`)
  - Locator: https://github.com/1CatAI/1Cat-vLLM-Gaudi/pull/5
  - Support: Describes the fused AR+residual+RMSNorm boundary with stock HCCL transport, the ~30% and ~45% decode-latency results with identical output hashes, the opt-in flag and two-rank restriction, fallback conditions, and the pending fresh hardware rerun due to a driver-level device-acquisition stall.
- **Pull request #10** (`pull-request-10-15427ad`)
  - Locator: https://github.com/1CatAI/1Cat-vLLM-Gaudi/pull/10
  - Support: States that GemmaRMSNorm did not consume the deferred-reduction marker so required collectives could be silently omitted, describes the consumer-validation fix and stock-HCCL Gemma routing, records 163 passing tests with no hardware skips and about +8% throughput in a correctness-gated warm-request A/B, and confirms native fused Gemma decode stays disabled after nonfinite-logit failures.

## deepseek-native-replay-and-continuation

**DeepSeek V4 / V4.1 native replay: 43-layer limited route for V4, 128-reduction TP2 joint replay, and a 10.4% device-continuation gain for V4.1**

DeepSeek V4 gains an opt-in prepared native decode (PR #21) that prepares Q16/S16 compressed expert weights at load time, keeps a single compressed expert-weight copy, and replays the whole decoder through the native compute/communication plan including the final mHC/head/norm; the documented limited route covers 43 layers and 86 decoder reductions. Validation for V4 was 96 CPU/meta tests with 16 hardware-gated skips, but frozen production token/logprob equality and standalone asynchronous-chain teardown remain unqualified. PR #19 adds opt-in native TP2 joint replay, validating 4,096 changing-input checks with exact outputs against an archived same-math reference while retaining all 128 layer reductions plus a separate embedding reduction;

- Kind: Claim
- Status: active
- Evidence: Author-validated
- Area: distributed
- Document date: 2026-09-14
- Retrieved: 2026-09-25
- Scope: not separately stated
- Topics: deepseek-v4, deepseek-v4-1, native-replay, graph-capture, pipeline-parallel, device-continuation, engram, mhc
- Basis Entries: none
- Omitted private support records: 0

### Citations

- **Pull request #21** (`pull-request-21-be1376d`)
  - Locator: https://github.com/1CatAI/1Cat-vLLM-Gaudi/pull/21
  - Support: Prepared Q16/S16 weights, single compressed expert copy, full decoder native replay, 96 CPU/meta tests with 16 hardware-gated skips, and the statement that frozen production token/logprob equality and standalone asynchronous-chain teardown remain unqualified.
- **Pull request #19** (`pull-request-19-98d9156`)
  - Locator: https://github.com/1CatAI/1Cat-vLLM-Gaudi/pull/19
  - Support: Retains all 128 layer reductions and the separate embedding reduction, reports 4,096 changing-input checks with exact outputs on both Gaudi2 ranks, and states qualification is open because the backported Synapse source is not numerically equivalent to the production compiler, with frozen logprob differences isolated to an FP8 MME accumulation difference.

## v4-1-swa-ring-state-repair

**Long-decode repetition collapse traced to an SWA mirror using logical positions after the packed cache wrapped to circular rows**

PR #34 documents a concrete reliability defect and its repair for DeepSeek V4.1 prepared deployment: the decoded SWA mirror used logical positions after the packed cache had wrapped to its circular row namespace, so long generations could read stale decoded rows and degrade into repetition or malformed output. The fix writes packed and decoded SWA state through the same circular address and publishes the hot Reindex prefix before the larger search bucket consumes it, while keeping the qualified norm/RoPE boundary. Validation recorded: full rebuild of the TPC kernel database, PyTorch extension and host-gather extension; native kernel database check; 54 focused V4.1 unit/contract tests passed with 1 skipped; Ruff and whitespace checks; a causal Gaudi2 ring-wrap check where the former logical-row contract diverged after wrap while the fixed circular contract matched the packed cache bit-for-bit;

- Kind: Claim
- Status: active
- Evidence: Author-validated
- Area: reliability
- Document date: 2026-09-20
- Retrieved: 2026-09-25
- Scope: topology: not-stated; model: DeepSeek V4.1
- Topics: deepseek-v4-1, sliding-window-attention, circular-cache, kv-cache, long-generation, state-correctness, regression
- Basis Entries: none
- Omitted private support records: 0

### Citations

- **Pull request #34** (`pull-request-34-a90425a`)
  - Locator: https://github.com/1CatAI/1Cat-vLLM-Gaudi/pull/34
  - Support: Explains the stale decoded-row root cause after cache wrap, the circular-address and Reindex-prefix fixes, the 54 passed / 1 skipped contract suite, the causal Gaudi2 ring-wrap bit-for-bit check, and the long streaming generation without repetition collapse at about one percent of parent latency.
- **docs/features/deepseek_v41.md** (`docs-features-deepseek-v41-md-e421582`)
  - Locator: https://github.com/1CatAI/1Cat-vLLM-Gaudi/blob/5fa3e08302716d458a82aa7d95d107e201b51d8c/docs/features/deepseek_v41.md
  - Support: States the decoded SWA mirror uses the same circular row namespace as the packed cache and that the hot index mirror is populated before its first larger search bucket, calling these state repairs required for long-generation quality.

## v4-1-long-context-paged-serving

**V4.1 long-context serving: 1,048,576-token capacity with 8,192-token prefill chunks, grouped expert prefill, and subsequent prefill-kernel efficiency work**

PR #32 restored V4.1 accelerated long-context serving by adding immutable fingerprinted N256 runtime shards with bounded preparation/loading and exact layout recovery, enabling bounded expert-grouped prefill at the scheduler's 8,192-token chunk size, extending paged KV/RoPE and bucket-specific replay, and authorizing continuation only after the next bucket is ready. It also isolated grouped-prefill reduction code objects per prompt shape because a real serving log showed repeated requests could exhaust Dynamo's shared recompile limit, and fixed CPU-versus-device completion-token ownership. Validation:

- Kind: Claim
- Status: active
- Evidence: Author-validated
- Area: serving
- Document date: 2026-09-25
- Retrieved: 2026-09-25
- Scope: not separately stated
- Topics: deepseek-v4-1, long-context, paged-kv, grouped-prefill, moe, dynamo-recompile, n256
- Basis Entries: none
- Omitted private support records: 0

### Citations

- **Pull request #32** (`pull-request-32-f820963`)
  - Locator: https://github.com/1CatAI/1Cat-vLLM-Gaudi/pull/32
  - Support: N256 fingerprinted shards with --n256-prepared-dir, bounded expert-grouped prefill at 8,192-token chunks, bucket-gated continuation, per-prompt-shape reduction code objects after a real serving log showed Dynamo recompile exhaustion, completion-token ownership fix, 129 CPU contract tests, and about 22% lower decode latency versus the prior long-context candidate with full-window quality still outstanding.
- **docs/features/deepseek_v41.md** (`docs-features-deepseek-v41-md-e421582`)
  - Locator: https://github.com/1CatAI/1Cat-vLLM-Gaudi/blob/5fa3e08302716d458a82aa7d95d107e201b51d8c/docs/features/deepseek_v41.md
  - Support: Gives the exact long-context launch arguments (--max-model-len 1048576 --max-num-batched-tokens 8192 --max-num-seqs 1 --block-size 128 --num-gpu-blocks-override 8193), states packed KV remains canonical with only the active working set decoded, and records that validation covers a chunk-boundary crossing, short-request reuse, eight arithmetic samples and public chat but not full-window quality.

## quantization-and-prepared-weights

**Quantization support is split between prepared MXFP4/FP8 expert layouts, mandatory FP8 sidecars and a TPC-dequant + BF16-MME block-FP8 path**

Prepared-weight contracts are a distinct research axis in this repository. For DeepSeek, the prepared path validates model revision and file identity, then generates rank-local shards for the target TP/PP topology using a Q16/S16 expert layout with scale encoding and K alignment; the V4 native decoder packs MXFP4 directly, supports 128-element K alignment and pads the TP-local 1152-element W2 K dimension, and keeps exactly one resident compressed expert-weight allocation per rank so runtime expert tensors are copied to their single destination. V4.1's prepared numerical profile uses N256 FP8 experts with fused activation preparation, channel-scaled FP8 wo_a, dedicated Router top-6, decoded KV with shared-KV MME attention, BF16 head operands with FP32 logits and fused Q/KV input projection;

- Kind: Claim
- Status: active
- Evidence: Documented
- Area: quantization
- Document date: 2026-09-21
- Retrieved: 2026-09-25
- Scope: not separately stated
- Topics: mxfp4, fp8, block-fp8, n256, prepared-weights, sidecars, mme, tpc
- Basis Entries: none
- Omitted private support records: 0

### Citations

- **docs/features/deepseek_v41.md** (`docs-features-deepseek-v41-md-e421582`)
  - Locator: https://github.com/1CatAI/1Cat-vLLM-Gaudi/blob/5fa3e08302716d458a82aa7d95d107e201b51d8c/docs/features/deepseek_v41.md
  - Support: Describes Q16/S16 MXFP4 packing, 128-element K alignment, TP-local 1152-element W2 padding, single resident compressed expert allocation, bounded host conversion of block-FP8 dense matrices to BF16 MME weights, the two mandatory sidecars validated before model load, and that the N256 cache is optional with manifest published only after exact inverse-layout checks.
- **Pull request #11** (`pull-request-11-f46d0cb`)
  - Locator: https://github.com/1CatAI/1Cat-vLLM-Gaudi/pull/11
  - Support: States the native block-linear recipe is exact-contract TPC dequantization plus BF16 MME GEMM (not FP8 MME) with no activation quantization or hidden output copy, reports about 6% complete-operation acceleration on tested small-batch down-projection shapes including real checkpoint-weight confirmation, records 172 passing tests (157 CPU/reference, 15 opt-in hardware), and notes the complete matrix is still slower on average with activations synthetic and no production dispatch changed.

## blockers-and-open-directions

**Open blockers: an unpublished V4.1 engine lock and runtime provenance, several default-off or failed experiments, and unresolved V4 quality/lifecycle gaps**

Issue #44 (opened 2026-09-25, still open) is a concrete reproducibility blocker for the headline V4.1 TP2xPP2 path: the repository publishes the plugin layer in Git but not the required V4.1 engine delta over vLLM base e47aa780bccf59f59dfa2cbb18e17a10b4fe69ba, the native runtime source/revision/build path for Bridge, Synapse and HCL (only revisions are recorded in native-runtime/manifest.json), or the gateway deployment delta, while docs/features/deepseek_v41.md states that no complete installable V4.1 engine lock is published and that previously built bridges with a fixed PP0 collective count cannot replay long CSA2 buckets. Other recorded blockers and negative results: PR #33 is a draft that fixes a streaming failure at a native decode search-bucket boundary, but its unconditional warmup of every C1 history bucket was rejected for disproportionate graph growth and no successful service recovery is claimed;

- Kind: Claim
- Status: active
- Evidence: Documented
- Area: reliability
- Document date: 2026-09-25
- Retrieved: 2026-09-25
- Scope: not separately stated
- Topics: reproducibility, provenance, engine-lock, native-runtime, draft-prs, negative-results, quality-gates, open-issues
- Basis Entries: none
- Omitted private support records: 0

### Citations

- **Issue #44 - Request Engine Provenance Bundle for TP2xPP2** (`issue-44-request-engine-provenance-bundle-606a838`)
  - Locator: https://github.com/1CatAI/1Cat-vLLM-Gaudi/issues/44
  - Support: Requests exactly three unpublished layers: the V4.1 engine delta over base e47aa780bccf59f59dfa2cbb18e17a10b4fe69ba, native runtime source plus exact revisions and build paths for Bridge 5176b1b2.../Synapse 6de1f66a.../HCL 11f9114b..., and the gateway deployment delta; confirms the plugin source layer (through 8e6ea399, plus B2 fix d0266b6) is already in Git. Opened 2026-09-25, open, no comments.
- **docs/features/deepseek_v41.md** (`docs-features-deepseek-v41-md-e421582`)
  - Locator: https://github.com/1CatAI/1Cat-vLLM-Gaudi/blob/5fa3e08302716d458a82aa7d95d107e201b51d8c/docs/features/deepseek_v41.md
  - Support: States the repository does not yet publish a complete installable V4.1 engine lock, that the upstream audit is evidence collection rather than an installer or qualified compatibility lock, and that previously built bridges with a fixed PP0 collective count cannot replay long CSA2 buckets.

## discord-gaudi2-dsv41-prefill-3000tps-disputed

**~3000 tok/s prefill on 4 Gaudi 2 (TP2xPP2) for DeepSeek V4.1 Flash - replication disputed**

A 1Cat-affiliated member reported ~3000 token/s prefill on Gaudi 2 using 4 HPUs in pp2 tp2 with DeepSeek V4.1 Flash, presenting it as the payoff of the TP2xPP2 approach; the claim was posted twice (09-23 and 09-24). Other participants state that everyone else has been unable to reproduce it, and the team replied that their code will be uploaded soon - so the number is currently an unverified community report. For baseline context, another member recalled that stock ('out of the box') vLLM-Gaudi on Qwen3.8-27B reaches roughly 4k prefill, and multiple people remarked that Gaudi prefill is otherwise poor (an independent single-stream test measured ~100 tok/s prefill, see separate finding).

- Kind: Claim
- Status: active
- Evidence: Unverified
- Area: performance
- Document date: 2026-09-23
- Retrieved: 2026-09-25
- Scope: topology: tp2-pp2; model: DeepSeek V4.1 Flash
- Topics: gaudi-2, prefill, deepseek-v4-1-flash, pp2, tp2, 4-hpu, replication, shortcut
- Basis Entries: none
- Omitted private support records: 0

### Citations

- **Discord — ~3000 tok/s TP2×PP2 prefill claim** (`discord-3000-tok-s-tp2-x-pp2-prefill-claim-838cbff`)
  - Locator: https://discord.com/channels/1550356974628114473/1550356975890727026/1552576164541894696
  - Support: 2026-09-24 report of ~3000 tok/s prefill on four Gaudi 2 HPUs using TP2×PP2 and DeepSeek V4.1 Flash; channel replies dispute reproducibility and state code was pending.

## discord-gaudi2-1cat-dsv41-partial

**Independent attempt: 80 tok/s single-stream decode but batching and MTP broken, ~100 tok/s prefill**

A community member reports getting the 1Cat DeepSeek 4.1 Flash path working on Gaudi 2: single-stream decode was 'pretty good' at 80 tok/s, but batching does not work, MTP does not appear to work, and prefill is slow at ~100 tok/s, with all three listed as open work items. This is the clearest published blocker set for the 1Cat stack and contrasts with the 3000 tok/s prefill claim made by the team two days later. Related sentiment in the same channel: raw Gaudi 2 power is not in doubt; compatibility, kernels and support are the real problems, and any working 'recipe' should be captured.

- Kind: Claim
- Status: active
- Evidence: Unverified
- Area: serving
- Document date: 2026-09-22
- Retrieved: 2026-09-25
- Scope: topology: not-stated; model: DeepSeek V4.1 Flash
- Topics: gaudi-2, deepseek-v4-1-flash, prefill, decode, batching, mtp, blocker
- Basis Entries: none
- Omitted private support records: 0

### Citations

- **Discord — independent 1Cat DeepSeek V4.1 attempt** (`discord-independent-1cat-deepseek-v4-1-att-cb3132f`)
  - Locator: https://discord.com/channels/1550356974628114473/1550356975890727026/1551786922664525875
  - Support: Independent report: 80 tok/s single-stream decode, batching and MTP not working, and about 100 tok/s prefill.

## discord-gaudi2-glm53-flash-community-fork

**Community vLLM-Gaudi fork adds GLM-5.3-Flash: ~14 tok/s decode, 16-24 with MTP**

A Gaudi/Habana-oriented developer published a vLLM-Gaudi fork adding GLM-5.3-Flash support, including a custom KDA kernel, and reports roughly 14 tok/s decode and 16-24 tok/s with MTP speculative decoding. They flag remaining work on batching and batch-size buckets/graphs and invited the 1Cat team to integrate the code upstream; they later stated they have no time to push the GLM work upstream themselves for now. Treated as the strongest independent (non-1Cat) Gaudi 2 model-enablement datapoint in the reviewed window.

- Kind: Claim
- Status: active
- Evidence: Unverified
- Area: model-support
- Document date: 2026-09-21
- Retrieved: 2026-09-25
- Scope: topology: not-stated; model: GLM-5.3-Flash
- Topics: gaudi-2, glm-5-3-flash, vllm-gaudi, kda-kernel, mtp, speculative-decoding, fork
- Basis Entries: none
- Omitted private support records: 0

### Citations

- **Discord — GLM-5.3-Flash Gaudi fork report** (`discord-glm-5-3-flash-gaudi-fork-report-30585c0`)
  - Locator: https://discord.com/channels/1550356974628114473/1550356975890727026/1551619992183644341
  - Support: Report links abotsis/vllm-gaudi, a KDA kernel, about 14 tok/s decode and 16–24 tok/s with MTP; batching and bucket work remained.

## discord-cdna2-gaudi2-dsv41-1m-context

**Reported DSV4.1 at 73.5 tok/s token-generation at 1M context on 4 Gaudi 2**

In the Launch80 #cdna2 channel (AMD CDNA2-focused, adjacent low-cost-accelerator research community) a participant relayed that someone got DeepSeek V4.1 running at 73.5 tok/s token generation at a 1M-token context window on 4 Gaudi 2 GPUs, linking the 1CatAI repository. This is the highest long-context decode datapoint surfaced in either server and cross-links the Gaudi server's 1Cat workstream.

- Kind: Claim
- Status: active
- Evidence: Unverified
- Area: performance
- Document date: 2026-09-21
- Retrieved: 2026-09-25
- Scope: topology: tp2-pp2; model: DeepSeek V4.1
- Topics: gaudi-2, deepseek-v4-1, 1m-context, long-context, decode, throughput, cross-community
- Basis Entries: none
- Omitted private support records: 0

### Citations

- **Discord — 1M-context DeepSeek V4.1 report** (`discord-1m-context-deepseek-v4-1-report-b88e323`)
  - Locator: https://discord.com/channels/1469905184892391597/1529585288110932272/1551613480191262870
  - Support: Launch80 report cites 73.5 tok/s token generation at a 1M context capacity on four Gaudi 2 cards and links 1Cat-vLLM-Gaudi.

## discord-gaudi2-quantization-gaps

**Quantization gaps: FP8 is E4M3-only (no E4M3FN), no native INT4, H3 degrades under FP8**

Gaudi 2's FP8 datapath supports E4M3 but not E4M3FN, which many published FP8 checkpoints target on Hopper-class GPUs - flagged as a real conversion/porting difference rather than a cosmetic one. Separately, a participant wished the hardware supported INT4 natively, and another reported hearing that MiniMax H3 'doesn't quantize all that well ... even fp8 quality degrades' (not independently tested). Net effect: low-precision model availability for Gaudi 2 is narrower than the headline FP8 support suggests.

- Kind: Claim
- Status: active
- Evidence: Unverified
- Area: quantization
- Document date: 2026-09-24
- Retrieved: 2026-09-25
- Scope: not separately stated
- Topics: gaudi-2, fp8, e4m3, e4m3fn, int4, quantization, checkpoints, minimax-h3
- Basis Entries: none
- Omitted private support records: 0

### Citations

- **Discord — Gaudi 2 FP8 format gap** (`discord-gaudi-2-fp8-format-gap-4b703a2`)
  - Locator: https://discord.com/channels/1550356974628114473/1550356975890727026/1552705978254762005
  - Support: Community report distinguishes Gaudi 2 E4M3 support from the E4M3FN format used by many checkpoints.

## discord-gaudi2-handwritten-mme-tpc-kernels

**Hand-written MME/TPC kernel findings: 1.5 TB/s TPC aggregate, 300 GB/s MME, 40 tok/s Qwen 27B on TPCs alone**

From a hand-rolled 'feed the TPCs and MMEs by hand' kernel experiment on Gaudi 2: the 24 TPCs provide roughly 1.5 TB/s aggregate memory bandwidth; the 2 MMEs are limited to roughly 300 GB/s of HBM bandwidth; Qwen 27B reached about 40 tok/s using only the TPCs (an inefficient use of the part); TPC FLOPs and bandwidth saturate at around the same point; and the real lever is the 48 MB of on-chip SRAM at ~6.4 TB/s, which requires pipelining HBM<->SRAM DMA transfers so they overlap with MME operations (enqueue DMA, then MME op reading SRAM/HBM, then the next DMA). The graph compiler performs this DMA scheduling automatically, which is why writing a resident scheduler by hand is hard.

- Kind: Claim
- Status: active
- Evidence: Unverified
- Area: performance
- Document date: 2026-09-24
- Retrieved: 2026-09-25
- Scope: topology: single-card; model: Qwen 27B
- Topics: gaudi-2, mme, tpc, sram, dma, bandwidth, qwen-27b, kernel-authoring
- Basis Entries: none
- Omitted private support records: 0

### Citations

- **Discord — handwritten MME/TPC measurements** (`discord-handwritten-mme-tpc-measurements-b18d844`)
  - Locator: https://discord.com/channels/1550356974628114473/1550356975890727026/1552706651612651521
  - Support: Reported experiments: ~1.5 TB/s across 24 TPCs, ~300 GB/s through two MMEs, ~40 tok/s Qwen 27B using TPCs, and a proposal to overlap HBM↔SRAM DMA with MME work.
- **Shared ChatGPT performance-tuning analysis** (`shared-chatgpt-performance-tuning-analysis-ee5cc57`)
  - Locator: https://chatgpt.com/share/6ab63afb-3f7c-83ec-8f95-04ceacab627d
  - Support: User-supplied secondary synthesis identifies DMA/SRAM/MME overlap, compiler-versus-dispatch costs, resident execution, and disciplined benchmark loops as hypotheses. It explicitly treats quoted community measurements as unverified rather than independent proof.

## discord-gaudi2-graph-compiler-opacity

**Closed HPU graph compiler and torch bridge are the central stack blocker; remedies proposed**

Community consensus is that nearly all inference goes vLLM -> torch -> Habana torch bridge -> HPU graph, but the bridge builds graphs through torch.compile and has limits relative to what raw HPU graphs can express, and there is no pure-C graph compiler baseline to attribute problems to the bridge versus the compiler. Proposed attacks: decompile/reverse-engineer SynapseAI so precompiled instruction sequences can be reused without it, build a lower-latency dispatch engine / custom executor and submitter for Synapse ops, and use early SynapseAI versions that expose graph construction. The wish that Intel would simply open the compiler recurs throughout.

- Kind: Claim
- Status: active
- Evidence: Unverified
- Area: software-stack
- Document date: 2026-09-24
- Retrieved: 2026-09-25
- Scope: not separately stated
- Topics: gaudi-2, synapseai, torch-bridge, hpu-graph, vllm, compiler, reverse-engineering, dispatch
- Basis Entries: none
- Omitted private support records: 0

### Citations

- **Discord — bridge and graph-compiler limits** (`discord-bridge-and-graph-compiler-limits-c17761a`)
  - Locator: https://discord.com/channels/1550356974628114473/1550356975890727026/1552704782295367721
  - Support: Discussion traces vLLM through PyTorch and the Habana bridge to HPU graphs, proposing that raw graph capabilities may exceed what the bridge exposes.
- **Shared ChatGPT performance-tuning analysis** (`shared-chatgpt-performance-tuning-analysis-ee5cc57`)
  - Locator: https://chatgpt.com/share/6ab63afb-3f7c-83ec-8f95-04ceacab627d
  - Support: User-supplied secondary synthesis identifies DMA/SRAM/MME overlap, compiler-versus-dispatch costs, resident execution, and disciplined benchmark loops as hypotheses. It explicitly treats quoted community measurements as unverified rather than independent proof.

## discord-gaudi2-dispatch-overhead-resident-graphs

**Per-token dispatch/compile overhead is the decode bottleneck; resident graph-chunk approach proposed**

Reported blocker: token generation is autoregressive, so the accelerator is hit with graphs repeatedly - 'hundreds per token (best case)' - and graph replay/dispatch cost is high; a participant states flatly that even after compiling once and resubmitting graphs the path 'is still slow'. Related quantified symptom: compiling HPU graphs for a large canvas (r768) exhausted host memory on a 128 GB host while smaller canvases worked, and graphs bought only ~5% over eager for the MiniMax H3 port. Proposed direction: build resident graphs from composable 'graph chunks' (groups of queue dispatch ops) using something like tinygrad, with a single host launch for the decode loop; a prototype resident TPC kernel polled a doorbell and executed GGML-like coarse ops. Bucket-level tuning is already visible in the 1Cat code:

- Kind: Claim
- Status: active
- Evidence: Unverified
- Area: serving
- Document date: 2026-09-24
- Retrieved: 2026-09-25
- Scope: not separately stated
- Topics: gaudi-2, decode, graph-replay, dispatch-latency, resident-graph, tinygrad, bucketing, compile-time
- Basis Entries: none
- Omitted private support records: 0

### Citations

- **Discord — composable resident graph proposal** (`discord-composable-resident-graph-proposal-4e18ec9`)
  - Locator: https://discord.com/channels/1550356974628114473/1550356975890727026/1552708068360327270
  - Support: Proposal to build resident execution from composable graph chunks and grouped queue-dispatch operations; a follow-up reports compile-once resubmission remains slow.
- **Shared ChatGPT performance-tuning analysis** (`shared-chatgpt-performance-tuning-analysis-ee5cc57`)
  - Locator: https://chatgpt.com/share/6ab63afb-3f7c-83ec-8f95-04ceacab627d
  - Support: User-supplied secondary synthesis identifies DMA/SRAM/MME overlap, compiler-versus-dispatch costs, resident execution, and disciplined benchmark loops as hypotheses. It explicitly treats quoted community measurements as unverified rather than independent proof.

## discord-gaudi2-oam-adapter-enablement

**Single Gaudi 2 runs on OAM-to-PCIe adapters, but scale-up SerDes/QSFP links are unwired**

Hardware enablement state: an enthusiast bought a Gaudi 2 instead of an MI250, used an OAM-to-PCIe adapter (an NVIDIA engineering sample sourced second-hand), and reports it works after patching the Habana driver, which objected to the absence of a UBB - but the SerDes/scale-in P2P QSFP ports are not wired on that adapter, so multi-accelerator P2P is unavailable. A vendor/team states a custom OAM carrier board went into production about a month earlier, 'suitable for MI250X and any OAM card', tested on MI250X and Gaudi. Community technical notes: OAM defines PCIe/power plus 'other' pins carrying Gaudi's on-die RDMA Ethernet (100 GbE per port, 24 ports per card), Intel calls the Gaudi baseboard 'OCP-inspired' rather than strictly OCP-compliant, and the OAM v1.1 specification was shared as the reference. A separate observation in Launch80 says the Gaudi2s expect baseboard signals that are patchable because the driver is open source.

- Kind: Claim
- Status: active
- Evidence: Unverified
- Area: hardware
- Document date: 2026-08-20
- Retrieved: 2026-09-25
- Scope: not separately stated
- Topics: gaudi-2, oam, ubb, pcie-adapter, serdes, roce, 100gbe, habana-driver
- Basis Entries: none
- Omitted private support records: 0

### Citations

- **Discord — OAM-to-PCIe adapter bring-up** (`discord-oam-to-pcie-adapter-bring-up-f8ab319`)
  - Locator: https://discord.com/channels/1469905184892391597/1529585288110932272/1540067026200961154
  - Support: An NVIDIA ES OAM-to-PCIe adapter reportedly runs Gaudi 2, but does not wire the scale-up SerDes/QSFP links.

## discord-gaudi2-wiwynn-supermicro-reliability

**Wiwynn ES baseboards show memory-training and mesh bring-up problems; Supermicro expected more stable**

Baseboard experience reports for 8x Gaudi 2 systems: the Wiwynn unit is an engineering-sample motherboard/BIOS with memory-training issues (disabling POR in BIOS helped) and it will not run the owner's ES Ice Lake CPUs; the chassis is cheaper but less reliable. A respondent without Supermicro hardware expects better stability, better memory support and a better BMC from Supermicro. One report claims other users' Wiwynn servers had trouble bringing up the HPU-to-HPU Ethernet interconnects (cause not determined: HPU, chassis or ES UBB). Mitigating detail: fewer than 8 accelerators can be powered in one box, and OAM-to-PCIe adapters are available for roughly USD 700, though the baseboard BMC behaviour is unclear. A separate owner reported losing at least a motherboard to a power surge.

- Kind: Claim
- Status: active
- Evidence: Unverified
- Area: reliability
- Document date: 2026-09-22
- Retrieved: 2026-09-25
- Scope: topology: eight-card
- Topics: gaudi-2, wiwynn, supermicro, es-silicon, bios, memory-training, interconnect, hardware-reliability
- Basis Entries: none
- Omitted private support records: 0

### Citations

- **Discord — Wiwynn ES memory-training issues** (`discord-wiwynn-es-memory-training-issues-7ba304a`)
  - Locator: https://discord.com/channels/1550356974628114473/1551630701252714637/1551811126080053339
  - Support: Operator reports Wiwynn ES motherboard/BIOS memory-training problems and a POR workaround; Supermicro stability is an expectation, not measured evidence.

## discord-gaudi2-ecosystem-support-risk

**Ecosystem risk: no community around Gaudi 2, and even supported paths underperform out of the box**

Recurring theme in both servers: the hardware is powerful for the price but the ecosystem is the bottleneck. A participant considering Gaudi 2 instead of CDNA2 concluded 'Gaudi 2 you'd be essentially alone' (versus ROCm, where CDNA3+ is catching up); another said they could not find any community around Gaudi 2 at all. Concrete support datapoints: stock vLLM-Gaudi on Gaudi 3 gave ~4 tokens/s for GLM-5.2-FP8 on 8 HPUs, and model coverage was claimed to stop around DeepSeek R1-era models. A vllm-gaudi issue thread (#1549) was shared as the tracking point for Gaudi 2 enablement, and a widely shared write-up on Intel's Gaudi pricing/programmability (the tinygrad/Geohot 'tragic-intel' post) was used to explain why Gaudi adoption stalled.

- Kind: Claim
- Status: active
- Evidence: Unverified
- Area: reliability
- Document date: 2026-09-21
- Retrieved: 2026-09-25
- Scope: not separately stated
- Topics: gaudi-2, ecosystem, community, support, vllm-gaudi, rocm-comparison, gaudi-3, geohot
- Basis Entries: none
- Omitted private support records: 0

### Citations

- **Discord — Launch80 ecosystem-risk assessment** (`discord-launch80-ecosystem-risk-assessment-322b7c0`)
  - Locator: https://discord.com/channels/1469905184892391597/1529585288110932272/1551611780785242165
  - Support: Community assessment warns Gaudi 2 experimenters may be largely alone relative to ROCm; treated as ecosystem sentiment, not a technical benchmark.

## discord-gaudi2-research-roadmap-thread

**Server roadmap thread: hardware access, vLLM MoE at 50-75 tok/s decode + 3000+ prefill, and a Gaudi interconnect board**

The Gaudi server's only substantive thread (created 2026-09-21) frames the community agenda in three items: (1) getting Gaudi systems and renting them out so unblocked developers can resolve work; (a) vLLM MoE at good speeds for Gaudi - target 50-75 tok/s decode and 3000+ prefill; (b) an interconnect board for the Gaudi. This matches the observed workstreams: the 1Cat TP2xPP2 prefill number, the vLLM-Gaudi MoE forks, and the OAM carrier-board projects discussed across both servers.

- Kind: Claim
- Status: active
- Evidence: Unverified
- Area: serving
- Document date: 2026-09-21
- Retrieved: 2026-09-25
- Scope: not separately stated
- Topics: gaudi-2, roadmap, moe, vllm, decode, prefill, interconnect-board, hardware-access
- Basis Entries: none
- Omitted private support records: 0

### Citations

- **Discord — Unofficial Intel Gaudi research tasks** (`discord-unofficial-intel-gaudi-research-ta-2fc250f`)
  - Locator: https://discord.com/channels/1550356974628114473/1551692814163902505/1551692814163902505
  - Support: Thread prioritizes hardware/rental access, vLLM MoE targets of 50–75 tok/s decode and 3000+ prefill, and a Gaudi interconnect board. Targets are proposed, not achieved.

## need-gaudi2-host

**Gaudi 2 hardware access for reproducible tests**

A contributor needs access to a working Gaudi 2 host so fixed single-card workloads and bring-up procedures can be reproduced.

- Kind: Question
- Status: active
- Area: hardware
- Document date: 2026-09-25
- Retrieved: 2026-09-25
- Scope: not separately stated
- Topics: hardware-access, reproduction
- Basis Entries: `discord-gaudi2-research-roadmap-thread`, `discord-gaudi2-oam-adapter-enablement`
- Omitted private support records: 0

### Citations

No public citation retained.

## need-profiler-trace

**Profiler trace from one fixed inference workload**

Capture one warmed workload with enough MME, TPC, DMA, graph, and host-dispatch timing to separate execution from submission overhead.

- Kind: Question
- Status: active
- Area: performance
- Document date: 2026-09-25
- Retrieved: 2026-09-25
- Scope: topology: single-card
- Topics: profiling, dispatch, mme, tpc
- Basis Entries: `discord-gaudi2-handwritten-mme-tpc-kernels`, `discord-gaudi2-dispatch-overhead-resident-graphs`
- Omitted private support records: 0

### Citations

No public citation retained.

## need-carrier-bringup-run

**Documented carrier and driver bring-up run**

Retain carrier identity, host platform, firmware, driver changes, health output, and a completed inference smoke workload.

- Kind: Question
- Status: active
- Area: hardware
- Document date: 2026-09-25
- Retrieved: 2026-09-25
- Scope: not separately stated
- Topics: oam, pcie, driver, bringup
- Basis Entries: `discord-gaudi2-oam-adapter-enablement`, `gaudi2-install-prereqs`
- Omitted private support records: 0

### Citations

No public citation retained.

## need-power-thermal-characterization

**Proposed power and thermal characterization**

The documented accelerator envelope reaches 600 W; a standalone carrier path needs measured power delivery and thermal behavior before it can be called reproducible.

- Kind: Question
- Status: active
- Area: hardware
- Document date: 2026-09-25
- Retrieved: 2026-09-25
- Scope: not separately stated
- Topics: power, thermal, oam, proposal
- Basis Entries: `gaudi2-arch-specs`, `gaudi2-reliability-observability`
- Omitted private support records: 0

### Citations

No public citation retained.

## question-direct-attach

**What is the reproducible single-card OAM-to-PCIe bring-up path?**

Define the carrier, missing-UBB driver behavior, host and firmware compatibility, power delivery, thermal setup, health checks, and inference smoke workload.

- Kind: Question
- Status: active
- Area: hardware
- Document date: 2026-09-25
- Retrieved: 2026-09-25
- Scope: not separately stated
- Topics: oam, pcie, driver, single-card
- Basis Entries: `discord-gaudi2-oam-adapter-enablement`, `gaudi2-install-prereqs`, `gaudi2-arch-specs`
- Omitted private support records: 0

### Citations

No public citation retained.

## question-graph-dispatch

**Where does warmed single-card decode time go: graph compilation, replay, host dispatch, or execution?**

Separate the costs on one fixed model and shape; success is a trace-backed latency budget that identifies the dominant controllable component.

- Kind: Question
- Status: active
- Area: software-stack
- Document date: 2026-09-25
- Retrieved: 2026-09-25
- Scope: not separately stated
- Topics: graph, dispatch, replay, profiling
- Basis Entries: `gaudi2-exec-modes`, `warmup-graph-cache-cost`, `discord-gaudi2-dispatch-overhead-resident-graphs`
- Omitted private support records: 0

### Citations

No public citation retained.

## question-prefill-batching

**Why do long-context prefill and batching results diverge so widely?**

Reconcile the disputed ~3000 tok/s TP2×PP2 report with the independent ~100 tok/s report under fixed model, prompt, precision, topology, and measurement definitions.

- Kind: Question
- Status: active
- Area: performance
- Document date: 2026-09-25
- Retrieved: 2026-09-25
- Scope: topology: single-card
- Topics: prefill, batching, long-context, reproduction
- Basis Entries: `discord-gaudi2-dsv41-prefill-3000tps-disputed`, `discord-gaudi2-1cat-dsv41-partial`, `qwen38-fp8-a800-vs-gaudi2-record`
- Omitted private support records: 0

### Citations

No public citation retained.

## question-quant-model

**Which quantization and model formats reliably execute on Gaudi 2 today?**

Map supported checkpoint formats, device-bound calibration, fallback paths, and validated models without conflating hardware dtype support with end-to-end quantized inference.

- Kind: Question
- Status: active
- Area: quantization
- Document date: 2026-09-25
- Retrieved: 2026-09-25
- Scope: not separately stated
- Topics: fp8, int4, model-support, calibration
- Basis Entries: `gaudi2-datatypes`, `quantization-backends-and-calibration`, `discord-gaudi2-quantization-gaps`
- Omitted private support records: 0

### Citations

No public citation retained.

## question-topology-transfer

**Which multi-card optimizations transfer to standalone single-card inference?**

Separate MME/TPC/data-movement techniques from HCCL, TP, PP, and scale-up fabric effects before using multi-card results to guide desktop work.

- Kind: Question
- Status: active
- Area: distributed
- Document date: 2026-09-25
- Retrieved: 2026-09-25
- Scope: not separately stated
- Topics: single-card, tp2, pp2, topology
- Basis Entries: `gaudi2-roce-network`, `tp2-reduction-fusion-and-correctness`, `discord-gaudi2-oam-adapter-enablement`
- Omitted private support records: 0

### Citations

No public citation retained.

## deepseek-v41-pr40-code-not-throughput-recipe

**Merged 1Cat PR #40 supplies an optimized DeepSeek V4.1 TP2×PP2 prefill implementation and correctness-qualified serving path, but it does not provide a reproducible throughput result or confirm 6.4k prefill tokens/s.**

PR #40 documents bounded sparse-MLA, projection, KV-reuse, grouped-MoE, pipeline, Engram-residency, native-build, and trace-analysis changes. Its reported normal TP2×PP2 serving qualification covers frozen 32K, 16K, and 32K+1 prompts with expected first tokens. The PR explicitly says raw profiles, model files, and one-off experiments remain outside the repository and that these serving checks qualify prefill correctness rather than concurrent-serving throughput or full-context generation quality. Therefore the implementation is a useful starting recipe, but confirmation of a throughput claim still requires pinned revisions/artifact identities, the exact benchmark command and workload, an explicit timing definition, and repeated raw measurements.

- Kind: Claim
- Status: active
- Evidence: Documented
- Area: performance
- Document date: 2026-09-24
- Retrieved: 2026-09-26
- Scope: topology: tp2-pp2; model: DeepSeek V4.1 Flash; precision: mixed BF16/FP8
- Topics: DeepSeek V4.1, prefill, TP2×PP2, benchmark reproducibility, 1Cat-vLLM-Gaudi
- Basis Entries: `deepseek-v41-full-accel-evidence-bundle`, `question-prefill-batching`, `question-topology-transfer`
- Omitted private support records: 0

### Citations

- **[HPU] Integrate general V4.1 prefill optimizations by yangzhuxinyzx · Pull Request #40 · 1CatAI/1Cat-vLLM-Gaudi · GitHub** (`github-1cat-pr40-prefill-qualification`)
  - Locator: https://github.com/1CatAI/1Cat-vLLM-Gaudi/pull/40
  - Support: PR #40 describes the merged implementation and expressly bounds its validation and retained artifacts.

## discord-gaudi2-prefill-6k4-claim

**A 1Cat-affiliated Discord participant claimed “6.4k prefill,” but the model, topology, units, benchmark definition, and measurement evidence were not stated.**

The 2026-09-26 message says only “Now we have 6.4k prefill.” Nearby context includes a request to push the repository but supplies no benchmark output or configuration. Although the surrounding project discussion makes DeepSeek V4.1 a plausible association, the retained message does not explicitly identify DeepSeek, Gaudi 2, card count, prompt length, concurrency, software commit, warmup treatment, timing boundary, or whether 6.4k means aggregate tokens per second. Retain this only as an unverified community report; it does not confirm reproducibility or standalone single-card performance.

- Kind: Claim
- Status: active
- Evidence: Unverified
- Area: performance
- Document date: 2026-09-26
- Retrieved: 2026-09-26
- Scope: topology: not-stated
- Topics: prefill, 6.4k-claim, discord, 1cat, benchmark-gap, reproducibility
- Basis Entries: `discord-gaudi2-dsv41-prefill-3000tps-disputed`, `discord-gaudi2-1cat-dsv41-partial`
- Omitted private support records: 1

### Citations

No public citation retained.

## discord-gaudi2-graph-break-tensor-clone-dispatch

**Per-token HPU graph breaks in communication ops can add 35–55 ms dispatch latency, reducible below 1 ms via tensor cloning**

Community benchmarking revealed that unoptimized tensor-parallel execution split each generated token into ~500 small HPU graph executions, where repeated CPU dispatch and accelerator synchronization added ~35–55 ms per token. Bypassing those graph breaks by cloning tensors before communication operations reduced CPU dispatch latency below 1 ms and increased token generation from ~18 to ~26 tok/s, leaving remaining latency in inter-card communication and MoE expert dispatch.

- Kind: Claim
- Status: active
- Evidence: Unverified
- Area: serving
- Document date: 2026-10-02
- Retrieved: 2026-10-02
- Scope: topology: not-stated; model: MiniMax M2.7
- Topics: gaudi-2, decode, dispatch-latency, graph-breaks, tensor-parallel
- Basis Entries: `discord-gaudi2-dispatch-overhead-resident-graphs`
- Omitted private support records: 1

### Citations

No public citation retained.

## experimental-triton-gaudi2-backend-pr11545

**Experimental Triton backend for Gaudi 2 lowers TTIR to TPC-C for SynapseAI 1.24.1, but remains unmerged upstream**

Triton PR #11545 ('Add experimental Gaudi2 backend support') introduced an experimental backend in third_party/gaudi that removes CUDA warp-size assumptions, lowers a subset of TTIR to TPC-C compiled via tpc-clang, and outputs content-addressed ELF artifacts for SynapseAI 1.24.1. Supported kernels include masked elementwise ops, residual RMSNorm, SiLU-and-mul, Qwen3.5 GDN specializations, and row-wise BF16-to-E4M3 dynamic quantization verified on the SynapseAI TPC simulator. MME partitioning, generic reductions, attention, and MoE were excluded. Upstream maintainers closed the PR unmerged due to backend acceptance policy, pointing to downstream repositories or triton-ext.

- Kind: Claim
- Status: active
- Evidence: Documented
- Area: software-stack
- Document date: 2026-09-02
- Retrieved: 2026-10-03
- Scope: topology: single-card; precision: FP8
- Topics: triton, tpc-c, tpc-clang, synapseai, quantization, custom-ops
- Basis Entries: `gaudi-sw-suite-scope`, `gaudi2-repo-scope-and-baseline`
- Omitted private support records: 0

### Citations

- **Add experimental Gaudi2 backend support by yangzhuxinyzx · Pull Request #11545 · triton-lang/triton · GitHub** (`github-pr-triton-11545`)
  - Locator: https://github.com/triton-lang/triton/pull/11545
  - Support: Triton PR #11545 implements an experimental Gaudi2 backend lowering TTIR to TPC-C for SynapseAI 1.24.1, covering elementwise, RMSNorm, SiLU-and-mul, and FP8 quantization, but was closed unmerged by upstream maintainers.
