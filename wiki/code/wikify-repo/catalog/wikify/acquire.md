---
title: 'Module: wikify/acquire.py'
type: catalog
provenance: extracted
module: wikify/acquire.py
status: fresh
symbol_base: scip-python python wikify-repo 0.0.0 `wikify.acquire`/
symbols:
  acquire: acquire().
  Acquired.repo_dir: Acquired#repo_dir.
  Acquired.commit: Acquired#commit.
  _git: _git().
  _toplevel: _toplevel().
  commit_of: commit_of().
  checkout: checkout().
  Acquired: Acquired#
  Acquired.slug: Acquired#slug.
---
# Module: [`wikify/acquire.py`](../../../../../raw/code/wikify-repo/wikify/acquire.py)

## Classes
### `Acquired`
- def: [`wikify/acquire.py:16`](../../../../../raw/code/wikify-repo/wikify/acquire.py#L16)
- signature: `class Acquired:`
- members:
  - `commit` — [`L19`](../../../../../raw/code/wikify-repo/wikify/acquire.py#L19)
  - `repo_dir` — [`L18`](../../../../../raw/code/wikify-repo/wikify/acquire.py#L18) — documented in [wikify-cli](../../concepts/wikify-cli.md)
  - `slug` — [`L17`](../../../../../raw/code/wikify-repo/wikify/acquire.py#L17)
- used by: [`prepare`](cli.md#prepare), [`finalize`](cli.md#finalize), [`plan`](cli.md#plan), [`acquire`](acquire.md#acquire)  (1 test-only)

## Functions
- `_git(args: list[str], cwd: str | Path)` — [`L22`](../../../../../raw/code/wikify-repo/wikify/acquire.py#L22)
- `_toplevel(path: str | Path)` — [`L39`](../../../../../raw/code/wikify-repo/wikify/acquire.py#L39) — The git work-tree root containing ``path``, or None if not in a repo.
- `acquire(source: str, slug: str, raw_dir: str | Path, ref: str | None = None, mode: str | None = None)` — [`L47`](../../../../../raw/code/wikify-repo/wikify/acquire.py#L47) — Resolve ``source`` (local path or git URL) to a pinned source tree. — documented in [wikify-cli](../../concepts/wikify-cli.md)
- `checkout(repo_dir: str | Path, ref: str)` — [`L35`](../../../../../raw/code/wikify-repo/wikify/acquire.py#L35)
- `commit_of(repo_dir: str | Path)` — [`L31`](../../../../../raw/code/wikify-repo/wikify/acquire.py#L31)

