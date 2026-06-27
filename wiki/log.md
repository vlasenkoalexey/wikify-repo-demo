# Wiki log

Append-only, chronological. One entry per operation, prefixed so it stays greppable with plain Unix tools
(`grep '^## \[' wiki/log.md | tail -5`). Prefixes: `ingest-code | <slug>` (code repo via the skill),
`ingest | <source>` (article/doc/note), `lint | <scope>`, `note | <title>`. Newest at the bottom.

## [2026-06-27] bootstrap | wikify-repo-demo
Created the demo: Karpathy LLM-wiki scaffolding for two source types — code repos (via the
`wikify-ingest-repo` skill) and prose (classic ingest). `SCHEMA.md` + `CLAUDE.md`/`AGENTS.md`/`GEMINI.md`
pointers, `wiki/index.md`, this log, `.gitignore`, and the skill installed under `.agents/skills/`.
Nothing ingested yet.
