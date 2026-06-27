---
title: 'Module: no_pytorch/tensor.py'
type: catalog
provenance: extracted
module: no_pytorch/tensor.py
status: fresh
symbol_base: scip-python python mini_pytorch_xla 0.0.0 `no_pytorch.tensor`/
symbols:
  _acc: _acc().
  Tensor: Tensor#
  _record: _record().
  mul: mul().
  Tensor.grad: Tensor#grad.
  reshape: reshape().
  sqrt: sqrt().
  rsqrt: rsqrt().
  tanh: tanh().
  transpose: transpose().
  reduce_sum: reduce_sum().
  neg: neg().
  sub: sub().
  div: div().
  exp: exp().
  from_numpy: from_numpy().
  log: log().
  add: add().
  bmm: bmm().
  mm: mm().
  Tensor.backward: Tensor#backward().
  _unbroadcast: _unbroadcast().
  div.bw: div().bw().
  broadcast_to: broadcast_to().
  _as: _as().
  reduce_sum.bw: reduce_sum().bw().
  mm.bw: mm().bw().
  bmm.bw: bmm().bw().
  reduce_max: reduce_max().
  Tensor.shape: Tensor#shape().
  zeros: zeros().
  linear: linear().
  _RECORD: _RECORD.
  ones: ones().
  matmul: matmul().
  transpose_last2: transpose_last2().
  no_grad.__exit__: no_grad#__exit__().
  Tensor.__add__: Tensor#__add__().
  Tensor.__radd__: Tensor#__radd__().
  Tensor.__sub__: Tensor#__sub__().
  Tensor.__rsub__: Tensor#__rsub__().
  Tensor.__mul__: Tensor#__mul__().
  Tensor.__rmul__: Tensor#__rmul__().
  Tensor.__truediv__: Tensor#__truediv__().
  Tensor.__rtruediv__: Tensor#__rtruediv__().
  Tensor.build: Tensor#build().
  Tensor.buf: Tensor#buf.
  no_grad._prev: no_grad#_prev.
  Tensor.ndim: Tensor#ndim().
  Tensor.numpy: Tensor#numpy().
  Tensor.item: Tensor#item().
  Tensor.requires_grad: Tensor#requires_grad.
  no_grad: no_grad#
  no_grad.__enter__: no_grad#__enter__().
  Tensor.dtype: Tensor#dtype().
  Tensor.__neg__: Tensor#__neg__().
  Tensor.__matmul__: Tensor#__matmul__().
  Tensor._prev: Tensor#_prev.
  Tensor._backward: Tensor#_backward.
  Tensor.__init__: Tensor#__init__().
---
# Module: [`no_pytorch/tensor.py`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/tensor.py)

## Classes
### `Tensor`
- def: [`no_pytorch/tensor.py:36`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/tensor.py#L36) — documented in [no_pytorch-nn](../../concepts/no_pytorch-nn.md)
- signature: `class Tensor:`
- members:
  - `backward(self)` — [`L68`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/tensor.py#L68) — documented in [no_pytorch-train_mini](../../concepts/no_pytorch-train_mini.md)
  - `build(t)` — [`L71`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/tensor.py#L71)
  - `dtype(self)` — [`L48`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/tensor.py#L48)
  - `item(self)` — [`L55`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/tensor.py#L55)
  - `ndim(self)` — [`L51`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/tensor.py#L51) — documented in [no_pytorch-tensor](../../concepts/no_pytorch-tensor.md)
  - `numpy(self)` — [`L53`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/tensor.py#L53)
  - `shape(self)` — [`L45`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/tensor.py#L45) — documented in [no_pytorch-nn](../../concepts/no_pytorch-nn.md)
  - `buf` — [`L38`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/tensor.py#L38) — documented in [no_pytorch-tensor](../../concepts/no_pytorch-tensor.md)
  - `grad` — [`L40`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/tensor.py#L40) — documented in [no_pytorch-nn](../../concepts/no_pytorch-nn.md)
  - `requires_grad` — [`L39`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/tensor.py#L39) — documented in [no_pytorch-nn](../../concepts/no_pytorch-nn.md)
- protocol/private: `__add__`[`L57`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/tensor.py#L57), `__init__`[`L37`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/tensor.py#L37), `__matmul__`[`L66`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/tensor.py#L66), `__mul__`[`L61`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/tensor.py#L61), `__neg__`[`L65`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/tensor.py#L65), `__radd__`[`L58`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/tensor.py#L58), `__rmul__`[`L62`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/tensor.py#L62), `__rsub__`[`L60`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/tensor.py#L60), `__rtruediv__`[`L64`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/tensor.py#L64), `__sub__`[`L59`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/tensor.py#L59), `__truediv__`[`L63`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/tensor.py#L63), `_backward`[`L42`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/tensor.py#L42), `_prev`[`L41`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/tensor.py#L41)
- uses (calls/refs, reference-scoped): [`mul`](tensor.md#mul), [`neg`](tensor.md#neg), [`sub`](tensor.md#sub), [`div`](tensor.md#div), [`add`](tensor.md#add), [`_as`](tensor.md#_as), [`matmul`](tensor.md#matmul), [`ones`](tensor.md#ones), [`no_grad`](tensor.md#no_grad)
- used by: [`_acc`](tensor.md#_acc), [`_record`](tensor.md#_record), [`main`](train_mini.md#main), [`mul`](tensor.md#mul), [`reshape`](tensor.md#reshape), [`rsqrt`](tensor.md#rsqrt), [`sqrt`](tensor.md#sqrt), [`tanh`](tensor.md#tanh), [`transpose`](tensor.md#transpose), [`reduce_sum`](tensor.md#reduce_sum), [`neg`](tensor.md#neg), [`sub`](tensor.md#sub), [`div`](tensor.md#div), [`exp`](tensor.md#exp), [`from_numpy`](tensor.md#from_numpy), [`log`](tensor.md#log), [`add`](tensor.md#add), [`bmm`](tensor.md#bmm), [`mm`](tensor.md#mm), [`_unbroadcast`](tensor.md#_unbroadcast), [`broadcast_to`](tensor.md#broadcast_to), [`bw`](tensor.md#div.bw), [`_as`](tensor.md#_as), [`visit`](nn.md#Module.visit), [`bw`](tensor.md#bmm.bw), [`bw`](tensor.md#mm.bw), [`bw`](tensor.md#reduce_sum.bw), [`parameter`](nn.md#parameter), [`reduce_max`](tensor.md#reduce_max), [`zeros`](tensor.md#zeros), [`ones`](tensor.md#ones)

### `no_grad`
- def: [`no_pytorch/tensor.py:25`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/tensor.py#L25)
- signature: `class no_grad:`
- protocol/private: `__enter__`[`L26`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/tensor.py#L26), `__exit__`[`L31`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/tensor.py#L31), `_prev`[`L28`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/tensor.py#L28)
- uses (calls/refs, reference-scoped): [`_RECORD`](tensor.md#_RECORD)
- used by: [`step`](nn.md#AdamW.step), [`backward`](tensor.md#Tensor.backward)

## Functions
- `_acc(p: Tensor, g: Tensor)` — [`L117`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/tensor.py#L117) — documented in [no_pytorch-nn](../../concepts/no_pytorch-nn.md)
- `_as(o)` — [`L96`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/tensor.py#L96) — documented in [no_pytorch-tensor](../../concepts/no_pytorch-tensor.md)
- `_record(out: Tensor, parents, backward)` — [`L109`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/tensor.py#L109) — documented in [no_pytorch-nn](../../concepts/no_pytorch-nn.md)
- `_unbroadcast(g: Tensor, shape)` — [`L124`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/tensor.py#L124) — documented in [no_pytorch-nn](../../concepts/no_pytorch-nn.md)
- `add(a, b)` — [`L139`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/tensor.py#L139) — documented in [mini_pytorch_xla-ops](../../concepts/mini_pytorch_xla-ops.md)
- `bmm(a, b)` — [`L257`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/tensor.py#L257) — documented in [no_pytorch-train_mini](../../concepts/no_pytorch-train_mini.md)
- `broadcast_to(a, shape)` — [`L218`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/tensor.py#L218)
- `bw()` — [`L157`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/tensor.py#L157) — documented in [no_pytorch-tensor](../../concepts/no_pytorch-tensor.md)
- `bw()` — [`L202`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/tensor.py#L202) — documented in [no_pytorch-train_mini](../../concepts/no_pytorch-train_mini.md)
- `bw()` — [`L251`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/tensor.py#L251) — documented in [no_pytorch-tensor](../../concepts/no_pytorch-tensor.md)
- `bw()` — [`L260`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/tensor.py#L260) — documented in [no_pytorch-train_mini](../../concepts/no_pytorch-train_mini.md)
- `div(a, b)` — [`L154`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/tensor.py#L154) — documented in [mini_pytorch_xla-ops](../../concepts/mini_pytorch_xla-ops.md)
- `exp(a)` — [`L169`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/tensor.py#L169) — documented in [mini_pytorch_xla-ops](../../concepts/mini_pytorch_xla-ops.md)
- `from_numpy(arr, requires_grad=False)` — [`L87`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/tensor.py#L87) — documented in [no_pytorch-nn](../../concepts/no_pytorch-nn.md)
- `linear(x, W)` — [`L270`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/tensor.py#L270) — x[...,in] @ W[in,out] -> [...,out], folding leading dims for a 2-D matmul.
- `log(a)` — [`L174`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/tensor.py#L174) — documented in [mini_pytorch_xla-ops](../../concepts/mini_pytorch_xla-ops.md)
- `matmul(a, b)` — [`L266`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/tensor.py#L266)
- `mm(a, b)` — [`L248`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/tensor.py#L248) — documented in [no_pytorch-tensor](../../concepts/no_pytorch-tensor.md)
- `mul(a, b)` — [`L149`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/tensor.py#L149) — documented in [mini_pytorch_xla-ops](../../concepts/mini_pytorch_xla-ops.md)
- `neg(a)` — [`L164`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/tensor.py#L164) — documented in [mini_pytorch_xla-ops](../../concepts/mini_pytorch_xla-ops.md)
- `ones(shape)` — [`L100`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/tensor.py#L100) — documented in [no_pytorch-tensor](../../concepts/no_pytorch-tensor.md)
- `reduce_max(a, axes, keepdim=False)` — [`L208`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/tensor.py#L208) — documented in [no_pytorch-nn](../../concepts/no_pytorch-nn.md)
- `reduce_sum(a, axes, keepdim=False)` — [`L195`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/tensor.py#L195) — documented in [no_pytorch-nn](../../concepts/no_pytorch-nn.md)
- `reshape(a, shape)` — [`L223`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/tensor.py#L223) — documented in [no_pytorch-nn](../../concepts/no_pytorch-nn.md)
- `rsqrt(a)` — [`L184`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/tensor.py#L184) — documented in [mini_pytorch_xla-ops](../../concepts/mini_pytorch_xla-ops.md)
- `sqrt(a)` — [`L179`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/tensor.py#L179) — documented in [mini_pytorch_xla-ops](../../concepts/mini_pytorch_xla-ops.md)
- `sub(a, b)` — [`L144`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/tensor.py#L144) — documented in [mini_pytorch_xla-ops](../../concepts/mini_pytorch_xla-ops.md)
- `tanh(a)` — [`L189`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/tensor.py#L189) — documented in [mini_pytorch_xla-ops](../../concepts/mini_pytorch_xla-ops.md)
- `transpose(a, perm)` — [`L232`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/tensor.py#L232) — documented in [no_pytorch-tensor](../../concepts/no_pytorch-tensor.md)
- `transpose_last2(a)` — [`L241`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/tensor.py#L241) — documented in [no_pytorch-train_mini](../../concepts/no_pytorch-train_mini.md)
- `zeros(shape)` — [`L104`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/tensor.py#L104) — documented in [no_pytorch-nn](../../concepts/no_pytorch-nn.md)

## Module values
- `_RECORD` — [`L22`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/tensor.py#L22) — documented in [no_pytorch-tensor](../../concepts/no_pytorch-tensor.md)

