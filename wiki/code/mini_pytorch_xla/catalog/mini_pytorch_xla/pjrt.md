---
title: 'Module: mini_pytorch_xla/pjrt.py'
type: catalog
provenance: extracted
module: mini_pytorch_xla/pjrt.py
status: fresh
symbol_base: scip-python python mini_pytorch_xla 0.0.0 `mini_pytorch_xla.pjrt`/
symbols:
  c_vp: c_vp.
  Buffer.shape: Buffer#shape.
  c_sz: c_sz.
  Buffer: Buffer#
  PjrtClient.from_host: PjrtClient#from_host().
  PjrtClient._execute: PjrtClient#_execute().
  PjrtClient._buffer_to_host: PjrtClient#_buffer_to_host().
  _NP_TO_PJRT: _NP_TO_PJRT.
  Buffer.dtype: Buffer#dtype.
  PjrtClient.compile: PjrtClient#compile().
  c_i64: c_i64.
  _args_header: _args_header().
  PjrtClient._raw_call: PjrtClient#_raw_call().
  PjrtClient._first_device: PjrtClient#_first_device().
  PjrtClient._wrap_output: PjrtClient#_wrap_output().
  PjrtClient._fn: PjrtClient#_fn().
  Buffer.delete: Buffer#delete().
  PjrtClient._check_error: PjrtClient#_check_error().
  PjrtClient._await: PjrtClient#_await().
  client: client().
  PjrtClient.counters: PjrtClient#counters.
  _MemoryLayout: _MemoryLayout#
  PjrtClient._fns: PjrtClient#_fns.
  PJRT_Api: PJRT_Api#
  _BufferFromHost_Args: _BufferFromHost_Args#
  PjrtClient.device_kind: PjrtClient#device_kind().
  PjrtClient.num_devices: PjrtClient#num_devices().
  Executable.execute: Executable#execute().
  PjrtClient._call: PjrtClient#_call().
  PjrtClient._api: PjrtClient#_api.
  PjrtClient.memory_stats: PjrtClient#memory_stats().
  _ApiVersion: _ApiVersion#
  _ExecuteOptions: _ExecuteOptions#
  _Buffer_Dimensions_Args: _Buffer_Dimensions_Args#
  _MemoryStats_Args: _MemoryStats_Args#
  _Buffer_ElementType_Args: _Buffer_ElementType_Args#
  _Counters.reset: _Counters#reset().
  PjrtClient.platform_name: PjrtClient#platform_name().
  Buffer.to_numpy: Buffer#to_numpy().
  c_int: c_int.
  _AddressableDevices_Args: _AddressableDevices_Args#
  _Event_Args: _Event_Args#
  PjrtClient._lib: PjrtClient#_lib.
  _GLOBAL._GLOBAL: _GLOBAL._GLOBAL.
  _Client_Create_Args: _Client_Create_Args#
  _Plugin_Initialize_Args: _Plugin_Initialize_Args#
  _Program: _Program#
  _Compile_Args: _Compile_Args#
  _Execute_Args: _Execute_Args#
  _ToHost_Args: _ToHost_Args#
  _PlatformName_Args: _PlatformName_Args#
  _GetDescription_Args: _GetDescription_Args#
  _Kind_Args: _Kind_Args#
  _rowmajor_layout: _rowmajor_layout().
  _Error_Message_Args: _Error_Message_Args#
  _Error_Destroy_Args: _Error_Destroy_Args#
  _Buffer_Destroy_Args: _Buffer_Destroy_Args#
  PjrtClient._device: PjrtClient#_device.
  PjrtError: PjrtError#
  PjrtClient._client: PjrtClient#_client.
  PjrtClient: PjrtClient#
  _Counters.readbacks: _Counters#readbacks.
  Buffer._h: Buffer#_h.
  Executable: Executable#
  _PJRT_FN: _PJRT_FN.
  _PJRT_TO_NP: _PJRT_TO_NP.
  _Counters.executes: _Counters#executes.
  Buffer.__init__: Buffer#__init__().
  Buffer.__del__: Buffer#__del__().
  Executable.__init__: Executable#__init__().
  Buffer._client: Buffer#_client.
  Buffer._deleted: Buffer#_deleted.
  _Counters.uploads: _Counters#uploads.
  _FN_NAMES: _FN_NAMES.
  _HBS_UNTIL_DONE: _HBS_UNTIL_DONE.
  _compile_options_bytes: _compile_options_bytes().
  _find_libtpu: _find_libtpu().
  Executable._client: Executable#_client.
  Executable._h: Executable#_h.
  Executable.num_outputs: Executable#num_outputs.
  _Counters: _Counters#
  PRED: PRED.
  S8: S8.
  S16: S16.
  S32: S32.
  S64: S64.
  U8: U8.
  F16: F16.
  F32: F32.
  F64: F64.
  _ApiVersion._fields_: _ApiVersion#_fields_.
  PJRT_Api._fields_: PJRT_Api#_fields_.
  _Client_Create_Args._fields_: _Client_Create_Args#_fields_.
  _Plugin_Initialize_Args._fields_: _Plugin_Initialize_Args#_fields_.
  _AddressableDevices_Args._fields_: _AddressableDevices_Args#_fields_.
  _Program._fields_: _Program#_fields_.
  _Compile_Args._fields_: _Compile_Args#_fields_.
  _BufferFromHost_Args._fields_: _BufferFromHost_Args#_fields_.
  _ExecuteOptions._fields_: _ExecuteOptions#_fields_.
  _Execute_Args._fields_: _Execute_Args#_fields_.
  _ToHost_Args._fields_: _ToHost_Args#_fields_.
  _Buffer_Destroy_Args._fields_: _Buffer_Destroy_Args#_fields_.
  _Buffer_Dimensions_Args._fields_: _Buffer_Dimensions_Args#_fields_.
  _PlatformName_Args._fields_: _PlatformName_Args#_fields_.
  _GetDescription_Args._fields_: _GetDescription_Args#_fields_.
  _Kind_Args._fields_: _Kind_Args#_fields_.
  _MemoryStats_Args._fields_: _MemoryStats_Args#_fields_.
  _Buffer_ElementType_Args._fields_: _Buffer_ElementType_Args#_fields_.
  _Event_Args._fields_: _Event_Args#_fields_.
  _MemoryLayout._fields_: _MemoryLayout#_fields_.
  _Error_Message_Args._fields_: _Error_Message_Args#_fields_.
  _Error_Destroy_Args._fields_: _Error_Destroy_Args#_fields_.
  _Counters.__init__: _Counters#__init__().
  PjrtClient.__init__: PjrtClient#__init__().
  U16: U16.
  U32: U32.
  U64: U64.
  BF16: BF16.
---
# Module: [`mini_pytorch_xla/pjrt.py`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py)

## Classes
### `Buffer`
- def: [`mini_pytorch_xla/pjrt.py:175`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L175) — documented in [mini_pytorch_xla-backend](../../concepts/mini_pytorch_xla-backend.md)
- doc: A handle to a tensor living in TPU HBM (a PJRT_Buffer*).
- signature: `class Buffer:`
- members:
  - `delete(self)` — [`L188`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L188)
  - `to_numpy(self)` — [`L185`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L185)
  - `dtype` — [`L182`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L182) — documented in [mini_pytorch_xla-ops](../../concepts/mini_pytorch_xla-ops.md)
  - `shape` — [`L181`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L181) — documented in [mini_pytorch_xla-ops](../../concepts/mini_pytorch_xla-ops.md)
- protocol/private: `__del__`[`L194`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L194), `__init__`[`L178`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L178), `_client`[`L179`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L179), `_deleted`[`L183`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L183), `_h`[`L180`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L180)
- uses (calls/refs, reference-scoped): [`_buffer_to_host`](pjrt.md#PjrtClient._buffer_to_host), [`_call`](pjrt.md#PjrtClient._call), [`_Buffer_Destroy_Args`](pjrt.md#_Buffer_Destroy_Args), [`PjrtClient`](pjrt.md#PjrtClient)
- used by: [`binary`](ops.md#binary), [`from_host`](pjrt.md#PjrtClient.from_host), [`_execute`](pjrt.md#PjrtClient._execute), [`const`](ops.md#const), [`_buffer_to_host`](pjrt.md#PjrtClient._buffer_to_host), [`unary`](ops.md#unary), [`reshape`](ops.md#reshape), [`_embedding_backward`](backend.md#_embedding_backward), [`_var_mean`](backend.md#_var_mean), [`compare`](ops.md#compare), [`_mean_dim`](backend.md#_mean_dim), [`from_np`](ops.md#from_np), [`transpose`](ops.md#transpose), [`_mean_all`](backend.md#_mean_all), [`_mse_loss`](backend.md#_mse_loss), [`_threshold_backward`](backend.md#_threshold_backward), [`broadcast_to`](ops.md#broadcast_to), [`run`](hlo.md#run), [`_amax`](backend.md#_amax), [`_mse_loss_backward`](backend.md#_mse_loss_backward), [`_ones_like`](backend.md#_ones_like), [`_sum_dim`](backend.md#_sum_dim), [`_view`](backend.md#_view), [`_zeros_like`](backend.md#_zeros_like), [`reduce`](ops.md#reduce), [`_wrap_output`](pjrt.md#PjrtClient._wrap_output), [`_expand`](backend.md#_expand), [`_izero`](backend.md#_izero), [`_permute`](backend.md#_permute), [`_squeeze`](backend.md#_squeeze), [`_sum_all`](backend.md#_sum_all), [`_t`](backend.md#_t), [`_transpose`](backend.md#_transpose), [`_unsqueeze`](backend.md#_unsqueeze), [`gather_rows`](ops.md#gather_rows), [`select`](ops.md#select), [`erf`](ops.md#erf), [`slice_dim`](ops.md#slice_dim), [`_dot_general`](ops.md#_dot_general), [`execute`](pjrt.md#Executable.execute)  (+1 more; 2 test-only)

### `Executable`
- def: [`mini_pytorch_xla/pjrt.py:201`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L201)
- doc: A compiled StableHLO program loaded on the TPU (a PJRT_LoadedExecutable*).
- signature: `class Executable:`
- members:
  - `execute(self, inputs: list[Buffer])` — [`L209`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L209) — documented in [mini_pytorch_xla-pjrt](../../concepts/mini_pytorch_xla-pjrt.md)
  - `num_outputs` — [`L207`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L207)
- protocol/private: `__init__`[`L204`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L204), `_client`[`L205`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L205), `_h`[`L206`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L206)
- uses (calls/refs, reference-scoped): [`Buffer`](pjrt.md#Buffer), [`_execute`](pjrt.md#PjrtClient._execute), [`PjrtClient`](pjrt.md#PjrtClient)
- used by: [`_execute`](pjrt.md#PjrtClient._execute), [`compile`](pjrt.md#PjrtClient.compile), [`run`](hlo.md#run), [`_EXE_CACHE`](hlo.md#_EXE_CACHE._EXE_CACHE)  (1 test-only)

### `PJRT_Api`  ·  implements/extends Structure
- def: [`mini_pytorch_xla/pjrt.py:105`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L105) — documented in [mini_pytorch_xla-pjrt](../../concepts/mini_pytorch_xla-pjrt.md)
- signature: `class PJRT_Api(ctypes.Structure):`
- protocol/private: `_fields_`[`L106`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L106)
- uses (calls/refs, reference-scoped): [`c_vp`](pjrt.md#c_vp), [`c_sz`](pjrt.md#c_sz), [`_ApiVersion`](pjrt.md#_ApiVersion), [`_FN_NAMES`](pjrt.md#_FN_NAMES)
- used by: [`_lib`](pjrt.md#PjrtClient._lib)

### `PjrtClient`
- def: [`mini_pytorch_xla/pjrt.py:373`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L373) — documented in [mini_pytorch_xla-profiler](../../concepts/mini_pytorch_xla-profiler.md)
- members:
  - `compile(self, stablehlo_text: str, num_outputs: int = 1)` — [`L510`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L510) — documented in [mini_pytorch_xla-pjrt](../../concepts/mini_pytorch_xla-pjrt.md)
  - `device_kind(self)` — [`L449`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L449)
  - `from_host(self, arr: np.ndarray)` — [`L471`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L471) — documented in [mini_pytorch_xla-backend](../../concepts/mini_pytorch_xla-backend.md)
  - `memory_stats(self)` — [`L461`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L461)
  - `num_devices(self)` — [`L455`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L455)
  - `platform_name(self)` — [`L445`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L445)
  - `counters` — [`L375`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L375)
- protocol/private: `__init__`[`L374`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L374), `_api`[`L379`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L379), `_await`[`L424`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L424), `_buffer_to_host`[`L493`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L493), `_call`[`L418`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L418), `_check_error`[`L401`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L401), `_client`[`L387`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L387), `_device`[`L388`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L388), `_execute`[`L527`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L527), `_first_device`[`L435`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L435), `_fn`[`L391`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L391), `_fns`[`L382`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L382), `_lib`[`L377`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L377), `_raw_call`[`L413`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L413), `_wrap_output`[`L552`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L552)
- uses (calls/refs, reference-scoped): [`c_vp`](pjrt.md#c_vp), [`shape`](pjrt.md#Buffer.shape), [`Buffer`](pjrt.md#Buffer), [`_NP_TO_PJRT`](pjrt.md#_NP_TO_PJRT), [`dtype`](pjrt.md#Buffer.dtype), [`_args_header`](pjrt.md#_args_header), [`c_i64`](pjrt.md#c_i64), [`PJRT_Api`](pjrt.md#PJRT_Api), [`_BufferFromHost_Args`](pjrt.md#_BufferFromHost_Args), [`_Buffer_Dimensions_Args`](pjrt.md#_Buffer_Dimensions_Args), [`_Buffer_ElementType_Args`](pjrt.md#_Buffer_ElementType_Args), [`_ExecuteOptions`](pjrt.md#_ExecuteOptions), [`_MemoryStats_Args`](pjrt.md#_MemoryStats_Args), [`_AddressableDevices_Args`](pjrt.md#_AddressableDevices_Args), [`_Event_Args`](pjrt.md#_Event_Args), [`_Client_Create_Args`](pjrt.md#_Client_Create_Args), [`_Compile_Args`](pjrt.md#_Compile_Args), [`_Error_Destroy_Args`](pjrt.md#_Error_Destroy_Args), [`_Error_Message_Args`](pjrt.md#_Error_Message_Args), [`_Execute_Args`](pjrt.md#_Execute_Args), [`_GetDescription_Args`](pjrt.md#_GetDescription_Args), [`_Kind_Args`](pjrt.md#_Kind_Args), [`_PlatformName_Args`](pjrt.md#_PlatformName_Args), [`_Plugin_Initialize_Args`](pjrt.md#_Plugin_Initialize_Args), [`_Program`](pjrt.md#_Program), [`_ToHost_Args`](pjrt.md#_ToHost_Args), [`_rowmajor_layout`](pjrt.md#_rowmajor_layout), [`PjrtError`](pjrt.md#PjrtError), [`Executable`](pjrt.md#Executable), [`_h`](pjrt.md#Buffer._h), [`readbacks`](pjrt.md#_Counters.readbacks), [`_PJRT_FN`](pjrt.md#_PJRT_FN), [`_PJRT_TO_NP`](pjrt.md#_PJRT_TO_NP), [`executes`](pjrt.md#_Counters.executes), [`uploads`](pjrt.md#_Counters.uploads), [`_Counters`](pjrt.md#_Counters), [`_HBS_UNTIL_DONE`](pjrt.md#_HBS_UNTIL_DONE), [`_compile_options_bytes`](pjrt.md#_compile_options_bytes), [`_find_libtpu`](pjrt.md#_find_libtpu), [`_h`](pjrt.md#Executable._h)  (+1 more)
- used by: [`_buf`](backend.md#_buf), [`const`](ops.md#const), [`from_np`](ops.md#from_np), [`run`](hlo.md#run), [`delete`](pjrt.md#Buffer.delete), [`client`](pjrt.md#client), [`execute`](pjrt.md#Executable.execute), [`_upload`](backend.md#_upload), [`to_numpy`](pjrt.md#Buffer.to_numpy), [`_GLOBAL`](pjrt.md#_GLOBAL._GLOBAL), [`__init__`](pjrt.md#Buffer.__init__), [`__init__`](pjrt.md#Executable.__init__)  (3 test-only)

### `PjrtError`  ·  implements/extends RuntimeError
- def: [`mini_pytorch_xla/pjrt.py:171`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L171)
- signature: `class PjrtError(RuntimeError):`
- used by: [`from_host`](pjrt.md#PjrtClient.from_host), [`_first_device`](pjrt.md#PjrtClient._first_device), [`_fn`](pjrt.md#PjrtClient._fn), [`_check_error`](pjrt.md#PjrtClient._check_error), [`_api`](pjrt.md#PjrtClient._api)

### `_AddressableDevices_Args`  ·  implements/extends Structure
- def: [`mini_pytorch_xla/pjrt.py:227`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L227) — documented in [mini_pytorch_xla-pjrt](../../concepts/mini_pytorch_xla-pjrt.md)
- signature: `class _AddressableDevices_Args(ctypes.Structure):`
- protocol/private: `_fields_`[`L228`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L228)
- uses (calls/refs, reference-scoped): [`c_vp`](pjrt.md#c_vp), [`c_sz`](pjrt.md#c_sz)
- used by: [`_first_device`](pjrt.md#PjrtClient._first_device), [`num_devices`](pjrt.md#PjrtClient.num_devices)

### `_ApiVersion`  ·  implements/extends Structure
- def: [`mini_pytorch_xla/pjrt.py:100`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L100) — documented in [mini_pytorch_xla-pjrt](../../concepts/mini_pytorch_xla-pjrt.md)
- signature: `class _ApiVersion(ctypes.Structure):`
- protocol/private: `_fields_`[`L101`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L101)
- uses (calls/refs, reference-scoped): [`c_vp`](pjrt.md#c_vp), [`c_sz`](pjrt.md#c_sz), [`c_int`](pjrt.md#c_int)
- used by: [`PJRT_Api`](pjrt.md#PJRT_Api)

### `_BufferFromHost_Args`  ·  implements/extends Structure
- def: [`mini_pytorch_xla/pjrt.py:246`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L246) — documented in [mini_pytorch_xla-pjrt](../../concepts/mini_pytorch_xla-pjrt.md)
- signature: `class _BufferFromHost_Args(ctypes.Structure):`
- protocol/private: `_fields_`[`L247`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L247)
- uses (calls/refs, reference-scoped): [`c_vp`](pjrt.md#c_vp), [`c_sz`](pjrt.md#c_sz), [`c_i64`](pjrt.md#c_i64), [`c_int`](pjrt.md#c_int)
- used by: [`from_host`](pjrt.md#PjrtClient.from_host)

### `_Buffer_Destroy_Args`
- def: [`mini_pytorch_xla/pjrt.py:278`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L278) — documented in [mini_pytorch_xla-pjrt](../../concepts/mini_pytorch_xla-pjrt.md)
- protocol/private: `_fields_`[`L279`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L279)
- uses (calls/refs, reference-scoped): [`c_vp`](pjrt.md#c_vp), [`c_sz`](pjrt.md#c_sz)
- used by: [`delete`](pjrt.md#Buffer.delete)

### `_Buffer_Dimensions_Args`  ·  implements/extends Structure
- def: [`mini_pytorch_xla/pjrt.py:282`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L282) — documented in [mini_pytorch_xla-pjrt](../../concepts/mini_pytorch_xla-pjrt.md)
- signature: `class _Buffer_Dimensions_Args(ctypes.Structure):`
- protocol/private: `_fields_`[`L283`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L283)
- uses (calls/refs, reference-scoped): [`c_vp`](pjrt.md#c_vp), [`c_sz`](pjrt.md#c_sz), [`c_i64`](pjrt.md#c_i64)
- used by: [`_wrap_output`](pjrt.md#PjrtClient._wrap_output)

### `_Buffer_ElementType_Args`  ·  implements/extends Structure
- def: [`mini_pytorch_xla/pjrt.py:318`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L318) — documented in [mini_pytorch_xla-pjrt](../../concepts/mini_pytorch_xla-pjrt.md)
- signature: `class _Buffer_ElementType_Args(ctypes.Structure):`
- protocol/private: `_fields_`[`L319`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L319)
- uses (calls/refs, reference-scoped): [`c_vp`](pjrt.md#c_vp), [`c_sz`](pjrt.md#c_sz), [`c_int`](pjrt.md#c_int)
- used by: [`_wrap_output`](pjrt.md#PjrtClient._wrap_output)

### `_Client_Create_Args`  ·  implements/extends Structure
- def: [`mini_pytorch_xla/pjrt.py:214`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L214) — documented in [mini_pytorch_xla-pjrt](../../concepts/mini_pytorch_xla-pjrt.md)
- signature: `class _Client_Create_Args(ctypes.Structure):`
- protocol/private: `_fields_`[`L215`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L215)
- uses (calls/refs, reference-scoped): [`c_vp`](pjrt.md#c_vp), [`c_sz`](pjrt.md#c_sz)
- used by: [`_fns`](pjrt.md#PjrtClient._fns)

### `_Compile_Args`  ·  implements/extends Structure
- def: [`mini_pytorch_xla/pjrt.py:239`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L239) — documented in [mini_pytorch_xla-pjrt](../../concepts/mini_pytorch_xla-pjrt.md)
- signature: `class _Compile_Args(ctypes.Structure):`
- protocol/private: `_fields_`[`L240`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L240)
- uses (calls/refs, reference-scoped): [`c_vp`](pjrt.md#c_vp), [`c_sz`](pjrt.md#c_sz)
- used by: [`compile`](pjrt.md#PjrtClient.compile)

### `_Counters`
- def: [`mini_pytorch_xla/pjrt.py:362`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L362)
- doc: Accounting of host&lt;-&gt;device traffic vs on-device executes (proof tooling).
- signature: `class _Counters:`
- members:
  - `reset(self)` — [`L369`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L369)
  - `executes` — [`L365`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L365)
  - `readbacks` — [`L367`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L367)
  - `uploads` — [`L366`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L366)
- protocol/private: `__init__`[`L364`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L364)
- used by: [`from_host`](pjrt.md#PjrtClient.from_host), [`_execute`](pjrt.md#PjrtClient._execute), [`_buffer_to_host`](pjrt.md#PjrtClient._buffer_to_host), [`counters`](pjrt.md#PjrtClient.counters)  (1 test-only)

### `_Error_Destroy_Args`  ·  implements/extends Structure
- def: [`mini_pytorch_xla/pjrt.py:358`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L358)
- signature: `class _Error_Destroy_Args(ctypes.Structure):`
- protocol/private: `_fields_`[`L359`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L359)
- uses (calls/refs, reference-scoped): [`c_vp`](pjrt.md#c_vp), [`c_sz`](pjrt.md#c_sz)
- used by: [`_check_error`](pjrt.md#PjrtClient._check_error)

### `_Error_Message_Args`  ·  implements/extends Structure
- def: [`mini_pytorch_xla/pjrt.py:353`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L353)
- signature: `class _Error_Message_Args(ctypes.Structure):`
- protocol/private: `_fields_`[`L354`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L354)
- uses (calls/refs, reference-scoped): [`c_vp`](pjrt.md#c_vp), [`c_sz`](pjrt.md#c_sz)
- used by: [`_check_error`](pjrt.md#PjrtClient._check_error)

### `_Event_Args`  ·  implements/extends Structure
- def: [`mini_pytorch_xla/pjrt.py:323`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L323) — documented in [mini_pytorch_xla-pjrt](../../concepts/mini_pytorch_xla-pjrt.md)
- signature: `class _Event_Args(ctypes.Structure):`
- protocol/private: `_fields_`[`L324`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L324)
- uses (calls/refs, reference-scoped): [`c_vp`](pjrt.md#c_vp), [`c_sz`](pjrt.md#c_sz)
- used by: [`_await`](pjrt.md#PjrtClient._await)

### `_ExecuteOptions`  ·  implements/extends Structure
- def: [`mini_pytorch_xla/pjrt.py:256`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L256) — documented in [mini_pytorch_xla-pjrt](../../concepts/mini_pytorch_xla-pjrt.md)
- signature: `class _ExecuteOptions(ctypes.Structure):`
- protocol/private: `_fields_`[`L257`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L257)
- uses (calls/refs, reference-scoped): [`c_vp`](pjrt.md#c_vp), [`c_sz`](pjrt.md#c_sz), [`c_int`](pjrt.md#c_int)
- used by: [`_execute`](pjrt.md#PjrtClient._execute)

### `_Execute_Args`  ·  implements/extends Structure
- def: [`mini_pytorch_xla/pjrt.py:264`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L264)
- signature: `class _Execute_Args(ctypes.Structure):`
- protocol/private: `_fields_`[`L265`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L265)
- uses (calls/refs, reference-scoped): [`c_vp`](pjrt.md#c_vp), [`c_sz`](pjrt.md#c_sz)
- used by: [`_execute`](pjrt.md#PjrtClient._execute)

### `_GetDescription_Args`  ·  implements/extends Structure
- def: [`mini_pytorch_xla/pjrt.py:292`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L292)
- signature: `class _GetDescription_Args(ctypes.Structure):`
- protocol/private: `_fields_`[`L293`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L293)
- uses (calls/refs, reference-scoped): [`c_vp`](pjrt.md#c_vp), [`c_sz`](pjrt.md#c_sz)
- used by: [`device_kind`](pjrt.md#PjrtClient.device_kind)

### `_Kind_Args`  ·  implements/extends Structure
- def: [`mini_pytorch_xla/pjrt.py:297`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L297)
- signature: `class _Kind_Args(ctypes.Structure):`
- protocol/private: `_fields_`[`L298`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L298)
- uses (calls/refs, reference-scoped): [`c_vp`](pjrt.md#c_vp), [`c_sz`](pjrt.md#c_sz)
- used by: [`device_kind`](pjrt.md#PjrtClient.device_kind)

### `_MemoryLayout`  ·  implements/extends Structure
- def: [`mini_pytorch_xla/pjrt.py:327`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L327) — documented in [mini_pytorch_xla-pjrt](../../concepts/mini_pytorch_xla-pjrt.md)
- signature: `class _MemoryLayout(ctypes.Structure):`
- protocol/private: `_fields_`[`L329`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L329)
- uses (calls/refs, reference-scoped): [`c_vp`](pjrt.md#c_vp), [`c_sz`](pjrt.md#c_sz), [`c_i64`](pjrt.md#c_i64), [`c_int`](pjrt.md#c_int)
- used by: [`_rowmajor_layout`](pjrt.md#_rowmajor_layout)

### `_MemoryStats_Args`  ·  implements/extends Structure
- def: [`mini_pytorch_xla/pjrt.py:303`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L303) — documented in [mini_pytorch_xla-pjrt](../../concepts/mini_pytorch_xla-pjrt.md)
- signature: `class _MemoryStats_Args(ctypes.Structure):`
- protocol/private: `_fields_`[`L304`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L304)
- uses (calls/refs, reference-scoped): [`c_vp`](pjrt.md#c_vp), [`c_sz`](pjrt.md#c_sz), [`c_i64`](pjrt.md#c_i64)
- used by: [`memory_stats`](pjrt.md#PjrtClient.memory_stats)

### `_PlatformName_Args`  ·  implements/extends Structure
- def: [`mini_pytorch_xla/pjrt.py:287`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L287)
- signature: `class _PlatformName_Args(ctypes.Structure):`
- protocol/private: `_fields_`[`L288`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L288)
- uses (calls/refs, reference-scoped): [`c_vp`](pjrt.md#c_vp), [`c_sz`](pjrt.md#c_sz)
- used by: [`platform_name`](pjrt.md#PjrtClient.platform_name)

### `_Plugin_Initialize_Args`  ·  implements/extends Structure
- def: [`mini_pytorch_xla/pjrt.py:223`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L223)
- signature: `class _Plugin_Initialize_Args(ctypes.Structure):`
- protocol/private: `_fields_`[`L224`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L224)
- uses (calls/refs, reference-scoped): [`c_vp`](pjrt.md#c_vp), [`c_sz`](pjrt.md#c_sz)
- used by: [`_fns`](pjrt.md#PjrtClient._fns)

### `_Program`  ·  implements/extends Structure
- def: [`mini_pytorch_xla/pjrt.py:233`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L233)
- signature: `class _Program(ctypes.Structure):`
- protocol/private: `_fields_`[`L234`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L234)
- uses (calls/refs, reference-scoped): [`c_vp`](pjrt.md#c_vp), [`c_sz`](pjrt.md#c_sz)
- used by: [`compile`](pjrt.md#PjrtClient.compile)

### `_ToHost_Args`  ·  implements/extends Structure
- def: [`mini_pytorch_xla/pjrt.py:272`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L272)
- signature: `class _ToHost_Args(ctypes.Structure):`
- protocol/private: `_fields_`[`L273`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L273)
- uses (calls/refs, reference-scoped): [`c_vp`](pjrt.md#c_vp), [`c_sz`](pjrt.md#c_sz)
- used by: [`_buffer_to_host`](pjrt.md#PjrtClient._buffer_to_host)

## Functions
- `_args_header(struct_instance)` — [`L115`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L115) — All *_Args structs start with {size_t struct_size; void* extension_start;}. — documented in [no_pytorch-train_mini](../../concepts/no_pytorch-train_mini.md)
- `_compile_options_bytes()` — [`L142`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L142)
- `_find_libtpu()` — [`L147`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L147)
- `_rowmajor_layout(rank: int)` — [`L336`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L336) — Standard row-major (descending minor_to_major) tiled layout, no tiling.
- `client()` — [`L567`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L567) — Process-wide singleton (one TPU client; the chips are a shared resource). — documented in [mini_pytorch_xla-backend](../../concepts/mini_pytorch_xla-backend.md)

## Module values
- `BF16` — [`L123`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L123)
- `F16` — [`L123`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L123)
- `F32` — [`L123`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L123)
- `F64` — [`L123`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L123)
- `PRED` — [`L123`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L123)
- `S16` — [`L123`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L123)
- `S32` — [`L123`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L123)
- `S64` — [`L123`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L123)
- `S8` — [`L123`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L123)
- `U16` — [`L123`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L123)
- `U32` — [`L123`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L123)
- `U64` — [`L123`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L123)
- `U8` — [`L123`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L123)
- `_FN_NAMES` — [`L31`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L31)
- `_GLOBAL` — [`L564`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L564) — documented in [mini_pytorch_xla-profiler](../../concepts/mini_pytorch_xla-profiler.md)
- `_HBS_UNTIL_DONE` — [`L133`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L133)
- `_NP_TO_PJRT` — [`L125`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L125) — documented in [mini_pytorch_xla-backend](../../concepts/mini_pytorch_xla-backend.md)
- `_PJRT_FN` — [`L112`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L112)
- `_PJRT_TO_NP` — [`L130`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L130)
- `c_i64` — [`L96`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L96) — documented in [no_pytorch-train_mini](../../concepts/no_pytorch-train_mini.md)
- `c_int` — [`L97`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L97)
- `c_sz` — [`L94`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L94) — documented in [mini_pytorch_xla-pjrt](../../concepts/mini_pytorch_xla-pjrt.md)
- `c_vp` — [`L95`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/pjrt.py#L95) — documented in [mini_pytorch_xla-ops](../../concepts/mini_pytorch_xla-ops.md)

