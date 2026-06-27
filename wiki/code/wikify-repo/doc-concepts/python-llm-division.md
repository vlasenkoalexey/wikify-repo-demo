---
title: The Python↔LLM division — a deterministic pipeline that suspends to a file handoff
type: doc-concept
provenance: doc
source: docs/implementation.md
updated: 2026-06-27
status: fresh
---
# The Python↔LLM division — a deterministic pipeline that suspends to a file handoff

## Definition
The implementation plan's single most emphasized build rule: wikify is *"mostly
deterministic Python with exactly two LLM-in-the-loop steps,"* and *"keeping this
boundary clean is the most important implementation rule."* Everything mechanical —
acquire/pin, run the indexer, parse `.scip`, build the symbol graph, symbol diff,
dispatch, evidence collection, citation lint, assemble, index, coverage, dependency
links — is Python with **zero model calls**. Only **concept synthesis → mechanism
pages** (Stage 5) and **concept-correspondence judgment** (Stage 7b) are LLM, driven
by `SKILL.md`. The two halves *never share memory*: **handoff is via files on disk**.
The deterministic half never calls a model; the agent half never parses protobuf.

## In wikify-repo (grounded)
The boundary is realized as two CLI verbs that bracket the agent step, with `.cache/`
as the shared medium. [`prepare`](../catalog/wikify/cli.md#prepare) is the front half
(Stages 0–4): it pins the source with
[`acquire`](../catalog/wikify/acquire.md#acquire), indexes with
[`run_indexer`](../catalog/wikify/scip_index.md#run_indexer) /
[`run_indexer_sharded`](../catalog/wikify/scip_index.md#run_indexer_sharded), folds the
`.scip` into a [`SymbolGraph`](../catalog/wikify/graph.md#SymbolGraph) through
[`_graph`](../catalog/wikify/cli.md#_graph) → [`build_graph`](../catalog/wikify/scip_index.md#build_graph),
derives the agenda with [`discover_concepts`](../catalog/wikify/discover.md#discover_concepts),
computes the reconcile delta with [`compute_plan`](../catalog/wikify/diff.md#compute_plan),
and writes **one synthesis packet per concept** via
[`build_packet`](../catalog/wikify/packet.md#build_packet) — then **stops**. The packet
lands under [`Paths.cache`](../catalog/wikify/cli.md#Paths.cache). That suspension *is*
the handoff: the out-of-process agent reads only the packet and writes one
`concepts/<concept>.md` page back to disk.

[`finalize`](../catalog/wikify/cli.md#finalize) is the back half (Stage 6): it picks up
the agent's pages, lays the catalog homes with
[`emit_catalogs`](../catalog/wikify/coverage.md#emit_catalogs), gates them through
[`lint_silo`](../catalog/wikify/lint.md#lint_silo) (or
[`fix_silo`](../catalog/wikify/fix.md#fix_silo) with `--fix`), and — if
[`LintReport.ok`](../catalog/wikify/lint.md#LintReport.ok) — records reconcile state and
grades coverage with [`compute_report`](../catalog/wikify/coverage.md#compute_report).
[`plan`](../catalog/wikify/cli.md#plan) and [`lint_cmd`](../catalog/wikify/cli.md#lint_cmd)
are read-only windows onto the same machinery. The conceptual `ingest` is exactly
`prepare` + agent + `finalize`; lint failure loops the agent back to fix flagged pages,
then `finalize` again.

## Why it matters / when it applies
The plan is explicit about the two failure modes this split avoids: *"Do **not** put
synthesis logic in Python (you'll get rigid templated junk) and do **not** push linting
into the prompt (you'll get nondeterministic validation)."* Because the agent never sees
protobuf and Python never sees a prompt, each half is independently testable and
re-runnable, and the expensive model work replays from a frozen packet without
re-indexing. This is *why* there are two commands rather than one monolithic `ingest`:
the pipeline must physically suspend so an external agent can do the writing. The same
discipline carries into Stage 7 (Phase 3) — dependency links (7a) are deterministic
Python, only concept-correspondence (7b) is LLM judgment.

## Connections
- Code concepts: [wikify-cli](../concepts/wikify-cli.md) — the Typer driver that *is*
  this split; [wikify-scip_index](../concepts/wikify-scip_index.md),
  [wikify-coverage](../concepts/wikify-coverage.md), [wikify-lint](../concepts/wikify-lint.md),
  [wikify-discover](../concepts/wikify-discover.md), [wikify-state](../concepts/wikify-state.md)
  — the deterministic stages on the Python side.
- Module catalogs: [cli](../catalog/wikify/cli.md), [packet](../catalog/wikify/packet.md),
  [coverage](../catalog/wikify/coverage.md), [lint](../catalog/wikify/lint.md) — the
  full per-module indexes.
- Related doc-concepts: [data-contracts](data-contracts.md) — the wire formats that pass
  *through* the `.cache/` handoff; [phased-build-plan](phased-build-plan.md) — the order
  these stages were built and hardened.

## Source
Extracted from [`docs/implementation.md`](../../../../raw/code/wikify-repo/docs/implementation.md)
§2 ("The Python ↔ LLM division") and §4 ("CLI surface"); the doc stays in place.
