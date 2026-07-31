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

Batch 1:
- [x] R1 — Test anatomy & scoring (648 lines)
- [x] R2 — Listening deep dive (1,336 lines)
- [~] R3 — Reading deep dive — RUNNING
- [x] R4 — Writing Task 1 (1,031 lines)

Batch 2 — **RUNNING**:
- [~] R5 — Writing Task 2
- [~] R6 — Speaking deep dive
- [~] R7 — Vocabulary system

> **Known risk — ledger write contention.** Batch 1 agents were told to
> read-append-write `research/sources-ledger.md` concurrently, which is not
> atomic; entries may be lost. Mitigation: batches 2–3 write per-agent ledger
> fragments (`sources-ledger-RN.md`) which the Editor merges. Batch 1 entries are
> reconstructed from the inline source notes in their research files during the
> V6 gate, so no claim escapes the ledger requirement.

Batch 2:
- [ ] R5 — Writing Task 2
- [ ] R6 — Speaking deep dive
- [ ] R7 — Vocabulary system

Batch 3:
- [ ] R8 — Grammar & L1 interference
- [ ] R9 — Test-day strategy & study plan

## Phase 2 — Writer agents

- [ ] Ch 1 — How IELTS Academic Really Works
- [ ] Ch 2 — Listening: Complete Playbook
- [ ] Ch 3 — Reading: Complete Playbook
- [ ] Ch 4 — Writing Task 1: Every Visual Type Mastered
- [ ] Ch 5 — Writing Task 2: Every Question Family Mastered
- [ ] Ch 6 — Speaking: All Three Parts
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

## Unresolved conflicts for verifiers

- Paper section order: IDP says Writing→Reading→Listening; BC/ielts.org say Listening→Reading→Writing. Both Tier 1.
- Speaking scheduling window: three different official figures.
- Computer results turnaround: five different official figures (1–2 to 5–7 days).
- Speaking delivery: face-to-face (ielts.org, IDP) vs "face-to-face or video call" (BC booking).
- `ONE WORD ONLY` could not be verified verbatim in any official Listening document.
- No official half-band raw-score table exists — the book must say so rather than publish a fabricated one.
- One Skill Retake in Tunisia: BC Tunisia hosts an OSR page but names no Tunisian centre. Upgraded from "unconfirmed" to "probable but unconfirmed". Separately, BC Tunisia lists only computer-delivered and IELTS Online — no paper.

---

## Log

| Time | Phase | Event |
|---|---|---|
| 2026-07-31 | 0 | Structure created; web tools confirmed available |
| 2026-07-31 | 1 | Batch 1 launched (R1–R4) |
| 2026-07-31 | 1 | R1, R2, R4 complete; 10 findings logged; `CLAUDE.md` corrected |
| 2026-07-31 | 1 | Batch 2 launched (R5–R7) |
