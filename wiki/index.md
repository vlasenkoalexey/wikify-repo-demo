# Wiki index

**Read this first.** A content catalog of everything in this wiki — both **code repos** (ingested by the
`wikify-ingest-repo` skill) and **prose** (articles/docs/notes ingested the classic Karpathy way). Find
the relevant entry here, then drill into its page. See [`log.md`](log.md) for the chronological history.

## Code repos
One `wiki/code/<slug>/` per ingested repo. Open its `overview.md` as a map, then `grep` to the concept/catalog
page and cite the catalog anchor; drop to the pinned source for line-level certainty.

| Slug | Source repo | Pinned commit | What it answers |
|---|---|---|---|
| _(planned)_ `mini-pytorch-xla` | github.com/vlasenkoalexey/mini-pytorch-xla | _pending_ | `__torch_dispatch__` TPU backend: PJRT/libtpu via ctypes, StableHLO lowering, autograd frontend |

_To add one:_ **`ingest <repo-url-or-path>`** — the skill adds a row here and an entry to [`log.md`](log.md).

## Topics
Synthesized prose pages (`wiki/topics/<topic>.md`) — entities, concepts, comparisons that span sources.

_None yet._

## Sources
One summary page (`wiki/sources/<source>.md`) per ingested article/doc/note; the raw source lives in
`raw/sources/`.

_None yet._

_To add one:_ drop the file in `raw/sources/`, then ask the agent to ingest it — it writes a summary,
updates the topic pages it touches, cross-links, and logs it.

## Notes
Cross-cutting answers filed back from queries (`wiki/notes/<note>.md`) — may mix code and prose.

_None yet._
