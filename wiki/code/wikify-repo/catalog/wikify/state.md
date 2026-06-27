---
title: 'Module: wikify/state.py'
type: catalog
provenance: extracted
module: wikify/state.py
status: fresh
symbol_base: scip-python python wikify-repo 0.0.0 `wikify.state`/
symbols:
  _empty_state: _empty_state().
  load_state: load_state().
  set_symbols: set_symbols().
  state_path: state_path().
  set_ref: set_ref().
  record_page: record_page().
  save_state: save_state().
  page_cited: page_cited().
  has_page: has_page().
---
# Module: [`wikify/state.py`](../../../../../raw/code/wikify-repo/wikify/state.py)

## Functions
- `_empty_state()` — [`L27`](../../../../../raw/code/wikify-repo/wikify/state.py#L27) — A fresh, never-built state with all top-level keys present. — documented in [wikify-state](../../concepts/wikify-state.md)
- `has_page(state: dict, concept: str)` — [`L85`](../../../../../raw/code/wikify-repo/wikify/state.py#L85) — Whether a page has been recorded for ``concept``.
- `load_state(path: str | Path)` — [`L32`](../../../../../raw/code/wikify-repo/wikify/state.py#L32) — Load the state dict, or a fresh empty state if the file does not exist. — documented in [wikify-state](../../concepts/wikify-state.md)
- `page_cited(state: dict, concept: str)` — [`L80`](../../../../../raw/code/wikify-repo/wikify/state.py#L80) — Return the cited monikers for ``concept`` (empty list if no such page).
- `record_page(state: dict, concept: str, cited: list[str], built_ref: str)` — [`L72`](../../../../../raw/code/wikify-repo/wikify/state.py#L72) — Record a built page: its (deduped, sorted) cited monikers and build ref.
- `save_state(path: str | Path, state: dict)` — [`L53`](../../../../../raw/code/wikify-repo/wikify/state.py#L53) — Write ``state`` as pretty-printed JSON (indent=2, sorted keys), making parents.
- `set_ref(state: dict, ref: str)` — [`L67`](../../../../../raw/code/wikify-repo/wikify/state.py#L67) — Record the pinned commit the state corresponds to.
- `set_symbols(state: dict, symbols: dict[str, str])` — [`L62`](../../../../../raw/code/wikify-repo/wikify/state.py#L62) — Replace the moniker → body-sha map. — documented in [wikify-state](../../concepts/wikify-state.md)
- `state_path(cache_dir: str | Path, slug: str)` — [`L22`](../../../../../raw/code/wikify-repo/wikify/state.py#L22) — Return the on-disk path of the state file: ``<cache_dir>/state/<slug>.json``. — documented in [wikify-state](../../concepts/wikify-state.md)

