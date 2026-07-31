# STATUS — The IELTS Academic War Book

**Started:** 2026-07-31
**Editor-in-Chief:** Claude Code
**Target reader:** IELTS Academic, band 7.0 overall (min 6.5/section), L1 Arabic
(Tunisian) + French, 6–10 weeks self-study.

---

## Phase 0 — Setup

- [x] Directory structure created
- [x] `STATUS.md` created
- [x] WebSearch available — confirmed working
- [x] WebFetch available — confirmed working (incl. PDF extraction via pdfplumber
      for the official band descriptor PDFs, which WebFetch alone cannot parse)

**Note on prior work.** This repository already contains verified research from
31 July 2026 in `../knowledge/sources.md` (test format, timings, band
descriptors, raw-score conversion, the mid-2026 move to computer-delivered
testing). Research agents are seeded with it as a starting hypothesis but are
required to verify independently — memory and prior notes are hypotheses, not
sources.

## Phase 1 — Research agents

Batch 1 — complete:
- [x] R1 — Test anatomy & scoring (648 lines)
- [x] R2 — Listening deep dive (1,336 lines)
- [x] R3 — Reading deep dive (1,410 lines, 233 inline source notes)
- [x] R4 — Writing Task 1 (1,031 lines)

Batch 2 — complete:
- [x] R5 — Writing Task 2 (1,432 lines)
- [x] R6 — Speaking deep dive (1,319 lines)
- [x] R7 — Vocabulary system (1,203 lines)

Batch 3 — complete:
- [x] R8 — Grammar & L1 interference (1,281 lines)
- [x] R9 — Test-day strategy & study plan (1,224 lines, 202 source notes)

**Phase 1 complete.** ~11,200 lines of sourced notes; **242 rows** in the sources
ledger.

> **Ledger write contention — resolved.** Batch 1 agents were told to
> read-append-write `research/sources-ledger.md` concurrently, which is not
> atomic. In the event no rows were lost: each agent re-read immediately before
> writing and reported preserving prior rows. R9 additionally mirrored its rows to
> `sources-ledger-R9.md`, which stands as the reconciliation reference. V6 still
> traces sampled claims back to the ledger independently.

## Phase 2 — Writer agents

Batch 1 — **RUNNING**:
- [~] Ch 1 — How IELTS Academic Really Works
- [~] Ch 2 — Listening: Complete Playbook
- [~] Ch 3 — Reading: Complete Playbook

Batch 2 — queued:
- [ ] Ch 4 — Writing Task 1: Every Visual Type Mastered
- [ ] Ch 5 — Writing Task 2: Every Question Family Mastered
- [ ] Ch 6 — Speaking: All Three Parts

Batch 3 — queued:
- [ ] Ch 7 — The Band 7 Vocabulary System
- [ ] Ch 8 — Grammar for Band 7 + Arabic/French Error Map
- [ ] Ch 9 — Study Plan, Practice System & Test Day

## Phase 3 — Verification agents (adversarial)

- [ ] V1 — Fact auditor
- [ ] V2 — Band descriptor auditor
- [ ] V3 — Coverage auditor
- [ ] V4 — Consistency & example auditor
- [ ] V5 — Level auditor
- [ ] V6 — Verification gate (runs last, after fix loop)

## Phase 4 — Fix loop

- [ ] All `[CRITICAL]` resolved
- [ ] All `[MAJOR]` resolved
- [ ] `[MINOR]` editing pass
- [ ] `fixes/changelog.md` complete

## Phase 5 — Assembly

- [ ] `book/IELTS-Academic-War-Book.md`
- [ ] `book/CHEAT-SHEETS.md`
- [ ] Appendices A–E
- [ ] Final Editor-in-Chief read-through
- [ ] PDF export

---

---

## Findings that changed work already in this repo

Research surfaced errors in the coaching files built earlier today. Corrections
applied immediately where they affect live grading, rather than waiting for the
fix loop.

| # | Finding | Evidence | Action taken |
|---|---|---|---|
| 1 | **Under-length has no published arithmetic penalty.** ielts.org says answers are "penalised if too short"; Cambridge's FAQ says there is "no direct penalty". The May 2023 descriptors contain no deduction — only that ≤20 words = band 1, and that Task Achievement is *defined* as fulfilling the task using the minimum word count. | R1 + R4 independently | `CLAUDE.md` rewritten: mark the shortfall through TR/TA (and LR/GRA), never as a flat deduction. Flagged for V1 to rule on the Tier 1 conflict. |
| 2 | **The Writing band formula is not published.** The 1:2 Task 2 ratio *is* official; `(T1 + 2×T2)/3` is inference. | R1, R4 | `CLAUDE.md` now labels it an estimate. Other files to follow in the fix loop. |
| 3 | **The top-ranked Writing descriptor PDF in search is the superseded 2013 edition** (`assets.ctfassets.net/...`). The live May 2023 file is `ielts.org/cdn/ielts-guides/ielts-writing-band-descriptors.pdf`. | R4 | Stale URL logged in the ledger as DO NOT CITE; all later agents warned. Earlier work used the British Council copy, which self-identifies as "Updated May 2023" — confirmed current. |
| 4 | **Band 7 Task Achievement now requires data "appropriately categorised"**, not just an overview. "Group, don't list" is in the descriptor, not folklore. | R4 | To be built into Ch.4. |
| 5 | **"No overview → cannot reach band 7" is overstated.** It caps *Task Achievement*; an official sample script scored band 7 overall without a clear overview because its language was band 8–9. | R4 | Existing repo files already scope this to Task Achievement — verified correct, no change needed. |
| 6 | **"Wrong plurals score zero" is too strong** — official Listening keys accept `summer school(s)`, `library/libraries`. Overstating it drives panic over-correction, which for an Arabic/French L1 reader means `informations`/`researches` — a real zero. | R2 | Correct in `knowledge/tricks.md` during the fix loop. |
| 7 | **American spellings are explicitly accepted** in Listening (official key prints `metre(s)/meter(s)`). Not previously recorded. | R2 | Add to Ch.2. |
| 8 | **Two answers written in one gap score zero** even if one is right (Cambridge FAQ). Appears on no format page. | R2 | Add to Ch.2. |
| 9 | **Copied rubric is discounted before the word count**, so copying the prompt can silently push a script under length. | R4 | Added to `CLAUDE.md`. |
| 10 | **Official 2024–25 performance data by L1:** Arabic-L1 mean Academic Writing 5.54 (overall 5.95); French-L1 Writing 6.15 (overall 6.75). Writing is the weakest skill for both. | R1 | Directs chapter weighting and the study plan. |
| 11 | **Summary / note / table / flow-chart completion answers are NOT in passage order** — only *sentence* completion is. `tricks.md` claimed all four were ordered. | R3 | Fixed in `knowledge/tricks.md` + `revision-playbook.md`. |
| 12 | **Matching Features reuse rule was backwards.** Options may be reused only when the instructions permit it; the repo said reuse was allowed unless forbidden. | R3 | Fixed in both files. |
| 13 | **Qualifier-trap rule was wrong.** A vague quantifier in the text (*numerous*, *many*) against a precise claim in the statement gives **NOT GIVEN**, not False — no contradiction exists. The repo taught the opposite. Scope mismatch is what yields False. | R3, from an official worked example | Fixed in both files with the corrected two-way rule. |
| 14 | **"Not Given is the safest blind guess" is unsourced folklore** and actively harmful — it trains premature NG-picking, turning findable answers into misses. | R3 | Removed from both files and replaced with a warning. |
| 15 | **"Passages get progressively harder" is unverified** — no Tier 1 source states it. The 16/19/21 time split is also not official; Cambridge says about 20 minutes per passage. | R3 | Both files now present the official even split as the baseline and the front-loaded split as a labelled personal tactic. |
| 16 | **CD Reading permits copy-paste from the passage**, and all completion answers are transcription rather than composition — so spelling errors are structurally avoidable on those types. Significant for a French/Arabic L1 reader. | R3 | To be built into Ch.3 as a tactic box. |
| 17 | **Reading 6.5 → 7.0 is exactly 3 marks** (27 → 30). Reading has no band descriptors, so every tip must justify itself in marks. | R3 | Framing device for Ch.3. |
| 18 | **The Speaking band descriptors used earlier today were the 2013 edition.** The widely-linked Cambridge webinars PDF has metadata created 2008, modified 2013. The live edition is `ielts.org/cdn/ielts-guides/ielts-speaking-band-descriptors.pdf`, created **2025-09-16**, and its Pronunciation criterion is substantially rewritten around *phonological features*, chunking, stress-timing and speech rate. | R7; confirmed by Editor fetching the PDF and reading its metadata | Speaking section of `knowledge/band-descriptors.md` rewritten from the 2025 text. R6 messaged mid-run with the correct URL. |
| 19 | **A claim in the repo was wrong: "band 7 hesitation is about ideas, not words."** The 2025 descriptor says band 7 hesitation *does* signal difficulty accessing language — it simply must not damage coherence. Content-related hesitation is the **band 8** boundary. | Editor, from the 2025 PDF | Corrected, with the error noted inline so the reader is not confused by older guides. |
| 20 | **Task 2 has a floor and no ceiling.** An official examiner-marked exemplar scoring **7.5** runs to ~375 words. The repo said over ~320 words "buys nothing and costs you". | R5 | Corrected in `tricks.md` and `revision-playbook.md`. |
| 21 | **Informal register is far less fatal than the repo claimed.** The same official 7.5 script uses *don't* three times and writes "In my opinion, I think". An 8.5 script was docked for "e.g." | R5 | "Band-7 killers" list rewritten to keep the advice but drop the overstatement. |
| 22 | **The "five question families" are a heuristic, not an official taxonomy.** IELTS publishes none; the British Council teaches five categories and IDP six, and they do not align. | R5 | Both files now say so explicitly. |
| 23 | **Linker overuse quantified:** an examiner flagged four sequencers in one paragraph of a 7.5 essay as overuse; a 6.5 script was docked for *under*-use. ~2 markers per paragraph is the safe band. | R5 | Added to both files. |
| 24 | **The Writing weighting is better sourced than R1 concluded.** ielts.org's Writing resources page states Task 1 is worth a third and Task 2 two thirds — which does support the (T1 + 2×T2)/3 arithmetic. | R5 | Softened wording in `CLAUDE.md` can be revisited at the fix loop; leaving the cautious phrasing for now pending V1. |
| 25 | **"If you don't discuss both [views], you will be limited to Band 5"** — official, and a sharper statement of the discussion-essay trap than anything in the repo. | R5 (needs verbatim confirmation — reached via rendered summary) | For Ch.5; flagged to V1. |
| 26 | **Spelling and word formation are scored under Lexical Resource, not GRA.** For a French/Arabic L1 reader whose misspellings are predictable, the damage concentrates on one criterion. | R7 | For Ch.7. |
| 27 | **The band-6 Writing descriptor explicitly describes the thesaurus candidate:** it names the "risk-taker" who deploys wider vocabulary at the cost of accuracy, and places them at band 6. This proves the precision-beats-rarity thesis from Tier 1 alone. | R7 | Centrepiece of Ch.7. |
| 28 | **Descriptor-sense "idiomatic" means natural collocation** (*strike a balance*), not figurative idiom (*rain cats and dogs*). In Writing the first raises LR and the second lowers it on register; in Speaking, IDP officially recommends idioms. The repo's advice already matches this — verified correct. | R7 | No change needed. |
| 29 | **A widely-cited statistic is fabricated:** "Cambridge research: 73% of test-takers lose LR points on collocation" traces to a single commercial listicle with no study, year or link. | R7 | Logged as a myth; must never appear in the book. |

## Unresolved conflicts for verifiers

- Paper section order: IDP says Writing→Reading→Listening; BC/ielts.org say Listening→Reading→Writing. Both Tier 1.
- Speaking scheduling window: three different official figures.
- Computer results turnaround: five different official figures (1–2 to 5–7 days).
- Speaking delivery: face-to-face (ielts.org, IDP) vs "face-to-face or video call" (BC booking).
- `ONE WORD ONLY` could not be verified verbatim in any official Listening document.
- No official half-band raw-score table exists — the book must say so rather than publish a fabricated one.
- One Skill Retake in Tunisia: BC Tunisia hosts an OSR page but names no Tunisian centre. Upgraded from "unconfirmed" to "probable but unconfirmed". Separately, BC Tunisia lists only computer-delivered and IELTS Online — no paper.
- Whether matching-headings answers follow text order — R3's reading of the official note needs confirming.
- ielts-simon.com URLs now return 404; any corroboration resting on that site is tagged unverified.
- Question-type count: ielts.org's format page defines **11** numbered Reading task types; the 2023 sample-tasks PDF names **14** by splitting the completion formats. Both official. The book uses the 11-type numbering, which is what Cambridge files its own teaching material under.

## Blocker the Editor could not clear

R9 recommended someone with JavaScript execution retrieve the British Council
terms at `ieltsregistration.britishcouncil.org/terms-and-conditions/Global_IELTS_CD/`,
expecting it would settle the "can a re-mark lower your band" question and
several other open items at once.

The Editor attempted this with headless Chromium, both direct and through the
environment's proxy. **The host returns HTTP 403 to automated requests** — this is
bot protection, not a JavaScript-rendering problem, so executing JavaScript does
not help. `curl` confirms 403 independently.

Consequence: the affected items stay unresolved and the book must present them as
explicit uncertainties (policy option (c)) pointing the reader at his booking
confirmation and his centre. This is an acceptable outcome under the
zero-unverified policy; asserting them would not be.

## Copyright watch

R3's research notes quote official worked examples verbatim (a Marie Curie
passage set, a smoking Yes/No/Not Given set) as evidence. **These must not reach
`chapters/` or `book/`.** Writer agents build original parallels with the same
logical shape. V4 checks for lifted material.

---

## Log

| Time | Phase | Event |
|---|---|---|
| 2026-07-31 | 0 | Structure created; web tools confirmed available |
| 2026-07-31 | 1 | Batch 1 launched (R1–R4) |
| 2026-07-31 | 1 | R1, R2, R4 complete; 10 findings logged; `CLAUDE.md` corrected |
| 2026-07-31 | 1 | Batch 2 launched (R5–R7) |
