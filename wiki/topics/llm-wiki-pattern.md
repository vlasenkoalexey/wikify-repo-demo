---
title: "The LLM Wiki Pattern"
type: topic
updated: 2026-06-27
sources:
  - wiki/sources/karpathy-llm-wiki-pattern.md
---

# The LLM Wiki Pattern

A way to use an LLM over a body of knowledge in which a **persistent, interlinked markdown wiki** sits
between raw sources and your questions — built and maintained by the model, curated by you. Introduced
by Andrej Karpathy ([source summary](../sources/karpathy-llm-wiki-pattern.md)); **this repository is a
working instantiation of it** ([`SCHEMA.md`](../../SCHEMA.md)).

## The shape of the idea
The pattern is defined by three layers and three operations.

**Layers:** (1) *raw sources*, immutable; (2) *the wiki*, LLM-generated and LLM-maintained markdown;
(3) *the schema*, the conventions doc that governs the other two. **Operations:** *ingest* (read a
source, summarize, integrate across 10–15 existing pages), *query* (search pages, answer in any format),
*lint* (find contradictions, orphans, gaps).

The load-bearing division of labor: **the human curates and questions; the LLM does the bookkeeping.**
The pattern's own explanation for why it works is that wikis fail not from the reading but from the
*maintenance* burden — and that is exactly the part an LLM is tireless at
([source](../sources/karpathy-llm-wiki-pattern.md)).

## How this repo realizes each piece
| Pattern element | In this repo |
|---|---|
| Raw sources (immutable) | `raw/sources/` (prose) and `raw/code/<slug>/` (git submodules) |
| The wiki (LLM-maintained) | `wiki/` — `sources/`, `topics/`, `notes/`, and `code/<slug>/` |
| The schema | [`SCHEMA.md`](../../SCHEMA.md) (Claude/Codex/Gemini all point here) |
| Ingest | prose: read→summarize→cross-link; code: the `wikify-ingest-repo` skill |
| Query | read `index.md`, route to the right page, cite, file good answers back as a note |
| Lint | prose: judgment pass; code: `wikify finalize`/`verify` + coverage gates |

## Extension: code as a source type {#extension-code-as-a-source-type}
The original gist is about **prose**. The contribution this repo layers on top is treating a **code
repository as a first-class, *automatically* ingested source**: the
[`wikify-ingest-repo`](../../.agents/skills/wikify-ingest-repo/SKILL.md) skill pins the repo, builds a
SCIP symbol graph, and synthesizes one grounded concept page per subsystem, lint-gated so every claim
cites a real symbol. The headline example is the [`mini_pytorch_xla`](../code/mini_pytorch_xla/overview.md)
wiki. Crucially both source types feed **one** `index.md` / `log.md`, so a prose topic page (this one)
and a code concept page ([`mini_pytorch_xla-backend`](../code/mini_pytorch_xla/concepts/mini_pytorch_xla-backend.md))
live in, and cross-link within, the same knowledge base.

## Why it's not just RAG
The distinction is sharp enough to deserve its own page: [[rag-vs-compiled-knowledge]]. In one line —
RAG re-derives the answer per query and accumulates nothing; the wiki is compiled once and kept current,
so the synthesis and cross-references already exist when you ask.

## Open questions
- The gist suggests "integrate across 10–15 pages" per ingest as the prose norm; at this repo's current
  size (one article, one code repo) that fan-out is smaller. The number is a target for a mature wiki,
  not a floor.
- Where prose and code *contradict* (e.g. an article describing a mechanism the code implements
  differently) the schema says to flag, not overwrite — but no such collision exists in the wiki yet.

## See also
- [[rag-vs-compiled-knowledge]] — the contrast with retrieval-augmented generation
- [Source summary](../sources/karpathy-llm-wiki-pattern.md) · canonical gist linked therein
- [`mini_pytorch_xla` overview](../code/mini_pytorch_xla/overview.md) — the code track the pattern is applied to
