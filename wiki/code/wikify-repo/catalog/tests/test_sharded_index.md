---
title: 'Module: tests/test_sharded_index.py'
type: catalog
provenance: extracted
module: tests/test_sharded_index.py
status: fresh
symbol_base: scip-python python wikify-repo 0.0.0 `tests.test_sharded_index`/
symbols:
  test_merged_index_builds_a_correct_graph: test_merged_index_builds_a_correct_graph().
  test_merge_repairs_target_relative_paths: test_merge_repairs_target_relative_paths().
  test_merge_keeps_repo_relative_spillover_and_prefers_complete: test_merge_keeps_repo_relative_spillover_and_prefers_complete().
  _doc: _doc().
  _write_index: _write_index().
  _fake_repo: _fake_repo().
---
# Module: [`tests/test_sharded_index.py`](../../../../../raw/code/wikify-repo/tests/test_sharded_index.py)

## Functions
- `_doc(rel_path: str, symbols: list[str])` — [`L18`](../../../../../raw/code/wikify-repo/tests/test_sharded_index.py#L18)
- `_fake_repo(tmp_path: Path)` — [`L33`](../../../../../raw/code/wikify-repo/tests/test_sharded_index.py#L33) — A repo tree mirroring two shardable subpackages + a shared dep file.
- `_write_index(path: Path, docs)` — [`L25`](../../../../../raw/code/wikify-repo/tests/test_sharded_index.py#L25)
- `test_merge_keeps_repo_relative_spillover_and_prefers_complete(tmp_path: Path)` — [`L57`](../../../../../raw/code/wikify-repo/tests/test_sharded_index.py#L57)
- `test_merge_repairs_target_relative_paths(tmp_path: Path)` — [`L44`](../../../../../raw/code/wikify-repo/tests/test_sharded_index.py#L44)
- `test_merged_index_builds_a_correct_graph(tmp_path: Path)` — [`L81`](../../../../../raw/code/wikify-repo/tests/test_sharded_index.py#L81) — End-to-end: a merged index drives build_graph with global monikers intact. — documented in [wikify-scip_index](../../concepts/wikify-scip_index.md)

