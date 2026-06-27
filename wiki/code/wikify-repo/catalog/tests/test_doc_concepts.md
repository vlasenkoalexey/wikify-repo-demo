---
title: 'Module: tests/test_doc_concepts.py'
type: catalog
provenance: extracted
module: tests/test_doc_concepts.py
status: fresh
symbol_base: scip-python python wikify-repo 0.0.0 `tests.test_doc_concepts`/
symbols:
  _graph: _graph().
  test_doc_concept_lint_fails_on_dead_or_unknown_citation: test_doc_concept_lint_fails_on_dead_or_unknown_citation().
  test_doc_concept_lint_passes_on_resolving_citation: test_doc_concept_lint_passes_on_resolving_citation().
  test_doc_concept_lint_ignores_subgraph_and_uncited: test_doc_concept_lint_ignores_subgraph_and_uncited().
  test_no_doc_concepts_dir_is_clean: test_no_doc_concepts_dir_is_clean().
  _catalog: _catalog().
  _doc_concept: _doc_concept().
  test_find_docs_globs_and_skips_noise: test_find_docs_globs_and_skips_noise().
  MON: MON.
---
# Module: [`tests/test_doc_concepts.py`](../../../../../raw/code/wikify-repo/tests/test_doc_concepts.py)

## Functions
- `_catalog(wiki_slug: Path)` — [`L28`](../../../../../raw/code/wikify-repo/tests/test_doc_concepts.py#L28)
- `_doc_concept(wiki_slug: Path, body: str)` — [`L35`](../../../../../raw/code/wikify-repo/tests/test_doc_concepts.py#L35)
- `_graph()` — [`L21`](../../../../../raw/code/wikify-repo/tests/test_doc_concepts.py#L21)
- `test_doc_concept_lint_fails_on_dead_or_unknown_citation(tmp_path)` — [`L59`](../../../../../raw/code/wikify-repo/tests/test_doc_concepts.py#L59) — documented in [wikify-lint](../../concepts/wikify-lint.md)
- `test_doc_concept_lint_ignores_subgraph_and_uncited(tmp_path)` — [`L67`](../../../../../raw/code/wikify-repo/tests/test_doc_concepts.py#L67) — A doc-concept may state prose freely and is not bound to any packet subgraph. — documented in [wikify-lint](../../concepts/wikify-lint.md)
- `test_doc_concept_lint_passes_on_resolving_citation(tmp_path)` — [`L52`](../../../../../raw/code/wikify-repo/tests/test_doc_concepts.py#L52) — documented in [wikify-lint](../../concepts/wikify-lint.md)
- `test_find_docs_globs_and_skips_noise(tmp_path)` — [`L41`](../../../../../raw/code/wikify-repo/tests/test_doc_concepts.py#L41)
- `test_no_doc_concepts_dir_is_clean(tmp_path)` — [`L76`](../../../../../raw/code/wikify-repo/tests/test_doc_concepts.py#L76) — documented in [wikify-lint](../../concepts/wikify-lint.md)

## Module values
- `MON` — [`L18`](../../../../../raw/code/wikify-repo/tests/test_doc_concepts.py#L18)

