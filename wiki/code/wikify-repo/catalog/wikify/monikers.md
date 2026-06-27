---
title: 'Module: wikify/monikers.py'
type: catalog
provenance: extracted
module: wikify/monikers.py
status: fresh
symbol_base: scip-python python wikify-repo 0.0.0 `wikify.monikers`/
symbols:
  parse_symbol: parse_symbol().
  ParsedSymbol.descriptors: ParsedSymbol#descriptors.
  _parse_descriptors: _parse_descriptors().
  ParsedSymbol.terminal: ParsedSymbol#terminal().
  _parse_name: _parse_name().
  ParsedSymbol: ParsedSymbol#
  ParsedSymbol.is_local: ParsedSymbol#is_local.
  ParsedSymbol.local_id: ParsedSymbol#local_id.
  ParsedSymbol.scheme: ParsedSymbol#scheme.
  _SUFFIX: _SUFFIX.
  ParsedSymbol.manager: ParsedSymbol#manager.
  ParsedSymbol.package: ParsedSymbol#package.
  _DELIMS: _DELIMS.
  ParsedSymbol.version: ParsedSymbol#version.
---
# Module: [`wikify/monikers.py`](../../../../../raw/code/wikify-repo/wikify/monikers.py)

## Classes
### `ParsedSymbol`
- def: [`wikify/monikers.py:27`](../../../../../raw/code/wikify-repo/wikify/monikers.py#L27) — documented in [wikify-monikers](../../concepts/wikify-monikers.md)
- signature: `class ParsedSymbol:`
- members:
  - `terminal(self)` — [`L37`](../../../../../raw/code/wikify-repo/wikify/monikers.py#L37) — (name, suffix) of the last descriptor, or ('', '') if none. — documented in [wikify-monikers](../../concepts/wikify-monikers.md)
  - `descriptors` — [`L34`](../../../../../raw/code/wikify-repo/wikify/monikers.py#L34) — documented in [wikify-coverage](../../concepts/wikify-coverage.md)
  - `is_local` — [`L28`](../../../../../raw/code/wikify-repo/wikify/monikers.py#L28) — documented in [wikify-monikers](../../concepts/wikify-monikers.md)
  - `local_id` — [`L29`](../../../../../raw/code/wikify-repo/wikify/monikers.py#L29) — documented in [wikify-monikers](../../concepts/wikify-monikers.md)
  - `manager` — [`L31`](../../../../../raw/code/wikify-repo/wikify/monikers.py#L31) — documented in [wikify-monikers](../../concepts/wikify-monikers.md)
  - `package` — [`L32`](../../../../../raw/code/wikify-repo/wikify/monikers.py#L32) — documented in [wikify-monikers](../../concepts/wikify-monikers.md)
  - `scheme` — [`L30`](../../../../../raw/code/wikify-repo/wikify/monikers.py#L30) — documented in [wikify-monikers](../../concepts/wikify-monikers.md)
  - `version` — [`L33`](../../../../../raw/code/wikify-repo/wikify/monikers.py#L33) — documented in [wikify-monikers](../../concepts/wikify-monikers.md)
- used by: [`build_graph`](scip_index.md#build_graph), [`slug_for`](slug.md#slug_for), [`parse_symbol`](monikers.md#parse_symbol), [`_synth_symbol`](scip_index.md#_synth_symbol), [`qualified_name`](coverage.md#qualified_name), [`_rel_names`](coverage.md#_rel_names), [`_owner_class`](coverage.md#_owner_class), [`_path_from_moniker`](scip_index.md#_path_from_moniker)

## Functions
- `_parse_descriptors(s: str)` — [`L82`](../../../../../raw/code/wikify-repo/wikify/monikers.py#L82) — documented in [wikify-monikers](../../concepts/wikify-monikers.md)
- `_parse_name(s: str, i: int)` — [`L59`](../../../../../raw/code/wikify-repo/wikify/monikers.py#L59) — Read a (possibly backtick-escaped) descriptor name starting at ``i``. — documented in [wikify-monikers](../../concepts/wikify-monikers.md)
- `parse_symbol(symbol: str)` — [`L42`](../../../../../raw/code/wikify-repo/wikify/monikers.py#L42) — documented in [wikify-monikers](../../concepts/wikify-monikers.md)

## Module values
- `_DELIMS` — [`L23`](../../../../../raw/code/wikify-repo/wikify/monikers.py#L23) — documented in [wikify-monikers](../../concepts/wikify-monikers.md)
- `_SUFFIX` — [`L22`](../../../../../raw/code/wikify-repo/wikify/monikers.py#L22) — documented in [wikify-monikers](../../concepts/wikify-monikers.md)

