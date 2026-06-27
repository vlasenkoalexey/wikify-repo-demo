---
title: 'Module: wikify/evidence.py'
type: catalog
provenance: extracted
module: wikify/evidence.py
status: fresh
symbol_base: scip-python python wikify-repo 0.0.0 `wikify.evidence`/
symbols:
  collect_tests: collect_tests().
  TestEvidence.path: TestEvidence#path.
  is_test_path: is_test_path().
  TestEvidence: TestEvidence#
  TestEvidence.line: TestEvidence#line.
  TestEvidence.name: TestEvidence#name.
  TestEvidence.exercises: TestEvidence#exercises.
  TestEvidence.moniker: TestEvidence#moniker.
  _matches_globs: _matches_globs().
---
# Module: [`wikify/evidence.py`](../../../../../raw/code/wikify-repo/wikify/evidence.py)

## Classes
### `TestEvidence`
- def: [`wikify/evidence.py:18`](../../../../../raw/code/wikify-repo/wikify/evidence.py#L18)
- signature: `class TestEvidence:`
- members:
  - `exercises` — [`L23`](../../../../../raw/code/wikify-repo/wikify/evidence.py#L23)
  - `line` — [`L22`](../../../../../raw/code/wikify-repo/wikify/evidence.py#L22)
  - `moniker` — [`L19`](../../../../../raw/code/wikify-repo/wikify/evidence.py#L19)
  - `name` — [`L20`](../../../../../raw/code/wikify-repo/wikify/evidence.py#L20)
  - `path` — [`L21`](../../../../../raw/code/wikify-repo/wikify/evidence.py#L21)
- used by: [`build_packet`](packet.md#build_packet), [`collect_tests`](evidence.md#collect_tests)

## Functions
- `_matches_globs(path: str, globs: list[str])` — [`L26`](../../../../../raw/code/wikify-repo/wikify/evidence.py#L26)
- `collect_tests(graph: SymbolGraph, test_globs: list[str], subgraph: set[str])` — [`L42`](../../../../../raw/code/wikify-repo/wikify/evidence.py#L42) — Tests whose body exercises any symbol in ``subgraph`` (asserts → symbols). — documented in [wikify-cli](../../concepts/wikify-cli.md)
- `is_test_path(path: str | None, test_globs: list[str])` — [`L33`](../../../../../raw/code/wikify-repo/wikify/evidence.py#L33)

