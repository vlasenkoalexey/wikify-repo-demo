---
title: 'Module: wikify/packet.py'
type: catalog
provenance: extracted
module: wikify/packet.py
status: fresh
symbol_base: scip-python python wikify-repo 0.0.0 `wikify.packet`/
symbols:
  build_packet: build_packet().
  gather_subgraph: gather_subgraph().
  resolve_seeds: resolve_seeds().
  auto_seeds: auto_seeds().
  _short: _short().
  _edge_name: _edge_name().
  gather_subgraph.relevance: gather_subgraph().relevance().
  read_subgraph: read_subgraph().
  MAX_SUBGRAPH: MAX_SUBGRAPH.
  MAX_HOPS: MAX_HOPS.
  SNIPPET_LINES: SNIPPET_LINES.
  _seed_tail: _seed_tail().
  _seed_container: _seed_container().
  _kind: _kind().
  write_packet: write_packet().
  _TEMPLATE_RULES: _TEMPLATE_RULES.
---
# Module: [`wikify/packet.py`](../../../../../raw/code/wikify-repo/wikify/packet.py)

## Functions
- `_edge_name(graph: SymbolGraph, src: str, dst: str)` — [`L131`](../../../../../raw/code/wikify-repo/wikify/packet.py#L131) — Display name for an edge ``src→dst``, tagged ``(virtual)`` if it is a — documented in [wikify-graph](../../concepts/wikify-graph.md)
- `_kind(sym)` — [`L138`](../../../../../raw/code/wikify-repo/wikify/packet.py#L138) — Display kind: scip-python often leaves Kind unspecified; fall back to the
- `_seed_container(token: str)` — [`L61`](../../../../../raw/code/wikify-repo/wikify/packet.py#L61)
- `_seed_tail(token: str)` — [`L30`](../../../../../raw/code/wikify-repo/wikify/packet.py#L30) — Last identifier of a seed token like ``Trainer::step`` or ``a.b.c``.
- `_short(moniker: str, graph: SymbolGraph)` — [`L127`](../../../../../raw/code/wikify-repo/wikify/packet.py#L127) — documented in [wikify-graph](../../concepts/wikify-graph.md)
- `auto_seeds(graph: SymbolGraph, n: int = 8)` — [`L68`](../../../../../raw/code/wikify-repo/wikify/packet.py#L68) — Discovery fallback: the n highest-importance callable symbols. — documented in [wikify-graph](../../concepts/wikify-graph.md)
- `build_packet(graph: SymbolGraph, repo_root: str | Path, slug: str, ref: str, concept: Concept, test_globs: list[str], date: str, seed_monikers: list[str] | None = None)` — [`L146`](../../../../../raw/code/wikify-repo/wikify/packet.py#L146) — Render the packet markdown and return (text, subgraph_monikers). — documented in [wikify-cli](../../concepts/wikify-cli.md)
- `gather_subgraph(graph: SymbolGraph, seeds: list[str], max_nodes: int = MAX_SUBGRAPH)` — [`L75`](../../../../../raw/code/wikify-repo/wikify/packet.py#L75) — Relevance-bounded subgraph: keep the seeds, then the most relevant neighbours. — documented in [wikify-cli](../../concepts/wikify-cli.md)
- `read_subgraph(cache_dir: str | Path, slug: str, concept_slug: str)` — [`L255`](../../../../../raw/code/wikify-repo/wikify/packet.py#L255) — documented in [wikify-lint](../../concepts/wikify-lint.md)
- `relevance(m: str)` — [`L107`](../../../../../raw/code/wikify-repo/wikify/packet.py#L107)
- `resolve_seeds(graph: SymbolGraph, seeds: list[str])` — [`L37`](../../../../../raw/code/wikify-repo/wikify/packet.py#L37) — Map seed tokens to monikers. Returns (resolved_monikers, unresolved_tokens). — documented in [wikify-graph](../../concepts/wikify-graph.md)
- `write_packet(cache_dir: str | Path, slug: str, concept_slug: str, text: str, subgraph: list[str])` — [`L242`](../../../../../raw/code/wikify-repo/wikify/packet.py#L242)

## Module values
- `MAX_HOPS` — [`L23`](../../../../../raw/code/wikify-repo/wikify/packet.py#L23)
- `MAX_SUBGRAPH` — [`L22`](../../../../../raw/code/wikify-repo/wikify/packet.py#L22)
- `SNIPPET_LINES` — [`L24`](../../../../../raw/code/wikify-repo/wikify/packet.py#L24)
- `_TEMPLATE_RULES` — [`L262`](../../../../../raw/code/wikify-repo/wikify/packet.py#L262)

