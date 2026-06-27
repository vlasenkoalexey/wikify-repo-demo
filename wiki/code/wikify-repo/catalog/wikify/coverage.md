---
title: 'Module: wikify/coverage.py'
type: catalog
provenance: extracted
module: wikify/coverage.py
status: fresh
symbol_base: scip-python python wikify-repo 0.0.0 `wikify.coverage`/
symbols:
  render_catalog: render_catalog().
  compute_report: compute_report().
  CoverageReport.render: CoverageReport#render().
  documentable_symbols: documentable_symbols().
  render_catalog._link_targets: render_catalog()._link_targets().
  emit_catalogs: emit_catalogs().
  covered_monikers: covered_monikers().
  qualified_name: qualified_name().
  class_symbols: class_symbols().
  _rel_names: _rel_names().
  render_catalog._detail: render_catalog()._detail().
  symbol_anchor_map: symbol_anchor_map().
  class_connections: class_connections().
  CoverageReport.represented: CoverageReport#represented().
  _clean_sig: _clean_sig().
  by_module: by_module().
  CoverageReport.total: CoverageReport#total.
  _params: _params().
  CoverageReport.pct_deep: CoverageReport#pct_deep().
  CoverageReport.pct_represented: CoverageReport#pct_represented().
  catalog_rel_path: catalog_rel_path().
  catalog_ref: catalog_ref().
  _owner_class: _owner_class().
  CoverageReport.covered: CoverageReport#covered.
  render_catalog._loc_line: render_catalog()._loc_line().
  CoverageReport.catalog_only: CoverageReport#catalog_only.
  CoverageReport.uncovered_examples: CoverageReport#uncovered_examples.
  _rel_catalog_link: _rel_catalog_link().
  _is_noise_path: _is_noise_path().
  render_catalog._loc: render_catalog()._loc().
  CoverageReport.classes_total: CoverageReport#classes_total.
  CoverageReport.classes_represented: CoverageReport#classes_represented.
  _src_link: _src_link().
  CoverageReport: CoverageReport#
  CoverageReport.modules: CoverageReport#modules.
  render_catalog._cov_tag: render_catalog()._cov_tag().
  DOCUMENTABLE_SUFFIXES: DOCUMENTABLE_SUFFIXES.
  _CATALOG_LINK: _CATALOG_LINK.
  _ANCHOR_UNSAFE: _ANCHOR_UNSAFE.
  _NOISE_SEGMENTS: _NOISE_SEGMENTS.
  _compress_anchor_map: _compress_anchor_map().
---
# Module: [`wikify/coverage.py`](../../../../../raw/code/wikify-repo/wikify/coverage.py)

## Classes
### `CoverageReport`
- def: [`wikify/coverage.py:118`](../../../../../raw/code/wikify-repo/wikify/coverage.py#L118)
- signature: `class CoverageReport:`
- members:
  - `pct_deep(self)` — [`L132`](../../../../../raw/code/wikify-repo/wikify/coverage.py#L132) — documented in [wikify-coverage](../../concepts/wikify-coverage.md)
  - `pct_represented(self)` — [`L136`](../../../../../raw/code/wikify-repo/wikify/coverage.py#L136) — documented in [wikify-coverage](../../concepts/wikify-coverage.md)
  - `render(self)` — [`L139`](../../../../../raw/code/wikify-repo/wikify/coverage.py#L139) — documented in [wikify-coverage](../../concepts/wikify-coverage.md)
  - `represented(self)` — [`L128`](../../../../../raw/code/wikify-repo/wikify/coverage.py#L128) — documented in [wikify-coverage](../../concepts/wikify-coverage.md)
  - `catalog_only` — [`L121`](../../../../../raw/code/wikify-repo/wikify/coverage.py#L121) — documented in [wikify-coverage](../../concepts/wikify-coverage.md)
  - `classes_represented` — [`L124`](../../../../../raw/code/wikify-repo/wikify/coverage.py#L124) — documented in [wikify-coverage](../../concepts/wikify-coverage.md)
  - `classes_total` — [`L123`](../../../../../raw/code/wikify-repo/wikify/coverage.py#L123)
  - `covered` — [`L120`](../../../../../raw/code/wikify-repo/wikify/coverage.py#L120) — documented in [wikify-coverage](../../concepts/wikify-coverage.md)
  - `modules` — [`L122`](../../../../../raw/code/wikify-repo/wikify/coverage.py#L122)
  - `total` — [`L119`](../../../../../raw/code/wikify-repo/wikify/coverage.py#L119) — documented in [wikify-coverage](../../concepts/wikify-coverage.md)
  - `uncovered_examples` — [`L125`](../../../../../raw/code/wikify-repo/wikify/coverage.py#L125) — documented in [wikify-coverage](../../concepts/wikify-coverage.md)
- used by: [`finalize`](cli.md#finalize), [`compute_report`](coverage.md#compute_report), [`coverage`](cli.md#coverage)  (1 test-only)

## Functions
- `_clean_sig(sym: Symbol)` — [`L243`](../../../../../raw/code/wikify-repo/wikify/coverage.py#L243) — The real `def …`/`class …` line — decorator lines stripped, collapsed to one — documented in [wikify-coverage](../../concepts/wikify-coverage.md)
- `_compress_anchor_map(anchor_map: dict[str, str])` — [`L329`](../../../../../raw/code/wikify-repo/wikify/coverage.py#L329) — Factor the common moniker prefix out of an anchor→moniker map.
- `_cov_tag(moniker: str)` — [`L370`](../../../../../raw/code/wikify-repo/wikify/coverage.py#L370)
- `_detail(sym, moniker: str)` — [`L388`](../../../../../raw/code/wikify-repo/wikify/coverage.py#L388) — One symbol's detail bullet: `name(params)` — Lnnn — docstring summary. — documented in [wikify-coverage](../../concepts/wikify-coverage.md)
- `_is_noise_path(def_path: str | None)` — [`L317`](../../../../../raw/code/wikify-repo/wikify/coverage.py#L317)
- `_link_targets(targets: list[str], cap: int = 40)` — [`L418`](../../../../../raw/code/wikify-repo/wikify/coverage.py#L418) — Render in-repo edge targets, ranked by importance, linked to their catalog. — documented in [wikify-coverage](../../concepts/wikify-coverage.md)
- `_loc(sym)` — [`L375`](../../../../../raw/code/wikify-repo/wikify/coverage.py#L375) — `def: file:line`, linked to the pinned source when ``source_base`` is set. — documented in [wikify-coverage](../../concepts/wikify-coverage.md)
- `_loc_line(sym)` — [`L382`](../../../../../raw/code/wikify-repo/wikify/coverage.py#L382) — Compact source link `Lnnn` (the file is the catalog's module). — documented in [wikify-coverage](../../concepts/wikify-coverage.md)
- `_owner_class(moniker: str)` — [`L231`](../../../../../raw/code/wikify-repo/wikify/coverage.py#L231) — Name of the enclosing class for a method/term, or None if module-level. — documented in [wikify-coverage](../../concepts/wikify-coverage.md)
- `_params(sym: Symbol)` — [`L254`](../../../../../raw/code/wikify-repo/wikify/coverage.py#L254) — The parameter tuple from a callable's signature, e.g. ``(self, modules=None)``. — documented in [wikify-coverage](../../concepts/wikify-coverage.md)
- `_rel_catalog_link(from_module: str, to_module: str)` — [`L271`](../../../../../raw/code/wikify-repo/wikify/coverage.py#L271) — Relative link from one module's catalog page to another's.
- `_rel_names(sym: Symbol)` — [`L300`](../../../../../raw/code/wikify-repo/wikify/coverage.py#L300) — documented in [wikify-monikers](../../concepts/wikify-monikers.md)
- `_src_link(source_base: str | None, path: str, line: int | None = None)` — [`L322`](../../../../../raw/code/wikify-repo/wikify/coverage.py#L322) — Permalink into the pinned source (``<base>/<path>#L<line>``), or None.
- `by_module(symbols: dict[str, Symbol])` — [`L106`](../../../../../raw/code/wikify-repo/wikify/coverage.py#L106) — Group documentable monikers by their definition file (the module). — documented in [wikify-coverage](../../concepts/wikify-coverage.md)
- `catalog_ref(module_path: str, moniker: str)` — [`L215`](../../../../../raw/code/wikify-repo/wikify/coverage.py#L215) — Citation target a concept page uses (``concepts/`` → ``../catalog/…#anchor``).
- `catalog_rel_path(module_path: str)` — [`L188`](../../../../../raw/code/wikify-repo/wikify/coverage.py#L188) — Map a module file path to its catalog page path (mirrors the source tree). — documented in [wikify-coverage](../../concepts/wikify-coverage.md)
- `class_connections(graph: SymbolGraph, class_moniker: str, member_monikers: list[str])` — [`L279`](../../../../../raw/code/wikify-repo/wikify/coverage.py#L279) — Roll member edges up to the class → (uses, used_by) target monikers. — documented in [wikify-coverage](../../concepts/wikify-coverage.md)
- `class_symbols(graph: SymbolGraph)` — [`L70`](../../../../../raw/code/wikify-repo/wikify/coverage.py#L70) — In-repo class definitions only (suffix == Type). — documented in [wikify-coverage](../../concepts/wikify-coverage.md)
- `compute_report(graph: SymbolGraph, wiki_slug_dir: str | Path, catalogued: set[str] | None = None)` — [`L151`](../../../../../raw/code/wikify-repo/wikify/coverage.py#L151) — Classify every documentable symbol as covered / catalog-only / unrepresented. — documented in [wikify-cli](../../concepts/wikify-cli.md)
- `covered_monikers(graph: SymbolGraph, wiki_slug_dir: str | Path)` — [`L82`](../../../../../raw/code/wikify-repo/wikify/coverage.py#L82) — Map each concept-cited moniker → the concept page slug that cites it. — documented in [wikify-coverage](../../concepts/wikify-coverage.md)
- `documentable_symbols(graph: SymbolGraph)` — [`L61`](../../../../../raw/code/wikify-repo/wikify/coverage.py#L61) — Every in-repo symbol worth representing in the wiki (has a def + is citable). — documented in [wikify-coverage](../../concepts/wikify-coverage.md)
- `emit_catalogs(graph: SymbolGraph, wiki_slug_dir: str | Path, repo_dir: str | Path | None = None, source_url: str | None = None)` — [`L501`](../../../../../raw/code/wikify-repo/wikify/coverage.py#L501) — Write one catalog page per in-repo module. Returns (catalogued monikers, paths). — documented in [wikify-cli](../../concepts/wikify-cli.md)
- `qualified_name(moniker: str)` — [`L199`](../../../../../raw/code/wikify-repo/wikify/coverage.py#L199) — Anchor for a symbol within its module catalog: descriptor names after the — documented in [wikify-coverage](../../concepts/wikify-coverage.md)
- `render_catalog(graph: SymbolGraph, module_path: str, monikers: list[str], covered: dict[str, str], source_base: str | None = None)` — [`L343`](../../../../../raw/code/wikify-repo/wikify/coverage.py#L343) — Render one module's catalog page from the graph (no synthesis). — documented in [wikify-coverage](../../concepts/wikify-coverage.md)
- `symbol_anchor_map(graph: SymbolGraph, monikers: list[str])` — [`L220`](../../../../../raw/code/wikify-repo/wikify/coverage.py#L220) — {anchor → moniker} for a module's symbols (the linter's resolution table). — documented in [wikify-coverage](../../concepts/wikify-coverage.md)

## Module values
- `DOCUMENTABLE_SUFFIXES` — [`L55`](../../../../../raw/code/wikify-repo/wikify/coverage.py#L55)
- `_ANCHOR_UNSAFE` — [`L196`](../../../../../raw/code/wikify-repo/wikify/coverage.py#L196)
- `_CATALOG_LINK` — [`L79`](../../../../../raw/code/wikify-repo/wikify/coverage.py#L79)
- `_NOISE_SEGMENTS` — [`L313`](../../../../../raw/code/wikify-repo/wikify/coverage.py#L313)

