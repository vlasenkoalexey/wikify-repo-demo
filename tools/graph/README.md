# Wiki graph viewer

A standalone, dependency-free force-directed graph of the whole wiki — modeled on
[vasturiano/force-graph](https://github.com/vasturiano/force-graph)'s "highlight" example.
Nodes float in a force layout; **hover** a node to light up it, its neighbors, and the
connecting links; **click** to open the underlying `.md` page.

Adapted from the prose-only original in
[`tpu_performance_autoresearch_wiki`](https://github.com/vasturiano/force-graph) to also
understand this repo's **code wikis** — the `wiki/code/<slug>/…` pages produced by the
`wikify-ingest-repo` skill — so a graph covers both source types in one view.

## Use

```bash
# 1. (re)generate the graph data from the wiki's markdown links
python3 tools/graph/build_graph.py        # writes tools/graph/graph.json

# 2. serve from the repo root so node clicks resolve to /wiki/... pages
python3 -m http.server 8000
#    then open  http://localhost:8000/tools/graph/
```

Opening `index.html` via `file://` shows the graph too, but node-click "open page"
needs the HTTP server (browsers block `file://` cross-directory navigation).

## What it shows

- **One node per `wiki/**/*.md` page**, sized by link degree (hubs like a code
  `overview.md` or a heavily-cited `catalog/<module>.md` are biggest).
- **One edge per resolvable relative markdown link** between pages (the schema-mandated
  `[text](../dir/page.md)` form). Anchors (`#QualifiedName`, used by every code catalog
  citation) are stripped to the page; links into `raw/`, `../../SCHEMA.md`, and external
  URLs are ignored. `[[wikilinks]]` are *not* edges (they aren't markdown links).
- **Color = category.** Prose keeps its top-level folder; **code is split by page type** so
  the code-wiki anatomy is visible and toggleable:

  | Group | Pages |
  |---|---|
  | `code:overview` | `code/<slug>/overview.md` — the god-node map |
  | `code:concepts` | `code/<slug>/concepts/*.md` — grounded mechanism pages |
  | `code:catalog` | `code/<slug>/catalog/<module>/*.md` — per-module symbol catalogs |
  | `code:doc-concepts` | `code/<slug>/doc-concepts/*.md` — pages from the repo's own docs |
  | `code:index` | `code/index.md` and `code/<slug>/index.md` |
  | `sources` / `topics` / `notes` | the prose wiki |
  | `meta` | root `index.md` / `log.md` |

  This scales to several ingested repos: every codebase's concepts share the `code:concepts`
  color, so you read structure by *page type* and tell codebases apart by cluster + path.
- **Legend** toggles groups on/off; **search box** dims everything except matches
  (Enter zooms to them, Esc clears). **☀/☾ button** switches dark/light (remembered
  across visits). Idle nodes drift gently; drift pauses only while you drag.

## Files

This repo serves the viewer live via **GitHub Pages** (source: `main`/root):
**<https://vlasenkoalexey.github.io/wikify-repo-demo/tools/graph/>**. The README embeds a static still
that links here.

## Files

| File | Role |
|------|------|
| `build_graph.py` | walks the wiki, emits `graph.json` (`{nodes, links}`); see `page_group()` for the code/prose bucketing |
| `index.html` | the interactive viewer (loads `force-graph` from unpkg CDN) — this is what GitHub Pages serves |
| `render_static.py` | renders `graph.png` (the README still) from `graph.json` — optional, needs `networkx` + `Pillow` |
| `graph.json` | generated data — regenerate after wiki edits; safe to delete |
| `graph.png` | generated still for the README — regenerate after `graph.json` changes |

`graph.json` is a generated artifact. Regenerate it whenever the wiki changes
(e.g. after an `ingest`, or wire `build_graph.py` into a lint/finalize step if you want it
always fresh).
