---
name: review
description: Weekly review — score trends, top 3 recurring error patterns, gap to target band, and a concrete 7-day plan.
---

# Weekly review

Run this once a week. It is the command that makes the rest of the system
cumulative rather than a series of disconnected drills.

## Step 1 — Read everything

Read all three progress files in full:
- `progress/band-tracker.md`
- `progress/error-log.md`
- `progress/vocab-bank.md`

Also read the "Current weak areas" and test-date lines in `CLAUDE.md`.

If there is too little data to review honestly, **say so** rather than
manufacturing trends from two data points. Tell me what to run this week to
generate enough.

## Step 2 — Report score trends

A table per skill, oldest to newest, with the direction of travel:

| Skill | Sessions | First | Latest | Best | Trend |
|---|---:|---:|---:|---:|---|
| Writing T2 | 4 | 5.5 | 6.5 | 6.5 | ↑ improving |
| Reading | 3 | 6.0 | 6.0 | 6.5 | → flat |

For Writing, break out the **four criteria separately** — the overall band hides
which criterion is stuck. A writer whose GRA has been 5.5 for four sessions has a
grammar problem, not a writing problem.

Be honest about flat or declining trends. Say plainly if something is not
working.

## Step 3 — Top 3 recurring error patterns

From `progress/error-log.md`, count errors by **category**, not by instance:

| Rank | Pattern | Count | Sessions seen | Example from my writing |
|---:|---|---:|---:|---|
| 1 | Articles with abstract nouns | 11 | 5 of 6 | "the society is changing" |
| 2 | Uncountable nouns pluralised | 7 | 4 of 6 | "many informations" |
| 3 | Undeveloped body paragraphs | 5 | 3 of 6 | — |

For each: name the rule in one sentence, and give the **fix strategy** — the
specific thing to check for in the next piece of writing.

Flag separately any error that is **still recurring after being logged three or
more times**. That is a habit, not a mistake, and needs a different approach —
usually a pre-submission checklist item rather than more explanation.

## Step 4 — Gap to target

Current estimated overall band, the arithmetic, and the distance to 7.0:

> Current: L 6.5 · R 6.5 · W 6.0 · S 6.5 → average 6.375 → **6.5**
> Target: **7.0**
> Cheapest route: Reading 6.5 → 7.0 needs 30/40, about 3 more correct answers,
> and your T/F/NG accuracy is 40%. That single question type is your band.

Show at least two viable routes to 7.0 using the routes table in
`knowledge/tricks.md` — you do not need 7 in every skill.

If a test date is set in `CLAUDE.md`, state days remaining and whether the
current trajectory reaches 7.0 in time. Be straight about it; a comfortable
answer that turns out wrong on test day helps nobody.

## Step 5 — A concrete 7-day plan

Not advice — a schedule. Seven rows, one per day, sized to **90 minutes**, each
naming the exact command to run:

| Day | Focus | Session (90 min) |
|---|---|---|
| Mon | Weakest criterion | `/writing2` — opinion essay, target Task Response (45m) + `/vocab` QUIZ (20m) + review last 3 error-log rows (25m) |
| Tue | Reading technique | `/reading` — T/F/NG focus (40m) + official free Reading passage, timed (50m) |

Rules for the plan:
- Follow the **70 / 20 / 10** split: 70% practice with feedback, 20% error
  review, 10% theory.
- Every day must include something from the top-3 error patterns.
- Include at least one full official practice section from `README.md`.
- Include one rest or light day if the previous week was heavy — fatigue lowers
  scores.

## Step 6 — Update CLAUDE.md

Rewrite the **"Current weak areas"** section of `CLAUDE.md` with what the data
now shows. Be specific: not *"grammar"* but *"complex sentences attempted but
faulty — GRA stuck at 5.5–6.0 across five sessions; articles and uncountables
dominate"*.

This is what makes future sessions target the right thing automatically.

## Step 7 — Commit and push

`review: week of <date> — overall ~x.x, top pattern <name>, plan set`

## Step 8 — End

One line: the single thing to concentrate on this week.
