---
title: Architecture — the Python ↔ LLM split
type: doc-concept
provenance: doc
source: README.md
updated: 2026-06-27
status: fresh
---
# Architecture — the Python ↔ LLM split

## Definition
The README frames wikify-repo's architecture as a deliberately **hard boundary**
between deterministic Python stages and a single LLM-in-the-loop synthesis step. A
**deterministic tool** does the grounding (SCIP symbol graph, packets, citation lint);
**one LLM-in-the-loop step** does the synthesis (writing the prose concept pages). The
README's pipeline reads `scip-python / scip-clang → symbol graph → packets → [agent
synthesis] → citation lint → markdown wiki`, and its architecture table assigns each
stage to a side: acquire/pin, SCIP index → graph, reconcile diff, evidence, and packet
build are **Python**; concern synthesis is the **LLM agent**; citation lint + assemble
are **Python** again. The split is "hard" because the model is fenced between two
deterministic walls — it only writes inside a packet, and a Python gate checks its work.

## In wikify-repo (grounded)
The Python stages are real modules. Stage 1 indexing is
[`build_graph`](../catalog/wikify/scip_index.md#build_graph) over
[`run_indexer`](../catalog/wikify/scip_index.md#run_indexer) /
[`parse_index`](../catalog/wikify/scip_index.md#parse_index), producing the
[`SymbolGraph`](../catalog/wikify/graph.md#SymbolGraph); the whole pipeline is driven
deterministically from the CLI's [`prepare`](../catalog/wikify/cli.md#prepare). The LLM
step is *not* a Python module at all — the README points it at
`.agents/skills/…/SKILL.md` + `prompts/synthesis.md`, a tool-neutral markdown procedure,
and hands work to it through files: a **packet** (a relevance-bounded subgraph) goes in,
written pages come back. The closing Python wall is the linter:
[`finalize`](../catalog/wikify/cli.md#finalize) runs
[`lint_silo`](../catalog/wikify/lint.md#lint_silo), which loads each page's authorized
symbol set via [`read_subgraph`](../catalog/wikify/packet.md#read_subgraph) and rejects
any citation that doesn't resolve, emitting a
[`LintError`](../catalog/wikify/lint.md#LintError). So the agent can only cite symbols
the packet handed it, and a deterministic gate — not a prompt — proves it did.

## Why it matters / when it applies
The README calls this split "hard" because it is the project's central engineering risk
and its central guarantee: keep synthesis out of Python (no model can do the SCIP
resolution faithfully) and keep linting out of the prompt (no model reliably gates its
own hallucinations). The README is candid that the **riskiest foundation** is the
SCIP-occurrence → callers/callees heuristic — SCIP has no "call" role, so the derivation
is reference-scoped, not true call resolution, and is validated by
`tests/test_callers_callees.py`. The payoff of the split: the install needs *both* the
`wikify` CLI (deterministic stages) *and* an agent running the skill (synthesis), because
neither side can do the other's job. The idea, in the README's words: record all classes,
methods, and relationships with SCIP, then have the LLM annotate the top ~20% most
important nodes to cover ~80% of the repo's meaning.

## Connections
- Code concepts: [the CLI](../concepts/wikify-cli.md) — the deterministic driver of every
  stage; [SCIP indexing → SymbolGraph](../concepts/wikify-scip_index.md) — Stage 1;
  [the citation linter](../concepts/wikify-lint.md) — the closing Python wall;
  [reconcile state](../concepts/wikify-state.md) — the diff/pin bookkeeping behind
  idempotent re-runs.
- Module catalogs: [wikify/cli](../catalog/wikify/cli.md),
  [wikify/scip_index](../catalog/wikify/scip_index.md), [wikify/lint](../catalog/wikify/lint.md),
  [wikify/graph](../catalog/wikify/graph.md).
- Related doc-concepts: [SCIP vs AST parsing](scip-vs-ast-parsing.md) (the deterministic
  foundation); [the wiki as storage format](wiki-as-storage-format.md) (what synthesis emits).

## Source
Extracted from `README.md` ("Architecture (the Python ↔ LLM split is hard)"), kept in
place at `../../../../raw/code/wikify-repo/README.md`.
