---
name: fact_check
description: Fast verified answer to a single factual question.
metadata:
  tools: [search_web, fetch_page_text, fetch_url]
---

# Fact check mode

Answer one factual question, verified.

1. SEARCH: search_web for the claim.
2. FETCH: read the top primary source (fetch_page_text).
3. ANSWER: state the answer, cite the source URL, note confidence.

If sources conflict or are thin, say so. Never state an unverified fact
as certain. Keep the answer to a few sentences.
