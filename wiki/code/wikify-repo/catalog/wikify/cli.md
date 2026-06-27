---
title: 'Module: wikify/cli.py'
type: catalog
provenance: extracted
module: wikify/cli.py
status: fresh
symbol_base: scip-python python wikify-repo 0.0.0 `wikify.cli`/
symbols:
  prepare: prepare().
  finalize: finalize().
  plan: plan().
  lint_cmd: lint_cmd().
  coverage: coverage().
  Paths.wiki_slug: Paths#wiki_slug.
  _load: _load().
  verify: verify().
  _graph: _graph().
  Paths.scip: Paths#scip.
  Paths.cache: Paths#cache.
  Paths.state: Paths#state.
  Paths.wiki_base: Paths#wiki_base.
  _source: _source().
  Paths.scip_cpp: Paths#scip_cpp.
  app: app.
  Paths: Paths#
  Paths.wiki: Paths#wiki.
  Paths.set_wiki_subdir: Paths#set_wiki_subdir().
  Paths.wiki_subdir: Paths#wiki_subdir.
  Paths.raw: Paths#raw.
  Paths.config: Paths#config.
  _today: _today().
  _find_docs: _find_docs().
  Paths.slug: Paths#slug.
  _scip_clang_bin: _scip_clang_bin().
  _expand_shards: _expand_shards().
  Paths.__init__: Paths#__init__().
  Paths.root: Paths#root.
---
# Module: [`wikify/cli.py`](../../../../../raw/code/wikify-repo/wikify/cli.py)

## Classes
### `Paths`
- def: [`wikify/cli.py:43`](../../../../../raw/code/wikify-repo/wikify/cli.py#L43)
- signature: `class Paths:`
- members:
  - `set_wiki_subdir(self, subdir: str | None)` — [`L56`](../../../../../raw/code/wikify-repo/wikify/cli.py#L56) — Place this repo's wiki at ``wiki/<subdir>/<slug>`` (subdir="" → ``wiki/<slug>``).
  - `cache` — [`L47`](../../../../../raw/code/wikify-repo/wikify/cli.py#L47) — documented in [wikify-cli](../../concepts/wikify-cli.md)
  - `config` — [`L49`](../../../../../raw/code/wikify-repo/wikify/cli.py#L49)
  - `raw` — [`L48`](../../../../../raw/code/wikify-repo/wikify/cli.py#L48)
  - `root` — [`L45`](../../../../../raw/code/wikify-repo/wikify/cli.py#L45)
  - `scip` — [`L50`](../../../../../raw/code/wikify-repo/wikify/cli.py#L50) — documented in [wikify-cli](../../concepts/wikify-cli.md)
  - `scip_cpp` — [`L51`](../../../../../raw/code/wikify-repo/wikify/cli.py#L51)
  - `slug` — [`L46`](../../../../../raw/code/wikify-repo/wikify/cli.py#L46)
  - `state` — [`L52`](../../../../../raw/code/wikify-repo/wikify/cli.py#L52) — documented in [wikify-cli](../../concepts/wikify-cli.md)
  - `wiki` — [`L53`](../../../../../raw/code/wikify-repo/wikify/cli.py#L53)
  - `wiki_base` — [`L59`](../../../../../raw/code/wikify-repo/wikify/cli.py#L59)
  - `wiki_slug` — [`L60`](../../../../../raw/code/wikify-repo/wikify/cli.py#L60) — documented in [wikify-cli](../../concepts/wikify-cli.md)
  - `wiki_subdir` — [`L58`](../../../../../raw/code/wikify-repo/wikify/cli.py#L58)
- protocol/private: `__init__`[`L44`](../../../../../raw/code/wikify-repo/wikify/cli.py#L44)
- uses (calls/refs, reference-scoped): [`state_path`](state.md#state_path)
- used by: [`prepare`](cli.md#prepare), [`finalize`](cli.md#finalize), [`plan`](cli.md#plan), [`coverage`](cli.md#coverage), [`lint_cmd`](cli.md#lint_cmd), [`_load`](cli.md#_load), [`verify`](cli.md#verify), [`_graph`](cli.md#_graph)  (1 test-only)

## Functions
- `_expand_shards(repo_dir: Path, patterns: list[str])` — [`L113`](../../../../../raw/code/wikify-repo/wikify/cli.py#L113) — Expand ``index_shards`` globs to sorted, de-duped repo-relative paths.
- `_find_docs(repo_dir: Path, patterns: list[str])` — [`L94`](../../../../../raw/code/wikify-repo/wikify/cli.py#L94) — Repo-relative project-doc paths matched by ``cfg.docs`` globs (sorted, deduped).
- `_graph(p: Paths)` — [`L126`](../../../../../raw/code/wikify-repo/wikify/cli.py#L126) — Build the graph, merging the C++ index (scip-clang) when present. — documented in [wikify-cli](../../concepts/wikify-cli.md)
- `_load(root: Path, slug: str)` — [`L76`](../../../../../raw/code/wikify-repo/wikify/cli.py#L76) — documented in [wikify-cli](../../concepts/wikify-cli.md)
- `_scip_clang_bin()` — [`L67`](../../../../../raw/code/wikify-repo/wikify/cli.py#L67) — The vendored scip-clang if present (glibc-compatible build), else PATH.
- `_source(cfg: RepoConfig, repo: str | None)` — [`L86`](../../../../../raw/code/wikify-repo/wikify/cli.py#L86)
- `_today()` — [`L63`](../../../../../raw/code/wikify-repo/wikify/cli.py#L63)
- `coverage(slug: str, root: Path = typer.Option(Path("."), help="Project root."), emit: bool = typer.Option(False, help="Write/refresh catalog pages."))` — [`L312`](../../../../../raw/code/wikify-repo/wikify/cli.py#L312) — Report whole-repo coverage (set-difference over the SCIP symbol table). — documented in [wikify-coverage](../../concepts/wikify-coverage.md)
- `finalize(slug: str, repo: str = typer.Option(None, help="Source path or git URL (overrides config)."), root: Path = typer.Option(Path("."), help="Project root."), fix: bool = typer.Option(False, help="Auto-repair deterministically-fixable lint errors first."))` — [`L224`](../../../../../raw/code/wikify-repo/wikify/cli.py#L224) — Stage 6: lint the agent-written pages, assemble the index, update state. — documented in [wikify-cli](../../concepts/wikify-cli.md)
- `lint_cmd(slug: str, root: Path = typer.Option(Path("."), help="Project root."), fix: bool = typer.Option(False, help="Auto-repair deterministically-fixable errors in place."))` — [`L290`](../../../../../raw/code/wikify-repo/wikify/cli.py#L290) — Re-run the citation linter alone (Stage 6 gate); ``--fix`` auto-repairs first. — documented in [wikify-cli](../../concepts/wikify-cli.md)
- `plan(slug: str, ref: str = typer.Option(None, help="Pinned commit/tag."), repo: str = typer.Option(None, help="Source path or git URL."), root: Path = typer.Option(Path("."), help="Project root."))` — [`L358`](../../../../../raw/code/wikify-repo/wikify/cli.py#L358) — Dry-run: print the reconcile delta, emit nothing. — documented in [wikify-cli](../../concepts/wikify-cli.md)
- `prepare(slug: str, ref: str = typer.Option(None, help="Pinned commit/tag to ingest."), repo: str = typer.Option(None, help="Source path or git URL (overrides config)."), root: Path = typer.Option(Path("."), help="Project root."), reindex: bool = typer.Option(True, help="(Re)run scip-python."))` — [`L138`](../../../../../raw/code/wikify-repo/wikify/cli.py#L138) — Stages 0-4: acquire, index, build graph, emit packets, print the plan. — documented in [wikify-cli](../../concepts/wikify-cli.md)
- `verify(slug: str, page: str = typer.Option(None, help="Dump claims for one concept (stem or filename)."), root: Path = typer.Option(Path("."), help="Project root."))` — [`L334`](../../../../../raw/code/wikify-repo/wikify/cli.py#L334) — List the load-bearing claims to adversarially verify (worklist for the — documented in [wikify-verify](../../concepts/wikify-verify.md)

## Module values
- `app` — [`L37`](../../../../../raw/code/wikify-repo/wikify/cli.py#L37)

