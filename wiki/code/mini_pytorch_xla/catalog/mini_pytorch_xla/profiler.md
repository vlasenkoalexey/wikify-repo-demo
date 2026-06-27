---
title: 'Module: mini_pytorch_xla/profiler.py'
type: catalog
provenance: extracted
module: mini_pytorch_xla/profiler.py
status: fresh
symbol_base: scip-python python mini_pytorch_xla 0.0.0 `mini_pytorch_xla.profiler`/
symbols:
  c_vp: c_vp.
  Trace._opts: Trace#_opts.
  Trace.__exit__: Trace#__exit__().
  Trace._call: Trace#_call().
  Trace._api: Trace#_api.
  c_sz: c_sz.
  _find_profiler_api: _find_profiler_api().
  OpProfile._record: OpProfile#_record().
  _vint: _vint().
  _ProfilerExt: _ProfilerExt#
  _ld: _ld().
  build_xspace: build_xspace().
  matmul_throughput: matmul_throughput().
  _Profiler_Args: _Profiler_Args#
  _hdr: _hdr().
  _ProfilerApi: _ProfilerApi#
  _CollectData_Args: _CollectData_Args#
  OpProfile.report: OpProfile#report().
  _str: _str().
  _ExtBase: _ExtBase#
  _Create_Args: _Create_Args#
  _Err_Msg_Args: _Err_Msg_Args#
  _Err_Destroy_Args: _Err_Destroy_Args#
  Trace._profiler: Trace#_profiler.
  OpProfile.write_xspace: OpProfile#write_xspace().
  _FN: _FN.
  OpProfile.__enter__: OpProfile#__enter__().
  _varint: _varint().
  OpProfile.calls: OpProfile#calls.
  OpProfile.secs: OpProfile#secs.
  OpProfile.__exit__: OpProfile#__exit__().
  Trace.data: Trace#data.
  OpProfile: OpProfile#
  OpProfile.events: OpProfile#events.
  c_i64: c_i64.
  _EXT_PROFILER: _EXT_PROFILER.
  Trace.out_path: Trace#out_path.
  OpProfile.compiles: OpProfile#compiles.
  _ExtBase._fields_: _ExtBase#_fields_.
  _ProfilerExt._fields_: _ProfilerExt#_fields_.
  _ProfilerApi._fields_: _ProfilerApi#_fields_.
  _Create_Args._fields_: _Create_Args#_fields_.
  _Profiler_Args._fields_: _Profiler_Args#_fields_.
  _CollectData_Args._fields_: _CollectData_Args#_fields_.
  _Err_Msg_Args._fields_: _Err_Msg_Args#_fields_.
  _Err_Destroy_Args._fields_: _Err_Destroy_Args#_fields_.
  Trace: Trace#
  Trace.__init__: Trace#__init__().
  Trace.__enter__: Trace#__enter__().
  OpProfile.__init__: OpProfile#__init__().
  summarize_xspace: summarize_xspace().
---
# Module: [`mini_pytorch_xla/profiler.py`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/profiler.py)

## Classes
### `OpProfile`
- def: [`mini_pytorch_xla/profiler.py:198`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/profiler.py#L198)
- doc: On-device operator timing profile. Each timed op's wall-time includes the
- signature: `class OpProfile:`
- members:
  - `report(self)` — [`L236`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/profiler.py#L236)
  - `write_xspace(self, logdir, run="minixla")` — [`L226`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/profiler.py#L226) — Write the timeline as <logdir>/plugins/profile/<run>/<host>.xplane.pb (xprof).
  - `calls` — [`L204`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/profiler.py#L204)
  - `compiles` — [`L206`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/profiler.py#L206)
  - `events` — [`L207`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/profiler.py#L207)
  - `secs` — [`L205`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/profiler.py#L205)
- protocol/private: `__enter__`[`L209`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/profiler.py#L209), `__exit__`[`L214`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/profiler.py#L214), `__init__`[`L202`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/profiler.py#L202), `_record`[`L219`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/profiler.py#L219)
- uses (calls/refs, reference-scoped): [`build_xspace`](profiler.md#build_xspace), [`set_timer`](hlo.md#set_timer)
- used by: (2 test-only callers)

### `Trace`
- def: [`mini_pytorch_xla/profiler.py:96`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/profiler.py#L96)
- doc: Context manager: capture a TPU XSpace trace of the enclosed work.
- signature: `class Trace:`
- members:
  - `data` — [`L103`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/profiler.py#L103) — documented in [mini_pytorch_xla-profiler](../../concepts/mini_pytorch_xla-profiler.md)
  - `out_path` — [`L100`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/profiler.py#L100) — documented in [mini_pytorch_xla-profiler](../../concepts/mini_pytorch_xla-profiler.md)
- protocol/private: `__enter__`[`L115`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/profiler.py#L115), `__exit__`[`L127`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/profiler.py#L127), `__init__`[`L99`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/profiler.py#L99), `_api`[`L101`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/profiler.py#L101), `_call`[`L105`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/profiler.py#L105), `_opts`[`L117`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/profiler.py#L117), `_profiler`[`L102`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/profiler.py#L102)
- uses (calls/refs, reference-scoped): [`c_vp`](profiler.md#c_vp), [`client`](pjrt.md#client), [`_find_profiler_api`](profiler.md#_find_profiler_api), [`_Profiler_Args`](profiler.md#_Profiler_Args), [`_hdr`](profiler.md#_hdr), [`_CollectData_Args`](profiler.md#_CollectData_Args), [`_Create_Args`](profiler.md#_Create_Args), [`_Err_Destroy_Args`](profiler.md#_Err_Destroy_Args), [`_Err_Msg_Args`](profiler.md#_Err_Msg_Args), [`_FN`](profiler.md#_FN)

### `_CollectData_Args`  ·  implements/extends Structure
- def: [`mini_pytorch_xla/profiler.py:63`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/profiler.py#L63) — documented in [mini_pytorch_xla-profiler](../../concepts/mini_pytorch_xla-profiler.md)
- signature: `class _CollectData_Args(ctypes.Structure):`
- protocol/private: `_fields_`[`L64`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/profiler.py#L64)
- uses (calls/refs, reference-scoped): [`c_vp`](profiler.md#c_vp), [`c_sz`](profiler.md#c_sz)
- used by: [`__exit__`](profiler.md#Trace.__exit__)

### `_Create_Args`  ·  implements/extends Structure
- def: [`mini_pytorch_xla/profiler.py:54`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/profiler.py#L54) — documented in [mini_pytorch_xla-profiler](../../concepts/mini_pytorch_xla-profiler.md)
- signature: `class _Create_Args(ctypes.Structure):`
- protocol/private: `_fields_`[`L55`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/profiler.py#L55)
- uses (calls/refs, reference-scoped): [`c_vp`](profiler.md#c_vp), [`c_sz`](profiler.md#c_sz)
- used by: [`_opts`](profiler.md#Trace._opts)

### `_Err_Destroy_Args`  ·  implements/extends Structure
- def: [`mini_pytorch_xla/profiler.py:73`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/profiler.py#L73) — documented in [mini_pytorch_xla-profiler](../../concepts/mini_pytorch_xla-profiler.md)
- signature: `class _Err_Destroy_Args(ctypes.Structure):`
- protocol/private: `_fields_`[`L74`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/profiler.py#L74)
- uses (calls/refs, reference-scoped): [`c_vp`](profiler.md#c_vp), [`c_sz`](profiler.md#c_sz)
- used by: [`_call`](profiler.md#Trace._call)

### `_Err_Msg_Args`  ·  implements/extends Structure
- def: [`mini_pytorch_xla/profiler.py:68`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/profiler.py#L68) — documented in [mini_pytorch_xla-profiler](../../concepts/mini_pytorch_xla-profiler.md)
- signature: `class _Err_Msg_Args(ctypes.Structure):`
- protocol/private: `_fields_`[`L69`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/profiler.py#L69)
- uses (calls/refs, reference-scoped): [`c_vp`](profiler.md#c_vp), [`c_sz`](profiler.md#c_sz)
- used by: [`_call`](profiler.md#Trace._call)

### `_ExtBase`  ·  implements/extends Structure
- def: [`mini_pytorch_xla/profiler.py:37`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/profiler.py#L37) — documented in [mini_pytorch_xla-profiler](../../concepts/mini_pytorch_xla-profiler.md)
- signature: `class _ExtBase(ctypes.Structure):`
- protocol/private: `_fields_`[`L38`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/profiler.py#L38)
- uses (calls/refs, reference-scoped): [`c_vp`](profiler.md#c_vp), [`c_sz`](profiler.md#c_sz)
- used by: [`_find_profiler_api`](profiler.md#_find_profiler_api)

### `_ProfilerApi`  ·  implements/extends Structure
- def: [`mini_pytorch_xla/profiler.py:46`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/profiler.py#L46) — documented in [mini_pytorch_xla-profiler](../../concepts/mini_pytorch_xla-profiler.md)
- signature: `class _ProfilerApi(ctypes.Structure):`
- protocol/private: `_fields_`[`L48`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/profiler.py#L48)
- uses (calls/refs, reference-scoped): [`c_vp`](profiler.md#c_vp), [`c_sz`](profiler.md#c_sz)
- used by: [`_find_profiler_api`](profiler.md#_find_profiler_api)

### `_ProfilerExt`  ·  implements/extends Structure
- def: [`mini_pytorch_xla/profiler.py:41`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/profiler.py#L41) — documented in [mini_pytorch_xla-profiler](../../concepts/mini_pytorch_xla-profiler.md)
- signature: `class _ProfilerExt(ctypes.Structure):`
- protocol/private: `_fields_`[`L42`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/profiler.py#L42)
- uses (calls/refs, reference-scoped): [`c_vp`](profiler.md#c_vp), [`c_sz`](profiler.md#c_sz), [`c_i64`](profiler.md#c_i64)
- used by: [`_find_profiler_api`](profiler.md#_find_profiler_api)

### `_Profiler_Args`  ·  implements/extends Structure
- def: [`mini_pytorch_xla/profiler.py:59`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/profiler.py#L59) — documented in [mini_pytorch_xla-profiler](../../concepts/mini_pytorch_xla-profiler.md)
- signature: `class _Profiler_Args(ctypes.Structure):`
- protocol/private: `_fields_`[`L60`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/profiler.py#L60)
- uses (calls/refs, reference-scoped): [`c_vp`](profiler.md#c_vp), [`c_sz`](profiler.md#c_sz)
- used by: [`_opts`](profiler.md#Trace._opts), [`__exit__`](profiler.md#Trace.__exit__)

## Functions
- `_find_profiler_api(client)` — [`L85`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/profiler.py#L85) — documented in [mini_pytorch_xla-profiler](../../concepts/mini_pytorch_xla-profiler.md)
- `_hdr(s)` — [`L80`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/profiler.py#L80) — documented in [mini_pytorch_xla-profiler](../../concepts/mini_pytorch_xla-profiler.md)
- `_ld(field, data)` — [`L166`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/profiler.py#L166)
- `_str(field, s)` — [`L170`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/profiler.py#L170)
- `_varint(n: int)` — [`L151`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/profiler.py#L151)
- `_vint(field, val)` — [`L162`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/profiler.py#L162)
- `build_xspace(events, plane="/device:TPU:0", line="XLA Ops", host="tpu")` — [`L174`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/profiler.py#L174) — events: list of (op_name, duration_seconds) in execution order.
- `matmul_throughput(n: int = 2048, iters: int = 50)` — [`L247`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/profiler.py#L247) — Measured GFLOP/s of an n×n matmul on the TPU (proof of real compute).
- `summarize_xspace(data: bytes)` — [`L264`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/profiler.py#L264) — Dependency-free scan of a serialized XSpace: device planes + op-name events.

## Module values
- `_EXT_PROFILER` — [`L34`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/profiler.py#L34) — documented in [mini_pytorch_xla-profiler](../../concepts/mini_pytorch_xla-profiler.md)
- `_FN` — [`L77`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/profiler.py#L77) — documented in [mini_pytorch_xla-profiler](../../concepts/mini_pytorch_xla-profiler.md)
- `c_i64` — [`L32`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/profiler.py#L32) — documented in [mini_pytorch_xla-profiler](../../concepts/mini_pytorch_xla-profiler.md)
- `c_sz` — [`L30`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/profiler.py#L30) — documented in [mini_pytorch_xla-profiler](../../concepts/mini_pytorch_xla-profiler.md)
- `c_vp` — [`L31`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/profiler.py#L31) — documented in [mini_pytorch_xla-profiler](../../concepts/mini_pytorch_xla-profiler.md)

