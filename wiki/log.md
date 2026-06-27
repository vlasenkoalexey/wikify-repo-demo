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
