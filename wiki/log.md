# Wiki log

Append-only, chronological. One entry per operation, prefixed so it stays greppable with plain Unix tools
(`grep '^## \[' wiki/log.md | tail -5`). Prefixes: `ingest-code | <slug>` (code repo via the skill),
`ingest | <source>` (article/doc/note), `lint | <scope>`, `note | <title>`. Newest at the bottom.

## [2026-06-27] bootstrap | wikify-repo-demo
Created the demo: Karpathy LLM-wiki scaffolding for two source types — code repos (via the
`wikify-ingest-repo` skill) and prose (classic ingest). `SCHEMA.md` + `CLAUDE.md`/`AGENTS.md`/`GEMINI.md`
pointers, `wiki/index.md`, this log, `.gitignore`, and the skill installed under `.agents/skills/`.
Nothing ingested yet.

## [2026-06-27] ingest-code | mini_pytorch_xla
Ingested github.com/vlasenkoalexey/mini_pytorch_xla as a git submodule under
`raw/code/mini_pytorch_xla`, pinned at `0b58029` (`acquire: submodule`). `wikify prepare` indexed
493 symbols (scip-python) and emitted 7 packets; synthesized one grounded concept page each —
`mini_pytorch_xla-pjrt`, `-backend`, `-ops`, `-profiler`, `no_pytorch-tensor`, `-nn`, `-train_mini`
(the `__torch_dispatch__` TPU backend track + the from-scratch `no_pytorch` autograd stack, meeting
at the StableHLO+PJRT waist). Wrote `overview.md`. No repo docs to ingest (empty worklist).
`wikify finalize` passed first try — citation lint OK, 14 module catalog pages, 100% symbol coverage
(183 deep / 310 catalog-only), `index.md` assembled. Updated `wiki/index.md` Code-repos row.

## [2026-06-27] ingest | karpathy-llm-wiki-pattern
First prose ingest (classic Karpathy path). Source: Karpathy's LLM-wiki gist —
the article this repo instantiates, so a self-referential ingest. Fetched into
`raw/sources/karpathy-llm-wiki-pattern.md` (a fetched rendering, not byte-verbatim; provenance noted
in-file). Wrote summary `wiki/sources/karpathy-llm-wiki-pattern.md`; created two synthesized topic
pages — `topics/llm-wiki-pattern.md` (three layers / three ops + the code-as-a-source-type extension)
and `topics/rag-vs-compiled-knowledge.md` (ingest-time vs. query-time synthesis, plus the code grounding
twist). Cross-linked both into the `mini_pytorch_xla` code wiki and `SCHEMA.md`. Updated `wiki/index.md`
Topics + Sources sections.

## [2026-06-27] ingest-code | wikify-repo
Self-referential ingest — the wiki tool ingesting its own source. Added
github.com/vlasenkoalexey/wikify-repo as a submodule under `raw/code/wikify-repo`, pinned `7ada755`
(`acquire: submodule`). `wikify prepare` indexed 514 symbols (scip-python) and emitted 11 packets;
synthesized one grounded concept page each — cli, graph, scip_index, ast_fallback, discover, monikers,
coverage, lint, verify, state, config. Wrote `overview.md`. Ingested the repo's own docs (README +
docs/design + docs/implementation) into 10 `doc-concepts/` pages (incl. scip-vs-ast-parsing,
wiki-as-storage-format, python-llm-split, idempotent-reconcile, two-tier-coverage, devirtualization,
data-contracts, …). `wikify finalize` passed after one rule-2 repair (uncited Mechanism step in
wikify-verify) — citation lint OK, 40 module catalog pages, 100% symbol coverage (266 deep / 248
catalog-only / 51.8%), `index.md` assembled. Updated `wiki/index.md` Code-repos row.
