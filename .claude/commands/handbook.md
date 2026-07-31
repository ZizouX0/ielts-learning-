---
name: handbook
description: Regenerate handbook.md — my personal revision book, built entirely from my own logged data.
---

# Regenerate my personal handbook

Rebuild `handbook.md` at the repo root, **overwriting** the previous version.

This is not a general IELTS guide — `knowledge/revision-playbook.md` already is
one. This is **my** book: every section built from **my** logged data, using
**my** sentences. If a section cannot be filled from my progress files, leave it
out rather than padding it with generic advice.

**Hard limit: under 8 pages** (roughly 3,500 words). It has to be readable in one
sitting the night before the test. Cut ruthlessly — the value is in what you
leave out.

## Source data

Read, in full:
- `progress/error-log.md`
- `progress/vocab-bank.md`
- `progress/band-tracker.md`
- `CLAUDE.md` (weak areas, test date)
- `knowledge/tricks.md` (pull only what matches my weaknesses)

If there is not enough data yet, say so and generate what you can, marking thin
sections clearly.

## Structure

### 1. Where I stand (½ page)
Current band per skill, most recent and best. Weighted Writing band. Estimated
overall. Gap to 7.0, and the cheapest route to close it. Days until the test if
the date is set.

### 2. My top 10 recurring mistakes (2 pages) — the core of the book
The ten highest-frequency errors from **my** error log, ranked by how often they
appear.

For each: **my actual sentence**, the correction, the rule in one line, and the
check that catches it.

> **3. Pluralising uncountable nouns** — logged 7 times
> **I wrote:** "There are many informations available on the internet."
> **Correct:** "There is a great deal of information available online."
> **Rule:** *information, research, advice, knowledge, equipment* are uncountable
> in English though countable in French. Never add -s; never use *a/many*.
> **Check:** scan every noun ending in -s and ask whether it is on the list.

Use my real sentences. Recognising my own wrong words is what makes this stick.

### 3. My personal L1 danger list (1 page)
Only the French/Arabic interference patterns **I have actually made** — not the
full list from `CLAUDE.md`. Ordered by frequency in my log. Each with the trigger
that produces it and the 5-second check that catches it.

### 4. The tricks that matter for me (1½ pages)
From `knowledge/tricks.md`, only the techniques addressing **my** weakest areas.
If my Reading T/F/NG accuracy is 40%, the full T/F/NG logic goes in. If my
Listening is already 7.5, Listening gets three lines.

Ruthless selection. A handbook covering everything covers nothing.

### 5. Vocabulary I have not mastered (1 page)
From `progress/vocab-bank.md`: items never tested, items I got wrong, items
untested longest. Word + collocation + one example each. Skip anything I have
reliably got right — I do not need to revise what I know.

### 6. My pre-submission checklists (½ page)
Task 1 and Task 2 checklists built from **my own** most expensive recurring
errors, in the order I should check them. Not a generic checklist.

### 7. Exam-day protocol (½ page)
Timings per paper, the computer-delivered specifics (no Listening transfer time,
2-minute check; word count on screen), what to do when panicking, guessing rules,
and the one instruction I most need to remember based on my error history.

## After generating

1. Tell me what changed since the last version — improved areas, new patterns,
   errors that dropped off.
2. Report the word count and confirm it is under the 8-page limit.
3. Offer to export to PDF (the `pdf` skill and reportlab are available; write to
   `exports/handbook.pdf`).
4. Commit and push: `handbook: regenerated from progress data — <date>`
