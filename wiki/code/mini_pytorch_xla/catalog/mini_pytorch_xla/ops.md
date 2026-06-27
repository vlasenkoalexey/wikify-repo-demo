---
title: 'Module: mini_pytorch_xla/ops.py'
type: catalog
provenance: extracted
module: mini_pytorch_xla/ops.py
status: fresh
symbol_base: scip-python python mini_pytorch_xla 0.0.0 `mini_pytorch_xla.ops`/
symbols:
  binary: binary().
  const: const().
  unary: unary().
  reshape: reshape().
  compare: compare().
  from_np: from_np().
  transpose: transpose().
  broadcast_to: broadcast_to().
  reduce: reduce().
  select: select().
  gather_rows: gather_rows().
  _run1: _run1().
  erf: erf().
  slice_dim: slice_dim().
  _dot_general: _dot_general().
  reduce_sum: reduce_sum().
  mm: mm().
  _arr: _arr().
  bmm: bmm().
  _bdims: _bdims().
  reduce_max: reduce_max().
  bshape: bshape().
  _f: _f().
---
# Module: [`mini_pytorch_xla/ops.py`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/ops.py)

## Functions
- `_arr(xs)` — [`L16`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/ops.py#L16)
- `_bdims(in_shape, out_shape)` — [`L52`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/ops.py#L52)
- `_dot_general(a, b, lb, rb, lc, rc, out_shape)` — [`L162`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/ops.py#L162) — documented in [mini_pytorch_xla-pjrt](../../concepts/mini_pytorch_xla-pjrt.md)
- `_f(v)` — [`L20`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/ops.py#L20)
- `_run1(module, inputs)` — [`L24`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/ops.py#L24) — documented in [mini_pytorch_xla-ops](../../concepts/mini_pytorch_xla-ops.md)
- `binary(opname, a: pjrt.Buffer, b: pjrt.Buffer)` — [`L69`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/ops.py#L69) — documented in [mini_pytorch_xla-ops](../../concepts/mini_pytorch_xla-ops.md)
- `bmm(a, b)` — [`L179`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/ops.py#L179)
- `broadcast_to(a: pjrt.Buffer, shape)` — [`L57`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/ops.py#L57) — documented in [mini_pytorch_xla-pjrt](../../concepts/mini_pytorch_xla-pjrt.md)
- `bshape(sa, sb)` — [`L38`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/ops.py#L38)
- `compare(direction, a: pjrt.Buffer, b: pjrt.Buffer)` — [`L101`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/ops.py#L101) — Elementwise compare -> bool buffer. direction in {GE,GT,LE,LT,EQ,NE}. — documented in [mini_pytorch_xla-pjrt](../../concepts/mini_pytorch_xla-pjrt.md)
- `const(value, shape, dtype=np.float32)` — [`L29`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/ops.py#L29) — documented in [mini_pytorch_xla-backend](../../concepts/mini_pytorch_xla-backend.md)
- `erf(a: pjrt.Buffer)` — [`L92`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/ops.py#L92) — documented in [mini_pytorch_xla-pjrt](../../concepts/mini_pytorch_xla-pjrt.md)
- `from_np(arr)` — [`L33`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/ops.py#L33) — documented in [mini_pytorch_xla-pjrt](../../concepts/mini_pytorch_xla-pjrt.md)
- `gather_rows(table: pjrt.Buffer, idx: np.ndarray)` — [`L213`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/ops.py#L213) — Embedding-style row gather: table[V,D], idx int array [...] -> [...,D]. — documented in [mini_pytorch_xla-ops](../../concepts/mini_pytorch_xla-ops.md)
- `mm(a, b)` — [`L175`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/ops.py#L175)
- `reduce(opname, init, a: pjrt.Buffer, axes)` — [`L187`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/ops.py#L187) — documented in [mini_pytorch_xla-pjrt](../../concepts/mini_pytorch_xla-pjrt.md)
- `reduce_max(a, axes)` — [`L209`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/ops.py#L209)
- `reduce_sum(a, axes)` — [`L205`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/ops.py#L205)
- `reshape(a: pjrt.Buffer, shape)` — [`L128`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/ops.py#L128) — documented in [mini_pytorch_xla-ops](../../concepts/mini_pytorch_xla-ops.md)
- `select(pred: pjrt.Buffer, a: pjrt.Buffer, b: pjrt.Buffer)` — [`L118`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/ops.py#L118) — documented in [mini_pytorch_xla-pjrt](../../concepts/mini_pytorch_xla-pjrt.md)
- `slice_dim(a: pjrt.Buffer, dim, start, limit, stride=1)` — [`L148`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/ops.py#L148) — documented in [mini_pytorch_xla-pjrt](../../concepts/mini_pytorch_xla-pjrt.md)
- `transpose(a: pjrt.Buffer, perm)` — [`L138`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/ops.py#L138) — documented in [mini_pytorch_xla-pjrt](../../concepts/mini_pytorch_xla-pjrt.md)
- `unary(opname, a: pjrt.Buffer)` — [`L85`](../../../../../raw/code/mini_pytorch_xla/mini_pytorch_xla/ops.py#L85) — documented in [mini_pytorch_xla-ops](../../concepts/mini_pytorch_xla-ops.md)

