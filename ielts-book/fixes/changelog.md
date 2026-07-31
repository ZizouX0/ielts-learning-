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

### Chapters 1 and 2 — fix agent

Scope: `chapters/01-how-ielts-works.md` and `chapters/02-listening.md` only.

#### `[CRITICAL]` `[V1]` `[V4]` `[V5]` — "Half-band thresholds are not published by any official source" was false

**Issue.** Ch1 asserted that no official source publishes half-band raw-score
thresholds and refused to print them; it also listed the half-band table as a
*myth*, with a fabricated provenance ("every 'complete' table online reconstructs
half-bands from retired practice books"). Ch2 printed half-band rows labelled
*(interpolated — not official)*. Ch3 printed the real IDP table as fact. Three
chapters, three positions, and the false one was load-bearing for the book's
strategic argument.

**Change (Ch1).** Deleted the "not published" sentence and the fabricated-provenance
myth. The band-math section now prints **both** official tables: the four ielts.org /
British Council anchors, and IDP's full nine-row table including every half band, for
Listening and Academic Reading side by side. Added the cross-check that every
ielts.org anchor is exactly the bottom mark of the corresponding IDP band row. Kept
and strengthened the official version caveat, from both sources. Rewrote the myth
entry to "There is an official one — it is just not a guarantee." Rewrote self-test
Q5, which asked the reader to defend a policy the book no longer holds.

**Change (Ch2).** Removed both *(interpolated — not official)* labels and the note
beneath the table. Corrected the numbers: band 6.5 is **26–29**, not "~26–27"; band 7
is 30–31; 7.5 is 32–34; 8.0 is 35–36. Sourced to IDP with IDP's own averaging caveat.
Added the pointer that Ch1 and Ch3 print the same table.

**Change (both).** Added the consequence in the text, because it is the most
motivating number in the book: **Listening band 6.5 runs to 29 and band 7 begins at
30 — one mark.** Ch1 also now warns that the anchors are identical from band 6 up but
the *ranges* are not: a raw 26 is 6.5 in Listening and still 6 in Reading; a raw 32 is
7.5 in Listening and still 7 in Reading.

**Source.** `[src: ielts.idp.com — Listening band scores]`, `[src: ielts.idp.com —
Reading band scores]`, both fetched by V1 on 2026-07-31; anchors and version caveat
`[src: ielts.org — IELTS scoring in detail: band scores explained]`.

**Not changed.** Ch3's Reading table — correct already, and owned by another agent.
Ch1's Reading band-5 anchor of 15 — already correct against ielts.org; the 16 that
needs fixing is in Ch3.

#### `[MAJOR]` `[V1]` `[V4]` — Ch1's 2h45-vs-2h40 reconciliation was unsourced inference

**Issue.** Ch1 asserted "2h40m is the paper-mode sitting". ielts.org publishes 2h40
for the written session with no delivery-mode caveat, and Ch9 uses 2h40 as the
*computer* figure — so Ch1's explanation was both unsourced and internally
contradictory.

**Change.** The invented reconciliation is gone. Ch1 now states both published
figures, says plainly that neither carries a mode caveat and that this book will not
invent one, notes that the computer components sum to about 2h32, and tells the reader
to treat 2h40 as the time he must be seated and to budget against the individual paper
timings. Also corrected the citation name to *What to expect on IELTS test day*.

**Source.** `[src: ielts.org — What to expect on IELTS test day]`.

#### `[MAJOR]` `[V1]` — Ch1's Tunisia paper-option reasoning was wrong

**Issue.** Ch1 said British Council Tunisia "lists only computer-delivered testing…
no paper option". The English-language General Training page on the same site quotes a
paper-based fee, so the site is inconsistent in English as well as French — which also
kills Ch9's "stale translation" diagnosis.

**Change.** Rewritten: the dates/fees/locations page lists computer and Online across
the five locations; other pages on the same site, **in English as well as French**,
still quote a paper-based fee; the site cannot settle the question, so phone the
centre. The operational conclusion (book computer) is unchanged.

**Source.** `[src: britishcouncil.tn — Test dates, fees and locations]`,
`[src: britishcouncil.tn — IELTS General Training (English page)]`.

#### `[MAJOR]` `[V4]` — Ch2 named three criteria as four and gave Writing a Speaking-only criterion

**Issue.** Ch2: "The four-criterion apparatus — Fluency and Coherence, Lexical
Resource, Grammatical Range and Accuracy — applies only to Writing and Speaking."
Three items, and *Fluency and Coherence* is Speaking-only. Ch1's self-test asks the
reader to name the four Writing Task 2 criteria; a reader who learned them here would
answer wrongly.

**Change.** Rewritten to name both sets in full: Task Response/Achievement, Coherence
and Cohesion, Lexical Resource, Grammatical Range and Accuracy in Writing; Fluency and
Coherence, Lexical Resource, Grammatical Range and Accuracy, Pronunciation in
Speaking.

**Source.** Matches Ch1 §Writing and Speaking and Ch6; `[src:
takeielts.britishcouncil.org — IELTS Guide for teachers (PDF)]`.

#### `[MAJOR]` `[V1]` `[V4]` — `ONE WORD ONLY` looked like a Ch2/Ch3 disagreement

**Issue.** Ch2 correctly reported that the phrase could not be verified verbatim in
any official *Listening* document. Ch3 quotes it as standard Reading rubric. Neither
mentioned the other, so a reader meeting Ch2 first distrusts Ch3.

**Change.** Ch2's entry rewritten: it **is** verbatim official — twice in the 2023
Academic Reading sample tasks — and is absent from the 2023 Listening sample tasks.
Expect it in Reading; do not assume it in Listening; the operating behaviour is
unchanged. Ch2's hedge survives as a Listening-specific finding rather than a global
doubt.

**Source.** `[src: T1 ielts.org — Academic Reading sample tasks 2023]`,
`[src: T1 ielts.org — Listening sample tasks 2023]`.

#### `[MAJOR]` `[V1]` — the five-accent citation did not corroborate five accents

**Issue.** Ch2 cited two "corroborating" sources for the five-accent list; neither
names five, and both are explicitly non-exhaustive.

**Change.** The list is now sourced to the one document that states it — the IELTS
Guide for teachers, quoted verbatim — and the chapter says openly that only one
official document names five, quoting ielts.org's "including" and Cambridge's "for
example" wording. Framing softened to "treat five as the working number and the list
as non-exhaustive".

**Source.** `[src: T1 takeielts.britishcouncil.org — IELTS Guide for teachers (PDF),
p.5]`, `[src: T1 ielts.org — Listening test format]`, `[src: T1 cambridgeenglish.org —
FAQs p.4]`.

#### `[CRITICAL]` `[V5]` — "Train on five accents" and "have them dictated back", with no source and no dictator

**Issue.** Ch2's premise is that one unfamiliar accent can cost ten marks, and it
named zero audio sources. "Have them dictated back" assumed a study partner the reader
does not have, and the repo's `/listening` command is text-adapted and cannot play
sound. The highest-frequency unexecutable instruction in the chapter, on the paper Ch1
identifies as the Arabic-L1 blind spot.

**Change.** New section **§Where the audio comes from**, in three layers:
*Layer 1 — official audio, finite:* British Council free practice tests, the
familiarisation test, the ielts.org 2023 sample tasks, IDP free practice / IELTS
Ready — plus a **re-use rule** (transcription pass around each answer; 1.25× speed
pass) and a rationing rule of one fresh part per session.
*Layer 2 — accent supply, unlimited:* one named free public-broadcaster source per
accent (BBC, ABC, RNZ, CBC, NPR), a transcript requirement, a named weekly rotation,
and a specific 10-minute exercise (60 seconds, write only numbers/dates/prices/proper
nouns, replay, check against transcript, log misses by accent).
*Layer 3 — his own dictator:* the OS text-to-speech voices every phone and desktop
ships, with the five regional English voices named, and a blind-typing drill built on
his own error log, the uncountables list and a shuffled `-teen`/`-ty` number set.
Layer 3 carries its **honest limit**: a synthetic voice never hesitates or
self-corrects, so it trains spelling, numbers and single-word perception only — trap
recognition must come from Layers 1 and 2.
Tip 9, L1 alert 6 (the `-teen`/`-ty` drill) and the Cross-training paragraph now point
at this section instead of naming an agent who does not exist. Self-test items 11 and
12 rewritten to be checkable.

**Source.** Official material `[src: T1 takeielts.britishcouncil.org — Free IELTS
practice tests]`, `[src: T1 ielts.org — Listening sample tasks 2023]`, `[src: T1
ielts.idp.com — Free IELTS practice tests]`. The broadcaster list is labelled
**[expert consensus]** in the text and explicitly flagged as not IELTS material and
not endorsed by any official body.

#### `[MAJOR]` `[V5]` — Ch2's Tips and Myths were the same content twice

**Issue.** Every Ch2 myth was the negation of a Ch2 tip, restated at full length with
the citation repeated — the chapter's own mark-budget table cited "Tip 1 / Myth 1",
"Tip 2 / Myth 10" for four of six rows.

**Change.** Both mandated sections kept. **Tips is now the canonical home**: each rule
stated once, with its source, and an intro saying so. **Myths keeps every entry** but
carries only what differs — the false belief, a pointer to the rule, *why the belief
survives*, and *what it costs*. Myths 1, 2, 3, 4, 7, 8, 9 and 10 lost their duplicated
rule statements and citations and gained a specific origin and cost; myths 5, 6, 11, 12
and 13 were already unique and are untouched. The mark-budget table now cites the tip
only.

#### `[CRITICAL, part]` `[V5]` — 60-second summaries moved to the top of both chapters

**Issue.** A reader on a 9-minute daily theory budget never reaches the end of a
chapter, which is where the summary sat.

**Change.** In both Ch1 and Ch2 the `## 60-second summary` section (heading name
unchanged, as mandated) now sits at the top, with the line *"Read this first."* A
one-line pointer replaces it at the old position. Ch1's summary text also had the
false "half-band thresholds are published nowhere official" claim, now replaced with
the real figures; Ch2's now states the published band ranges rather than "band 6 is 23,
band 7 is 30". Ch3 already had its summary at the top, so the book is now consistent on
this.

#### `[MINOR]` cluster — Ch1

- **Arithmetic slip `[V1]`.** French-L1 Reading−Writing gap corrected from 0.86 to
  **0.85** (7.006159 − 6.152480 = 0.854). `[src: ielts.org — Test taker performance
  data 2024-2025 (XLSX)]`
- **Writing timing `[V1]`.** "at least 150 words in about 20 minutes" → "at least 150
  words… no more than 20 minutes", matching the printed rubric, with the enforcement
  point kept separate. `[src: ielts.org — IELTS Academic: Writing test format]`
- **Cambridge is two-handed on under-length `[V1]`.** Added the other half of the
  quotation the book was omitting — "Don't write less than the required number of
  words" — with the note that neither statement is a tariff. `[src: cambridgeenglish.org
  — IELTS FAQs, Academic module (PDF)]`
- **Listening question types `[V3]`.** Ch1 enumerated all 11 Reading types and none of
  the 6 Listening types. The six are now named, with one sentence explaining why Ch2
  works through eleven layouts instead. `[src: ielts.org — IELTS Academic: Listening
  test format]`
- **"Rubric" glossed at first use `[V5]`.** Ch1's *copied rubric* myth now defines the
  word — the printed wording of the task: prompt, instruction line, chart title — which
  is the sense used everywhere else in the book.

#### `[MINOR]` cluster — Ch2

- **Mark budget promised seven and sourced six-to-nine `[V5]`.** Reframed as "here is
  where six to nine of those marks are", with the missing sentence added: fix every row
  and you clear the gap with margin; fix half and you do not. The seven-mark climb is
  now correctly attributed to the *floor* of band 6, alongside the one-mark step from
  the top of 6.5.
- **The summary introduced two traps found nowhere in the chapter `[V5]`.**
  *proposed* ≠ *actual* and *modern* ≠ *recently opened* are now trap **(d) the status
  word** in §2 Note completion, with an original worked example. The summary now points
  at something.
- **Summary-completion example contradicted its own rule `[V4]`.** Added the decision
  procedure: this is the rare forced conversion because the noun is genuinely absent;
  if you can hear the noun anywhere, write that instead.
- **Short-answer example bolded answers that breach its own word limit `[V4]`.** The
  keyed answers `(main) reception` and `(the) noticeboard` are now printed, with the
  word counts that make the spoken phrases zeros.
- **"Distractor" used but never defined `[V5]`.** Glossed at first use in §9 Matching.
- **Official sample PDF's own 5-vs-6 type discrepancy `[V3]`.** Recorded: the 2023
  Listening sample tasks preamble lists five types and then ships a short-answer task
  and key; the format page's six is authoritative. `[src: T1 ielts.org — Listening
  sample tasks 2023]`
- **False-friend duplication `[V5]`.** Ch2's list keeps only the Listening-specific
  consequence (in Writing it costs a fraction of a criterion; in a gap it is the whole
  mark) and points to Chapter 8 for the full annotated list.
- **"Six named types; four are one family"** corrected to "one of them is a family of
  completion layouts", which is what the format page actually shows.

#### Judged NOT to change

- **Ch3's Reading table, and Ch3's 16/40 band-5 anchor.** Correct table, wrong anchor —
  but Ch3 belongs to another agent. Ch1 is already right (15) and now states the
  asymmetry explicitly, so the two will reconcile when Ch3 is fixed.
- **The mandated "Question types, one by one" heading in Ch1.** V5 (MINOR) proposed
  renaming it, since Ch1's "types" are the four papers. The fix brief requires every
  mandated H2 to survive verbatim, so the heading stays and the one-line framing
  sentence with it.
- **Ch2's `ONE WORD ONLY` hedge itself.** V1 tried to break it and could not; the
  phrase genuinely does not appear in any official Listening document. Only the missing
  Reading contrast was added — the hedge is correct and stays.
- **The `[expert consensus]` and `[verified]` labels throughout Ch2's tips.** They are
  accurate and the reader relies on the distinction; the dedupe did not touch them.
