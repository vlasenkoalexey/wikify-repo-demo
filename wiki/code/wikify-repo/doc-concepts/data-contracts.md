---
title: Pinned data contracts — the wire formats the two halves agree on
type: doc-concept
provenance: doc
source: docs/implementation.md
updated: 2026-06-27
status: fresh
---
# Pinned data contracts — the wire formats the two halves agree on

## Definition
With synthesis pushed out-of-process and linting kept in Python, the two halves can only
cooperate if the **formats they exchange are frozen**. §5 of the plan does exactly that —
*"Data contracts (pin these — the linter and stubs depend on them)"* — fixing six
interfaces: (5.1) the **SymbolGraph derived from SCIP**, (5.2) **moniker ↔ filename**,
(5.3) the **citation grammar** the linter parses, (5.4) the **synthesis packet**, (5.5)
the **reconcile state JSON**, and (5.6) the **coverage / catalog** contract. These are
the load-bearing shapes; once pinned, both the deterministic side and the agent side can
be built and tested against them in isolation.

## In wikify-repo (grounded)
**SymbolGraph (5.1).** SCIP has *no "call" role*, so callers/callees are **approximated
by reference scoping**: a reference to symbol `S` whose range falls inside function `F`'s
definition span becomes edge `F → S` — symbol-accurate (the frontend bound the name) but
reference-derived, not true call resolution. This is the contract
[`build_graph`](../catalog/wikify/scip_index.md#build_graph) implements in
[`_process_document`](../catalog/wikify/scip_index.md#_process_document), with importance
ranked `outbound*5 + ref_count*2`.

**Moniker ↔ filename (5.2).** The *authoritative* identity is the full SCIP moniker, not
the slug filename — [`parse_symbol`](../catalog/wikify/monikers.md#parse_symbol) splits it
into a [`ParsedSymbol`](../catalog/wikify/monikers.md#ParsedSymbol) whose terminal
descriptor names the symbol. The linter resolves a citation by reading the *target's
frontmatter moniker* and checking it exists in the SCIP index, never by parsing the
filename, so the slug only needs to be deterministic and collision-free.

**Citation grammar (5.3).** A citation is a markdown link into a module **catalog**;
[`lint_silo`](../catalog/wikify/lint.md#lint_silo) enforces three hard, NLP-free rules
(every link resolves; every `## Entry points` / `## Mechanism` list item carries a
citation or evidence link; no symbol cited outside the packet subgraph), emitting a
[`LintReport`](../catalog/wikify/lint.md#LintReport) whose `.ok` gates the build. The
catalog frontmatter anchor map ([`symbol_anchor_map`](../catalog/wikify/coverage.md#symbol_anchor_map),
keyed by [`qualified_name`](../catalog/wikify/coverage.md#qualified_name)) is the
resolution table — and because the packet's citations and the catalog's anchors derive
from the *same* `qualified_name`, what a page cites and what resolves always agree.

**Synthesis packet (5.4).** One markdown file per concept (Seeds / Subgraph / Source /
Evidence / Template+rules), built by [`build_packet`](../catalog/wikify/packet.md#build_packet)
over a relevance-bounded [`gather_subgraph`](../catalog/wikify/packet.md#gather_subgraph)
plus [`collect_tests`](../catalog/wikify/evidence.md#collect_tests) evidence. The agent
reads *only* the packet — the subgraph is the exact set of symbols a page may cite.

**Reconcile state (5.5).** A flat `.cache/state/<slug>.json` of `{ref, symbols
(moniker→body-sha), pages (cited monikers, built_ref)}`. A page is *stale* iff a symbol
it cited changed body — the diff that [`compute_plan`](../catalog/wikify/diff.md#compute_plan)
computes from [`current_hashes`](../catalog/wikify/diff.md#current_hashes) against this
ledger.

**Coverage / catalog (5.6).** A **set-difference over the SCIP symbol table, NOT a graph
walk**: [`documentable_symbols`](../catalog/wikify/coverage.md#documentable_symbols) is
the universe, [`covered_monikers`](../catalog/wikify/coverage.md#covered_monikers) the
deep-cited subset, and [`emit_catalogs`](../catalog/wikify/coverage.md#emit_catalogs)
writes one generated page per module for the remainder so the catalogued set equals the
documentable set by construction.

## Why it matters / when it applies
The plan's framing is that these contracts are *prerequisites* — *"pin these — the linter
and stubs depend on them."* They are what let the file handoff work without coupling: the
packet tells the agent exactly which symbols are citable (5.4), the citation grammar lets
the linter verify grounding without understanding prose (5.3), and the shared
`qualified_name`/anchor derivation (5.3, 5.6) guarantees a cited anchor and a catalog
anchor never disagree. Touch any of these and both halves must move together — which is
why the SCIP-occurrence → callers/callees derivation (5.1) is called out as the *risky
foundation* that keeps a focused pinning test green.

## Connections
- Code concepts: [wikify-scip_index](../concepts/wikify-scip_index.md) (5.1),
  [wikify-monikers](../concepts/wikify-monikers.md) (5.2),
  [wikify-lint](../concepts/wikify-lint.md) (5.3),
  [wikify-state](../concepts/wikify-state.md) (5.5),
  [wikify-coverage](../concepts/wikify-coverage.md) (5.6),
  [wikify-graph](../concepts/wikify-graph.md) — the `SymbolGraph` these contracts ride on.
- Module catalogs: [scip_index](../catalog/wikify/scip_index.md),
  [monikers](../catalog/wikify/monikers.md), [packet](../catalog/wikify/packet.md),
  [lint](../catalog/wikify/lint.md), [coverage](../catalog/wikify/coverage.md).
- Related doc-concepts: [python-llm-division](python-llm-division.md) — the boundary these
  formats cross; [phased-build-plan](phased-build-plan.md) — how the contracts hardened
  under real ingests.

## Source
Extracted from [`docs/implementation.md`](../../../../raw/code/wikify-repo/docs/implementation.md)
§5 ("Data contracts"); the doc stays in place.
