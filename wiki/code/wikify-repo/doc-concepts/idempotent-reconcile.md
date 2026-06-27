---
title: Idempotent reconcile (ingest = plan/apply)
type: doc-concept
provenance: doc
source: docs/design.md
updated: 2026-06-27
status: fresh
---
# Idempotent reconcile (ingest = plan/apply)

## Definition
`/wikify-ingest-repo` is **one declarative reconcile**, in the spirit of `make`
or `terraform apply` — not a set of imperative build/update/add commands. Its
desired state is `{the pinned commit's symbols} × {the requested concept set}`,
and re-running simply *converges* the wiki to that state. The design is explicit
that there is therefore **no separate `update` skill**: first build, version bump
(`--ref <commit>`), and "add one more concept" are all the *same* operation, and
"update" is just `ingest --ref <newcommit>`. Same inputs → no-op; a new concept
in the config → build only that page; a moved `--ref` → diff the symbols and
rebuild only the stale pages; a wiped cache → regenerate the SCIP index.

## In wikify-repo (grounded)
Reconcile is the contract behind the deterministic stages, not a single function.
Convergence is anchored in **persisted state**: the prior symbol set lives in the
silo's state file, loaded by [`load_state`](../catalog/wikify/state.md#load_state)
and written by [`set_symbols`](../catalog/wikify/state.md#set_symbols) at the path
[`state_path`](../catalog/wikify/state.md#state_path) (first run starts from
[`_empty_state`](../catalog/wikify/state.md#_empty_state)). The `plan`-then-`apply`
split the doc calls for — preview the delta (`will build / will rebuild (stale) /
will leave / candidate concepts available`) before doing expensive work — is the
[`plan`](../catalog/wikify/cli.md#plan) command; the actual passes are
[`prepare`](../catalog/wikify/cli.md#prepare) (pin → SCIP index → graph → packets)
and [`finalize`](../catalog/wikify/cli.md#finalize) (lint → coverage → assemble),
both reading the same [`Paths.state`](../catalog/wikify/cli.md#Paths.state).

The **Stage 2 structural diff** is the *mechanism* reconcile uses when the commit
moved — not a separate command. Each symbol's `(signature + body-span)` is hashed;
a new-vs-old comparison yields `{added, removed, changed}`, and any concept page
citing a `changed` symbol is flagged `stale` for free via the citation graph. So
an upgrade re-runs only the changed symbols and the stale pages, while unchanged
pages stay `fresh` at the new commit without a SHA bump (the per-page `status`
flag, not a per-page SHA, is the currency source of truth).

## Why it matters / when it applies
This is what makes the wiki *cheap to keep current*: an overloaded ingest never
surprises you (plan previews the delta first), re-running is safe (idempotent),
and an upgrade rebuilds only the delta rather than the whole tree. Adding a
concept later is a same-commit reconcile — build only the new page from the
existing SCIP index, no re-extraction, no commit bump, nothing else marked stale,
then wire links and re-lint. It collapses the usual build/update/add command
surface into a single converging operation.

## Connections
- Code concepts: [wikify-state](../concepts/wikify-state.md) — the persisted
  reconcile state; [wikify-cli](../concepts/wikify-cli.md) — the `plan` /
  `prepare` / `finalize` command surface; [wikify-scip_index](../concepts/wikify-scip_index.md)
  — the SCIP index reconcile diffs against; [wikify-discover](../concepts/wikify-discover.md)
  — where candidate concepts come from.
- Module catalogs: [wikify/state.md](../catalog/wikify/state.md) ·
  [wikify/cli.md](../catalog/wikify/cli.md).
- Related doc-concepts: [packet-subgraph-grounding](packet-subgraph-grounding.md) ·
  [two-tier-coverage](two-tier-coverage.md).

## Source
Extracted from `../../../raw/code/wikify-repo/docs/design.md` (kept in place):
"Product surface — two skills", "Pipeline stages — Stage 2", "How this minimizes
effort".
