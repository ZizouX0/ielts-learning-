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

### Chapter 3 — fix agent

Scope: `chapters/03-reading.md` only. Every factual change below was re-verified by
fresh fetch on 2026-07-31, not taken from the research notes.

#### `[CRITICAL]` `[V4]` — the Y/N/NG "scope mismatch" example was keyed wrong, and the error had been generalised into doctrine

**Issue.** The Type 3 mini-example gave a passage stating a figure about *managerial
staff*, a statement generalising it to *employees*, and keyed it **NO — scope
mismatch**. Nothing in the passage confirmed or denied the wider claim, so by the
chapter's own step 7 (*"can I put my finger on a sentence…? NO → NOT GIVEN. Stop."*)
the answer is **NOT GIVEN**. It was wrong a second way: in a **Y/N/NG** set the object
judged is the writer's view, and a statistic is not a view — the item was mis-cast as
Y/N/NG in the first place. The same error appeared as a row of the qualifier table
("deaths in general / deaths from one cause → FALSE") and as a flat assertion in the
60-second summary ("A scope mismatch is FALSE").

**Change — all three locations, plus the underlying rule.**
- **Type 3 mini-example replaced** with an original one built on an opinion piece about
  library opening hours, giving five shapes: **NO** (the writer names an argument and
  says it *"gets the causation backwards"* — a contradiction of a stated view),
  **YES** (paraphrase of a claim marked *In my view*), **NOT GIVEN / adjacent
  proposition**, **NOT GIVEN / attribution gap**, and **NOT GIVEN / population gap**.
  Every YES and NO item now targets an actual claim by the writer.
- **The two cases are now distinguished explicitly**, because the old text collapsed
  them: vague-or-narrow in the passage against precise-or-wider in the statement is a
  **gap → NOT GIVEN**; a scope mismatch where the passage says something about the part
  the statement adds, and it goes the other way, is a **contradiction → FALSE / NO**
  (worked on original material: *"only in Scotland"* vs *"nowhere in the UK"*).
- **Qualifier table:** the single bad row is replaced by **two** rows — scope mismatch
  *gap version* → NOT GIVEN, scope mismatch *contradiction version* → FALSE / NO — and
  a paired worked demonstration follows the table, ending on the discriminator: *has
  the writer said anything about the part the statement adds?*
- **60-second summary:** "A scope mismatch is FALSE" → "**A scope mismatch is NOT GIVEN
  too** — unless the text explicitly rules the statement's population out."
- Self-test gains item 17 on exactly this decision.

**Source.** No new external source needed — the fix is the chapter's own step-7
procedure applied consistently, which is itself sourced to `[src: britishcouncil —
T/F/NG PDF, Worksheet 3 Ex.1 + key]` and corroborated by `[src: ielts.idp.com —
Examples of how to use 'not given']` (*"'False' and 'No' can be proven… there is
evidence in the article"*).

#### `[CRITICAL]` `[V1]` `[V4]` `[V5]` — matching-headings order, stated three incompatible ways

**Issue.** The order table said "questions yes, numerals no"; Tip 4 listed type 5 among
the types where order *fails*; the 60-second summary put matching headings in the "not
ordered" list. Three answers to one question, and the summary is the part the reader
re-reads before a drill.

**Change.** One position, stated identically in all four places (order table row 5,
Type 5's *Order:* line, Tip 4, 60-second summary): **the questions run one per paragraph
in paragraph order — work the paragraphs top to bottom — and the Roman numerals do not,
so never expect heading (i) to belong to paragraph A.** The chapter's old hedge ("that
reading is not certain") is replaced by the evidence, because a fresh fetch settled it.

**Source.** The ambiguous official note is *"NB The answers are NOT in the same order as
the text"* `[src: britishcouncil — Dealing with Matching Headings questions (PDF), p.2]`.
Two things disambiguate it: (a) the **same document's** teacher's notes tell the class to
notice that the *list of headings* is *"not in text order, use of roman numerals, and
there are more headings than paragraphs"* `[src: same, Exercise 5]` — it is the headings
that are shuffled; (b) the official 2023 sample task numbers its questions one per
section **in section order**, with one section done as the Example, while the numerals
awarded are scattered across the list `[src: ielts.org — Academic Reading Sample Tasks
2023 PDF]`. ielts.org's format page says nothing about the order of this type, and the
chapter now says so rather than implying an official statement exists.

#### `[MAJOR]` `[V4]` — Reading band-5 anchor was 16; it is 15

**Change.** "8 → 35, 7 → 30, 6 → 23, **5 → 15** out of 40", with the added half-sentence
that the band-5 figure is the *only* difference between the Academic Reading and
Listening conversions (Reading 15, Listening 16); from band 6 up they are identical. The
chapter's own nine-row table already said 15–18 = band 5, so the cross-check now actually
cross-checks.

**Source.** `[src: britishcouncil — IELTS Guide for teachers (PDF), p.10]`, PDF fetched
and text-extracted 2026-07-31 — the anchor table reads 8/35, 7/30, 6/23, 5/15 for
Reading and 5/16 for Listening. The chapter's two `p.7` citations for this document were
also corrected to **p.10**, which is where the scoring section actually sits.

#### `[MAJOR]` — the half-band table is KEPT, with explicit sourcing

**Change.** The nine-row table stays as published fact (Ch1 and Ch2 are being corrected
to match). Added a paragraph naming the source explicitly and quoting its caveat
verbatim, plus the co-owners' equivalent statement from the other direction, and the
operating rule: *whole-band rows are hard anchors, half-band rows are a published
average, neither is a guarantee for your particular paper — use the table to set a
target, never to argue you "should have got" a band.*

**Source.** `[src: ielts.idp.com — IELTS Reading band scores]`, fetched 2026-07-31:
9 = 39–40, 8.5 = 37–38, 8 = 35–36, 7.5 = 33–34, 7 = 30–32, 6.5 = 27–29, 6 = 23–26,
5.5 = 19–22, 5 = 15–18 — matching the chapter row for row. Caveat quoted verbatim
(*"the average number of marks needed… actual scores may differ slightly between
tests"*), corroborated by `[src: britishcouncil — IELTS Guide for teachers (PDF), p.10]`
(*"the Band 6 boundary may be set at a slightly different raw score across individual
tests"*).

#### `[MAJOR]` — "exactly three marks" was arithmetic the table does not support

**Issue.** With 6.5 = 27–29 and 7 = 30–32, "6.5 → 7.0 is exactly three marks" is true
only from the floor of 6.5. From 29 it is one mark.

**Change.** Heading restated as **"Band 7 starts at 30. From the floor of 6.5 that is
three marks; from the top of it, one."** followed by a three-row table (27 → 3, 28 → 2,
29 → 1) and the framing that **three marks is the worst case and the number to plan
against**. The 60-second summary carries the same arithmetic. The rest of the section —
which is about *where* the three marks are — is unchanged, because it was right.

#### `[MAJOR]` `[V3]` — Reading multiple choice with more than one answer had one subordinate clause

**Issue.** The multi-answer variant was disposed of in half a sentence, although it
ships as its own official sample task with its own answer key, and Chapter 2 gives the
Listening equivalent a full section.

**Change.** Type 1 is now explicitly two forms. **Form A — one answer** is the old
content, intact. **Form B — more than one answer** is a new full-mandated block:
appearance (lead-in, *"Choose TWO letters, A–G"*, *"Write the correct letters in boxes 1
and 2"*); a five-row rules table contrasting it with form A (longer option list, **two
question numbers, two marks — one per letter**, either order accepted, *mentioned by the
writer* rather than *true*); the trap (an **exclusion sweep** across a long list whose
wrong options are true-of-the-world and simply never said — plus the mechanical trap
that the two correct letters need not appear in passage order, which the official sample
demonstrates); a five-step technique; an original mini-example (parish-register
volunteers, six options, key **B and D**, with the two plausible-but-unstated decoys
identified); and two band-6 mistakes — **writing one letter for a two-mark item**, and
treating it as two independent one-answer questions. The order line and the order table
row now distinguish where the *item* sits from the order of the *letters*. Self-test
gains item 16.

**Source.** `[src: ielts.org — Academic Reading Sample Tasks 2023 PDF]`, fetched and
text-extracted 2026-07-31: it ships *Multiple Choice: more than one answer* as a separate
sample task with two consecutive items (A–G and A–F), and its key prints *"1&2 IN EITHER
ORDER"* and *"3&4 IN EITHER ORDER"*. Also `[src: ielts.org — Reading test format]` for
*"Sometimes you are given a longer list of possible answers…"*.

#### `[MAJOR]` `[V5]` — 60-second summary moved to the START

**Change.** `## 60-second summary` (heading name unchanged, as mandated) now sits
immediately after the chapter's originality header, opening with *"Read this first"* and
naming the two sections worth the reader's nine minutes. A one-line pointer sits at the
old position, after the self-test. The summary text was rewritten for every fix in this
entry: band arithmetic, matching headings, scope mismatch, and a new clause on the
two-mark multiple-choice form.

#### `[MINOR]` `[V1]` `[V4]` — `ONE WORD ONLY`, Reading vs Listening

**Change.** A callout under Type 8 states the position plainly: the wording is **verbatim
official in Academic Reading** (twice in the 2023 sample tasks — a Sentence Completion
set and a Summary/Notes Completion set), and Chapter 2's finding that it could not be
verified for **Listening** is also correct. Two papers, two findings, no contradiction.

**Source.** `[src: ielts.org — Academic Reading Sample Tasks 2023 PDF]` (both instances
located in the extracted text) and `[src: ielts.org — Listening Sample Tasks 2023 PDF]`
— independently re-extracted: the phrase does not occur, and the only word-limit wordings
present are `NO MORE THAN THREE WORDS AND/OR A NUMBER` and `NO MORE THAN TWO WORDS`.

#### `[MINOR]` cluster — Chapter 3

- **T/F/NG mini-example taught word-matching `[V4]`.** The item *"The word 'floor'
  appears in the sentence" → TRUE* verified typography, not information, and modelled the
  exact habit Myth 8 exists to break. Replaced: passage *"occupies the top floor of the
  four-storey annexe"*, statement *"is on the fourth floor"* → **TRUE**, with the point
  made explicitly — not a word of the statement appears in the passage; the information
  does.
- **Order-table caveat overstated ielts.org `[V1]`.** The page states an order rule in so
  many words for **4** types, not 6. Corrected, and types 9 and 10 now carry the page's
  actual opposite wording, quoted. `[src: ielts.org — Reading test format]`
- **"Front-loaded" described a back-loaded split `[V4]`.** 16/19/21 gives Passage 3 the
  most time. Now "a **back-loaded** split — roughly 17 / 19 / 21, plus the three-minute
  sweep" (which also fixes the missing minute), with a clause tying it to Myth 13.
- **Word-bank example's key was not licensed by its text `[V4]`.** *Absconding
  apprentices* carry knowledge deliberately, so "accidental" did not follow. Text
  rewritten to *"it travelled by chance contact between crews wintering in the same
  harbour"*, bank option B changed from *costly* (which did not fit the slot, breaking the
  "all options fit grammatically" claim) to *official*.
- **Diagram example justified itself with text it did not print `[V4]`.** The decoys are
  now in the quoted text (*a brass bezel… a brass pin…*), so *brass* genuinely fails to
  discriminate and *immediately below* genuinely does the work.
- **"Academic items are pitched at bands 5–8" dropped a qualifier `[V1]`.** The source
  says the Academic paper has *"more items pitched at bands 5–8"* than General Training
  does — a distribution claim, not a floor. Restated, conclusion unchanged.
  `[src: britishcouncil — IELTS Guide for teachers (PDF), p.4]`
- **"Distractor" used but never defined `[V5]`.** Glossed at first use in Type 1.
- **"Rubric" glossed `[V5]`.** Type 6 now says what the word means in this chapter — the
  printed instruction line above a set of questions.
- **False-friend duplication `[V5]`.** The 12-row table is kept, because its fourth
  column (*what the misreading costs you on the answer sheet*) is Reading-specific and is
  the part worth memorising here; a pointer to Chapter 8's full annotated list is added
  above it.
- **Multiple-choice order quotation replaced** with the wording actually on the ielts.org
  format page.

#### Judged NOT to change

- **The half-band raw-score table.** V4 read it as a contradiction of Ch1 and proposed
  labelling every half-band row *(interpolated — not official)*. V1 re-fetched and found
  the opposite: IDP publishes it, and it matches this chapter row for row. Ch1 and Ch2
  are being corrected to match Ch3, not the other way round. Kept, with sourcing and
  caveat strengthened instead.
- **Order-table row 4 (matching information → NO).** Still the weakest row in the table
  and still unsupported by any official statement. It stays as it is, including the
  honest admission and the structural argument, because the chapter already says the
  cost of being wrong here is zero.
- **Type 5's "it always comes first" claim.** Re-verified verbatim on fresh fetch —
  *"if it is on a Reading test, it will be the first set of questions in the section"* —
  so it stays. `[src: ielts.org — News & Insights: matching headings]`
- **Myth 2 (NOT GIVEN as safest blind guess) and Myth 14 (the fabricated Cambridge
  statistic).** Both refuse to publish an unsourced number and both were confirmed clean
  by V1 and V5. Untouched.
- **The three-passage timing baseline of 19/19/19 + 3.** V4's only complaint was the
  mislabelled alternative split, now fixed; the baseline itself is derived from the
  official *"about 20 minutes on each text"* and stands.

---

### Chapters 4 and 5 — Writing Task 1 and Task 2

#### `[CRITICAL]` `[V3]` — Task 1 had no section for a static, non-process diagram

**Issue.** Chapter 4 quoted the official rubric — *"a diagram of an object, device,
process or event"* — and then built an eight-way split in which **every** diagram
was a process. A static input (two devices compared, a labelled cross-section, a
diagram of an event) has **no time axis**, so the trend toolkit is illegal, and **no
sequence**, so the process toolkit does not apply. The reader would have met this
task with two toolkits and neither of them usable, and the chapter's own
tense-by-visual table had no row for it.

**Change.** New **§9 — Static diagram (an object, a device, or an event)**, carrying
the full mandated treatment: what it looks like (three shapes); the two-absence
recognition test; why *no trend verb applies* and why process sequencers invent an
order that is not there; the structure table; the rule to **group by function or
component across both objects, never object by object**; tense (present simple,
largely active, past for a historical artefact); three separate language sets (parts
and their function · spatial relationships · comparison between two objects); two
traps (the label inventory, and commentary); an **original** worked mini-example
(two designs of a hand-operated well pump) with a counted 51-word overview; and the
band-6 mistake. Also added: two new rows to the tense-by-visual table, a self-test
item, a line in the 60-second summary, and — per V3's MINOR — a paragraph unpacking
*"or other visual input"* as a **two-question classifier** (time axis? sequence?)
that handles an input with no name in the chapter. The preamble's "eight-way split"
is now a nine-way split.

**Source.** `https://ielts.org/take-a-test/test-types/ielts-academic-test/ielts-academic-format-writing`
(re-fetched 2026-07-31: *"a diagram of an object, device, process or event"*) and
`https://ielts.org/cdn/ielts-guides/ielts-writing-key-assessment-criteria.pdf` p.2,
re-fetched and re-extracted 2026-07-31 — *"a diagram, graph, table, chart, map or
other visual input"*, and the TA bullet *"comparing or contrasting the information
by adequately highlighting the identifiable trends, principal changes or differences
in the data **and other inputs**"*. That last phrase is the load-bearing one: it
establishes that the comparison requirement is **not** limited to numeric inputs,
which is what makes a static diagram markable at all.

#### `[MAJOR]` `[V4]` — Chapter 4 marked a defining relative clause as an article error

**Issue.** Ch4's L1 alert listed *✗ the people who travelled by bus → people*. That
is not an error. Chapter 8's own rule names **a defining relative clause** as one of
the triggers that makes a noun specific and brings *the* back. Marking it wrong would
have trained the reader to strip an article from the exact slot the other chapter
tells him to restore it in.

**Change.** Replaced with genuine generics (*the people prefer cars* → *people prefer
cars*; *the cycling declined* → *cycling declined*) and added a short block stating
the real rule — *the* is only wrong on a **bare** generic — with a minimal pair
showing the same noun correct **with** the article once a defining clause specifies
it. Cross-referenced to Chapter 8 for the full trigger list. The genuinely correct ✗
examples (*the car use*, *the tourism*, *the electricity consumption*) are kept.

**Source.** Internal consistency with `08-grammar-L1.md` §L1 alert → "The rule that
stops the overcorrection"; no external claim involved.

#### `[MAJOR]` `[V4]` `[V5]` — a model overview claimed 45 words and was 34

**Issue.** Ch4 §1's line-graph overview was labelled "Forty-five words." Counted: 34.
In a chapter that instructs the reader to count his words every time, and that sets a
55–70-word checkpoint after the overview, a demonstration model with a wrong count
would have sent him ten words light while believing he was long.

**Change.** "**Thirty-four words** — counted, not estimated", plus the arithmetic that
reconciles it with tip 12's checkpoint (a 20–25-word introduction plus 34 lands
inside 55–70 with nothing to spare, which is the point). Every word count printed in
these two chapters was recomputed programmatically, not eyeballed.

#### `[MAJOR]` `[V4]` — the table model asserted a gap the table contradicts

**Issue.** Ch4 §4's band-7 exemplar said *"a gap of roughly forty-five points between
them **in every country**"*. Worked: Canada 96−51 = 45, Ireland 97−47 = **50**,
Portugal 89−39 = **50**. Two of three are 50. The chapter's own band-7 model would
have lost a TA accuracy mark, on the exact charge the chapter levels elsewhere
(*"Plummeted for a 3% fall is a TA accuracy error"*; self-test item 10, "Is every
figure correct?").

**Change.** Model rewritten to *"a gap of between forty-five and fifty percentage
points"*, and the three subtractions are now printed underneath with the general
lesson attached: **when an approximation has to cover several figures, check it
against the worst one, not the first one you looked at.** The error was turned into
the teaching point rather than quietly deleted.

#### `[MAJOR]` `[V1]` — the hedge on "limited to Band 5" is deleted; it is verbatim official

**Issue.** Ch5 carried the sentence with a caveat in *What is still unsettled*: reached
"through a rendering layer rather than read verbatim off the live page… pending
verbatim confirmation." V1's instruction was confirm-don't-downgrade, and it
confirmed.

**Change.** Re-fetched independently today and found it verbatim on the live page.
The caveat bullet is **deleted** from *What is still unsettled*. The in-chapter
passage now presents it as a block quotation of published fact with an inline source
and fetch date, notes that the bolded band-5 TR cell corroborates it independently
("two sources, one rule"), and adds the two other verbatim sentences the same page
supplies (the one-third / two-thirds weighting, and the official definitions of
*extend* and *support*). It is also promoted into the 60-second summary.

**Source.** `https://ielts.org/take-a-test/preparation-resources/writing-test-resources`
— re-fetched 2026-07-31, returning verbatim: *"If you don't discuss both, you will be
limited to Band 5."*

#### `[MAJOR]` `[V4]` — Chapter 5's article side-list put *government* on the wrong side

**Issue.** Ch5's drop-the-article list included *government (as an institution)* —
contradicting Chapter 8's counter-list, which exists specifically to stop that
over-correction, and contradicting Ch5 itself four sections later (*the government
decides*). The parenthetical made it worse: *as an institution* is exactly the sense
that **takes** *the*.

**Change.** *government* removed from the drop list. A full counter-list block added
in its place — *the government · the environment · the media · the economy · the
internet · the public · the police* **keep** their article; *society, technology,
nature, life, history* (and the rest of the drop family) do not — with *government*
called out by name as the trap on the list, a ✓ model sentence, and an explicit
statement that Ch5 §6 uses it correctly. Cross-referenced to Chapter 8 as the owner
of the counter-list and the decision procedure. Chapter 5 is now internally
consistent: all seven remaining uses of the word take the article or a bare plural,
both of which are correct.

#### `[V5]` — 60-second summaries moved to the START of both chapters

Both now sit immediately under the H1, keep the heading name, and open with "Read
this first" plus one line explaining why they are there (the nine-minute theory cap
means the end of a chapter is the one place the reader never reaches). Ch5's summary
additionally absorbs the promotion V5 asked for: the **four-move body paragraph**
(claim → because → so what → instance) was Tip 4, halfway down, behind five pages of
question families; it is now on the first page. Ch4's summary gains the
**time-axis-or-not** gate, which governs half the chapter's decisions.

#### Padding reduction `[V5]`

V5 quantified the false-friend list appearing in 8 of 9 chapters and the uncountables
list in 8. In these two chapters the rule applied was: keep what is load-bearing for
*this* skill, cut the rest to a pointer.

- **Ch4 uncountables** — the generic 16-word list replaced by the eight *industrial*
  uncountables a chart actually hands you, plus the two Task-1-only points that live
  nowhere else (**treat *data* as plural**, which matches the band-7 descriptor's own
  *"the data **are** appropriately categorised"*; and partitives for chart nouns).
  Full list → Chapter 8 §The nine words.
- **Ch4 false friends** — cut from ten to the **five that attach to a figure**
  (*significative · augmented · diminution · evolution · important*), with the reason
  they and not the others: Task 1's narrow lexical field means these recur four times
  a report. Full annotated list → Chapter 8 §French: 3.
- **Ch5 false friends** — cut to the four that change what an *argument* claims
  (*formation · evolution · inconvenient · société*) plus the two non-words, one of
  which is the official examiner's own cited example of L1 interference. Full list →
  Chapter 8.
- **Ch5 prepositions** — cut to the six that attach to the verbs of arguing, plus
  *prevent … from*. Full table → Chapter 8.
- **Ch5 uncountables** — list removed to Chapter 8; what stays is why Task 2 is where
  this bites (an abstract-argument essay is made of five of the nine words).
- **Ch5's four-pass proofread** — kept, because self-test 15 and the summary both
  depend on the four passes being named here, but Chapter 8 is now stated as the
  owner of the procedure, and the one rule Ch5 was missing is imported: **in the three
  minutes you may delete and repair; you may not add.**

#### `[MINOR]` items applied

- **`[V4]` `[V5]` Ch4's LR error count.** "Seven problems in thirty words" → the text
  is **28 words** and carries **eight** faults, now split by criterion: six against
  LR, and two against **GRA** — *a important* (determiner choice is grammar) and
  ***the** cycling*, the generic article, which is the book's flagship error and was
  missing from its own error list. Matches Ch7 and Ch8's allocation of articles to
  GRA. The unnamed tense clash (*who use* … *decreased*) is now called out too.
- **`[V2]` Ch4's band-8 CC row cited band 9's wording.** *"The reader follows with no
  effort"* is band 9 (*effortlessly*, cohesion that *very rarely attracts attention*).
  Band 8 row rewritten to *followed with ease · cohesion well managed*, with the
  band-9 wording named as band 9 so the reader stops aiming a band too high. The
  linker myth is corrected the same way and is now stronger: over-use is named at band
  6 **and** band 7, and nothing anywhere rewards quantity.
- **`[V2]` `[V4]` `[V5]` the "half your sentences error-free" collision.** Ch4 set the
  band-7 working target *at* a majority while Ch8 argues band 7 must sit *below* one.
  Ch4 tip 5 re-tagged `[expert consensus — derived]` (it was tagged `[verified]`,
  which it is not — no official source quantifies *frequent*) and restated as **four
  in ten rising to five**; the GRA 6→7 gate and self-test 15 follow. Ch5's decoder
  restated as **six of about sixteen** for band 7, nine or ten for band 8, with
  Chapter 8 named as the owner of the derivation.
- **`[V2]` Ch4 overstated the band-5 TA cell.** The word *overview* does not appear at
  band 5. Restated by paraphrase — *a tendency to focus on details without referring
  to the bigger picture* — with the conclusion (no overview ≠ below band 5) unchanged.
- **`[V4]` Ch5's five skeletons all overshot the chapter's own word target.** They
  summed to 295–305 against a stated 270–290. All five retrimmed to 280–285, each now
  printing its own total, and the asymmetries that carry an argument (Family 2's
  100/120, Family 4's weaker-side/stronger-side split) are preserved as 95/110 and
  90/110. Arithmetic re-verified programmatically.
- **`[V2]` Ch5's self-test enforced a 300-word ceiling its own M6 debunks.** Item 8 →
  *at or above 260, 270–290 comfortable, no upper limit beyond what you can proofread
  in three minutes*, with a pointer to M6 and an explicit instruction not to cut 320
  good words to hit a number the book never set.
- **`[V4]` Ch5's "five markers, four sentences"** described five sentences. Fixed.
- **`[V2]` criterion weighting cited to a document that does not state it.** The Key
  assessment criteria PDF names the four criteria and never mentions weighting. Ch5's
  table now sources the **names** to that PDF and the **equal weighting** to
  `ielts.org — Understanding and setting IELTS scores` (*"The criteria are weighted
  equally and the score on the task is the average"*), matching Chapter 1.
- **`[V2]` uncountables assigned to LR here and GRA in Ch8.** Standardised on Ch8's
  hedged version: **GRA, and arguably LR too** — IELTS files word formation under LR
  and does not say which side countability falls on. Stating a contested allocation as
  settled fact was the error, not the allocation.
- **`[V5]` undefined terms.** *collocation* now defined at first use, in Ch4's opening
  summary, with a minimal pair (*heavy rain* / *strong rain*); *participle clause*
  defined where the trend toolkit introduces it, with the reason it is the cheapest
  complex structure in Task 1.
- **`[V5]` the keyboard.** One line at the head of Ch4's 20-minute budget and inside
  Ch5's tip 13, pointing at Chapter 9's L1 alert — with the specific consequence
  spelled out in Ch5: nine words a minute assumes the layout you trained on, and the
  shortfall lands on Task Response.

#### Strengthened, not weakened

- **Ch5's bold-extraction analysis.** Confirmed independently twice (V2 and V1 both
  re-extracted the font runs; V1 recorded "I tried hard to break this and could not").
  It is **not** softened. It is expanded with the three details that make it
  reproducible by the reader: the PDF's own legend quoted, page 7 (bands 9/8/7)
  carrying **zero** bolds, page 9 dense with them — and the trap on page 8, where the
  band labels are **vertically centred**, so the two bolds that belong to the band-5
  row sit level with the *6*. Chapters 7 and 8 are being corrected to match this
  chapter, not the other way round.

#### Judged NOT to change

- **Ch4's 17-minute Task 1 stop time vs Ch8's 18.** `[V4-MINOR]` A real
  inconsistency, but it cannot be fixed from inside Chapter 4: whichever number this
  agent picks has a 50% chance of colliding with the Chapter 8 agent's choice in the
  same pass. Ch4's table is internally coherent (write to 0:17, check 0:17–0:20) and
  is left alone. **Flagged for a single owner to settle across Ch4, Ch8 and Ch9 after
  this pass** — one number, three chapters.
- **Ch5's copied-rubric section and Ch4's parallel passage.** `[V5]` flagged "copied
  rubric" as appearing in five chapters and proposed stating the mechanism once in
  Ch1. Both passages are kept at length here, because in these two chapters the point
  is not a repeated warning — it is **arithmetic the reader has to be able to do
  himself** (Ch4: copy a 20-word title plus a 17-word instruction from a 175-word
  report and you submitted 138; Ch5: copy a 25–45-word prompt into a 265-word essay
  and your counted length is 225–240 while the on-screen counter says you are fine).
  Deduplicating that into a cross-reference would remove the only place the reader
  sees the numbers for his own task. The generic *why it is penalised* material is
  what carries the duplication, and it is already short in both.
- **Ch5 M7, M6 and the length argument in §Length.** They look like three statements
  of one point, but they are three different claims — no published tariff (M7), no
  published ceiling (M6), and the structural bold-extraction proof (§Length) — and
  only the third is original to this book. Kept.
- **Ch4's `(T1 + 2×T2) ÷ 3` estimate.** V1 checked for a published combination
  arithmetic and found none, and endorsed printing it as a labelled estimate.
  Untouched.
- **Ch5's "no official taxonomy of Task 2 essay types" framing**, stated in the
  preamble and again as M12. V3 marked both as correct and the duplication is
  load-bearing: the preamble governs how the five families are read, and M12 is where
  a reader who learned the families elsewhere will look. Kept.
