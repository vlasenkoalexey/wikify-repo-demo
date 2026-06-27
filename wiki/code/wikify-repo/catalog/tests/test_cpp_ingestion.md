---
title: 'Module: tests/test_cpp_ingestion.py'
type: catalog
provenance: extracted
module: tests/test_cpp_ingestion.py
status: fresh
symbol_base: scip-python python wikify-repo 0.0.0 `tests.test_cpp_ingestion`/
symbols:
  test_merge_cpp_and_python: test_merge_cpp_and_python().
  test_cpp_call_structure.callees: test_cpp_call_structure().callees().
  test_cpp_symbols_and_kinds: test_cpp_symbols_and_kinds().
  cpp_index: cpp_index().
  test_cpp_call_structure: test_cpp_call_structure().
  SCIP_CLANG: SCIP_CLANG.
  pytestmark: pytestmark.
  _VENDORED: _VENDORED.
  FIXTURE: FIXTURE.
  PY_FIXTURE: PY_FIXTURE.
---
# Module: [`tests/test_cpp_ingestion.py`](../../../../../raw/code/wikify-repo/tests/test_cpp_ingestion.py)

## Functions
- `callees(name)` — [`L58`](../../../../../raw/code/wikify-repo/tests/test_cpp_ingestion.py#L58)
- `cpp_index(tmp_path_factory)` — [`L28`](../../../../../raw/code/wikify-repo/tests/test_cpp_ingestion.py#L28) — Run scip-clang on the C++ fixture → parsed SCIP index.
- `test_cpp_call_structure(cpp_index)` — [`L54`](../../../../../raw/code/wikify-repo/tests/test_cpp_ingestion.py#L54) — The reference-scoping callers/callees derivation works on C++ too. — documented in [wikify-scip_index](../../concepts/wikify-scip_index.md)
- `test_cpp_symbols_and_kinds(cpp_index)` — [`L46`](../../../../../raw/code/wikify-repo/tests/test_cpp_ingestion.py#L46) — documented in [wikify-scip_index](../../concepts/wikify-scip_index.md)
- `test_merge_cpp_and_python(cpp_index, tmp_path)` — [`L67`](../../../../../raw/code/wikify-repo/tests/test_cpp_ingestion.py#L67) — Two indexes (C++ + Python) union into ONE graph — the mixed-repo path. — documented in [wikify-graph](../../concepts/wikify-graph.md)

## Module values
- `FIXTURE` — [`L17`](../../../../../raw/code/wikify-repo/tests/test_cpp_ingestion.py#L17)
- `PY_FIXTURE` — [`L18`](../../../../../raw/code/wikify-repo/tests/test_cpp_ingestion.py#L18)
- `SCIP_CLANG` — [`L22`](../../../../../raw/code/wikify-repo/tests/test_cpp_ingestion.py#L22)
- `_VENDORED` — [`L21`](../../../../../raw/code/wikify-repo/tests/test_cpp_ingestion.py#L21)
- `pytestmark` — [`L24`](../../../../../raw/code/wikify-repo/tests/test_cpp_ingestion.py#L24)

