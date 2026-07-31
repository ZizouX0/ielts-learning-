# V3 — Coverage Audit (adversarial)

**Auditor:** V3 — Coverage Auditor
**Date:** 2026-07-31
**Scope:** all nine chapters in `ielts-book/chapters/`
**Method:** The master list below was compiled **before any chapter was opened**, from
ielts.org format pages, the official 2023 sample-task PDFs (downloaded and text-extracted,
not summarised from a search result), the official *IELTS Guide for Teachers*, the official
Writing Key Assessment Criteria PDF, and the British Council / IDP teaching pages.
`ielts-book/research/` was **not** consulted at any point — not before, not during, not to
resolve a disputed item. Diffing began only after the list was closed.

**Headline.** Coverage is unusually strong. Every official Listening and Reading question
type is present and fully treated; the Reading 11-vs-14 framing question is answered
correctly and defensibly; the mandated eight sections are present in all nine chapters
(verified mechanically). Two genuine holes survive: a Writing Task 1 input type named in
IELTS's own rubric that has no section, and a Speaking Part 2 element that appears once as a
table cell. Four appendix deliverables are absent from the repository entirely.

---

## Independent master list

### Listening — question types

Source of record: `https://ielts.org/take-a-test/test-types/ielts-academic-test/ielts-academic-format-listening`
(6 named types), cross-checked against the official sample-tasks PDF
`https://ielts.org/cdn/ielts-sample-tests/ielts-listening-sample-tasks-2023.pdf`.

| # | Official type | Sub-shapes attested in the sample PDF |
|---|---|---|
| L1 | Multiple choice | 3 options / one answer; longer list, choose 2–3 |
| L2 | Matching | "Matching 1" (repeatable criteria) and "Matching 2" (one-to-one from a box) — the PDF ships **two separate sample tasks** |
| L3 | Plan/map/diagram labelling | letters from a box; free-written within a word limit |
| L4 | Form / note / table / flow-chart / summary completion | Form Completion and Note Completion both ship as separate samples |
| L5 | Sentence completion | — |
| L6 | Short-answer questions | paired items sharing one prompt; official key marks them **in either order** |

**Discrepancy found, worth recording.** The 2023 Listening sample-tasks PDF's own
introduction lists only **five** types — it omits short-answer questions — while shipping a
short-answer sample task and answer key on pp. 11–13. The format page's **six** is current
and correct. (`v3-listen.txt`, p.1 vs contents.)

**Four parts** (same source, plus *IELTS Guide for Teachers* p.–):
Part 1 conversation, everyday/social; Part 2 monologue, everyday/social; Part 3 dialogue
(ielts.org "two main speakers", British Council "up to four"), educational/training;
Part 4 monologue/lecture, educational/training. Recording plays once. Five national accents.

### Academic Reading — question types

**The 11-vs-14 question, settled.** Both framings are live and current, from the same owner:

- ielts.org's format page defines **11 numbered task types** — verified by direct fetch;
  the page literally numbers them "Academic Reading Question Type 1 … Type 11".
  `https://ielts.org/take-a-test/test-types/ielts-academic-test/ielts-academic-format-reading`
- The 2023 sample-tasks PDF's own p.1 preamble names **14** by splitting Type 9 into
  summary / note / table / flow-chart completion.
  `https://ielts.org/cdn/Sample-tests/ielts-academic-reading-sample-tasks-2023.pdf`

Neither supersedes the other; the format page is the *numbered* definition and is the
defensible spine. **The book's choice of 11 is correct.**

| # | Official type | Sub-variants shipped as separate samples in the 2023 PDF |
|---|---|---|
| R1 | Multiple choice | **one answer** *and* **more than one answer** — two distinct sample tasks; the multi-answer key reads "IN EITHER ORDER" and occupies two question numbers |
| R2 | Identifying information (True/False/Not Given) | — |
| R3 | Identifying writer's views/claims (Yes/No/Not Given) | — |
| R4 | Matching information | — |
| R5 | Matching headings | — |
| R6 | Matching features | — |
| R7 | Matching sentence endings | — |
| R8 | Sentence completion | — |
| R9 | Summary / note / table / flow-chart completion | **Summary Completion: selecting from a list of words/phrases**; **Summary Completion: selecting words from the text**; **Flow-chart Completion: selecting words from the text**; **Note Completion**; **Table Completion** — five separate samples |
| R10 | Diagram label completion | — |
| R11 | Short-answer questions | — |

Passage facts (format page): 3 passages, 40 questions, 60 min, no extra transfer time,
2,150–2,750 words, at least one text with detailed logical argument, texts may contain
diagrams/graphs/illustrations, glossary provided for technical vocabulary.

### Writing Task 1 (Academic) — input types

Two official statements, and they do not enumerate identically:

- Format page: *"one or more graphs, charts or tables"* and *"a diagram of an **object,
  device, process or event**"*.
  `https://ielts.org/take-a-test/test-types/ielts-academic-test/ielts-academic-format-writing`
- Writing Key Assessment Criteria PDF, p.2: *"a diagram, graph, table, chart, **map** or
  other visual input"* — this is the only official document I found that names **map**.
  `https://ielts.org/cdn/ielts-guides/ielts-writing-key-assessment-criteria.pdf`
- *IELTS Guide for Teachers*: *"a table, graph, chart, or diagram"*.
  `https://ielts.org/cdn/ielts-guides/ielts-guide-for-teachers.pdf`
- IDP's teaching page enumerates line graph, bar chart, pie chart, table, process diagram,
  **map**, and explicitly names **combination tasks** ("a graph and a pie chart, or a table
  and a bar graph … happens quite often").
  `https://ielts.idp.com/prepare/article-ielts-writing-task-1-question-types`

Master list of inputs the reader must be able to handle:

1. Line graph
2. Bar chart (time-series and categorical)
3. Pie chart
4. Table
5. Process diagram — man-made / linear
6. Process diagram — natural / cyclical
7. Map comparison
8. Combination / multiple visuals on one prompt
9. **Diagram of an object, device or event — static, non-process** (format page wording;
   e.g. two designs of the same device compared, a labelled cross-section, a floor plan of a
   building shown as an object rather than a before/after map)

Rubric is fixed and verbatim on all three official 2023 Task 1 samples: *"Summarise the
information by selecting and reporting the main features, and make comparisons where
relevant."* — 20 minutes, at least 150 words. The three shipped samples are a **bar chart**
(1A), a **line graph** (1B) and a **process diagram** (1C).

### Writing Task 2 — prompt types

**IELTS publishes no official taxonomy — verified true.** It is absent from the format page,
the sample-tasks PDF, the Key Assessment Criteria PDF and the band descriptors. The format
page instead names four *abilities*: present a solution to a problem; present and justify an
opinion; compare and contrast evidence, opinions and implications; evaluate and challenge
ideas, evidence or an argument.

The two owners teach non-matching lists. IDP names seven
(`https://ielts.idp.com/about/news-and-articles/article-how-to-understand-task-2-writing-questions`):
opinion; discussion; multi-part; multi-part + opinion; advantage/disadvantage;
positive/negative development; cause/solution. British Council teaches five.

The two official 2023 sample tasks are an **opinion** prompt (*"To what extent do you agree
or disagree with this opinion?"*) and an **outweigh** prompt (*"Do the disadvantages of
international tourism outweigh the advantages?"*). Rubric: *"Give reasons for your answer and
include any relevant examples from your own knowledge or experience. Write at least 250
words."* 40 minutes.

Master list — the shapes a reader must recognise: opinion/agree-disagree · discussion (both
views + own opinion) · advantages–disadvantages, including the *outweigh* verdict form ·
problem/cause/solution · positive-or-negative development · two-part / direct question ·
hybrids of the above.

### Speaking

`https://ielts.org/take-a-test/test-types/ielts-academic-test/ielts-academic-format-speaking`
plus `https://ielts.org/cdn/ielts-sample-tests/ielts-speaking-sample-tasks-2023.pdf`.

- **Part 1 — Introduction and interview**, 4–5 min. ID check, then interview in topic blocks.
  Official frame shows *"Let's talk about your home town or village"* (4 questions) →
  *"Let's move on to talk about accommodation"* (4 questions).
- **Part 2 — Individual long turn**, 3–4 min. Task card; 1 minute preparation; pencil and
  paper for notes; speak 1–2 minutes; then **"Rounding off questions"** — the PDF's own
  heading — one or two short questions on the same topic. The official card is
  *"Describe something you own which is very important to you"* with three "You should say"
  bullets plus an explain-clause, and rounding-off questions *"Is it valuable in terms of
  money?"* / *"Would it be easy to replace?"*
- **Part 3 — Two-way discussion**, 4–5 min. Themed sub-blocks tied to the Part 2 topic
  (*"Let's consider first of all how people's values have changed"* → *"Finally, let's talk
  about the role of advertising"*), abstract/general treatment, examiner pushback.
- **Cue-card shapes.** No official taxonomy exists. The attested shape is
  bullets + final explain-clause; the shipped card is an **object** card. The functional
  families in circulation (person / place / object / event or experience / activity /
  media / abstract idea / future plan) are teaching convention, not official.

### Computer-delivered vs paper — every difference that matters

- Listening: paper 10 minutes transfer; **computer 2 minutes to check, no transfer time**.
- Reading: transfer inside the 60 minutes in both modes; computer adds a highlighter,
  note tool, on-screen timer, free navigation.
- Writing: computer shows a **live word count**, autosaves, allows moving between tasks
  freely; no spellchecker.
- Test-taking order and results turnaround differ (computer 1–5 days vs paper ~13).
- *"There is no difference to the test questions, or format, only the way you complete your
  answers."*
  `https://ielts.org/take-a-test/why-choose-ielts/ways-to-take-ielts`

---

## Coverage matrix

**Quality key:** *full* = looks-like + rules + trap + technique + worked example + band-6
mistake. *mentioned only* = named but missing most of that. *absent* = not present.

### Listening

| Item | Covered? | Chapter / section | Quality |
|---|---|---|---|
| Multiple choice — one answer | Yes | Ch 2 §7 | full |
| Multiple choice — more than one | Yes | Ch 2 §8 | full |
| Matching (a) repeatable criteria | Yes | Ch 2 §9 | full |
| Matching (b) one-to-one from box | Yes | Ch 2 §9 | full |
| Plan / map / diagram labelling | Yes | Ch 2 §10 | full (+ L1-specific preposition drill) |
| Form completion | Yes | Ch 2 §1 | full |
| Note completion | Yes | Ch 2 §2 | full |
| Table completion | Yes | Ch 2 §3 | full |
| Flow-chart completion | Yes | Ch 2 §4 | full |
| Summary completion | Yes | Ch 2 §5 | full |
| Sentence completion | Yes | Ch 2 §6 | full |
| Short-answer questions | Yes | Ch 2 §11 | full (incl. either-order key rule) |
| Four parts — content, voices, register | Yes | Ch 2 "What the test actually asks" table | full |
| Accents (5 nationalities) | Yes | Ch 2 | full |
| Plays once / order-is-guaranteed / no negative marking | Yes | Ch 2 | full |
| Paper-vs-computer timing | Yes | Ch 2 §🖥️; Ch 1 | full |
| Sample-PDF's own 5-vs-6 type discrepancy | No | — | absent (see MINOR-2) |
| The six official type names listed in Ch 1 | No | Ch 1 Listening block | absent (see MINOR-1) |

### Academic Reading

| Item | Covered? | Chapter / section | Quality |
|---|---|---|---|
| 11-vs-14 framing, and which is used | Yes | Ch 3 §"11 types or 14?" | full and correctly argued |
| R1 Multiple choice — one answer | Yes | Ch 3 Type 1 | full |
| R1 Multiple choice — **more than one answer** | Partly | Ch 3 Type 1, one clause | **mentioned only** (see MAJOR-1) |
| R2 T/F/NG | Yes | Ch 3 Type 2 + dedicated decision procedure | full, best-in-book |
| R3 Y/N/NG | Yes | Ch 3 Type 3 | full |
| R4 Matching information | Yes | Ch 3 Type 4 | full |
| R5 Matching headings | Yes | Ch 3 Type 5 | full |
| R6 Matching features | Yes | Ch 3 Type 6 | full |
| R7 Matching sentence endings | Yes | Ch 3 Type 7 | full |
| R8 Sentence completion | Yes | Ch 3 Type 8 | full |
| R9 Summary completion — from the text | Yes | Ch 3 Type 9, variation 1 | full |
| R9 Summary completion — from a word bank | Yes | Ch 3 Type 9, variation 2 | full (correctly notes bank words are often absent from the passage) |
| R9 Note / table / flow-chart completion | Yes | Ch 3 Type 9 | full |
| R10 Diagram label completion | Yes | Ch 3 Type 10 | full |
| R11 Short-answer questions | Yes | Ch 3 Type 11 | full |
| Order-in-passage table, all 11 types | Yes | Ch 3 §"The order table" | full, with honest sourcing caveats |
| Passage facts, glossary, non-verbal material | Yes | Ch 3 opening | full |
| Computer highlighter / copy-paste / timer | Yes | Ch 1; Ch 3 Tips; Ch 9 | full |

### Writing Task 1

| Item | Covered? | Chapter / section | Quality |
|---|---|---|---|
| Line graph | Yes | Ch 4 §1 | full |
| Bar chart | Yes | Ch 4 §2 | full |
| Pie chart | Yes | Ch 4 §3 | full |
| Table | Yes | Ch 4 §4 | full |
| Process diagram — man-made | Yes | Ch 4 §5 | full |
| Process diagram — natural / cyclical | Yes | Ch 4 §6 | full |
| Map comparison | Yes | Ch 4 §7 | full |
| Combination / multiple visuals | Yes | Ch 4 §8 | full |
| **Diagram of an object / device / event (static)** | No | quoted at Ch 4 l.99, never taught | **absent** (see CRITICAL-1) |
| "or other visual input" — what "other" covers | No | quoted, never unpacked | absent (see MINOR-3) |
| Fixed rubric wording | Yes | Ch 4 opening | full |
| Tense-by-visual decision table | Yes | Ch 4 | full — genuinely good |
| Word count mechanism (TA, not a tariff) | Yes | Ch 4 opening | full |
| Copied rubric discounted | Yes | Ch 4 opening | full, triple-sourced |
| Computer word counter / start-with-either-task | Yes | Ch 4 §🖥️ | full |

### Writing Task 2

| Item | Covered? | Chapter / section | Quality |
|---|---|---|---|
| "No official taxonomy exists" — stated | Yes | Ch 5 §preamble + Myth M12 | full, and correct |
| Opinion / agree–disagree | Yes | Ch 5 Family 1 | full |
| Discussion (both views + opinion) | Yes | Ch 5 Family 2 | full |
| Problem / cause / solution | Yes | Ch 5 Family 3 | full |
| Advantages–disadvantages, incl. *outweigh* | Yes | Ch 5 Family 4 | full |
| Positive-or-negative development | Yes | Ch 5 Family 5 | full |
| Two-part / direct question | Yes | Ch 5 Family 5 | full |
| Hybrids, and the "count the demands" rule | Yes | Ch 5 §30-second triage | full |
| 250-word floor, copied rubric, bullet points | Yes | Ch 5 | full |

### Speaking

| Item | Covered? | Chapter / section | Quality |
|---|---|---|---|
| Part 1 — format, topic blocks, timing | Yes | Ch 6 Part 1 | full |
| Part 2 — card structure, 1 min prep, notes | Yes | Ch 6 Part 2 | full |
| Part 2 — **rounding-off questions** | Barely | Ch 6, one table cell (l.12) | **mentioned only** (see MAJOR-2) |
| Part 2 — **range of cue-card shapes** | No | one example card only | **absent as a taxonomy** (see MAJOR-3) |
| Part 3 — discussion, pushback, answer shape | Yes | Ch 6 Part 3 | full |
| Four criteria + the two grid footnotes | Yes | Ch 6 opening | full |
| Face-to-face vs video call | Yes | Ch 6 opening; Ch 1; Ch 9 | full, with the conflict flagged |
| Asking for repetition / clarification by part | Yes | Ch 6 table | full, with sourcing honestly caveated |

### Cross-cutting

| Item | Covered? | Where | Quality |
|---|---|---|---|
| Mandated 8 sections in all 9 chapters | Yes | verified mechanically, 9/9 | full |
| Paper vs computer, everywhere it matters | Yes | Ch 1, 2, 3, 4, 9 | full |
| Band math: raw→band, averaging, .25/.75 rounding | Yes | Ch 1 | full |
| Descriptor tables per criterion | Partly | Ch 4, 5, 6, 8 | bands 6/7/8 only (see MINOR-4) |
| **Appendix: full descriptor summary tables** | No | — | absent (see MAJOR-4) |
| **Appendix: complete question-type index** | No | — | absent (see MAJOR-5) |
| **Appendix: Arabic/French error quick-reference** | Scattered | Ch 8 sweeps + error map; Ch 7 false-friend list | material exists, no consolidated reference (see MINOR-5) |
| **Appendix: pre-test-day checklist** | Scattered | Ch 9 tables + self-test checklist | material exists, no single day-before checklist (see MINOR-6) |

---

## Findings

### [CRITICAL] — the static diagram of an object, device or event is absent

**Should be in:** Chapter 4 (Writing Task 1), as a ninth type in "Question types, one by one"
**Source establishing it exists:** `https://ielts.org/take-a-test/test-types/ielts-academic-test/ielts-academic-format-writing` — *"a diagram of an **object, device**, process or event"*; corroborated by `https://ielts.org/cdn/ielts-guides/ielts-guide-for-teachers.pdf` (*"a table, graph, chart, or diagram"*)

The chapter quotes this exact rubric wording at line 99, then builds an eight-way split in
which every "diagram" is a **process**. There is no section for a diagram that is not a
process and not a before/after map: two designs of the same device compared side by side, a
labelled cross-section of an object, a static floor plan, a diagram of an *event*. The reader
is left with two toolkits — the trend/comparison apparatus (needs figures) and the process
apparatus (needs a sequence) — and this input has neither. On the day it would read as an
unfamiliar task, and the chapter's own tense table has no row for it.

**What the chapter must add:** a section "§9 — Static diagram (object, device, event)" with
the mandated treatment: what it looks like (two comparable objects/designs, or one labelled
artefact); the rule that the fixed rubric still says *make comparisons where relevant*, so
the organising principle is **comparison of features, not sequence**; the tense (present
simple, or past for a historical artefact) and a new row in the tense-by-visual table; the
trap (writing a bullet-by-bullet inventory of every label — the same "list, don't group" TA
failure the chapter already names for process); the technique (group by **function or
component**, e.g. structure / power source / user interface, not by picking one object and
then the other); a worked overview and a band-6 mistake, matched to the format of §5–§8. It
must also say plainly that **no trend verb applies** — there is no time axis — because the
chapter's trend toolkit is otherwise the reader's default.

---

### [MAJOR] — Reading multiple choice "more than one answer" is a clause, not a variant

**Should be in:** Chapter 3, Type 1
**Source establishing it exists:** `https://ielts.org/cdn/Sample-tests/ielts-academic-reading-sample-tasks-2023.pdf` — ships **two separate sample tasks**, "Multiple Choice: one answer" and "Multiple Choice: more than one answer" (pp. 24–26), the latter with the key *"1&2 IN EITHER ORDER"*

Type 1 disposes of the multi-answer variant in a subordinate clause — *"sometimes a longer
list from which you choose more than one"* — and then gives its rules, trap, technique,
worked example and band-6 mistake entirely for the four-option single-answer form. This is
inconsistent with the book's own standard: Chapter 2 gives Listening's multiple-answer form a
full dedicated section (§8) with its own trap and worked example. The mechanics differ
materially — two question numbers, two marks, either order accepted, seven options rather
than four, and the distractor logic is exclusion across a long list rather than discrimination
between four.

**What the chapter must add:** a "Variation" block inside Type 1, parallel to the
two-variation table already used for Type 9. It must state: the item occupies **two (or three)
question numbers and is worth that many marks**; answers are accepted **in either order**
(officially confirmed in the 2023 key); option lists run A–G or A–F; and it must carry its own
mini-example and its own band-6 mistake (selecting one letter for a two-mark item, or
treating the option list as running in passage order when a multi-answer item is not
guaranteed to).

---

### [MAJOR] — Speaking Part 2 rounding-off questions get one table cell and no treatment

**Should be in:** Chapter 6, Part 2
**Source establishing it exists:** `https://ielts.org/cdn/ielts-sample-tests/ielts-speaking-sample-tasks-2023.pdf` p.5 — the heading **"Rounding off questions"** is IELTS's own, with the two official examples *"Is it valuable in terms of money?"* and *"Would it be easy to replace?"*, and the transcript shows the examiner asking one and the candidate answering in a single sentence

The words "rounding-off questions" appear exactly once in the entire book, inside a cell of
the format table at line 12. Part 2 is otherwise treated to five pages. This is an examined
stretch of speech — it is inside the 3–4 minutes of Part 2, it is rated on the same four
criteria, and the official transcript shows the sample candidate producing a thin two-clause
answer to it immediately after a strong long turn. A candidate who mentally "finishes" when
the examiner says *thank you* will answer these flat.

**What the section must add:** what they look like (one or two short, concrete, closed
questions about the same card topic); the rule that they are **part of Part 2 and are rated**;
the trap (treating them as small talk and answering in three words, immediately after two
minutes of your best English — the contrast is audible); the technique (answer + one clause of
reason, no more — they are not a second long turn, and over-running them eats Part 3 time);
a worked band-6 vs band-7 pair on the official card's own rounding-off question; and the
band-6 mistake (a bare *"Yes"* or *"No, it wouldn't"*).

---

### [MAJOR] — the range of Part 2 cue-card shapes is never mapped

**Should be in:** Chapter 6, Part 2
**Source establishing the range:** `https://ielts.org/cdn/ielts-sample-tests/ielts-speaking-sample-tasks-2023.pdf` (an **object** card: *"Describe something you own which is very important to you"*) against `https://ielts.org/take-a-test/test-types/ielts-academic-test/ielts-academic-format-speaking` (*"a task card which asks you to talk about a particular topic"*, *"instructs you to explain one aspect of the topic"*)

The chapter teaches Part 2 through a single invented card (*Describe a skill you learned from
someone in your family*) and never tells the reader what else a card can ask. Because IELTS
publishes no taxonomy, this is not an omitted *official* type and so is not CRITICAL — but the
consequence is real and specific to this reader. Card shape determines **tense**, and tense is
this reader's costliest grammar area: a *describe a person* card runs in present + habitual
past, a *describe an event* card in past simple + past continuous, a *describe a plan* card in
future + conditional. The book's own Chapter 4 makes exactly this move for Task 1 (a
tense-by-visual table) and it is the strongest thing in that chapter. Part 2 gets nothing
equivalent.

**What the section must add:** a short table of card families — person · place · object ·
event or experience · activity or habit · media (a book/film/programme) · abstract idea ·
future plan — each with the dominant tense, the one structure worth planting, and the
characteristic failure. It must be labelled explicitly as **a preparation heuristic, not an
official taxonomy**, in the same voice Chapter 5 already uses for the Task 2 families, and it
must not imply IELTS publishes such a list.

---

### [MAJOR] — no full band-descriptor summary tables anywhere in the book

**Should be in:** a new appendix, or Chapter 1's "Band descriptor decoder"
**Source establishing they exist:** `https://ielts.org/cdn/ielts-guides/ielts-writing-band-descriptors.pdf` and `https://ielts.org/cdn/ielts-guides/ielts-speaking-band-descriptors.pdf` — the public grids run bands 0–9 across all four criteria for each of Writing Task 1, Writing Task 2 and Speaking

The book paraphrases descriptors well but only ever bands **6, 7 and 8**, split across four
chapters, one criterion at a time, in prose-heavy tables. There is no single place a reader
can see all four criteria for a task side by side. That is precisely what is needed when
self-marking, which Chapter 9 instructs the reader to do weekly ("mark one criterion per pass
against the real public descriptors") — the book sends the reader out to the PDFs for the one
task it should have made cheap.

**What must be added:** three consolidated tables — Writing Task 1, Writing Task 2, Speaking —
each with four criteria as columns and bands **5 through 8** as rows (5 matters: it is the
band a bad day produces, and the reader needs to recognise it in his own work). One cell per
criterion-band, paraphrased, with at most one short quoted phrase, consistent with the
copyright rule the chapters already follow. Cross-reference each cell to the chapter section
that decodes it.

---

### [MAJOR] — no complete question-type index

**Should be in:** an appendix
**Source establishing the type inventory:** ielts.org format pages for Listening (6 types) and Reading (11 numbered types), plus the 2023 sample-task PDFs

There is no index of any kind — the string "appendix" does not occur anywhere in
`ielts-book/`, and `ielts-book/book/` is empty. A 70,000-word reference book whose central
organising unit is the question type has no way to get from "I just got a matching-features
question wrong" to the four pages that fix it. The reader is on 90 minutes a day; a lookup
that costs a scroll through Chapter 3 costs him practice minutes.

**What must be added:** a single table listing every Listening layout (11), every Reading type
(11), every Task 1 input (9 once CRITICAL-1 is fixed), every Task 2 family (5) and the three
Speaking parts — each row giving the official name, the chapter and section anchor, and the
one-line "band-6 mistake" for that type, so the index doubles as a revision sweep.

---

### [MINOR] — Chapter 1 lists all 11 Reading types but none of the 6 Listening types

**Should be in:** Chapter 1, "Listening — approximately 30 minutes, 4 parts, 40 questions"
**Source:** `https://ielts.org/take-a-test/test-types/ielts-academic-test/ielts-academic-format-listening`

Chapter 1 enumerates the eleven Academic Reading types in full and then says "Chapter 3 takes
them one at a time." The Listening block does no such thing — it covers timing, the
play-once rule and the transfer-time difference, but never names the six official types before
handing off to Chapter 2. The asymmetry makes Chapter 1 unusable as the orientation map it is
trying to be.

**What the chapter must add:** one sentence naming the six official types, with the note that
Chapter 2 splits the completion family into separate layouts and why.

---

### [MINOR] — the Listening sample-PDF's own 5-vs-6 type discrepancy is unrecorded

**Should be in:** Chapter 2, "Question types, one by one"
**Source:** `https://ielts.org/cdn/ielts-sample-tests/ielts-listening-sample-tasks-2023.pdf` p.1 lists five types, omitting short-answer questions, while pp. 11–13 ship a short-answer sample task and key

Chapter 2 states "Officially there are six named types", which is right. But the book's whole
method is to surface exactly this kind of official self-contradiction (it does so for Part 3
speaker counts, results timing, the stationery rule, and the Reading 11-vs-14). A reader who
downloads the sample PDF — which Chapter 9 tells him to do — will find a five-item list and
have no way to reconcile it.

**What the chapter must add:** one line noting the sample PDF's preamble omits short-answer
questions while shipping one, and that the format page's six is authoritative.

---

### [MINOR] — "or other visual input" is quoted but never unpacked

**Should be in:** Chapter 4, "Question types, one by one" preamble
**Source:** `https://ielts.org/cdn/ielts-guides/ielts-writing-key-assessment-criteria.pdf` p.2 — *"a diagram, graph, table, chart, map or other visual input"*

The chapter quotes the phrase and then asserts its eight-way split "covers every input those
documents describe". Once CRITICAL-1 is fixed the claim is much stronger, but "other visual
input" is an open category by construction and the reader deserves one sentence of guidance
for the unfamiliar case.

**What the chapter must add:** one paragraph — if the visual is unrecognisable, ask two
questions in order: *is there a time axis?* (decides tense and whether trend language is
legal) and *is there a sequence?* (decides process shape vs comparison shape). Those two
questions reduce any novel input to a type already taught.

---

### [MINOR] — descriptor decoders stop at band 6

**Should be in:** Chapters 4, 5, 6, 8
**Source:** the public descriptor PDFs run 0–9

Every decoder table gives bands 8, 7 and 6. Band 5 is never shown. The reader's baseline is
undiagnosed (per `CLAUDE.md`) and a first Task 2 could land at 5.5; he would have no
descriptor language for what he actually produced. Adding the band-5 row costs four lines per
table and makes the self-marking instruction in Chapter 9 workable from wherever he starts.

---

### [MINOR] — the Arabic/French quick-reference exists but is not consolidated

**Should be in:** an appendix
**Where the material lives now:** Chapter 8 §"The 60-second Arabic sweep", §"The 45-second French sweep", §"Your error map, ranked by expected cost", §"The three-minute self-edit"; Chapter 7 §"The false-friend list", §"Uncountables that French pluralises"

The content is present and is the strongest L1 material I have seen in a book of this kind.
But it is spread across two chapters and four sections, and the artefact the reader needs is
one page he can keep beside the keyboard during every timed drill. Nothing new needs writing —
this is a consolidation task: article decision procedure, the keep-the-article counter-list,
the uncountables list, the false friends, the preposition set, and the two timed sweeps, on
one page.

---

### [MINOR] — no single pre-test-day checklist

**Should be in:** an appendix, or Chapter 9's "60-second summary"
**Where the material lives now:** Chapter 9 §"What you may take into the room", §"The shape of the day", §"Things you must ask your centre before you pay", §"Self-test checklist"

Chapter 9's self-test checklist is a *preparation* audit ("have you asked your centre about
AZERTY?"), not a *night-before* checklist. The what-to-bring table and the shape-of-the-day
table together contain everything needed, but the reader would have to assemble it himself at
the worst possible moment. Fifteen tickable lines — documents by the door, alarms, what goes
in the locker, arrival time from the booking confirmation, water bottle, eat first, volume set
during the instructions, two minutes at the end of Listening, never leave a box blank — would
close it.

---

## Over-coverage

I looked specifically for invented types and for types that no longer exist. **I found none.**
Every taxonomy in the book is either official or explicitly labelled as convention:

- **Chapter 2's eleven Listening layouts** exceed the official six. This is not
  over-coverage: the chapter states "Officially there are six named types; four are one family
  of completion layouts sharing one rule set" and then splits them for teaching. The split
  maps exactly onto the sample PDF's own eight separate sample tasks. Correct and honest.
- **Chapter 3's eleven Reading types** are the official numbered eleven, and the chapter
  resolves the 11-vs-14 question explicitly rather than picking silently. Its reasoning is
  sound and its choice is defensible.
- **Chapter 4's eight Task 1 types** are flagged as "a **teaching convention, not an official
  taxonomy**". Map comparison is not on the format page but *is* named in the official Key
  Assessment Criteria PDF, which the chapter cites correctly. No fabrication.
- **Chapter 5's five Task 2 families** are flagged twice — in the preamble and again as Myth
  M12 — as "a recognition heuristic, not an examined category", with the correct observation
  that IELTS publishes no taxonomy and that the two owners' lists disagree. This is exactly
  right.
- **Chapter 7's "six components of Lexical Resource"** and **Chapter 8's "eight band-7
  structures"** are pedagogical constructs, not claimed as official, and both chapters say so.

Two things to keep watching rather than fix:

1. **Paper-mode material.** Chapter 1's 2h40 arithmetic, the 10-minute transfer window and the
   handwriting-legibility rule describe a mode being retired from mid-2026 and one this reader
   will not sit. The brief required both modes covered and every difference flagged, and the
   book does flag them — this is correct as written, not over-coverage. Do not cut it.
2. **General Training.** Correctly absent throughout, except where Chapter 2 notes the
   Listening paper is shared between modules, which is a useful practical fact (any Listening
   material is usable).

---

## Verdict

| Severity | Count | Items |
|---|---|---|
| CRITICAL | 1 | static object/device/event diagram absent from Task 1 |
| MAJOR | 5 | Reading multi-answer MC; Part 2 rounding-off questions; Part 2 card shapes; descriptor summary tables; question-type index |
| MINOR | 6 | Ch 1 Listening type list; Listening PDF 5-vs-6; "other visual input"; band-5 rows; consolidated L1 reference; night-before checklist |
| Over-coverage | 0 | — |

The single CRITICAL is narrow but real, and it is the one an adversarial read is supposed to
find: the chapter quotes the official sentence that establishes the type and then does not
teach it. Three of the five MAJORs are appendix-level deliverables that were specified in the
brief and simply do not exist in the repository — `ielts-book/book/` is empty and no file
anywhere contains the string "appendix".
