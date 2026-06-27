---
title: 'Module: mini_pytorch_xla/hlo.py'
type: catalog
provenance: extracted
module: mini_pytorch_xla/hlo.py
status: fresh
symbol_base: scip-python python mini_pytorch_xla 0.0.0 `mini_pytorch_xla.hlo`/
symbols:
  ttype: ttype().
  run: run().
  set_timer: set_timer().
  _EXE_CACHE._EXE_CACHE: _EXE_CACHE._EXE_CACHE.
  _TIMER: _TIMER.
  mlir_dtype: mlir_dtype().
  _NP_TO_MLIR: _NP_TO_MLIR.
  _op_kind: _op_kind().
---
# Module: [`mini_pytorch_xla/hlo.py`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/hlo.py)

## Functions
- `_op_kind(text: str)` — [`L48`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/hlo.py#L48)
- `mlir_dtype(dt)` — [`L25`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/hlo.py#L25)
- `run(module_text: str, inputs: list[pjrt.Buffer], n_out: int = 1)` — [`L55`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/hlo.py#L55) — Compile (cached) and execute a StableHLO module on the TPU. — documented in [mini_pytorch_xla-ops](../../concepts/mini_pytorch_xla-ops.md)
- `set_timer(fn)` — [`L43`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/hlo.py#L43)
- `ttype(shape, dt)` — [`L29`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/hlo.py#L29) — MLIR tensor type, e.g. (2,3),f32 -> 'tensor<2x3xf32>'; () -> 'tensor<f32>'. — documented in [mini_pytorch_xla-ops](../../concepts/mini_pytorch_xla-ops.md)

## Module values
- `_EXE_CACHE` — [`L37`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/hlo.py#L37)
- `_NP_TO_MLIR` — [`L17`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/hlo.py#L17)
- `_TIMER` — [`L40`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/hlo.py#L40)

