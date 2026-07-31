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

---

### Chapters 8 and 9 — grammar/L1 and study plan/test day

Fix agent scope: `08-grammar-L1.md`, `09-studyplan-testday.md`.

#### `[MAJOR]` `[V2]` `[V1]` — Chapter 8 asserted a descriptor clause is printed in bold. It is not.

**Issue.** Ch8's Band descriptor decoder stated: *"The band-6 accuracy cell is set in
bold in the original, and the PDF's own legend reserves bold for negative features
that limit a rating."* The error map repeated the premise ("a multiplier where the
descriptors bold it as a limiter"). Chapter 5 states the correct fact and invites the
reader to verify it by font extraction — so a reader who followed Ch5's instruction
would have caught the book contradicting itself.

**Verification.** Re-downloaded `ielts-writing-band-descriptors.pdf`
(`CreationDate D:20230503120242`) and extracted per-character `fontname`. On the two
pages covering bands 6 and 5, the entire bold inventory is at **band 5**:
*"incompletely addressed."*, *"Paragraphing may be inadequate or missing."*,
*"There may be no data to support the description."* The band-6 GRA accuracy clause
and the band-6 LR risk-taker clause are `OpenSans-Regular`. The page covering bands
9, 8 and 7 carries no bolded body text at all. This reproduces V2's and V1's findings
independently.

**Change.** The bold claim is deleted and replaced with what the text actually is: a
**positive-feature description** of band 6, binding because the grid's header rule
requires a script to *fully* fit a level's positive features. The correct bold
inventory is printed so the reader can check it, and the underlying advice — close the
accuracy gap, do not add complexity — is untouched, because it never depended on the
typography. The error map's ranking principle loses the bold multiplier.

**Source.** `[src: ielts.org — Writing band descriptors (PDF, Updated May 2023), pp.4
and 8; per-character font extraction, fetched 2026-07-31]`

#### `[MAJOR]` `[V2]` — Chapter 9 coached a sub-6.0 reader into exactly what Chapter 8 debunks

**Issue.** The 10-week plan (explicitly *"for a starting point below 6.0"*) set week 3
as *"Band 7 GRA needs a range of complex forms, not error-free simple ones"* with the
milestone *"Every essay contains 4+ correctly formed complex sentences"*, and the
decoder's step 2.4 said *"band 7 wants range, not merely accurate simple sentences."*
Ch8's Myth 1 debunks the first and Myth 2 debunks numeric complexity quotas by name.
Ch9 is the artefact the reader executes daily, so it would have beaten Ch8 in practice.

**Change.** The quota is deleted. Week 3 now drills **three** structures to control
rather than a large set to coverage, and its milestone is a **ratio of error-free
sentences**, not a count of clauses. A warning block above the 10-week table states the
mechanism: band 6 already credits a mix of simple and complex forms, so the gate is the
next clause — complex structures *not marked by the same level of accuracy as in simple
structures* — and band 7 requires variety **and** frequent error-free sentences,
conjunctively. Decoder step 2.4 now scores the ratio first and reads the two numbers in
that order. The 2025 Speaking change is noted: *complex* was dropped from the band-7
range clause and simple sentences used effectively are explicitly endorsed.

**Source.** `[src: ielts.org — Writing band descriptors (PDF, Updated May 2023),
pp.1, 5, 9]` `[src: ielts.org — Speaking band descriptors (PDF, created 2025-09-16)]` —
both re-downloaded and the band 5/6/7 GRA cells re-extracted, 2026-07-31.

#### `[MAJOR]` `[V5]` — Chapter 1's strategy and Chapter 9's timetable were never reconciled

**Issue.** Ch1 argues the cheap marks are in Listening and Reading; Ch9's rotation gives
Writing three days and Reading one. Both are individually right and the reader was left
to resolve them by mood.

**Change.** §Why Writing gets the most time is renamed *"— and how that squares with
Chapter 1"* and states it: Writing is a **gate** (statistically weakest, fails the
application outright below 6.5, moves in weeks), Listening and Reading are **levers**
(technique converts in sessions, which is *why* Ch1 calls those marks cheap). A
three-line decision rule for a spare hour is added. Ch1's caveat is carried across:
Arabic-L1 Listening (5.70) sits 0.40 **below** Arabic-L1 Reading (6.10) while French-L1
Listening and Reading sit level (6.95 / 7.01), so the two L1 profiles disagree about
which receptive paper is cheap — **diagnose before allocating**, which is also why plan
selection moves to day 8.

**Source.** `[src: ielts.org — Test statistics → test taker performance data 2024–25]`
(figures re-checked against Ch1's table, which V1 verified against the spreadsheet).

#### `[MAJOR]` `[V5]` — Chapter 9 reintroduced a study partner Chapter 6 admits does not exist

**Issue.** Decoder Step 4 offered only one route to assessing Pronunciation — 25% of the
Speaking band — *"play a recording to a fluent English speaker"*. Ch6 is honest that the
reader is solo, so Pronunciation silently dropped out of the plan.

**Change.** Replaced with two genuinely solo procedures: the Ch6 three-target recording
review (speech rate, stress-timing, chunking), and a speech-to-text proxy — dictate the
recording back and treat the words the recogniser gets wrong as the words a listener has
to work for, tracked weekly on the same passage. Its crudeness is stated. The fluent
speaker survives as a bonus, not the method.

#### `[CRITICAL]` `[V5]` — 70,000 words of book against a 9-minute daily theory cap, with no reading plan

**Issue.** Reading this book once consumes the entire theory budget of the plan Ch9
itself sets, and nothing told the reader which 10% to read first.

**Change.** New §How to read this book inside the nine-minute rule: a day-zero setup
block explicitly outside the cap (all nine 60-second summaries, Ch1 §The strategic core,
Ch8 §The spine and §Your error map, Ch9's plan tables); a day-by-day table naming **one
section** per skill day; and an explicit read-once / skim-on-demand / keep-open-beside-
the-keyboard split. It also states plainly that the book is not to be read straight
through. Rule 4 of the six rules is restated as "nine minutes, from one named section".

Chapter 8 gets the matching artefact — §How to use this chapter — ordering its own
sections by value (error map → article material → three-minute self-edit → the eight
structures last), plus a gate at the head of the structures section: do not start it
until article error rate is under 10%, because every structure there creates new article
decisions.

#### `[MAJOR]` `[V5]` — the spaced-repetition ladder had no mechanism and `/anki` went unmentioned

**Change.** Ch9's rotation now carries a full command table for all eleven repo commands
(`/writing1` `/writing2` `/speaking` `/reading` `/listening` `/vocab` `/mock` `/official`
`/review` `/handbook` `/anki`), saying what each is for and when it fires. `/anki` is
added to the Sunday row with the running instruction: keep items in
`progress/vocab-bank.md`, export on Sunday, let the app compute the ladder — with a
five-envelope paper fallback for anyone who prefers it. A "miss a day, never double up"
catch-up rule is added.

#### `[MAJOR]` `[V5]` — AZERTY was flagged as the biggest unpublished risk, then given no procedure and no time

**Change.** New §The keyboard plan in Ch9's L1 alert: (1) test first — 250 words timed on
QWERTY, and above 20 clean words a minute there is no problem, stop; (2) below that it is
a week-1 task, 20 minutes a day for ten days *on top of* the 90, never inside the
practice slot, because a timed essay written while fighting the keyboard corrupts
`band-tracker.md`; (3) buy the layout, not the willpower; (4) re-test in week 3 and drill
punctuation keys specifically. Budgeted explicitly at ≈3.5 hours in weeks 1–2.

#### `[MAJOR]` `[V1]` — the "stale French translation" diagnosis of the Tunisia paper option does not hold

**Issue.** Ch9 attributed the paper-versus-computer conflict to a lagging French
translation, and the L1 alert generalised it into a rule ("where the French and English
versions disagree, the English one is more likely current").

**Verification (fresh fetch, 2026-07-31).** britishcouncil.tn's **English** IELTS Academic
page says *"You can choose between IELTS on paper or computer"* and quotes
*"Paper-based: 750 TND"*; the English General Training page quotes the same paper fee. The
English dates/fees/locations page offers only IELTS on computer and IELTS Online. So the
site is internally inconsistent **within English**, and the translation-lag diagnosis is
unsupported.

**Change.** Both passages rewritten honestly: the conflict is real, it is not
French-versus-English, the website cannot settle it, and the rule is *phone the centre and
confirm on the booking confirmation*. The chapter's conclusion — book computer at a centre
— is unchanged and unaffected; paper is retired from mid-2026 either way.

**Source.** `[src: britishcouncil.tn/en — IELTS Academic]`
`[src: britishcouncil.tn/en — IELTS General Training]`
`[src: britishcouncil.tn — Test dates, fees and locations]` — all fetched 2026-07-31.

#### `[MAJOR]` `[V1]` `[V4]` — 2h45 versus 2h40

**Change.** Ch9 now states both published figures and invents no reconciliation between
them: 2h40 is the Listening + Reading + Writing session, published **with no
delivery-mode caveat**; 2h45 is the total test time for IELTS Academic quoted alongside
the four component timings including Speaking. The chapter notes that the computer
components sum to roughly 2h32 and tells the reader to practise against 2h40 seated and to
budget the individual paper timings.

**Source.** `[src: ielts.org — What to expect on IELTS test day]` (*"This takes 2 hours 40
minutes, and there are no breaks between each section of the test"*, no mode caveat) and
`[src: ielts.org — IELTS Academic test]` (*"The test time is 2 hours and 45 minutes"*) —
both fetched 2026-07-31.

#### Smaller corrections applied

**Chapter 8**
- **Criterion weighting re-sourced `[V2]`.** "A quarter of every Writing task" was cited
  to the Key assessment criteria PDF, which never mentions weighting. Now cited to
  `[src: ielts.org — Understanding and setting IELTS scores]`, matching Ch1.
- **Band 8's modal restored `[V2]` `[V4]`.** Band 7 says a few basic errors *persist*;
  band 8 says a few *may* persist. The prose dropped the modal and the Speaking table
  omitted the clause from band 8 entirely. Both fixed, and the *a few* quantifier is now
  read as a **density** claim against the official error-density criterion, with the 70.6%
  band-6 third-person `-s` rate as the threshold.
- **Myth 3 scoped `[V2]`.** *Complex* was dropped from the **Speaking** band-7 range
  clause only; Writing band 7 still reads *"A variety of complex structures is used with
  some flexibility and accuracy"*. The myth previously licensed short **Writing** sentences
  from a Speaking descriptor. Verified by re-extraction of both PDFs.
- **Uncountables allocation hedged `[V2]`.** Error map row 4 is now "GRA, and arguably LR
  too", with the note that IELTS files word formation under LR and does not say which side
  countability falls. The book previously stated a contested allocation as settled.
- **Band-5 row added to the Writing GRA decoder `[V3]`.** The decoders stopped at band 6
  and the reader's baseline is undiagnosed. Wording taken from the re-extracted band-5 GRA
  cell.
- **First conditional un-filed from the second-conditional section `[V4]`.** *If the
  subsidy will end…* is a first conditional; it now sits in a one-line note about the
  shared no-modal-in-the-*if*-clause rule, so the section keeps one pattern.
- **Task 1 stop time aligned to 17 minutes `[V4]`** (was 18, against Ch4's 17), pointing at
  Ch9's new canonical numbers table.
- **Band-7 error-free ratio quantified `[V4]` `[V2]`** as four in ten rising to five, so
  Ch4, Ch5 and Ch8 carry one figure rather than three.
- **60-second summary moved to the top `[V5]`**, the duplicated opening data folded into
  it, and the section kept under its mandated heading.

**Chapter 9**
- **60-second summary moved to the top `[V5]`** and rewritten to carry the corrected
  figures.
- **New §The numbers, in one table `[V5]`** — the canonical clocks and word counts for the
  whole book (T1 3/12/3, stop 17, 170–190, floor 150; T2 5/32/3, stop 37, 270–290, floor
  250), so no chapter has to be adjudicated against another.
- **Study-plan hour totals corrected `[V4]`** from 54/72/90 to **63/84/105** — the rotation
  works seven days, including the Sunday review.
- **Plan selection de-circularised `[V5]`.** The rule refers to four sections; week 1 is
  identical in all three plans, so the choice is now explicitly made on **day 8**.
- **8-week week 3 body paragraph `[V2]`** changed from *claim → explain → example* to
  **claim → because → so what → instance** (Ch5 Tip 4). The dropped *so what* is the
  consequence step that separates band 6 from band 7 on Task Response.
- **"Writing is sat at the two-and-a-half-hour mark" `[V4]`** → sat in the **last hour** of
  the block, starting at roughly 1h32. The breakfast argument is unaffected.
- **Pen-or-pencil downgraded from "genuine unresolved conflict" `[V1]`.** The British
  Council rule is explicitly scoped to *"your IELTS on Paper test"*; Cambridge answers a
  different question. Both are about paper and neither applies to a computer candidate.
  `[src: takeielts.britishcouncil.org — Test day advice, fetched 2026-07-31]`
- **New bullet on coach-versus-book disagreement `[V5]`.** When an AI coach contradicts a
  rule here, ask it to quote the official document; if it cannot, the book's sourced
  version stands; if it can, log it.
- **New §The night-before checklist `[V3]`** — fifteen tickable lines, distinct from the
  existing preparation audit.
- **L1 alert de-duplicated `[V5]`.** The interference material is cross-referenced to
  Chapter 8 rather than partially restated; only the test-day-specific consequence (the
  sweeps fit inside the checking window) is kept here.

#### Judged NOT to change

- **Ch9's refusal to treat "a re-mark can only go up" as verified.** V1 confirms only IDP
  states it; ielts.org and the British Council are silent, and the BC terms page returns
  HTTP 403. The hedge is correct and stays exactly as written.
- **Tunisia fees (750 / 820 / 640), the six-week EOR deadline, the 60-day One Skill Retake
  rule, and every IELTS Online claim.** V1 verified all exact against live sources. Left
  untouched.
- **The Cambridge IELTS 21 publication-date hedge.** V1 hit the same HTTP 403 at
  cambridge.org and explicitly recorded that the hedge should not be tidied into an
  assertion. Kept verbatim.
- **Chapter 8's ~90 wrong→right pairs.** V4 worked every one individually and found each
  genuinely wrong and genuinely right. Not touched, and the full L1 treatment stays here:
  Ch8 is the canonical home for the false-friend, uncountables, preposition and article
  material, so the cross-cutting de-duplication removes copies elsewhere, never here.
- **Physical reordering of Chapter 8's H2 sections.** V5 proposed promoting the error map
  and article material above the eight structures. The value is real, but reordering
  mandated H2 sections in one chapter alone would break the book-wide section order that
  V4 exists to protect, and other agents hold live cross-references into this chapter by
  section name. Solved instead by moving the 60-second summary to the top, adding §How to
  use this chapter as an explicit value-ordered reading route, and gating the structures
  section — same navigational effect, no structural risk.
- **The mandated "Question types, one by one" heading in both chapters.** V5 wanted it
  renamed to describe its contents. The heading is mandated across all nine chapters;
  renaming it in two would cost more consistency than it buys.

---

### Chapters 6 and 7 — Speaking and Vocabulary

Scope: `chapters/06-speaking.md` and `chapters/07-vocabulary.md` only. Both PDFs
re-fetched and re-extracted by this agent on 2026-07-31 rather than taken from the
audit reports.

#### `[MAJOR]` `[V2]` `[V1]` — Chapter 7 asserted three times that descriptor clauses are printed in bold. They are not.

**Issue.** Ch7 claimed the band-6 risk-taker clause (opening, and 60-second summary)
and the band-4 memorised-chunks clause (Myth 3) are set in **bold**, and that bold is
IELTS's marker for rating-limiting features — so the clauses were being presented as
hard limiters. Myth 1 repeated it. The Band descriptor decoder header also asserted
the bold rule "applies throughout", which in the LR column it does not.

**Independent verification.** `ielts-writing-band-descriptors.pdf` downloaded and every
character's `fontname` inspected. The complete `OpenSans-Bold` body-text inventory is:
p.4 (T1 bands 6/5) *"There may be no data to support the description."* — **band 5 TA**;
p.8 (T2 bands 6/5) *"incompletely addressed."* — **band 5 TR** — and *"Paragraphing may
be inadequate or missing."* — **band 5 CC**. The pages covering bands 9/8/7 (pp. 3 and 7)
contain **no bold body text at all**. Nothing at band 6, nothing at band 4, nothing in
any Lexical Resource cell above band 5. Chapter 5's analysis is confirmed for the third
time and is **not** contradicted anywhere in Chapter 7.

**Change.** All four assertions removed and replaced with the status the text actually
has, which loses nothing because the clauses genuinely sit where the chapter says.
- **Opening** — the quotation stands; a new paragraph, *"A note on its status, because
  it is easy to overclaim"*, states that the clause is **not** bolded, that bold starts
  at band 5 and runs downward, and that the header's *other* rule is what makes it bite:
  a script must **fully** fit a band's positive features, and this is a positive-feature
  description of what a band-6 script *is*.
- **Myth 1** — "contains, in bold, a description of exactly this candidate" → "contains
  a description of exactly this candidate — the risk-taker with the wider range and the
  higher inaccuracy".
- **Myth 3** — "names this at band 4, in bold" → names it at band 4, with the band-0
  total-memorisation point added and an explicit note that the band-4 clause is not
  bolded and does not need to be.
- **60-second summary** — rewritten to "At band 6 … the current descriptors describe the
  candidate who reaches for a wider range at the cost of accuracy", with the fully-fit
  rule carrying the argument instead.
- **Decoder header** — now quotes the legend verbatim (*"Bolded text indicates negative
  features that will limit a rating"*) **and** states what it does not give you here:
  nothing in the LR column at bands 6–9 is bolded.

**Source.** `[src: ielts.org — Writing band descriptors PDF (May 2023), per-character
font extraction]`; legend wording quoted verbatim from p.7 of the same file.

#### `[MAJOR]` `[V1]` — Chapter 6 under-claimed its own sourcing in two places

Both are strengthenings: the book was hedging claims that are stated verbatim in an
official document it already cites eleven times. Both quotations were re-fetched and
re-extracted from the PDF by this agent.

**1 — the asking-for-help table.** Was sourced to IELTS Liz / IELTS Advantage / Magoosh
with the caveat "the Part 1 ban is probable rather than certain". It is officially
stated. The three Tier-2 citations and the hedge are deleted; the official paragraph is
now block-quoted above the table, the table is explained as that paragraph read by
contrast (repetition named for Parts 1 and 3; rephrasing and word explanation named only
for Part 3; Part 2 told to consult the card), and the official limit is quoted — *"The
most important thing is not to ask the examiner to repeat every question or explain every
word."* The descriptor argument is kept underneath as corroboration rather than as the
only support. Myths → *"Never ask the examiner to repeat"* upgraded from a derived rule
to a quotable one; self-test item 4 now asks the reader to know it is officially stated.

**2 — the Part 2 stop rule.** The myth entry read *"The examiner cannot stop you before
two minutes, and you must signal if you finish early. Widely circulated; unsupported"* —
which taught the reader to distrust something reassuring. Retitled **"You must signal if
you finish Part 2 early"** (the half that really is unsupported) and rewritten around the
official half: *"Don't worry if the examiner stops you in the Part 2 long turn. It means
you have spoken for 2 minutes."* The same fix is applied in-chapter, in §Part 2
*Finishing early is the real risk*, with the target sentence added — *"You should try to
talk for the full 2 minutes to give the examiner a good sample of your English."*

**Source.** `[src: cambridgeenglish.org — IELTS FAQs, Academic module (PDF), pp.10–11]`,
re-fetched 2026-07-31.

#### `[MAJOR]` `[V2]` — Chapter 6 contradicted Chapter 8 on third-person `-s`, and Chapter 8 was right

**Issue.** Ch6 quoted the band-7 tolerance without its quantifier and told a reader whose
documented omission rate is habitual to "leave them alone", in three places: Tip 3, L1
alert priority 4, and the 60-second summary. The GRA decoder said the same. Ch8 quotes
the IELTS-published figure — **70.6% error at band 6 falling to 7.6% at band 7** — and
frames the target correctly as *occasional slip, not habitual omission*.

**Change.** The threshold is now stated everywhere the tolerance appears, and the
reallocation-of-attention argument (which is good) is kept behind it as a **conditional**.
- **Tip 3** retitled *"Stop hunting basic slips — once they are already occasional"*, with
  *a few* read strictly as a density claim, the official metric named (*error density*),
  the 70.6 / 7.6 figures printed, and the repair pointed at Chapter 8.
- **L1 alert priority 4** → *"once your written error rate on them is already low"*, plus
  a closing paragraph: at 70% you are not spending a tolerance, you are producing the
  band-6 measurement.
- **60-second summary** and the **GRA decoder** carry the same gate.
- **Modal precision restored** throughout: band 7 says a few basic errors *persist*;
  band 8 says a few *may* persist. Also corrected in the myth *"You can't get band 7 …
  with basic grammar slips"*, which had flattened both into "permits".
- **Self-test item 11** now asks whether the written rate is occasional yet, since that
  is the condition for being allowed to stop monitoring in speech.

**Source.** `[src: Roothooft & Breeze 2019 — Speaking data, L1 mix unreported]`;
`[src: ielts.org — Speaking key assessment criteria (PDF, 2023)]` for *error density*;
`[src: ielts.org — Speaking band descriptors (PDF, 2025)]` for both modals.

#### `[MAJOR]` `[V2]` — Chapter 6 taught deliberate repetition as a `[verified]` technique

**Issue.** Tip 1 instructed the reader to *"repeat your last two or three words"* when he
stalls, tagged `[verified]`; Self-test 6 drilled the habit; the summary absolutised it
(*"Never abandon and restart"*), contradicting the tip's own escape hatch four lines
below. But repetition is a **descending** feature of the whole scale: bands 8/9 are
defined by *very occasional* repetition, band 6 names it as a coherence-breaker, and
**band 5 is defined by relying on it**. Band 7 *tolerates* it; nothing rewards
manufacturing it.

**Change.** Tag downgraded to `[expert consensus — descriptor-derived, not officially
stated]`, and repetition demoted from first resort to third. Tip 1 now gives an explicit
order of preference — (1) pause and complete the structure, (2) paraphrase round the gap,
(3) only then repeat your own last words — followed by the scale evidence and the reason
the book's old defence fails: the examiner cannot classify your repetition as
"functional", he hears it and rates density. Self-test 6 rewritten to test holding the
structure rather than repeating. The summary now says abandon-and-restart is for a
genuinely lost proposition, and keeps repetition as a rare rescue.

**Source.** `[src: ielts.org — Speaking band descriptors (PDF, 2025), bands 9–5 Fluency &
Coherence]`; `[src: ielts.org — Speaking key assessment criteria (PDF, 2023)]` for
*"functionless repetitions of words and phrases"*.

#### `[CRITICAL]` `[V5]` — the best pronunciation drill was written in a notation the reader cannot read

**Issue.** The stress-timing drill — which the chapter itself calls the single most
efficient route out of Pronunciation 6 — turned on the unexplained term *schwa* and on
IPA (`/wʊdəv/`, `/ðə/`, `/ɑːskt/`, `/θ/`, `/ð/`). This reader has no teacher and no IPA.
The drill was also called "the rubber-band drill" and contained no rubber band.

**Change.** Fixed at the root and then everywhere downstream.
- New box **§Three words you need before the rest of this chapter makes sense**, placed
  immediately after the format table: **chunking**, **stress-timing** and **schwa**, each
  in plain words with a French anchor for schwa (*le*, *je*) and the explanation of why
  French rhythm comes out even. All three are named in the official band-6 Pronunciation
  cell, so the box also makes the decoder legible.
- **Every phonetic symbol in the chapter now carries an ordinary-letters respelling**, and
  the box says so: *would have* → "wud-uv", *the* → "thuh" not "thee", *asked* → "ahst".
  The two *th* sounds are introduced as "the *th* of *think*" and "the *th* of *this*" in
  the L1 table, the drill heading and the drill's diagnosis step. `/ɑːskt/` removed from
  the transfer table in favour of a plain description.
- Drill 4 renamed **the three-beat drill** (V5's option B — the elastic was never part of
  the procedure), with the instruction rewritten as a countable action: three taps, same
  number of seconds per line, more than twice the syllables on line three.
- The decoder's band-6/band-7 delivery pair now explains the compression in words instead
  of the symbol — and, per `[V4]`, the two lines are now **lexically identical**
  (*I think that the GOVernment should inVEST MORE*), so "Same words. Same accent.
  Different band." is literally true.
- **§The one thing this book cannot do** kept and hardened into a procedure with a written
  output: three checks, each with an explicit pass/fail test and a number to log, and the
  honest note that the coaching system can grade a transcript but cannot hear these three
  either.

#### `[MAJOR]` `[V3]` — Part 2 coverage gaps

**1 — rounding-off questions.** IELTS's own heading appeared once in the book, in a table
cell. They now have a full treatment: what they look like, that they sit **inside Part 2**
and are rated, the officially stated fact that **a short answer is what is expected there**
— *"A short answer is usually expected only when the examiner asks a question at the end of
the long turn in Part 2"* — the trap (a bare *yes* immediately after two minutes of your
best English; the drop in level is audible), the shape that fixes it (answer + one clause),
and an original band-6 / band-7 pair. Self-test item 8 extended to cover it.
**Source.** `[src: ielts.org — Speaking sample tasks (PDF, 2023), p.5]` for the heading and
the transcript; `[src: cambridgeenglish.org — IELTS FAQs, Academic module (PDF), p.10]` for
the short-answer rule.

**2 — cue-card shapes.** The chapter taught Part 2 through one invented card and never said
what else a card can ask, although **card shape determines tense** and tense is this
reader's costliest area. New table of eight families — person · place · object · event or
experience · activity or habit · media · abstract idea · future plan — each with the tenses
it hands you, one structure worth planting, and its characteristic failure. Labelled
explicitly as **a preparation heuristic, not an official taxonomy**; all eight example cards
are original. Tied back to the note template's existing "the tense I'll use here" line, and
to self-test item 9. **Source.** `[src: ielts.org — Academic Speaking test format]` for what
IELTS does say about the card; the absence of an official taxonomy is stated in the text.

#### `[MAJOR]` `[V5]` — jargon and structure in Chapter 7

- **`collocation` now has an unmissable, early canonical definition.** It load-bears three
  chapters before Ch7 defines it, and Ch7 is its home. The definition is now the **first
  paragraph of the chapter** (in the relocated 60-second summary), with three minimal pairs
  and the reason it is the assessed unit; it is repeated in the sub-feature table at first
  use in the body; §1 keeps the full treatment. Other agents' cross-references land here.
- **`hedging`, `stance`, `register` and `nominalisation` glossed in plain words at first
  use** — the first three in the sub-feature table and the §What the criterion contains
  paragraph, nominalisation at the head of its own table.
- **Chapter 6's jargon glossed too**, with pointers rather than duplicate treatments:
  *register* (§Part 1 traps → Ch7 §3), *hedging* (§Part 3 → Ch7 §5), *collocation* (§Myths
  → Ch7 §1), *clefting / fronting* (Tip 7 → Ch8 §7).
- **Both 60-second summaries moved to the START** of their chapters, heading name unchanged,
  each opening "Read this first" with a one-line pointer left at the old position — matching
  Ch1, Ch2, Ch3, Ch4 and Ch5.

#### Padding reduction `[V5]`

Ch7 is the canonical home for vocabulary and false friends, so its 23-row false-friend
table, its 15-row uncountables table and its spelling list are **kept in full**. Chapter 6
carried a compressed re-run of the same material inside §The grammar transfers; it is now
one sentence naming the classes plus a pointer to Ch7 (false friends, uncountables,
spelling) and Ch8 (articles, agreement, the counter-list). Nothing was deleted from a
mandated section — the ranked priority list, which is the part that is Speaking-specific
and lives nowhere else, is untouched and is now the whole of that subsection.

#### `[MINOR]` items applied

- **`[V2]` two 7.5 scripts presented as one (Ch7).** The comparison table is from Sample
  Tasks 2023 Task 2B; the vocabulary inventory and the softening credit come from the CD
  example-responses PDF — a different response to a different prompt. Now "**another**
  official 7.5 script — a different response, to a different prompt".
- **`[V4]` two error miscounts in Ch7's before/after pairs.** "Four spelling errors … six LR
  hits" → **three** misspellings, one wrong suffix, one non-word = **five**, each now named.
  "Four errors disappear" → **five**, because there are **two** generic articles in the
  sentence (*the pollution*, *the society*) — undercounting the book's flagship error in its
  own demonstration was the worst place to be imprecise.
- **`[V4]` Ch7's opening arithmetic was a non-sequitur.** LR is a quarter of the Writing band
  because the four criteria are equally weighted, not because Task 2 counts double. Restated,
  with the double weighting given its real consequence (two thirds of that quarter is decided
  in Task 2) and the equal-weighting claim sourced to the page that states it.
  `[src: ielts.org — Understanding and setting IELTS scores]`
- **`[V2]` pluralised uncountables allocated to LR here and GRA in Ch8.** Standardised on
  Ch8's hedged version: **GRA, and arguably LR too** — IELTS files word formation under LR
  and does not say which side countability falls on. Either way it is scored and the repair
  is the same list.
- **`[V2]` "self-correction is limiting at all nine bands" (Ch6 Myths).** It appears at bands
  4–9 only, which the chapter's own Tip 6 already said. Corrected to **4 to 9**.
- **`[V2]` "buy one band-8 feature outright" (Ch6 Tip 2 and Pronunciation decoder).** Band 7
  needs *"some, but not all"* of band 8's **five** features. Both places now say **budget for
  two** and name them in order of cost: sustained rhythm, then flexible stress and intonation
  across long utterances.
- **`[V4]` *possiBIlity* contradicted the rule it illustrated** (Ch6 Drill 3). Corrected to
  `possiBIlity`, with the capitals pointed at explicitly. *phoTOgraphy* did not end in any of
  the four suffixes listed, so `-graphy / -ology / -ography` is now stated as its own rule
  line with two more examples.
- **`[V1]` the video-call research was a 99-candidate preliminary study.** All three figures
  are verbatim correct; the scale was missing. Now "99 test-takers in Shanghai in 2015, each
  sitting both modes, in a study its own authors describe as a preliminary comparison", in
  both the body and the summary.

#### Judged NOT to change

- **The `[verified]` tag on Chapter 6 Tip 2 (buy stress-timing).** V2 challenged only the
  arithmetic ("one" band-8 feature), not the claim. Band 7 Pronunciation genuinely is defined
  by reference to bands 6 and 8, and sustained rhythm genuinely is band 8's named feature.
  The number was fixed; the tag is correct and stays.
- **Chapter 6's refusal to treat the 2008/2013 Speaking descriptors as current**, and its
  claim about that file's creation and modification dates. V2 re-pulled the file and recorded
  the book as "exactly right". Untouched.
- **Chapter 7's Myth 7** (the fabricated collocation statistic) and its deliberate refusal to
  print the number even while debunking it. Confirmed clean by V2 and V5; untouched.
- **Chapter 7's `[src: ielts-simon.com]` and `[src: myieltsclassroom.com]` citations.** They
  support technique advice, not descriptor claims, and are labelled as what they are. No
  official source states them, and inventing one would be the error the bold finding exists
  to prevent.
- **Chapter 6's honest disclaimer on the phonological transfer table** ("descriptive
  linguistics, not IELTS documentation … I have not verified them to the standard applied to
  the descriptor claims"). V4 and V1 both left it standing; hardening it into fact is exactly
  what the /p/ incident earlier in this log punished.
- **Chapter 6's `[verified]` self-correction tip and the `[expert consensus]` tag on
  "record every practice answer".** Both accurate; the distinction is load-bearing for a
  reader deciding what to trust.
- **Chapter 7's ten topic banks and the AWL myth at full length.** V5 flagged chapter length
  generally, but this is the chapter those belong to; the deduplication was applied to
  Chapter 6's copy of Chapter 7's material, not to Chapter 7's own.

---

## Post-gate repairs (V6)

### `[MAJOR]` `[V6]` — the Listening band-score citation pointed at a page without the table

**Issue.** Chapters 1 and 2 cited `[src: ielts.idp.com — Listening band scores]`
by page title. V6 followed it: the canonical `ielts.idp.com/results/scores/listening`
and the Turkey variant carry **no table**, only a single worked example, and IDP
Japan publishes the four anchors alone. The table is real — V6 found it on
`ielts.idp.com/thailand/results/scores/listening`, matching both chapters row for
row with the caveat quote verbatim — but a reader checking the obvious URL would
have found nothing.

**Why it mattered more than a normal citation slip.** This is the book's most
emphatic sourcing claim. Chapter 2 asserts in bold that these are official
figures and not interpolations, chapter 1 says official and not a reconstruction,
the claim **reverses a position the book previously held**, and the whole
"one mark to band 7" argument rests on it. A sourcing claim that loud must
survive being checked.

**Change.** All six citations in chapters 1 and 2 now name the market page that
actually carries the table, and say so explicitly — the table lives on IDP's
market pages, not on the canonical `/results/scores/listening` URL. Reading needed
no change; V6 verified `ielts.idp.com/turkey/results/scores/reading/en-gb` exactly.

**Verified.** Editor re-fetched the Thailand page: full table returned, 30–31 for
band 7 and 26–29 for 6.5, with IDP's caveat that marks may vary slightly between
tests. Matches both chapters.

**Note on fetching.** `curl` returns 403 on all three IDP score URLs — bot
protection, the same wall met earlier at the British Council terms page. WebFetch
retrieves them. A future verifier getting 403 should not conclude the page is
gone.

### `[MINOR]` `[V6]` — STATUS.md carried a refuted instruction

`STATUS.md` still listed "No official half-band raw-score table exists — the book
must say so rather than publish a fabricated one" among the open conflicts, long
after V1 disproved it and V6 re-certified the correction. Left standing, it would
have told a later pass to undo a fix the gate had just passed. Struck through in
place rather than deleted, so the error remains visible in the record.
