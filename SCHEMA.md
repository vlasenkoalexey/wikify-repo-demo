# wikify-repo-demo — project memory

## What this is
A **live demo + template** of the [Karpathy LLM-wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
applied to **code**: instead of articles, the immutable sources are whole *code repos*, and the
wiki is a grounded, lint-clean **markdown** knowledge base an agent answers internals questions
from. The wiki is built and maintained by the **`wikify-ingest-repo`** skill (see
[wikify-repo](https://github.com/vlasenkoalexey/wikify-repo)); this repo is what that skill
*produces and lives in*.

Clone it to browse a real wiki, or use it as a GitHub **template** to start your own.

## The three layers (Karpathy)
1. **Raw sources — immutable.** Upstream repos, pinned by commit SHA, cloned under `raw/code/<slug>`.
   Never edited; `raw/` is gitignored (we pin by SHA, we don't vendor the code).
2. **The wiki — generated.** `wiki/<slug>/` — `overview.md`, `concepts/`, `catalog/`, `doc-concepts/`.
   This is the committed product. Every claim is grounded in a SCIP-resolved symbol and cited.
3. **The schema — this file.** `SCHEMA.md` is the one source of truth; `CLAUDE.md` / `AGENTS.md` /
   `GEMINI.md` are thin pointers so Claude Code, Codex, and Antigravity all read the same brain.

## The three operations
- **Ingest** — add a source. Run the skill: just ask your agent to **`ingest <repo-url-or-path>`**.
  It pins + indexes the repo, writes grounded concept pages, runs the citation linter, assembles
  `wiki/<slug>/`, then appends to `wiki/log.md` and updates `wiki/index.md`. A single ingest is
  idempotent — re-running converges (no-op or just the delta).
  > **Procedure:** `.agents/skills/wikify-ingest-repo/SKILL.md` (Claude Code runs it as a skill;
  > Codex + Antigravity read it from `.agents/skills/`).
- **Query** — answer a question *from the wiki*, cheaply. Read `wiki/index.md` first, then the
  relevant `wiki/<slug>/overview.md` as a map; **grep** to locate the concept/catalog page, read
  only that section, and cite it. Do **not** bulk-read whole pages. A valuable answer worth keeping
  becomes a new/updated wiki page rather than vanishing into chat.
- **Lint / update** — keep it healthy. `wikify finalize <slug>` is the hard citation gate;
  `wikify verify <slug>` is the adversarial check; `wikify prepare <slug> --ref <commit>` rebuilds
  only the symbols that changed at a new commit.

## Conventions
- **`wiki/index.md` is read first** — a content catalog of every ingested repo and the questions it
  answers. Updated on every ingest.
- **`wiki/log.md` is append-only** — one line per ingest, prefixed `## [YYYY-MM-DD] ingest | <slug>`,
  so it stays greppable with plain Unix tools.
- **Grounding before prose.** Synthesis cites only symbols in the packet subgraph; uncited claims go
  in `> [!inferred]` blocks. The linter is a build gate, not a prompt.
- **Markdown is the only product.** No SQLite / graph DB; SCIP indexes + build artifacts live in
  gitignored `.cache/`.

## Retrieval rule (for answering questions here)
> Source of truth: the wikis under `wiki/`. **Retrieve**, don't bulk-read — `index.md` → the slug's
> `overview.md` → grep for the concept/catalog page → read only that section and cite the catalog
> anchor. Prefer the author's docstrings (catalog `extracted` blocks) over re-deriving behavior.
