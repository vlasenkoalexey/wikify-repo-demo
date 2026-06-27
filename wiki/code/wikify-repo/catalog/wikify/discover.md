---
title: 'Module: wikify/discover.py'
type: catalog
provenance: extracted
module: wikify/discover.py
status: fresh
symbol_base: scip-python python wikify-repo 0.0.0 `wikify.discover`/
symbols:
  detect_communities: detect_communities().
  discover_concepts: discover_concepts().
  module_importance: module_importance().
  _library_nodes: _library_nodes().
  _excluded_fraction: _excluded_fraction().
  pareto_communities: pareto_communities().
  _undirected_adj: _undirected_adj().
  DiscoveredConcept.slug: DiscoveredConcept#slug.
  Community.interactions: Community#interactions().
  label_propagation: label_propagation().
  DiscoveredConcept: DiscoveredConcept#
  Community: Community#
  DiscoveredConcept.module: DiscoveredConcept#module.
  DiscoveredConcept.importance: DiscoveredConcept#importance.
  DiscoveredConcept.seeds: DiscoveredConcept#seeds.
  _excluded: _excluded().
  DEFAULT_EXCLUDES: DEFAULT_EXCLUDES.
  Community.internal_edges: Community#internal_edges.
  Community.boundary_edges: Community#boundary_edges.
  DiscoveredConcept.symbol_count: DiscoveredConcept#symbol_count.
  DiscoveredConcept.class_count: DiscoveredConcept#class_count.
  _concept_slug: _concept_slug().
  Community.label: Community#label.
  Community.members: Community#members.
  Community.top_members: Community#top_members.
  Community.modules: Community#modules.
  Community.neighbors: Community#neighbors.
---
# Module: [`wikify/discover.py`](../../../../../raw/code/wikify-repo/wikify/discover.py)

## Classes
### `Community`
- def: [`wikify/discover.py:122`](../../../../../raw/code/wikify-repo/wikify/discover.py#L122)
- signature: `class Community:`
- members:
  - `interactions(self)` — [`L132`](../../../../../raw/code/wikify-repo/wikify/discover.py#L132)
  - `boundary_edges` — [`L126`](../../../../../raw/code/wikify-repo/wikify/discover.py#L126)
  - `internal_edges` — [`L125`](../../../../../raw/code/wikify-repo/wikify/discover.py#L125)
  - `label` — [`L123`](../../../../../raw/code/wikify-repo/wikify/discover.py#L123)
  - `members` — [`L124`](../../../../../raw/code/wikify-repo/wikify/discover.py#L124)
  - `modules` — [`L128`](../../../../../raw/code/wikify-repo/wikify/discover.py#L128)
  - `neighbors` — [`L129`](../../../../../raw/code/wikify-repo/wikify/discover.py#L129)
  - `top_members` — [`L127`](../../../../../raw/code/wikify-repo/wikify/discover.py#L127)
- used by: [`detect_communities`](discover.md#detect_communities), [`pareto_communities`](discover.md#pareto_communities)

### `DiscoveredConcept`
- def: [`wikify/discover.py:33`](../../../../../raw/code/wikify-repo/wikify/discover.py#L33) — documented in [wikify-discover](../../concepts/wikify-discover.md)
- signature: `class DiscoveredConcept:`
- members:
  - `class_count` — [`L39`](../../../../../raw/code/wikify-repo/wikify/discover.py#L39) — documented in [wikify-discover](../../concepts/wikify-discover.md)
  - `importance` — [`L36`](../../../../../raw/code/wikify-repo/wikify/discover.py#L36) — documented in [wikify-discover](../../concepts/wikify-discover.md)
  - `module` — [`L35`](../../../../../raw/code/wikify-repo/wikify/discover.py#L35) — documented in [wikify-discover](../../concepts/wikify-discover.md)
  - `seeds` — [`L37`](../../../../../raw/code/wikify-repo/wikify/discover.py#L37) — documented in [wikify-discover](../../concepts/wikify-discover.md)
  - `slug` — [`L34`](../../../../../raw/code/wikify-repo/wikify/discover.py#L34) — documented in [wikify-discover](../../concepts/wikify-discover.md)
  - `symbol_count` — [`L38`](../../../../../raw/code/wikify-repo/wikify/discover.py#L38) — documented in [wikify-discover](../../concepts/wikify-discover.md)
- used by: [`prepare`](cli.md#prepare), [`discover_concepts`](discover.md#discover_concepts)  (3 test-only)

## Functions
- `_concept_slug(module: str)` — [`L46`](../../../../../raw/code/wikify-repo/wikify/discover.py#L46) — Readable concept slug from a module path (drop top package + extension). — documented in [wikify-discover](../../concepts/wikify-discover.md)
- `_excluded(path: str, excludes: tuple[str, ...])` — [`L42`](../../../../../raw/code/wikify-repo/wikify/discover.py#L42) — documented in [wikify-discover](../../concepts/wikify-discover.md)
- `_excluded_fraction(graph: SymbolGraph, members: list[str], excludes: tuple[str, ...])` — [`L183`](../../../../../raw/code/wikify-repo/wikify/discover.py#L183)
- `_library_nodes(graph: SymbolGraph, excludes: tuple[str, ...])` — [`L149`](../../../../../raw/code/wikify-repo/wikify/discover.py#L149) — In-repo nodes that are NOT test/example/benchmark — the library proper. — documented in [wikify-discover](../../concepts/wikify-discover.md)
- `_undirected_adj(graph: SymbolGraph, allowed: set[str] | None = None)` — [`L136`](../../../../../raw/code/wikify-repo/wikify/discover.py#L136)
- `detect_communities(graph: SymbolGraph, min_size: int = 4, excludes: tuple[str, ...] = DEFAULT_EXCLUDES)` — [`L189`](../../../../../raw/code/wikify-repo/wikify/discover.py#L189) — Cluster the graph and summarise each community (edges, top members, modules). — documented in [wikify-discover](../../concepts/wikify-discover.md)
- `discover_concepts(graph: SymbolGraph, max_deep: int = 24, min_importance: int = 25, seeds_per_concept: int = 4, excludes: tuple[str, ...] = DEFAULT_EXCLUDES)` — [`L75`](../../../../../raw/code/wikify-repo/wikify/discover.py#L75) — Top modules by centrality → deep concept specs, auto-seeded. Deterministic. — documented in [wikify-cli](../../concepts/wikify-cli.md)
- `label_propagation(graph: SymbolGraph, iterations: int = 10, allowed: set[str] | None = None)` — [`L157`](../../../../../raw/code/wikify-repo/wikify/discover.py#L157) — Deterministic label-propagation community detection over the ref graph. — documented in [wikify-discover](../../concepts/wikify-discover.md)
- `module_importance(graph: SymbolGraph)` — [`L58`](../../../../../raw/code/wikify-repo/wikify/discover.py#L58) — Per-module aggregate stats: fan-in (centrality), symbol/class counts, seeds. — documented in [wikify-coverage](../../concepts/wikify-coverage.md)
- `pareto_communities(graph: SymbolGraph, cover: float = 0.8, min_size: int = 4)` — [`L230`](../../../../../raw/code/wikify-repo/wikify/discover.py#L230) — The smallest set of top communities whose interactions cover ``cover`` of all. — documented in [wikify-discover](../../concepts/wikify-discover.md)

## Module values
- `DEFAULT_EXCLUDES` — [`L23`](../../../../../raw/code/wikify-repo/wikify/discover.py#L23) — documented in [wikify-discover](../../concepts/wikify-discover.md)

