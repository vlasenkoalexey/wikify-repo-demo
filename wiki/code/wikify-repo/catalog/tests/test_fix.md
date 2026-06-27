---
title: 'Module: tests/test_fix.py'
type: catalog
provenance: extracted
module: tests/test_fix.py
status: fresh
symbol_base: scip-python python wikify-repo 0.0.0 `tests.test_fix`/
symbols:
  _graph: _graph().
  test_rule2_uncited_step_links_named_symbol: test_rule2_uncited_step_links_named_symbol().
  test_rule2_unfixable_when_no_citable_symbol_named: test_rule2_unfixable_when_no_citable_symbol_named().
  test_rule1_dead_anchor_repaired_to_packet_link: test_rule1_dead_anchor_repaired_to_packet_link().
  test_rule3_out_of_subgraph_delinked: test_rule3_out_of_subgraph_delinked().
  test_clean_page_no_edits: test_clean_page_no_edits().
  test_empty_subgraph_page_is_left_untouched: test_empty_subgraph_page_is_left_untouched().
  FOO: FOO.
  _write_catalog: _write_catalog().
  _page: _page().
  CITE_MAP: CITE_MAP.
  BAR: BAR.
---
# Module: [`tests/test_fix.py`](../../../../../raw/code/wikify-repo/tests/test_fix.py)

## Functions
- `_graph()` — [`L25`](../../../../../raw/code/wikify-repo/tests/test_fix.py#L25)
- `_page(wiki_slug: Path, body: str)` — [`L42`](../../../../../raw/code/wikify-repo/tests/test_fix.py#L42)
- `_write_catalog(wiki_slug: Path)` — [`L34`](../../../../../raw/code/wikify-repo/tests/test_fix.py#L34)
- `test_clean_page_no_edits(tmp_path)` — [`L107`](../../../../../raw/code/wikify-repo/tests/test_fix.py#L107)
- `test_empty_subgraph_page_is_left_untouched(tmp_path)` — [`L93`](../../../../../raw/code/wikify-repo/tests/test_fix.py#L93) — A page with no packet/subgraph isn't subgraph-checked by the linter, so --fix — documented in [wikify-lint](../../concepts/wikify-lint.md)
- `test_rule1_dead_anchor_repaired_to_packet_link(tmp_path)` — [`L50`](../../../../../raw/code/wikify-repo/tests/test_fix.py#L50) — documented in [wikify-lint](../../concepts/wikify-lint.md)
- `test_rule2_uncited_step_links_named_symbol(tmp_path)` — [`L74`](../../../../../raw/code/wikify-repo/tests/test_fix.py#L74) — documented in [wikify-lint](../../concepts/wikify-lint.md)
- `test_rule2_unfixable_when_no_citable_symbol_named(tmp_path)` — [`L85`](../../../../../raw/code/wikify-repo/tests/test_fix.py#L85) — documented in [wikify-lint](../../concepts/wikify-lint.md)
- `test_rule3_out_of_subgraph_delinked(tmp_path)` — [`L61`](../../../../../raw/code/wikify-repo/tests/test_fix.py#L61) — documented in [wikify-lint](../../concepts/wikify-lint.md)

## Module values
- `BAR` — [`L21`](../../../../../raw/code/wikify-repo/tests/test_fix.py#L21)
- `CITE_MAP` — [`L22`](../../../../../raw/code/wikify-repo/tests/test_fix.py#L22)
- `FOO` — [`L20`](../../../../../raw/code/wikify-repo/tests/test_fix.py#L20)

