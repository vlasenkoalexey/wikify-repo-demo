---
title: 'Module: wikify/slug.py'
type: catalog
provenance: extracted
module: wikify/slug.py
status: fresh
symbol_base: scip-python python wikify-repo 0.0.0 `wikify.slug`/
symbols:
  slug_for: slug_for().
  SlugAllocator.allocate: SlugAllocator#allocate().
  _sanitize: _sanitize().
  SlugAllocator: SlugAllocator#
  SlugAllocator._by_slug: SlugAllocator#_by_slug.
  _hash8: _hash8().
  SlugAllocator._by_moniker: SlugAllocator#_by_moniker.
  _UNSAFE: _UNSAFE.
  _DASHES: _DASHES.
  SlugAllocator.__init__: SlugAllocator#__init__().
---
# Module: [`wikify/slug.py`](../../../../../raw/code/wikify-repo/wikify/slug.py)

## Classes
### `SlugAllocator`
- def: [`wikify/slug.py:54`](../../../../../raw/code/wikify-repo/wikify/slug.py#L54)
- doc: Hands out collision-free slugs, stable across a run.
- signature: `class SlugAllocator:`
- members:
  - `allocate(self, moniker: str)` — [`L66`](../../../../../raw/code/wikify-repo/wikify/slug.py#L66)
- protocol/private: `__init__`[`L62`](../../../../../raw/code/wikify-repo/wikify/slug.py#L62), `_by_moniker`[`L63`](../../../../../raw/code/wikify-repo/wikify/slug.py#L63), `_by_slug`[`L64`](../../../../../raw/code/wikify-repo/wikify/slug.py#L64)
- uses (calls/refs, reference-scoped): [`slug_for`](slug.md#slug_for), [`_sanitize`](slug.md#_sanitize), [`_hash8`](slug.md#_hash8)
- used by: (3 test-only callers)

## Functions
- `_hash8(moniker: str)` — [`L50`](../../../../../raw/code/wikify-repo/wikify/slug.py#L50)
- `_sanitize(text: str)` — [`L29`](../../../../../raw/code/wikify-repo/wikify/slug.py#L29) — Replace unsafe chars with ``-``, collapse repeats, strip ends.
- `slug_for(moniker: str)` — [`L36`](../../../../../raw/code/wikify-repo/wikify/slug.py#L36) — Deterministic base filename stem for ``moniker`` (no ``.md``). — documented in [wikify-monikers](../../concepts/wikify-monikers.md)

## Module values
- `_DASHES` — [`L26`](../../../../../raw/code/wikify-repo/wikify/slug.py#L26)
- `_UNSAFE` — [`L25`](../../../../../raw/code/wikify-repo/wikify/slug.py#L25)

