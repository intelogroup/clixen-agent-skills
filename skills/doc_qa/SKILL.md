---
name: doc_qa
description: Answer questions from a PDF/document with quoted evidence.
metadata:
  tools: [fetch_page_pdf, fetch_page_text, fetch_url]
---

# Document Q&A mode

1. FETCH: use fetch_page_pdf (or fetch_page_text) to load the document.
2. ANSWER: respond only from the document's content. Quote the relevant
   passage for each claim, with page/section when available.
3. CITE: if a question cannot be answered from the document, say so
   explicitly -- do not guess or use outside knowledge.

Keep answers tight. Prefer quotes over paraphrase when precision matters.

