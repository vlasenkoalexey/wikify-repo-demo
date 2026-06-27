---
title: Phased build plan & the mechanisms scale forced
type: doc-concept
provenance: doc
source: docs/implementation.md
updated: 2026-06-27
status: fresh
---
# Phased build plan & the mechanisms scale forced

## Definition
The plan is staged on purpose: *"Build **Phase 1 first** and make it pass its acceptance
test before anything else."* Phase 1 is a pure-Python repo end-to-end (Stages 0,1,2,5,6,6b),
**skipping** dispatch, C++, connect, discovery, and L4; evidence is tests-only. Later
phases are strictly additive — Phase 2 adds C++/dispatch, Phase 3 adds multi-repo connect,
Phase 4 adds discovery/lanes/L4. Each phase *ends at an acceptance test*. §10 ("Realized
mechanisms") then records what three real ingests (torchtitan, pytorch, jax, torch_tpu)
forced beyond the §1–9 plan, and is marked **authoritative**: *"Where this section
conflicts with an earlier one, this section wins."*

## In wikify-repo (grounded)
**Phase 1 acceptance** is the definition of done: [`prepare`](../catalog/wikify/cli.md#prepare)
emits one packet per concept with no model calls; agent synthesis writes one page per
concept; [`finalize`](../catalog/wikify/cli.md#finalize) exits 0 only when every citation
resolves; re-running with no change is a no-op ([`compute_plan`](../catalog/wikify/diff.md#compute_plan)
yields empty `todo`); adding one concept builds only that packet; and **whole-repo
coverage** ([`emit_catalogs`](../catalog/wikify/coverage.md#emit_catalogs) +
[`compute_report`](../catalog/wikify/coverage.md#compute_report)) represents every class
SCIP found.

**What scale forced (§10), grounded in the code that exists:**
- *Indexing at scale* — single-process scip-python OOMs on pytorch, so
  [`run_indexer_sharded`](../catalog/wikify/scip_index.md#run_indexer_sharded) runs one
  bounded `--target-only` process per shard (via
  [`_one`](../catalog/wikify/scip_index.md#run_indexer_sharded._one)) and unions them;
  [`_merge_shards_index`](../catalog/wikify/scip_index.md#_merge_shards_index) repairs each
  doc's path back to repo-relative, falling back to
  [`_path_from_moniker`](../catalog/wikify/scip_index.md#_path_from_moniker).
- *Recovery* — files pyright crashes on are reparsed by the AST fallback, and
  [`build_graph`](../catalog/wikify/scip_index.md#build_graph) synthesizes orphan nodes
  from a bare definition occurrence via
  [`_synth_symbol`](../catalog/wikify/scip_index.md#_synth_symbol) so they stay citable.
- *Devirtualization* — [`devirtualize`](../catalog/wikify/graph.md#devirtualize) runs Class
  Hierarchy Analysis over SCIP `is_implementation` to cross the dynamic-dispatch seam
  reference-scoping can't see — *"the 'connection' op decision 7 deferred."*
- *Relevance-bounded packets* — [`gather_subgraph`](../catalog/wikify/packet.md#gather_subgraph)
  replaces a flat BFS cap with an importance ÷ (1 + distance) frontier filling a budget.
- *Stage-6 hardening* — the catalog format ([`render_catalog`](../catalog/wikify/coverage.md#render_catalog),
  with `symbol_base` compression and **relative** source links),
  `finalize --fix` ([`fix_silo`](../catalog/wikify/fix.md#fix_silo)), adversarial
  `verify`, a synthesized `overview.md`, and **doc-concept ingest** itself — the last
  synthesis step, linted on **rule 1 only** by
  [`lint_doc_concepts`](../catalog/wikify/lint.md#lint_doc_concepts) (this very page is its
  product).

## Why it matters / when it applies
The phasing exists so the build never relitigates a working floor: Phase 1 proves the
deterministic-Python/LLM loop on a tractable repo before C++, connect, or discovery are
layered on. §10's *"this section wins"* clause is the practical instruction for anyone
modifying ingestion — the plan held in shape, but the scaled-up mechanisms (sharding, AST
fallback, devirtualization, relevance-bounded packets, the realized catalog format) are
where the *current* truth lives. Status per the doc: Phase 1 ✅, Phase 2 (C++ via bazel)
✅, discovery + scaled synthesis ✅.

## Connections
- Code concepts: [wikify-cli](../concepts/wikify-cli.md) — the `prepare`/`finalize`
  acceptance surface; [wikify-scip_index](../concepts/wikify-scip_index.md) and
  [wikify-ast_fallback](../concepts/wikify-ast_fallback.md) — Stage 1 at scale;
  [wikify-graph](../concepts/wikify-graph.md) — devirtualization;
  [wikify-coverage](../concepts/wikify-coverage.md) — the Phase-1 coverage gate;
  [wikify-verify](../concepts/wikify-verify.md) — the adversarial correctness floor;
  [wikify-discover](../concepts/wikify-discover.md) — the derived agenda.
- Module catalogs: [scip_index](../catalog/wikify/scip_index.md),
  [graph](../catalog/wikify/graph.md), [packet](../catalog/wikify/packet.md),
  [coverage](../catalog/wikify/coverage.md), [cli](../catalog/wikify/cli.md).
- Related doc-concepts: [python-llm-division](python-llm-division.md) — the loop Phase 1
  proves; [data-contracts](data-contracts.md) — the formats §10's mechanisms preserve.

## Source
Extracted from [`docs/implementation.md`](../../../../raw/code/wikify-repo/docs/implementation.md)
§6 ("Phased plan"), §8 ("What success looks like"), and §10 ("Realized mechanisms —
authoritative"); the doc stays in place.
