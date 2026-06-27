---
title: "RAG vs. compiled knowledge"
type: topic
updated: 2026-06-27
sources:
  - wiki/sources/karpathy-llm-wiki-pattern.md
---

# RAG vs. compiled knowledge

The conceptual contrast at the heart of the [[llm-wiki-pattern]]: two different places to put the work
of turning raw documents into answers.

## The two strategies
**Retrieval-augmented generation (RAG)** does the work *at query time*. Each question triggers a
retrieval of raw chunks, and the model reconstructs an answer from them on the spot. Nothing persists
between queries — the synthesis is thrown away and re-derived next time.

**Compiled knowledge (the wiki)** does the work *at ingest time*. The model reads a source once, writes
the synthesis into durable pages, and wires the cross-references then. At query time it reads pages that
**already** contain the synthesis ([source](../sources/karpathy-llm-wiki-pattern.md): "the
cross-references are already there. The contradictions have already been flagged.").

## Why "compiled" is the right word
The analogy is interpretation vs. compilation. RAG *interprets* the corpus on every query; the wiki
*compiles* it once into an intermediate representation (interlinked markdown) that is cheap to read
repeatedly and is kept current as sources change. The cost moves from per-query to per-ingest, and —
critically — it **amortizes**: the synthesis compounds instead of being recomputed.

| | RAG | Compiled wiki |
|---|---|---|
| When synthesis happens | every query | once, at ingest |
| What persists | nothing (embeddings of raw chunks) | interlinked pages + cross-refs |
| Cross-references | reconstructed each time | already present |
| Contradictions | re-encountered each time | flagged once, recorded |
| Marginal query cost | full retrieve + synthesize | read the relevant page(s) |
| Failure mode | drift, no memory | staleness if not re-linted |

## The grounding twist for code
For prose, "compiled" means summaries + cross-links. For the **code** source type this repo adds, the
compile step is stronger: it is *grounded*. Every mechanism claim on a page like
[`mini_pytorch_xla-backend`](../code/mini_pytorch_xla/concepts/mini_pytorch_xla-backend.md) must cite a
real SCIP symbol, and a deterministic **coverage** pass enumerates the whole symbol table so no
subsystem is silently dropped — things a query-time call-graph walk would miss (e.g. the
dynamic-dispatch seams in `__torch_dispatch__`). So the wiki isn't just *pre-computed* RAG; for code
it's pre-computed **and** verified. (See [`SCHEMA.md`](../../SCHEMA.md), "Grounding".)

## The catch
Compiled knowledge has one liability RAG doesn't: **staleness**. A wiki is only as good as its last
lint/re-ingest. The pattern's answer is that maintenance is near-zero-cost for an LLM, so re-linting is
cheap; for code, `ingest --ref <commit>` rebuilds only the symbols that moved. The bet is that cheap
maintenance beats per-query recomputation — which is the same bet the [[llm-wiki-pattern]] makes about
why wikis are worth keeping at all.

## See also
- [[llm-wiki-pattern]] — the parent pattern
- [Source summary](../sources/karpathy-llm-wiki-pattern.md)
- [`mini_pytorch_xla` overview](../code/mini_pytorch_xla/overview.md) — grounded, compiled code knowledge in practice
