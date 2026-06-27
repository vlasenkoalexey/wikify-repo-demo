---
title: 'Module: examples/train_torch.py'
type: catalog
provenance: extracted
module: examples/train_torch.py
status: fresh
symbol_base: scip-python python mini_pytorch_xla 0.0.0 `examples.train_torch`/
symbols:
  main: main().
  Block.attn: Block#attn().
  collect_profile: collect_profile().
  Block.forward: Block#forward().
  LLM.forward: LLM#forward().
  to_xla_: to_xla_().
  LLM.blocks: LLM#blocks.
  generate: generate().
  train_step: train_step().
  Block.dk: Block#dk.
  LLM: LLM#
  main.batch: main().batch().
  Block: Block#
  Block.h: Block#h.
  Block.q: Block#q.
  Block.k: Block#k.
  Block.v: Block#v.
  Block.o: Block#o.
  Block.n1: Block#n1.
  Block.n2: Block#n2.
  Block.f1: Block#f1.
  Block.f2: Block#f2.
  LLM.tok: LLM#tok.
  LLM.pos: LLM#pos.
  LLM.lnf: LLM#lnf.
  LLM.head: LLM#head.
  Block.__init__: Block#__init__().
  LLM.__init__: LLM#__init__().
  LLM.block: LLM#block.
---
# Module: [`examples/train_torch.py`](../../../../../raw/code/mini_pytorch_xla/examples/train_torch.py)

## Classes
### `Block`  ·  implements/extends Module
- def: [`examples/train_torch.py:38`](../../../../../raw/code/mini_pytorch_xla/examples/train_torch.py#L38)
- signature: `class Block(nn.Module):`
- members:
  - `attn(self, x, mask)` — [`L49`](../../../../../raw/code/mini_pytorch_xla/examples/train_torch.py#L49)
  - `forward(self, x, mask)` — [`L57`](../../../../../raw/code/mini_pytorch_xla/examples/train_torch.py#L57)
  - `dk` — [`L41`](../../../../../raw/code/mini_pytorch_xla/examples/train_torch.py#L41)
  - `f1` — [`L47`](../../../../../raw/code/mini_pytorch_xla/examples/train_torch.py#L47)
  - `f2` — [`L47`](../../../../../raw/code/mini_pytorch_xla/examples/train_torch.py#L47)
  - `h` — [`L41`](../../../../../raw/code/mini_pytorch_xla/examples/train_torch.py#L41)
  - `k` — [`L43`](../../../../../raw/code/mini_pytorch_xla/examples/train_torch.py#L43)
  - `n1` — [`L46`](../../../../../raw/code/mini_pytorch_xla/examples/train_torch.py#L46)
  - `n2` — [`L46`](../../../../../raw/code/mini_pytorch_xla/examples/train_torch.py#L46)
  - `o` — [`L45`](../../../../../raw/code/mini_pytorch_xla/examples/train_torch.py#L45)
  - `q` — [`L42`](../../../../../raw/code/mini_pytorch_xla/examples/train_torch.py#L42)
  - `v` — [`L44`](../../../../../raw/code/mini_pytorch_xla/examples/train_torch.py#L44)
- protocol/private: `__init__`[`L39`](../../../../../raw/code/mini_pytorch_xla/examples/train_torch.py#L39)
- used by: (1 test-only callers)

### `LLM`  ·  implements/extends Module
- def: [`examples/train_torch.py:63`](../../../../../raw/code/mini_pytorch_xla/examples/train_torch.py#L63)
- signature: `class LLM(nn.Module):`
- members:
  - `forward(self, idx)` — [`L75`](../../../../../raw/code/mini_pytorch_xla/examples/train_torch.py#L75)
  - `block` — [`L66`](../../../../../raw/code/mini_pytorch_xla/examples/train_torch.py#L66)
  - `blocks` — [`L69`](../../../../../raw/code/mini_pytorch_xla/examples/train_torch.py#L69)
  - `head` — [`L71`](../../../../../raw/code/mini_pytorch_xla/examples/train_torch.py#L71)
  - `lnf` — [`L70`](../../../../../raw/code/mini_pytorch_xla/examples/train_torch.py#L70)
  - `pos` — [`L68`](../../../../../raw/code/mini_pytorch_xla/examples/train_torch.py#L68)
  - `tok` — [`L67`](../../../../../raw/code/mini_pytorch_xla/examples/train_torch.py#L67)
- protocol/private: `__init__`[`L64`](../../../../../raw/code/mini_pytorch_xla/examples/train_torch.py#L64)
- uses (calls/refs, reference-scoped): (1 test-only callers)
- used by: (2 test-only callers)

## Functions
- `batch()` — [`L178`](../../../../../raw/code/mini_pytorch_xla/examples/train_torch.py#L178)
- `collect_profile(model, opt, make_batch, V, logdir, prof_steps)` — [`L93`](../../../../../raw/code/mini_pytorch_xla/examples/train_torch.py#L93) — Capture an on-device op profile of the backend and write an xprof xplane.pb.
- `generate(model, V, L, stoi, itos, prompt, max_new_tokens, temperature=0.8, top_k=40)` — [`L120`](../../../../../raw/code/mini_pytorch_xla/examples/train_torch.py#L120) — nanoGPT-style sampling. Each step's forward runs on the TPU (fixed block_size
- `main()` — [`L138`](../../../../../raw/code/mini_pytorch_xla/examples/train_torch.py#L138)
- `to_xla_(module: nn.Module)` — [`L27`](../../../../../raw/code/mini_pytorch_xla/examples/train_torch.py#L27) — In-place: replace every parameter with an XLATensor leaf on the TPU.
- `train_step(model, opt, x, y, V)` — [`L84`](../../../../../raw/code/mini_pytorch_xla/examples/train_torch.py#L84)

