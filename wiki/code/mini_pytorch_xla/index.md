---
slug: mini_pytorch_xla
commit: 0b580293319231283ef88640b3c0d41a8bfba9e4
scip_tool: scip-python
updated: 2026-06-27
---

# mini_pytorch_xla internals wiki

Generated, grounded wiki. Start from a concept (or an area); drill into cited symbols.
The commit pin above is the single source version for every page in this silo.

**Start here → [Overview](overview.md)** — the whole system in one page (main concepts + core diagrams + a map of the wiki).

## Concepts (deep)
| Concept | Page | Status |
|---|---|---|
| mini_pytorch_xla-backend | [mini_pytorch_xla-backend](concepts/mini_pytorch_xla-backend.md) | fresh |
| mini_pytorch_xla-ops | [mini_pytorch_xla-ops](concepts/mini_pytorch_xla-ops.md) | fresh |
| mini_pytorch_xla-pjrt | [mini_pytorch_xla-pjrt](concepts/mini_pytorch_xla-pjrt.md) | fresh |
| mini_pytorch_xla-profiler | [mini_pytorch_xla-profiler](concepts/mini_pytorch_xla-profiler.md) | fresh |
| no_pytorch-nn | [no_pytorch-nn](concepts/no_pytorch-nn.md) | fresh |
| no_pytorch-tensor | [no_pytorch-tensor](concepts/no_pytorch-tensor.md) | fresh |
| no_pytorch-train_mini | [no_pytorch-train_mini](concepts/no_pytorch-train_mini.md) | fresh |

## Coverage
Two tiers: **concept pages** explain mechanisms deeply (selective); **module
catalogs** represent the rest so the whole repo is navigable. Coverage is a
set-difference over the SCIP symbol table, not a graph walk — every documentable
symbol is enumerated and represented.

- documentable symbols: **493** across 14 modules
- deep (concept pages): **183** (37.1%)
- catalog-only: **310**
- represented total: **493** (100.0%)
- classes represented: **51/51**

See [`catalog/`](catalog/) for the generated per-module structural index.

## Provenance
`extracted` = from SCIP / source. `inferred` = LLM judgment, treat as such.
Design-intent dynamics are labeled; none are runtime-measured (no L4 pass run).
Callers/callees are reference-scoped (SCIP has no call role), labeled "calls/refs".
