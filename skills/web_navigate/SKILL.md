---
name: web_navigate
description: Move around a real, hostile web page — clear overlays, find search, reach content anywhere on the page — on the way to a goal.
metadata:
  tools: [browser_navigate, browser_snapshot, browser_read, browser_click, browser_type, browser_scroll, browser_screenshot]
---

# Web navigation mode

You are operating a page the user can see (Clixen Desktop) or a browser
session on their behalf. Pages fight back: consent banners, popups,
sticky bars, lazy layout. Work this order, every time.

1. PERCEIVE THE WHOLE PAGE, NOT THE VIEWPORT. Your snapshot covers the
   full document, including everything below the fold. Never
   scroll-and-search for something your snapshot already contains —
   resolve the target directly and let it come into view in one move.
   The user sees one screenful; you know the whole page. Act like it.
2. FUSE YOUR SOURCES. An accessibility snapshot can miss controls that
   exist in the DOM (hidden until toggled, marked ignored). If a target
   that should exist (search, menu, close) is absent from the snapshot,
   check the DOM before concluding it isn't there. Absence in one
   source is not absence on the page.
3. CLEAR OVERLAYS BEFORE ANYTHING ELSE. Consent banners, subscribe
   modals and chat popups intercept clicks meant for content under
   them. Dismiss them first, under these strict rules — no exceptions:
   - The control must be a real button (or role=button), not a link or
     a text match inside an article.
   - Its accessible name must match the dismiss rule: an exact
     lexicon hit (Accept / Accept all / Reject all / Agree / Close /
     Dismiss / Got it / Continue / No thanks), OR a verb-first name —
     first word in {dismiss, close, accept, reject, agree, continue},
     at most ~6 words, every remaining word a notice-noun (privacy,
     cookie, consent, notice, banner, all…). Real example: "Dismiss
     privacy notice". Never substring-match names — "closed border"
     in a headline is not a Close button.
   - It must sit inside the overlay container (fixed-position layer),
     not in page content.
   - Prefer Reject all over Accept all when both exist and the task
     doesn't need the site's features.
   - After dismissing, verify: the overlay is gone AND the page URL
     did not change. If the URL changed, you clicked content, not the
     overlay — say so and recover, don't pretend it worked.
   - One overlay per pass, then re-perceive: banners stack.
4. SEARCH-FIRST ON SEARCH-LED SITES. News, shopping, docs and listing
   sites are built around search. If the goal names content, use the
   site's search instead of paging through listings: find the search
   control (step 2 if it hides behind a button), type the query,
   submit, and work from the results. Browse by hand only when search
   fails or the goal is the browsing itself.
5. CACHE IDENTITY, NEVER COORDINATES. Remember targets by role + name
   + what they are, never by pixel position. Pages move under you —
   humans scroll, layouts shift, banners land. Resolve the position
   fresh at the moment of action; a remembered coordinate is a future
   wrong click.
6. VERIFY AFTER EVERY ACTION. Re-perceive after each click/type and
   check the expected change actually happened (overlay gone, results
   loaded, value present). A dispatched action is not a done action.
   If the check fails, say what you see now — never report the intent
   as the outcome.
7. THE HUMAN WINS. If the user is touching the page — scrolling,
   clicking, typing — yield immediately and let them finish. Resume
   only when they hand it back. Your work is never worth a fight over
   the mouse.

Hand-offs: a form or booking in front of you → web_form_fill (its
approval gate owns the commit). Reading/research synthesis →
research_brief. This skill is movement and page control only; it never
submits, pays, or posts by itself.

## Field notes (tested verdicts — update as reality teaches)

- 2026-10-26 · Resolve-don't-scroll (step 1): WORKED on BBC home —
  2,745 elements, 90% below the fold (page 13,233 px, viewport 800 px);
  a footer-deep target resolved in one move from scroll 0 → 11,040.
  Fixture protocol: 140/140 runs, 0 stale clicks (scroll/move/modal/
  navigation interference).
- 2026-10-26 · AX misses DOM controls (step 2): CONFIRMED on BBC —
  Search button (aria-label "Search") and the search input existed in
  the DOM but not in the AX snapshot; input is hidden until toggled.
- 2026-10-26 · Hidden search controls (steps 2+4): BBC serves exactly
  one search input ("Search news, topics and more") and a Search toggle
  button — BOTH visibility:hidden at load in the variant the test
  egress received. DOM fusion finds them; click and focus routes both
  correctly refuse a hidden input (you cannot type into what isn't
  shown). Lesson: a found-but-hidden search means find and work the
  reveal toggle first; if the toggle is hidden too, re-perceive after
  hydration/scroll before concluding — and treat "present but hidden"
  as a distinct state from "absent", never click blind.
- 2026-10-26 · Multi-site sweep (Guardian/Verge/YouTube/Amazon/Reddit/
  Wikipedia): search found on 4 of 6 — Amazon and Wikipedia via AX
  (searchbox present), YouTube via AX (button), The Verge ONLY via DOM
  fusion (287 DOM nodes the AX pass missed; search textbox among them).
  Fusion (step 2) is load-bearing, not optional.
- 2026-10-26 · Real banner dismissal: WORKED end-to-end on The Verge.
  Correction to the earlier iframe guess (same day): frame enumeration
  found exactly ONE frame — the PMC privacy banner lives in the main
  document, and its control is a BUTTON aria-labelled "Dismiss
  privacy notice" inside the banner. The exact-name lexicon missed it;
  the verb-first + notice-noun rule (step 3, amended) qualifies it.
  Protocol run: perceive → announce → beat → revalidate → click →
  banner gone, URL unchanged. VERIFIED. (Frame enumeration is still
  worth having — other CMPs do use iframes — but it was not the
  blocker here; name-matching was.)
- 2026-10-26 · Unreachable from the sandbox egress (not perception
  failures): Guardian timed out; Reddit served a "Prove your humanity"
  bot wall (6 nodes); eBay a bot error page; CNN a blank. These sites
  need the user's real browser (Surface B), full stop.
- 2026-10-26 · Substring dismiss (step 3): FAILED in probe v1 —
  matched "close" inside a headline ("…closed border…") and clicked an
  article. The exact-name + inside-overlay + URL-unchanged rules above
  are the fix; a real consent banner end-to-end is still UNTESTED
  (BBC served none to the test egress; CNN/eBay unreachable there).
