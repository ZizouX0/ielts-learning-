# V6 — Verification Gate

**Date:** 2026-07-31
**Scope:** all nine chapters in `ielts-book/chapters/`, against
`ielts-book/research/sources-ledger.md` (287 rows) and `sources-ledger-R9.md` (47 rows).
**Status of this document:** a gate. Assembly is authorised only on `PASS`.

Nine independent source retrievals were performed (seven live fetches, two PDF
binary extractions). Findings below are ordered by severity, not by check number.

---

## Severity tally

| Severity | Count |
|---|---:|
| `[CRITICAL]` | **0** |
| `[MAJOR]` | **1** |
| `[MINOR]` | **5** |

Verdict rules: any `[CRITICAL]` → FAIL; more than three `[MAJOR]` → FAIL. Neither
threshold is reached.

---

## Check 1 — Zero unverified

```
grep -c "\[UNVERIFIED\]" chapters/*.md
```

| Chapter | Count |
|---|---:|
| 01-how-ielts-works.md | 0 |
| 02-listening.md | 0 |
| 03-reading.md | 0 |
| 04-writing-task1.md | 0 |
| 05-writing-task2.md | 0 |
| 06-speaking.md | 0 |
| 07-vocabulary.md | 0 |
| 08-grammar-L1.md | 0 |
| 09-studyplan-testday.md | 0 |
| **Total** | **0** |

**PASS.** The research files still carry `[UNVERIFIED]` tags (correctly — that is
their job); no tag survives into a chapter.

Secondary observation, recorded as sound rather than as a defect: the book operates a
three-tier epistemic labelling system that survives into the chapters intact —
`[src: ...]` for sourced fact (483 instances), `[verified]` (76) and
`[expert consensus]` (30) for technique. I sampled twelve `[expert consensus]` tags
at random; every one attaches to strategy or drill advice, none to a claim about
official policy or scoring. Chapter 5 line 465 defines the tag in the text. This is
the correct discipline and it holds.

---

## Check 2 — Random claim tracing

Twenty-one claims sampled by seeded shuffle across the `[src:` inventory, minimum two
per chapter. Nine were spot-checked by live retrieval.

### Traced claims

| # | Ch | Claim (abbreviated) | `[src:]` note | Ledger row | Result |
|---:|---|---|---|---|---|
| 1 | 1 | Computer results: about half within one day, 80% within two | ielts.org — Fast IELTS results | `ielts.org/take-a-test/your-results/fast-test-results-and-sharing` | traced |
| 2 | 1 | Arabic-L1 Academic means L5.70 R6.10 W5.54 S6.22 O5.95; French 6.95/7.01/6.15/6.65/6.75 | ielts.org — Test taker performance data 2024-2025 (XLSX) | `ielts.org/cdn/…/ielts-test-taker-performance-data-2024-2025.xlsx` | traced |
| 3 | 1 | ielts.org/BC publish four anchors; IDP publishes the full half-band table | ielts.idp.com — Listening / Reading band scores | Reading: rows 119–120. **Listening: no row** | see `[MAJOR] M1` |
| 4 | 2 | Accents list is illustrative, not closed; five is the working number | T1 ielts.org — Listening test format; T1 cambridgeenglish.org — FAQs p.4 | rows 35, 74, 63, 78 | traced |
| 5 | 2 | Both UK and US spellings accepted (`metre(s)/meter(s)`) | T1 cambridgeenglish.org — FAQs p.4 | rows 63, 78, 79 | traced |
| 6 | 2 | `-teen`/`-ty` stress contrast; NAmE flapped /t/ | T2 E2 — Understanding distractors; T2 IELTS Advantage | rows 95, 96 | traced (Tier 2, correctly labelled) |
| 7 | 3 | ielts.org defines 11 numbered types; 2023 sample-tasks PDF names 14 | ielts.org — Reading test format; Sample Tasks 2023 PDF | rows 36, `…academic-reading-sample-tasks-2023.pdf` | **fetched ✓** |
| 8 | 3 | *Choose TWO letters* occupies two question numbers, two marks, either order | ielts.org — Academic Reading Sample Tasks 2023 PDF + key; Reading test format | as above | **fetched ✓** (format page quote confirmed verbatim) |
| 9 | 3 | FALSE/NO can be proven; NOT GIVEN cannot | britishcouncil — T/F/NG PDF; ielts.idp.com — 'not given' examples | `reading_tfng_.pdf`; `article-n-is-for-not-given` | traced |
| 10 | 4 | TA is *defined* as fulfilling the task using a minimum of 150 words | Key Assessment Criteria PDF p.1 | rows 14, 49 | traced |
| 11 | 4 | Inputs include *"a diagram of an object, device, process or event"* | ielts.org — IELTS Academic format: Writing | rows 17, 37 | traced |
| 12 | 5 | *"If you don't discuss both, you will be limited to Band 5."* | ielts.org — Writing test resources | `ielts.org/take-a-test/preparation-resources/writing-test-resources` | **fetched ✓ verbatim** |
| 13 | 5 | BC teaches five essay categories, IDP six; ielts.org publishes no taxonomy | takeielts…/how-to-write-an-english-essay-for-ielts; ielts.idp.com — how-to-understand-task-2-writing-questions | both present | traced |
| 14 | 6 | Chunking, stress-timing and speech rate are named in the band-6 Pronunciation cell | ielts.org — Speaking band descriptors (PDF, 2025) | R9 row 41 | **fetched ✓** (metadata Author IELTS, CreationDate 2025-09-16) |
| 15 | 6 | *"It means you have spoken for 2 minutes"* (p.10); *"talk for the full 2 minutes"* (p.11) | cambridgeenglish.org — IELTS FAQs (PDF), p.10 | rows 63, 78, R9 36 | **fetched ✓ verbatim, page numbers exact** |
| 16 | 7 | AWL = Coxhead (2000), corpus ~3.5m words | Coxhead 2000, described in Therova 2020, TESL-EJ 24(1) | row 160 (`files.eric.ed.gov/fulltext/EJ1257224.pdf`) | traced |
| 17 | 7 | Band-6 LR wording on inappropriacy | ielts.org — Writing band descriptors PDF (May 2023) | row 13 | **fetched ✓** (metadata CreationDate 2023-05-03) |
| 18 | 8 | Articles 18.4% at band 6 → 7.4% at band 7; third-person *-s* 70.6% → 7.6% | Roothooft & Breeze 2019 | row 270 | **fetched ✓ exact** |
| 19 | 8 | Uncount nouns are not used in the plural | British Council LearnEnglish (Tier 2) | row 282 | traced |
| 20 | 9 | Water only in a clear bottle; no food; no watches; 2h40 with no breaks | ielts.org — What to expect on IELTS test day | R9 row 9 | **fetched ✓ verbatim** |
| 21 | 9 | Tunisia ID rule and TND fees | britishcouncil.tn — Réservez votre examen IELTS (FR) | R9 row 30 | traced |

### Spot-checks performed by retrieval

1. **`ielts.idp.com/turkey/results/scores/reading/en-gb`** — returned the full
   Academic Reading table. Matches Ch1 and Ch3 **row for row**: 39–40=9, 37–38=8.5,
   35–36=8, 33–34=7.5, 30–32=7, 27–29=6.5, 23–26=6, 19–22=5.5, 15–18=5. Caveat
   *"As a result of the variations in texts used on different occasions, actual scores
   may differ slightly between tests"* confirmed. Also *"no penalty for incorrect
   responses"*.
2. **`ielts.idp.com/thailand/results/scores/listening`** — returned the full Listening
   table. Matches Ch1 and Ch2 **row for row**: 39–40=9, 37–38=8.5, 35–36=8, 32–34=7.5,
   30–31=7, 26–29=6.5, 23–25=6, 18–22=5.5, 16–17=5. Caveat *"Actual marks may vary
   slightly between tests due to the variation in listening questions used on
   different occasions"* — the exact sentence Ch2 quotes. **The claim verifies.** The
   citation route to it does not; see `[MAJOR] M1`.
3. **`ielts.org/take-a-test/preparation-resources/writing-test-resources`** — all three
   Ch5 quotations returned verbatim, including *"If you don't discuss both, you will be
   limited to Band 5."*
4. **`ielts.org/…/ielts-academic-format-reading`** — 11 numbered types confirmed;
   *"60 minutes (including transfer time)"*; *"Each correct answer receives 1 mark"*;
   *"you will lose marks for incorrect spelling and grammar"*; the multiple-answer
   sentence Ch3 quotes.
5. **`ielts.org/take-a-test/preparation-resources/on-test-day`** — clear-bottle water,
   food ban, watch ban, belongings, and *"This takes 2 hours 40 minutes, and there are
   no breaks between each section of the test"* all verbatim.
6. **`cambridgeenglish.org/images/269898-ielts-academic-faqs.pdf`** (pdfplumber) —
   p.10 *"Don't worry if the examiner stops you in the Part 2 long turn. It means you
   have spoken for 2 minutes."* and p.11 *"You should try to talk for the full 2
   minutes…"*. Page attributions in Ch6 are correct. Also confirmed p.8 *"There is no
   direct penalty for writing fewer than 150 words"* and the Task 2 double-weighting.
7. **`ielts.org/cdn/Research/…roothooft-et-al-2019.pdf`** (pdfplumber) — every figure
   the book leans on: articles `241/833 28.9% · 214/1020 21% · 254/1377 18.4% ·
   115/1546 7.4% · 88/1703 5.2%`; third-person *-s* `36/47 76.6% · 34/58 58.6% ·
   36/51 70.6% · 8/105 7.6% · 6/115 5.2%`; chi-square band 6→7 = 80.1178;
   conditionals peaking at 27.8% at band 7; *"There were no third conditional
   structures"*; and *"…'peoples' or 'informations') were found to occur at all band
   levels"*. **Exact.** This is the highest-stakes source in the book and it is clean.
8. **`ielts.org/cdn/ielts-guides/ielts-speaking-band-descriptors.pdf`** — HTTP 200,
   metadata `Author: IELTS`, `CreationDate: 2025-09-16`. Ch6's and Ch8's
   `(PDF, 2025-09-16)` attribution is exact, and Ch6's myth entry against the 2008/2013
   Cambridge webinar copy is well founded.
9. **`ielts.org/cdn/ielts-guides/ielts-writing-band-descriptors.pdf`** — bold extracted
   by font name; see Check 7, item B, where this settles a contested claim.

**Result of Check 2: no `[CRITICAL]`.** Every sampled claim either traces to a ledger
row or verifies on retrieval. Four ledger gaps are recorded as `[MINOR]` below.

---

## Check 3 — Ledger tier audit

Tier column across both ledger files: 227 rows Tier 1 (plus 12 Tier-1 rows annotated
dead / inaccessible / unretrieved / superseded), 51 Tier 2 (plus 9 annotated), 13 rows
Tier 3, 1 row marked `—` (the superseded 2013 Writing PDF, logged as DO-NOT-CITE).

Non-obvious domains checked individually and correctly tiered: `files.eric.ed.gov`
(peer-reviewed TESL-EJ / ELT journals), `onlinelibrary.wiley.com` (TESOL Quarterly,
Language Learning), `owl.purdue.edu`, `learnenglish.britishcouncil.org`,
`www.eapfoundation.com`, `students.unimelb.edu.au`, `dictionary.cambridge.org` — all
Tier 2 academic or institutional. `al-kindipublishers.org` and
`www.academypublication.com` are the weakest two; both are labelled `(Tier 2)`
**inline in Chapter 8's own citations**, which is the right handling.

**No Tier 3 source is load-bearing anywhere.** All thirteen Tier-3 rows are aggregate
discovery rows. I checked the three that could plausibly have leaked into evidence:

- `langogh.com` (the "73% of test-takers" collocation statistic) — logged as
  **REJECTED, MYTH 7**. `grep "73%" chapters/*.md` returns **zero**. Correctly quarantined.
- `heatherhughes.co.uk` (French false friends) — never retrieved, never cited.
- The Tunisian-Arabic / VOT / `/θ/`-`/ð/` / word-stress phonology rows — these *do*
  inform Chapter 6's L1 alert, and Chapter 6 handles it exactly right, in the text:
  *"Those phonological descriptions come from descriptive linguistics, not IELTS
  documentation, and I have not verified them to the standard applied to the descriptor
  claims in this book"*, and for the initial-cluster question, *"Treat it as strong
  reasoning to test, not established fact."* The load-bearing conclusion is then carried
  by the Tier 1 band-6 Pronunciation cell. That is not a Tier 3 source doing evidential
  work; it is a Tier 3 source explicitly demoted to a hypothesis with a four-minute
  self-test attached.

The only Tier 2 prep-blog name appearing inside a chapter is
`myieltsclassroom.com` (Ch7 ×2), which the ledger classifies Tier 2, not Tier 3.

**PASS.**

---

## Check 4 — No superseded editions

```
grep -n "ctfassets"            chapters/*.md   → 0 hits
grep -n "assets.cambridgeenglish" chapters/*.md → 0 hits
```

Neither superseded PDF is cited anywhere. Both are *named as traps*, which is better
than silence:

- Ch4 line 797: *"If you find a descriptor PDF whose band-7 TA line reads 'presents a
  clear overview of main trends, differences or stages', you have the superseded 2013
  edition — close it."*
- Ch5 lines 673, 684 make the same point for Task 2.
- Ch6 lines 539–540: *"That file was created in 2008 and last modified in 2013; the
  current descriptors carry a 2025 revision."* — independently confirmed by spot-check 8
  (the live ielts.org Speaking PDF has CreationDate 2025-09-16).

**PASS.**

---

## Check 5 — Copyright

```
grep -niE "Mkere|Westall|Packham|Carlton House|Royal Oak|Majestic|Imperial|Marie Curie|radium|polonium" chapters/*.md
→ 0 hits
```

The proper nouns V4 flagged, and the Marie Curie / smoking sets STATUS.md warned about,
are absent from all nine chapters. They remain in the R3 research file only, which is
where STATUS.md said they must stop.

Exact-phrase web searches on the two chapter passages that most closely imitate real
test material returned **no source match**:

- *"Every regional library I visited had cut its opening hours"* (Ch3 Y/N/NG worked
  example) — no match; results are unrelated news reporting.
- *"Two thirds of the households on the eastern bank were connected"* (Ch3 scope-mismatch
  pair) — no match.

Band descriptor handling is compliant. The decoder sections paraphrase and say so —
Ch4: *"Restated in my own words… one short official phrase quoted per criterion"*;
Ch6: *"Paraphrased from the current official descriptors… One short quotation per
criterion."* Quoted fragments are short and analytic (*"the data are appropriately
categorised"*, *"these will not affect coherence"*). No chapter reproduces a descriptor
grid. Worked examples throughout are original constructions.

**PASS.**

---

## Check 6 — Structural integrity

Tested as an exact `^## <heading>` match for each of the eight mandated sections.

| Chapter | Result |
|---|---|
| 01-how-ielts-works.md | all 8 present |
| 02-listening.md | all 8 present |
| 03-reading.md | all 8 present |
| 04-writing-task1.md | all 8 present |
| 05-writing-task2.md | all 8 present |
| 06-speaking.md | all 8 present |
| 07-vocabulary.md | all 8 present |
| 08-grammar-L1.md | all 8 present |
| 09-studyplan-testday.md | all 8 present |

Five chapters extend a mandated heading with a subtitle after the required string
(Ch1 *"Band descriptor decoder — the band math"*; Ch2 *"L1 alert — Arabic and French
traps in Listening"*; Ch4 *"L1 alert — French and Arabic in Task 1"*; Ch7 and Ch8
*"Question types, one by one — …"*). Each still opens with the mandated string, so
each matches. Not a defect; noted so the Editor can normalise them in the ToC if the
assembled book needs identical section names.

Additional H2s beyond the eight (Ch2 *Answer-rule reference*, *Where the audio comes
from*; Ch3 *The FALSE / NOT GIVEN decision procedure*; Ch5 *What is still unsettled*;
Ch8 *The spine of this chapter*) are permitted extras, not omissions.

**PASS.**

---

## Check 7 — The fixes actually landed

Each verified independently of the changelog's claim.

### A. Half-band raw-score tables — printed, sourced to IDP, false claim removed

- **Ch1** lines 365–398 print **both** tables side by side: the four ielts.org/BC
  anchors (L 16/23/30/35, AR 15/23/30/35) and IDP's full nine-row table with every half
  band, for Listening and Academic Reading. Followed by the cross-check that each
  ielts.org anchor is the bottom mark of the matching IDP row.
- **Ch2** lines 806–824 print the Listening half-bands as a mark budget. The
  `(interpolated — not official)` labels are **gone**; the text now reads *"These are
  official figures, not interpolations."*
- **Ch3** lines 997–1030 print the Reading table with IDP's caveat quoted.
- `grep -niE "not published by any official|no official source publishes"` returns
  **one** hit, Ch3 line 918 — and it is about the *answer-key letter distribution*, an
  entirely different claim, correctly stated. The raw-score claim is gone.
- Arithmetic cross-check of Ch2's "losses affordable" column against its own ranges:
  all five rows correct.
- Ch1's derived warnings check out against both verified tables: *"a raw 26 is a 6.5 in
  Listening and still a 6 in Academic Reading; a raw 32 is a 7.5 in Listening"* — true
  on both.
- Ch3's band-5 asymmetry note (*Academic Reading 15, Listening 16*) is correct and
  resolves the earlier Ch1/Ch3 conflict.

**Landed.** Caveat at `[MAJOR] M1` concerns the citation route, not the numbers.

### B. No chapter claims the band-6 descriptor clauses are bold

Three chapters state the position, and they agree:

- Ch5 lines 141–145: page 7 (bands 9/8/7) has **zero** bolded negative features;
  page 8 (bands 6/5/4) has **only two** bolds, both belonging to **band 5**; plus the
  warning that *"rows are tall and text is top-aligned in their cells, so a bold phrase
  can sit level with the 6 label while belonging to band 5."*
- Ch7 lines 83–90, 774–776: *"every bolded phrase sits at band 5 — nothing at 6."*
- Ch8 lines 639–643: *"on the descriptor pages covering bands 6 and 5 the entire bold
  inventory sits at band 5."*

**I tested this rather than accepting it.** Bold extracted by font name from the live
`ielts-writing-band-descriptors.pdf` (metadata: Author IELTS, CreationDate 2023-05-03,
9 pages):

- Page 7 (Task 2, bands 9/8/7): zero bold body runs. Confirmed.
- Page 8 (Task 2, bands 6/5/4): exactly two bold body runs —
  *"incompletely addressed."* at y=313 and *"Paragraphing may be inadequate or
  missing."* at y=499.
- Ownership resolved by extracting the Task Response column word-by-word with
  y-coordinates. Band 6's TR text runs y=120–225 (*"The main parts of the prompt are
  addressed (though some may be more fully covered than others)…"*). Band 5's TR text
  **begins at y=313** with *"The main parts of the prompt are **incompletely
  addressed**."* The band-5 row label sits at y=408 — i.e. **below its own cell text**,
  which is precisely the trap Ch5 warns about. *"Paragraphing may be inadequate or
  missing."* sits in the band-5 Coherence & Cohesion cell.

Both bolds are band 5. Ch5, Ch7 and Ch8 are correct, and Ch5's top-alignment caveat is
not hand-waving — it is the exact mechanism that makes the claim non-obvious.
**Landed, and independently confirmed.**

### C. Ch3's Yes/No/Not Given example and the scope-mismatch rule

Required in three places; present in all three.

- **Worked example** (lines 355–388). The population item is keyed **NOT GIVEN**:
  *"The writer's claim covers the libraries he visited; the statement covers all of
  them… Narrow in the passage, wide in the statement, is a gap, not a contradiction."*
  Immediately followed by the contrasting contradiction case (*"outside the two northern
  counties, not a single library changed its hours"* → **NO**), with the discriminator
  stated: *"it is whether a sentence exists that rules the statement out."*
- **Qualifier table** (lines 758–759). Two adjacent rows, explicitly named
  *"Scope mismatch, gap version"* → **NOT GIVEN** and *"Scope mismatch, contradiction
  version"* → **FALSE / NO**, each with a worked original pair beneath (lines 777–795,
  the eastern-bank / district households example).
- **Chapter summary** (lines 34–38): *"A scope mismatch is NOT GIVEN too — unless the
  text explicitly rules the statement's population out, in which case it is FALSE.
  Narrow in the passage against wide in the statement is a gap, not a contradiction."*

Terminology is also correct throughout: Y/N/NG uses YES/NO/NOT GIVEN, T/F/NG uses
TRUE/FALSE/NOT GIVEN, and the split table at lines 335–340 keeps them apart.
**Landed.**

### D. Ch4 has a section for a static, non-process, non-map diagram

`### 9. Static diagram — an object, a device, or an event`, Ch4 lines 522–630. It
derives its own existence from the official wording (*"object and device are separate
items from process, so a diagram is not automatically a sequence"*), covers the
single-moment arrangement case, names the tense rules in the type table at lines
182–183 (present simple active/passive; past simple for a historical artefact), and
flags the two traps — the label inventory, and inventing a sequence
(*"first · then · once completed · in the final stage all invent an order the diagram
does not contain"*). The self-test checklist at line 1078 tests it. **Landed.**

### E. Ch5 states "limited to Band 5" as official fact with no hedge

Twice, and unhedged both times. Line 16 (60-second summary): *"ielts.org states the
outcome in its own words."* Lines 104–113: *"This is not an inference and it is not a
teacher's rule of thumb… Take it as the published fact it is."* **Fetched and confirmed
verbatim on the live page** (spot-check 3). Corroborated in the chapter by the band-5
bold. **Landed.**

### F. Ch6 and Ch8 agree on third-person *-s*

- Ch6 line 896: *"The target is **occasional slip, not habitual omission**."* Preceded
  by the descriptor's own tolerance (line 679: band 7 *"does not demand that you
  eliminate… missing third-person -s"*) and the 70.6% → 7.6% measurement.
- Ch8 line 875: *"…**occasional slip**, not **habitual omission**."* Same framing at
  line 687 against the key assessment criteria.

Same numbers, same source, same conclusion, no contradiction. **Landed.**

### G. Ch2, Ch6 and Ch7 agree that /p/ is not a missing phoneme

- Ch2 line 904: *"French supplies /p/, so the phoneme is not missing from your
  [inventory]."*
- Ch6 line 749 (table) and lines 779–785: *"/p/ is almost certainly not a missing
  phoneme. You speak French; French has [p]. The likely problem is **aspiration**…"*
- Ch7 lines 961–964: *"you also speak French, which supplies both, so these are not
  missing from your inventory (see Chapter 6, where the real issue turns out to be
  aspiration rather than an absent phoneme)."*

Three chapters, one position, with Ch7 explicitly cross-referencing Ch6 rather than
restating a rival account. **Landed.**

**Check 7: all seven fixes verified independently. PASS.**

---

## Check 8 — Cross-chapter numeric consistency

| Quantity | Value | Where checked | Agreement |
|---|---|---|---|
| Total test time | 2h45 total; 2h40 for L+R+W with no breaks | Ch1 44–55, Ch6 119, Ch9 21–23, 186–199 | consistent, and both figures are *reconciled in the text* in Ch1 and Ch9 rather than asserted |
| Listening duration | ~30 min | Ch1 119, Ch2 19/55, Ch9 298 | consistent |
| Listening review time (computer) | 2 minutes, no transfer | Ch1 155, Ch2, Ch9 211/298/608 | consistent |
| Listening raw anchors | 5=16, 6=23, 7=30, 8=35 | Ch1 369–372, Ch2, Ch3 | consistent; matches IDP Japan four-anchor page |
| Listening half-bands | 9=39–40 · 8.5=37–38 · 8=35–36 · 7.5=32–34 · 7=30–31 · 6.5=26–29 · 6=23–25 · 5.5=18–22 · 5=16–17 | Ch1 380–390, Ch2 808–814 | identical in both; **verified against IDP Thailand** |
| Reading raw anchors | 5=15, 6=23, 7=30, 8=35 | Ch1 369–372, Ch3 1050 | consistent; band-5 asymmetry (15 vs 16) explained in both |
| Reading half-bands | 9=39–40 · 8.5=37–38 · 8=35–36 · 7.5=33–34 · 7=30–32 · 6.5=27–29 · 6=23–26 · 5.5=19–22 · 5=15–18 | Ch1 380–390, Ch3 997–1006 | identical; **verified against IDP Turkey** |
| Band-7 threshold | 30/40 in both papers | Ch1 419, Ch2 812, Ch3 24, 1032 | consistent |
| Gap from 6.5 to 7 | Listening 1 mark from 29; Reading 3 from 27, 1 from 29 | Ch1 410–417, Ch2 819–823, Ch3 30–33, 1032–1042 | consistent and arithmetically correct |
| Reading total text length | 2,150–2,750 words | Ch1 162, Ch3 60, 914 | consistent |
| Reading transfer time | none; 60 min inclusive | Ch1 165, Ch3 10 | consistent; **fetched ✓** |
| Speaking duration | 11–14 min, 3 parts (4–5 / 3–4 / 4–5) | Ch1 9, 201, Ch6 7, 55, 62, Ch9 195 | consistent |
| Speaking Part 2 | 1 min prep, 1–2 min long turn, aim to be stopped at 2 | Ch6 62, 217–219, 283–285, Ch9 300 | consistent; **fetched ✓** |
| Task 1 minimum | 150 words | Ch1 190, Ch4 9, 65, 90 | consistent |
| Task 2 minimum | 250 words | Ch1 191, Ch5 90 | consistent |
| Task 1 stop time | 20 minutes | Ch1 190, Ch4 118–131 (schedule ends 0:20, *"Stop and move on"*), Ch9 488 | consistent |
| Task 2 time | 40 minutes | Ch1 191, Ch5 80, 543, Ch9 527 | consistent |
| Working word targets | T1 170–190; T2 270–290 | Ch4 96, 695, Ch5 27, Ch9 621 | consistent |
| Writing combination | `(T1 + 2×T2) ÷ 3`, labelled unpublished estimate | Ch1 25–26, 463 | consistent, and correctly hedged per project rule |
| Under-length mechanism | no tariff; TA/TR + LR/GRA; ≤20 words = band 1; copied rubric discounted | Ch1 317, Ch4 88–98, Ch5 125 | consistent; **fetched ✓** on both the descriptors PDF and the Cambridge FAQ |

**PASS.** I found no numeric disagreement between chapters.

---

## Issues

### `[MAJOR]` M1 — `[src: ielts.idp.com — Listening band scores]` does not resolve to a page carrying the table

The Listening half-band table is cited five-plus times across Ch1 and Ch2 by page
*title*, not URL. Following that title leads to the wrong page:

| URL tried | Result |
|---|---|
| `ielts.idp.com/results/scores/listening` (canonical, the exact parallel of the Reading URL in ledger row 120) | **No table.** One example only: *"you will need a raw score of 35 out of 40 to achieve a band score of 8"* |
| `ielts.idp.com/turkey/results/scores/listening/en-gb` (parallel of the ledger's Reading URL at row 119) | **No table.** |
| `ieltsjp.com/japan/about/about-ielts/ielts-band-scores/en-gb` | Four anchors only (16/23/30/35) — i.e. the ielts.org position, not the half-bands |
| `ielts.idp.com/thailand/results/scores/listening` | **Full table, exact match, caveat verbatim** |

So the table is real and official — but it exists only on some regional variants, and
the two variants the ledger already uses for *Reading* are precisely the two that lack
it for *Listening*.

Why this is `[MAJOR]` and not cosmetic: Ch2 line 815 asserts, in bold,
**"These are official figures, not interpolations,"** and Ch1 line 398 says
*"it is official, not a reconstruction."* This is the book's most emphatic single
sourcing claim, it reverses a position the book previously held, and the whole
"your last half-band is one mark" argument — described in the changelog as *"the most
motivating number in the book"* — rests on it. A reader or a future verifier who checks
the citation at the obvious URL will find nothing and conclude the numbers were
reconstructed from prep blogs, which is exactly the accusation the fix was meant to
retire. The numbers are right; the audit trail to them is not.

**Required before assembly:** replace `[src: ielts.idp.com — Listening band scores]`
with a citation naming a URL that actually carries the table
(`https://ielts.idp.com/thailand/results/scores/listening`, verified 2026-07-31), in
Ch1 and Ch2, and add the corresponding ledger row. Consider adding a one-line note that
IDP's Listening table is not present on every regional page. The Reading citation needs
no change — `ielts.idp.com/turkey/results/scores/reading/en-gb` is already correct in
the ledger and verifies.

### `[MINOR]` ledger gaps — claim verifies, ledger row missing

Per the gate's own rule these do not fail the book. All four are Tier 1 or
Tier 1-domain, and each claim verified. Close in Appendix E.

| # | Citation | Used in | Actual source | Status |
|---|---|---|---|---|
| m1 | `ielts.idp.com — Listening band scores` | Ch1 ×3, Ch2 ×2 | `https://ielts.idp.com/thailand/results/scores/listening` | **verified by fetch**; no ledger row exists under any URL |
| m2 | `takeielts.britishcouncil.org — common mistakes in IELTS Writing` | Ch7 lines 359, 719 | `https://takeielts.britishcouncil.org/blog/common-mistakes-ielts` | **verified**: *"Using the wrong register is one of the most common mistakes made in the IELTS Writing test."* No ledger row |
| m3 | `britishcouncil — IELTS on computer: Making notes` | Ch3 line 837 | `…/free-ielts-english-practice-tests/ielts-on-computer/about/making-notes` | page confirmed to exist; ledger has only the sibling `how-it-works` and `highlighting-text` rows |
| m4 | `ielts.idp.com — Speaking Part 3` | Ch6 line 425 | not located | ledger holds IDP Speaking Part 1 and Part 2 articles but no Part 3. Claim is low-stakes technique advice, corroborated elsewhere in the chapter |

### `[MINOR]` m5 — `STATUS.md` still carries the refuted half-band finding

`ielts-book/STATUS.md` lists, as a live open question:

> *"No official half-band raw-score table exists — the book must say so rather than
> publish a fabricated one."*

That finding was overturned by V1 and reversed across three chapters by the fix loop.
Leaving it in the file that steers assembly is a live hazard: it instructs the Editor to
undo the very fix Check 7A just certified. STATUS.md's copyright-watch note should also
be updated to record that Check 5 found the flagged material absent from all chapters.

---

## Summary

Nine chapters. Zero `[UNVERIFIED]`. Twenty-one claims traced, nine sources retrieved
live, and the two hardest claims in the book — the Roothooft & Breeze error rates and
the band-ownership of the bolded descriptor clauses — were re-derived from the primary
PDFs rather than taken on trust. Both held exactly. All eight mandated sections present
in all nine chapters. No superseded edition cited. No official test material reproduced.
No Tier 3 source doing evidential work. No numeric disagreement between chapters. All
seven claimed fixes independently confirmed landed, including the three that had
previously been fixed wrongly or half-way.

One `[MAJOR]`: the Listening half-band table is genuinely official and its numbers are
exactly right, but the citation points at pages that do not carry it, which would leave
the book's boldest sourcing claim indefensible under inspection. That is a citation
repair, not a rewrite, and it does not reach the failure threshold. Five `[MINOR]`
items — four ledger gaps whose claims verify on fetch, and one stale instruction in
STATUS.md.

The book passes. **M1 must be repaired during assembly, not after**, and the four ledger
gaps must be closed in Appendix E.

## VERDICT: PASS
