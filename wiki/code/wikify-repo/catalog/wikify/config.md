---
title: 'Module: wikify/config.py'
type: catalog
provenance: extracted
module: wikify/config.py
status: fresh
symbol_base: scip-python python wikify-repo 0.0.0 `wikify.config`/
symbols:
  load_config: load_config().
  _parse_concept: _parse_concept().
  Concept.slug: Concept#slug.
  RepoConfig.concepts: RepoConfig#concepts.
  Concept: Concept#
  Concept.seeds: Concept#seeds.
  RepoConfig: RepoConfig#
  RepoConfig.ref: RepoConfig#ref.
  RepoConfig.acquire: RepoConfig#acquire.
  _parse_seeds: _parse_seeds().
  _parse_concepts: _parse_concepts().
  validate_config: validate_config().
  Concept.auto: Concept#auto.
  RepoConfig.bazel_targets: RepoConfig#bazel_targets.
  RepoConfig.languages: RepoConfig#languages.
  RepoConfig.wiki_subdir: RepoConfig#wiki_subdir.
  RepoConfig.tests: RepoConfig#tests.
  RepoConfig.docs: RepoConfig#docs.
  _as_list: _as_list().
  _SEEDS_RE: _SEEDS_RE.
  RepoConfig.slug: RepoConfig#slug.
  RepoConfig.build: RepoConfig#build.
  RepoConfig.compile_commands: RepoConfig#compile_commands.
  RepoConfig.index_shards: RepoConfig#index_shards.
  _ALLOWED_KEYS: _ALLOWED_KEYS.
  _DASH: _DASH.
  _HTML_COMMENT_RE: _HTML_COMMENT_RE.
  _BACKTICK_TOKEN_RE: _BACKTICK_TOKEN_RE.
  Concept.note: Concept#note.
  RepoConfig.repo: RepoConfig#repo.
  RepoConfig.source_url: RepoConfig#source_url.
  _CONCEPT_RE: _CONCEPT_RE.
  _AUTO_RE: _AUTO_RE.
  _split_frontmatter: _split_frontmatter().
---
# Module: [`wikify/config.py`](../../../../../raw/code/wikify-repo/wikify/config.py)

## Classes
### `Concept`
- def: [`wikify/config.py:50`](../../../../../raw/code/wikify-repo/wikify/config.py#L50) — documented in [wikify-cli](../../concepts/wikify-cli.md)
- doc: One architectural concept from the `## Concepts` list.
- signature: `class Concept:`
- members:
  - `auto` — [`L60`](../../../../../raw/code/wikify-repo/wikify/config.py#L60) — documented in [wikify-config](../../concepts/wikify-config.md)
  - `note` — [`L61`](../../../../../raw/code/wikify-repo/wikify/config.py#L61) — documented in [wikify-config](../../concepts/wikify-config.md)
  - `seeds` — [`L59`](../../../../../raw/code/wikify-repo/wikify/config.py#L59) — documented in [wikify-config](../../concepts/wikify-config.md)
  - `slug` — [`L58`](../../../../../raw/code/wikify-repo/wikify/config.py#L58) — documented in [wikify-cli](../../concepts/wikify-cli.md)
- used by: [`prepare`](cli.md#prepare), [`build_packet`](packet.md#build_packet), [`compute_plan`](diff.md#compute_plan), [`_parse_concept`](config.md#_parse_concept), [`concepts`](config.md#RepoConfig.concepts), [`_parse_concepts`](config.md#_parse_concepts)  (8 test-only)

### `RepoConfig`
- def: [`wikify/config.py:65`](../../../../../raw/code/wikify-repo/wikify/config.py#L65) — documented in [wikify-config](../../concepts/wikify-config.md)
- doc: Parsed `config/<slug>.md` — an authored ingest input, not a product.
- signature: `class RepoConfig:`
- members:
  - `acquire` — [`L78`](../../../../../raw/code/wikify-repo/wikify/config.py#L78) — documented in [wikify-config](../../concepts/wikify-config.md)
  - `bazel_targets` — [`L88`](../../../../../raw/code/wikify-repo/wikify/config.py#L88) — documented in [wikify-config](../../concepts/wikify-config.md)
  - `build` — [`L70`](../../../../../raw/code/wikify-repo/wikify/config.py#L70) — documented in [wikify-config](../../concepts/wikify-config.md)
  - `compile_commands` — [`L83`](../../../../../raw/code/wikify-repo/wikify/config.py#L83) — documented in [wikify-config](../../concepts/wikify-config.md)
  - `concepts` — [`L101`](../../../../../raw/code/wikify-repo/wikify/config.py#L101) — documented in [wikify-cli](../../concepts/wikify-cli.md)
  - `docs` — [`L100`](../../../../../raw/code/wikify-repo/wikify/config.py#L100) — documented in [wikify-config](../../concepts/wikify-config.md)
  - `index_shards` — [`L98`](../../../../../raw/code/wikify-repo/wikify/config.py#L98) — documented in [wikify-config](../../concepts/wikify-config.md)
  - `languages` — [`L69`](../../../../../raw/code/wikify-repo/wikify/config.py#L69) — documented in [wikify-config](../../concepts/wikify-config.md)
  - `ref` — [`L71`](../../../../../raw/code/wikify-repo/wikify/config.py#L71) — documented in [wikify-config](../../concepts/wikify-config.md)
  - `repo` — [`L72`](../../../../../raw/code/wikify-repo/wikify/config.py#L72) — documented in [wikify-config](../../concepts/wikify-config.md)
  - `slug` — [`L68`](../../../../../raw/code/wikify-repo/wikify/config.py#L68) — documented in [wikify-config](../../concepts/wikify-config.md)
  - `source_url` — [`L93`](../../../../../raw/code/wikify-repo/wikify/config.py#L93) — documented in [wikify-config](../../concepts/wikify-config.md)
  - `tests` — [`L99`](../../../../../raw/code/wikify-repo/wikify/config.py#L99) — documented in [wikify-config](../../concepts/wikify-config.md)
  - `wiki_subdir` — [`L82`](../../../../../raw/code/wikify-repo/wikify/config.py#L82) — documented in [wikify-config](../../concepts/wikify-config.md)
- uses (calls/refs, reference-scoped): [`Concept`](config.md#Concept)
- used by: [`prepare`](cli.md#prepare), [`finalize`](cli.md#finalize), [`load_config`](config.md#load_config), [`plan`](cli.md#plan), [`compute_plan`](diff.md#compute_plan), [`_load`](cli.md#_load), [`_source`](cli.md#_source), [`validate_config`](config.md#validate_config)  (11 test-only)

## Functions
- `_as_list(value: object)` — [`L115`](../../../../../raw/code/wikify-repo/wikify/config.py#L115) — Coerce an absent/scalar/list frontmatter value to a list of str. — documented in [wikify-config](../../concepts/wikify-config.md)
- `_parse_concept(line: str)` — [`L139`](../../../../../raw/code/wikify-repo/wikify/config.py#L139) — Parse one ``- ...`` concept list item into a ``Concept``. — documented in [wikify-config](../../concepts/wikify-config.md)
- `_parse_concepts(body: str)` — [`L172`](../../../../../raw/code/wikify-repo/wikify/config.py#L172) — Extract concepts from the ``## Concepts`` section of the body. — documented in [wikify-config](../../concepts/wikify-config.md)
- `_parse_seeds(payload: str)` — [`L124`](../../../../../raw/code/wikify-repo/wikify/config.py#L124) — Parse a ``seeds:`` payload → ``(seeds, auto, note)``. — documented in [wikify-config](../../concepts/wikify-config.md)
- `_split_frontmatter(text: str)` — [`L104`](../../../../../raw/code/wikify-repo/wikify/config.py#L104) — Return ``(frontmatter_yaml, body)`` from leading ``---`` fences. — documented in [wikify-config](../../concepts/wikify-config.md)
- `load_config(path: str | Path)` — [`L199`](../../../../../raw/code/wikify-repo/wikify/config.py#L199) — Parse and validate ``config/<slug>.md`` into a ``RepoConfig``. — documented in [wikify-cli](../../concepts/wikify-cli.md)
- `validate_config(cfg: RepoConfig)` — [`L193`](../../../../../raw/code/wikify-repo/wikify/config.py#L193) — Raise ``ValueError`` if the parsed config violates the schema. — documented in [wikify-config](../../concepts/wikify-config.md)

## Module values
- `_ALLOWED_KEYS` — [`L24`](../../../../../raw/code/wikify-repo/wikify/config.py#L24) — documented in [wikify-config](../../concepts/wikify-config.md)
- `_AUTO_RE` — [`L46`](../../../../../raw/code/wikify-repo/wikify/config.py#L46) — documented in [wikify-config](../../concepts/wikify-config.md)
- `_BACKTICK_TOKEN_RE` — [`L45`](../../../../../raw/code/wikify-repo/wikify/config.py#L45) — documented in [wikify-config](../../concepts/wikify-config.md)
- `_CONCEPT_RE` — [`L32`](../../../../../raw/code/wikify-repo/wikify/config.py#L32) — documented in [wikify-config](../../concepts/wikify-config.md)
- `_DASH` — [`L29`](../../../../../raw/code/wikify-repo/wikify/config.py#L29) — documented in [wikify-config](../../concepts/wikify-config.md)
- `_HTML_COMMENT_RE` — [`L44`](../../../../../raw/code/wikify-repo/wikify/config.py#L44) — documented in [wikify-config](../../concepts/wikify-config.md)
- `_SEEDS_RE` — [`L39`](../../../../../raw/code/wikify-repo/wikify/config.py#L39) — documented in [wikify-config](../../concepts/wikify-config.md)

