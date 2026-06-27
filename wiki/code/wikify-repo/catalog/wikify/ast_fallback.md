---
title: 'Module: wikify/ast_fallback.py'
type: catalog
provenance: extracted
module: wikify/ast_fallback.py
status: fresh
symbol_base: scip-python python wikify-repo 0.0.0 `wikify.ast_fallback`/
symbols:
  _document: _document().
  _document.walk_class_body: _document().walk_class_body().
  _document.emit: _document().emit().
  synthesize_index: synthesize_index().
  _emit_attr: _emit_attr().
  _Kind: _Kind.
  module_path: module_path().
  _DEFINITION: _DEFINITION.
  _assign_targets: _assign_targets().
  _class_sig: _class_sig().
  _func_sig: _func_sig().
  _simple_name: _simple_name().
  _name_col: _name_col().
---
# Module: [`wikify/ast_fallback.py`](../../../../../raw/code/wikify-repo/wikify/ast_fallback.py)

## Functions
- `_assign_targets(node)` — [`L120`](../../../../../raw/code/wikify-repo/wikify/ast_fallback.py#L120) — Simple ``name =``/``name: T =`` target names (module/class-level vars). — documented in [wikify-ast_fallback](../../concepts/wikify-ast_fallback.md)
- `_class_sig(node: ast.ClassDef)` — [`L143`](../../../../../raw/code/wikify-repo/wikify/ast_fallback.py#L143) — documented in [wikify-ast_fallback](../../concepts/wikify-ast_fallback.md)
- `_document(rel: str, tree: ast.Module, prefix: str)` — [`L67`](../../../../../raw/code/wikify-repo/wikify/ast_fallback.py#L67) — documented in [wikify-ast_fallback](../../concepts/wikify-ast_fallback.md)
- `_emit_attr(doc, base: str, name_path: str, node)` — [`L112`](../../../../../raw/code/wikify-repo/wikify/ast_fallback.py#L112) — documented in [wikify-ast_fallback](../../concepts/wikify-ast_fallback.md)
- `_func_sig(node)` — [`L150`](../../../../../raw/code/wikify-repo/wikify/ast_fallback.py#L150) — documented in [wikify-ast_fallback](../../concepts/wikify-ast_fallback.md)
- `_name_col(node)` — [`L136`](../../../../../raw/code/wikify-repo/wikify/ast_fallback.py#L136) — Column of the name token after the ``class ``/``def ``/``async def `` keyword. — documented in [wikify-ast_fallback](../../concepts/wikify-ast_fallback.md)
- `_simple_name(node)` — [`L132`](../../../../../raw/code/wikify-repo/wikify/ast_fallback.py#L132) — documented in [wikify-ast_fallback](../../concepts/wikify-ast_fallback.md)
- `emit(name_path: str, node, kind, sig: str)` — [`L72`](../../../../../raw/code/wikify-repo/wikify/ast_fallback.py#L72) — documented in [wikify-ast_fallback](../../concepts/wikify-ast_fallback.md)
- `module_path(rel_path: str)` — [`L33`](../../../../../raw/code/wikify-repo/wikify/ast_fallback.py#L33) — ``torch/optim/adam.py`` → ``torch.optim.adam``; ``a/b/__init__.py`` → ``a.b``. — documented in [wikify-ast_fallback](../../concepts/wikify-ast_fallback.md)
- `synthesize_index(repo_dir: str | Path, rel_paths: list[str], project_name: str, project_version: str = "0.0.0")` — [`L42`](../../../../../raw/code/wikify-repo/wikify/ast_fallback.py#L42) — Build a SCIP ``Index`` for ``rel_paths`` (repo-relative) via AST parsing. — documented in [wikify-ast_fallback](../../concepts/wikify-ast_fallback.md)
- `walk_class_body(cls: ast.ClassDef, scope: str)` — [`L87`](../../../../../raw/code/wikify-repo/wikify/ast_fallback.py#L87) — documented in [wikify-ast_fallback](../../concepts/wikify-ast_fallback.md)

## Module values
- `_DEFINITION` — [`L29`](../../../../../raw/code/wikify-repo/wikify/ast_fallback.py#L29) — documented in [wikify-ast_fallback](../../concepts/wikify-ast_fallback.md)
- `_Kind` — [`L30`](../../../../../raw/code/wikify-repo/wikify/ast_fallback.py#L30) — documented in [wikify-ast_fallback](../../concepts/wikify-ast_fallback.md)

