# IELTS Academic preparation system

A personal, examiner-calibrated IELTS Academic coaching system. Target band
**7.0 overall**; ~90 minutes of study a day.

Open this repository in Claude Code and run a slash command. `CLAUDE.md` loads
automatically and sets the coaching rules — strict grading, criterion by
criterion, with every correction explained and every result logged.

---

## Commands

| Command | What it does | Typical length |
|---|---|---|
| `/writing2` | Timed Task 2 drill on the question family I am weakest at, graded per criterion, with 3–5 of my own sentences fixed and one paragraph rewritten at band 8–9 | 60 min |
| `/writing1` | Timed Academic Task 1 drill (rotates chart/table/process/map), with specific checks on overview, grouping and data accuracy; band-8 model shown only after grading | 40 min |
| `/speaking` | Full three-part simulation with examiner-style pushback in Part 3, graded per criterion, plus five upgraded phrases | 30 min |
| `/reading` | An original 400–600 word academic passage plus 8–10 questions of my weakest type; afterwards, exactly which sentence held each answer and which paraphrase disguised it | 40 min |
| `/listening` | Text-adapted training: prediction drills, trap-spotting on written transcripts, spelling dictation, transfer discipline | 30 min |
| `/vocab` | ADD mode builds the bank with collocations by topic; QUIZ mode tests the 10 least-recently-tested items strictly | 20 min |
| `/mock` | Full timed 60-minute Writing test — both tasks, no help during, Task 2 double-weighted | 90 min |
| `/official` | Debrief an official Cambridge or ielts.org test done on paper: raw scores → bands, error-pattern analysis, writing graded | 30 min |
| `/review` | Weekly: score trends, top 3 recurring error patterns, gap to target, and a concrete 7-day plan | 30 min |
| `/handbook` | Regenerate `handbook.md` — my personal revision book built from my own logged data | — |
| `/anki` | Export the vocabulary bank to `exports/anki-vocab.csv` | — |

## Suggested daily routine — 90 minutes

The ratio that matters: **70% practice with feedback · 20% error review ·
10% theory.** Reading about IELTS does not raise your band; being corrected does.

| Day | Session |
|---|---|
| **Mon** | `/writing2` (60m) + `/vocab` QUIZ (20m) + reread yesterday's error-log rows (10m) |
| **Tue** | `/reading` (40m) + one official Reading passage, timed (40m) + log errors (10m) |
| **Wed** | `/writing1` (40m) + `/vocab` ADD (25m) + review top-3 error patterns (25m) |
| **Thu** | `/listening` (30m) + one official Listening test under real conditions (40m) + `/vocab` QUIZ (20m) |
| **Fri** | `/speaking` (30m) — record yourself on your phone — + `/writing2` (60m) |
| **Sat** | `/mock` (90m) every other week; otherwise official practice + `/official` debrief |
| **Sun** | `/review` (30m) + read one chapter of `knowledge/revision-playbook.md` (20m) + rest |

Two rules that matter more than the schedule:

1. **Do the error review.** The 20% you spend rereading your own logged mistakes
   is worth more than another drill. Errors you do not revisit, you repeat.
2. **Record yourself for Speaking.** This system reads text; it cannot hear you.
   Pronunciation is a quarter of your Speaking band and it is the one part you
   must close yourself.

---

## Official practice material

Practise on **genuine** material. Everything this system generates is original by
design — never a copy of a real test — which makes it good for technique but no
substitute for the real thing.

### Free, official

- **IELTS Academic sample test questions** — Listening, Reading, Writing,
  Speaking:
  <https://ielts.org/take-a-test/preparation-resources/sample-test-questions/academic-test>
- **British Council free practice tests** — full sections with answer keys, plus
  a computer-delivered familiarisation test:
  <https://takeielts.britishcouncil.org/take-ielts/prepare/free-ielts-english-practice-tests>
- **IDP practice tests:** <https://ielts.idp.com/about/practice-tests>
- **All ielts.org preparation resources:**
  <https://ielts.org/take-a-test/preparation-resources>
- **Academic Writing sample tasks (PDF):**
  <https://ielts.org/cdn/Sample-tests/ielts-academic-writing-sample-tasks-2023.pdf>
- **Sample candidate writing with examiner comments and band scores (PDF)** —
  the single most useful free document for calibrating what a band actually looks
  like. Read it early:
  <https://ielts.org/cdn/computer-delivered-sample-tests-academic-writing/ielts-academic-writing-example-responses-to-parts-1-and-2-with-band-scores-and-examiner-comments.pdf>

### Official band descriptors

- **Writing (Task 1 and 2), updated May 2023:**
  <https://takeielts.britishcouncil.org/sites/default/files/ielts_writing_band_descriptors.pdf>
- **Speaking (public version):**
  <https://assets.cambridgeenglish.org/webinars/ielts-speaking-band-descriptors.pdf>

### Worth buying

**Cambridge IELTS 15–20** (Academic). Past papers written by the test producers —
the only practice material with genuine difficulty calibration. Do these on
paper or screen under timed conditions, then run `/official` to convert your raw
scores and analyse the error pattern.

---

## Test format — verified 31 July 2026

Total test time **2 hours 45 minutes**.

| Paper | Format | Time |
|---|---|---|
| Listening | 4 parts, 40 questions | ~30 min |
| Reading (Academic) | 3 passages, 40 questions, 2,150–2,750 words | 60 min, **no transfer time** |
| Writing | Task 1 ≥150 words, Task 2 ≥250 words (**Task 2 counts double**) | 60 min |
| Speaking | 3 parts, face-to-face, recorded | 11–14 min |

### ⚠️ Paper-based IELTS is being discontinued

**From mid-2026 IELTS is no longer offered on paper** — all tests move to
computer, with timelines varying by market. This changes how you should train:

- **Listening on computer has no 10-minute transfer time.** You get **2 minutes**
  to check at the end. You must be accurate as you type, not tidy up afterwards.
- **Type your Writing practice.** Your real typing speed and on-screen
  proofreading are now part of your score.
- A **"Writing on Paper"** option (computer test, handwritten Writing) is
  appearing in selected markets.
- The skills assessed and how results are interpreted are **unchanged**.

**One Skill Retake** is available in 110+ countries but **could not be confirmed
for Tunisia** from official sources. Check with your test centre when you book —
do not assume it is your safety net. Details in `knowledge/sources.md`.

### Raw score to band

| Band | Listening | Academic Reading |
|---:|---:|---:|
| 5 | 16 | 15 |
| 6 | 23 | 23 |
| 7 | 30 | 30 |
| 8 | 35 | 35 |

Conversion varies slightly between test versions — planning targets, not
promises.

---

## What is in here

```
CLAUDE.md                      Coaching rules — loaded every session
handbook.md                    My personal revision book (via /handbook)
README.md                      This file
knowledge/
  band-descriptors.md          What bands 5–8+ look like, per criterion
  tricks.md                    Complete exam-technique reference
  revision-playbook.md         10-chapter strategy book (~4,000 words)
  sources.md                   What was verified, when, and from where
progress/
  error-log.md                 Every correction, with the rule
  vocab-bank.md                Vocabulary with collocations
  band-tracker.md              Every score over time
exports/
  anki-vocab.csv               Anki export (via /anki)
.claude/commands/              The 11 slash commands
.claude/skills/                60 Claude Code skills (see its README)
```

## A note on integrity

This system never reproduces official test material or the official band
descriptor wording. Practice passages, questions and cue cards are original.
`knowledge/band-descriptors.md` is a paraphrase written from the official public
documents — for any official purpose, read those directly. `/official` never asks
you to paste copyrighted passages; you report scores and question types, and
paste only your own writing.
