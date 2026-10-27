---
name: messaging-judgment
description: How a Clixen agent triages a human's messages — read the thread before classifying it, and treat "do nothing" as a first-class, evidenced outcome.
---

# Messaging judgment

Triage metadata lies. A human sender, a "RE:" subject, an unread
flag — none of these say what a thread needs. In the live Level 7
run, the highest-priority-looking thread in a real inbox needed no
action at all, and the genuinely important one needed something
no agent may do: the user's own decision. Both judgments came from
READING, not from the listing.

## Rules

1. **Open the thread before classifying it.** Read the full thread,
   newest message last, before assigning any verdict. Never draft,
   answer, or file from listing metadata alone.
2. **Every triage ends in a verdict with evidence.** Quote the
   sentence that decided it.
3. **"Do nothing" is a first-class outcome**, equal in dignity to
   acting — when the evidence supports it. The verdicts:
   - `needs_reply` — a question or request stands open for the
     user, and a reply from the agent is appropriate. Draft; the
     human sends.
   - `loop_closed` — the last message resolves the matter
     (confirmation, thanks, a decision already stated). No reply,
     no draft. Drafting here manufactures noise and can reopen
     settled threads.
   - `user_decision` — the thread asks for the USER's judgment: an
     offer, a negotiation, a commitment, money. Surface it with a
     one-line summary and the deciding facts. Never answer it, never
     draft an acceptance or a decline.
   - `not_mine` — the open question is addressed to someone else;
     the user is a cc or a bystander. No action.
4. **Sends are the human's.** This skill produces verdicts and, for
   `needs_reply`, drafts. It never sends.

## Worked examples

See `examples.md` in this skill: the two live Level 7 cases and
three synthetic misleaders, each with its verdict and the deciding
sentence.
