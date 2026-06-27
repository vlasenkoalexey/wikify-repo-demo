# Wiki index

**Read this first.** A content catalog of every code repo ingested into this wiki. For each, follow
its `overview.md` as a map, then grep to the concept/catalog page that answers your question and cite
the catalog anchor. See [`log.md`](log.md) for the chronological ingest history.

## Ingested repos

_None yet — this demo is bootstrapped but not yet populated._

To add one, ask your agent (Claude Code / Codex / Antigravity): **`ingest <repo-url-or-path>`**. On
each ingest, the skill adds a row here and an entry to [`log.md`](log.md).

| Slug | Source repo | Pinned commit | What it answers |
|---|---|---|---|
| _(planned)_ `mini-pytorch-xla` | github.com/vlasenkoalexey/mini-pytorch-xla | _pending_ | `__torch_dispatch__` TPU backend: PJRT/libtpu via ctypes, StableHLO lowering, autograd frontend |

## How to query
1. Read this index, pick the relevant slug.
2. Open `wiki/<slug>/overview.md` — the high-level map (main concepts + diagrams).
3. `grep -ri "<term>" wiki/<slug>/` to locate the page; read only the relevant section.
4. Cite the catalog anchor (`catalog/<module>.md#<QualifiedName>`); prefer extracted docstrings.
