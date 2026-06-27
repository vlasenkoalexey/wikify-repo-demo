---
title: Two-tier coverage (concepts for depth, catalogs for the whole repo)
type: doc-concept
provenance: doc
source: docs/design.md
updated: 2026-06-27
status: fresh
---
# Two-tier coverage (concepts for depth, catalogs for the whole repo)

## Definition
Concept-driven synthesis is **selective by design** — it drives understanding
top-down from an explicit list of architectural concepts precisely to avoid the
shallow answers that bottom-up "summarize every file" produces. But selectivity
has a failure mode: a *forgotten* concept is a *missing subsystem*. The design's
fix is a second, deterministic tier — a **coverage floor** that guarantees every
documentable symbol is at least *represented*, even where no concept touched it.
The two tiers split cleanly: **concepts give depth**, **catalogs give whole-repo
breadth**.

## In wikify-repo (grounded)
The load-bearing insight is that coverage is a **set-difference over the SCIP
symbol table, never a graph walk**:
`coverage = documentable_symbols − concept-cited`. The documentable set comes from
[`documentable_symbols`](../catalog/wikify/coverage.md#documentable_symbols)
(in-repo classes / functions / methods / module values; locals, params, and
externals already pruned); the cited set is read back from the concept pages via
[`covered_monikers`](../catalog/wikify/coverage.md#covered_monikers); the whole
report is assembled by [`compute_report`](../catalog/wikify/coverage.md#compute_report).
The difference is then emitted as **one catalog page per module** by
[`emit_catalogs`](../catalog/wikify/coverage.md#emit_catalogs) /
[`render_catalog`](../catalog/wikify/coverage.md#render_catalog), so the repo is
fully represented and **cannot miss a file**. The measured outcome —
documentable total, deep-concept % ([`CoverageReport.pct_deep`](../catalog/wikify/coverage.md#CoverageReport.pct_deep)),
represented % ([`CoverageReport.pct_represented`](../catalog/wikify/coverage.md#CoverageReport.pct_represented)),
catalog-only count, classes represented — makes "whole repo ingested" a *measured
property*, not a hope.

The doc is emphatic about **why enumeration, not traversal**: the first
torchtitan ingest covered three Trainer concepts and missed *every model*
(`Transformer`, `Attention`, …). Reachability traversal fails by construction —
the trainer invokes a model as `model_parts[0](inputs)` through
`nn.Module.__call__`, a dynamic dispatch with **no static call edge** — and a
per-file "is it connected?" check is worse, false-flagging model files as dead
code. SCIP already enumerated *every* symbol, so coverage never asks "what is
reachable?" but "what is *represented*?"

## Why it matters / when it applies
Coverage is **representation, not connection**. A catalog represents each module
and captures its *internal* edges (real static calls, via
[`class_connections`](../catalog/wikify/coverage.md#class_connections) over
[`class_symbols`](../catalog/wikify/coverage.md#class_symbols)), so a model's
`Transformer → TransformerBlock → Attention → FeedForward` spine is fully
grounded. It deliberately does **not** synthesize the missing trainer→model edge,
nor unify the N independent `Attention` classes into one concept — those are
separate, optional operations (see [devirtualization](devirtualization.md)), never
a precondition for whole-repo coverage. Catalogs are `extracted` provenance,
correct by construction, and so are *not* run through the citation linter.

## Connections
- Code concepts: [wikify-coverage](../concepts/wikify-coverage.md) — the
  set-difference + catalog emitter; [wikify-discover](../concepts/wikify-discover.md)
  — where the selective concept agenda comes from; [wikify-graph](../concepts/wikify-graph.md)
  — the symbol graph the catalog's intra-module edges read.
- Module catalogs: [wikify/coverage.md](../catalog/wikify/coverage.md) ·
  [wikify/discover.md](../catalog/wikify/discover.md).
- Related doc-concepts: [devirtualization](devirtualization.md) ·
  [packet-subgraph-grounding](packet-subgraph-grounding.md).

## Source
Extracted from `../../../raw/code/wikify-repo/docs/design.md` (kept in place):
"Load-bearing design decisions" #7, "Stage 6b — Structural coverage / module
catalogs".
