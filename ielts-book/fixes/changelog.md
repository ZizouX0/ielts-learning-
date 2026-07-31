# Fix log

Every `[CRITICAL]` and `[MAJOR]` issue, what changed, and the source that
justified the change.

Issues found by the Editor before Phase 3 are logged here too, marked
`[editor]` — the adversarial verifiers still run independently and are not
bound by anything recorded here.

---

## Editor pre-verification pass (before Phase 3)

Run in the main thread while agent capacity was unavailable. These are the
checks that do not require independent re-research.

### Clean results

| Check | Result |
|---|---|
| `[UNVERIFIED]` tags surviving into any chapter | **0** across all nine chapters |
| Citations of the superseded 2013 Writing descriptors (`assets.ctfassets.net`) | **0** |
| Citations of the superseded 2008/2013 Speaking descriptors (`cambridgeenglish.org/webinars`) | **0** |
| The fabricated "73% lose LR points on collocation" statistic | **0** — correctly absent, and not repeated even to debunk |
| Official worked-example material flagged by R3 (Marie Curie / radium / polonium set) | **0** |
| Chapters ending mid-sentence or missing the mandated 60-second summary | **0** |

### `[MAJOR]` `[editor]` — Chapters 2 and 6 contradicted each other on the reader's own phonology

**Issue.** Chapter 2 stated flatly that *"Arabic does not use a /p/ phoneme"* and
prescribed dictation drills on that basis. Chapter 6, working from R6's research,
states the opposite and with better grounding: Tunisian Arabic has /p/ in
loanwords, **French supplies [p]**, so the phoneme is not missing — the real
issue is **aspiration** on English word-initial /p t k/.

**Why it matters.** Beyond the contradiction, Chapter 2's version is precisely the
generic Arabic-L1 advice R6 warned against, built on Modern Standard and Gulf
phonotactics rather than on a Tunisian bilingual. Left as written, it would have
sent the reader drilling a problem Chapter 6 tells him he does not have.

**Change.** Chapter 2's claim rewritten to match Chapter 6: the phoneme is not
missing, the difficulty is aspiration, and that is a production issue treated in
Chapter 6. The listening drill is **kept** but re-justified honestly — perceiving
the contrast under time pressure in an unfamiliar proper noun is a genuinely
separate skill from producing it, and a misheard name still costs a mark.

**Source.** R6 research file (`research/R6-speaking.md`), §L1 alert; cross-checked
against Chapter 6 lines 553, 583–585, 596.

**Status.** ~~Fixed.~~ **Was incomplete — see below.**

### `[MAJOR]` `[V4]` — the /p/ fix above was incomplete, and the Editor should have caught it

**Issue.** V4 confirmed the Chapter 2 rewrite was sound and that Chapters 2 and 6
now agree — but found `07-vocabulary.md` §L1 alert still asserting *"Arabic has
no /p/ and no /v/"*, where the claim is load-bearing for an entire
spelling-error class. Three chapters, two of them corrected, one missed.

**Root cause — Editor error.** The original fix was made by editing the one
location the Editor happened to find while checking a *different* consistency
question. **No grep was run across the book before the entry was marked fixed.**
That is exactly the mistake the verification phase exists to catch, and it is
worth recording rather than quietly patching: a fix applied by inspection instead
of by search is not a fix, it is a coincidence.

**Change.** Chapter 7's passage rewritten to match Chapters 2 and 6 — Tunisian
Arabic carries /p/ and /v/ in loanwords, French supplies both regardless, so
neither is missing from the reader's inventory; what survives into *spelling* is
the older substitution habit (*broblem*). Cross-referenced to Chapter 6 for the
aspiration explanation. The short-vowel point, which is independent and correct,
is retained.

**Verification this time.** Grepped all nine chapters plus `knowledge/` and
`CLAUDE.md` for every phrasing of the claim. Zero remaining. All /p/ mentions
across the book now agree.

**Still open for V1:** the underlying phonological claim about Tunisian Arabic
phonotactics, which R6 flagged as its own highest-stakes Tier-3-dependent
finding.

---

## Phase 4 — post-verification fix loop

_Populated once V1–V5 have reported._
