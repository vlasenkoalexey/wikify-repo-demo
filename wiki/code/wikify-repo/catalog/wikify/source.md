---
title: 'Module: wikify/source.py'
type: catalog
provenance: extracted
module: wikify/source.py
status: fresh
symbol_base: scip-python python wikify-repo 0.0.0 `wikify.source`/
symbols:
  read_snippet: read_snippet().
  body_span: body_span().
  body_hash: body_hash().
  _read_lines: _read_lines().
---
# Module: [`wikify/source.py`](../../../../../raw/code/wikify-repo/wikify/source.py)

## Functions
- `_read_lines(repo_root: Path, rel_path: str)` — [`L15`](../../../../../raw/code/wikify-repo/wikify/source.py#L15)
- `body_hash(repo_root: str | Path, sym: Symbol)` — [`L48`](../../../../../raw/code/wikify-repo/wikify/source.py#L48) — Stable hash of (signature + body source) for reconcile diffing (§5.5).
- `body_span(sym: Symbol)` — [`L23`](../../../../../raw/code/wikify-repo/wikify/source.py#L23) — 0-based [start_line, end_line] inclusive for the symbol's definition body.
- `read_snippet(repo_root: str | Path, sym: Symbol, max_lines: int = 60)` — [`L33`](../../../../../raw/code/wikify-repo/wikify/source.py#L33) — Return the source text of ``sym``'s definition body (capped). — documented in [wikify-graph](../../concepts/wikify-graph.md)

