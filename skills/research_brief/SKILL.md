---
name: research_brief
description: Search, fetch, and synthesize a cited research brief.
metadata:
  tools: [search_web, fetch_page_text, fetch_page_pdf, fetch_url]
---

# Research brief mode

You are producing a research brief, not a chat reply. Work in three phases:

1. SEARCH: use search_web to find 3-6 relevant, diverse sources. Prefer
   primary sources (official docs, papers, vendor sites) over aggregators.
2. FETCH: use fetch_page_text (and fetch_page_pdf for PDFs) on the best
   sources. Do not rely on search snippets alone -- read the pages.
3. SYNTHESIZE: produce a brief with these sections:
   - Bottom line (2-3 sentences)
   - Key findings (bulleted, each with a citation [1], [2], ...)
   - Sources (numbered list of URLs actually fetched)
   - Open questions (what you could not verify)

Cite only what you actually fetched and read. Never fabricate a citation.
If a claim cannot be verified from fetched sources, say so under open
questions. Keep the brief scannable; the user asked for a brief, not an essay.
