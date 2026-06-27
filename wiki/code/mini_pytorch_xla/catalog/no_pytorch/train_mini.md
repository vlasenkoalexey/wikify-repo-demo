---
title: 'Module: no_pytorch/train_mini.py'
type: catalog
provenance: extracted
module: no_pytorch/train_mini.py
status: fresh
symbol_base: scip-python python mini_pytorch_xla 0.0.0 `no_pytorch.train_mini`/
symbols:
  main: main().
  MultiHeadAttention.forward: MultiHeadAttention#forward().
  LLM.forward: LLM#forward().
  MultiHeadAttention._split: MultiHeadAttention#_split().
  Block.forward: Block#forward().
  MLP.forward: MLP#forward().
  MultiHeadAttention: MultiHeadAttention#
  MultiHeadAttention.q: MultiHeadAttention#q.
  MultiHeadAttention.k: MultiHeadAttention#k.
  MultiHeadAttention.v: MultiHeadAttention#v.
  MultiHeadAttention.o: MultiHeadAttention#o.
  MultiHeadAttention.scale: MultiHeadAttention#scale.
  MLP: MLP#
  MLP.fc1: MLP#fc1.
  MLP.fc2: MLP#fc2.
  Block: Block#
  Block.attn: Block#attn.
  Block.mlp: Block#mlp.
  Block.n1: Block#n1.
  Block.n2: Block#n2.
  LLM: LLM#
  LLM.tok: LLM#tok.
  LLM.pos: LLM#pos.
  LLM.blocks: LLM#blocks.
  LLM.lnf: LLM#lnf.
  LLM.head: LLM#head.
  LLM._mask: LLM#_mask.
  LLM._pos_oh: LLM#_pos_oh.
  main.batch: main().batch().
  MultiHeadAttention.dk: MultiHeadAttention#dk.
  onehot: onehot().
  get_text: get_text().
  MultiHeadAttention.h: MultiHeadAttention#h.
  MultiHeadAttention.__init__: MultiHeadAttention#__init__().
  MLP.__init__: MLP#__init__().
  Block.__init__: Block#__init__().
  LLM.__init__: LLM#__init__().
  LLM.block_size: LLM#block_size.
---
# Module: [`no_pytorch/train_mini.py`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/train_mini.py)

## Classes
### `Block`  ·  implements/extends Module
- def: [`no_pytorch/train_mini.py:73`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/train_mini.py#L73) — documented in [no_pytorch-nn](../../concepts/no_pytorch-nn.md)
- signature: `class Block(Module):`
- members:
  - `forward(self, x, mask)` — [`L80`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/train_mini.py#L80)
  - `attn` — [`L75`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/train_mini.py#L75)
  - `mlp` — [`L76`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/train_mini.py#L76)
  - `n1` — [`L77`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/train_mini.py#L77)
  - `n2` — [`L78`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/train_mini.py#L78)
- protocol/private: `__init__`[`L74`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/train_mini.py#L74)
- uses (calls/refs, reference-scoped): [`Module`](nn.md#Module), [`LayerNorm`](nn.md#LayerNorm), [`MLP`](train_mini.md#MLP), [`MultiHeadAttention`](train_mini.md#MultiHeadAttention)
- used by: [`Module`](nn.md#Module), [`blocks`](train_mini.md#LLM.blocks)

### `LLM`  ·  implements/extends Module
- def: [`no_pytorch/train_mini.py:86`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/train_mini.py#L86) — documented in [no_pytorch-nn](../../concepts/no_pytorch-nn.md)
- signature: `class LLM(Module):`
- members:
  - `forward(self, tok_onehot)` — [`L100`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/train_mini.py#L100) — documented in [no_pytorch-train_mini](../../concepts/no_pytorch-train_mini.md)
  - `block_size` — [`L88`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/train_mini.py#L88)
  - `blocks` — [`L91`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/train_mini.py#L91)
  - `head` — [`L93`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/train_mini.py#L93)
  - `lnf` — [`L92`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/train_mini.py#L92)
  - `pos` — [`L90`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/train_mini.py#L90)
  - `tok` — [`L89`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/train_mini.py#L89)
- protocol/private: `__init__`[`L87`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/train_mini.py#L87), `_mask`[`L96`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/train_mini.py#L96), `_pos_oh`[`L98`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/train_mini.py#L98)
- uses (calls/refs, reference-scoped): [`Module`](nn.md#Module), [`from_numpy`](tensor.md#from_numpy), [`Linear`](nn.md#Linear), [`LayerNorm`](nn.md#LayerNorm), [`Embedding`](nn.md#Embedding), [`Block`](train_mini.md#Block)
- used by: [`main`](train_mini.md#main), [`Module`](nn.md#Module)

### `MLP`  ·  implements/extends Module
- def: [`no_pytorch/train_mini.py:64`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/train_mini.py#L64) — documented in [no_pytorch-nn](../../concepts/no_pytorch-nn.md)
- signature: `class MLP(Module):`
- members:
  - `forward(self, x)` — [`L69`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/train_mini.py#L69)
  - `fc1` — [`L66`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/train_mini.py#L66)
  - `fc2` — [`L67`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/train_mini.py#L67)
- protocol/private: `__init__`[`L65`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/train_mini.py#L65)
- uses (calls/refs, reference-scoped): [`Module`](nn.md#Module), [`Linear`](nn.md#Linear), [`gelu`](nn.md#gelu)
- used by: [`Module`](nn.md#Module), [`mlp`](train_mini.md#Block.mlp)

### `MultiHeadAttention`  ·  implements/extends Module
- def: [`no_pytorch/train_mini.py:37`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/train_mini.py#L37) — documented in [no_pytorch-nn](../../concepts/no_pytorch-nn.md)
- signature: `class MultiHeadAttention(Module):`
- members:
  - `forward(self, x, mask)` — [`L51`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/train_mini.py#L51) — documented in [no_pytorch-train_mini](../../concepts/no_pytorch-train_mini.md)
  - `dk` — [`L40`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/train_mini.py#L40)
  - `h` — [`L40`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/train_mini.py#L40)
  - `k` — [`L42`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/train_mini.py#L42)
  - `o` — [`L44`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/train_mini.py#L44)
  - `q` — [`L41`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/train_mini.py#L41)
  - `scale` — [`L45`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/train_mini.py#L45)
  - `v` — [`L43`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/train_mini.py#L43)
- protocol/private: `__init__`[`L38`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/train_mini.py#L38), `_split`[`L47`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/train_mini.py#L47)
- uses (calls/refs, reference-scoped): [`Module`](nn.md#Module), [`reshape`](tensor.md#reshape), [`transpose`](tensor.md#transpose), [`bmm`](tensor.md#bmm), [`Linear`](nn.md#Linear), [`softmax`](nn.md#softmax), [`transpose_last2`](tensor.md#transpose_last2)
- used by: [`Module`](nn.md#Module), [`attn`](train_mini.md#Block.attn)

## Functions
- `batch()` — [`L136`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/train_mini.py#L136)
- `get_text()` — [`L25`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/train_mini.py#L25)
- `main()` — [`L115`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/train_mini.py#L115) — documented in [no_pytorch-nn](../../concepts/no_pytorch-nn.md)
- `onehot(ids, V)` — [`L109`](../../../../../raw/code/mini_pytorch_xla/no_pytorch/train_mini.py#L109)

