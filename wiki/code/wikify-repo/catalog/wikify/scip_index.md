---
title: 'Module: wikify/scip_index.py'
type: catalog
provenance: extracted
module: wikify/scip_index.py
status: fresh
symbol_base: scip-python python wikify-repo 0.0.0 `wikify.scip_index`/
symbols:
  build_graph: build_graph().
  _process_document: _process_document().
  _synth_symbol: _synth_symbol().
  run_indexer_sharded: run_indexer_sharded().
  index_repo: index_repo().
  run_indexer: run_indexer().
  parse_index: parse_index().
  Range: Range.
  _merge_shards_index: _merge_shards_index().
  _path_from_moniker: _path_from_moniker().
  merge_shards: merge_shards().
  _has_documents: _has_documents().
  run_clang_indexer: run_clang_indexer().
  _span_size: _span_size().
  _NODE_HEAP_MB: _NODE_HEAP_MB.
  run_indexer_sharded._one: run_indexer_sharded()._one().
  _repair_doc_path: _repair_doc_path().
  _occ_range: _occ_range().
  _occ_enclosing: _occ_enclosing().
  _contains: _contains().
  _DEFINITION: _DEFINITION.
  _LOCALISH_SUFFIXES: _LOCALISH_SUFFIXES.
  _IMPORT: _IMPORT.
  _KIND_NAME: _KIND_NAME.
  _SUFFIX_KIND: _SUFFIX_KIND.
  _missing_target_files: _missing_target_files().
  _signature: _signature().
---
# Module: [`wikify/scip_index.py`](../../../../../raw/code/wikify-repo/wikify/scip_index.py)

## Functions
- `_contains(span: Range, point: tuple[int, int])` — [`L368`](../../../../../raw/code/wikify-repo/wikify/scip_index.py#L368) — Is (line, char) within half-open span [start, end)? — documented in [wikify-scip_index](../../concepts/wikify-scip_index.md)
- `_has_documents(scip_path: Path)` — [`L102`](../../../../../raw/code/wikify-repo/wikify/scip_index.py#L102) — True if ``scip_path`` exists and parses to a non-empty SCIP index.
- `_merge_shards_index(project_dir: str | Path, shards: list[tuple[str, Path]])` — [`L167`](../../../../../raw/code/wikify-repo/wikify/scip_index.py#L167) — Union shard ``.scip`` files into one Index, repairing target-relative paths. — documented in [wikify-scip_index](../../concepts/wikify-scip_index.md)
- `_missing_target_files(project_dir: str | Path, targets: list[str], emitted: set[str])` — [`L259`](../../../../../raw/code/wikify-repo/wikify/scip_index.py#L259) — Repo-relative ``.py`` files under ``targets`` that ``emitted`` doesn't cover.
- `_occ_enclosing(occ)` — [`L352`](../../../../../raw/code/wikify-repo/wikify/scip_index.py#L352) — documented in [wikify-scip_index](../../concepts/wikify-scip_index.md)
- `_occ_range(occ)` — [`L336`](../../../../../raw/code/wikify-repo/wikify/scip_index.py#L336) — documented in [wikify-scip_index](../../concepts/wikify-scip_index.md)
- `_one(item: tuple[int, str])` — [`L132`](../../../../../raw/code/wikify-repo/wikify/scip_index.py#L132) — documented in [wikify-scip_index](../../concepts/wikify-scip_index.md)
- `_path_from_moniker(doc, project_dir: Path)` — [`L227`](../../../../../raw/code/wikify-repo/wikify/scip_index.py#L227) — Derive a repo-relative file path from a document's symbol monikers. — documented in [wikify-monikers](../../concepts/wikify-monikers.md)
- `_process_document(g: SymbolGraph, doc)` — [`L487`](../../../../../raw/code/wikify-repo/wikify/scip_index.py#L487) — documented in [wikify-graph](../../concepts/wikify-graph.md)
- `_repair_doc_path(doc, project_dir: Path, base: str)` — [`L205`](../../../../../raw/code/wikify-repo/wikify/scip_index.py#L205) — Restore a shard document's ``relative_path`` to repo-relative, in place. — documented in [wikify-scip_index](../../concepts/wikify-scip_index.md)
- `_signature(si)` — [`L380`](../../../../../raw/code/wikify-repo/wikify/scip_index.py#L380) — Best-effort signature: first fenced code block in the documentation.
- `_span_size(span: Range)` — [`L375`](../../../../../raw/code/wikify-repo/wikify/scip_index.py#L375) — documented in [wikify-scip_index](../../concepts/wikify-scip_index.md)
- `_synth_symbol(moniker: str)` — [`L464`](../../../../../raw/code/wikify-repo/wikify/scip_index.py#L464) — Build a minimal Symbol from a moniker alone (no SymbolInformation). — documented in [wikify-graph](../../concepts/wikify-graph.md)
- `build_graph(*indexes)` — [`L396`](../../../../../raw/code/wikify-repo/wikify/scip_index.py#L396) — Build one SymbolGraph from one OR MORE SCIP indexes. — documented in [wikify-cli](../../concepts/wikify-cli.md)
- `index_repo(project_dir: str | Path, output_path: str | Path, project_name: str | None = None)` — [`L541`](../../../../../raw/code/wikify-repo/wikify/scip_index.py#L541) — End-to-end: run the indexer, parse, build the graph. — documented in [wikify-graph](../../concepts/wikify-graph.md)
- `merge_shards(project_dir: str | Path, shards: list[tuple[str, Path]], output_path: str | Path)` — [`L247`](../../../../../raw/code/wikify-repo/wikify/scip_index.py#L247) — Union shard ``.scip`` files into ``output_path`` (path-writing wrapper).
- `parse_index(scip_path: str | Path)` — [`L327`](../../../../../raw/code/wikify-repo/wikify/scip_index.py#L327) — documented in [wikify-scip_index](../../concepts/wikify-scip_index.md)
- `run_clang_indexer(project_root: str | Path, compile_commands_path: str | Path, output_path: str | Path, scip_clang_bin: str = "scip-clang")` — [`L277`](../../../../../raw/code/wikify-repo/wikify/scip_index.py#L277) — Invoke ``scip-clang`` against a ``compile_commands.json`` → ``output_path`` (.scip).
- `run_indexer(project_dir: str | Path, output_path: str | Path, project_name: str | None = None, project_version: str = "0.0.0", target_only: str | None = None, heap_mb: str | int | None = None)` — [`L56`](../../../../../raw/code/wikify-repo/wikify/scip_index.py#L56) — Invoke ``scip-python index`` on ``project_dir`` → ``output_path`` (.scip). — documented in [wikify-cli](../../concepts/wikify-cli.md)
- `run_indexer_sharded(project_dir: str | Path, output_path: str | Path, targets: list[str], project_name: str | None = None, project_version: str = "0.0.0", max_parallel: int = 8, heap_mb: str | int | None = None)` — [`L110`](../../../../../raw/code/wikify-repo/wikify/scip_index.py#L110) — Index ``targets`` concurrently (one scip-python per ``--target-only``), then — documented in [wikify-ast_fallback](../../concepts/wikify-ast_fallback.md)

## Module values
- `Range` — [`L35`](../../../../../raw/code/wikify-repo/wikify/scip_index.py#L35) — documented in [wikify-scip_index](../../concepts/wikify-scip_index.md)
- `_DEFINITION` — [`L29`](../../../../../raw/code/wikify-repo/wikify/scip_index.py#L29)
- `_IMPORT` — [`L30`](../../../../../raw/code/wikify-repo/wikify/scip_index.py#L30)
- `_KIND_NAME` — [`L33`](../../../../../raw/code/wikify-repo/wikify/scip_index.py#L33)
- `_LOCALISH_SUFFIXES` — [`L38`](../../../../../raw/code/wikify-repo/wikify/scip_index.py#L38)
- `_NODE_HEAP_MB` — [`L25`](../../../../../raw/code/wikify-repo/wikify/scip_index.py#L25)
- `_SUFFIX_KIND` — [`L44`](../../../../../raw/code/wikify-repo/wikify/scip_index.py#L44)

