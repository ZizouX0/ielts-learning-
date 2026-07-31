# V2 — Band Descriptor Audit (adversarial)

**Auditor:** V2 — Band Descriptor Auditor
**Date:** 2026-07-31
**Scope:** all nine chapters in `ielts-book/chapters/`, closest attention to Ch 4–8.

## Sources fetched and edition-verified

Every claim below was checked against the PDFs I downloaded myself, not against the
repo's research notes. Metadata printed via `pdfplumber` and confirmed before use:

| Document | `CreationDate` | Verdict |
|---|---|---|
| `ielts-writing-band-descriptors.pdf` | `D:20230503120242+01'00'` | ✅ current (May 2023) |
| `ielts-writing-key-assessment-criteria.pdf` | `D:20230503102438+01'00'` | ✅ current |
| `ielts-speaking-band-descriptors.pdf` | `D:20250916161031+01'00'` | ✅ current (16 Sep 2025) |
| `ielts-speaking-key-assessment-criteria.pdf` | `D:20230503102329+01'00'` | ✅ current |

Also pulled for cross-checking, and **not** cited as current: the superseded public
Speaking descriptor (`CreationDate D:20080929113907`, `ModDate D:20130521105425`,
Company `UCLES`) — the book's claim in Ch 6 that this file "was created in 2008 and
last modified in 2013" is **exactly right**.

Official examiner-commented scripts used as evidence: `Academic Writing Sample Tasks`
(2023, 26 pp.) and `Sample candidate responses … with band scores and examiner
comments` (CD, 2023, 5 pp.).

**Method note on the bold claim.** Several chapters make load-bearing claims about
which descriptor text is set in **bold** (the legend reserves bold for "negative
features that will limit a rating"). Text extraction cannot see bold, so I extracted
per-character `fontname` and mapped `OpenSans-Bold` runs to band rows. That test is
what produced the audit's largest finding.

---

# Task A — scoring advice vs. the actual descriptor wording

## The eight specific verifications requested

**1. Band 7 Task Achievement (Task 1), 2023 wording — CONFIRMED.**
The band-7 Task 1 TA cell reads, verbatim: *"(Academic) It presents a clear overview,
the data are appropriately categorised, and main trends or differences are
identified."* Ch 4 quotes `"the data are appropriately categorised"` accurately and
correctly labels it Academic-only. The 6→7 gate it builds on that (clear not merely
attempted · categorised · trends named) is a faithful reading. Band 6 does say only
*"A relevant overview is attempted"*, so the "group, don't list" thesis is in the mark
scheme, exactly as claimed.

**2. Scoping of the "no overview" claim — CONFIRMED, and correctly scoped.**
Ch 4's myth entry ("Missing the overview caps **Task Achievement**… it does not cap
the overall band") is right, and its supporting script is real. Sample Tasks 2023
p. 15, **Band 7**: *"This test taker uses an inappropriate format at times (e.g. the
letter-style opening and personal comments) and this limits the band for Task
Achievement… there is no clear overview… A wide range of structures is also used
fluently with only occasional slight error and the majority of sentences are
error-free. In spite of the high level of language proficiency, the flaws in format
and organisation limit the rating for this response to Band 7."* The book's framing —
capped criterion, carried by the other three — is precisely what the examiner wrote.

**3. Band 7 Speaking Fluency, 2025 wording — CONFIRMED, and the book is right where
most material is wrong.**
Band 7 FC, verbatim: *"Some hesitation, repetition and/or self-correction may occur,
**often mid-sentence** and indicate problems with accessing appropriate language.
However, these will not affect coherence."* Band 8: *"Hesitation may occasionally be
used to find words or grammar, but **most will be content related**."* So yes:
band-7 hesitation *is* language-related and mid-sentence, the only requirement is
coherence survival, and content-related hesitation is the band-**8** line. The 2008
file said merely *"may demonstrate language-related hesitation at times"* — "often
mid-sentence" is genuinely new in 2025. Ch 6 is correct.

**4. "A few basic errors persist" at bands 7 and 8 — CONFIRMED with one slip.**
Speaking band 7 GRA: *"A few basic errors persist."* Band 8 GRA: *"A few basic errors
**may** persist."* Ch 6's decoder table reproduces both correctly (7 = "persist",
8 = "may persist"). Ch 8's prose ("appears at band 7 and band 8 alike") drops the
modal — see MINOR-9. The bigger problem is what the book *does* with the tolerance —
see MAJOR-2.

**5. 2025 Speaking GRA dropped "complex" from the range clause — CONFIRMED verbatim.**
Old (2008/2013): *"uses a range of **complex** structures with some flexibility."*
Current (2025): *"A range of structures flexibly used. Error-free sentences are
frequent. **Both simple and complex sentences are used effectively** despite some
errors."* Ch 8's Myth 3 and Ch 6's decoder are both exactly right.

**6. Spelling and word formation under Lexical Resource — CONFIRMED.**
`Writing key assessment criteria` p. 4 lists under LR: *"the density and communicative
effect of errors in spelling"* and *"the density and communicative effect of errors in
word formation."* GRA lists structures, accuracy, error density and **punctuation** —
no spelling. Spelling/word formation appear in the LR cell at every band from 2 to 9.
Ch 7 and Ch 8 both state this correctly and consistently.

**7. The band-6 "risk-taker" line — CONFIRMED verbatim, but NOT in bold.**
Band 6 LR, Task 1 and Task 2 alike: *"If the writer is a risk-taker, there will be a
wider range of vocabulary used but higher degrees of inaccuracy or inappropriacy."*
The clause exists, at band 6, in both grids. **The claim that it is printed in bold is
false** — see MAJOR-1.

**8. The band-6 GRA limiter — CONFIRMED verbatim, but NOT in bold.**
Band 6 GRA: *"Examples of more complex structures are not marked by the same level of
accuracy as in simple structures."* (Band 5: *"the greatest accuracy is achieved on
simple sentences."*) Ch 8's accuracy-parity thesis is well founded. The bold claim
attached to it is false — see MAJOR-1.

---

# Findings

### [MAJOR] — "Printed in bold" is false in Ch 7 and Ch 8, and Ch 5 already refutes it

**Chapter:** 07, opening + Myth 1 + Myth 3 + 60-second summary; 08, Band descriptor decoder

**The book says:**
> Ch 7, opening: "It sits in the **band 6** Lexical Resource cell of the current
> Writing descriptors, in Task 1 and Task 2 alike, and **it is printed in bold** — and
> the descriptor's own header rubric says bold marks features that **limit** a rating"
>
> Ch 7, Myth 1: "The band-6 cell contains, **in bold**, a description of exactly this
> candidate and places them at band 6."
>
> Ch 7, Myth 3: "The LR descriptor names this at **band 4**, **in bold**: inappropriate
> use of lexical chunks…"
>
> Ch 8, decoder: "The band-6 accuracy cell is **set in bold in the original**, and the
> PDF's own legend reserves bold for negative features that limit a rating."

**The descriptor says:** None of these is bold. Per-character font extraction from
`ielts-writing-band-descriptors.pdf`:

| Phrase | Band | Font |
|---|---|---|
| `risk-taker, … wider … inaccuracy … inappropriacy` (T1 **and** T2) | 6 LR | `OpenSans-Regular` |
| `not marked by the same level of accuracy` (T1 **and** T2) | 6 GRA | `OpenSans-Regular` |
| `faulty or mechanical` | 6 CC | `OpenSans-Regular` |
| `(e.g. memorised phrases, formulaic language…)` | 4 LR | `OpenSans-Regular` |
| `incompletely addressed` | **5** TR | `OpenSans-Bold` |
| `Paragraphing may be inadequate or missing` | **5** CC | `OpenSans-Bold` |
| `There may be no data to support the description` | **5** TA | `OpenSans-Bold` |
| `memorised.` (total-memorisation clause) | **0** | `OpenSans-Bold` |

The complete bold inventory on the two pages covering bands 6 and 5 sits **entirely at
band 5**. The page covering bands 9, 8 and 7 contains **no bold body text at all**.

This is not an obscure inconsistency: **Ch 5 states the correct fact and invites the
reader to check it** — *"Extract the bold runs from the Task 2 descriptor pages by font
name… **There is not one bolded negative feature at bands 6, 7, 8 or 9**."* I ran
exactly that extraction. Ch 5 is right; Ch 7 and Ch 8 are wrong. A reader who follows
Ch 5's instruction will catch the book contradicting itself.

**Why this matters:** The *advice* survives — the risk-taker clause really is at band 6,
and the GRA limiter really is at band 6, so "thesaurus strategy stalls at 6" and
"close the accuracy gap, don't add complexity" are both sound. What dies is the
book's authority. Ch 7 opens on this claim ("Start with the sentence that decides
everything else in this chapter"), tells the reader the bold is what proves it, and
repeats it in the 60-second summary. A reader who verifies one claim and finds it
false discounts the whole chapter — including the parts that are meticulously right.
It also inflates the clause: a non-bold descriptive feature is *characteristic* of
band 6, whereas a bold one is a hard limiter. The book is claiming the stronger
status without entitlement.

**Fix:** Delete every "in bold" assertion at bands 4 and 6 and replace with the
status the text actually has.

- Ch 7 opening → "It sits in the **band 6** Lexical Resource cell of the current Writing
  descriptors, in Task 1 and Task 2 alike. It is not one of the bolded rating-limiting
  features — bold is reserved for bands 5 and below — but it does not need to be. It is
  a **positive-feature description of what a band-6 script looks like**, and a script
  must fully fit a band's positive features to be rated there. IELTS has written the
  thesaurus candidate into the definition of band 6."
- Ch 7 Myth 1 → "The band-6 cell contains a description of exactly this candidate and
  places them at band 6."
- Ch 7 Myth 3 → "The LR descriptor names this at **band 4**: inappropriate use of
  lexical chunks…"
- Ch 7 60-second summary → "The current descriptors describe, at **band 6**, the
  candidate who reaches for a wider range at the cost of accuracy."
- Ch 8 decoder → delete the sentence "The band-6 accuracy cell is set in bold in the
  original, and the PDF's own legend reserves bold for negative features that limit a
  rating." Replace with: "That clause is the whole of the band-6 GRA definition on
  accuracy. It is not bolded — bold starts at band 5 — but it does not have to be:
  fitting it *is* what band 6 means."
- Ch 8 "Your error map" table, row 5 → delete "with a multiplier where the descriptors
  bold it as a limiter" from the ranking-principle paragraph, since nothing in your
  error map is bolded.

---

### [MAJOR] — Ch 6 drops the load-bearing "a few" and tells a band-6 speaker to stop monitoring basic errors

**Chapter:** 06, Tips & tricks #3, L1 alert priority 4, 60-second summary

**The book says:**
> Tip 3: "**Stop hunting basic slips; make complex sentences land.** `[verified]`
> Band-7 GRA now states that both simple and complex sentences are used effectively
> despite some errors, and that **a few basic errors persist** — band 8 permits the
> same. **Your missing third-person *-s* is not what keeps you at 6.** A botched
> conditional is."
>
> L1 alert, priority 4: "**Articles, uncountables, third-person -s.** Leave them alone
> during the test; fix them in writing practice…"
>
> 60-second summary: "Band 7 now permits a few basic errors to persist, and so does
> band 8. **Your articles and your third-person *-s* are not what is capping you. Stop
> hunting slips**…"

**The descriptor says:** Band 7 GRA tolerates *"**A few** basic errors persist."* The
quantifier is the entire content of the clause. The official Speaking key assessment
criteria defines accuracy by *"error density (the number of grammatical errors in a
given amount of speech)"*. A tolerance of "a few" is not a licence for a *habitual*
pattern; a habitual pattern is a density statement, and density is the named metric.

**Why this matters:** This is addressed to a reader whose documented profile is
habitual, not occasional. The book's own Chapter 8 quantifies it from the same IELTS
study it cites here: **70.6% third-person `-s` error at band 6 falling to 7.6% at band
7 — "the sharpest cliff of any morpheme"** — and Ch 8 draws the correct conclusion in
one line: *"The target is **occasional slip**, not **habitual omission**."* Ch 6 quotes
the tolerance and omits the threshold. A reader at 70% omission who follows Ch 6's
instruction to "leave them alone during the test" is not exploiting a band-7 tolerance;
he is producing the density that defines band 6, while believing the descriptor has
excused him. Ch 6 is the Speaking chapter, so this is the version he will act on in
the room.

The reallocation-of-attention argument underneath is genuinely good and worth keeping.
It just needs the gate in front of it.

**Fix:** Insert the threshold everywhere the tolerance appears.

- Tip 3 → "**Stop hunting basic slips — once they are already occasional; make complex
  sentences land.** `[verified]` Band-7 GRA states that both simple and complex
  sentences are used effectively despite some errors, and that **a few** basic errors
  persist. Read *a few* strictly: it is a density claim, and accuracy is officially
  rated on error density. The IELTS study puts third-person `-s` at 70.6% error at band
  6 and 7.6% at band 7 — so an *occasional* dropped `-s` will not keep you at 6, and a
  *habitual* one is precisely what does. Fix the habit in writing practice until it is
  occasional. Then stop monitoring it in speech and spend the attention on making the
  conditional land."
- L1 alert priority 4 → "**Articles, uncountables, third-person `-s` — once your
  written error rate is already under one in ten.** Leave them alone *during the test*;
  fix them in writing practice, where you have time to monitor. If your written rate is
  still one in three, this is not yet a reallocation you have earned — it is your
  binding constraint, and Chapter 8 is where it gets fixed."
- 60-second summary → "Band 7 permits **a few** basic errors to persist — a few, not a
  habit. Once your `-s` and your articles are occasional rather than systematic, stop
  hunting slips in the room and make complex sentences **land**."

---

### [MAJOR] — Ch 6 teaches deliberate repetition as a fluency technique and tags it `[verified]`

**Chapter:** 06, Tips & tricks #1; Self-test #6; 60-second summary

**The book says:**
> "**Train sentence recovery, not hesitation elimination.** `[verified]` … So when you
> stall mid-clause, **repeat your last two or three words and continue the same
> structure.**"
>
> 60-second summary: "So the trainable skill is **sentence recovery**: when you stall,
> repeat your last two or three words and finish the same structure. **Never abandon
> and restart.**"

**The descriptor says:** Band 7 FC says repetition *"may occur"* — it **tolerates** the
phenomenon, it does not endorse manufacturing it. One band down, band 6 FC:
*"Coherence may be lost at times as a result of hesitation, **repetition** and/or
self-correction."* Two bands down, band 5: *"Usually able to keep going, but **relies
on repetition** and self-correction to do so."* And the key assessment criteria names,
under speech continuity, *"functionless repetitions of words and phrases"* as a
negative fluency indicator. Bands 9 and 8 are both defined as *"Fluent with only very
occasional repetition or self-correction."* Repetition is a **descending** feature
across the whole scale — the less of it, the higher the band.

**Why this matters:** The inference chain — "band 7 tolerates repetition, therefore
repetition is a safe deliberate tactic" — does not hold, and `[verified]` is the wrong
tag for it. The book's own defence (that the criteria penalise only *functionless*
repetition, so a functional recovery repeat is exempt) is an interpretation the
examiner does not have access to: he hears repetition and rates density. Turning a
tolerated symptom into a trained reflex is how a candidate manufactures the band-5
profile — *relies on repetition to keep going* — while believing he is executing a
band-7 behaviour. The book compounds it by drilling the habit in Self-test #6 ("do you
repeat your last two or three words… rather than restarting?") and by absolutising it
in the summary ("Never abandon and restart"), which is flatly contradicted by the
tip's own escape hatch four lines earlier ("end the clause short, breathe, and open a
clean new sentence").

**Fix:** Downgrade the tag and demote repetition from first resort to last.

- Tip 1 → "**Train sentence recovery, not hesitation elimination.** `[expert
  consensus — descriptor-derived, not stated]` The band-7 Fluency cell says
  hesitation, repetition and self-correction **do** occur at 7, often mid-sentence, and
  **do** signal difficulty accessing language — the only requirement is that they not
  affect coherence. So the target is not silence, it is a thread that survives.
  **In order of preference:** (1) pause, breathe, and complete the structure you
  started — a filled pause costs less than a repeat; (2) if the word is gone, route
  round it — paraphrase is separately credited at bands 6, 7 and 8; (3) only if both
  fail, repeat your last two or three words and continue the same structure. Keep (3)
  rare. Repetition is a **descending** feature of the scale — bands 8 and 9 are defined
  by *very occasional* repetition, band 6 names it as a coherence-breaker, and band 5
  is defined by *relying* on it. It is a rescue, not a technique."
- Self-test #6 → "When you stall mid-sentence, do you finish the structure you started
  — by pausing, or by paraphrasing round the gap — rather than abandoning and
  restarting?"
- 60-second summary → "So the trainable skill is **sentence recovery**: when you stall,
  hold the structure and finish it — pause, or paraphrase round the missing word.
  Abandon and restart only when the proposition is genuinely gone, and keep repeating
  your own last words as a last resort, not a habit."

---

### [MAJOR] — Ch 9's grammar plan tells a sub-6.0 reader to add complex sentences, which Ch 8 spends a chapter refuting

**Chapter:** 09, 10-week plan week 3; Band descriptor decoder step 2.4

**The book says:**
> 10-week plan, week 3: "Grammar block 2 — relative clauses, conditionals, concession.
> **Band 7 GRA needs a *range* of complex forms, not error-free simple ones**"
> Milestone: "**Every essay contains 4+ correctly formed complex sentences**"
>
> Decoder step 2.4: "Then count *types* of complex structure — **band 7 wants range,
> not merely accurate simple sentences.**"

**The descriptor says:** Band 6 GRA already credits *"A mix of simple and complex
sentence forms"* — the presence of complex forms is not the gate. What separates 6
from 7 is the clause immediately after: *"Examples of more complex structures are
**not marked by the same level of accuracy** as in simple structures."* Band 7 asks for
*"A variety of complex structures … with some flexibility and accuracy"* **and**
*"error-free sentences are frequent."* Range and accuracy are conjunctive, not
alternative.

**Why this matters:** Ch 8's spine is the exact opposite instruction, stated as the
governing principle of the whole chapter: *"The 5 → 6 → 7 ladder is therefore **not a
complexity ladder**. It is an accuracy-parity ladder… **a band-6 writer who responds by
adding more complex sentences at his current accuracy moves down, not up.**"* Ch 8's
Myth 1 is literally *"More complex sentences means a higher GRA band"* — debunked — and
its Myth 2 debunks numeric complexity quotas (*"A quota makes you write complex
sentences you do not need and cannot check, which is myth 1 with a number attached"*).

Ch 9 then issues a numeric complexity quota ("4+ correctly formed complex sentences")
to the **10-week reader**, defined two paragraphs earlier as *"a starting point below
6.0"* — precisely the candidate Ch 8 says will be harmed. The "not error-free simple
ones" phrasing invites him to trade the accuracy he has for the range he doesn't, which
is the band-6 limiter made more visible. Since Ch 9 is the plan the reader actually
executes daily, it will beat Ch 8's theory in practice.

**Fix:**

- Week 3 focus → "Grammar block 2 — relative clauses, second conditionals, concession.
  Band 7 GRA needs a **variety** of complex structures *and* frequent error-free
  sentences; band 6 already has the mix, and is capped because its complex sentences
  are less accurate than its simple ones. So drill a small number of structures to
  **control**, not a large number to coverage."
- Week 3 milestone → "Every essay contains **three complex structures you got right**,
  drawn from a fixed repertoire — and no complex sentence you could not check. Measure
  the ratio of error-free sentences, not the count of clauses."
- Decoder step 2.4 → "Then count *types* of complex structure — band 7 wants a variety.
  But score the ratio first: an essay with four clean complex structures beats one with
  eight faulty ones, because band 6 is *defined* by complex sentences that are less
  accurate than the simple ones."

---

### [MAJOR] — Ch 3 builds its headline number on a half-band table Ch 1 explicitly refuses to print

**Chapter:** 03, Band descriptor decoder; 60-second summary

**The book says:**
> Ch 3 prints a nine-row raw-score table including **6.5 = 27–29**, 7.5 = 33–34, 8.5 =
> 37–38, sourced to `ielts.idp.com`, then:
> "### **6.5 → 7.0 is exactly three marks. 27 → 30.**"
> and repeats it in the summary: "There are no band descriptors: **6.5 → 7.0 is exactly
> three marks, 27 → 30.**"

**The descriptor / official position says:** IELTS publishes four anchor points only
(L 16/23/30/35; AR 15/23/30/35), with the caveat that *"The precise number of marks
needed to achieve these band scores will vary slightly from test version to test
version"* — boundaries are equated per version.

**Why this matters:** This is the book contradicting itself on a planning number the
reader will budget six weeks of revision against. **Ch 1 refuses to print this table
and debunks it as a myth**: *"Half-band thresholds (6.5, 7.5) are **not published by
any official source**, so this book will not print them"*, and *"'There's a raw-score
table that tells me exactly what 6.5 needs.' **Not an official one.** … never budget
your revision on the assumption that 26/40 is definitely a 6.5."* **Ch 2 gets it right
too**, labelling its own half-band rows `~26–27 (interpolated — not official)`.
Ch 3 alone prints the table straight and then hard-codes "exactly" into the chapter's
organising claim, repeated in the summary. A reader who targets exactly 30 on a version
whose band-7 boundary sits at 31 misses by one mark on the paper the book calls his
cheapest. The word "exactly" is doing damage that "about" would not.

**Fix:**

- Table caption → add, immediately above the table: "⚠️ **Half-band rows are not
  official.** IELTS publishes four anchors only — 5, 6, 7, 8 — and states the raw score
  for each band varies slightly between versions. The half-bands below are IDP's
  interpolation, reproduced as a planning aid and consistent with the official anchors
  (8 → 35, 7 → 30, 6 → 23, 5 → 15). Do not budget revision against them. See Chapter 1."
- Heading → "### **6.5 → 7.0 is about three marks. Roughly 27 → 30.**"
- Body → "Three marks is this chapter's whole job — and because the band-7 boundary can
  sit a mark higher on your version, **target 32, not 30**. Everything above 30 is
  insurance."
- 60-second summary → "There are no band descriptors, only a raw score: band 7 is
  officially 30/40, the 6.5 boundary is not published, and the gap is about three
  marks. Target 32 so a hard version cannot take band 7 off you."

---

### [MINOR] — Ch 4 debunks the linker myth using band 9's wording labelled as band 8

**Chapter:** 04, Myths ("Use as many linking words as possible"); Band descriptor decoder, CC

**The book says:** "band 8 CC is cohesion the reader does not notice"; decoder band 8
row: "The reader follows with **no effort**."

**The descriptor says:** *"Cohesion is used in such a way that it very rarely attracts
attention"* and *"The message can be followed **effortlessly**"* are both **band 9**.
Band 8 reads *"The message can be followed **with ease**. Information and ideas are
logically presented, sequenced, and cohesion is **well managed**."*

**Why this matters:** The myth's primary reason — band 6 CC is *defined* by cohesion
that is *"faulty or mechanical due to misuse, overuse or omission"* — is correct and
load-bearing, so the debunking works. But the supporting contrast is a band out, which
sets the reader an invisible-cohesion target one band above where he needs it and
misdescribes the 7→8 step in his own decoder.

**Fix:**
- Myth → "Band 6 CC is *defined* by cohesion that is faulty or mechanical through
  misuse, overuse or omission; band 7 still names *some over/under use*; and only at
  band 9 does cohesion stop attracting attention at all. Nothing anywhere in the grid
  rewards quantity."
- Decoder band 8 row → "**8** — The message can be followed **with ease**. Logical
  presentation and sequencing, cohesion **well managed**, paragraphing sufficient and
  appropriate. Occasional lapses allowed."

---

### [MINOR] — The band-7 "half your sentences error-free" target collides with band 8's "majority"

**Chapter:** 04, Tips #5 and Self-test #15; 05, decoder GRA; 08, "How accurate is accurate enough?"

**The book says:**
> Ch 4 Tip 5 `[verified]`: "Band 7 GRA requires error-free sentences to be *frequent*;
> band 8 requires the *majority*. **The working target for 7 is roughly half.**"
> Ch 4 Self-test #15: "is **at least half** completely error-free"
> Ch 5: "in a 280-word essay of about sixteen sentences, if fewer than seven or eight
> are completely clean, you are arguing for a 6."
> Ch 8: "Band 8 asks for the **majority** … so band 7 must be regularly occurring but
> **short of a majority**."

**The descriptor says:** Band 7 = *"error-free sentences are frequent"*; band 8 = *"The
majority of sentences are error-free."* No official source quantifies "frequent".

**Why this matters:** Ch 8's reasoning is the defensible one and it explicitly bounds
band 7 *below* a majority. Ch 4 then sets the band-7 working target *at* a majority,
tags it `[verified]` (it is an inference, not a quotation), and hard-codes it into the
self-test. That makes bands 7 and 8 indistinguishable on the one criterion the book
says you can audit yourself, and it sets a bar the reader will read as unreachable.

**Fix:**
- Ch 4 Tip 5 → change tag to `[expert consensus — derived]` and replace the last
  sentence with: "Band 8 needs the *majority*, so band 7 sits below that — a working
  target of **four in ten clean, rising to five**, is the honest read. Nine sentences
  with three clean is a band 6, however ambitious the other six."
- Ch 4 Self-test #15 → "is **at least four in ten** completely error-free…"
- Ch 5 decoder → "…if fewer than six or seven of sixteen are completely clean, you are
  arguing for a 6; at nine or ten you are arguing for an 8."

---

### [MINOR] — "Self-correction is limiting at all nine bands" is wrong, and Ch 6 contradicts itself

**Chapter:** 06, Myths ("Correct every mistake so the examiner knows you know")

**The book says:** "Self-correction is limiting at **all nine bands**."

**The descriptor says:** Self-correction appears in the Speaking FC column at bands 9,
8, 7, 6, 5 and 4 only. Bands 3, 2 and 1 do not mention it. The chapter's own Tip 6 says
this correctly: *"Self-correction is a limiting feature at every band from **4 to 9**."*

**Fix:** "Self-correction is a limiting feature at every band from 4 to 9; there is no
band at which more is better."

---

### [MINOR] — "Buy one band-8 feature" understates what band 7 Pronunciation asks for

**Chapter:** 06, Tips #2 and decoder, Pronunciation

**The book says:** "**secure every band-6 feature completely, then buy one band-8
feature outright.**"

**The descriptor says:** Band 7 Pron: *"Displays all the positive features of band 6,
and **some, but not all**, of the positive features of band 8."* Band 8 has five
distinct positive features (wide range of phonological features conveying precise/
subtle meaning · sustained rhythm · flexible stress and intonation across long
utterances · easily understood throughout · accent has minimal effect). "Some" of five
is more naturally two or three than one.

**Why this matters:** The strategy (buy stress-timing) is excellent and correctly
identifies band 8's named feature. The arithmetic promise ("one") may leave the reader
short of the band he was told he had bought.

**Fix:** "…secure every band-6 feature completely, then buy band-8 features outright.
Band 7 needs *some* of band 8's five, so budget for **two**: **sustained rhythm** first
— the cheapest, because it is a motor habit — then **flexible stress and intonation
across long utterances**, which the same drills give you."

---

### [MINOR] — Criterion weighting cited to a document that does not state it

**Chapter:** 05, "What the test actually asks" table; 07 opening; 08 opening

**The book says:** Ch 5: "Criteria | Task Response · Coherence and Cohesion · Lexical
Resource · Grammatical Range and Accuracy — four, **equally weighted** inside the task
`[src: Key assessment criteria PDF, p.1]`". Ch 8: "GRA is a quarter of every Writing
task `[src: … key assessment criteria (PDF, 2023), p.1]`".

**The descriptor says:** The `Writing key assessment criteria` PDF names the four
criteria and never mentions weighting. The claim is nevertheless **true** and the book
has the right source elsewhere — Ch 1 quotes ielts.org's *Understanding and setting
IELTS scores*: *"Each task is assessed independently. The criteria are weighted equally
and the score on the task is the average."*

**Fix:** In Ch 5, Ch 7 and Ch 8, change the citation to
`[src: ielts.org — Understanding and setting IELTS scores]`, matching Chapter 1.

---

### [MINOR] — Ch 5's self-test enforces the 300-word ceiling that Ch 5's own M6 debunks

**Chapter:** 05, Self-test #8 vs Myth M6

**The book says:** M6: "'**Never go over 300 words.**' The reverse myth… The official
**7.5** exemplar runs to roughly 375 words and drew no comment on length… **There is a
floor. There is no ceiling.**" Self-test #8: "Is my word count **between 260 and 300**,
counting only words I wrote myself?"

**Why this matters:** Verified — the CD 7.5 exemplar does run ~375 words and the
examiner comment mentions length nowhere. The checklist is the artefact the reader
applies to every essay, so it, not the myth entry, is what he will obey. A reader who
has written 320 well-developed words will cut them to satisfy item 8.

**Fix:** Self-test #8 → "Am I **at or above 260** words, counting only words I wrote
myself — with 270–290 as the comfortable target, and no upper limit beyond what I can
still proofread in three minutes?"

---

### [MINOR] — Ch 7 conflates two different official 7.5 scripts as one

**Chapter:** 07, "The proof that it is density, not range"

**The book says:** A comparison table headed "Band 5.5 script / Band 7.5 script" cited
to `Academic Writing sample tasks (PDF, 2023), Task 2B Scripts A and B`, then: "Now look
at what **the band-7.5 script** actually wrote. A separate official publication
reproduces a 7.5 Task 2 response in full…"

**What the sources say:** Both halves of the table are verified verbatim against Sample
Tasks 2023 — p. 24 (5.5): *"there are **frequent** spelling errors that can cause some
difficulties for the reader, thus **keeping the rating down for the lexical
criterion**"*; p. 26 (7.5): *"these are only **occasional** and **do not limit the
rating** for this criterion."* The density argument is airtight. But the vocabulary
inventory quoted next (*fast food, gadgets, obesity, laziness*) and the "softening"
credit come from the **CD samples PDF's** 7.5 — a **different response to a different
prompt**. "The band-7.5 script" implies one script.

**Fix:** "Now look at what **another** official 7.5 script wrote — a different response,
to a different prompt, published with its own examiner comment `[src: CD example
responses PDF, Part 2, Response 2]`."

---

### [MINOR] — Pluralised uncountables are assigned to LR in two chapters and GRA in a third

**Chapter:** 05, L1 alert #2; 07, "Uncountables that French pluralises"; 08, error map row 4

**The book says:** Ch 5: "Each instance is a **word-formation error under LR**." Ch 7:
"Writing *informations* is a **word-formation error under LR**." Ch 8, error map:
"Uncountables pluralised | **GRA (+LR)**".

**The descriptor says:** IELTS does not adjudicate this. LR covers *"errors in word
formation"*; GRA covers *"the accuracy of simple, compound and complex sentences"* and
error density. Pluralising a mass noun is arguably either.

**Why this matters:** Low stakes — the repair is identical — but the book states a
contested allocation as settled fact in two places and the opposite in a third, and
Ch 8's Myth 7 leans on criterion allocation ("cannot be offset by clean grammar").

**Fix:** Standardise on Ch 8's hedged version everywhere: "Uncountables pluralised —
**GRA, and arguably LR too**, since IELTS files word formation under LR and does not
say which side countability falls. Either way it is scored, and the fix is the same
nine-word list."

---

### [MINOR] — Ch 8 drops the modal from band 8's "may persist"

**Chapter:** 08, Speaking GRA decoder

**The book says:** "**'A few basic errors persist' appears at band 7 and band 8
alike.**"

**The descriptor says:** Band 7: *"A few basic errors persist."* Band 8: *"A few basic
errors **may** persist."* Band 7 asserts that they do; band 8 permits that they might.
Ch 6's decoder table reproduces both correctly.

**Fix:** "**Basic errors are tolerated at 7 and at 8** — band 7 says a few *persist*,
band 8 that a few *may* persist. The difference is real: at 7 they are expected, at 8
they are merely survivable."

---

### [MINOR] — Ch 3's summary contradicts Ch 3's own order table on matching headings

**Chapter:** 03, order table vs 60-second summary

**The book says:** Table row 5: "Matching headings | **Questions yes; the heading
numerals no**", with a careful caveat and the instruction *"Work the paragraphs in
order — safe either way."* Summary: "**Not ordered** — matching information, matching
features, **matching headings**, summary/note/table/flow-chart completion, diagram
labelling."

**Why this matters:** The summary is the part that gets re-read before the test, and it
reverses the chapter's own working instruction. A reader who treats matching headings
as unordered abandons the paragraph-by-paragraph sweep that the 10-step official
strategy is built on.

**Fix:** Summary → "Not ordered — matching information, matching features. Order not
guaranteed — summary/note/table/flow-chart completion, diagram labelling. **Matching
headings: work the paragraphs in order, but never expect heading (i) to belong to
paragraph A.**"

---

### [MINOR] — Ch 9's body-paragraph formula drops the move Ch 5 says separates 6 from 7

**Chapter:** 09, 8-week plan week 3 vs 05, Tips #4

**The book says:** Ch 9: "body paragraph = **claim → explain → example**". Ch 5, Tip 4
`[verified]`: "**The four-move body paragraph: claim → because → so what → instance.**
This *is* the official gloss on Task Response: extension means detail and depth,
support means relevant examples."

**Why this matters:** The dropped move is "so what" — the consequence step. Ch 5's own
band-6/band-7 worked pair turns on it ("*a consequence* (which households gain most)"),
and band 7 TR asks for main ideas *"extended and supported"* where band 6 has them
*"insufficiently developed."* Three moves is the band-6 shape.

**Fix:** Week 3 focus → "body paragraph = **claim → because → so what → instance**
(Ch 5 Tip 4). The *so what* is the move that turns a stated idea into an extended one."

---

### [MINOR] — Ch 8 licenses short Writing sentences from a Speaking descriptor, when official Writing commentary flags exactly that

**Chapter:** 08, Myths #3

**The book says:** "'Never write a simple sentence — they look basic.' The **current**
Speaking descriptor (the file created 2025-09-16) dropped the word *complex* from the
band-7 range clause and now states outright that both simple and complex sentences are
used **effectively** at band 7… A short declarative is error-free by construction and
is a rhetorical instrument."

**The descriptor says:** That change is real and verified — but it is in the **Speaking**
grid. The Writing band-7 GRA cell still reads *"A variety of **complex** structures is
used with some flexibility and accuracy."* The word was not dropped there.

**Why this matters:** The myth is about Writing as much as Speaking, and the
counterweight the book offers is an IDP teaching page. There is stronger, directly
on-point official Writing evidence sitting in the book's own source set and unused:
the CD 7.5 exemplar's examiner comment ends *"there is some **overuse of rather short
sentence forms**."* An official Writing examiner penalised short-sentence overuse at
7.5 — that is the counterweight, and it makes the myth entry unarguable.

**Fix:** Add after the IDP sentence: "And the Writing evidence is direct: the official
**7.5** CD exemplar was told there was *some overuse of rather short sentence forms* —
in a script otherwise praised for a variety of complex structures. Note too that
*complex* was dropped only from the **Speaking** band-7 range clause; Writing band 7
still asks for *a variety of complex structures*. All-simple is capped in both papers;
simple **among** complex is rewarded in both."

---

### [MINOR] — Ch 4 overstates what the band-5 TA cell "explicitly" says

**Chapter:** 04, Myths ("A missing overview means you cannot get band 7")

**The book says:** "Note also that the **band-5 TA descriptor explicitly describes an
overview-less script**, so the common claim that no overview means below band 5 is
simply wrong."

**The descriptor says:** Band 5 Task 1 Academic TA never uses the word *overview*. The
nearest wording is *"There may be a tendency to focus on details (without referring to
the bigger picture)"* — which supports the book's conclusion, but by paraphrase, not
explicitly.

**Fix:** "Note also that the band-5 TA cell describes a script with *a tendency to focus
on details without referring to the bigger picture* — an overview-less script in all but
the word — so the common claim that no overview means below band 5 is simply wrong."

---

# Task B — the helps-not-hurts sweep, chapters 1–9

I ran every tip, myth and checklist item against one question: *how does this raise a
band at 6.5–7.5, per the descriptors?* The book survives this test unusually well. What
I hunted for and **did not** find:

- **Memorised templates.** Nowhere endorsed. Ch 5 M2 correctly identifies the risk as
  **band 0**, not merely zero credit; Ch 7 M3 traces memorised chunks to band 4 LR;
  Ch 8 M5 to the plagiarism clause. The distinction Ch 5 Tip 12 draws — memorise
  *concepts*, never sentences — is the right one.
- **Forced rare vocabulary.** Actively campaigned against, in three chapters, on the
  correct grounds (the band-6 risk-taker clause). Ch 7's *"pecuniary/ameliorate"*
  worked pair is a genuinely good demonstration.
- **Linker-stuffing.** Debunked in Ch 4, Ch 5 (M3), Ch 6 and Ch 7 (M6), each time with
  the right mechanism (over-use named at band 6 *and* band 7). Ch 5 Tip 7 correctly
  adds the **under**-use side, which almost no prep material does, and both halves are
  backed by real examiner comments I verified (7.5 docked for four sequencers in one
  paragraph; 6.5 told better linkers would have helped).
- **"Write very long" / "write very short."** Both refuted, and the *mechanism* is
  right: under-length is marked through Task Response/Achievement, not a tariff. I
  independently confirmed the structural claim underpinning this — the bold inventory
  contains no rating-limiting feature above band 5.
- **"Always pick C" folklore.** Absent. Ch 3 M2 goes further and refuses to invent an
  answer-key distribution for NOT GIVEN — replacing the statistical version with a
  procedural one. That is the correct call.
- **Risky guessing presented as reliable.** Not found. Guessing advice is confined to
  Listening/Reading, where it is correct (no negative marking) and correctly bounded
  (one answer per gap, inside the word limit).
- **Fabricated statistics.** The book hunts these itself — Ch 7 M7 and Ch 3 M14 both
  refuse to repeat an untraceable number, and Ch 7 explicitly declines to print the
  figure even inside its own debunking. That is the right instinct.
- **Accuracy traded for showiness.** The whole of Ch 8 argues the opposite, correctly.

**Myths sections — debunked with the right reason?** I checked the mechanism of every
myth entry in all nine chapters against the descriptors. All are sound except two, both
already logged: Ch 4's linker myth cites band 9's wording as band 8 (MINOR-1), and
Ch 6's self-correction myth says "all nine bands" where the range is 4–9 (MINOR-3).
Ch 7's Myth 1 and Myth 3 reach the right conclusion via a false premise (the bold
claim, MAJOR-1).

**Where the book is stronger than its sources require** — worth preserving through any
edit:
- Ch 5's structural bold-extraction argument. I reproduced it independently and it
  holds exactly.
- Ch 7's density-not-range table. Verified word for word against Sample Tasks 2023
  pp. 24 and 26; the examiner really did write *frequent* / *keeping the rating down*
  against *occasional* / *do not limit the rating*. This is the best-evidenced
  paragraph in the book.
- Ch 4's band-7-overall-without-an-overview correction, and the 8.5 script held below 9
  for counting stages instead of naming phases. Both verified verbatim.
- Ch 5 Tip 15 (*e.g.* logged as a lapse in an **8.5** script) — verified on p. 22.
- Ch 6's refusal to treat the 2008/2013 Speaking file as current, with the metadata
  dates exactly right.
- Ch 3's insistence that FALSE requires a pointable contradiction.
- Ch 9's honest account of AI grading drift.

---

# Summary

| Severity | Count |
|---|---|
| CRITICAL | 0 |
| MAJOR | 5 |
| MINOR | 13 |

**No CRITICAL findings, and that is a real verdict rather than a failure to look.** I
went after every scoring claim in the book with the official PDFs open, including a
font-level forensic test the book itself proposed. Nothing in these nine chapters
would push a band-6 candidate down a band if followed as written. The five MAJORs are
of two kinds: **one false claim about the descriptor document** (the bold assertion,
which the book's own Ch 5 refutes) and **four places where a chapter's operational
instruction contradicts another chapter's correct analysis** — Ch 6 vs Ch 8 on basic
errors, Ch 6 vs its own tolerance/technique distinction on repetition, Ch 9 vs Ch 8 on
complexity, Ch 3 vs Ch 1 on half-band thresholds. In every case the book already
contains the right version somewhere; the fix is to propagate it, not to research
anything new.

The single highest-value repair is **MAJOR-1**: it is a factually false statement about
the official document, it is repeated four times across two chapters, it is the opening
premise of Chapter 7, and the book elsewhere hands the reader the exact method that
disproves it.
