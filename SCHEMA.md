# wikify-repo-demo — project memory

## What this is
The **companion demo + template for [wikify-repo](https://github.com/vlasenkoalexey/wikify-repo)** —
the tool (CLI + agent skill) that ingests a code repo into a grounded markdown wiki. This repo is what
that tool *produces and lives in*: a working instantiation of the
[Karpathy LLM-wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) for the
**code** domain. The sections below follow that gist and adapt it; the `wikify-ingest-repo` skill (which
**ships with wikify-repo**, installed into `.agents/skills/` here) is the maintainer that does the work.

## The core idea — instantiated for code
The usual way an agent answers a question about a codebase is RAG-shaped: grep the source, read some
chunks, reconstruct the answer from scratch — *every time*. Nothing accumulates, and the hard parts get
re-derived on every question: how a `nn.Module` is actually dispatched, which of five files a mechanism
really spans, whether a claim is grounded in real code.

This repo is different. Between the raw repos and your internals questions sits a **persistent,
compounding wiki**: when you ingest a repo, the tooling reads it, resolves its symbols, writes grounded
concept + catalog pages, links them, and lints every citation. The cross-references are already there;
the dynamic-dispatch seams a call-graph walk misses are already covered by deterministic catalogs; every
mechanism claim already cites a real symbol. **Compiled once, then kept current** — not re-derived per
query.

You never hand-write the wiki. The skill + deterministic CLI write and maintain all of it. **Your job:**
choose which repos to ingest, ask good internals questions, and file the good answers back. **Their job:**
the indexing, summarizing, cross-referencing, grounding, and bookkeeping.

## Architecture — three layers
1. **Raw sources — immutable.** Upstream repos, pinned by commit SHA, cloned under `raw/code/<slug>`.
   Read, never edited. `raw/` is gitignored — we pin by SHA, we don't vendor the code. This is the
   source of truth.
2. **The wiki — generated, owned by the tooling.** `wiki/<slug>/` — `overview.md`, `concepts/`,
   `catalog/`, `doc-concepts/`. The skill + CLI own this layer: they create pages on ingest, rebuild
   only the delta on update, maintain cross-links, and keep citations resolving. You read it.
3. **The schema — this file.** `SCHEMA.md` tells the agent how the wiki is structured and what workflow
   to follow for ingest / query / lint. `CLAUDE.md` / `AGENTS.md` / `GEMINI.md` are thin pointers so
   Claude Code, Codex, and Antigravity all read this one brain. Co-evolve it as conventions settle.

## Operations

**Ingest.** Add a repo. Just tell your agent: **`ingest <repo-url-or-local-path>`** — it runs the
procedure in **`.agents/skills/wikify-ingest-repo/SKILL.md`**:
`prepare` (pin + SCIP-index + symbol graph + packets) → synthesize one grounded concept page per packet
→ synthesize `overview.md` → ingest the repo's own docs into `doc-concepts/` → `finalize` (citation lint
+ coverage catalogs + assemble). One ingest touches many pages: every concept/catalog page for the repo,
plus `wiki/index.md` and an entry in `wiki/log.md`. **Idempotent reconcile** — re-running converges
(no-op, or just the changed delta); `ingest --ref <commit>` updates a pinned repo and rebuilds only the
symbols that moved.

**Query.** Ask a code-internals question and let the wiki's structure *route* you — don't fall back to
grepping raw source. Different questions want different page types:
- *"Where do I start / what are the main systems?"* → **`wiki/<slug>/overview.md`** — top-level concepts,
  system diagrams, and a map of *which concept page answers which question*.
- *"How does `<mechanism>` work — the control/data flow, and why is it built this way?"* →
  **`concepts/<concept>.md`** — a grounded mechanism page: prose + a Mermaid diagram + woven citations.
- *"What is `<symbol>` — its signature, where it's defined, who calls it?"* → **`catalog/<module>.md`** —
  the symbol's single home: signature, extracted docstring, a relative link to its exact source line, and
  an importance-ranked **uses-by** list (the inbound edges a name-based grep would miss or mis-attribute).
- *"What do the project's own docs say about `<X>`?"* → **`doc-concepts/<concept>.md`**.

Workflow: read **`index.md` first** to pick the repo, use `overview.md` as the map, then
`grep -ri "<symbol-or-term>" wiki/<slug>/` to land on the page and read only the relevant section. **Cite
the catalog anchor** (`catalog/<module>.md#<QualifiedName>`) and prefer the author's extracted docstring
over re-deriving behavior. Don't bulk-read whole pages.

**When you need line-level certainty, drop to the pinned source.** The wiki is *grounded in* the code, not
a replacement for it: every catalog entry carries a relative link to `raw/code/<slug>/…` at the pinned
commit. Follow it to confirm an exact signature, a branch, an edge case — the wiki's job is to get you to
the right ten lines without reading the whole repo.

**File good answers back.** A cross-cutting trace you reconstructed (e.g. the full dispatch path from a
public API call down to the backend kernel), a cross-repo comparison, an invariant you verified — write it
as a new `concepts/…` or `notes/…` page, link it from `index.md`, and log it, so explorations compound in
the wiki just like ingests do.

**Lint.** Periodically health-check the wiki. The deterministic gates: `wikify finalize <slug>` (hard
citation gate — every cited symbol must resolve, every mechanism claim must be cited), `wikify verify
<slug>` (adversarial check), and the **coverage** pass (set-difference over the symbol table → a catalog
page per module, so no subsystem is silently dropped). Then the judgment pass — look for: stale pages a
newer commit superseded (`ingest --ref`), orphan concept pages with no inbound links, important symbols
mentioned but lacking a page, missing cross-references between related concepts, and modules that only
got a thin catalog and deserve a real mechanism page.

## Indexing and logging
- **`wiki/index.md` is content-oriented and read first.** A catalog of every ingested repo — each with a
  link, a one-line summary, the pinned commit, and the questions it answers. The tooling updates it on
  every ingest; an agent reads it first to find the right pages, then drills in. At this scale (a handful
  of repos, hundreds of pages) the index + `grep` replaces embedding-based RAG entirely.
- **`wiki/log.md` is chronological and append-only.** One entry per operation, prefixed
  `## [YYYY-MM-DD] <op> | <slug>` (`ingest` / `update` / `lint` / `note`) so it stays parseable with plain
  unix tools — `grep '^## \[' wiki/log.md | tail -5` gives the last five operations.

## Grounding — what makes a *code* wiki trustworthy
Faithful synthesis is non-negotiable here (stronger than a freeform notes wiki): synthesis cites **only**
symbols in the packet subgraph; uncited claims go in `> [!inferred]` blocks; the citation linter is a
build gate, not a prompt. **Markdown is the only product** — SCIP indexes and build artifacts live in
gitignored `.cache/`, never in `raw/`.

## Why this works
The tedious part of a code knowledge base isn't the reading — it's the bookkeeping: keeping
cross-references current, re-grounding claims when code moves, representing every module, noticing when a
new commit invalidates a page. Humans abandon internals docs because that burden outgrows the value. The
tooling doesn't get bored, doesn't forget a cross-reference, and rebuilds only the delta — so the wiki
stays maintained because maintenance is near-zero-cost and idempotent. You curate and question; the skill
does everything else.
