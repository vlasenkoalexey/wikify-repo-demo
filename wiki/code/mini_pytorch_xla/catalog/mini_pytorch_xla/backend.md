---
title: 'Module: mini_pytorch_xla/backend.py'
type: catalog
provenance: extracted
module: mini_pytorch_xla/backend.py
status: fresh
symbol_base: scip-python python mini_pytorch_xla 0.0.0 `mini_pytorch_xla.backend`/
symbols:
  _buf: _buf().
  aten: aten.
  impl: impl().
  _wrap: _wrap().
  _var_mean: _var_mean().
  _embedding_backward: _embedding_backward().
  _mean_dim: _mean_dim().
  _threshold_backward: _threshold_backward().
  _mean_all: _mean_all().
  _mse_loss: _mse_loss().
  _pow: _pow().
  _sum_dim: _sum_dim().
  _amax: _amax().
  _view: _view().
  _ones_like: _ones_like().
  _zeros_like: _zeros_like().
  _addmm: _addmm().
  _mse_loss_backward: _mse_loss_backward().
  to_xla: to_xla().
  to_cpu: to_cpu().
  _add: _add().
  _sub: _sub().
  _recip: _recip().
  _sum_all: _sum_all().
  _expand: _expand().
  _t: _t().
  _transpose: _transpose().
  _permute: _permute().
  _unsqueeze: _unsqueeze().
  _squeeze: _squeeze().
  _clamp_min: _clamp_min().
  _relu: _relu().
  _embedding: _embedding().
  _izero: _izero().
  _mm: _mm().
  _bmm: _bmm().
  _mul: _mul().
  _div: _div().
  _neg: _neg().
  _exp: _exp().
  _log: _log().
  _sqrt: _sqrt().
  _rsqrt: _rsqrt().
  _tanh: _tanh().
  _erf: _erf().
  _where: _where().
  _ge: _ge().
  _le: _le().
  _gt: _gt().
  _lt: _lt().
  _maximum: _maximum().
  _iadd: _iadd().
  _isub: _isub().
  _iaddcmul: _iaddcmul().
  _iaddcdiv: _iaddcdiv().
  _ilerp: _ilerp().
  XLATensor: XLATensor#
  _identity: _identity().
  _to_copy: _to_copy().
  _imul: _imul().
  _upload: _upload().
  _DECOMP: _DECOMP.
  _cpu_fallback: _cpu_fallback().
  _dispatch: _dispatch().
  _icopy: _icopy().
  _to_cpu: _to_cpu().
  _idx_np: _idx_np().
  to_xla_: to_xla_().
  _kd: _kd().
  XLATensor._buf: XLATensor#_buf.
  _torch_dtype: _torch_dtype().
  impl.deco: impl().deco().
  _from_cpu: _from_cpu().
  HANDLERS.HANDLERS: HANDLERS.HANDLERS.
  XLATensor.__new__: XLATensor#__new__().
  XLATensor.__torch_dispatch__: XLATensor#__torch_dispatch__().
  _WARNED: _WARNED.
  _NP_TO_TORCH: _NP_TO_TORCH.
  _norm_shape: _norm_shape().
  _TORCH_TO_NP: _TORCH_TO_NP.
  XLATensor.__init__: XLATensor#__init__().
  XLATensor.__repr__: XLATensor#__repr__().
---
# Module: [`mini_pytorch_xla/backend.py`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/backend.py)

## Classes
### `XLATensor`  ·  implements/extends Tensor
- def: [`mini_pytorch_xla/backend.py:44`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/backend.py#L44)
- signature: `class XLATensor(torch.Tensor):`
- protocol/private: `__init__`[`L51`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/backend.py#L51), `__new__`[`L46`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/backend.py#L46), `__repr__`[`L58`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/backend.py#L58), `__torch_dispatch__`[`L55`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/backend.py#L55), `_buf`[`L52`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/backend.py#L52)
- uses (calls/refs, reference-scoped): [`_dispatch`](backend.md#_dispatch), [`_torch_dtype`](backend.md#_torch_dtype)
- used by: [`_buf`](backend.md#_buf), [`_wrap`](backend.md#_wrap), [`to_xla`](backend.md#to_xla), [`to_cpu`](backend.md#to_cpu), [`_upload`](backend.md#_upload), [`_idx_np`](backend.md#_idx_np), [`_to_cpu`](backend.md#_to_cpu)

## Functions
- `_add(a, b, *, alpha=1)` — [`L223`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/backend.py#L223) — documented in [mini_pytorch_xla-backend](../../concepts/mini_pytorch_xla-backend.md)
- `_addmm(bias, m1, m2, *, beta=1, alpha=1)` — [`L427`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/backend.py#L427) — documented in [mini_pytorch_xla-backend](../../concepts/mini_pytorch_xla-backend.md)
- `_amax(a, dim, keepdim=False)` — [`L319`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/backend.py#L319) — documented in [mini_pytorch_xla-backend](../../concepts/mini_pytorch_xla-backend.md)
- `_bmm(a, b)` — [`L218`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/backend.py#L218) — documented in [mini_pytorch_xla-backend](../../concepts/mini_pytorch_xla-backend.md)
- `_buf(x, ref_dtype=np.float32)` — [`L101`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/backend.py#L101) — Coerce an op argument to a device Buffer. — documented in [mini_pytorch_xla-backend](../../concepts/mini_pytorch_xla-backend.md)
- `_clamp_min(a, mn)` — [`L443`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/backend.py#L443) — documented in [mini_pytorch_xla-ops](../../concepts/mini_pytorch_xla-ops.md)
- `_cpu_fallback(func, args, kwargs)` — [`L154`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/backend.py#L154)
- `_dispatch(func, args, kwargs)` — [`L162`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/backend.py#L162)
- `_div(a, b)` — [`L244`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/backend.py#L244) — documented in [mini_pytorch_xla-backend](../../concepts/mini_pytorch_xla-backend.md)
- `_embedding(weight, indices, padding_idx=-1, scale_grad_by_freq=False, sparse=False)` — [`L511`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/backend.py#L511) — documented in [mini_pytorch_xla-backend](../../concepts/mini_pytorch_xla-backend.md)
- `_embedding_backward(grad, indices, num_weights, padding_idx, scale_grad_by_freq)` — [`L516`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/backend.py#L516) — documented in [mini_pytorch_xla-backend](../../concepts/mini_pytorch_xla-backend.md)
- `_erf(a)` — [`L279`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/backend.py#L279) — documented in [mini_pytorch_xla-backend](../../concepts/mini_pytorch_xla-backend.md)
- `_exp(a)` — [`L254`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/backend.py#L254) — documented in [mini_pytorch_xla-backend](../../concepts/mini_pytorch_xla-backend.md)
- `_expand(a, size, *, implicit=False)` — [`L330`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/backend.py#L330) — documented in [mini_pytorch_xla-backend](../../concepts/mini_pytorch_xla-backend.md)
- `_from_cpu(x)` — [`L150`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/backend.py#L150)
- `_ge(a, b)` — [`L384`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/backend.py#L384) — documented in [mini_pytorch_xla-backend](../../concepts/mini_pytorch_xla-backend.md)
- `_gt(a, b)` — [`L394`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/backend.py#L394) — documented in [mini_pytorch_xla-backend](../../concepts/mini_pytorch_xla-backend.md)
- `_iadd(self, other, *, alpha=1)` — [`L527`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/backend.py#L527) — documented in [mini_pytorch_xla-backend](../../concepts/mini_pytorch_xla-backend.md)
- `_iaddcdiv(self, t1, t2, *, value=1)` — [`L560`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/backend.py#L560) — documented in [mini_pytorch_xla-backend](../../concepts/mini_pytorch_xla-backend.md)
- `_iaddcmul(self, t1, t2, *, value=1)` — [`L551`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/backend.py#L551) — documented in [mini_pytorch_xla-backend](../../concepts/mini_pytorch_xla-backend.md)
- `_icopy(self, src, non_blocking=False)` — [`L577`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/backend.py#L577)
- `_identity(a, **kw)` — [`L416`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/backend.py#L416)
- `_idx_np(indices)` — [`L505`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/backend.py#L505)
- `_ilerp(self, end, weight)` — [`L569`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/backend.py#L569) — documented in [mini_pytorch_xla-backend](../../concepts/mini_pytorch_xla-backend.md)
- `_imul(self, other)` — [`L545`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/backend.py#L545)
- `_isub(self, other, *, alpha=1)` — [`L536`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/backend.py#L536) — documented in [mini_pytorch_xla-backend](../../concepts/mini_pytorch_xla-backend.md)
- `_izero(self)` — [`L583`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/backend.py#L583) — documented in [mini_pytorch_xla-backend](../../concepts/mini_pytorch_xla-backend.md)
- `_kd(buf, reduced, dims)` — [`L177`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/backend.py#L177) — Reshape a reduced buffer back to keepdim shape (1s at reduced dims).
- `_le(a, b)` — [`L389`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/backend.py#L389)
- `_log(a)` — [`L259`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/backend.py#L259)
- `_lt(a, b)` — [`L399`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/backend.py#L399)
- `_maximum(a, b)` — [`L438`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/backend.py#L438) — documented in [mini_pytorch_xla-backend](../../concepts/mini_pytorch_xla-backend.md)
- `_mean_all(a, *, dtype=None)` — [`L460`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/backend.py#L460) — documented in [mini_pytorch_xla-backend](../../concepts/mini_pytorch_xla-backend.md)
- `_mean_dim(a, dim, keepdim=False, *, dtype=None)` — [`L468`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/backend.py#L468) — documented in [mini_pytorch_xla-backend](../../concepts/mini_pytorch_xla-backend.md)
- `_mm(a, b)` — [`L213`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/backend.py#L213) — documented in [mini_pytorch_xla-backend](../../concepts/mini_pytorch_xla-backend.md)
- `_mse_loss(inp, tgt, reduction=1)` — [`L482`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/backend.py#L482) — documented in [mini_pytorch_xla-backend](../../concepts/mini_pytorch_xla-backend.md)
- `_mse_loss_backward(grad, inp, tgt, reduction=1)` — [`L495`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/backend.py#L495) — documented in [mini_pytorch_xla-backend](../../concepts/mini_pytorch_xla-backend.md)
- `_mul(a, b)` — [`L239`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/backend.py#L239) — documented in [mini_pytorch_xla-backend](../../concepts/mini_pytorch_xla-backend.md)
- `_neg(a)` — [`L249`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/backend.py#L249)
- `_norm_shape(size, numel=None)` — [`L201`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/backend.py#L201)
- `_ones_like(a, **kw)` — [`L404`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/backend.py#L404) — documented in [mini_pytorch_xla-backend](../../concepts/mini_pytorch_xla-backend.md)
- `_permute(a, dims)` — [`L359`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/backend.py#L359) — documented in [mini_pytorch_xla-backend](../../concepts/mini_pytorch_xla-backend.md)
- `_pow(a, e)` — [`L289`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/backend.py#L289) — documented in [mini_pytorch_xla-backend](../../concepts/mini_pytorch_xla-backend.md)
- `_recip(a)` — [`L284`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/backend.py#L284) — documented in [mini_pytorch_xla-ops](../../concepts/mini_pytorch_xla-ops.md)
- `_relu(a)` — [`L448`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/backend.py#L448) — documented in [mini_pytorch_xla-ops](../../concepts/mini_pytorch_xla-ops.md)
- `_rsqrt(a)` — [`L269`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/backend.py#L269) — documented in [mini_pytorch_xla-backend](../../concepts/mini_pytorch_xla-backend.md)
- `_sqrt(a)` — [`L264`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/backend.py#L264)
- `_squeeze(a, dim)` — [`L371`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/backend.py#L371) — documented in [mini_pytorch_xla-backend](../../concepts/mini_pytorch_xla-backend.md)
- `_sub(a, b, *, alpha=1)` — [`L231`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/backend.py#L231) — documented in [mini_pytorch_xla-backend](../../concepts/mini_pytorch_xla-backend.md)
- `_sum_all(a, *, dtype=None)` — [`L302`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/backend.py#L302)
- `_sum_dim(a, dim, keepdim=False, *, dtype=None)` — [`L308`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/backend.py#L308) — documented in [mini_pytorch_xla-backend](../../concepts/mini_pytorch_xla-backend.md)
- `_t(a)` — [`L345`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/backend.py#L345) — documented in [mini_pytorch_xla-backend](../../concepts/mini_pytorch_xla-backend.md)
- `_tanh(a)` — [`L274`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/backend.py#L274) — documented in [mini_pytorch_xla-backend](../../concepts/mini_pytorch_xla-backend.md)
- `_threshold_backward(grad, self, threshold)` — [`L453`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/backend.py#L453) — documented in [mini_pytorch_xla-backend](../../concepts/mini_pytorch_xla-backend.md)
- `_to_copy(a, *args, **kw)` — [`L421`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/backend.py#L421)
- `_to_cpu(x)` — [`L146`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/backend.py#L146)
- `_torch_dtype(npdt)` — [`L29`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/backend.py#L29)
- `_transpose(a, d0, d1)` — [`L351`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/backend.py#L351) — documented in [mini_pytorch_xla-backend](../../concepts/mini_pytorch_xla-backend.md)
- `_unsqueeze(a, dim)` — [`L364`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/backend.py#L364) — documented in [mini_pytorch_xla-backend](../../concepts/mini_pytorch_xla-backend.md)
- `_upload(t: torch.Tensor)` — [`L63`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/backend.py#L63)
- `_var_mean(self, dim=None, *, correction=1, keepdim=False)` — [`L184`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/backend.py#L184) — documented in [mini_pytorch_xla-backend](../../concepts/mini_pytorch_xla-backend.md)
- `_view(a, size)` — [`L338`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/backend.py#L338) — documented in [mini_pytorch_xla-backend](../../concepts/mini_pytorch_xla-backend.md)
- `_where(cond, a, b)` — [`L379`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/backend.py#L379)
- `_wrap(buf)` — [`L97`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/backend.py#L97) — documented in [mini_pytorch_xla-backend](../../concepts/mini_pytorch_xla-backend.md)
- `_zeros_like(a, **kw)` — [`L410`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/backend.py#L410) — documented in [mini_pytorch_xla-backend](../../concepts/mini_pytorch_xla-backend.md)
- `deco(fn)` — [`L117`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/backend.py#L117)
- `impl(*ops_overloads)` — [`L116`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/backend.py#L116) — documented in [mini_pytorch_xla-backend](../../concepts/mini_pytorch_xla-backend.md)
- `to_cpu(x)` — [`L80`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/backend.py#L80)
- `to_xla(t: torch.Tensor)` — [`L70`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/backend.py#L70) — Move a tensor onto the registered 'tpu' device (it reports device='tpu:0').
- `to_xla_(module: torch.nn.Module)` — [`L86`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/backend.py#L86) — In-place: replace every parameter of `module` with an XLATensor leaf on the TPU.

## Module values
- `HANDLERS` — [`L113`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/backend.py#L113)
- `_DECOMP` — [`L126`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/backend.py#L126)
- `_NP_TO_TORCH` — [`L23`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/backend.py#L23)
- `_TORCH_TO_NP` — [`L25`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/backend.py#L25)
- `_WARNED` — [`L143`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/backend.py#L143)
- `aten` — [`L21`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/backend.py#L21) — documented in [mini_pytorch_xla-backend](../../concepts/mini_pytorch_xla-backend.md)

