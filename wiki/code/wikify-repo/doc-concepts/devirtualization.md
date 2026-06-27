---
title: Devirtualization of dynamic dispatch (CHA over is_implementation)
type: doc-concept
provenance: doc
source: docs/design.md
updated: 2026-06-27
status: fresh
---
# Devirtualization of dynamic dispatch (CHA over is_implementation)

## Definition
The hardest seam in framework code is **dynamic dispatch**: a call like
`model_parts[0](inputs)` routes through `nn.Module.__call__` to an override that
SCIP's reference-scoping leaves with *no static call edge*. Walking the call graph
from entry points dies at exactly that seam, so the override (the real model code)
looks unreachable. **Devirtualization** is the design's named answer: a Class
Hierarchy Analysis (CHA) over SCIP's `is_implementation` relationships that
synthesizes the base→override edges reference-scoping misses. The doc states it
plainly: *"Devirtualization IS the connection op"* — it is the bridge that
coverage (representation) deliberately does not build.

## In wikify-repo (grounded)
The CHA pass is [`devirtualize`](../catalog/wikify/graph.md#devirtualize) over the
[`SymbolGraph`](../catalog/wikify/graph.md#SymbolGraph). It reads each symbol's
[`relationships`](../catalog/wikify/graph.md#Symbol.relationships) (the SCIP
`is_implementation` / override edges) and adds the missing base→override links so
that a caller reaching a base method is connected through to the concrete
implementations. Those synthesized edges then flow into the same
[`callers`](../catalog/wikify/graph.md#SymbolGraph.callers) /
[`callees`](../catalog/wikify/graph.md#SymbolGraph.callees) adjacency the rest of
the pipeline traverses — so packet-gathering and importance ranking can cross the
dispatch seam that a raw call graph cannot.

## Why it matters / when it applies
This is what keeps the wiki from mislabeling a backend's real work as dead code —
the exact blind spot of name-based call graphs (e.g. CodeGraphContext's dead-code
detector). The design is careful about its boundaries: **coverage still ≠
connection** — the two-tier coverage floor *represents* every module by
enumeration and never needs reachability, while devirtualization is a *separate,
optional* operation that genuinely *connects* base classes to their overrides.
Per design decision 6, any *heuristic* bridge (e.g. a future tree-sitter edge)
must carry `ast-heuristic` / `inferred` provenance so it never masquerades as a
resolved fact; devirtualization itself is grounded in SCIP's resolved
`is_implementation` relations, not a heuristic.

## Connections
- Code concepts: [wikify-graph](../concepts/wikify-graph.md) — the `devirtualize`
  CHA pass and the edge model it augments; [wikify-scip_index](../concepts/wikify-scip_index.md)
  — where `is_implementation` relationships are parsed; [wikify-coverage](../concepts/wikify-coverage.md)
  — the representation floor this connection op complements.
- Module catalogs: [wikify/graph.md](../catalog/wikify/graph.md) ·
  [wikify/scip_index.md](../catalog/wikify/scip_index.md).
- Related doc-concepts: [two-tier-coverage](two-tier-coverage.md) ·
  [packet-subgraph-grounding](packet-subgraph-grounding.md).

## Source
Extracted from `../../../raw/code/wikify-repo/docs/design.md` (kept in place):
"Load-bearing design decisions" #7 (dynamic-dispatch failure modes) and the
"Decisions log" entry *"Devirtualization IS the connection op."*
