---
title: 'Module: no_pytorch/nn.py'
type: catalog
provenance: extracted
module: no_pytorch/nn.py
status: fresh
symbol_base: scip-python python mini_pytorch_xla 0.0.0 `no_pytorch.nn`/
symbols:
  AdamW.step: AdamW#step().
  Module: Module#
  cross_entropy: cross_entropy().
  Module.visit: Module#visit().
  LayerNorm.forward: LayerNorm#forward().
  Linear: Linear#
  parameter: parameter().
  softmax: softmax().
  AdamW.m: AdamW#m.
  AdamW.v: AdamW#v.
  Linear.forward: Linear#forward().
  LayerNorm: LayerNorm#
  Embedding: Embedding#
  Embedding.forward: Embedding#forward().
  Linear.b: Linear#b.
  AdamW.params: AdamW#params.
  Module.parameters: Module#parameters().
  Linear.W: Linear#W.
  LayerNorm.g: LayerNorm#g.
  LayerNorm.b: LayerNorm#b.
  gelu: gelu().
  AdamW.zero_grad: AdamW#zero_grad().
  AdamW.b1: AdamW#b1.
  AdamW.b2: AdamW#b2.
  AdamW.t: AdamW#t.
  Embedding.__init__: Embedding#__init__().
  AdamW.wd: AdamW#wd.
  Embedding.W: Embedding#W.
  LayerNorm.eps: LayerNorm#eps.
  AdamW: AdamW#
  AdamW.lr: AdamW#lr.
  AdamW.eps: AdamW#eps.
  Module.__call__: Module#__call__().
  Linear.__init__: Linear#__init__().
  LayerNorm.__init__: LayerNorm#__init__().
  AdamW.__init__: AdamW#__init__().
---
# Module: [`no_pytorch/nn.py`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/nn.py)

## Classes
### `AdamW`
- def: [`no_pytorch/nn.py:112`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/nn.py#L112)
- signature: `class AdamW:`
- members:
  - `step(self)` — [`L125`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/nn.py#L125) — documented in [no_pytorch-nn](../../concepts/no_pytorch-nn.md)
  - `zero_grad(self)` — [`L121`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/nn.py#L121)
  - `b1` — [`L115`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/nn.py#L115) — documented in [no_pytorch-nn](../../concepts/no_pytorch-nn.md)
  - `b2` — [`L115`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/nn.py#L115) — documented in [no_pytorch-nn](../../concepts/no_pytorch-nn.md)
  - `eps` — [`L116`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/nn.py#L116)
  - `lr` — [`L115`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/nn.py#L115)
  - `m` — [`L118`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/nn.py#L118) — documented in [no_pytorch-nn](../../concepts/no_pytorch-nn.md)
  - `params` — [`L114`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/nn.py#L114) — documented in [no_pytorch-nn](../../concepts/no_pytorch-nn.md)
  - `t` — [`L117`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/nn.py#L117) — documented in [no_pytorch-nn](../../concepts/no_pytorch-nn.md)
  - `v` — [`L119`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/nn.py#L119) — documented in [no_pytorch-nn](../../concepts/no_pytorch-nn.md)
  - `wd` — [`L116`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/nn.py#L116)
- protocol/private: `__init__`[`L113`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/nn.py#L113)
- uses (calls/refs, reference-scoped): [`sqrt`](tensor.md#sqrt), [`zeros`](tensor.md#zeros), [`no_grad`](tensor.md#no_grad)
- used by: [`main`](train_mini.md#main)

### `Embedding`  ·  implements/extends Module
- def: [`no_pytorch/nn.py:54`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/nn.py#L54) — documented in [no_pytorch-nn](../../concepts/no_pytorch-nn.md)
- doc: Lookup as one-hot @ table. `idx_onehot` is \[..., num_embeddings\] (host one-hot).
- signature: `class Embedding(Module):`
- members:
  - `forward(self, idx_onehot)` — [`L60`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/nn.py#L60)
  - `W` — [`L58`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/nn.py#L58)
- protocol/private: `__init__`[`L57`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/nn.py#L57)
- uses (calls/refs, reference-scoped): [`Module`](nn.md#Module), [`parameter`](nn.md#parameter), [`linear`](tensor.md#linear)
- used by: [`Module`](nn.md#Module), [`pos`](train_mini.md#LLM.pos), [`tok`](train_mini.md#LLM.tok)

### `LayerNorm`  ·  implements/extends Module
- def: [`no_pytorch/nn.py:64`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/nn.py#L64)
- signature: `class LayerNorm(Module):`
- members:
  - `forward(self, x)` — [`L70`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/nn.py#L70)
  - `b` — [`L67`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/nn.py#L67)
  - `eps` — [`L68`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/nn.py#L68)
  - `g` — [`L66`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/nn.py#L66)
- protocol/private: `__init__`[`L65`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/nn.py#L65)
- uses (calls/refs, reference-scoped): [`Module`](nn.md#Module), [`rsqrt`](tensor.md#rsqrt), [`reduce_sum`](tensor.md#reduce_sum), [`parameter`](nn.md#parameter)
- used by: [`Module`](nn.md#Module), [`lnf`](train_mini.md#LLM.lnf), [`n1`](train_mini.md#Block.n1), [`n2`](train_mini.md#Block.n2)

### `Linear`  ·  implements/extends Module
- def: [`no_pytorch/nn.py:41`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/nn.py#L41) — documented in [no_pytorch-nn](../../concepts/no_pytorch-nn.md)
- doc: y = x @ W (+ b). Weight stored \[in, out\] (so forward is a clean matmul).
- signature: `class Linear(Module):`
- members:
  - `forward(self, x)` — [`L49`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/nn.py#L49)
  - `W` — [`L46`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/nn.py#L46)
  - `b` — [`L47`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/nn.py#L47)
- protocol/private: `__init__`[`L44`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/nn.py#L44)
- uses (calls/refs, reference-scoped): [`Module`](nn.md#Module), [`parameter`](nn.md#parameter), [`linear`](tensor.md#linear)
- used by: [`Module`](nn.md#Module), [`fc1`](train_mini.md#MLP.fc1), [`fc2`](train_mini.md#MLP.fc2), [`head`](train_mini.md#LLM.head), [`k`](train_mini.md#MultiHeadAttention.k), [`o`](train_mini.md#MultiHeadAttention.o), [`q`](train_mini.md#MultiHeadAttention.q), [`v`](train_mini.md#MultiHeadAttention.v)

### `Module`
- def: [`no_pytorch/nn.py:17`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/nn.py#L17) — documented in [no_pytorch-nn](../../concepts/no_pytorch-nn.md)
- signature: `class Module:`
- members:
  - `parameters(self)` — [`L18`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/nn.py#L18) — documented in [no_pytorch-nn](../../concepts/no_pytorch-nn.md)
  - `visit(o)` — [`L21`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/nn.py#L21) — documented in [no_pytorch-nn](../../concepts/no_pytorch-nn.md)
- protocol/private: `__call__`[`L34`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/nn.py#L34)
- uses (calls/refs, reference-scoped): [`Tensor`](tensor.md#Tensor), [`Linear`](nn.md#Linear), [`LayerNorm`](nn.md#LayerNorm), [`Embedding`](nn.md#Embedding), [`Block`](train_mini.md#Block), [`LLM`](train_mini.md#LLM), [`MLP`](train_mini.md#MLP), [`MultiHeadAttention`](train_mini.md#MultiHeadAttention), [`requires_grad`](tensor.md#Tensor.requires_grad)
- used by: [`main`](train_mini.md#main), [`Linear`](nn.md#Linear), [`LayerNorm`](nn.md#LayerNorm), [`Embedding`](nn.md#Embedding), [`Block`](train_mini.md#Block), [`LLM`](train_mini.md#LLM), [`MLP`](train_mini.md#MLP), [`MultiHeadAttention`](train_mini.md#MultiHeadAttention)

## Functions
- `cross_entropy(logits, target_onehot)` — [`L97`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/nn.py#L97) — logits, target_onehot both [..., V]; mean NLL over all leading positions. — documented in [no_pytorch-nn](../../concepts/no_pytorch-nn.md)
- `gelu(x)` — [`L83`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/nn.py#L83)
- `parameter(np_array)` — [`L13`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/nn.py#L13) — documented in [no_pytorch-tensor](../../concepts/no_pytorch-tensor.md)
- `softmax(x, axis=-1)` — [`L90`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/nn.py#L90) — documented in [no_pytorch-train_mini](../../concepts/no_pytorch-train_mini.md)

