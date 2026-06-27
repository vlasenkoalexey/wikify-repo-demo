---
title: 'Module: tests/test_lint.py'
type: catalog
provenance: extracted
module: tests/test_lint.py
status: fresh
symbol_base: scip-python python wikify-repo 0.0.0 `tests.test_lint`/
symbols:
  _graph: _graph().
  test_rule1_anchor_not_in_catalog: test_rule1_anchor_not_in_catalog().
  test_rule3_out_of_subgraph: test_rule3_out_of_subgraph().
  test_rule1_resolves_to_unknown_moniker: test_rule1_resolves_to_unknown_moniker().
  test_rule2_uncited_mechanism_item: test_rule2_uncited_mechanism_item().
  test_clean_page_passes: test_clean_page_passes().
  test_rule2_inferred_block_is_exempt: test_rule2_inferred_block_is_exempt().
  test_page_citations_resolves_via_catalog: test_page_citations_resolves_via_catalog().
  MONIKER: MONIKER.
  _write_catalog: _write_catalog().
  _page: _page().
  CLEAN: CLEAN.
  OTHER: OTHER.
---
# Module: [`tests/test_lint.py`](../../../../../raw/code/wikify-repo/tests/test_lint.py)

## Functions
- `_graph()` — [`L19`](../../../../../raw/code/wikify-repo/tests/test_lint.py#L19)
- `_page(wiki_slug: Path, body: str)` — [`L36`](../../../../../raw/code/wikify-repo/tests/test_lint.py#L36)
- `_write_catalog(wiki_slug: Path, anchors: dict[str, str])` — [`L28`](../../../../../raw/code/wikify-repo/tests/test_lint.py#L28) — Write a catalog page whose frontmatter `symbols` map resolves anchors.
- `test_clean_page_passes(tmp_path)` — [`L54`](../../../../../raw/code/wikify-repo/tests/test_lint.py#L54) — documented in [wikify-lint](../../concepts/wikify-lint.md)
- `test_page_citations_resolves_via_catalog(tmp_path)` — [`L94`](../../../../../raw/code/wikify-repo/tests/test_lint.py#L94)
- `test_rule1_anchor_not_in_catalog(tmp_path)` — [`L60`](../../../../../raw/code/wikify-repo/tests/test_lint.py#L60) — documented in [wikify-lint](../../concepts/wikify-lint.md)
- `test_rule1_resolves_to_unknown_moniker(tmp_path)` — [`L67`](../../../../../raw/code/wikify-repo/tests/test_lint.py#L67) — documented in [wikify-lint](../../concepts/wikify-lint.md)
- `test_rule2_inferred_block_is_exempt(tmp_path)` — [`L81`](../../../../../raw/code/wikify-repo/tests/test_lint.py#L81) — documented in [wikify-lint](../../concepts/wikify-lint.md)
- `test_rule2_uncited_mechanism_item(tmp_path)` — [`L74`](../../../../../raw/code/wikify-repo/tests/test_lint.py#L74) — documented in [wikify-lint](../../concepts/wikify-lint.md)
- `test_rule3_out_of_subgraph(tmp_path)` — [`L87`](../../../../../raw/code/wikify-repo/tests/test_lint.py#L87) — documented in [wikify-lint](../../concepts/wikify-lint.md)

## Module values
- `CLEAN` — [`L45`](../../../../../raw/code/wikify-repo/tests/test_lint.py#L45)
- `MONIKER` — [`L15`](../../../../../raw/code/wikify-repo/tests/test_lint.py#L15)
- `OTHER` — [`L16`](../../../../../raw/code/wikify-repo/tests/test_lint.py#L16)

