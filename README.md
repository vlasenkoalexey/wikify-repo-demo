# wikify-repo-demo

**The companion demo for [wikify-repo](https://github.com/vlasenkoalexey/wikify-repo).** wikify-repo
is the tool — a CLI + agent skill that ingests a code repo into a grounded markdown wiki. This repo
is what that tool *produces*: a live, browseable example so you can see the output before installing
anything.

It's a [Karpathy LLM-wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) applied
to **code** — the immutable "sources" are whole code repositories; the wiki is a grounded, lint-clean
**markdown** knowledge base an agent can answer internals questions from. It is built and kept current
by the **`wikify-ingest-repo`** skill, which ships with
[wikify-repo](https://github.com/vlasenkoalexey/wikify-repo) (not defined here — installed from there).

This repo is both:
- a **showcase** — clone it and browse a real, populated wiki under [`wiki/`](wiki/); and
- a **template** — click **“Use this template”** to start your own code-wiki with the skill and the
  agent conventions already wired up.

## What's in here

| Path | What it is |
|---|---|
| [`wiki/`](wiki/) | The product — one `wiki/<slug>/` per ingested repo (`overview.md`, `concepts/`, `catalog/`, `doc-concepts/`). All claims grounded + cited. |
| [`wiki/index.md`](wiki/index.md) | **Read first** — catalog of every ingested repo and the questions it answers. |
| [`wiki/log.md`](wiki/log.md) | Append-only ingest history (`## [date] ingest | <slug>`). |
| [`SCHEMA.md`](SCHEMA.md) | The agent brain — the three layers, the ingest/query/lint loop, retrieval rules. |
| `CLAUDE.md` / `AGENTS.md` / `GEMINI.md` | Thin pointers to `SCHEMA.md` (Claude Code / Codex / Antigravity). |
| `.agents/skills/wikify-ingest-repo/` | The ingest skill **installed from [wikify-repo](https://github.com/vlasenkoalexey/wikify-repo)** (read natively by Codex + Antigravity; symlinked into `.claude/skills/` for Claude Code). |

## Browse it (no install)

Open [`wiki/index.md`](wiki/index.md) and follow links, or `grep -ri "<term>" wiki/`. Everything is
plain markdown — no embeddings, no database. An agent answers cheaply by reading `index.md`, grepping
to the right page, and citing the catalog anchor.

## Make your own

1. **Use this template** (or `git clone` this repo).
2. Install the tooling once — see [wikify-repo](https://github.com/vlasenkoalexey/wikify-repo)
   (`pip install -e .` → `setup-vendor.sh` → `install-skill.sh /path/to/this-repo`).
3. In **Claude Code, Codex, or Antigravity**, just say:
   > ingest https://github.com/owner/your-repo
   The skill pins + indexes the repo, writes the grounded pages, lints them, assembles `wiki/<slug>/`,
   and updates `index.md` + `log.md`. Re-running is idempotent; `ingest --ref <commit>` updates to a
   newer commit and rebuilds only what changed.

## Why a wiki and not just grep over the source?

The wiki sits *between* raw repos and your questions: the cross-references are already there, the
dynamic-dispatch seams a call-graph walk misses are covered by deterministic catalogs, and every
mechanism page is grounded in real SCIP symbols. The tedious part — the bookkeeping — is done once
and kept current, so answers are fast, grounded, and consistent.
