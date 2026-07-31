---
name: official
description: Process an official Cambridge or IELTS practice test I did on paper — convert raw scores to bands, analyse error patterns, grade my writing.
---

# Official test debrief

For tests I do on genuine material (Cambridge IELTS books, official free tests).

## Copyright rule — non-negotiable

**Never ask me to paste passages, questions, transcripts or answer keys from
copyrighted material.** Not Cambridge books, not official practice tests, not
anything published.

I report **numbers and categories**. I paste only **my own writing**, which is
mine to share.

If I paste copyrighted content anyway, do not reproduce it back in your response,
and remind me once that we do not need it — the debrief works from my data alone.

## Step 1 — Collect the data

Ask me for whichever of these apply:

**Listening / Reading:**
- Which test (e.g. "Cambridge 18, Test 2, Academic Reading")
- **Raw score out of 40**
- **Which question numbers I got wrong**
- **What type each wrong question was** (T/F/NG, matching headings, MCQ, note
  completion, map labelling, etc.)
- Whether I finished in time, and where I lost time

**Writing:** paste my own answers, plus a description of the task in my own words
(*"line graph, coffee consumption in four countries, 1990–2020"*) — not the
original prompt text.

**Speaking:** the topics I was asked about and my own notes on how it went.

Do not proceed until I have given you the raw scores. If I only have a total,
work with that but say the error-type analysis will be weaker.

## Step 2 — Convert raw scores to bands

Use the table in `knowledge/tricks.md`:

| Band | Listening | Academic Reading |
|---:|---:|---:|
| 5 | 16 | 15 |
| 6 | 23 | 23 |
| 7 | 30 | 30 |
| 8 | 35 | 35 |

State the band for each, **and state the official caveat**: conversion varies
slightly between test versions, so this is an estimate, not a guarantee.

Then show the gap: marks needed for the next half band, and how many more correct
answers that is. Concrete numbers, e.g. *"27/40 is band 6.5. Three more correct
answers is band 7."*

## Step 3 — Analyse the error pattern

This is the real value of the command. Group my wrong answers by **question
type**, not by number:

| Question type | Wrong | Total | Accuracy |
|---|---:|---:|---:|
| True/False/Not Given | 4 | 6 | 33% |
| Matching headings | 1 | 5 | 80% |

Then diagnose:
- Which type is bleeding marks? That is the next drill.
- Were errors clustered in one passage/section? → a timing problem, not a skill
  problem.
- Were they spread evenly? → a technique problem.
- Any pattern in the **last** questions of a section? → running out of time.

Compare against previous entries in `progress/band-tracker.md`. Is the same type
failing repeatedly?

## Step 4 — Grade my writing

Grade exactly as in `/writing1` and `/writing2` — full criterion tables, evidence
quoted from my text, strict banding, weighted Writing band if both tasks are
present. Fix 3–5 sentences with the rule behind each.

## Step 5 — Estimate the overall band

Combine whatever skills I have data for:

> L 6.5 · R 6.0 · W 6.0 · S (no data)
> Provisional across three skills: 6.17
> With Speaking at 6.5: (6.5+6.0+6.0+6.5) ÷ 4 = 6.25 → **6.5 overall**
> To reach 7.0: ...

State the distance to band 7.0 and which skill is the cheapest place to find it.
Usually Listening and Reading — objective, trainable, technique-driven.

## Step 6 — Prescribe

Two or three specific actions, each tied to a command in this repo:
*"Your T/F/NG accuracy is 33%. Run `/reading` twice this week — I'll target
T/F/NG both times."*

## Step 7 — Log and push

Append to `progress/band-tracker.md`, marked **OFFICIAL** with the test name.
Error patterns to `progress/error-log.md`. Commit and push:
`progress: OFFICIAL <test name> — L x/40 (band x), R x/40 (band x), W band x`

## Step 8 — End the session

One line: the single highest-impact fix.
