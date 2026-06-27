# Wiki log

Append-only, chronological. One entry per operation, prefixed `## [YYYY-MM-DD] <op> | <slug>` so it
stays greppable with plain Unix tools (`grep '^## ' wiki/log.md`). Newest at the bottom.

## [2026-06-27] bootstrap | wikify-repo-demo
Created the demo: Karpathy LLM-wiki scaffolding (`SCHEMA.md` + `CLAUDE.md`/`AGENTS.md`/`GEMINI.md`
pointers, `wiki/index.md`, this log), `.gitignore`, and the `wikify-ingest-repo` skill installed
under `.agents/skills/`. No repo ingested yet.
