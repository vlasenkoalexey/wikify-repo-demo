---
slug: wikify-repo
commit: 7ada75520e46e4823f676bbfee48304de83ccf8e
scip_tool: scip-python
updated: 2026-06-27
---

# wikify-repo internals wiki

Generated, grounded wiki. Start from a concept (or an area); drill into cited symbols.
The commit pin above is the single source version for every page in this silo.

**Start here → [Overview](overview.md)** — the whole system in one page (main concepts + core diagrams + a map of the wiki).

## Concepts (deep)
| Concept | Page | Status |
|---|---|---|
| wikify-ast_fallback | [wikify-ast_fallback](concepts/wikify-ast_fallback.md) | fresh |
| wikify-cli | [wikify-cli](concepts/wikify-cli.md) | fresh |
| wikify-config | [wikify-config](concepts/wikify-config.md) | fresh |
| wikify-coverage | [wikify-coverage](concepts/wikify-coverage.md) | fresh |
| wikify-discover | [wikify-discover](concepts/wikify-discover.md) | fresh |
| wikify-graph | [wikify-graph](concepts/wikify-graph.md) | fresh |
| wikify-lint | [wikify-lint](concepts/wikify-lint.md) | fresh |
| wikify-monikers | [wikify-monikers](concepts/wikify-monikers.md) | fresh |
| wikify-scip_index | [wikify-scip_index](concepts/wikify-scip_index.md) | fresh |
| wikify-state | [wikify-state](concepts/wikify-state.md) | fresh |
| wikify-verify | [wikify-verify](concepts/wikify-verify.md) | fresh |

## Doc-derived concepts
Concepts extracted from the project's own docs (README / `docs/`), grounded to the symbol catalog. The source docs stay in place.
- [data-contracts](doc-concepts/data-contracts.md)
- [devirtualization](doc-concepts/devirtualization.md)
- [idempotent-reconcile](doc-concepts/idempotent-reconcile.md)
- [packet-subgraph-grounding](doc-concepts/packet-subgraph-grounding.md)
- [phased-build-plan](doc-concepts/phased-build-plan.md)
- [python-llm-division](doc-concepts/python-llm-division.md)
- [python-llm-split](doc-concepts/python-llm-split.md)
- [scip-vs-ast-parsing](doc-concepts/scip-vs-ast-parsing.md)
- [two-tier-coverage](doc-concepts/two-tier-coverage.md)
- [wiki-as-storage-format](doc-concepts/wiki-as-storage-format.md)

## Coverage
Two tiers: **concept pages** explain mechanisms deeply (selective); **module
catalogs** represent the rest so the whole repo is navigable. Coverage is a
set-difference over the SCIP symbol table, not a graph walk — every documentable
symbol is enumerated and represented.

- documentable symbols: **514** across 40 modules
- deep (concept pages): **266** (51.8%)
- catalog-only: **248**
- represented total: **514** (100.0%)
- classes represented: **19/19**

See [`catalog/`](catalog/) for the generated per-module structural index.

## Provenance
`extracted` = from SCIP / source. `inferred` = LLM judgment, treat as such.
Design-intent dynamics are labeled; none are runtime-measured (no L4 pass run).
Callers/callees are reference-scoped (SCIP has no call role), labeled "calls/refs".
