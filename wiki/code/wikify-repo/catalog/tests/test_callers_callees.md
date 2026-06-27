---
title: 'Module: tests/test_callers_callees.py'
type: catalog
provenance: extracted
module: tests/test_callers_callees.py
status: fresh
symbol_base: scip-python python wikify-repo 0.0.0 `tests.test_callers_callees`/
symbols:
  _one: _one().
  graph: graph().
  test_callees: test_callees().
  test_callers: test_callers().
  test_method_body_scoping: test_method_body_scoping().
  test_importance_rank: test_importance_rank().
  FIXTURE: FIXTURE.
  pytestmark: pytestmark.
  test_symbols_present: test_symbols_present().
---
# Module: [`tests/test_callers_callees.py`](../../../../../raw/code/wikify-repo/tests/test_callers_callees.py)

## Functions
- `_one(graph, name)` — [`L28`](../../../../../raw/code/wikify-repo/tests/test_callers_callees.py#L28) — Resolve the single in-repo moniker whose terminal descriptor is `name`.
- `graph(tmp_path_factory)` — [`L23`](../../../../../raw/code/wikify-repo/tests/test_callers_callees.py#L23)
- `test_callees(graph)` — [`L41`](../../../../../raw/code/wikify-repo/tests/test_callers_callees.py#L41)
- `test_callers(graph)` — [`L53`](../../../../../raw/code/wikify-repo/tests/test_callers_callees.py#L53)
- `test_importance_rank(graph)` — [`L71`](../../../../../raw/code/wikify-repo/tests/test_callers_callees.py#L71) — Importance = outbound*5 + ref_count*2; compute (2 callees) outranks add.
- `test_method_body_scoping(graph)` — [`L64`](../../../../../raw/code/wikify-repo/tests/test_callers_callees.py#L64) — A reference inside a method body must scope to the method, not the class.
- `test_symbols_present(graph)` — [`L36`](../../../../../raw/code/wikify-repo/tests/test_callers_callees.py#L36)

## Module values
- `FIXTURE` — [`L15`](../../../../../raw/code/wikify-repo/tests/test_callers_callees.py#L15)
- `pytestmark` — [`L17`](../../../../../raw/code/wikify-repo/tests/test_callers_callees.py#L17)

