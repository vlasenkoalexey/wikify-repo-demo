---
title: PJRT client — the libtpu runtime layer
type: concept
provenance: mixed
concept: mini_pytorch_xla-pjrt
updated: 2026-06-27
status: fresh
---
# PJRT client — the libtpu runtime layer

## Overview
`pjrt.py` is the entire *runtime* of mini-pytorch-xla: the seam where Python stops
and the TPU begins. It dials `libtpu.so` directly through its PJRT C API — the same
plugin PyTorch/XLA and JAX load — with **zero** dependency on torch_xla or jax, using
nothing but `ctypes`. The key design idea is uniformity: every PJRT entry point has
the identical C signature `PJRT_Error* fn(FOO_Args*)`, where the args struct opens
with `{size_t struct_size; void* extension_start; …}` and a NULL return means
success. Because of that regularity the whole API surface collapses to one
function-table struct ([`PJRT_Api`](../catalog/mini_pytorch_xla/pjrt.md#PJRT_Api)),
one calling convention, and a handful of per-call `*_Args` structs. The four verbs
the rest of the project ever needs are host→device
([`from_host`](../catalog/mini_pytorch_xla/pjrt.md#PjrtClient.from_host)), compile
([`compile`](../catalog/mini_pytorch_xla/pjrt.md#PjrtClient.compile)), execute
([`_execute`](../catalog/mini_pytorch_xla/pjrt.md#PjrtClient._execute)), and
device→host ([`_buffer_to_host`](../catalog/mini_pytorch_xla/pjrt.md#PjrtClient._buffer_to_host)) —
everything else is plumbing around those.

A tensor never lives "in Python." A
[`Buffer`](../catalog/mini_pytorch_xla/pjrt.md#Buffer) is just a thin handle to bytes
in TPU HBM (a `PJRT_Buffer*`); its only state is an opaque pointer plus the
[`shape`](../catalog/mini_pytorch_xla/pjrt.md#Buffer.shape) and dtype Python remembers
so it can allocate the right numpy array on the way back. All real compute happens on
the chip, and `pjrt.py` is the courier.

## Diagram
```mermaid
flowchart TD
  subgraph host[Host / Python]
    np[np.ndarray]
    out[np.ndarray result]
  end
  subgraph client[PjrtClient over libtpu]
    fh[from_host]
    cmp[compile]
    ex[_execute]
    wrap[_wrap_output]
    toh[_buffer_to_host]
    dev[_first_device]
  end
  subgraph tpu[TPU HBM]
    bufin[Buffer in]
    exe[Executable]
    bufout[Buffer out]
  end
  np --> fh -->|PJRT_Client_BufferFromHostBuffer| bufin
  dev -. self._device .-> fh
  cmp -->|PJRT_Client_Compile| exe
  bufin --> ex
  exe --> ex -->|PJRT_LoadedExecutable_Execute| bufout
  bufout --> wrap -->|Dimensions + ElementType| Buffer
  bufout --> toh -->|PJRT_Buffer_ToHostBuffer| out
```

## Design rationale (why it's built this way)
The whole file is an exercise in *not* taking a dependency. The module docstring is
explicit that this is "the equivalent of PyTorch/XLA's
`torch_xla/csrc/runtime` PjRt computation client, but in pure Python," talking
"straight to `libtpu.so`'s PJRT C API (`GetPjrtApi`)." That forces three notable
choices.

First, **the API is modeled, not bound.** Rather than declaring each function's
signature, the code lays out the function-table struct
[`PJRT_Api`](../catalog/mini_pytorch_xla/pjrt.md#PJRT_Api) field-by-field in the exact
order of `pjrt_c_api.h` (v0.72), with every entry typed as a raw `c_vp`
([`c_vp`](../catalog/mini_pytorch_xla/pjrt.md#c_vp)) function pointer. The header
comment warns the order is "load-bearing — it mirrors the header": one inserted field
shifts every later pointer. The version prefix
[`_ApiVersion`](../catalog/mini_pytorch_xla/pjrt.md#_ApiVersion) sits at the front of
the table for the same reason — its offset must match the C layout exactly.

Second, **every call is the same call.** Each `*_Args` struct — e.g.
[`_BufferFromHost_Args`](../catalog/mini_pytorch_xla/pjrt.md#_BufferFromHost_Args),
[`_Compile_Args`](../catalog/mini_pytorch_xla/pjrt.md#_Compile_Args),
[`_ExecuteOptions`](../catalog/mini_pytorch_xla/pjrt.md#_ExecuteOptions) — begins with
the same `(struct_size, extension_start)` header (`_args_header` fills `struct_size`
via `ctypes.sizeof` so the plugin can do forward/backward-compatible field detection).
`struct_size` is a [`c_sz`](../catalog/mini_pytorch_xla/pjrt.md#c_sz). This is why a
generic `_raw_call(name, args)` can drive any entry point: fill the struct, pass it by
reference, NULL means success.

Third, **no protobuf.** Compile options would normally be a serialized
`CompileOptionsProto`; instead the code hand-emits four bytes of varint-encoded
protobuf (`num_replicas=1`, `num_partitions=1`) so it needn't link protobuf at all.

> [!inferred]
> Typing every table entry as an untyped `c_vp` means ctypes does no argument
> checking at the boundary — correctness rests entirely on the struct layouts
> matching `pjrt_c_api.h`. That is the price of the zero-dependency design: a header
> version skew would surface as a memory-corruption crash, not a clean error.

## Entry points
- [`from_host`](../catalog/mini_pytorch_xla/pjrt.md#PjrtClient.from_host) — the host→device
  on-ramp. Everything that puts data on the TPU funnels here: constants via
  [`const`](../catalog/mini_pytorch_xla/ops.md#const), numpy arrays via
  [`from_np`](../catalog/mini_pytorch_xla/ops.md#from_np), and test probes like
  [`bb`](../catalog/tests/probe_add.md#bb). It returns a fresh
  [`Buffer`](../catalog/mini_pytorch_xla/pjrt.md#Buffer).
- [`compile`](../catalog/mini_pytorch_xla/pjrt.md#PjrtClient.compile) and
  [`execute`](../catalog/mini_pytorch_xla/pjrt.md#Executable.execute) /
  [`_execute`](../catalog/mini_pytorch_xla/pjrt.md#PjrtClient._execute) — the compute path.
  Reached through [`run`](../catalog/mini_pytorch_xla/hlo.md#run) in `hlo.py`, which
  caches the [`compile`](../catalog/mini_pytorch_xla/pjrt.md#PjrtClient.compile) result
  per StableHLO text and then calls `execute`. Every op in `ops.py` —
  [`binary`](../catalog/mini_pytorch_xla/ops.md#binary),
  [`unary`](../catalog/mini_pytorch_xla/ops.md#unary),
  [`reshape`](../catalog/mini_pytorch_xla/ops.md#reshape),
  [`transpose`](../catalog/mini_pytorch_xla/ops.md#transpose),
  [`compare`](../catalog/mini_pytorch_xla/ops.md#compare),
  [`select`](../catalog/mini_pytorch_xla/ops.md#select),
  [`reduce`](../catalog/mini_pytorch_xla/ops.md#reduce),
  [`broadcast_to`](../catalog/mini_pytorch_xla/ops.md#broadcast_to),
  [`slice_dim`](../catalog/mini_pytorch_xla/ops.md#slice_dim),
  [`erf`](../catalog/mini_pytorch_xla/ops.md#erf),
  [`gather_rows`](../catalog/mini_pytorch_xla/ops.md#gather_rows),
  [`_dot_general`](../catalog/mini_pytorch_xla/ops.md#_dot_general) — emits StableHLO
  text and lands here.
- [`Buffer.to_numpy`](../catalog/mini_pytorch_xla/pjrt.md#Buffer) →
  [`_buffer_to_host`](../catalog/mini_pytorch_xla/pjrt.md#PjrtClient._buffer_to_host) —
  the device→host off-ramp, the only way bytes leave the chip. It allocates a host
  array sized by the buffer's [`shape`](../catalog/mini_pytorch_xla/pjrt.md#Buffer.shape).
- [`_first_device`](../catalog/mini_pytorch_xla/pjrt.md#PjrtClient._first_device) — runs
  once at client construction to pick the device every later
  [`from_host`](../catalog/mini_pytorch_xla/pjrt.md#PjrtClient.from_host) targets via
  [`_AddressableDevices_Args`](../catalog/mini_pytorch_xla/pjrt.md#_AddressableDevices_Args).

## Mechanism (step-by-step)
1. **Client bring-up and device discovery.** Constructing the client loads `libtpu.so`,
   resolves `GetPjrtApi` into a `POINTER(PJRT_Api)`, then runs the mandatory
   `Plugin_Initialize` → `Client_Create` sequence
   ([`_Client_Create_Args`](../catalog/mini_pytorch_xla/pjrt.md#_Client_Create_Args)).
   It then calls [`_first_device`](../catalog/mini_pytorch_xla/pjrt.md#PjrtClient._first_device),
   which queries `PJRT_Client_AddressableDevices`, raises if there are zero TPU
   devices, and casts the returned array to grab `dev_array[0]`. That handle is cached
   as `self._device` — single-device by construction.

2. **Upload (host → HBM).** [`from_host`](../catalog/mini_pytorch_xla/pjrt.md#PjrtClient.from_host)
   forces the numpy array contiguous, maps its dtype into the PJRT element-type enum
   (rejecting anything unsupported), and packs shape/dtype/data-pointer/device into a
   [`_BufferFromHost_Args`](../catalog/mini_pytorch_xla/pjrt.md#_BufferFromHost_Args). It
   sets `host_buffer_semantics` to *kImmutableUntilTransferCompletes*, fires
   `PJRT_Client_BufferFromHostBuffer`, then **awaits `done_with_host_buffer`** before
   returning — the comment notes it's only "safe to free `arr` after this." The result
   is wrapped in a [`Buffer`](../catalog/mini_pytorch_xla/pjrt.md#Buffer) carrying the
   device handle plus the original [`shape`](../catalog/mini_pytorch_xla/pjrt.md#Buffer.shape)
   and dtype.

3. **Compile (StableHLO → Executable).** [`compile`](../catalog/mini_pytorch_xla/pjrt.md#PjrtClient.compile)
   UTF-8-encodes the StableHLO text, declares format `b"mlir"`, attaches the
   hand-rolled compile-options bytes, and calls `PJRT_Client_Compile` through a
   [`_Compile_Args`](../catalog/mini_pytorch_xla/pjrt.md#_Compile_Args). It returns an
   [`Executable`](../catalog/mini_pytorch_xla/pjrt.md#Executable.execute) holding the
   `PJRT_LoadedExecutable*` and the declared output count. Compilation is expensive, so
   [`run`](../catalog/mini_pytorch_xla/hlo.md#run) memoizes executables keyed on the
   exact module text — identical ops recompile zero times.

4. **Execute (run on TPU).** [`_execute`](../catalog/mini_pytorch_xla/pjrt.md#PjrtClient._execute)
   builds the doubly-indirect argument layout PJRT expects: an array of input buffer
   handles ([`c_vp`](../catalog/mini_pytorch_xla/pjrt.md#c_vp)) wrapped in a
   one-element list-of-lists (one device), parallel output and completion-event arrays,
   and a default [`_ExecuteOptions`](../catalog/mini_pytorch_xla/pjrt.md#_ExecuteOptions).
   It calls `PJRT_LoadedExecutable_Execute`, **awaits the device-completion event**, and
   then wraps each raw output handle.

5. **Self-describing outputs.** The execute call hands back bare `PJRT_Buffer*`
   pointers with no shape attached, so
   [`_wrap_output`](../catalog/mini_pytorch_xla/pjrt.md#PjrtClient._wrap_output) asks the
   device: `PJRT_Buffer_Dimensions` via
   [`_Buffer_Dimensions_Args`](../catalog/mini_pytorch_xla/pjrt.md#_Buffer_Dimensions_Args)
   for the shape and `PJRT_Buffer_ElementType` via
   [`_Buffer_ElementType_Args`](../catalog/mini_pytorch_xla/pjrt.md#_Buffer_ElementType_Args)
   for the dtype, then reconstructs a [`Buffer`](../catalog/mini_pytorch_xla/pjrt.md#Buffer).
   Shape information round-trips *through the device*, not through Python bookkeeping.

6. **Readback (HBM → host).** [`_buffer_to_host`](../catalog/mini_pytorch_xla/pjrt.md#PjrtClient._buffer_to_host)
   pre-allocates a host array of the right [`shape`](../catalog/mini_pytorch_xla/pjrt.md#Buffer.shape)
   and dtype, then — crucially — requests an explicit **row-major host layout** built by
   `_rowmajor_layout` into a [`_MemoryLayout`](../catalog/mini_pytorch_xla/pjrt.md#_MemoryLayout).
   The comment explains why: "XLA may keep a transpose as a pure layout change on
   device, so without this the bytes come back un-permuted." Forcing descending
   `minor_to_major` makes PJRT physically materialize the standard layout. It calls
   `PJRT_Buffer_ToHostBuffer`, awaits the event, and returns the populated array.

## Key data structures
- [`Buffer`](../catalog/mini_pytorch_xla/pjrt.md#Buffer) — the central value type: an
  opaque device handle `_h`, the [`shape`](../catalog/mini_pytorch_xla/pjrt.md#Buffer.shape),
  the numpy dtype, and a `_deleted` flag. Its `delete`/`__del__` issue
  `PJRT_Buffer_Destroy` ([`_Buffer_Destroy_Args`](../catalog/mini_pytorch_xla/pjrt.md#_Buffer_Destroy_Args)),
  so HBM is freed when the Python handle is collected.
- [`PJRT_Api`](../catalog/mini_pytorch_xla/pjrt.md#PJRT_Api) — the order-sensitive
  function-pointer table, fronted by [`_ApiVersion`](../catalog/mini_pytorch_xla/pjrt.md#_ApiVersion);
  the single source of every callable entry.
- The `*_Args` structs are the only ABI contract that matters at runtime — each is a
  flat C layout the plugin reads in place:
  [`_BufferFromHost_Args`](../catalog/mini_pytorch_xla/pjrt.md#_BufferFromHost_Args),
  [`_Compile_Args`](../catalog/mini_pytorch_xla/pjrt.md#_Compile_Args),
  [`_ExecuteOptions`](../catalog/mini_pytorch_xla/pjrt.md#_ExecuteOptions),
  [`_Buffer_Dimensions_Args`](../catalog/mini_pytorch_xla/pjrt.md#_Buffer_Dimensions_Args),
  [`_Buffer_ElementType_Args`](../catalog/mini_pytorch_xla/pjrt.md#_Buffer_ElementType_Args),
  [`_AddressableDevices_Args`](../catalog/mini_pytorch_xla/pjrt.md#_AddressableDevices_Args),
  [`_MemoryLayout`](../catalog/mini_pytorch_xla/pjrt.md#_MemoryLayout),
  [`_MemoryStats_Args`](../catalog/mini_pytorch_xla/pjrt.md#_MemoryStats_Args),
  [`_Event_Args`](../catalog/mini_pytorch_xla/pjrt.md#_Event_Args).

## Dynamics (design intent)
The runtime is **synchronous at every boundary** even though PJRT is event-based. Each
data-moving call returns a completion event, and the client immediately awaits (then
destroys) it: [`from_host`](../catalog/mini_pytorch_xla/pjrt.md#PjrtClient.from_host)
awaits `done_with_host_buffer`, [`_execute`](../catalog/mini_pytorch_xla/pjrt.md#PjrtClient._execute)
awaits the device-completion event, and
[`_buffer_to_host`](../catalog/mini_pytorch_xla/pjrt.md#PjrtClient._buffer_to_host)
awaits the transfer event. That makes the await inside execute a true wall-clock
measurement of device compute — which is exactly what
[`run`](../catalog/mini_pytorch_xla/hlo.md#run) relies on to time ops. Concurrency is
deliberately absent: the client is a process-wide singleton over a single device
(`self._device`), since the TPU chips are a shared resource.

## Edge cases
- **Layout surprise on readback.** Without the forced row-major host layout in
  [`_buffer_to_host`](../catalog/mini_pytorch_xla/pjrt.md#PjrtClient._buffer_to_host), a
  device-side transpose that XLA implemented as a metadata-only layout change would
  return bytes in the wrong order. Scalars (`shape == ()`) skip the layout entirely.
- **Dtype gate.** [`from_host`](../catalog/mini_pytorch_xla/pjrt.md#PjrtClient.from_host)
  raises on any dtype outside the PJRT enum map; bf16, for instance, is not in the
  host-side table.
- **Unknown output dtype.** [`_wrap_output`](../catalog/mini_pytorch_xla/pjrt.md#PjrtClient._wrap_output)
  falls back to `float32` if the device reports an element type the reverse map doesn't
  recognize, rather than failing.

## Open questions
- The PJRT plugin's own asynchrony is unused here — whether overlapping uploads with
  execution would help is outside what the synchronous source shows.
- `_Counters` tracks uploads/executes/readbacks for proof tooling, but the source in
  this packet doesn't reveal which tests assert on those counts.

## See also
- [`mini_pytorch_xla-ops`](./mini_pytorch_xla-ops.md) — the StableHLO emitters that feed
  [`compile`](../catalog/mini_pytorch_xla/pjrt.md#PjrtClient.compile).
- [`mini_pytorch_xla-backend`](./mini_pytorch_xla-backend.md) — the ATen ops layer that
  drives these buffers.
- [`mini_pytorch_xla-hlo`](./mini_pytorch_xla-hlo.md) — the compile cache and timing
  wrapper around [`run`](../catalog/mini_pytorch_xla/hlo.md#run).
