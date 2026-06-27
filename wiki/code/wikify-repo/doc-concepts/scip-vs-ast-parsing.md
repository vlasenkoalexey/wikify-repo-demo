---
title: SCIP vs AST parsing
type: doc-concept
provenance: doc
source: README.md
updated: 2026-06-27
status: fresh
---
# SCIP vs AST parsing

## Definition
The README's central technical claim: how you resolve symbol references decides
whether the wiki can be *grounded*. Most code-knowledge tools (graphify,
understand-anything) parse with **tree-sitter** — a fast, build-free AST, one tree
per file — which resolves references **by name**: it sees a call to something
*called* `forward`, not *which* `forward`. Cross-file bindings, import aliases,
inheritance/overrides, and overloads are therefore guesses. wikify-repo instead
indexes with **SCIP** (Sourcegraph's Code Intelligence Protocol) via `scip-python`
(pyright) and `scip-clang` (clang) — the language's *real* name-and-type resolver —
so every definition and reference binds to a globally-unique **moniker**: a citation
points at *the* symbol, across files, not a string that happens to match.

## In wikify-repo (grounded)
The SCIP path is Stage 1, owned by the `wikify.scip_index` module.
[`run_indexer`](../catalog/wikify/scip_index.md#run_indexer) shells out to the
external indexer and [`parse_index`](../catalog/wikify/scip_index.md#parse_index)
reads the emitted `.scip` protobuf;
[`build_graph`](../catalog/wikify/scip_index.md#build_graph) normalizes it into the
in-repo [`SymbolGraph`](../catalog/wikify/graph.md#SymbolGraph), the node-and-edge
table every later stage cites against. The moniker is the load-bearing artifact:
[`parse_symbol`](../catalog/wikify/monikers.md#parse_symbol) splits each SCIP symbol
string into a [`ParsedSymbol`](../catalog/wikify/monikers.md#ParsedSymbol), and
because monikers are global and stable, a Python index and a C++ index simply *union*
by moniker. The README's "textbook failure" — dynamic dispatch through
`nn.Module.__call__`, which has no static name edge — is exactly what
[`devirtualize`](../catalog/wikify/graph.md#devirtualize) repairs by reading SCIP's
`is_implementation` relationships and adding `base → override` edges that a name-based
call graph would silently miss (or worse, flag as dead code).

## Why it matters / when it applies
SCIP is what makes grounding **enforceable** rather than aspirational: a claim's
`cite:` either resolves to a real symbol in the SCIP table, or the citation linter
**fails the build**. The README is honest about the price: SCIP needs a real indexer
(`scip-python` over npm; a `compile_commands.json` for C++), heavier than a zero-build
tree-sitter parse — the cost of precision. And SCIP records *occurrences*, not *calls*,
so wikify derives callers/callees by reference-scoping inside
[`_process_document`](../catalog/wikify/scip_index.md#_process_document) — a heuristic
the README pins by `tests/test_callers_callees.py`. Tree-sitter trades that precision
for breadth (20+ languages, no toolchain): the right call for navigation, the wrong one
for *citeable* grounding. Where pyright drops a file entirely, an AST fallback recovers
it deterministically.

## Connections
- Code concepts: [SCIP indexing → SymbolGraph](../concepts/wikify-scip_index.md) — the
  deep page on Stage 1; [moniker grammar](../concepts/wikify-monikers.md);
  [the SymbolGraph](../concepts/wikify-graph.md);
  [AST fallback](../concepts/wikify-ast_fallback.md) — the recovery path for files the
  SCIP indexer dropped.
- Module catalogs: [wikify/scip_index](../catalog/wikify/scip_index.md),
  [wikify/graph](../catalog/wikify/graph.md), [wikify/monikers](../catalog/wikify/monikers.md).
- Related doc-concepts: [the Python ↔ LLM split](python-llm-split.md) (SCIP is the
  deterministic foundation it builds on); [the wiki as storage format](wiki-as-storage-format.md).

## Source
Extracted from `README.md` ("SCIP vs AST parsing"), kept in place at
`../../../../raw/code/wikify-repo/README.md`.
