---
title: "Source summary — Karpathy: the LLM Wiki Pattern"
type: source-summary
source: raw/sources/karpathy-llm-wiki-pattern.md
canonical: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
author: Andrej Karpathy
ingested: 2026-06-27
---

# Karpathy — the LLM Wiki Pattern

> Self-referential note: this is the article **this whole repo instantiates**. See
> [`SCHEMA.md`](../../SCHEMA.md) and the [root README](../../README.md), which cite the same gist.
> Ingesting it is the wiki documenting its own design pattern.

## What it argues
The gist proposes a way to use an LLM over a document collection that is *not* RAG. Instead of
retrieving raw chunks at query time and reconstructing the answer from scratch every time, you keep a
**persistent, compounding wiki** — interlinked markdown the model maintains — sitting between the raw
sources and your questions ([source](../../raw/sources/karpathy-llm-wiki-pattern.md): "the wiki is a
persistent, compounding artifact. The cross-references are already there. The contradictions have
already been flagged.").

The division of labor is the crux: **the human curates and asks; the LLM does the bookkeeping**
(summarizing, cross-referencing, keeping pages consistent). The article's punchline is a claim about
*why wikis fail* — "the tedious part of maintaining a knowledge base is not the reading...it's the
bookkeeping" — and the bet that an LLM removes exactly that burden.

## The three layers
The source names a three-layer architecture, which this repo adopts verbatim:

1. **Raw sources — immutable.** Articles, papers, data; read, never edited.
2. **The wiki — LLM-generated markdown** the model actively maintains.
3. **The schema** — the conventions/workflow doc governing how it all operates.

## The three operations
- **Ingest** — read a new source, summarize it, and **integrate across 10–15 existing pages** (not a
  single dumped summary; the spread across pages is the point).
- **Query** — search the relevant pages and answer in whatever format (markdown, tables, slides).
- **Lint** — periodic health check for contradictions, orphan pages, and knowledge gaps.

## Takeaways / why it matters here
- This repo is a faithful instantiation: same three layers, same three operations. The synthesized
  topic pages below ([[llm-wiki-pattern]], [[rag-vs-compiled-knowledge]]) carry the concepts forward.
- The article is **source-type-agnostic** — it describes prose ingestion. This repo *extends* it with a
  second, automated source type: **code repos**, ingested by the `wikify-ingest-repo` skill into the
  grounded [`mini_pytorch_xla`](../code/mini_pytorch_xla/overview.md) wiki. That extension is the
  contribution layered on top of the gist (see [[llm-wiki-pattern#extension-code-as-a-source-type]]).

## Provenance caveat
The raw copy in `raw/sources/` is a **fetched rendering**, lightly paraphrased by the fetch step, not a
byte-for-byte capture; quoted phrases are reproduced as returned. The canonical gist is the authority.
This does not affect the conceptual claims above, which are stable across the rendering.

## See also
- Topic pages: [[llm-wiki-pattern]] · [[rag-vs-compiled-knowledge]]
- The code track this pattern is applied to: [`mini_pytorch_xla` overview](../code/mini_pytorch_xla/overview.md)
- The project's own schema, which operationalizes this gist: [`SCHEMA.md`](../../SCHEMA.md)
