---
title: 'Module: tests/test_coverage.py'
type: catalog
provenance: extracted
module: tests/test_coverage.py
status: fresh
symbol_base: scip-python python wikify-repo 0.0.0 `tests.test_coverage`/
symbols:
  _graph: _graph().
  test_docstring_extracted_into_catalog: test_docstring_extracted_into_catalog().
  test_member_detail_promotes_documented_and_folds_plumbing: test_member_detail_promotes_documented_and_folds_plumbing().
  test_report_classifies_covered_vs_catalog: test_report_classifies_covered_vs_catalog().
  test_used_by_excludes_tests_and_ranks_by_importance: test_used_by_excludes_tests_and_ranks_by_importance().
  PKG: PKG.
  test_catalog_frontmatter_factors_out_moniker_prefix: test_catalog_frontmatter_factors_out_moniker_prefix().
  test_catalog_cross_links_carry_symbol_anchors: test_catalog_cross_links_carry_symbol_anchors().
  test_docstring_strips_signature_fence: test_docstring_strips_signature_fence().
  M_CLASS: M_CLASS.
  test_documentable_excludes_external: test_documentable_excludes_external().
  test_catalog_def_lines_link_to_source_when_base_given: test_catalog_def_lines_link_to_source_when_base_given().
  test_classes_enumerated: test_classes_enumerated().
  test_catalog_drops_boilerplate_paragraph: test_catalog_drops_boilerplate_paragraph().
  test_catalog_no_source_links_without_base: test_catalog_no_source_links_without_base().
  M_METHOD: M_METHOD.
  M_ATTN: M_ATTN.
  M_FUNC: M_FUNC.
  test_catalog_pages_mirror_source_tree: test_catalog_pages_mirror_source_tree().
  test_emit_uses_relative_source_path_never_absolute: test_emit_uses_relative_source_path_never_absolute().
  _mark_covered: _mark_covered().
---
# Module: [`tests/test_coverage.py`](../../../../../raw/code/wikify-repo/tests/test_coverage.py)

## Functions
- `_graph()` — [`L20`](../../../../../raw/code/wikify-repo/tests/test_coverage.py#L20)
- `_mark_covered(wiki_slug: Path, module: str, anchor: str)` — [`L37`](../../../../../raw/code/wikify-repo/tests/test_coverage.py#L37) — Write a concept page citing a catalog anchor so that symbol is covered.
- `test_catalog_cross_links_carry_symbol_anchors()` — [`L236`](../../../../../raw/code/wikify-repo/tests/test_coverage.py#L236) — `uses`/`used by` links point at the symbol anchor, not the page top — so
- `test_catalog_def_lines_link_to_source_when_base_given()` — [`L201`](../../../../../raw/code/wikify-repo/tests/test_coverage.py#L201)
- `test_catalog_drops_boilerplate_paragraph()` — [`L196`](../../../../../raw/code/wikify-repo/tests/test_coverage.py#L196)
- `test_catalog_frontmatter_factors_out_moniker_prefix(tmp_path)` — [`L93`](../../../../../raw/code/wikify-repo/tests/test_coverage.py#L93) — The repeated scheme/project/version/namespace prefix is stored once as
- `test_catalog_no_source_links_without_base()` — [`L231`](../../../../../raw/code/wikify-repo/tests/test_coverage.py#L231)
- `test_catalog_pages_mirror_source_tree(tmp_path)` — [`L77`](../../../../../raw/code/wikify-repo/tests/test_coverage.py#L77)
- `test_classes_enumerated()` — [`L54`](../../../../../raw/code/wikify-repo/tests/test_coverage.py#L54)
- `test_docstring_extracted_into_catalog()` — [`L137`](../../../../../raw/code/wikify-repo/tests/test_coverage.py#L137) — The author's docstring (parsed from scip `documentation`) reaches the page — — documented in [wikify-coverage](../../concepts/wikify-coverage.md)
- `test_docstring_strips_signature_fence()` — [`L247`](../../../../../raw/code/wikify-repo/tests/test_coverage.py#L247)
- `test_documentable_excludes_external()` — [`L47`](../../../../../raw/code/wikify-repo/tests/test_coverage.py#L47) — documented in [wikify-coverage](../../concepts/wikify-coverage.md)
- `test_emit_uses_relative_source_path_never_absolute(tmp_path)` — [`L210`](../../../../../raw/code/wikify-repo/tests/test_coverage.py#L210) — Source links from a local repo are RELATIVE to the catalog page — never an
- `test_member_detail_promotes_documented_and_folds_plumbing()` — [`L161`](../../../../../raw/code/wikify-repo/tests/test_coverage.py#L161) — A: public/documented members get full detail (name(params) — line — doc); — documented in [wikify-coverage](../../concepts/wikify-coverage.md)
- `test_report_classifies_covered_vs_catalog(tmp_path)` — [`L60`](../../../../../raw/code/wikify-repo/tests/test_coverage.py#L60) — documented in [wikify-coverage](../../concepts/wikify-coverage.md)
- `test_used_by_excludes_tests_and_ranks_by_importance()` — [`L113`](../../../../../raw/code/wikify-repo/tests/test_coverage.py#L113) — documented in [wikify-coverage](../../concepts/wikify-coverage.md)

## Module values
- `M_ATTN` — [`L16`](../../../../../raw/code/wikify-repo/tests/test_coverage.py#L16)
- `M_CLASS` — [`L14`](../../../../../raw/code/wikify-repo/tests/test_coverage.py#L14)
- `M_FUNC` — [`L17`](../../../../../raw/code/wikify-repo/tests/test_coverage.py#L17)
- `M_METHOD` — [`L15`](../../../../../raw/code/wikify-repo/tests/test_coverage.py#L15)
- `PKG` — [`L13`](../../../../../raw/code/wikify-repo/tests/test_coverage.py#L13)

