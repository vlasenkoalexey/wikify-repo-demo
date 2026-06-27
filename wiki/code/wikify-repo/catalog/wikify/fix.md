---
title: 'Module: wikify/fix.py'
type: catalog
provenance: extracted
module: wikify/fix.py
status: fresh
symbol_base: scip-python python wikify-repo 0.0.0 `wikify.fix`/
symbols:
  fix_page: fix_page().
  fix_silo: fix_silo().
  _cite_item_mention: _cite_item_mention().
  _packet_cite_map: _packet_cite_map().
  _BACKTICK: _BACKTICK.
  _CITE_LINE: _CITE_LINE.
  _strip_ticks: _strip_ticks().
---
# Module: [`wikify/fix.py`](../../../../../raw/code/wikify-repo/wikify/fix.py)

## Functions
- `_cite_item_mention(lines: list[str], start: int, cite_map: dict[str, str])` — [`L120`](../../../../../raw/code/wikify-repo/wikify/fix.py#L120) — Link the first backticked, citable, not-yet-linked symbol in the list item
- `_packet_cite_map(cache_dir: Path, slug: str, concept_slug: str)` — [`L41`](../../../../../raw/code/wikify-repo/wikify/fix.py#L41) — Parse the packet's ``- cite:`` lines → {symbol name: correct catalog link}.
- `_strip_ticks(label: str)` — [`L64`](../../../../../raw/code/wikify-repo/wikify/fix.py#L64)
- `fix_page(page_path: Path, graph: SymbolGraph, subgraph: set[str], cite_map: dict[str, str])` — [`L68`](../../../../../raw/code/wikify-repo/wikify/fix.py#L68) — Repair fixable lint errors in ``page_path`` in place. Returns #edits made. — documented in [wikify-lint](../../concepts/wikify-lint.md)
- `fix_silo(wiki_slug_dir: str | Path, graph: SymbolGraph, cache_dir: str | Path, slug: str)` — [`L143`](../../../../../raw/code/wikify-repo/wikify/fix.py#L143) — Auto-repair every concept page, then re-lint. Returns (#edits, residual report). — documented in [wikify-cli](../../concepts/wikify-cli.md)

## Module values
- `_BACKTICK` — [`L37`](../../../../../raw/code/wikify-repo/wikify/fix.py#L37)
- `_CITE_LINE` — [`L38`](../../../../../raw/code/wikify-repo/wikify/fix.py#L38)

