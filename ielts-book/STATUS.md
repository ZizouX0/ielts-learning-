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

Batch 1 — **RUNNING**:
- [~] R1 — Test anatomy & scoring
- [~] R2 — Listening deep dive
- [~] R3 — Reading deep dive
- [~] R4 — Writing Task 1 (Academic)

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

## Log

| Time | Phase | Event |
|---|---|---|
| 2026-07-31 | 0 | Structure created; web tools confirmed available |
