# V4 — Consistency & Example Auditor

**Scope.** All nine chapters in `ielts-book/chapters/`, read in full. Every worked
example, mini-example, model paragraph, skeleton and ✗/✓ pair was worked
individually — T/F/NG and Y/N/NG items reasoned from the text as printed, model
answers word-counted with a script, band averages and percentage claims
recomputed, and every article example checked against the book's own
generic/specific rule and its own counter-list.

**Verdict: not clean.** 2 CRITICAL, 11 MAJOR, 21 MINOR. The single most important
finding is that **the changelog fix for the /p/ contradiction is incomplete** —
Chapter 7 still carries the claim Chapter 2 was corrected for (issue 3).

Coverage record, so this reads as an audit rather than a spot-check:

| Task | What was actually done | Result |
|---|---|---|
| A — contradictions | 14 repeated assertions tabulated across chapters (timings, question counts, word limits, raw-score anchors, rounding, the Writing formula, transfer time, criterion names, article doctrine, error-free-sentence target, stop times, test-day logistics) | 6 disagree |
| B — worked examples | 41 examples/skeletons worked: 11 Ch2 listening items, 12 Ch3 reading items, 8 Ch4 visual models, 5 Ch5 skeletons, 5 Ch6 band pairs; all claimed word counts and all band arithmetic recomputed | 4 fail hard, 9 wobble |
| C — ✗/✓ pairs | ~130 pairs across Ch3–Ch8 checked individually; all 47 article examples checked against the *the environment / the government* counter-list | 2 on the wrong side, 1 stress error |
| D — copyright | Full proper-noun extraction per chapter + targeted grep for Mkere, Westall, Packham's, Carlton House, Royal Oak, Majestic, Imperial, Marie Curie, radium, polonium + web searches on the four most distinctive invented passages | **Clean** |
| E — cross-references | All 25 internal references resolved against target content | **All 25 valid** |

---

## CRITICAL

### [CRITICAL] — The Y/N/NG "scope mismatch" example is keyed wrong, and it teaches the reasoning the chapter spends four pages forbidding

**Where:** Chapter 03 §Type 3 mini-example (and the same doctrine at §The qualifier
trap row 3, and §60-second summary)

**Problem.** The text supplied is:

> "Forty per cent of *managerial* staff at the firms surveyed reported working
> entirely from home. The Institute of Transport Studies, which has long campaigned
> against car commuting, published the results. Fewer journeys means less time lost
> to traffic — and, I would argue, a working week measurably longer in useful hours."

The chapter keys:

> "· *40% of employees at these firms worked entirely from home* → **NO. Scope
> mismatch** — right number, wrong population (*managerial staff*)."

Work it. The passage says nothing whatever about the *whole* employee population.
It is entirely possible that 40% of all employees also work from home — the text
neither confirms nor denies it. There is no sentence to point at.

That is exactly the test the chapter itself prints:

> "7  DECIDE — can I put my finger on a sentence that ANSWERS my yes/no question?
>       NO  → NOT GIVEN. Stop. Do not reason further."

and again:

> "**FALSE requires a contradiction you can point at. NOT GIVEN is the absence of a
> sentence.** If you catch yourself constructing an argument — *'well, it probably
> isn't, because…'* — you are inferring, not reading, and the answer is NOT GIVEN."

The keyed answer requires precisely the argument-construction step 7 bans. **The
answer is NOT GIVEN.**

It is wrong a second way. This is a **Y/N/NG** set, and the chapter's own table
defines the object judged as "The writer's opinions and claims" and NO as "writer
**explicitly** claims the opposite". A statistic is not a view, and the writer
nowhere claims the opposite. A statement of this shape would not carry a NO key in
a Y/N/NG set at all.

The same error is generalised into doctrine two sections later —

> "| deaths in general | deaths from one cause | **FALSE / NO** | Scope mismatch —
> right number, wrong population |"

— and stated flatly in the summary: *"A scope mismatch is FALSE."*

**Fix.** Re-key the mini-example to **NOT GIVEN**, and relabel its mechanism
*Population gap* — the statement's population is never quantified in the text — so
it sits alongside "Adjacent proposition" and "Attribution gap" rather than against
them. Delete the "deaths in general / deaths from one cause → FALSE" row, or
replace it with a genuine contradiction (e.g. statement *"the outbreak killed 200"*
against text *"the outbreak killed 200, of whom fewer than half died of cholera"*
→ statement *"cholera killed 200"* = FALSE). Change the summary line to **"A scope
mismatch is NOT GIVEN unless the text explicitly excludes the statement's
population."** Then re-run the whole qualifier table against step 7, because rows
1, 4, 5, 6 and 7 are all correctly keyed NOT GIVEN on exactly the reasoning row 3
abandons.

---

### [CRITICAL] — Chapter 3 prints, as fact, the raw-score table Chapter 1 lists as a myth

**Where:** Chapter 01 §Band descriptor decoder + §Myths ↔ Chapter 03 §Band
descriptor decoder (and Chapter 02 §Band descriptor decoder, a third position)

**Problem.** Chapter 1:

> "**Half-band thresholds (6.5, 7.5) are not published by any official source**, so
> this book will not print them."

and, as a *myth that holds you back*:

> "**'There's a raw-score table that tells me exactly what 6.5 needs.'** Not an
> official one. IELTS publishes four anchor points per test and nothing else… Every
> 'complete' table online reconstructs half-bands from retired practice books. **Do
> instead:** use the published anchors… and never budget your revision on the
> assumption that 26/40 is definitely a 6.5."

Chapter 3 then prints the complete nine-row table with no such caveat —

> "| 37–38 | 8.5 | / | 33–34 | 7.5 | / | **30–32** | **7** | / | **27–29** | **6.5** |"
> `[src: ielts.idp.com — Reading band scores]`

— and makes it the chapter's headline claim, repeated in the summary:

> "### **6.5 → 7.0 is exactly three marks. 27 → 30.**"
> "There are no band descriptors: **6.5 → 7.0 is exactly three marks, 27 → 30.**"

So Chapter 1 tells the reader never to budget revision on "26/40 is definitely a
6.5", and Chapter 3 budgets the entire chapter on "27/40 is a 6.5". The research
file is unambiguous about which is right: `research/R1-test-anatomy-scoring.md`
says "**Do not publish half-band raw scores (6.5 = 26–29 etc.).** No official source
gives them… `[UNVERIFIED]`".

Chapter 2 is a third, different position — it prints half-bands but labels them:

> "| 6.5 | ~26–27 *(interpolated — not official)* |"

which also disagrees numerically with Chapter 3 (26 vs 27 as the 6.5 floor) in two
papers Chapter 1 says are identical from band 6 upward.

**Fix.** Adopt Chapter 2's treatment everywhere. In Chapter 3, mark the 6.5, 7.5,
8.5 and 9 rows *(interpolated — not official)*, keep 35 / 30 / 23 / 15 unmarked as
the published anchors, and rewrite the headline as **"6.5 → 7.0 is about three
marks — treat 30 as the target and everything above it as insurance"**, which
survives the caveat. Align the 6.5 figure across Chapters 2 and 3 (pick one). Add a
one-line pointer in Chapter 3 back to Chapter 1's myth so the reader is not left
with two doctrines.

---

## MAJOR

### [MAJOR] — The /p/ fix is incomplete: Chapter 7 still carries the corrected claim

**Where:** Chapter 07 §L1 alert → Arabic-specific issues ↔ Chapter 06 §L1 alert;
Chapter 02 §L1 alert item 7; `fixes/changelog.md`

**Problem.** The changelog records the fix as done and asks V4 to "confirm the
reconciliation is sound and complete". Chapters 2 and 6 now agree:

- Ch6: "Tunisian Arabic has /p/ and /v/ only in loanwords, usually replaced. **But
  French supplies [p] — the phoneme is not missing.**"
- Ch6: "**2 — /p/ is almost certainly not a missing phoneme.** You speak French;
  French has [p]. The likely problem is **aspiration**…"
- Ch2 (rewritten): "you are a fluent French speaker, and **French supplies /p/, so
  the phoneme is not missing from your inventory**. What English adds is
  *aspiration*…"

Chapter 7 was never touched and still states the opposite, flatly and without the
French qualifier:

> "**Consonant and vowel transfer into spelling.** **Arabic has no /p/ and no /v/**,
> and its writing system does not represent short vowels the way English does. The
> predictable results are consonant substitutions (*broblem*, *sufer*)…"

**Assessment of the fix.** The Ch2 rewrite itself is sound — it matches Ch6, keeps
the dictation drill, and re-justifies it honestly on perception-vs-production. But
the fix is **not complete**: the same claim survives in a third chapter, and in
Chapter 7 it is load-bearing (it is the stated cause of a named spelling-error
class and of a thirty-word rote list).

**Fix.** Rewrite the Chapter 7 sentence to match Chapter 6: *"Tunisian Arabic has
/p/ and /v/ only in loanwords — but French supplies both, so these are not missing
phonemes for you. What survives into spelling is the b/p and f/v grapheme
confusion under time pressure (*broblem*, *sufer*), not an inability to hear the
sounds; see Chapter 6."* Then grep the whole book for `no /p/`, `no /v/`, `does not
use a /p/` before closing the changelog entry.

---

### [MAJOR] — Chapter 5 puts *government* on the drop-the-article side; Chapter 8 puts it on the keep side, and Chapter 5 itself uses it with the article

**Where:** Chapter 05 §L1 alert item 1 ↔ Chapter 08 §L1 alert → "The counter-list"
(and Chapter 05 §L1 alert item 6)

**Problem.** Chapter 5:

> "Same family: *society, nature, life, technology, education, history, crime,
> poverty, health, pollution, science, **government** (as an institution), work,
> research, progress*."

Chapter 8, in the table whose whole purpose is to stop this over-correction:

> "| Take **the** in generic use | the environment · **the government** · the media ·
> the economy · the internet · the public · the police · … |"

and demonstrates it as a wrong→right pair:

> "| *Government should regulate emissions more strictly.* | ***The** government
> should regulate emissions more strictly.* |"

Chapter 5 contradicts itself four sections later, modelling it *with* the article:

> "*the government are decide* → the government **decides**"

The parenthetical "(as an institution)" makes it worse, not better: *as an
institution* is exactly the sense that takes **the**. The article-less use is the
abstract-concept sense (*"Government is expensive"*), which is not what a Task 2
writer produces.

**Fix.** Delete *government* from the Chapter 5 list. Add a one-line pointer:
*"and see the counter-list in Chapter 8 — the government, the media, the economy,
the environment, the internet keep their article."* Chapter 7's equivalent list
(*nature, life, technology, education, history, science, poverty, crime, pollution,
unemployment, globalisation*) is clean and needs no change.

---

### [MAJOR] — Chapter 4 marks a defining relative clause as an article error

**Where:** Chapter 04 §L1 alert item 1 ↔ Chapter 08 §L1 alert → "The rule that stops
the overcorrection"

**Problem.** Chapter 4:

> "✗ *the people who travelled by bus* (people in general) → **people**"

Chapter 8's rule:

> "The error is not *the*. The error is *the* with a **generic**. The moment a noun
> is made specific — by an *of*-phrase, **a defining relative clause**, a
> superlative, an ordinal, a date, or previous mention — English wants *the* back."

A defining relative clause is the second trigger on Chapter 8's own list. *The
people who travelled by bus* is correct English in a Task 1 report — the relative
clause identifies which people, exactly as *the measures that were introduced*
does in Chapter 8's ✓ column. Marking it ✗ trains the reader to strip an article
from a slot where the book's other chapter says to restore it.

The bracketed gloss "(people in general)" does not rescue it, because the past-tense
relative clause pins the noun to the chart's population, which is not "in general".

**Fix.** Replace the pair with a genuine generic: *✗ the people prefer cars → ✓
people prefer cars*, or *✗ the bus passengers fell → ✓ bus passenger numbers fell*.
Keep *the car use*, *the tourism*, *the electricity consumption*, which are all
correct ✗ examples.

---

### [MAJOR] — Chapter 3 gives matching headings two incompatible order verdicts

**Where:** Chapter 03 §The order table + §Type 5 ↔ §Tips & tricks 4 + §60-second
summary

**Problem.** The order table and the Type 5 section:

> "| 5 | Matching headings | **Questions yes; the heading numerals no** |"
> "**Order: questions run in paragraph order; the numerals do not**"

The tip and the summary put type 5 with the unordered types:

> "**4. Learn the order table.** … It **fails** on types 4, **5**, 6, 9 and 10 —
> applying it there makes you abandon correct answers."
> "Not ordered — matching information, matching features, **matching headings**,
> summary/note/table/flow-chart completion, diagram labelling."

These give opposite instructions. Under the table the reader works paragraphs in
order and resumes from the last answer; under the tip and summary he abandons that
and searches the whole passage. Self-test question 1 ("Can I say, for each of the 11
task types, whether its answers follow passage order?") has no single right answer
as the chapter stands.

**Fix.** The table's reading is the careful one and the chapter defends it at
length. Change tip 4 to "*fails on types 4, 6, 9 and 10; on type 5 the questions
are ordered but the numerals are not*", and change the summary to move matching
headings into the ordered list with the same eight-word qualifier.

---

### [MAJOR] — Chapter 4's line-graph model overview is 34 words, not the 45 claimed

**Where:** Chapter 04 §1. Line graph → Worked example

**Problem.**

> "*Overall, the two long-established attractions moved in opposite directions over
> the two decades, with the gallery overtaking the castle around the midpoint of the
> period. The aquarium, by contrast, saw almost no net change.*
>
> A category, a named trend, the crossover flagged, the flat series separated, no
> figures. **Forty-five words.**"

Counted: **34 words** (35 if *long-established* is split). The claim is out by about
a third. In a chapter that says "Count my words and tell me the number every time"
and sets a 55–70-word checkpoint at the end of the overview, a demonstration model
carrying a wrong count is the wrong thing to be wrong about — a reader who trusts
"forty-five" and writes two sentences of that shape will hit the counter checkpoint
ten words light and think his introduction is too long.

**Fix.** Change to "Thirty-four words." Then re-check the 55–70-word checkpoint in
tip 12: a one-sentence introduction of ~22 words plus a 34-word overview is 56,
which just clears it — the checkpoint survives, but only because the number was
recomputed.

---

### [MAJOR] — Chapter 4's table model states a figure the table contradicts

**Where:** Chapter 04 §4. Table → Worked example

**Problem.** The data:

| | Canada | Ireland | Portugal |
|---|---|---|---|
| Nursing | 96 | 97 | 89 |
| Fine art | 51 | 47 | 39 |

The model overview:

> "*…with a gap of roughly forty-five points between them **in every country**.*"

Worked: Canada 96−51 = **45**; Ireland 97−47 = **50**; Portugal 89−39 = **50**. Two
of the three countries are 50, not "roughly forty-five", and the model asserts the
figure holds *in every country*.

This is the exact error the chapter charges elsewhere: "*Plummeted* for a 3% fall is
a TA accuracy error as well as an LR imprecision", and "Is every figure
**correct**?" is self-test item 10. The chapter's own band-7 exemplar would lose a
TA accuracy mark.

**Fix.** "*…with a gap of between forty-five and fifty points between them in every
country*", or "*…with a gap of roughly fifty points in every country*". Both are
accurate and both still demonstrate the categorisation the example exists to show.

---

### [MAJOR] — Chapter 6 marks the wrong stressed syllable in *possibility*, one line after stating the rule it breaks

**Where:** Chapter 06 §L1 alert → Drill 3, Word stress

**Problem.**

> "*-ion, -ic, -ical, -ity* pull stress onto the syllable immediately before:
> `eduCAtion, ecoNOMic, poLItical, **posSIbility**, phoTOgraphy`."

*possibility* is /ˌpɒsəˈbɪləti/ — **possi·BIL·i·ty**. The stressed syllable is
*bil*, which is precisely "the syllable immediately before *-ity*". The book's
marking, *posSIbility*, puts the stress on the second syllable, two syllables early
— so the example contradicts the rule it is printed to illustrate.

The other four are correct (eduCAtion, ecoNOMic, poLItical, phoTOgraphy), which
makes this a single slip rather than a broken rule, but the reader is told to "**hum
the word before you say it** — just the rhythm, *da-DA-da-da*. Wrong hum, wrong
word", i.e. to drill the marking as given.

**Fix.** `possiBIlity`. Note also that *phoTOgraphy* does not end in any of the four
suffixes listed; either add *-graphy/-ology/-ography* to the rule statement or move
that item to the noun/verb-shift line below, where *PHOtograph → phoTOgraphy →
photoGRAPHic* already sits correctly.

---

### [MAJOR] — Chapter 2 names three criteria as four and attributes a Speaking-only criterion to Writing

**Where:** Chapter 02 §Band descriptor decoder ↔ Chapter 01 §Writing and Speaking:
four criteria; Chapter 06 §What the test actually asks

**Problem.** Chapter 2:

> "The four-criterion apparatus — **Fluency and Coherence, Lexical Resource,
> Grammatical Range and Accuracy** — applies only to Writing and Speaking."

Three criteria are named, not four, and *Fluency and Coherence* is Speaking-only.
Chapter 1 has it right:

> "Writing Task 1: Task Achievement, Coherence and Cohesion, Lexical Resource,
> Grammatical Range and Accuracy. Task 2 substitutes Task Response for Task
> Achievement. Speaking: Fluency and Coherence, Lexical Resource, Grammatical Range
> and Accuracy, Pronunciation."

Chapter 6 also has it right. Self-test item 9 of Chapter 1 asks the reader to name
the four Writing Task 2 criteria from memory; a reader who learned them from
Chapter 2 answers wrongly.

**Fix.** "The four-criterion apparatus applies only to Writing and Speaking —
Task Response/Achievement, Coherence and Cohesion, Lexical Resource and Grammatical
Range and Accuracy in Writing; Fluency and Coherence, Lexical Resource, Grammatical
Range and Accuracy and Pronunciation in Speaking."

---

### [MAJOR] — 2h40 is the paper sitting in Chapter 1 and the computer sitting in Chapters 6 and 9

**Where:** Chapter 01 §What the test actually asks ↔ Chapter 09 §The shape of the
day; Chapter 06 §When is it?

**Problem.** Chapter 1 reconciles the two published headline figures by assigning
2h40 to paper:

> "Different quantities, not a contradiction: **2h40m is the paper-mode sitting**
> (Listening 30 + transfer 10 + Reading 60 + Writing 60); 2h45m counts all four
> papers including a ~15-minute Speaking test and excludes the paper-only transfer
> window."

Chapter 9 applies 2h40 to the computer day, sourced to official pages:

> "Listening, Reading and Writing run as one block of **2 hours 40 minutes with no
> breaks at all**… On computer the order is Listening → Reading → Writing"

and builds the whole practice regime on it — "Sit at least two full 2h40 mocks,
typed", "Have you sat two full 2h40 sittings?", weeks 5/7 of the study plans.
Chapter 6 does the same: "you may speak after **2h40** of Listening, Reading and
Writing".

By Chapter 1's own arithmetic the computer sitting is 30 + 2 + 60 + 60 ≈ **2h32**,
because the ten-minute transfer window it uses to build 2h40 does not exist on
computer — the single fact Chapter 1 calls "the big one".

**Fix.** Chapter 1's reconciliation needs one more clause, because the 2h40 figure
is published on computer-test-day pages too: *"2h40 is the advertised sitting length
for the three written papers, and it is quoted for both modes; on paper it is
Listening 30 + transfer 10 + Reading 60 + Writing 60, on computer the transfer
window is replaced by instructions, seating and the 2-minute check."* Then keep
2h40 in Chapters 6 and 9 as the planning figure, which is what the reader needs.

---

### [MAJOR] — Chapter 3 quotes 16/40 as the Reading band-5 anchor; Chapter 1 (and Chapter 3's own table) says 15

**Where:** Chapter 03 §Band descriptor decoder ↔ Chapter 01 §Listening and Academic
Reading: raw marks to band

**Problem.** Chapter 3:

> "Cross-checked against the coarser official table — 8 → 35, 7 → 30, 6 → 23,
> **5 → 16** out of 40 — which is consistent with it."

Chapter 1 prints the anchors per paper and calls out the difference explicitly:

> "| 5 | 16 | 15 |" (Listening | Academic Reading)
> "The one asymmetry is at band 5 — **Reading 15, Listening 16**; from band 6 upward
> they are identical."

`research/R1-test-anatomy-scoring.md` confirms 15 for Academic Reading. Chapter 3 is
also inconsistent with itself: its own table two lines above gives "| 15–18 | 5 |".
So the "cross-check" that is offered as evidence the table is sound uses the wrong
paper's figure.

**Fix.** "5 → **15** out of 40" in Chapter 3, and add the half-sentence about the
band-5 asymmetry so the reader is not surprised by Chapter 1.

---

### [MAJOR] — The T/F/NG mini-example tests the page, not the passage

**Where:** Chapter 03 §Type 2 mini-example

**Problem.**

> "*Passage, entire:* 'The meeting room is on the fourth floor.'
> · 'The meeting room is on the second floor.' → **FALSE**, direct contradiction.
> · **'The word *floor* appears in the sentence.' → TRUE.**
> · 'The building has a lift.' → **NOT GIVEN.**"

Items 1 and 3 are correct and well chosen. Item 2 is not an IELTS relation at all:
it is a claim about the passage's typography, verified by looking at the letters
rather than by comparing information. No official item of any type asks this, and
the chapter's own definition — *"Do the following statements agree with the
information given in the passage?"* — has no purchase on it.

The example is labelled "(deliberately trivial, to isolate the logic)", but the
logic it isolates is *surface match → TRUE*, which is the single habit the rest of
the chapter exists to break ("word-matching is the mechanism by which distractors
are built, in every type", Myth 8).

**Fix.** Replace with a paraphrase item, which isolates the same logic without
modelling word-matching: *"The meeting room is three storeys above street level."*
→ **TRUE** (fourth floor = third above ground in UK usage — or pick a cleaner
paraphrase, e.g. passage *"The meeting room is on the top floor of a four-storey
building"* / statement *"The meeting room is on the fourth floor"* → **TRUE**).

---

## MINOR

### [MINOR] — Every Chapter 5 skeleton totals more than the word target the same chapter sets

**Where:** Chapter 05 §Families 1–5 skeletons ↔ §Length + §Tips 10 + §Self-test 8

**Problem.** The target: "**Your target: 270–290 words, hard floor 260**" and
"**10. Target 270–290 words; hard floor 260.**" The five skeletons sum to:

| Family | Intro | B1 | B2 | Conc | Total |
|---|---:|---:|---:|---:|---:|
| 1 Opinion | 45 | 110 | 110 | 35 | **300** |
| 2 Discussion | 50 | 100 | 120 | 35 | **305** |
| 3 Problem–cause–solution | 45 | 105 | 110 | 35 | **295** |
| 4 Advantages–disadvantages | 50 | 95 | 120 | 35 | **300** |
| 5 Two-part | 45 | 105 | 110 | 35 | **295** |

All five exceed 290; Family 2 exceeds even the self-test ceiling ("Is my word count
between **260 and 300**?"). Three different numbers are in play: 270–290, 260 floor,
260–300.

**Fix.** Trim each skeleton by 10–15 words (bodies to 100/105) so they land at
275–285, and make self-test item 8 read "between 270 and 290, hard floor 260" to
match tip 10.

### [MINOR] — Task 1 stop time is 17 minutes in Chapter 4 and 18 in Chapter 8

**Where:** Chapter 04 §The 20-minute budget ("| 0:17–0:20 | Check word count,
figures, tense, agreement, articles. |") ↔ Chapter 08 §Tips 6 ("Stop writing at 37
minutes on Task 2, **18 minutes** on Task 1"). Task 2 agrees at 37 across both
chapters (Ch5 tip 13's 5/32/3 also gives 37). **Fix:** pick 17 or 18 and change the
other.

### [MINOR] — Chapters 4/5 tell the reader to aim for ≥ half error-free sentences; Chapter 8 says band 7 is below half

**Where:** Chapter 04 §Tips 5 ("The working target for 7 is roughly half") and
§Self-test 15 ("is **at least half** completely error-free"); Chapter 05 §GRA ("of
about sixteen sentences, if fewer than seven or eight are completely clean, you are
arguing for a 6") ↔ Chapter 08 §How accurate is "accurate enough"? ("Band 8 asks for
the **majority** of sentences to be error-free, so band 7 must be regularly
occurring but **short of a majority**"). One says aim at 50%+, the other says 50%+
*is* band 8 territory. **Fix:** state it once — "*frequent* is not quantified;
target half as a working proxy, and treat consistently above half as band-8
evidence" — and cross-reference rather than re-deriving in three chapters.

### [MINOR] — "Front-loaded" describes a back-loaded split

**Where:** Chapter 03 §Timing. "A **front-loaded** split — roughly 16 / 19 / 21 — is
a legitimate personal tactic… if across three timed tests your Passage 1 accuracy is
at or above 90% and Passage 3 is below 70%, **shift time to the end**." 16/19/21
gives Passage 3 the most time; it is back-loaded. The rationale sentence says so
outright. (16+19+21 = 56, plus the 3-minute sweep = 59, so a minute is also
unaccounted for against the 19/19/19+3 = 60 baseline.) It also sits awkwardly beside
Myth 13, which warns that budgeting extra for Passage 3 "persuades people to
under-budget Passage 1, where marks are cheapest". **Fix:** "A back-loaded split —
roughly 17 / 19 / 21…", and add a clause acknowledging Myth 13.

### [MINOR] — The study-plan hour totals assume six study days; the rotation has seven

**Where:** Chapter 09 §The weekly rotation ↔ §6-week / 8-week / 10-week plan
headings. 54 / 72 / 90 hours = weeks × **6** × 1.5h. The rotation table runs Mon–Sun
with Sunday as a working review day (`/review`, `/vocab`), and the plans themselves
allocate work to days 1–7 ("Days 5–7: build the error map", "Day 7: rest" only in
the taper week). Seven days gives 63 / 84 / 105 hours. **Fix:** either mark Sunday
as a half-session and restate the totals, or change the headings to ≈63 / ≈84 / ≈105.

### [MINOR] — Writing does not start at the two-and-a-half-hour mark

**Where:** Chapter 09 §Tips 9. "No food inside, no breaks for 2h40, and **Writing —
the section worth most and marked hardest — is sat at the two-and-a-half-hour
mark.**" Listening (~32 min including the 2-minute check) plus Reading (60) puts the
start of Writing at about **1h32**; you are at 2h30 as you finish it. **Fix:**
"…is sat in the last hour of a 2h40 block, when you are at your most tired." The
argument for eating breakfast is unaffected.

### [MINOR] — "Five markers, four sentences" describes five sentences

**Where:** Chapter 05 §Coherence and Cohesion. "**Band 6 (five markers, four
sentences):** Firstly… Moreover… Furthermore… In addition… Therefore, governments
should act." That is five sentences and five markers. (Chapter 4's parallel example
is correct: four connectors, four sentences, "Four bolted-on connectors have become
zero.") **Fix:** "(five markers, five sentences)".

### [MINOR] — Two error miscounts in Chapter 7's before/after pairs

**Where:** Chapter 07 §6. Spelling and word formation, and §Writing — Lexical
Resource.

1. "*The goverment should give more importance to the developement of a sustainible
   economical growth, which is a significative challenge.*" → "**Four spelling
   errors, one wrong suffix, one non-word — six LR hits.**" There are **three**
   misspellings (*goverment, developement, sustainible*), plus *economical* (suffix)
   and *significative* (non-word) = five named items, not six.
2. "*Nowadays the pollution is a very big problem which gives many bad effects to the
   society and the healthy of the peoples.*" → "Four errors disappear with them: **an
   article on an abstract noun**, *gives effects to*, a pluralised *peoples*, and
   *the healthy* for *health*." There are **two** generic articles (*the pollution*
   **and** *the society*) — and since the article error is the reader's named
   highest-frequency error, undercounting it in the demonstration is the wrong place
   to be imprecise.

**Fix:** "Three spelling errors, one wrong suffix, one non-word — five LR hits"; and
"**two** articles on abstract nouns… — five errors disappear".

### [MINOR] — Chapter 4's LR example omits the book's flagship error from its own error list

**Where:** Chapter 04 §Lexical Resource. "*The number of car users augmented
significatively, whereas the number of people who use the walk decreased strongly.
In the other hand, **the cycling** had a important diminution.*" → "**Seven problems
in thirty words:** *augmented*, *significatively*, *use the walk* and *decreased
strongly*, *in the other hand*, *a important*, *diminution*." The generic article in
*the cycling* — the single error the book calls "your highest-value error" — is
present in the example and absent from the list. (The text is also 28 words, not
thirty, and *who use the walk* carries a tense clash with *decreased* that is not
named.) **Fix:** name *the cycling* as an eighth problem, tagged GRA, and change
"thirty" to "twenty-eight".

### [MINOR] — Chapter 4 scores an article error under LR; Chapters 7 and 8 assign it to GRA

**Where:** Chapter 04 §Lexical Resource (*a important* listed as an LR problem) ↔
Chapter 07 §L1 alert ("Note that this particular error lands on **GRA**, not LR") and
Chapter 08 §Your error map (row 1 articles → GRA; row 7 false friends and
word-formation → LR). Determiner choice is grammar; Chapters 7 and 8 are right.
**Fix:** move *a important* out of the LR count in Chapter 4 with a one-clause note
that it costs GRA, keeping the six genuine LR items.

### [MINOR] — The Listening summary-completion example requires the conversion the surrounding rule forbids

**Where:** Chapter 02 §5. Summary completion. The gap "*The team's main difficulty
was the ……… of suitable sites*" against audio "suitable sites were incredibly hard
to **identify**" is keyed `identification` — a derivation the speaker never utters.
The paragraph then says: "*'Don't try to rephrase what you hear'*… When grammar and
that instruction pull apart, **the usual explanation is that the exact word *was*
spoken and you missed it.** Convert form only when you are certain." In the
constructed audio the noun definitively was not spoken, so the example is the
counter-case to its own rule and leaves the reader without a decision procedure.
**Fix:** either put the noun in the audio and make the trap a *different* noun
nearby, or keep the derivation and add one line: "*This is the rare case where the
conversion is forced — the noun is genuinely absent. If you can hear the noun
anywhere, write it instead.*"

### [MINOR] — The short-answer example bolds answers that would breach the limit the same section teaches

**Where:** Chapter 02 §11. Short-answer questions. The bolded strings are "**in the
main reception**" (4 words) and "**on the noticeboard by the canteen**" (6 words),
and the Band-6 mistake immediately below is: "'You can find it in the main
reception' is six words — **zero under a THREE WORDS limit**." No reduced answer is
shown, so a reader copying the bold gets zero on both. **Fix:** print the keyed
answers explicitly — `main reception` · `(the) noticeboard` — as the form example
and the table example both do.

### [MINOR] — "Same words. Same accent. Different band." — the two lines do not use the same words

**Where:** Chapter 06 §Pronunciation.

> Band 6: `I · THINK · THAT · THE · GOV · ERN · MENT · SHOULD · IN · VEST · MORE`
> Band 7: `I think the GOVernment should inVEST a lot MORE in it`
> "**Same words. Same accent. Different band.**"

The band-7 line drops *that* and adds *a lot* and *in it*. The point — that prosody
alone moves the band — is right and worth making, and it is weakened by an
overclaim the reader can see through. **Fix:** make the two lines lexically
identical (`I think that the GOVernment should inVEST MORE`) so the claim is
literally true.

### [MINOR] — Chapter 8's Speaking GRA table omits from band 8 what its own prose says appears there

**Where:** Chapter 08 §Speaking GRA — the current (2025) file. The table shows "**a
few basic errors persist**" only in the band-7 row; the prose two lines later says
"**'A few basic errors persist' appears at band 7 and band 8 alike.**" Chapter 6's
table has it in both rows ("| **8** | … **A few basic errors may persist.** |"), so
Chapter 6 and Chapter 8's prose agree and Chapter 8's table is the outlier. **Fix:**
add the clause to the band-8 accuracy cell in Chapter 8's table.

### [MINOR] — A first conditional is filed as a second-conditional error

**Where:** Chapter 08 §6. The second conditional → "The recurring wrong forms":

> "- ✗ *If the subsidy **will end** next year, ticket prices will rise.*
>   ✓ *If the subsidy **ends** next year, ticket prices will rise.*"

Both versions are first conditionals (real future condition). The pair is a genuine
and useful error, but it does not belong under a heading whose stated form is "*If*
+ past simple, *would* + base". **Fix:** move it to a one-line note — "*the same
no-modal-in-the-if-clause rule governs the first conditional: ✗ if the subsidy will
end…*" — so the second-conditional section keeps one pattern.

### [MINOR] — The map worked example asserts a tense the chapter's own table does not give it

**Where:** Chapter 04 §7. Map comparison. The tense table:

> "| Maps | past → past | past simple passive: *a car park **was built*** |
>  | Maps | past → 'today' | present perfect passive: *the woodland **has been
>  cleared*** |"

The example is *"Ashcombe village, **1985 and 2025**"* — two dates, i.e. past →
past — yet the model is justified as "Dated 1985 → 2025 **with 'today' implied**, so
**present perfect passive** throughout." Nothing in the prompt implies "today"; both
snapshots are dated, and the book is written in 2026. This is the type the chapter
says "tense goes wrong most", so the example should be the cleanest in the chapter.
**Fix:** either relabel the second map "*today*" (then present perfect is right and
demonstrates the harder row), or keep 2025 and switch the model to past simple
passive. Do not leave the reader to infer when a date counts as "today".

### [MINOR] — The process overview calls a loop linear

**Where:** Chapter 04 §5. Process diagram — man-made. "*The sequence is **linear**,
ending with bottles that **re-enter the same collection system**.*" A sequence whose
output re-enters its own input is the definition of the cycle §6 goes on to treat,
and §6's trap is "Treating a cycle as a line". **Fix:** "*The sequence is linear,
though the bottles it produces will eventually return to the collection stage that
begins it*" — which keeps the (correct) point that this is a linear process, without
using *ending with* and *re-enter* in the same clause.

### [MINOR] — The band-7 GRA model leans on an ambiguous substitution and is claimed error-free

**Where:** Chapter 04 §Grammatical Range & Accuracy. "*The number of children
travelling by car rose over the period, while **those** walking to school fell
substantially.*" → "Two sentences; a participial modifier, **substitution (*those*)**
… **Both error-free.**" *Those* has to substitute for *the number*, which is
singular — and children do not "fall", numbers do. The intended reading needs *the
numbers*, which the first clause does not supply. **Fix:** "*…while the number
walking to school fell substantially*", which keeps the substitution (ellipsis of
*of children*) and removes the mismatch. The rest of the analysis stands.

### [MINOR] — The word-bank example's key is not what the text establishes

**Where:** Chapter 03 §Type 9 mini-example, variation 2. Bank: A gradual · B costly ·
C deliberate · D accidental · E rapid · F local. Text: "*No guild ever sanctioned the
transfer; it moved by way of sailors changing ships and apprentices absconding.*"
Key: **D, accidental**. What the text establishes is *unsanctioned / informal* —
absconding apprentices carry knowledge quite deliberately; it is the guilds'
intention that is absent, not anyone's. C (*deliberate*) is what the text negates,
which makes D the intended answer by elimination, but the semantic step from
"unsanctioned" to "accidental" is one the item does not license. (Also, "the spread
… was largely costly" does not fit the slot, so the claim that "all options fit
grammatically" is loose.) **Fix:** change D to *unofficial* or *informal*, or change
the text to "*it spread through chance contact between crews rather than by any
deliberate transfer*", which makes *accidental* exact.

### [MINOR] — The diagram example justifies itself with text it does not print

**Where:** Chapter 03 §Type 10 mini-example. Text: "*A brass collar sits immediately
below the spindle; the outer casing, made of lacquered oak, encloses both.*" Key:
"**brass collar**, chosen by *immediately below*, not by *brass*, **which also
describes two other parts**." No other brass part appears in the quoted text, so the
reader cannot verify the reasoning the example exists to teach. **Fix:** add the
decoys to the text — "*a brass bezel rings the dial and a brass pin secures the
arm*" — so *brass* genuinely fails to discriminate and *immediately below* genuinely
does the work.

### [MINOR] — A non-sequitur in Chapter 7's opening arithmetic

**Where:** Chapter 07 §What the test actually asks. "**Because Task 2 counts double**,
LR is worth a quarter of your Speaking band and a quarter of your Writing band." LR
is a quarter of each Writing task independently, so it is a quarter of the Writing
band **regardless** of the 1:2 weighting — the weighting is irrelevant to the
conclusion. **Fix:** "LR is one of four equally weighted criteria in every Writing
task and in Speaking, so it is a quarter of your Writing band and a quarter of your
Speaking band — and because Task 2 counts double, two thirds of the Writing quarter
is decided in Task 2."

### [MINOR] — "well over twice as much" overstates a 2.06× ratio

**Where:** Chapter 04 §2. Bar chart worked example. Data: A 210, B 185, C 90, D 75,
E 40. Model: "*two use **well over twice** as much water per head as the remaining
three*." Against the highest of the remaining three, B/C = 185/90 = **2.06×** —
"just over twice". The chapter's own tip 9 is "**Match the intensity of the word to
the size of the change**… a TA accuracy error as well as an LR imprecision".
**Fix:** "*two use more than twice as much water per head as any of the remaining
three*", which is exactly true and still carries the grouping.

### [MINOR] — `ONE WORD ONLY` is unverified in Chapter 2 and quoted as rubric in Chapter 3

**Where:** Chapter 02 §Answer-rule reference ("Research for this book could **not
verify it verbatim in any official IELTS Listening document**… Treat it as plausible
but unconfirmed") ↔ Chapter 03 §Type 8 Appearance (*"Complete the sentences below.
Choose **ONE WORD ONLY** from the passage for each answer."* presented in quotation
marks as the standard rubric) and §Type 8 mini-example ("*Rubric:* ONE WORD ONLY").
Not strictly a contradiction — Chapter 2's claim is Listening-specific and Reading
does use the wording — but a reader who has just been told the phrase is unconfirmed
meets it two chapters later as a quoted rubric with no note. **Fix:** one clause in
Chapter 3: "*(this rubric is attested in Reading; Chapter 2 explains why it could not
be confirmed for Listening)*".

---

## Clean results

### Task D — copyright: no violation found

- **Targeted grep across all nine chapters** for `Mkere`, `Westall`, `Packham`,
  `Carlton`, `Royal Oak`, `Majestic`, `Imperial`, `Marie Curie`, `Curie`, `radium`,
  `polonium`: **zero hits**. The Marie Curie / radium / polonium set flagged in R3
  and the named Listening tapescript proper nouns are entirely absent.
- **Full capitalised-token extraction per chapter** to catch anything the targeted
  list would miss. The only distinctive invented proper nouns are: *Nadia, Youssef,
  Riverside, Miller's, Long Shadow* (Ch2); *Genoese, Restrepo, Halvorsen, Portsea,
  Institute of Transport Studies* (Ch3); *Ashcombe* (Ch4). Everything else is a
  place name from the reader's own context (Tunis, Bizerte, Sousse, Sfax, Gabes,
  Malta) or a country/organisation named in official sourcing.
- **Web searches on the four most distinctive invented passages** — the Genoese
  rope-making guild paragraph, the *Long Shadow* New Zealand documentary listening
  item, the Ashcombe 1985/2025 map, and the Restrepo/Halvorsen sediment matching-
  features item — returned **no published test containing any of them**.
- **Attributed answer-key fragments used as load-bearing evidence**, noted and not
  flagged, per brief: `summer school(s)`, `metre(s)/meter(s)`, `library/libraries`,
  `town hall` (Chapter 2 §Answer-rule reference, Myths 4 and 13). Each is a short
  key fragment cited to support a marking rule, which is the acceptable use.
- Chapter 3's standing header — *"Every example in this chapter is invented for this
  book"* — is accurate on inspection. Chapter 2's equivalent — *"**All examples are
  original**, written to reproduce the trap structure of official material, not the
  material itself"* — is also accurate.

### Task E — internal references: all 25 resolve

Every cross-reference points at content that exists and says what the reference
claims. Checked individually:

| Reference | Target | Verdict |
|---|---|---|
| Ch1 → "Chapter 2 takes the marking rules in detail" | Ch2 §Answer-rule reference | ✓ |
| Ch1 → "Chapter 3 takes them one at a time" | Ch3 §Types 1–11 | ✓ |
| Ch1 → "see *Myths*" (transfer window) | Ch1 §Myths, first entry | ✓ |
| Ch1 → "(see *L1 alert*)" (Writing weakest) | Ch1 §L1 alert | ✓ |
| Ch1 → "(see the next section)" (6.75 → 7.0) | Ch1 §Band math | ✓ |
| Ch1 → "which Chapter 6 treats as a trainable quarter" | Ch6 §Pronunciation | ✓ |
| Ch2 → "learn the pair together (Tip 4)" | Ch2 §Tips 4, correction traps | ✓ |
| Ch2 → mark-budget table: Answer-rule reference / Tip 1 / Myth 1 / Tip 2 / Myth 10 / Tip 4 / Tip 3 / L1 alert (8 refs) | all present and on-topic | ✓ ×8 |
| Ch2 → "With Myth 13" (plurals) | Ch2 §Myths 13 | ✓ |
| Ch2 → "(see Chapter 6)" (aspiration) | Ch6 §L1 alert correction 2 | ✓ |
| Ch3 → "see below" ×2 (order table rows 4, 5) | Ch3 §Two honest caveats | ✓ |
| Ch4 → "(§6)" ×2 (natural-cycle voice) | Ch4 §6 Process — natural | ✓ |
| Ch5 → "Chapter 1 covers this" (Writing formula) | Ch1 §Combining Task 1 and Task 2 | ✓ |
| Ch6 → "see the end of *L1 alert*" (recording) | Ch6 §The one thing this book cannot do | ✓ |
| Ch6 → "See *L1 alert*" (initial clusters) | Ch6 §Correction 1 | ✓ |
| Ch6 → "See below" (/p/) | Ch6 §Correction 2 | ✓ |
| Ch6 → "drill 7" (final clusters) | Ch6 §Drill 7 | ✓ |
| Ch7 → "see Chapter 4" (trend adverbs) | Ch4 §Trend toolkit — *markedly, dramatically, marginally* all present | ✓ |
| Ch7 → "Chapter 4 supplies the trend verbs, approximation and proportion toolkits" | Ch4 §Trend toolkit, §Tips 8, §Six word families | ✓ |
| Ch7 → "See *L1 alert*" (spelling set) | Ch7 §Your standing spelling list | ✓ |
| Ch8 → "see the L1 alert" (article decision) | Ch8 §L1 alert | ✓ |
| Ch8 → "see below" (economic/economical) | Ch8, two lines below | ✓ |
| Ch8 → "which is myth 1 with a number attached" | Ch8 §Myths 1 | ✓ |
| Ch9 → "see *L1 alert*" (AZERTY) | Ch9 §L1 alert | ✓ |
| Ch9 → "rebuild `knowledge/revision-playbook.md` ch.9" | playbook §Chapter 9 — The 30-day plan | ✓ exists |

### Arithmetic that checks out

Recomputed and correct, so the reader can trust these:

- **Overall-band worked examples** (Ch1): A 25.0/6.25→6.5 ✓; B 15.5/3.875→4.0 ✓;
  C 24.5/6.125→6.0 ✓.
- **Routes A–E and the near-miss** (Ch1): all six totals and reported bands correct;
  6.625 → 6.5 ✓.
- **Writing formula table** (Ch1): 6.5 ✓, 6.0 ✓, 6.33 ✓.
- **Task 2 ≈ 17% of the whole result** (Ch1): ⅔ × ¼ = 16.7% ✓.
- **"Half a band on Task 2 is worth a full band on Task 1"** (Ch5): 2×0.5/3 = 1/3 =
  1×1/3 ✓ — a genuinely elegant and correct claim.
- **Listening mark budget** (Ch2): losses column 17/13/10/8/5 all = 40 − raw ✓;
  band 6→7 gap of seven marks ✓.
- **Pie-chart model** (Ch4): packaging overtakes food ✓; 57% then 56% for the top two
  ✓; paper's −40% relative decline genuinely exceeds food's −31% ✓ — the "sharpest
  *proportional* decline" claim is exactly right and is the best example in Ch4.
- **CC before/after** (Ch4): 4→11 is "more than doubled" ✓; the +7 rise and −7 fall
  "almost exactly matching" ✓; cycling 4→2 "halved" ✓.
- **Daily architecture** (Ch9): 9 + 63 + 18 = 90 ✓.
- **Cambridge-book claim** (Ch9): IELTS 21 flagged as needing verification, correctly.

### Examples that work exactly as advertised

Worked individually and confirmed correct:

- **Ch2** — form completion (2 m / 1.4 m / 65, with 40+25 = 65 ✓ and the self-
  correction on width ✓); note completion (a) *crèche* by subtraction ✓, (b)
  *converted* filtered by the printed `1990s` ✓, (c) *the regional council* after the
  negated lead-in ✓; table completion (*Long Shadow* / 6 euros, answer-first
  correction ✓); flow chart (*two references* / *supervisor*, with the narrated
  backtrack ✓); sentence completion (*budgeting* fits, *got good at budgeting*
  breaches ✓); MCQ single (**C**, via "the top one" ✓); MCQ multiple (**D** and **F**,
  neither word spoken ✓ — the best item in the chapter); matching (a) **C** via
  "Forget that one, then" ✓, (b) *Miller's* with "not central ≠ quiet" ✓.
- **Ch3** — Type 1 MC (**B**, with *mechanism*/*failed* correctly identified as the
  distractor sitting in the clause that says the opposite ✓); Type 3 items 2, 3 and 4
  (NOT GIVEN / YES / NOT GIVEN, all correct, and the *attribution gap* item is
  excellent); Type 5 headings (**ii** over the one-sentence match ✓); Type 6
  (**Halvorsen**, *argues* vs *showed* ✓); Type 7 (**C**, A failing on number and B on
  agent ✓); Type 8 (*agate* ✓); Type 11 (*1247*, not *in 1247* ✓); the *numerous* vs
  *most* → NOT GIVEN and *every … except Portsea* → FALSE pair ✓; and both
  reading-vs-inferring items ✓.
- **Ch6** — all five band-6/band-7 pairs contain every structure claimed for them:
  Part 1 (conditional, contrast, causal clause, elliptical opener, stance ✓); Part 2
  (relative clause, past perfect continuous, *when*-clause ✓); Part 3 (*less about X
  than about Y*, perfect participle, modal, sentential relative ✓); GRA (second
  conditional clean, *that in turn take* a genuine third-person *-s* omission ✓);
  the rubber-band drill lines genuinely equalise ✓.
- **Ch8** — all ~90 ✗/✓ pairs are genuinely wrong and genuinely right, the stated
  rule explains the error in every case, and the article counter-list is correct as
  printed. The resumptive-pronoun set, the *Although … but* / *Despite* + clause
  split, the intransitive-passive set, the dangling-participle set, the
  preposition table and the false-friend table all check out. Chapter 8 is the
  cleanest chapter in the book on Task C, which is why the two article errors sit in
  Chapters 4 and 5 rather than here.

---

## Recommended fix order

1. **Issue 3** — the incomplete /p/ fix. It is the one the changelog believes is
   closed, and it is a one-sentence edit.
2. **Issues 1 and 13** — the two Chapter 3 examples that teach wrong reasoning.
3. **Issue 2** — the raw-score table, because it is a chapter debunking another
   chapter's headline.
4. **Issues 4 and 5** — the two article examples on the wrong side of the book's own
   counter-list, which is the reader's highest-value error class.
5. **Issues 7, 8 and 9** — the three model answers that are factually wrong (word
   count, figure, stress mark).
6. Everything else.
