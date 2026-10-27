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

1. PERCEIVE THE WHOLE PAGE, NOT THE VIEWPORT — BUT TRAVEL LIKE A
   HUMAN. Your snapshot covers the full document, including
   everything below the fold. Use that knowledge to PLAN, never to
   teleport. Clixen is not an agent-browser: perception may be
   instant and programmatic, PERFORMANCE IS HUMAN — visible actions
   a human would take, at a pace a human can follow. Scroll in
   steps until the target arrives in view (never resolve-and-jump),
   click the real control a human would click (the Search button,
   not the Enter shortcut; the link, not a scripted navigation),
   type visibly. The user sees one screenful; you know the whole
   page. Plan like it — move like them. (Performance grammar, Jim,
   2026-10-26.)
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
   - CONSENT LADDER (2026-10-26): consent is the human's to give, so
     on a cookie/consent banner take the least-permissive exit that
     keeps the page usable, in this order: (1) Refuse / Reject all;
     (2) Necessary / essential only — many banners offer Accept all +
     Necessary only with NO Refuse all, and tier 2 is the answer
     there, never tier 4; (3) Close / Dismiss (no consent decision);
     (3.5) ESCAPE TRICKS (Jim, 2026-10-26) — no sanctioned exit, but
     the site is still needed: first click OUTSIDE the banner (one
     neutral click on a non-interactive page area; some banners
     dismiss themselves), then HUNT inside the banner for any
     element whose click deletes it — an unlabelled ×, an icon, a
     span with a pointer cursor — x-like and corner elements first,
     one candidate at a time. The hunt NEVER clicks a consent
     control, and a click that navigates stops it at once. Verify
     after: banner gone, URL unchanged, and no consent granted as a
     side effect — deleting a banner is not accepting its cookies.
     Only when both tricks fail does the card come out;
     (4) Accept all — NEVER auto-clicked. If Accept all is the only
     way through, STOP and ask the human — the buddy puts up a CARD
     with the question and the choices as buttons ("Accept all
     cookies" / "Leave the site") and waits; the human's pick IS
     the authorization, and no pick (timeout) is NOT a yes. Their
     consent is not yours to grant. Default posture stays keen to
     refuse: tiers 1–3 never need the human. The existing "Prefer
     Reject all" line is tier 1 of this ladder, not the whole
     policy.
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

8. SIGN-IN IS A VAULT JOB. When a page asks for credentials:
   - Recognize the login form (email + password fields, a Sign in
     button). Check the vault for THIS domain first — an entry is
     bound to the domain it was saved for and never cross-fills
     another site's form.
   - Vault hit: fill through the credential route
     (browser_fill_credentials), click the form's real Sign in
     control, and verify the signed-in state on a fresh percept
     (rule 6). You never see the values — you work with a masked
     account label and the fill outcome.
   - Vault miss: have the vault card presented and wait. The user
     types into the card, never into chat. A cancel or a timeout
     BLOCKS the sign-in — never guess a credential, never ask for
     one in conversation, never type one from memory.
   - "Sign in with Google" is OAuth, not a password: click it,
     follow the account chooser as a new tab, and pick the account
     the user named (ask when several exist and none was named). A
     Google password is never collected into the vault. If Google
     refuses the automated browser ("this browser or app may not
     be secure"), hand that step to the user and resume on the
     post-login page.
   - Expect no screenshots here: the screenshot gate refuses
     photography while a password field is rendered or the card
     is up. Verify sign-ins from the tree, never from pictures.

9. VERIFY AGAINST STATE, NEVER AGAINST THE ANNOUNCEMENT. Every
   action ends in a verification, and the verification reads the
   state the action was meant to change — the counter, the cart
   total, the saved record, the URL — never the page's own success
   claim. Pages lie: a banner that cries "Order placed!" while
   nothing was ordered is a real, tested pattern (2026-10-27: the
   badge said placed, the orders counter said zero, and only the
   counter told the truth). A toast, badge or checkmark that the
   clicked control itself produces is evidence of nothing. If the
   state did not change, the action FAILED — say so, re-plan or
   escalate; never report the announcement as the outcome. Name
   the evidence in the receipt (verified_by): what you observed
   change.

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
- 2026-10-26 · SPA loading overlays (InfoChir tour): the site's own
  `#initial-loader` covered the whole page; the protocol REFUSED the
  first click (occluded, naming the loader) — correct behavior. The
  move is wait-for-loader → re-perceive → retry, never click through.
  Same tour proved step 5 the hard way: a retry that carried a ref
  across percepts clicked the WRONG card (IGM instead of the atlas),
  and step 6's verify caught it (VERIFY_FAIL, wrong URL). Refs are
  percept-scoped, positional, disposable — re-pick by identity after
  every perceive. Also: SPA pages need a render wait (poll until the
  expected content exists) before a percept can be trusted; the atlas
  went from 25 nodes (shell) to 101 nodes / 19 chapter links rendered.
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
- 2026-10-26 · Consent ladder (step 3): fixture-proven in the probe
  (consent.py + test_consent.py). Variant A (Accept all + Necessary
  only, no Refuse all) → picked Necessary, site recorded
  consent=necessary. Variant B (Accept all + Close ×) → closed,
  consent=none. Variant C (Accept all ONLY) → ask_human, banner left
  untouched, consent stayed undecided. Before the ladder, "Accept
  all cookies" matched the verb-first dismiss rule and could be
  picked over the minimal option sitting next to it — a consent
  grant the user never made. A live-site banner run is still owed.
- 2026-10-26 · Buddy ask-card (step 3, tier 4): Jim's design — when
  the ladder reaches ask_human, the buddy shows a card (question +
  choice buttons, agent overlay band so the mutation alarm ignores
  it) and WAITS. Probe-proven both ways (ask.py + test_ask.py):
  pick "Accept all cookies" → agent clicks it, outcome recorded as
  the USER's pick, consent=all; pick "Leave the site" → nothing
  clicked, consent stayed undecided, banner left standing. Timeout
  returns no pick, and no pick is not a yes.
- 2026-10-26 · Consent escape tricks (step 3, tier 3.5): Jim's two
  tricks for enforced-cookie banners, probe-proven (escapes.py +
  test_escapes.py; fixtures D/E, both ladder-dead-ends at
  ask_human). D (unlabelled span ✕ deletes the banner): click
  outside correctly failed, the hunt deleted it via the span on the
  first try, the Accept button never touched, badge stayed
  consent=undecided, URL unchanged. E (banner self-dismisses on
  outside click): click_outside alone won, consent undecided. The
  ask-card is now the LAST resort, after tiers 1–3.5 all fail.
- 2026-10-26 · Wikipedia mission (Jim's serious test): PASSED
  end-to-end on the live site — home → search "Portugal history" →
  open History of Portugal → scroll to the "Second Punic War"
  mention → it was a link → click → Second Punic War article →
  browser back → History of Portugal again, every step VERIFIED.
  Quirk worth keeping: the Vector search box + Enter does NOT land
  on a results page; it opens the suggestion list, whose top item
  is named "History of Portugal (Redirected from
  Portugal/History)" — match the article by name PREFIX, not exact
  name, or the mission stalls one step from done.
