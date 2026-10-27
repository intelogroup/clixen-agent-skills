---
name: web_form_fill
description: Navigate, fill, and commit web forms with approval gates.
metadata:
  tools: [browser_navigate, browser_read, browser_snapshot, browser_type, browser_click, browser_screenshot, browser_request_commit, browser_fill_credentials]
---

# Web form fill mode

You are filling a web form or completing a booking on the user's behalf.

1. NAVIGATE: open the target page with browser_navigate.
2. INSPECT: use browser_snapshot/browser_read to understand fields and
   required inputs.
3. FILL: use browser_type / browser_fill (credentials via browser_fill_credentials
   only when the user has approved that site). TYPE VISIBLY by
   default — the performance grammar (see web_navigate step 1):
   the user watches text appear as if typed, field by field, never
   a whole form populated in one blink. Instant fill is a named
   exception only: credentials through the vault route, and values
   too long to type (pasted documents, tokens).
4. VERIFY: screenshot before committing; show the user what will be submitted.
   Exception: on a sign-in form the screenshot gate refuses
   photography — verify by field readback and the post-submit
   state instead (the vault flow is web_navigate step 8).
5. COMMIT: use browser_request_commit and wait for explicit approval before
   the final submit.

6. POST-COMMIT VERIFICATION FOLLOWS THE SAME RULE (web_navigate
   step 9): the submission counts only when the underlying state
   shows it — the confirmation record, the saved value on
   readback, the entry in the list — never the success banner
   alone. If the banner claims success and the state disagrees,
   report the disagreement as a failure, not a success.

Never submit a payment or irreversible action without approval. Stop and ask
if a field is ambiguous or requires info only the user has.

