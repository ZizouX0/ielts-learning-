# V1 — Fact Audit (adversarial verification)

**Auditor:** V1 — Fact Auditor
**Date of audit:** 2026-07-31. Every URL below was fetched fresh today; no claim in this
report rests on `ielts-book/research/`.
**Scope:** all nine chapters in `ielts-book/chapters/`. Every factual claim about format,
timing, question counts, word limits, scoring, band conversion, rounding, penalties,
policy, fees, ID and results timelines was extracted and re-tested against Tier 1 sources
(ielts.org, takeielts.britishcouncil.org, ielts.idp.com, cambridgeenglish.org) plus the
primary PDFs those sites publish.

**Headline:** the book is unusually well sourced, and several claims I expected to break
survived (see *Claims verified clean*, and especially the four marked ⭐ where I tried
hardest to break them and could not). But there is **one factually wrong claim repeated
across three chapters** — that no official source publishes half-band raw-score
thresholds — and it is load-bearing: it drives Chapter 1's refusal to print a 6.5 target
and Chapter 2's "interpolated, not official" mark budget. There is also a cluster of
places where the book *understates* how well sourced it is, downgrading to Tier 2 or
"unsettled" three things that are officially stated verbatim.

**Counts:** 3 CRITICAL · 8 MAJOR · 9 MINOR.

---

## CRITICAL

### [CRITICAL] — "Half-band thresholds are not published by any official source" is false
**Chapter:** 01, *Band descriptor decoder — the band math* (also 01 *Myths*, 01
*60-second summary*, 02 *Band descriptor decoder*)
**The book says:** "**Half-band thresholds (6.5, 7.5) are not published by any official
source**, so this book will not print them."
**What I found:** IDP IELTS — a joint owner of IELTS, and a source this book itself treats
as Tier 1 throughout (it is cited ~40 times) — publishes complete raw-score-to-band tables
**including every half band**, for both papers:

*Academic Reading (ielts.idp.com):* 39–40 = 9 · 37–38 = 8.5 · 35–36 = 8 · 33–34 = 7.5 ·
30–32 = 7 · 27–29 = 6.5 · 23–26 = 6 · 19–22 = 5.5 · 15–18 = 5 · 13–14 = 4.5 · 10–12 = 4 ·
8–9 = 3.5 · 6–7 = 3 · 4–5 = 2.5, with the caveat "As a result of the variations in texts
used on different occasions, actual scores may differ slightly between tests."

*Listening (ielts.idp.com):* 39–40 = 9 · 37–38 = 8.5 · 35–36 = 8 · 32–34 = 7.5 ·
30–31 = 7 · 26–29 = 6.5 · 23–25 = 6 · 18–22 = 5.5 · 16–17 = 5 · 13–15 = 4.5 · 11–12 = 4,
with the caveat "The IELTS Listening band score tables that are shown here highlight the
average number of marks required to achieve a particular IELTS band score. Actual marks
may vary slightly between tests due to the variation in listening questions used on
different occasions."

The book **already knows this**: Chapter 3 prints the Reading table verbatim and sources it
to `[src: ielts.idp.com — Reading band scores]`. So Chapter 1 and Chapter 3 contradict each
other on a central fact.
**Source:** https://ielts.idp.com/southafrica/results/scores/reading and
https://ielts.idp.com/vietnam/results/scores/listening/en-gb — both fetched 2026-07-31.
**Fix:** replace the sentence with:

> **ielts.org and the British Council publish only four anchor points per paper (bands 5,
> 6, 7, 8). IDP — the third joint owner — publishes a full table including half bands, with
> its own caveat that actual marks vary between tests.** This book prints the IDP table
> because it is official, and treats it as an *average* boundary, not a guarantee:
> Listening 6.5 = 26–29, 7 = 30–31, 7.5 = 32–34; Academic Reading 6.5 = 27–29, 7 = 30–32,
> 7.5 = 33–34.

Then delete "so this book will not print them" and update the *Myths* and *60-second
summary* passages below, and the Chapter 2 mark budget.

---

### [CRITICAL] — "IELTS publishes four anchor points per test and nothing else"
**Chapter:** 01, *Myths that hold you back* → "There's a raw-score table that tells me
exactly what 6.5 needs."
**The book says:** "Not an official one. IELTS publishes four anchor points per test and
nothing else, with an explicit warning that the numbers move between versions. Every
'complete' table online reconstructs half-bands from retired practice books."
**What I found:** false on both counts. IDP publishes a complete official table (above), so
"nothing else" is wrong, and the "every complete table online is reconstructed from retired
practice books" claim is a fabricated provenance for a table that is in fact published by a
test owner. The *caveat* half of the myth-busting is correct and should survive.
**Source:** https://ielts.idp.com/southafrica/results/scores/reading — fetched 2026-07-31.
**Fix:**

> **"There's a raw-score table that tells me exactly what 6.5 needs."**
> There is an official one, but it is not a guarantee. ielts.org and the British Council
> publish four anchors per paper (5/6/7/8); IDP publishes a full half-band table. Both
> carry the same warning: "The precise number of marks needed to achieve these band scores
> will vary slightly from test version to test version." **Do instead:** use the IDP table
> as a planning average — Academic Reading 27 is the *bottom* of 6.5, not a safe 6.5 — and
> aim a mark or two above every boundary.

---

### [CRITICAL] — Chapter 2's mark budget is labelled "not official" and understates band 6.5
**Chapter:** 02, *Band descriptor decoder*
**The book says:** "| 6.5 | ~26–27 *(interpolated — not official)* | ~13 |" and
"| 7.5 | ~32 *(interpolated — not official)* | ~8 |", followed by "Official guidance
publishes bands 5, 6, 7 and 8; the half-band rows are interpolations, labelled as such."
**What I found:** the half-band rows are not interpolations — official IDP figures exist,
and they differ from the book's guesses in a way that matters. Official Listening: **6.5 =
26–29** (the book stops at 27, so it silently tells the reader that 28 and 29 are already
band 7 territory when they are not), **7 = 30–31**, **7.5 = 32–34**.
**Source:** https://ielts.idp.com/vietnam/results/scores/listening/en-gb — fetched
2026-07-31.
**Fix:** replace the table body and the note beneath it with:

> | Target band | Official raw marks / 40 (IDP) | Losses affordable |
> |---|---|---|
> | 6.0 | 23–25 | 15–17 |
> | 6.5 | 26–29 | 11–14 |
> | **7.0** | **30–31** | **9–10** |
> | 7.5 | 32–34 | 6–8 |
> | 8.0 | 35–36 | 4–5 |
>
> ielts.org and the British Council publish only the band 5/6/7/8 anchors; IDP publishes
> the full table above. IDP's own caveat: these are *average* marks and "actual marks may
> vary slightly between tests". Plan against the **top** of each band, not the bottom.

---

## MAJOR

### [MAJOR] — The Speaking "asking for help" table is officially sourced, and the book says it is not
**Chapter:** 06, *What the test actually asks* → *Asking for help*
**The book says:** "This split is not on any official page I could retrieve; it rests on
three independent preparation sources that agree `[src: ieltsliz.com]` `[src:
ieltsadvantage.com]` `[src: magoosh.com]`." … "Honest caveat: IDP's Part 1 article lists
both 'Could you repeat that?' and 'What does ___ mean?' without naming a part, so the Part 1
ban is probable rather than certain."
**What I found:** it is on an official page — the **Cambridge English IELTS Academic FAQs
PDF, p.11**, the same document the book cites eleven times elsewhere:

> "What should I do if I don't understand a question, a word, or the Part 2 task? You should
> tell the examiner that you don't understand. **In Part 1, the examiner will be able to
> repeat the question. In Part 2 you should look carefully at the task card** because you
> may be able to guess the meaning of a word you have not understood. **In Part 3, the
> examiner will be able to repeat the question or ask it in a different way, or may be able
> to help you to understand the question. If you don't understand a word, the examiner will
> be able to give you a brief explanation.** The most important thing is not to ask the
> examiner to repeat every question or explain every word."

That is the book's table exactly: Part 1 repetition only; Part 2 nothing but the card; Part 3
repetition *and* rephrasing *and* word explanation.
**Source:** https://www.cambridgeenglish.org/images/269898-ielts-academic-faqs.pdf, p.11 —
fetched 2026-07-31.
**Fix:** delete the three Tier 2 citations and the "probable rather than certain" caveat.
Replace the sentence introducing the table with:

> This split is officially stated `[src: cambridgeenglish.org — IELTS FAQs, Academic
> module (PDF), p.11]`, and the same source adds the limit that makes it usable: "The most
> important thing is not to ask the examiner to repeat every question or explain every
> word."

Also update Self-test item 4 and the *Myths* entry "Never ask the examiner to repeat",
which currently says "explanation exists only in Part 3" as a derived rule — it is now a
quotable one.

---

### [MAJOR] — "The examiner cannot stop you before two minutes … unsupported" is contradicted by Cambridge
**Chapter:** 06, *Myths that hold you back*
**The book says:** "**'The examiner cannot stop you before two minutes, and you must signal
if you finish early.'** Widely circulated; unsupported."
**What I found:** the first half is officially supported. Cambridge's Academic FAQs, p.10:
"**Don't worry if the examiner stops you in the Part 2 long turn. It means you have spoken
for 2 minutes.** The examiner has to keep to the timing of the test." And p.11: "You will
have the opportunity to talk for 2 minutes. You should try to talk for the full 2 minutes
to give the examiner a good sample of your English." Only the *second* half — that you must
signal when you finish early — is unsupported.
**Source:** https://www.cambridgeenglish.org/images/269898-ielts-academic-faqs.pdf,
pp.10–11 — fetched 2026-07-31.
**Fix:**

> **"You must signal if you finish Part 2 early."** Unsupported — no official source says
> so, and the official transcript shows the examiner simply moving on after a short turn.
> What *is* official is the other half of this folklore: being stopped means you reached
> two minutes — "Don't worry if the examiner stops you in the Part 2 long turn. It means
> you have spoken for 2 minutes" `[src: cambridgeenglish.org — IELTS FAQs, Academic module
> (PDF), p.10]`. **Do instead:** keep going until you are stopped; aim to be stopped.

---

### [MAJOR] — The "limited to Band 5" sentence is now verbatim-confirmed; the caveat should go
**Chapter:** 05, *What is still unsettled* (and *What the test actually asks*)
**The book says:** "**The 'limited to Band 5' sentence.** ielts.org's Writing test
resources page states that if you do not discuss both parts you will be limited to band 5.
It was reached through a rendering layer rather than read verbatim off the live page, so
treat it as officially stated but pending verbatim confirmation."
**What I found:** confirmed verbatim on the live page today, exactly as the book quotes it:
"**If you don't discuss both, you will be limited to Band 5.**" The same page also confirms
verbatim three other things the book relies on: "Task 1 is worth a third of your overall
mark for Writing. Task 2 is worth two thirds."; "You can 'extend' your ideas by going into
more detail and you can 'support' them by giving examples."; and the definition of complex
structures — "They include passive forms, modal verbs, comparative structures or complex
noun phrases."
**Source:** https://ielts.org/take-a-test/preparation-resources/writing-test-resources —
fetched 2026-07-31.
**Fix:** delete that bullet from *What is still unsettled* entirely, and change the
in-chapter framing from "ielts.org's guidance says" to a flat verbatim quotation with the
citation. This is a strengthening, not a correction — but leaving the hedge in place makes
the book's strongest Task Response claim look weaker than it is.

---

### [MAJOR] — Chapter 1's reconciliation of 2h45 vs 2h40 is unsourced inference, and it contradicts Chapter 9
**Chapter:** 01, *What the test actually asks*
**The book says:** "Different quantities, not a contradiction: 2h40m is the paper-mode
sitting (Listening 30 + transfer 10 + Reading 60 + Writing 60); 2h45m counts all four
papers including a ~15-minute Speaking test and excludes the paper-only transfer window."
**What I found:** ielts.org publishes 2h40 for the Listening + Reading + Writing session
with **no delivery-mode caveat at all** — "You will do the Listening, Reading, and Writing
sections in one test session. This takes 2 hours 40 minutes, and there are no breaks
between each section of the test." No official source says 2h40 is paper-only. The book's
reconciliation is its own arithmetic, presented as fact, and it is internally inconsistent:
Chapter 9 uses 2h40 as the **computer** test-day figure ("Listening, Reading and Writing run
as one block of **2 hours 40 minutes with no breaks at all**") and the study plans instruct
"two full 2h40 sittings, typed". On computer the components sum to ~2h32 (30 + 2 + 60 + 60),
not 2h40.
**Source:** https://ielts.org/take-a-test/preparation-resources/on-test-day and
https://ielts.org/take-a-test/test-types/ielts-academic-test — both fetched 2026-07-31.
**Fix:**

> You will also see **2 hours 40 minutes** for the Listening + Reading + Writing session,
> with "no breaks between each section of the test" `[src: ielts.org — What to expect on
> IELTS test day]`. ielts.org applies that figure with no delivery-mode caveat, even though
> the computer components sum to about 2h32 (Listening 30 + a 2-minute check + Reading 60 +
> Writing 60). **Treat 2h40 as the session you must be seated and concentrating for, and
> budget against the individual paper timings below rather than either headline.**

---

### [MAJOR] — "British Council Tunisia lists only computer-delivered testing — no paper option" is not what the English pages show
**Chapter:** 01, *What the test actually asks* (and 09, *Things you must ask your centre*
and *L1 alert*)
**The book says (Ch1):** "British Council Tunisia already lists only computer-delivered
testing at a centre and IELTS Online — no paper option."
**The book says (Ch9):** "**Conflicting.** The English dates/fees page and every Tunis
booking link on ielts.org show computer only … while the French BC Tunisia page still lists
'papier ou ordinateur' — very likely stale text." And in *L1 alert*: "Translated pages lag.
Where the French and English versions disagree, the English one is more likely current."
**What I found:** the **English-language** britishcouncil.tn page for IELTS General Training
also lists a paper-based option, with a fee: "The fee for the IELTS General Training
paper-based is 750 TND" and "The fee for the IELTS General Training computer-delivered is
750 TND." So the disagreement is not French-vs-English and the "stale translation"
diagnosis is unsupported. The English dates/fees/locations page does mention only IELTS on
computer and IELTS Online, and does confirm the five locations — so the book's *conclusion*
(book computer at a centre) is still right; the *reasoning* is wrong.
**Source:** https://www.britishcouncil.tn/en/exam/ielts/which-test/general-training and
https://www.britishcouncil.tn/en/exam/ielts/dates-fees-locations — both fetched 2026-07-31.
**Fix (Ch1):**

> British Council Tunisia's dates, fees and locations page lists only IELTS on computer at
> a centre and IELTS Online, across five locations: Tunis, Bizerte, Sousse, Sfax and Gabes
> `[src: britishcouncil.tn — Test dates, fees and locations]`. Other pages on the same site
> — both English and French — still quote paper-based fees, so **the site is not internally
> consistent; ask the centre.** Either way, paper is being retired from mid-2026, and every
> timing, technique and drill in this book assumes a screen and a keyboard.

**Fix (Ch9):** replace "very likely stale text" and the *L1 alert* "translated pages lag"
inference with: "britishcouncil.tn is internally inconsistent in **both** languages — an
English page still quotes a paper-based fee. Do not resolve this from the website; phone
the centre."

---

### [MAJOR] — Chapter 3 states three different answers for whether Matching Headings runs in passage order
**Chapter:** 03, *The order table* vs *Tips & tricks* #4 vs *60-second summary*
**The book says (order table, row 5):** "| 5 | Matching headings | **Questions yes; the
heading numerals no** |"
**The book says (Tip 4):** "It **fails** on types 4, 5, 6, 9 and 10 — applying it there
makes you abandon correct answers."
**The book says (60-second summary):** "Not ordered — matching information, matching
features, **matching headings**, summary/note/table/flow-chart completion, diagram
labelling."
**What I found:** these cannot all be true, and the reader is left without an operating
rule for a type that ielts.org says "will be the first set of questions in the section".
This is an internal contradiction, not an external factual error — no Tier 1 source
resolves the underlying ambiguity, which is exactly why the chapter must pick one line and
hold it. (I could not find any official statement that the *questions* jump around; the
British Council note "NB The answers are NOT in the same order as the text" is the only
official wording, and it is genuinely ambiguous.)
**Source:** https://ielts.org/take-a-test/test-types/ielts-academic-test/ielts-academic-format-reading
— fetched 2026-07-31 (confirms Matching Headings is one of the 11 types and that more
headings than paragraphs are given; says nothing about question order).
**Fix:** make all three passages say the same thing, using the table's more careful reading:

- Order table row 5: keep as is.
- Tip 4: "It **fails** on types 4, 6, 9 and 10. On type 5 the *questions* still run in
  paragraph order, but the heading numerals do not — so work the paragraphs in sequence and
  never expect heading (i) to belong to paragraph A."
- 60-second summary: "Not ordered — matching information, matching features,
  summary/note/table/flow-chart completion, diagram labelling. Matching headings is the odd
  one: work the paragraphs in order, but the numerals are scrambled."

---

### [MAJOR] — The five-accent list is correct, but the corroborating citation does not corroborate it
**Chapter:** 02, *What the test actually asks*
**The book says:** "**Five national accents:** Australia, Canada, New Zealand, the UK, the
USA `[src: T1 ielts.org — Teacher's guide to IELTS p.26; corroborated at T1 ielts.org —
Listening test format, T1 cambridgeenglish.org — FAQs p.4, T1 ielts.idp.com — 9 myths]`."
**What I found:** the substance is right — the *IELTS Guide for teachers* says "It also
incorporates a mix of native speaker accents from **Australia, Canada, New Zealand, the UK
and US** in the Listening section." But **neither** of the two named corroborating sources
lists five, and both are non-exhaustive:
- ielts.org Listening format page: "Different accents, **including** British, Australian,
  New Zealand and North American, are used." (four, "including")
- Cambridge FAQs p.4: "You will hear a range of English native-speaker accents on the
  recordings (**for example**, Australian, British, New Zealand and North American
  speakers)." (four, "for example")

So a reader checking the citation finds it does not say what the book says it says. Worth
noting too that the Guide for teachers PDF is dated 2019 and reproduces the **superseded
2013 band descriptors** — it is safe for the accent and scoring facts the book takes from
it, but it must never be cited for descriptor wording.
**Source:** https://takeielts.britishcouncil.org/sites/default/files/ielts_guide_for_teachers.pdf
(p.5, "International English"; PDF CreationDate 2019-08-19);
https://ielts.org/take-a-test/test-types/ielts-academic-test/ielts-academic-format-listening;
https://www.cambridgeenglish.org/images/269898-ielts-academic-faqs.pdf p.4 — all fetched
2026-07-31.
**Fix:**

> **Five national accents:** Australia, Canada, New Zealand, the UK and the US — "a mix of
> native speaker accents from Australia, Canada, New Zealand, the UK and US in the
> Listening section" `[src: T1 takeielts.britishcouncil.org — IELTS Guide for teachers
> (PDF), p.5]`. The front-line format pages name only four and leave the list open —
> "Different accents, *including* British, Australian, New Zealand and North American"
> `[src: T1 ielts.org — Listening test format]` — so treat five as the working number and
> the list as non-exhaustive.

---

### [MAJOR] — "ONE WORD ONLY" is unverified in Listening but verbatim official in Reading; the book never says so
**Chapter:** 02, *Answer-rule reference* → *On `ONE WORD ONLY`* vs 03, Type 8
**The book says (Ch2):** "Research for this book could **not verify it verbatim in any
official IELTS Listening document** … Treat it as plausible but unconfirmed, and confirm at
ielts.org before your test date if it matters to you."
**The book says (Ch3, Type 8):** "**Appearance.** *'Complete the sentences below. Choose ONE
WORD ONLY from the passage for each answer.'*" — presented as the standard rubric, with no
hedge, and used again in the mini-example.
**What I found:** both are right, for different papers, and the book never reconciles them.
I checked the primary documents:
- *Listening sample tasks 2023* uses only `NO MORE THAN THREE WORDS AND/OR A NUMBER` and
  `NO MORE THAN TWO WORDS`. "ONE WORD ONLY" does **not** appear. **Chapter 2's hedge is
  correct and I could not break it.**
- *Academic Reading sample tasks 2023* contains "**Choose ONE WORD ONLY from the passage for
  each answer**" twice (Sentence Completion and Summary Completion). So Chapter 3 is right
  too.

As written, a reader who reads Chapter 2 first will distrust Chapter 3's rubric.
**Source:** https://ielts.org/cdn/ielts-sample-tests/ielts-listening-sample-tasks-2023.pdf
and https://ielts.org/cdn/Sample-tests/ielts-academic-reading-sample-tasks-2023.pdf — both
fetched 2026-07-31.
**Fix (Ch2):**

> **On `ONE WORD ONLY`.** It is verbatim official — but in **Reading**, not Listening. The
> 2023 Academic Reading sample tasks print "Choose ONE WORD ONLY from the passage for each
> answer" `[src: T1 ielts.org — Academic Reading sample tasks 2023]`, while the 2023
> Listening sample tasks use only `NO MORE THAN THREE WORDS AND/OR A NUMBER` and `NO MORE
> THAN TWO WORDS`. So expect it in Reading; do not assume it in Listening. Either way the
> behaviour is the same: **read the instruction printed above every task, every time, and
> obey exactly that.**

---

## MINOR

### [MINOR] — Arithmetic slip in the L1 gap figure
**Chapter:** 01, *L1 alert*
**The book says:** "Writing is the weakest skill for both of your languages, by a wide
margin — 0.56 below Reading for Arabic L1, **0.86 below for French L1**."
**What I found:** from the official spreadsheet, French L1 Academic Reading = 7.006159174
and Writing = 6.152479737. The gap is **0.854**, i.e. 0.85, not 0.86. (The Arabic figure
checks out: 6.099948584 − 5.539552146 = 0.560.) Every other number in the L1 table is exact:
Arabic 5.70/6.10/5.54/6.22/5.95 and French 6.95/7.01/6.15/6.65/6.75 all match the source to
two decimals, and the global means 6.45 Listening / 6.32 Academic Reading are confirmed.
**Source:** https://ielts.org/cdn/ielts-downloadable-assets/ielts-research/ielts-research-data/ielts-test-taker-performance-data-2024-2025.xlsx,
sheet "AC mean by first languages"; https://ielts.org/researchers/our-research/test-statistics
— both fetched 2026-07-31. (Note: the URL in the sources ledger,
`ielts.org/cdn/ielts-research-data/…`, now 404s; the working path is the one above.)
**Fix:** "0.56 below Reading for Arabic L1, **0.85** below for French L1."

---

### [MINOR] — "The band-5 TA descriptor explicitly describes an overview-less script"
**Chapter:** 04, *Myths that hold you back* → "A missing overview means you cannot get band 7."
**The book says:** "Note also that the **band-5 TA descriptor explicitly describes an
overview-less script**, so the common claim that no overview means below band 5 is simply
wrong."
**What I found:** the band-5 Task 1 Task Achievement cell does **not** mention an overview
at all. It reads: "The response generally addresses the requirements of the task. The format
may be inappropriate in places. (Academic) Key features which are selected are not
adequately covered. The recounting of detail is mainly mechanical. **There may be no data to
support the description.**" (that last clause is the only bolded, rating-limiting item in
the row). Band 6 is where the overview appears — "A relevant overview is attempted." The
book's *conclusion* is sound (silence at band 5 + a requirement at band 6 ⇒ no overview caps
TA at 5, it does not push you below 5), but "explicitly describes" is not true of a cell
that is silent.
**Source:** https://ielts.org/cdn/ielts-guides/ielts-writing-band-descriptors.pdf, p.4
(Task 1 bands 6–4) — fetched 2026-07-31, PDF CreationDate 2023-05-03.
**Fix:** "Note also that the **band-5 TA descriptor does not mention an overview at all** —
the overview requirement first appears at band 6, as something to be *attempted*. So a
missing overview caps TA at 5; it does not put you below 5, and the common claim that it
does is simply wrong."

---

### [MINOR] — "Academic items are pitched at bands 5–8" drops the qualifier
**Chapter:** 03, *Band descriptor decoder*
**The book says:** "One honest constraint: Academic items are *'pitched at bands 5–8'*
`[src: britishcouncil — Guide for teachers, p.4]`, so 30/40 means converting some genuinely
hard items."
**What I found:** the actual sentence is "The Academic Reading section has **more items**
pitched at bands 5–8, whereas the General Training has more items pitched at bands 3–6."
"More items" is a distribution claim, not a floor — the book's phrasing implies every
Academic item sits at 5–8.
**Source:** https://takeielts.britishcouncil.org/sites/default/files/ielts_guide_for_teachers.pdf,
p.4 — fetched 2026-07-31.
**Fix:** "One honest constraint: the Academic Reading paper has *'more items pitched at bands
5–8'* than General Training does, so 30/40 means converting some genuinely hard items."

---

### [MINOR] — The pen-or-pencil "genuine unresolved conflict" is largely reconcilable, and moot for this reader
**Chapter:** 09, *What you may take into the room* and *Myths*
**The book says:** "This conflict is unresolved, and I could not settle it from the British
Council registration terms and conditions" / "This is a genuine unresolved conflict between
two official sources."
**What I found:** the two statements are scoped differently and mostly compatible. The
British Council rule is about *bringing your own*, and is explicitly scoped to paper
delivery: "**You must use a black ink pen, supplied by the test centre, to complete your
IELTS on Paper test.** Personal stationery, including pencils, are not permitted in the test
room." Cambridge's "You can write in pen or pencil" answers a different question — which
implement is acceptable — and its Listening advice elsewhere says answers are transferred
"in pencil", which is also paper-only. For a computer-delivered candidate the whole question
is moot: the centre supplies pen and paper for notes.
**Source:** https://takeielts.britishcouncil.org/take-ielts/test-day-advice and
https://www.cambridgeenglish.org/images/269898-ielts-academic-faqs.pdf p.7 — both fetched
2026-07-31.
**Fix:** downgrade from "genuine unresolved conflict" to: "The British Council bans personal
stationery and says the centre supplies a black ink pen **for the paper test**; Cambridge's
FAQ says you may write in pen or pencil. The two are answering different questions, and
neither applies to you: on computer the centre supplies pen and paper for notes. **Bring
nothing.**"

---

### [MINOR] — Cambridge's own Writing "Don't" list contains a bald under-length instruction the book does not quote
**Chapter:** 01 *Myths* and 05 *Length: a floor, and no ceiling*
**The book says:** the under-length position rests on ielts.org ("you will be penalised if
your answer is too short") versus Cambridge ("There is no direct penalty for writing fewer
than 150 words…"), resolved through Task Response.
**What I found:** the same Cambridge FAQ that supplies the "no direct penalty" line also
lists, under Writing → Don't: "**Don't write less than the required number of words.**"
Quoting only the softer half makes Cambridge look more permissive than it is. The book's
*ruling* is still the right one — see *Claims verified clean* — but the audit brief asked me
to rule on the conflict, and the honest version is that Cambridge is internally two-handed.
**Source:** https://www.cambridgeenglish.org/images/269898-ielts-academic-faqs.pdf, pp.6–8 —
fetched 2026-07-31.
**Fix:** add one sentence to both passages: "Cambridge is two-handed about it: the same FAQ
that says there is no direct penalty also instructs 'Don't write less than the required
number of words.' Neither statement is a tariff, and neither contradicts the mechanism
below."

---

### [MINOR] — Chapter 4's Task 1 timing quote is looser than the official wording
**Chapter:** 01, *Writing — 60 minutes, 2 tasks*
**The book says:** "Task 1 asks for **at least 150 words in about 20 minutes**, Task 2 for
**at least 250 words in about 40 minutes**."
**What I found:** the official rubric is prescriptive, not approximate: "You should spend no
more than 20 minutes on this task" (Task 1) and "You should spend no more than 40 minutes on
this task" (Task 2). Chapter 4 gets this right ("no more than 20 minutes"); Chapter 1 softens
it to "about", then two sentences later says "The 20/40 split is guidance, not an enforced
boundary" — which is true of enforcement but not of the printed instruction.
**Source:** https://ielts.org/take-a-test/test-types/ielts-academic-test/ielts-academic-format-writing
— fetched 2026-07-31.
**Fix:** "Task 1 asks for **at least 150 words** and instructs you to spend **no more than
20 minutes**; Task 2 for **at least 250 words** in **no more than 40 minutes**. The
instruction is printed on the paper but not enforced by the software: the computer gives you
60 minutes for both and lets you move between tasks freely."

---

### [MINOR] — The Phase 2 video-call research is a 99-candidate preliminary study, presented as settled
**Chapter:** 06, *What the test actually asks* and *60-second summary*
**The book says:** "the partners' own research found scores essentially equivalent, the
difference 'negligibly small', with **80% of examiners** judging the modes to give equal
opportunity … under video-conferencing **63.3%** of candidates asked for clarification in
Part 1, against **26.7%** face-to-face."
**What I found:** **all three figures are verbatim correct** — "Significantly more
test-takers asked questions to clarify what the examiner said in the video-conferencing mode
(63.3%) than in the face-to-face mode (26.7%)" and "The majority of them (80%) reporting that
the two modes gave test-takers equal opportunity to demonstrate their level of English
proficiency". What is missing is scale: Phase 2 was 99 test-takers in Shanghai in May 2015,
and the Phase 1 report describes itself as "A preliminary comparison of test-taker and
examiner behaviour". The book presents it as if it settles the question.
**Source:** https://www.ielts.org/researchers/our-research/research-reports/exploring-performance-across-two-delivery-modes-for-the-ielts-speaking-test-face-to-face-and-video-conferencing-delivery-phase-2
and https://cdn.ielts.org/Research/exploring-performance-across-two-delivery-modes-for-same-l2-speaking-test-nakatsuhara-et-al-2016.pdf
— both fetched 2026-07-31.
**Fix:** add the scale in-line: "…the partners' own research — 99 test-takers in Shanghai,
2015, each sitting both modes — found the score difference 'negligibly small', with 80% of
examiners judging the modes to give equal opportunity."

---

### [MINOR] — Cambridge IELTS 21's publication date remains unverified from the publisher
**Chapter:** 09, *What to practise on*
**The book says:** "IELTS 21 appears to be the current Academic volume, published July 2026
— I take that date from search listings rather than the publisher's page, which blocks
automated requests, so verify it at the bookshop."
**What I found:** I hit the same wall. cambridge.org returns **HTTP 403** to automated
requests. Search listings agree that *IELTS 21 Practice Tests Academic Student's Book with
Answers with Digital Pack* exists (ISBN 9781009826723, listed at 146 pages) and place it in
2026, but I could not read the publisher's own page. **The book's hedge is correct and
should stay exactly as written.** Recording it here so the Editor does not "tidy it up" into
a bare assertion.
**Source:** https://www.cambridge.org/cambridgeenglish/catalog/cambridge-english-exams-ielts/ielts-21-practice-tests/ielts-21-practice-tests-academic-students-book-answers-digital-pack
— HTTP 403, 2026-07-31.
**Fix:** none. Keep the hedge.

---

### [MINOR] — Broken source URL in the performance-data citation
**Chapter:** 01, 04, 05, 09 (all cite "ielts.org — Test taker performance data 2024-2025 (XLSX)")
**The book says:** the chapters cite the file by name; `research/sources-ledger.md` records
the path.
**What I found:** the widely indexed URL
`https://ielts.org/cdn/ielts-research-data/ielts-test-taker-performance-data-2024-2025.xlsx`
now returns **404**. The live path is
`https://ielts.org/cdn/ielts-downloadable-assets/ielts-research/ielts-research-data/ielts-test-taker-performance-data-2024-2025.xlsx`,
reachable from https://ielts.org/researchers/our-research/test-statistics. The data itself is
unchanged and matches the book.
**Source:** both URLs tested 2026-07-31.
**Fix:** update the ledger to the working path, and prefer citing the parent page
(`ielts.org — Test statistics`) since CDN paths on this site move.

---

## Claims verified clean

Everything below was tested against a live Tier 1 source today and **survived**. Four are
marked ⭐ — these are the ones I most expected to break, and could not.

**Format, timing and counts**
- Total IELTS Academic duration "2 hours and 45 minutes"; Listening "Approximately 30
  minutes"; Reading "60 minutes (including transfer time)"; Writing "60 minutes"; Speaking
  "11–14 minutes". *(ielts.org — IELTS Academic test format and sections)*
- Speaking Part 1 "4–5 minutes", Part 2 "3–4 minutes, including the preparation time",
  Part 3 "4–5 minutes"; "a face-to-face interview between the test taker and an examiner";
  "The Speaking test is recorded"; one minute to prepare with pencil and paper.
  *(ielts.org — Academic Speaking test format)*
- Reading: 3 passages, 40 questions, total text length **2,150–2,750 words**; "Unlike the
  Listening test, no extra transfer time is given"; **11** listed question types; "You must
  be careful not to use any information you already know about the topic of the text".
  *(ielts.org — Academic Reading test format)*
- The 11-vs-14 question-type split: the 2023 Academic Reading sample-tasks PDF does name
  14 by splitting summary / note / table / flow-chart apart. Both numbers are official, as
  the book says. *(ielts.org — Academic Reading sample tasks 2023, p.1)*
- Reading pacing: "You have 60 minutes to read three texts and answer 40 questions. You
  should spend about 20 minutes on each text." *(Cambridge FAQs p.5)*
- Listening: 4 parts, 40 questions, 1 mark each; recording heard "ONCE only"; questions in
  the same order as the recording "for all question types"; the unannounced Part 4
  mid-recording pause "to allow you time to refocus", with all Part 4 reading time given at
  the start; the spoken situational introduction "is not written on the question paper".
  *(Cambridge FAQs pp.2–3)*
- British Council's "up to four people" in Listening Part 3, against ielts.org's "two main
  speakers" — the conflict the book flags is real and both sources still say it.
  *(takeielts.britishcouncil.org — IELTS test format explained; ielts.org — Listening test
  format)*

**⭐ Listening transfer time — the book handles the conflict correctly**
- ielts.org's Listening format page **still** reads "Approximately 30 minutes (plus 10
  minutes to transfer your answers to an answer sheet)" with **no computer caveat**, exactly
  as the book warns. *(ielts.org — Academic Listening test format)*
- The computer position is confirmed operationally: "no extra time" is given to transfer,
  and you get **2 minutes** at the end to review. *(ielts.idp.com — How computer-delivered
  IELTS works)*
- The British Council test-day page likewise gives the 10 minutes under the paper heading
  only. The book's instruction to ignore the ielts.org figure is correct.

**⭐ Raw-score anchors and rounding — exact**
- Listening 5 = 16, 6 = 23, 7 = 30, 8 = 35; Academic Reading 5 = **15**, 6 = 23, 7 = 30,
  8 = 35. The band-5 asymmetry the book highlights is real. Confirmed independently in two
  places. *(ielts.org — IELTS scoring in detail; IELTS Guide for teachers p.10)*
- The version caveat, verbatim: "The precise number of marks needed to achieve these band
  scores will vary slightly from test version to test version" and "the Band 6 boundary may
  be set at a slightly different raw score across individual tests."
- Rounding: ".25 … rounded up to the next half band … .75 … rounded up to the next whole
  band."
- All three worked examples reproduce exactly, on **both** sources: A 6.5/6.5/5.0/7.0 →
  6.25 → 6.5; B 4.0/3.5/4.0/4.0 → 3.875 → 4.0; C 6.5/6.5/5.5/6.0 → 6.125 → 6.0. The book's
  "identical examples on both, which is a strong cross-check" is accurate.
- Chapter 1's derived band maths all check out: 6.75 average → 7.0; 27.0/28.0; route rows
  A–E and the near-miss row (26.5 → 6.625 → 6.5) are all arithmetically correct; "Task 2
  alone is about 17% of your entire result" (⅔ × ¼ = 16.7%) is right.
- Chapter 3's Reading conversion table matches IDP's published table row for row.

**⭐ The Writing band formula — the "labelled estimate" call is correct**
- Both official statements are live and verbatim: "Task 2 contributes twice as much as Task
  1 to the Writing score" *(ielts.org — Writing test format; Cambridge FAQs p.8)* and "Task
  1 is worth a third of your overall mark for Writing. Task 2 is worth two thirds."
  *(ielts.org — Writing test resources)*
- I searched ielts.org, the British Council, IDP, the descriptors PDF and the key assessment
  criteria PDF: **no official source states the arithmetic for combining the two task scores,
  and none states how the Writing sub-score is rounded.** The book's decision to print
  `(T1 + 2×T2) ÷ 3` as a labelled planning estimate — never as IELTS's method — is the right
  call and should not be changed.

**⭐ Under-length — the ruling is defensible**
- ielts.org: "will be penalised if your answer is too short" — confirmed live on the Writing
  format page, for both tasks.
- Cambridge: "There is no direct penalty for writing fewer than 150 words for the Task 1
  question and 250 words for the Task 2 question. However, writing fewer words may impact on
  the range of ideas and evidence produced and may therefore affect your score." — confirmed
  verbatim (p.8). *(Both are current and both are Tier 1; see the MINOR note above about
  Cambridge's own "Don't write less than the required number of words".)*
- "Responses of 20 words or fewer are rated at Band 1." — confirmed, present in **all four
  criteria columns**, on both the Task 1 and the Task 2 grid.
- "Any copied rubric must be discounted." — confirmed, band 1 Task Response, both grids.
- The key assessment criteria define the task as fulfilled "using a minimum of 150 words" /
  "using a minimum of 250 words", exactly as the book argues — so the count sits inside the
  definition of TA/TR.
- **Verdict: the book is right.** There is no published tariff, the two sources differ in
  emphasis rather than substance, and marking it through Task Response is the only position
  the documents support. Printing no number is correct.
  *(ielts.org — Writing test format; Cambridge FAQs p.8; ielts.org — Writing band
  descriptors PDF; ielts.org — Writing key assessment criteria PDF)*

**⭐ Chapter 5's bold-extraction claim — I tried hard to break this and could not**
- The legend is real: "A script must fully fit the positive features of the descriptor at a
  particular level. **Bolded text indicates negative features that will limit a rating.**"
- I re-extracted the bold runs from the PDF independently (font/XML positions, not the
  book's method). On the Task 2 grid: page 7 carries bands 9/8/7 and contains **zero** bolded
  negative features; page 8 carries bands 6/5/4 and its only two bolds — "incompletely
  addressed." and "Paragraphing may be inadequate or missing." — both sit inside the **band
  5** row (band labels are vertically centred; the band-6 row ends above them). Page 9
  (bands 4–0) is dense with them.
- **Chapter 5's claim "There is not one bolded negative feature at bands 6, 7, 8 or 9" is
  confirmed.** This is the strongest piece of original analysis in the book and it holds.
  *(ielts.org — Writing band descriptors PDF, pp.7–9)*

**Writing descriptors (May 2023 edition)**
- PDF metadata: Title "IELTS Writing Band Descriptors", Author "IELTS", **CreationDate
  2023-05-03**, 9 pages. The book's edition claim and page references are correct.
- Band 7 Task 1 TA: "(Academic) It presents a clear overview, **the data are appropriately
  categorised**, and main trends or differences are identified." — the spine of Chapter 4,
  confirmed verbatim.
- Band 6 Task 1 TA: "A relevant overview is attempted."
- Band 7 CC: reference and substitution "used flexibly"; band 6 CC: "cohesion within and/or
  between sentences may be faulty or mechanical due to misuse, overuse or omission" and
  reference/substitution "may lack flexibility or clarity and result in some repetition or
  error".
- Band 7 LR: "An awareness of style and collocation is evident"; band 6 LR: "If the writer
  is a risk-taker, there will be a wider range of vocabulary used but higher degrees of
  inaccuracy or inappropriacy" — the book's "risk-taker clause" reading is exact.
- Band 7 GRA: "error-free sentences are frequent"; band 6 GRA: "Examples of more complex
  structures are not marked by the same level of accuracy as in simple structures."
- Band 7 Task 2 TR: "A clear and developed position is presented." — and *throughout* is
  indeed absent, as Chapter 5 claims.
- Bullet points / note form: "not written as full, connected text (e.g. using bullet points
  in any part of the response, or note form, is not appropriate)"; plagiarism named.
  *(ielts.org — Writing key assessment criteria PDF)*

**Speaking descriptors (2025 edition)**
- PDF metadata: Title "IELTS Speaking Band Descriptors", **CreationDate 2025-09-16** — the
  book's "2025" is right, and its warning that the 2008/2013 Cambridge public version is
  obsolete is well founded.
- Notes verbatim: "(i) A candidate must fully fit the positive features of the descriptor at
  a particular level. (ii) A candidate will be rated on their average performance across all
  parts of the test." — both used correctly in Chapter 6.
- Band 7 F&C: "Some hesitation, repetition and/or self-correction may occur, **often
  mid-sentence** and indicate problems with accessing appropriate language. However, these
  will not affect coherence." — Chapter 6's headline myth-bust is exactly right.
- Band 7 GRA: "Error-free sentences are frequent… **A few basic errors persist.**"; band 8
  GRA: "A few basic errors may persist." — the book's counter-intuitive advice to stop
  hunting basic slips is descriptor-accurate.
- Band 7 Pronunciation: "Displays all the positive features of band 6, and some, but not
  all, of the positive features of band 8." Band 5 has the same construction against bands
  4/6 — so Chapter 6's "bands 5 and 7 have no positive features of their own" is correct.
- Band 6 Pronunciation: "Chunking is generally appropriate, but rhythm may be affected by a
  lack of stress-timing and/or a rapid speech rate." Band 8: "Can sustain appropriate
  rhythm"; "Accent has minimal effect on intelligibility". Accent appears **only** at bands
  8 and 9 — confirmed by full-text search.

**Listening and Reading answer rules**
- Two answers in one gap: "Don't write more than one answer when only one is required. **Even
  if one of your answers is correct, you will not receive a mark.**" — appears under **both**
  Listening and Reading. *(Cambridge FAQs pp.3, 5)*
- Over the word limit: "Answers which are over the word limit will be marked as incorrect."
  *(Cambridge FAQs pp.4, 5)*
- American spellings: "**Both UK and US spellings are accepted.**" *(Cambridge FAQs p.4)* —
  and the official Listening answer key does print `0.75 m/metre(s)/meter(s)`, exactly as
  Chapter 2 claims. *(ielts.org — Listening sample tasks 2023, answer key)*
- Hyphenated words: "**Hyphenated words such as 'check-in' count as single words.**"
  *(ielts.org — Academic Listening test format; Academic test format in detail)*
- Contractions: "Contracted words such as 'they're' will not be tested." *(same)*
- Capitals: "Your answers may be written in either capital letters or lower case."
  *(takeielts.britishcouncil.org — Test day advice)*
- No negative marking, verbatim: "**Try to answer all questions; you will not lose points for
  incorrect answers**" (Listening) and "Try to answer all questions; if an answer is
  incorrect, there will not be a penalty, so give it a go" (Reading). *(same page)*
- Spelling is marked: "You will lose marks for incorrect spelling and grammar."
  *(Cambridge FAQs p.4)*
- Memorised essays: "Don't waste your time learning essays by heart to use in the exam. You
  will be penalised for this"; and "Don't simply copy words and phrases from the question
  paper". *(Cambridge FAQs pp.7–8)*
- Task-2-first timing advice: "Finish Writing Task 1 after about 20 minutes to allow enough
  time to answer Writing Task 2. Remember Task 2 contributes twice as much as Task 1"
  *(Cambridge FAQs p.6)* — and, supporting Chapter 5's "open question" framing, the same FAQ
  says "It is your choice how you divide this time."

**Computer-delivered interface (Chapter 9)**
- Timer top-centre, flashing "in the last 10 minutes and 5 minutes"; word count "in the
  lower-left corner"; volume "in the upper right corner"; Review button changes "the question
  number… from a square to a circle". All four confirmed verbatim.
  *(ielts.idp.com — How computer-delivered IELTS works)*
- Highlighting is invisible to markers and does not affect the score; CTRL+F is unavailable;
  copy-paste works in Reading and Writing — consistent with the official pages cited.

**Policy, results and Tunisia**
- Fees at British Council Tunis, live listing: IELTS Academic **TND 750**, General Training
  TND 750, UKVI Academic/GT **TND 820**, Life Skills A1/B1 **TND 640**. Every figure in
  Chapter 9's table is exact. *(ielts.org — Test centre: British Council Tunis)*
- Five Tunisian locations — Tunis, Bizerte, Sousse, Sfax, Gabes. *(britishcouncil.tn)*
- ID: "You must bring the passport/national identity card you used on the IELTS Application
  Form to the test." *(takeielts.britishcouncil.org — FAQs)*
- "There is no limit on sitting the test"; "Test Report Form (TRF) is valid for two years."
  *(same)*
- Speaking window conflict is real and current: the test-format page says "either on the same
  day or seven days before or after"; the FAQ says "either on the same day or seven days
  before or **two days after**". Both confirmed today — the book is right to flag it and to
  tell the reader to trust the booking confirmation.
- Watches: "Personal watches are not allowed in the test room." Water: "with the exception of
  water in a transparent bottle." Food banned. Toilet before entry. All confirmed.
- Test day session: "2 hours 40 minutes, and there are no breaks between each section of the
  test." *(ielts.org — What to expect on test day)* — see the MAJOR note on how the book
  reconciles this with 2h45.
- Results: "**About half are ready within only 1 day**" and "Globally 80% of IELTS scores are
  available within 2 days" (based on global test data, May–June 2024); "IELTS on Computer:
  results usually within 1-2 days"; "IELTS Online: results usually within 6-8 days". Chapter
  1 and Chapter 9's figures are exact, and the advice to plan against five days is prudent.
  *(ielts.org — Fast IELTS results)*
- Enquiry on Results: "up to six weeks after your test date"; fee "fully refunded if your
  band score changes"; "Your result can become available on the same day as your application
  and up to 21 days after your application." All confirmed. **On whether a re-mark can lower
  a band: ielts.org and the British Council say nothing either way; only IDP states it "either
  stays the same or is higher".** Chapter 9's refusal to treat that as verified is correct and
  should stand. *(ielts.org — Cancellations, refunds, remarks and transfers)*
- Test-date transfer: "You must select a new test date, where available, within three months
  of your original test date"; beyond that "your transfer will be treated as a cancellation";
  "You can only transfer the same booking once" (the book omits the once-only rule — worth
  adding). *(same)*
- One Skill Retake: "You must sit the One Skill Retake within 60 days from your original test
  date"; "You can only complete the One Skill Retake once per full IELTS test"; computer only;
  selected centres; institutional acceptance is not universal. Chapter 1's and Chapter 9's
  statements of the rules are accurate, and the refusal to build a plan on Tunisian
  availability is correct — no Tunisian centre is named anywhere.
  *(takeielts.britishcouncil.org — One Skill Retake FAQs)*
- IELTS Online: "not currently accepted for immigration purposes"; headphones "not permitted";
  passport is the only acceptable ID; results 6–8 days. All four confirmed — Chapter 9's
  opening recommendation is soundly built. *(ielts.org — IELTS Online;
  takeielts.britishcouncil.org — Your IELTS Online FAQs Answered)*
- Paper retirement: "from mid-2026, we will no longer offer IELTS as a paper-based test. All
  IELTS tests will be delivered on computer"; "this update does not change the IELTS skills
  assessed, the test construct, or the way results should be interpreted"; "In selected
  markets, we will introduce 'Writing on Paper'" — with **no market named**, exactly as the
  book says. *(ielts.org — Updates to IELTS test delivery)*

**Performance data**
- Every figure in Chapter 1's L1 table, and the Writing means quoted in Chapters 4, 5 and 9,
  match the official spreadsheet to the stated precision (Arabic Writing 5.539552 → 5.54 /
  5.540; French Writing 6.152480 → 6.15 / 6.152). Global means 6.45 Listening and 6.32
  Academic Reading confirmed on the Test Statistics page. Only the 0.86/0.85 gap figure is
  wrong (MINOR above).

**No invented statistics found.** Every number I could trace, I traced. Chapter 3's Myth 14
("Cambridge item analysis shows X% of band-6 candidates fail NG questions… No such published
dataset was found") and Myth 2 ("No official data supports this… this book will not invent
one") are exactly the right posture, and I found nothing in the book that violates it. The
Roothooft & Breeze figures in `CLAUDE.md` are outside this audit's scope (they are not in the
nine chapters).

---

## Priority for the Editor

1. **The half-band table** (3 CRITICAL items, Chapters 1, 2 and 3). One factual correction
   fixes an internal contradiction, removes a false "nothing else is published" claim, and
   gives the reader the 6.5 target Chapter 1 currently refuses to print. Highest value in the
   report.
2. **The three under-claimed sources** (Speaking help table, the Part 2 stop rule, the
   "limited to Band 5" sentence). All three are officially stated; the book calls them
   unverified. Cheap to fix, and each strengthens a chapter's central advice.
3. **The 2h40 reconciliation and the Tunisia paper-option reasoning.** Both are unsourced
   inference presented as fact, and both contradict another chapter.
4. **The Matching Headings order inconsistency** — three statements, one reader.
5. Everything else is polish.
