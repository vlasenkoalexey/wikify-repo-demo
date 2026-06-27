---
title: 'Module: wikify/graph.py'
type: catalog
provenance: extracted
module: wikify/graph.py
status: fresh
symbol_base: scip-python python wikify-repo 0.0.0 `wikify.graph`/
symbols:
  SymbolGraph: SymbolGraph#
  Symbol.def_path: Symbol#def_path.
  Symbol: Symbol#
  Symbol.name: Symbol#name.
  SymbolGraph.symbols: SymbolGraph#symbols.
  SymbolGraph.add_symbol: SymbolGraph#add_symbol().
  Symbol.suffix: Symbol#suffix.
  Symbol.moniker: Symbol#moniker.
  Symbol.def_line: Symbol#def_line.
  Symbol.kind: Symbol#kind.
  SymbolGraph.add_edge: SymbolGraph#add_edge().
  devirtualize: devirtualize().
  Symbol.signature: Symbol#signature.
  SymbolGraph.callees: SymbolGraph#callees().
  SymbolGraph.importance: SymbolGraph#importance().
  Symbol.is_callable: Symbol#is_callable().
  Symbol.doc_summary: Symbol#doc_summary().
  Symbol.documentation: Symbol#documentation.
  SymbolGraph.callers: SymbolGraph#callers().
  SymbolGraph.find: SymbolGraph#find().
  Symbol.docstring: Symbol#docstring().
  Symbol.relationships: Symbol#relationships.
  SymbolGraph.is_virtual: SymbolGraph#is_virtual().
  SymbolGraph._callees: SymbolGraph#_callees.
  SymbolGraph.ref_count: SymbolGraph#ref_count.
  Symbol.enclosing: Symbol#enclosing.
  SymbolGraph._callers: SymbolGraph#_callers.
  SymbolGraph.__len__: SymbolGraph#__len__().
  SymbolGraph.__contains__: SymbolGraph#__contains__().
  SymbolGraph.refs: SymbolGraph#refs.
  SymbolGraph.virtual_edges: SymbolGraph#virtual_edges.
  _clean_doc: _clean_doc().
  _CALLABLE_KINDS: _CALLABLE_KINDS.
  SymbolGraph.__init__: SymbolGraph#__init__().
---
# Module: [`wikify/graph.py`](../../../../../raw/code/wikify-repo/wikify/graph.py)

## Classes
### `Symbol`
- def: [`wikify/graph.py:18`](../../../../../raw/code/wikify-repo/wikify/graph.py#L18) — documented in [wikify-cli](../../concepts/wikify-cli.md)
- doc: One global, in-repo symbol (a node in the citation namespace).
- signature: `class Symbol:`
- members:
  - `doc_summary(self)` — [`L55`](../../../../../raw/code/wikify-repo/wikify/graph.py#L55) — First non-empty line of the docstring (the summary), or ''. — documented in [wikify-coverage](../../concepts/wikify-coverage.md)
  - `docstring(self)` — [`L38`](../../../../../raw/code/wikify-repo/wikify/graph.py#L38) — Author-written prose from ``documentation``, signature code-fence stripped. — documented in [wikify-coverage](../../concepts/wikify-coverage.md)
  - `is_callable(self)` — [`L34`](../../../../../raw/code/wikify-repo/wikify/graph.py#L34)
  - `def_line` — [`L26`](../../../../../raw/code/wikify-repo/wikify/graph.py#L26) — documented in [wikify-cli](../../concepts/wikify-cli.md)
  - `def_path` — [`L25`](../../../../../raw/code/wikify-repo/wikify/graph.py#L25) — documented in [wikify-cli](../../concepts/wikify-cli.md)
  - `documentation` — [`L29`](../../../../../raw/code/wikify-repo/wikify/graph.py#L29) — documented in [wikify-coverage](../../concepts/wikify-coverage.md)
  - `enclosing` — [`L27`](../../../../../raw/code/wikify-repo/wikify/graph.py#L27) — documented in [wikify-scip_index](../../concepts/wikify-scip_index.md)
  - `kind` — [`L22`](../../../../../raw/code/wikify-repo/wikify/graph.py#L22) — documented in [wikify-cli](../../concepts/wikify-cli.md)
  - `moniker` — [`L21`](../../../../../raw/code/wikify-repo/wikify/graph.py#L21) — documented in [wikify-cli](../../concepts/wikify-cli.md)
  - `name` — [`L24`](../../../../../raw/code/wikify-repo/wikify/graph.py#L24) — documented in [wikify-cli](../../concepts/wikify-cli.md)
  - `relationships` — [`L30`](../../../../../raw/code/wikify-repo/wikify/graph.py#L30) — documented in [wikify-scip_index](../../concepts/wikify-scip_index.md)
  - `signature` — [`L28`](../../../../../raw/code/wikify-repo/wikify/graph.py#L28) — documented in [wikify-scip_index](../../concepts/wikify-scip_index.md)
  - `suffix` — [`L23`](../../../../../raw/code/wikify-repo/wikify/graph.py#L23) — documented in [wikify-cli](../../concepts/wikify-cli.md)
- uses (calls/refs, reference-scoped): [`_CALLABLE_KINDS`](graph.md#_CALLABLE_KINDS), [`_clean_doc`](graph.md#_clean_doc)
- used by: [`build_packet`](packet.md#build_packet), [`build_graph`](scip_index.md#build_graph), [`render_catalog`](coverage.md#render_catalog), [`detect_communities`](discover.md#detect_communities), [`symbols`](graph.md#SymbolGraph.symbols), [`add_symbol`](graph.md#SymbolGraph.add_symbol), [`_process_document`](scip_index.md#_process_document), [`compute_report`](coverage.md#compute_report), [`collect_tests`](evidence.md#collect_tests), [`_synth_symbol`](scip_index.md#_synth_symbol), [`_link_targets`](coverage.md#render_catalog._link_targets), [`documentable_symbols`](coverage.md#documentable_symbols), [`devirtualize`](graph.md#devirtualize), [`covered_monikers`](coverage.md#covered_monikers), [`module_importance`](discover.md#module_importance), [`class_symbols`](coverage.md#class_symbols), [`read_snippet`](source.md#read_snippet), [`_library_nodes`](discover.md#_library_nodes), [`_rel_names`](coverage.md#_rel_names), [`auto_seeds`](packet.md#auto_seeds), [`_short`](packet.md#_short), [`_excluded_fraction`](discover.md#_excluded_fraction), [`body_hash`](source.md#body_hash), [`body_span`](source.md#body_span), [`_clean_sig`](coverage.md#_clean_sig), [`find`](graph.md#SymbolGraph.find), [`_params`](coverage.md#_params), [`by_module`](coverage.md#by_module)  (15 test-only)

### `SymbolGraph`
- def: [`wikify/graph.py:87`](../../../../../raw/code/wikify-repo/wikify/graph.py#L87) — documented in [wikify-cli](../../concepts/wikify-cli.md)
- doc: In-repo symbol graph: nodes + reference-derived edges.
- signature: `class SymbolGraph:`
- members:
  - `add_edge(self, caller: str, callee: str, virtual: bool = False)` — [`L115`](../../../../../raw/code/wikify-repo/wikify/graph.py#L115) — Record that ``caller``'s body references in-repo symbol ``callee``. — documented in [wikify-scip_index](../../concepts/wikify-scip_index.md)
  - `add_symbol(self, sym: Symbol)` — [`L108`](../../../../../raw/code/wikify-repo/wikify/graph.py#L108) — documented in [wikify-graph](../../concepts/wikify-graph.md)
  - `callees(self, moniker: str)` — [`L129`](../../../../../raw/code/wikify-repo/wikify/graph.py#L129) — documented in [wikify-coverage](../../concepts/wikify-coverage.md)
  - `callers(self, moniker: str)` — [`L132`](../../../../../raw/code/wikify-repo/wikify/graph.py#L132) — documented in [wikify-coverage](../../concepts/wikify-coverage.md)
  - `find(self, name: str)` — [`L140`](../../../../../raw/code/wikify-repo/wikify/graph.py#L140) — Monikers whose terminal descriptor name == ``name`` (test/debug helper).
  - `importance(self, moniker: str)` — [`L135`](../../../../../raw/code/wikify-repo/wikify/graph.py#L135) — context-sherpa rank: outbound*5 + ref_count*2 (no clustering). — documented in [wikify-coverage](../../concepts/wikify-coverage.md)
  - `is_virtual(self, caller: str, callee: str)` — [`L144`](../../../../../raw/code/wikify-repo/wikify/graph.py#L144)
  - `ref_count` — [`L100`](../../../../../raw/code/wikify-repo/wikify/graph.py#L100) — documented in [wikify-scip_index](../../concepts/wikify-scip_index.md)
  - `refs` — [`L101`](../../../../../raw/code/wikify-repo/wikify/graph.py#L101) — documented in [wikify-scip_index](../../concepts/wikify-scip_index.md)
  - `symbols` — [`L97`](../../../../../raw/code/wikify-repo/wikify/graph.py#L97) — documented in [wikify-coverage](../../concepts/wikify-coverage.md)
  - `virtual_edges` — [`L104`](../../../../../raw/code/wikify-repo/wikify/graph.py#L104)
- protocol/private: `__contains__`[`L150`](../../../../../raw/code/wikify-repo/wikify/graph.py#L150), `__init__`[`L96`](../../../../../raw/code/wikify-repo/wikify/graph.py#L96), `__len__`[`L147`](../../../../../raw/code/wikify-repo/wikify/graph.py#L147), `_callees`[`L98`](../../../../../raw/code/wikify-repo/wikify/graph.py#L98), `_callers`[`L99`](../../../../../raw/code/wikify-repo/wikify/graph.py#L99)
- uses (calls/refs, reference-scoped): [`Symbol`](graph.md#Symbol), [`name`](graph.md#Symbol.name), [`moniker`](graph.md#Symbol.moniker)
- used by: [`build_packet`](packet.md#build_packet), [`build_graph`](scip_index.md#build_graph), [`render_catalog`](coverage.md#render_catalog), [`detect_communities`](discover.md#detect_communities), [`_process_document`](scip_index.md#_process_document), [`compute_report`](coverage.md#compute_report), [`collect_tests`](evidence.md#collect_tests), [`lint_page`](lint.md#lint_page), [`compute_plan`](diff.md#compute_plan), [`discover_concepts`](discover.md#discover_concepts), [`fix_page`](fix.md#fix_page), [`_link_targets`](coverage.md#render_catalog._link_targets), [`documentable_symbols`](coverage.md#documentable_symbols), [`gather_subgraph`](packet.md#gather_subgraph), [`emit_catalogs`](coverage.md#emit_catalogs), [`lint_doc_concepts`](lint.md#lint_doc_concepts), [`devirtualize`](graph.md#devirtualize), [`covered_monikers`](coverage.md#covered_monikers), [`lint_silo`](lint.md#lint_silo), [`module_importance`](discover.md#module_importance), [`class_symbols`](coverage.md#class_symbols), [`fix_silo`](fix.md#fix_silo), [`_library_nodes`](discover.md#_library_nodes), [`auto_seeds`](packet.md#auto_seeds), [`index_repo`](scip_index.md#index_repo), [`resolve_seeds`](packet.md#resolve_seeds), [`_short`](packet.md#_short), [`current_hashes`](diff.md#current_hashes), [`_excluded_fraction`](discover.md#_excluded_fraction), [`pareto_communities`](discover.md#pareto_communities), [`_edge_name`](packet.md#_edge_name), [`_undirected_adj`](discover.md#_undirected_adj), [`class_connections`](coverage.md#class_connections), [`symbol_anchor_map`](coverage.md#symbol_anchor_map), [`label_propagation`](discover.md#label_propagation), [`relevance`](packet.md#gather_subgraph.relevance)  (20 test-only)

## Functions
- `_clean_doc(text: str)` — [`L64`](../../../../../raw/code/wikify-repo/wikify/graph.py#L64) — Undo scip-python's markdown escaping for readable inline display.
- `devirtualize(graph: SymbolGraph)` — [`L154`](../../../../../raw/code/wikify-repo/wikify/graph.py#L154) — Class Hierarchy Analysis: cross the dynamic-dispatch seam the reference — documented in [wikify-cli](../../concepts/wikify-cli.md)

## Module values
- `_CALLABLE_KINDS` — [`L75`](../../../../../raw/code/wikify-repo/wikify/graph.py#L75)

