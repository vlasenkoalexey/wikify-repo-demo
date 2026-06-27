---
title: 'Module: wikify/verify.py'
type: catalog
provenance: extracted
module: wikify/verify.py
status: fresh
symbol_base: scip-python python wikify-repo 0.0.0 `wikify.verify`/
symbols:
  aggregate: aggregate().
  load_bearing_claims: load_bearing_claims().
  load_bearing_claims.flush: load_bearing_claims().flush().
  Claim.id: Claim#id().
  _citations: _citations().
  PageReport.refuted: PageReport#refuted.
  Verdict: Verdict#
  PageReport.ok: PageReport#ok().
  Claim: Claim#
  Claim.section: Claim#section.
  Claim.text: Claim#text.
  Claim.citations: Claim#citations.
  Verdict.refuted: Verdict#refuted.
  Claim.line: Claim#line.
  PageReport: PageReport#
  PageReport.total: PageReport#total.
  _CLAIM_SECTIONS: _CLAIM_SECTIONS.
  Claim.page: Claim#page.
  Verdict.note: Verdict#note.
  PageReport.page: PageReport#page.
  Verdict.claim_id: Verdict#claim_id.
---
# Module: [`wikify/verify.py`](../../../../../raw/code/wikify-repo/wikify/verify.py)

## Classes
### `Claim`
- def: [`wikify/verify.py:31`](../../../../../raw/code/wikify-repo/wikify/verify.py#L31) — documented in [wikify-verify](../../concepts/wikify-verify.md)
- signature: `class Claim:`
- members:
  - `id(self)` — [`L39`](../../../../../raw/code/wikify-repo/wikify/verify.py#L39) — documented in [wikify-verify](../../concepts/wikify-verify.md)
  - `citations` — [`L36`](../../../../../raw/code/wikify-repo/wikify/verify.py#L36)
  - `line` — [`L33`](../../../../../raw/code/wikify-repo/wikify/verify.py#L33) — documented in [wikify-verify](../../concepts/wikify-verify.md)
  - `page` — [`L32`](../../../../../raw/code/wikify-repo/wikify/verify.py#L32) — documented in [wikify-verify](../../concepts/wikify-verify.md)
  - `section` — [`L34`](../../../../../raw/code/wikify-repo/wikify/verify.py#L34)
  - `text` — [`L35`](../../../../../raw/code/wikify-repo/wikify/verify.py#L35)
- used by: [`verify`](cli.md#verify), [`aggregate`](verify.md#aggregate), [`load_bearing_claims`](verify.md#load_bearing_claims), [`flush`](verify.md#load_bearing_claims.flush)  (6 test-only)

### `PageReport`
- def: [`wikify/verify.py:115`](../../../../../raw/code/wikify-repo/wikify/verify.py#L115) — documented in [wikify-verify](../../concepts/wikify-verify.md)
- signature: `class PageReport:`
- members:
  - `ok(self)` — [`L121`](../../../../../raw/code/wikify-repo/wikify/verify.py#L121)
  - `page` — [`L116`](../../../../../raw/code/wikify-repo/wikify/verify.py#L116) — documented in [wikify-verify](../../concepts/wikify-verify.md)
  - `refuted` — [`L118`](../../../../../raw/code/wikify-repo/wikify/verify.py#L118) — documented in [wikify-verify](../../concepts/wikify-verify.md)
  - `total` — [`L117`](../../../../../raw/code/wikify-repo/wikify/verify.py#L117) — documented in [wikify-verify](../../concepts/wikify-verify.md)
- uses (calls/refs, reference-scoped): [`Verdict`](verify.md#Verdict)
- used by: [`aggregate`](verify.md#aggregate)  (2 test-only)

### `Verdict`
- def: [`wikify/verify.py:108`](../../../../../raw/code/wikify-repo/wikify/verify.py#L108) — documented in [wikify-verify](../../concepts/wikify-verify.md)
- signature: `class Verdict:`
- members:
  - `claim_id` — [`L109`](../../../../../raw/code/wikify-repo/wikify/verify.py#L109)
  - `note` — [`L111`](../../../../../raw/code/wikify-repo/wikify/verify.py#L111)
  - `refuted` — [`L110`](../../../../../raw/code/wikify-repo/wikify/verify.py#L110) — documented in [wikify-verify](../../concepts/wikify-verify.md)
- used by: [`aggregate`](verify.md#aggregate), [`refuted`](verify.md#PageReport.refuted)  (2 test-only)

## Functions
- `_citations(text: str)` — [`L43`](../../../../../raw/code/wikify-repo/wikify/verify.py#L43) — documented in [wikify-verify](../../concepts/wikify-verify.md)
- `aggregate(page: str, claims: list[Claim], verdicts: list[Verdict])` — [`L125`](../../../../../raw/code/wikify-repo/wikify/verify.py#L125) — Fold per-claim verdicts into a page report (refuted claims fail the page). — documented in [wikify-verify](../../concepts/wikify-verify.md)
- `flush()` — [`L64`](../../../../../raw/code/wikify-repo/wikify/verify.py#L64) — documented in [wikify-verify](../../concepts/wikify-verify.md)
- `load_bearing_claims(page_path: str | Path)` — [`L47`](../../../../../raw/code/wikify-repo/wikify/verify.py#L47) — Extract the falsifiable claims from a concept page, in document order. — documented in [wikify-verify](../../concepts/wikify-verify.md)

## Module values
- `_CLAIM_SECTIONS` — [`L27`](../../../../../raw/code/wikify-repo/wikify/verify.py#L27) — documented in [wikify-verify](../../concepts/wikify-verify.md)

