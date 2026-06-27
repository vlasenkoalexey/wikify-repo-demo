---
title: Why use a wiki as the storage format
type: doc-concept
provenance: doc
source: README.md
updated: 2026-06-27
status: fresh
---
# Why use a wiki as the storage format

## Definition
The README argues that plain interlinked **markdown** — not a graph database, vector
index, or hosted service — is the right output because **the consumer is an AI agent**,
and agents already read markdown and retrieve with `grep` / `ripgrep` natively: no
query language, no graph runtime, no MCP server. "**The output is the interface.**"
Drop `wiki/` into a repo and any agent (Claude Code, Codex, Antigravity) answers from it
with zero adapter. The README's five reasons: it's **git** (versioned, diffable,
reviewable in a PR); **`grep` beats embeddings at this scale** (a read-first `index.md`
plus ripgrep finds the right page deterministically); **one artifact, two readers** (the
same page serves a human on GitHub and an agent answering a question); **the graph is in
the links** (markdown links + catalog anchors encode the relationships); and **you own
it** (plain files, no SaaS, no lock-in, markdown outlives proprietary formats).

## In wikify-repo (grounded)
"The graph is in the links" is concrete: a citation is a catalog anchor of the form
`catalog/<module>.md#Symbol`, and the citation linter keeps every such link resolvable —
graph-like navigation with no graph database to stand up. That linter is
[`lint_silo`](../catalog/wikify/lint.md#lint_silo) (driven by
[`finalize`](../catalog/wikify/cli.md#finalize)), which resolves each anchor through the
target catalog's frontmatter via
[`_resolve_citation`](../catalog/wikify/lint.md#_resolve_citation) and records any
failure as a [`LintError`](../catalog/wikify/lint.md#LintError) — so a link is only a
"graph edge" if it points at a real symbol. The README's honest tradeoff — a graph DB
wins at arbitrary transitive queries like "every transitive caller of `X`" — is answered
by **materializing** the common ones into the pages: per-symbol uses-by lists and
per-module catalogs derived from the
[`SymbolGraph`](../catalog/wikify/graph.md#SymbolGraph), so the frequent questions are
already answered as text and the rare deep query drops to the pinned source. Retrieval
itself needs no symbol resolution — an agent reads `overview.md` as the index and greps,
the same set membership the linter performs in reverse.

## Why it matters / when it applies
This is the ownership-and-trust thesis: the wiki is a product you keep in your own git
repo, offline and diffable, that "works well into the hundreds of pages" without
embedding infrastructure, similarity-threshold misses, or re-indexing. It applies
whenever the reader is an agent doing internals retrieval — the README notes you don't
even need the wikify-repo tool to *consume* a wiki, only a few lines in your
`CLAUDE.md` / `AGENTS.md` telling the agent to navigate it. The format also stays
trustworthy only because the links are gated: markdown is the *only* shipped product,
while SCIP indexes and build artifacts live in gitignored `.cache/`, never in `raw/`.

## Connections
- Code concepts: [the citation linter](../concepts/wikify-lint.md) — what keeps the
  link-graph resolvable; [coverage](../concepts/wikify-coverage.md) — the deterministic
  set-difference guaranteeing every module gets a page; [the CLI](../concepts/wikify-cli.md)
  — `finalize`/`assemble` that emit the markdown.
- Module catalogs: [wikify/lint](../catalog/wikify/lint.md),
  [wikify/graph](../catalog/wikify/graph.md), [wikify/cli](../catalog/wikify/cli.md).
- Related doc-concepts: [SCIP vs AST parsing](scip-vs-ast-parsing.md) (what makes a link
  citeable); [the Python ↔ LLM split](python-llm-split.md) (who writes the markdown).

## Source
Extracted from `README.md` ("Why use a wiki as the storage format"), kept in place at
`../../../../raw/code/wikify-repo/README.md`.
