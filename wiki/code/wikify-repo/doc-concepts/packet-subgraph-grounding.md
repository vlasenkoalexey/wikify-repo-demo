---
title: Packet/subgraph grounding contract (two floors: linter + verify)
type: doc-concept
provenance: doc
source: docs/design.md
updated: 2026-06-27
status: fresh
---
# Packet/subgraph grounding contract (two floors: linter + verify)

## Definition
The wiki's trustworthiness rests on a hard contract: synthesis is grounded in a
**packet** — a relevance-bounded subgraph of SCIP symbols — and **every
non-trivial claim must cite a symbol that exists in that grounding**. Uncited
claims are quarantined into `> [!inferred]` blocks. The design layers *two floors*
at different altitudes: a **grounding floor** (the citation linter proves every
claim cites a *real* symbol) and a **correctness floor** above it (adversarial
*verify* proves the claim is *true*). Both are build gates, not prompt
suggestions — *"this is the hallucination floor."*

## In wikify-repo (grounded)
A concept seeds from entry symbols and gathers its implementing subgraph by
traversing real SCIP edges, packaged by
[`build_packet`](../catalog/wikify/packet.md#build_packet) /
[`gather_subgraph`](../catalog/wikify/packet.md#gather_subgraph)
(seeds resolved via [`resolve_seeds`](../catalog/wikify/packet.md#resolve_seeds) /
[`auto_seeds`](../catalog/wikify/packet.md#auto_seeds)). The packet is the
citation index the synthesis prose cites into; the linter later reads the same
subgraph back via [`read_subgraph`](../catalog/wikify/packet.md#read_subgraph).

The **grounding floor** is [`lint_silo`](../catalog/wikify/lint.md#lint_silo) /
[`lint_page`](../catalog/wikify/lint.md#lint_page): every citation is resolved
against the catalog's symbol map by
[`_resolve_citation`](../catalog/wikify/lint.md#_resolve_citation), a dead
citation is a [`LintError`](../catalog/wikify/lint.md#LintError), and any
mechanism claim outside an `[!inferred]` block that lacks a citation also fails —
the rules collected in a [`LintReport`](../catalog/wikify/lint.md#LintReport).
Doc-concept pages (like this one) get a lighter rule via
[`lint_doc_concepts`](../catalog/wikify/lint.md#lint_doc_concepts): prose need not
stay inside a subgraph, but **every catalog link must still resolve to a real
symbol**.

The **correctness floor** is the adversarial `verify` pass:
[`load_bearing_claims`](../catalog/wikify/verify.md#load_bearing_claims) extracts
the citable claims ([`Claim`](../catalog/wikify/verify.md#Claim)), skeptic agents
refute each against source, and [`aggregate`](../catalog/wikify/verify.md#aggregate)
fails a [`PageReport`](../catalog/wikify/verify.md#PageReport) on *any* refutation.
The linter proves a claim *cites a real symbol*; verify proves the claim is *true*
— two gates at different altitudes.

## Why it matters / when it applies
This is the mechanism behind "minimal hallucination": a hallucinated API name
cannot survive the build, and `extracted` vs `inferred` provenance separates fact
from model guess at the page and claim level. The grounding contract is also what
makes citations *useful at query time* — a reader can verify or drill down
deterministically from a catalog anchor rather than re-deriving the answer.

## Connections
- Code concepts: [wikify-lint](../concepts/wikify-lint.md) — the grounding-floor
  citation linter; [wikify-verify](../concepts/wikify-verify.md) — the adversarial
  correctness floor; [wikify-graph](../concepts/wikify-graph.md) — the symbol graph
  packets are carved from; [wikify-scip_index](../concepts/wikify-scip_index.md) —
  the SCIP citation namespace every claim resolves into.
- Module catalogs: [wikify/lint.md](../catalog/wikify/lint.md) ·
  [wikify/verify.md](../catalog/wikify/verify.md) ·
  [wikify/packet.md](../catalog/wikify/packet.md).
- Related doc-concepts: [idempotent-reconcile](idempotent-reconcile.md) ·
  [two-tier-coverage](two-tier-coverage.md).

## Source
Extracted from `../../../raw/code/wikify-repo/docs/design.md` (kept in place):
"Three layers, not one" (decision 2), "Stage 6 — Assemble, lint, publish",
"A correctness floor above the grounding floor", "How this minimizes
hallucination".
