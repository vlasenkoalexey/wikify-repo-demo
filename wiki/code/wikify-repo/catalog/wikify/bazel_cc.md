---
title: 'Module: wikify/bazel_cc.py'
type: catalog
provenance: extracted
module: wikify/bazel_cc.py
status: fresh
symbol_base: scip-python python wikify-repo 0.0.0 `wikify.bazel_cc`/
symbols:
  convert: convert().
  _absolutize: _absolutize().
  generate_compile_db: generate_compile_db().
  _strip_outputs: _strip_outputs().
  _abs: _abs().
  _bazel: _bazel().
  _SEP_PATH_FLAGS: _SEP_PATH_FLAGS.
  SRC_EXT: SRC_EXT.
  _ATTACHED_PREFIXES: _ATTACHED_PREFIXES.
  _DROP_FLAGS: _DROP_FLAGS.
  _DROP_WITH_ARG: _DROP_WITH_ARG.
---
# Module: [`wikify/bazel_cc.py`](../../../../../raw/code/wikify-repo/wikify/bazel_cc.py)

## Functions
- `_abs(p: str, execroot: str)` — [`L44`](../../../../../raw/code/wikify-repo/wikify/bazel_cc.py#L44)
- `_absolutize(args: list[str], execroot: str)` — [`L52`](../../../../../raw/code/wikify-repo/wikify/bazel_cc.py#L52)
- `_bazel(repo_dir: Path, args: list[str], bazel: str)` — [`L104`](../../../../../raw/code/wikify-repo/wikify/bazel_cc.py#L104)
- `_strip_outputs(args: list[str])` — [`L72`](../../../../../raw/code/wikify-repo/wikify/bazel_cc.py#L72)
- `convert(aquery: dict, execroot: str, repo_root: str)` — [`L84`](../../../../../raw/code/wikify-repo/wikify/bazel_cc.py#L84) — Convert parsed `bazel aquery --output=jsonproto` → compile_commands entries.
- `generate_compile_db(repo_dir: str | Path, targets: str, output_path: str | Path, bazel: str = "bazel")` — [`L112`](../../../../../raw/code/wikify-repo/wikify/bazel_cc.py#L112) — Build, aquery, and convert → write a scip-clang-ready compile_commands.json.

## Module values
- `SRC_EXT` — [`L32`](../../../../../raw/code/wikify-repo/wikify/bazel_cc.py#L32)
- `_ATTACHED_PREFIXES` — [`L35`](../../../../../raw/code/wikify-repo/wikify/bazel_cc.py#L35)
- `_DROP_FLAGS` — [`L37`](../../../../../raw/code/wikify-repo/wikify/bazel_cc.py#L37)
- `_DROP_WITH_ARG` — [`L38`](../../../../../raw/code/wikify-repo/wikify/bazel_cc.py#L38)
- `_SEP_PATH_FLAGS` — [`L33`](../../../../../raw/code/wikify-repo/wikify/bazel_cc.py#L33)

