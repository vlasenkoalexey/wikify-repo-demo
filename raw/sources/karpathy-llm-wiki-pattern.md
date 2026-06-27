<!--
provenance: fetched rendering (not byte-for-byte verbatim) of the gist below.
canonical: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
author: Andrej Karpathy
fetched: 2026-06-27 via WebFetch (gist.githubusercontent.com/.../raw)
note: The fetch summarized lightly; quoted phrases are reproduced as returned.
      For the exact original, see the canonical URL. This file is the curated
      raw source of truth for the prose ingest of this article.
-->

# LLM Wiki Pattern Summary

This document presents a framework for building personal knowledge bases with LM assistance. Rather than traditional RAG systems that retrieve raw documents on each query, the pattern proposes maintaining a persistent wiki—a structured collection of interlinked markdown files that compounds over time.

## Core Concept

The approach differs fundamentally from conventional document retrieval. As the creator explains: "the wiki is a persistent, compounding artifact. The cross-references are already there. The contradictions have already been flagged."

The human handles curation and strategic questions while the LLM manages the labor-intensive work of summarizing, cross-referencing, and maintaining consistency across pages.

## Three-Layer Architecture

**Raw sources** remain immutable—your collection of articles, papers, and data.

**The wiki** consists of LLM-generated markdown pages that the model actively maintains and updates.

**The schema** documents governing how the system operates—conventions, workflows, and structural rules.

## Key Operations

*Ingest*: Processing new sources by reading, summarizing, and integrating information across 10-15 existing wiki pages.

*Query*: Searching relevant pages and generating answers in various formats—markdown, tables, or slides.

*Lint*: Periodic health checks identifying contradictions, orphaned pages, and knowledge gaps.

## Why This Succeeds

The pattern works because "the tedious part of maintaining a knowledge base is not the reading...it's the bookkeeping." LLMs excel at the maintenance work that causes humans to abandon wikis, keeping the structure current through sustained effort.
