# R6 — Speaking deep dive

Research file for the IELTS Academic revision book. Reader: Tunisian Arabic L1,
fluent French, English L3, target band 7.0 (min 6.5/section), 6–10 weeks
self-study, computer-delivered assumed.

**Every factual claim below carries an inline source note.** Nothing here is
written from memory. Where a claim could not be confirmed against Tier 1 or two
independent Tier 2 sources it is tagged `[UNVERIFIED]`.

---

## ⚠️ HEADLINE FINDING — the prior work used a superseded descriptor

`knowledge/band-descriptors.md` and `knowledge/sources.md` were written from
`https://assets.cambridgeenglish.org/webinars/ielts-speaking-band-descriptors.pdf`.

That file's **PDF metadata reads: Author `borour`, Company `UCLES`, created
2008-09-29, last modified 2013-05-21, 1 page, titled "IELTS Speaking Band
Descriptors (public version)"**. It is a ~2008-vintage document.

The **current** Speaking descriptors live at
`https://ielts.org/cdn/ielts-guides/ielts-speaking-band-descriptors.pdf`
— **metadata: Author `IELTS`, created 2025-09-16, modified 2025-09-17, 4 pages,
titled "IELTS Speaking Band Descriptors"**, footer "Please visit IELTS.org for
updates". (Both PDFs downloaded and metadata read directly with pdfplumber,
2026-07-31.)

This is the same trap a sibling agent hit on the Writing descriptors. The two
Speaking versions are **not** cosmetic rewrites — the 2025 text changes what
band 6 and band 7 actually mean in Fluency & Coherence and in Pronunciation, in
ways that change the coaching advice. Deltas are itemised in the
[Band descriptor decoder](#band-descriptor-decoder) and summarised in
[MYTHS](#myths).

A British Council–hosted copy at
`takeielts.britishcouncil.org/sites/default/files/ielts_speaking_band_descriptors.pdf`
returns 403 to direct fetch, but its indexed title line reads "Speaking Band
Descriptors Please visit IELTS.org for updates" — the 2025 footer, not the 2008
"(public version)" heading. So the partners appear to distribute the current
version too. `[UNVERIFIED — inferred from search-index title only; verifier
should retrieve the file]`

There is also a **companion document** the prior work did not have at all:
`https://ielts.org/cdn/ielts-guides/ielts-speaking-key-assessment-criteria.pdf`
— **metadata: Author `IELTS`, Title "IELTS Speaking key assessment criteria",
created 2023-05-03, modified 2023-10-18, 4 pages** (downloaded and extracted
2026-07-31). It does not give bands; it gives the **key indicators** behind each
of the four criteria — i.e. the operational definition of what an examiner is
listening for. It is the most directly actionable Tier 1 document in this whole
research file, and it is decoded in
[What each criterion actually measures](#what-each-criterion-actually-measures).

### Exactly which band wordings changed (2008 → 2025)

| Criterion / band | 2008 public version | 2025 edition | Consequence |
|---|---|---|---|
| **FC 7** | hesitation "may" be language-related, at times | hesitation/repetition/self-correction occur, **often mid-sentence**, and **do** indicate difficulty accessing language — but must not affect coherence | Repo claim "band 7 hesitates about ideas, not words" is **wrong** (MYTHS M1). The 6→7 test is coherence survival, not hesitation type |
| **FC 6** | "may lose coherence at times due to occasional repetition, self-correction or hesitation" | "**Coherence may be lost at times** as a result of hesitation, repetition and/or self-correction" | Same substance, sharper. Confirms the 6/7 boundary sits on coherence |
| **FC 7 (markers)** | "uses a range of connectives and discourse markers with some flexibility" | "**Flexible** use of spoken discourse markers, connectives and cohesive features" | Band 6 now explicitly owns "uses a range… though not always appropriately"; band 7 owns flexibility |
| **GRA 7** | "uses a range of complex structures with some flexibility; frequently produces error-free sentences" | "A range of structures flexibly used. Error-free sentences are frequent. **Both simple and complex sentences are used effectively despite some errors. A few basic errors persist.**" | **New.** Basic errors are explicitly tolerated at 7 *and* 8. Changes the revision priority — stop hunting `-s` slips, make complex sentences land |
| **GRA 6** | "uses a mix of simple and complex structures, but with limited flexibility; may make frequent mistakes with complex structures" | "Produces a mix of **short and complex** sentence forms and a variety of structures with limited flexibility. Though errors frequently occur in complex structures, these rarely impede communication" | Minor |
| **LR 6** | "has a wide enough vocabulary to discuss topics at length" | "Resource sufficient to discuss topics at length. **Vocabulary use may be inappropriate but meaning is clear**" | Minor |
| **Pron 6** | range of features with mixed control; some effective use not sustained; mispronunciation reduces clarity at times | all of that **plus**: "**Chunking** is generally appropriate, but rhythm may be affected by **a lack of stress-timing and/or a rapid speech rate**"; "Can generally be understood throughout **without much effort**" | **The biggest change, and the one that matters most to this reader.** The 2025 text publishes his exact pronunciation syllabus. None of it existed in the 2008 file |
| **Pron 8** | "sustains flexible use of features, with only occasional lapses"; "L1 accent has minimal effect" | "**Can sustain appropriate rhythm.** Flexible use of stress and intonation **across long utterances**"; "Accent has minimal effect" | Rhythm named as the band-8 feature → identifies the cheapest 6→7 purchase |
| **Pron 5 / 7** | defined by reference to neighbours | **still** defined by reference to neighbours | Prior work's claim **confirmed** |
| **Grid notes** | none | Note (i) must fully fit the positive features; Note (ii) "**rated on their average performance across all parts of the test**" | New. Note (ii) means one bad part does not sink you |

---

## Verified facts

### Structure and timing

| Fact | Source |
|---|---|
| Speaking is **11–14 minutes**, three parts | ielts.org Academic Speaking format page, fetched 2026-07-31; British Council `takeielts` test-format page, same date — Tier 1, two independent partners |
| **Part 1 — Introduction and interview, 4–5 minutes.** Examiner introduces themself and checks the candidate's ID, then asks general questions on familiar topics (home, family, work, studies, interests) | ielts.org Academic Speaking format page; British Council practice test Part 1 states "You should spend 4 - 5 minutes on this part of the test" — Tier 1 |
| **Part 2 — Long turn, 3–4 minutes in total, including 1 minute preparation.** Examiner hands a task card; candidate gets 1 minute to prepare and make notes, then speaks 1–2 minutes, then answers one or two rounding-off questions | ielts.org Academic Speaking format page; British Council practice test Part 2 — Tier 1 |
| **Part 3 — Two-way discussion, 4–5 minutes.** Questions connected to the Part 2 topic, treated more generally and abstractly | ielts.org Academic Speaking format page — Tier 1 |
| The test **is recorded** | British Council `takeielts` test-format page ("the test will be recorded"); IDP test-day page ("is recorded") — Tier 1 |
| Assessed on **four criteria**: fluency and coherence, lexical resource, grammatical range and accuracy, pronunciation | ielts.org Academic Speaking format page; the 2025 descriptor PDF is laid out in exactly these four columns — Tier 1 |
| The four Speaking criteria are **equally weighted** (each 25%) | IDP "Mastering IELTS Speaking: Enhancing Fluency and Coherence" states fluency and coherence "accounts for 25% of your total band score"; IDP "Seven mistakes" states pronunciation "comprises 25% of your speaking score" — Tier 1, two IDP pages. Also derivable: the descriptor grid gives four parallel columns with no weighting note |
| **You are rated on your average performance across the whole test, not part by part** | 2025 descriptor PDF, Note (ii) at the foot of the grid: *"A candidate will be rated on their average performance across all parts of the test."* — Tier 1 |
| **You must fully fit a band's positive features to be awarded it** | 2025 descriptor PDF, Note (i) — Tier 1. (Same governing rule already in `CLAUDE.md`.) |
| **There are nine bands and four criteria**, and each criterion has a published set of *key indicators* defining what is listened for | Official Speaking Key Assessment Criteria PDF (created 2023-05-03, modified 2023-10-18), downloaded and extracted 2026-07-31 — Tier 1. Decoded in full [below](#what-each-criterion-actually-measures) |

### Face-to-face vs video call — CONFLICT RESOLVED

The brief flagged that ielts.org/IDP say "face-to-face" while a British Council
booking page says "either face-to-face or via video call". Both are true; they
are describing different things.

- **ielts.org Academic Speaking format page** (fetched 2026-07-31): "The
  Speaking test is a face-to-face interview between the test taker and an
  examiner." — Tier 1.
- **British Council `takeielts` test-format page** (same date): the test "can be
  conducted face-to-face or via video call", and "the video call Speaking test
  will maintain the face-to-face feature of the in-person Speaking test." —
  Tier 1.
- **IDP's dedicated F2F-vs-VCS page** (`ielts.idp.com/thailand/prepare/speaking/ielts-speaking-format`,
  same date): both modes use certified examiners applying the same criteria;
  "Both formats are identical in terms of content, timing, scoring, and
  structure"; "The test is exactly the same in content, difficulty, and
  scoring." In VCS the candidate sits in a test-centre room with computer and
  headset, an invigilator sets up the technology, the Part 2 topic "will be
  displayed on the screen", and pen and paper are still provided for notes. The
  video call is recorded. — Tier 1.

**Resolution.** "Face-to-face" in IELTS copy means *a live human examiner in
real-time two-way interaction* — as opposed to a recorded or machine-marked
speaking test. It does **not** guarantee the examiner is in the room. Video Call
Speaking (VCS) is a real, current delivery mode at some centres. You do **not
choose** it — IDP: "the format depends on the test center you select." The
candidate should confirm with their centre at booking.

For **IELTS Online** specifically, the British Council FAQ states the Speaking
test "will take place with a trained examiner via video call", and usually
happens *before* Listening/Reading/Writing (Tier 1).

### Does video-call delivery change assessment? — evidence

The IELTS partners' own published research (`ielts.org` research reports,
"Exploring performance across two delivery modes… Phase 2", fetched 2026-07-31,
Tier 1) reports:

- Scores were **essentially equivalent** across modes under Many-Facet Rasch
  analysis; video-conferencing was marginally harder but "the actual score
  difference was negligibly small".
- **80%** of examiners judged the two modes to give equal opportunity to
  demonstrate proficiency.
- Sound quality was rated "Clear" or "Very clear" by most participants.
- Behavioural difference worth knowing: **far more candidates asked for
  clarification in Part 1 under video-conferencing (63.3%) than face-to-face
  (26.7%)**.
- 71.7% of test takers *preferred* face-to-face, yet slightly *more* reported
  anxiety in face-to-face (38.4%) than in video-conferencing (34.3%).

**Practical read for the book:** the criteria and the standard do not change.
What changes is that you will lose more of the exchange to audio degradation, so
(a) build the clarification phrases into your practice, and (b) treat crisp
articulation of final consonants as higher-value in VCS than in a quiet room.
The last sentence is my inference from the clarification-rate gap, not a
published finding — tag it `[UNVERIFIED]` if the book states it as fact.

### Speaking-test scheduling — CONFLICT RESOLVED (it is a genuine partner difference)

The brief flagged "7 days before or after" vs "7 days before or 2 days after".
**Both wordings are currently live on official sites. They belong to different
test partners.** All fetched 2026-07-31.

| Partner / mode | Official wording | Source |
|---|---|---|
| **British Council**, paper and computer | "Your Speaking test will be held either on the same day or seven days before or two days after that, depending on local arrangements." | `takeielts.britishcouncil.org/frequently-asked-questions` — Tier 1 |
| **British Council**, test-format page | Speaking is held "either on the same day or seven days before or after" the LRW tests, depending on local arrangements | `takeielts.britishcouncil.org/take-ielts/test-format` — Tier 1. **Note: this contradicts BC's own FAQ.** |
| **IDP**, paper-based | "up to 7 days before or after your test date" | `ielts.idp.com/about/test-day` — Tier 1 |
| **IDP**, computer-based | "on the same day, either before, or after the other three parts" | `ielts.idp.com/about/test-day` — Tier 1 |
| **British Council**, IELTS Online | Speaking is "usually … before your Listening, Reading and Writing. It could be on the same or a different day." | BC FAQ — Tier 1 |

**Resolution for the book.** There is no single global rule, and the two
partners' pages disagree with each other and, in BC's case, with themselves. The
only safe statements are:

1. **Computer-delivered (this reader's assumed mode): expect Speaking on the
   same day**, before or after the other three papers — both partners say so for
   CD-IELTS.
2. Paper-based can be up to a week either side, subject to local arrangements.
3. **Whatever the general rule, the binding fact is on your own booking
   confirmation. Check it, and plan the day around it.**

Do not print a bare "7 days before or 2 days after" — it is BC-specific and its
own sibling page contradicts it.

### The official Part 2 task card and examiner frame

From the official **IELTS Speaking Sample Tasks** PDF
(`ielts.org/cdn/ielts-sample-tests/ielts-speaking-sample-tasks-2023.pdf`; PDF
metadata: Author IELTS, created 2023-10-10, 7 pages; downloaded and extracted
2026-07-31 — Tier 1):

- The card carries the standing instruction that you will have to talk about the
  topic for **one to two minutes**, that you have **one minute to think** about
  what you are going to say, and that "**You can make some notes to help you if
  you wish**". Notes are explicitly **optional**.
- The examiner's spoken frame before you start: "*Remember you have one to two
  minutes for this, so don't worry if I stop you. I'll tell you when the time is
  up.*" Being stopped is announced in advance as normal, before you speak.
- British Council practice test Part 2 (Tier 1) confirms "A pencil and paper will
  be provided for you to make notes."
- The sample card's three bullets are all *concrete* (where you got it, how long
  you have had it, what you use it for) plus a final explain-clause. That is the
  standard shape.
- The sample rounding-off questions are short and closed-ish ("Is it valuable in
  terms of money?", "Would it be easy to replace?"). In the official transcript
  the examiner asks **only one** of them.

### Part 1 and Part 3 examiner frames — what the official transcript shows

Same PDF (Tier 1). This is unusually good evidence because it shows examiner
behaviour, not advice about it.

- **Part 1 is scripted in topic blocks.** The examiner says "Let's talk about
  your home town or village", asks four questions, then "Let's move on to talk
  about accommodation", and asks four more. So Part 1 ≈ **two to three topic
  frames of roughly four questions each**. In the transcript the examiner reads
  the questions essentially verbatim and adds nothing.
- **Part 3 is visibly improvised around a frame.** The frame lists three
  questions ("Let's consider first of all how people's values have changed…",
  "Finally, let's talk about the role of advertising"), but the transcript shows
  the examiner interjecting far beyond them: "Is that a new development?",
  "People have thought like that for quite a long time?", "What do you think of
  this way of thinking…?", "You don't think of it as a healthy way of thinking?",
  "And do you think this will change?", "Can you tell me a little bit more about
  that?"
- This is **direct Tier 1 evidence for the pushback pattern**: the examiner
  probes, re-frames your own claim back at you, and pushes for elaboration. It is
  not hostility and it is not a signal you are doing badly — it is how the part
  is designed to elicit ratable language.
- It also **explains** the differing clarification rules below: in Part 1 the
  examiner is reading a fixed script and has no licence to reword; in Part 3 they
  are already rewording as a matter of course.

### Clarification — what you may ask for, and where

Not stated on any Tier 1 page I could retrieve. Promoted on **three independent
Tier 2 sources** which agree on the substance, plus a descriptor-derived
argument.

| Part | Repetition? | Explanation / rephrasing? |
|---|---|---|
| **Part 1** | Yes | **No** — examiner may not explain, paraphrase, or define a word |
| **Part 2** | n/a (no examiner question during the long turn) | **No** — you must work with the card you were given |
| **Part 3** | Yes | **Yes** — examiner may rephrase the question and explain a word |

- IELTS Liz, "IELTS Speaking Tips: Asking the Examiner Questions" (Tier 2,
  fetched 2026-07-31): Part 1 repetition only ("Could you repeat that,
  please?"); Part 2 nothing; Part 3 repetition, explanation and word definitions
  ("Could you explain that, please?", "What does X mean?").
- IELTS Advantage, "Speaking: Asking the Examiner Questions" (Tier 2, via search
  index, 2026-07-31): you can ask for repetition and for **one word** to be
  explained, but not for a whole sentence to be explained; the examiner will not
  volunteer either unless you ask; do not use it on every question.
- Magoosh, "How to Ask for Clarification in IELTS Speaking" (Tier 2, fetched
  2026-07-31): repetition in Parts 1 and 3; rephrasing in Part 3; **not in
  Part 2**; do not ask twice for the same item.

**Descriptor-derived justification (this is the strong argument, and it is
Tier 1).** The 2025 grid rates exactly four things: fluency and coherence,
lexical resource, grammatical range and accuracy, pronunciation. **Listening
comprehension is not one of them.** So asking for a repeat cannot itself lose
you a mark. What *can* cost you is the second-order effect: the seconds spent,
and — if you guess instead of asking — an answer that misses the question, which
does bite through coherence.

Two live divergences to be honest about: Magoosh puts *rephrasing* in "parts 1
and 3" in one sentence and then restricts it to Part 3; IDP's Part 1 article
(Tier 1) lists both "Could you repeat that, please?" **and** "What does _____
mean?" as things a candidate can say, without naming a part. Logged as an
[open question](#open-questions-for-verifiers).

---

## Part 1 — Introduction and interview

### What is actually assessed

Not your life. The examiner is sampling **whether you can produce fluent,
accurate, appropriately-worded English about predictable everyday content**,
across a spread of tenses. ielts.org's own teacher-facing article
("Three parts of IELTS Speaking, and what to look out for", fetched 2026-07-31,
Tier 1) puts it as capacity to speak smoothly while showing a broad vocabulary
range, and advises: stick to what you know, be yourself, talk about day-to-day
activities, personal interests, home life.

IDP's Part 1 article (Tier 1, fetched 2026-07-31) adds what examiners are
listening for here specifically: a range of cohesive devices and linking
phrases; varied language for introducing personal experience; clear speech at an
appropriate pace with proper intonation and rhythm.

### Topic families

Officially confirmed: **home town or village, accommodation** (the two frames in
the official sample tasks PDF — Tier 1); **home, family, work, studies,
interests** (ielts.org format page — Tier 1); **yourself, what you do, where you
come from, your family, your country, your personal experiences, the activities
you do**, with worked examples on hometown, accommodation, friends, and food and
cooking (IDP Part 1 article — Tier 1).

Everything beyond that list circulating on prep sites (weather, colours,
handwriting, birthdays, mirrors, patience…) is Tier 3 aggregation of candidate
reports. Useful as practice stimulus, **not** printable as an official list.
`[UNVERIFIED]`

### Technique

**Answer + reason + detail. Two to six sentences.** IDP's "Seven mistakes"
article (Tier 1, fetched 2026-07-31) gives the concrete range: typically "two to
six sentences, depending on the question", and names bare yes/no answers as
mistake #4 because they don't showcase fluency or ability. IDP's Part 1 article
(Tier 1) frames the same target differently and better: *extend your response
before the examiner has to ask "why?"*.

**Vary the tense deliberately.** IDP (Tier 1) names tense-mismatch — answering a
present-tense question in the past, or vice versa — as a common Part 1 error.
Part 1 frames are built to sample tenses: "What kind of place is it?" (present),
"How long have you lived there?" (present perfect), "What sort of accommodation
would you *most like* to live in?" (conditional). All three appear in the
official sample frame. Hitting each cleanly is free Grammatical Range.

**Do not parrot the question.** IDP "Seven mistakes" #7 (Tier 1): repeating the
question back fails to demonstrate paraphrase — and paraphrase is named in the
Lexical Resource descriptor at bands 6, 7 and 8 (2025 PDF, Tier 1). "Do I enjoy
cooking? Well, I do enjoy cooking…" burns three seconds and shows nothing.

**Control the topic.** IDP (Tier 1) makes an unexpectedly sharp point: don't say
you both study *and* work, because the examiner expects you to control the choice
of topic. Pick the version of your life you have the best vocabulary for and
commit to it.

### Traps

- **Over-answering.** Part 1 has 4–5 minutes and ~8–12 questions to get through.
  IELTS Liz (Tier 2, "Why the IELTS Speaking Examiner Stops your Answer", fetched
  2026-07-31) explains examiners stop long or slow answers to manage time and to
  cover all the language functions they need to sample — and that being stopped
  **does not** lower your score. But an answer so long it forces the examiner to
  cut you off has cost you nothing *and gained you nothing*; you would have got
  the same rating from three sentences.
- **Memorised openers.** ielts.org's own "Don't overdo it" article (Tier 1,
  fetched 2026-07-31): "Examiners are highly trained to spot memorised answers,
  which never bodes well." IDP names memorisation as mistake #1 and specifically
  warns against it in Part 1, because Part 1 is where candidates most often
  deploy a rehearsed hometown paragraph.
- **Register collapse.** Part 1 is conversation. French-academic formality
  ("Concerning my domicile, it is situated…") is a *worse* fit here than plain
  speech, and Lexical Resource at band 7 explicitly requires awareness of style
  (2025 descriptor, Tier 1).

### Band-6 failure mode in Part 1

Two-clause answers that are grammatically fine and completely flat: *"Yes, I
like cooking. It's very nice."* This sits at band 6 across the board — Lexical
Resource "sufficient to discuss topics at length" but nothing less common,
Grammatical Range "a mix of short and complex sentence forms… with limited
flexibility", Fluency "willingness to produce long turns" never actually
exercised (2025 descriptor, Tier 1). Nothing is *wrong*. Nothing reaches 7
either.

---

## Part 2 — The long turn

### What is actually assessed

ielts.org (Tier 1, "Three parts…"): the ability to talk continuously about a
given topic and develop ideas about it, with proper grammar and vocabulary. This
is the only part where you produce a genuinely uninterrupted monologue, so it is
where **Fluency & Coherence** is most exposed — specifically the band-6/7
discriminator of whether hesitation breaks your thread.

### The 1-minute note method

Tier 1 gives you the permissions; Tier 2 gives you the method.

**Permissions (Tier 1).** Pencil and paper are provided (British Council). Notes
are optional — the card says you *can* make some notes "if you wish"
(official sample tasks PDF). IDP's Part 2 article (Tier 1, fetched 2026-07-31)
adds: "Keep writing until the examiner asks you to start."

**Method (Tier 2, two independent sources agreeing).**

- **Keywords, never sentences.** IELTS Advantage: jot a few key words, not
  sentences, roughly 35 seconds of the minute; one or two words per card point;
  these are reminders, not a script. E2Language: you will not have time to write
  full sentences, but you will have time for keywords, and they should guide you
  and rescue you if you dry up.
- **Use the bullets as headings.** IELTS Advantage: write the headings with space
  between, then fill keywords beside each. IDP (Tier 1) independently recommends
  dividing the paper into four sections for the three bullets plus the final
  clause, using abbreviations.
- **Follow them in order.** IDP (Tier 1): "Start at the first bullet point and
  then keep going in a logical manner."
- **Plan the grammar, not just the content.** E2Language (Tier 2) makes the point
  that matters most for a 6→7 push: use the minute to plan *the range of English
  you intend to show* — tenses and structures, not only vocabulary. This is
  directly supported by the 2025 GRA descriptor, where band 7 requires both
  simple and complex sentences used effectively (Tier 1).

**Concrete note template for this reader** (my synthesis of the two Tier 2
methods and IDP's four-box layout — presented as a method, not as an official
prescription):

```
bullet 1 →  2–3 keywords   (+ one specific: a name, a number, a place)
bullet 2 →  2–3 keywords   (+ the tense you'll use here)
bullet 3 →  2–3 keywords
why/how  →  the feeling word + one comparison
SPARE    →  ...if I dry up: how I felt / compare to X / would I again
```

The "SPARE" line is the insurance policy against the 40-second collapse.

### Sustaining two minutes

- **Structure**: paraphrased opening, then bullet by bullet, with discourse
  markers between (IDP, Tier 1). IDP suggests an opener of the shape "Today, I
  would like to describe … to you" — serviceable, but see MYTHS: a memorable
  fixed opener used by thousands of candidates is exactly what examiners are
  trained to notice. Prefer a natural one you vary.
- **Extension moves when you run dry** (IELTS Liz, Tier 2): descriptions of the
  people or place involved; comparisons; a past memory; a future hope; your
  opinion; a recommendation. IDP (Tier 1) adds: use stalling phrases, glance
  back at the card, and *always say yes* if the examiner asks whether you have
  more to say.
- **Pace and breathing**: IDP (Tier 1) says speak at a measured pace, neither
  rushed nor sluggish, and breathe between sentences. This is not a soft tip —
  the 2025 Pronunciation descriptor names "a rapid speech rate" as one of the two
  named causes of band-6-level rhythm problems (Tier 1). Speeding up to *seem*
  fluent actively caps your Pronunciation band.

### Finishing early, and being stopped

- **Being stopped is normal and pre-announced.** The examiner tells you so before
  you start ("don't worry if I stop you", official frame, Tier 1). IELTS Liz
  (Tier 2) is unambiguous that interruption does not lower your score: "100%
  not."
- **Time-up mid-idea is fine.** IDP (Tier 1): if you didn't cover every point,
  "Don't worry if this happens, as you have already shown the examiner that you
  can speak at length."
- **Finishing early is the real risk.** In the official transcript the sample
  candidate stops well short of two minutes and the examiner simply says "Thank
  you" and moves to the rounding-off question (Tier 1). Nothing rescues you.
  Under the 2025 FC descriptor, band 7 requires readily producing **long turns**
  without noticeable effort; a 45-second turn gives the examiner no evidence of
  that (Tier 1).
- IELTS Liz (Tier 2) states the examiner cannot interrupt before the 2 minutes
  are up and that if you finish early you must indicate it. That is stricter than
  anything Tier 1 says, and the official transcript shows the examiner moving on
  after a short turn without any explicit signal from the candidate. **Do not
  print Liz's version.** Print the safe operational rule instead: *keep going
  until you are stopped; aim to be stopped.*

### Notes and the task card afterwards

- **Notes are not assessed.** Derivable from Tier 1: the 2025 descriptor rates
  four spoken criteria and nothing written. Safe to state.
- Whether the examiner physically collects the notes and card at the end could
  **not** be confirmed on any Tier 1 or Tier 2 page. Widely asserted on forums;
  no official statement located. `[UNVERIFIED]` — do not print as fact. Practical
  consequence is nil either way.

### Traps

- **Reading the notes aloud.** IELTS Advantage (Tier 2): notes are reminders; read
  them and your delivery goes flat and unnatural. Under the 2025 descriptor this
  costs twice — flat delivery hits Pronunciation ("Some effective use of
  intonation and stress, but this is not sustained" is the band-6 line), and a
  read-out register reads as memorised, which ielts.org names explicitly as
  something examiners spot (Tier 1).
- **A memorised story bent to fit the card.** The commonest high-cost Part 2
  failure. ielts.org (Tier 1) on over-rehearsal: memorisation leads to robotic
  delivery, and scripted responses stop the examiner assessing your real ability.
- **Treating the card as a checklist to be raced through.** Covering three
  bullets in 50 seconds and stopping is worse than covering two properly for
  two minutes, because the descriptor rewards the long turn, not the coverage.

### Band-6 failure mode in Part 2

Runs out at 50–70 seconds; the last 20 seconds are audible searching
("…and, erm… yeah, that's… that's basically it"); coherence visibly frays at the
end. That is *precisely* the 2025 band-6 FC line — coherence lost at times as a
result of hesitation, repetition or self-correction — sitting immediately below
the band-7 line where the same hesitation occurs but does not break coherence
(Tier 1).

---

## Part 3 — The two-way discussion

### What is actually assessed

ielts.org (Tier 1, format page): explaining opinions, and analysing, discussing
and speculating about issues. ielts.org's article (Tier 1, "Three parts…") adds:
the capacity to speak about related issues in greater depth, provide analysis,
and justify opinions.

This is where a 6.5 becomes a 7. Parts 1 and 2 can be carried by prepared
personal content; Part 3 cannot.

### The answer shape

ielts.org's own article (Tier 1) sets out a four-step framework: **give a direct
answer → explain with reasons → provide supporting examples → offer alternatives
or consequences.** That is an official endorsement of the shape the prior work in
`knowledge/tricks.md` §5 already recommends (opinion + reason + example +
concession), with one useful difference: the official fourth step is
*alternatives or consequences*, which is broader and easier to execute under
pressure than "concession".

Practical version for the reader:

> **Answer → Because → For instance → Although / which means**

The fourth slot is the one that separates bands. Either concede
("*although* that's much less true of older workers") or extrapolate
("*which means* within a decade the whole training model has to change").

### Handling pushback

Pushback is designed in — see the official Part 3 transcript above, where the
examiner interrogates the candidate's own claim four separate times (Tier 1).
ielts.org states it plainly: "Expect to be interrupted by the examiner from time
to time during this part of the test. This is completely normal." (Tier 1)

Two things follow, and only two:

1. **You are allowed to disagree.** ielts.org, "Don't overdo it" (Tier 1),
   explicitly warns against constantly agreeing with the examiner: disagreeing
   respectfully will not harm your score, because examiners assess coherence,
   grammar and pronunciation, **not whether they share your view**.
2. **Concede then hold.** The high-value move is to grant the examiner's point
   and then re-establish your own with a reason — this simultaneously produces a
   complex structure (concessive subordination) and demonstrates the flexible
   discourse-marker use the band-7 FC descriptor requires (Tier 1, 2025 PDF).

### Abstract and speculative language

The Part 3 question set is deliberately non-personal — the official frame moves
from "things we own" (Part 2) to "what gives people status in your country",
"have things changed since your parents' time", "does advertising influence what
people buy" (Tier 1). Notice the three axes: **generalisation, change over time,
causation.** Those are the three grammars you need.

British Council's Part 3 lesson PDF (Tier 1, fetched via WebFetch 2026-07-31)
confirms the functional set: expressing opinions, speculating about hypothetical
scenarios, and comparing/contrasting with discourse markers; and states that
requesting clarification is available and that pausing to think is acceptable.

| Function | Structures that earn GRA credit |
|---|---|
| **Generalising, hedged** | *tend to · on the whole · as a rule · broadly speaking · there are exceptions, but* |
| **Change over time** | present perfect + *over the last decade*; *used to*; *whereas a generation ago* |
| **Speculating** | *it's likely that · I'd imagine · that could well lead to · presumably · there's a good chance* |
| **Unreal conditions** | *if governments were to… they'd…*; *had that not happened, …* — the second/third conditional is the single highest-yield complex structure in Part 3 |
| **Causation** | *which in turn · that stems largely from · the knock-on effect is · it's driven less by X than by Y* |
| **Conceding** | *granted, … even so · that's true up to a point, but · I can see why people say that, although* |

Hedging is not decoration. The Lexical Resource descriptor at band 7 requires
awareness of style and collocation (Tier 1); unhedged absolutes ("all young
people are addicted to phones") read as both stylistically wrong and
analytically thin.

### Traps

- **Reverting to the personal.** Part 3 asks about *people in general*; answering
  about yourself ("For me, I use my phone a lot") is the commonest band-6 slide,
  because it dodges the analysis the part exists to elicit.
- **Length inflation.** Part 3 answers are longer than Part 1 but they are still
  answers, not speeches. The examiner has 4–5 minutes and several questions;
  IELTS Liz (Tier 2) notes the examiner will move on once you've demonstrated the
  language function in play.
- **Silence.** IDP (Tier 1) names going off-topic as a coherence risk and bare
  non-answers as a fluency risk. Saying something imperfect beats saying nothing.
- **Over-asking for clarification.** Allowed in Part 3, but IELTS Advantage
  (Tier 2) warns against using it on every question and Magoosh (Tier 2) says
  stop after two attempts and pivot to related content.

### Band-6 failure mode in Part 3

Opinion stated, one reason given, then the answer stalls — no example, no
consequence, no concession — and the candidate rescues it by restating the
opinion in different words. That is the 2025 band-6 FC picture exactly:
willingness to produce long turns, with coherence lost at times through
repetition and self-correction (Tier 1).

---

## Band descriptor decoder

**Source: the current official Speaking descriptors,
`ielts.org/cdn/ielts-guides/ielts-speaking-band-descriptors.pdf`, PDF metadata
created 2025-09-16 / modified 2025-09-17, Author IELTS, 4 pages. Downloaded and
extracted with pdfplumber, 2026-07-31 — Tier 1.**

Everything below is paraphrase. Per the research brief, **one short quote per
criterion only**; those four quotes are marked with ». Where the 2025 text
differs materially from the 2008 Cambridge public version, the delta is flagged
**Δ**.

### What each criterion actually measures

**Source: the official IELTS Speaking Key Assessment Criteria,
`ielts.org/cdn/ielts-guides/ielts-speaking-key-assessment-criteria.pdf`, Author
IELTS, created 2023-05-03, modified 2023-10-18, 4 pages — Tier 1.** This
document gives no bands. It gives the **key indicators** examiners listen for.
It is the single most useful Tier 1 document for a 6.5→7 candidate, because it
converts four vague criterion names into a checklist of trainable behaviours.
All paraphrased.

**Fluency & Coherence** — talking with normal continuity, rate and effort, and
linking ideas into connected speech.

*Fluency indicators:* **speech rate** — ideally not too slow, because slow speech
makes it hard to hold the links between words and propositions in mind;
**speech continuity** — flow should not be excessively broken by false starts,
backtracking, **functionless** repetitions of words and phrases, or pausing while
you hunt for a word.

*Coherence indicators:* logical sequencing of spoken sentences; **clear marking
of the stages of a discussion, narration or argument — using appropriate pausing,
spoken discourse markers, and fillers**; **relevance of your spoken sentences to
the general purpose of the turn**; cohesive devices within and between spoken
sentences (logical connectors, pronouns, conjunctions).

Three things fall straight out of this, and all three change advice:

1. **Fillers are named in the official criteria as a coherence device.** Not
   tolerated — *listed*, alongside pausing and discourse markers, as a way of
   marking the stages of an argument. This is Tier 1 backing for S15/S16 and
   kills the "never use fillers" advice outright.
2. **Repetition is only penalised when it is "functionless".** Repeating for
   emphasis, or repeating your last two words to hold a sentence together while
   you retrieve the next one, is not the repetition the criterion is
   complaining about. That is exactly the recovery technique recommended for the
   6→7 FC jump.
3. **Relevance is an explicit coherence indicator.** This is the Tier 1
   refutation of "content doesn't matter" (MYTHS M3). Your answer's relevance to
   the purpose of the turn is assessed — at every band, not just 8 and 9.

*Also note the definition of a "spoken sentence"* the document supplies: the
spoken unit that most closely corresponds to a written sentence, but which may
include **verbless structures and ellipsis** performing a sentence-like function,
marked off by a brief final pause and falling intonation. This matters for GRA:
natural spoken ellipsis ("Depends on the country, really.") is **not an error**.
Candidates who force every utterance into a full written sentence are solving a
problem that does not exist, at the cost of sounding stilted.

**Lexical Resource** — the range of vocabulary available, which determines what
topics you can discuss and how precisely you can express meaning and attitude.

*Indicators:* variety of words; adequacy and appropriacy for **referential
meaning** (labelling things correctly), **style** (formal/informal),
**collocation** (including idiomatic expressions), and **indicating the speaker's
attitude to the content — favourable, neutral or unfavourable**; and the ability
to **paraphrase round a vocabulary gap, with or without noticeable hesitation**.

Two under-exploited levers here:

- **Attitude marking is a named indicator, and almost nobody trains it.** Stance
  adverbials and evaluative framing are cheap, natural, and directly creditable:
  *regrettably · thankfully · to be fair · worryingly · it's encouraging that ·
  what troubles me is · the real upside is · I'm not entirely convinced.* For a
  Part 3 answer this is often worth more than a rare noun.
- **Paraphrase is credited "with or without noticeable hesitation."** So groping
  visibly toward the right words and getting there still counts as paraphrase.
  Not knowing a word is not the problem; going silent is.

**Grammatical Range & Accuracy** — accurate, appropriate syntax, and the range of
grammar that determines how complex a proposition you can express.

*Range indicators:* length of spoken sentences; appropriate use of **subordinate
clauses**; **complexity of the verb phrase** — auxiliaries in continuous and
perfect aspect, **modality**, and the **passive**; **complexity of other phrases**
— modification before and after the head noun or adjective; and **range of
sentence structures, especially moving elements around for information focus**.

*Accuracy indicators:* **error density** (errors per amount of speech) and the
**communicative effect** of the errors (their impact on intelligibility and
precision).

This is the most concretely useful list in the document, because it names the
grammar to drill rather than saying "use complex structures":

| Range indicator | What to actually practise |
|---|---|
| Subordinate clauses | *although / whereas / which in turn / the reason being that* |
| Verb-phrase complexity — aspect | *has been rising · had already fallen · will have changed* |
| Verb-phrase complexity — **modality** | *might well · would have to · ought to · is bound to · can't have been* |
| Verb-phrase complexity — passive | *is often argued · has been overlooked · would be seen as* |
| Phrase complexity (pre/post-modification) | *a **deeply entrenched** cultural **assumption about work*** — adjectives before the head noun, prepositional and relative material after it |
| **Information focus** | **clefting and fronting**: *What really matters is… · It's the parents who… · That, I think, is the real issue.* Almost no band-6 candidate does this, and it is explicitly listed |

Note that **error density**, not error presence, is what is rated — consistent
with the band-7 descriptor tolerating "a few basic errors". And the
**communicative effect** clause tells you which errors to prioritise: an error
that obscures meaning costs more than one that does not. That is the principled
basis for the self-correction rule in S19.

**Pronunciation** — accurate and sustained use of a range of phonological
features to convey meaning.

*Indicators:* the ability to **divide speech into meaningful utterances or
chunks**; appropriate **rhythm and stress timing**, and the **linking of sounds,
using features such as elision, to produce connected speech**; use of **stress
(including emphatic and contrastive) and intonation to enhance meaning**;
production of sounds at word and phoneme level (**word stress**, vowel and
consonant production) and **the degree of effort required of the listener** to
understand them; and **the overall effect of accent on intelligibility**.

This is Tier 1, dated 2023, and it confirms the entire
[Pronunciation for Arabic + French L1](#pronunciation-for-arabic--french-l1)
section below, item for item. Two points are worth pulling out:

- **"The overall effect of accent on intelligibility"** is now a *direct* Tier 1
  statement, not an inference from where the word "accent" appears in the band
  grid. Accent is assessed **only** through its effect on how hard you are to
  understand. Nothing else about it is rated.
- **Linking and elision are named.** Connected speech is not a band-9 luxury; it
  is one of five listed indicators. For a syllable-timing L1 this is the same
  muscle as stress-timing — *asked_a_lot* → /ɑːstəlɒt/ — and drilling one trains
  the other.

**One nuance the two documents create together:** the Key Assessment Criteria
warns against speech that is **too slow** (a fluency risk), while the 2025 band-6
descriptor names a **rapid speech rate** as a rhythm-wrecker (a pronunciation
risk). They are not in conflict — they bracket the target. Slow costs you
Fluency; fast costs you Pronunciation. The instruction is *measured*, which is
also what IDP advises (Tier 1).

### Fluency & Coherence

| Band | Paraphrase of the 2025 descriptor |
|---|---|
| **8** | Fluent, with only occasional repetition or self-correction. Hesitation may still occasionally be for language, but most of it is about content. Topic development is coherent, appropriate and relevant. |
| **7** | Keeps going and readily produces long turns with no visible effort. Hesitation, repetition and self-correction do occur, often mid-sentence, and they do signal difficulty reaching the right language — but » *"these will not affect coherence."* Spoken discourse markers, connectives and cohesive features are used **flexibly**. |
| **6** | Keeps going and shows willingness to produce long turns. **Coherence is lost at times** because of hesitation, repetition or self-correction. Uses a range of discourse markers, connectives and cohesive features, but not always appropriately. |

**Δ — this is the correction that matters most.** The 2008 version's band 7 read
"may demonstrate language-related hesitation at times". `knowledge/band-descriptors.md`
extrapolated from that to: *"Where band 6 becomes band 7: hesitation stops being
about finding words. Both bands hesitate — band 7 hesitates while thinking about
the idea."* **The 2025 text says the opposite.** At band 7 the hesitation is
still explicitly about accessing language, and it is explicitly mid-sentence.
Hesitating *about content rather than language* is the **band 8** line, not the
band 7 line.

**The real 6→7 discriminator in FC is whether the hesitation breaks the thread.**

> **Band 6 (coherence lost):**
> "I think it depends on… the government should — well, actually the *parents*
> should… hmm. What was I… sorry. Yes, so, parents."
> The thread is dropped and has to be restarted.

> **Band 7 (same hesitation, thread intact):**
> "I think it depends largely on — well, on how early it starts, really. If
> children are taught to budget at, say, ten or eleven, then by the time they're
> earning they've already got the habit."
> There are two clear language-searches ("depends largely on — well, on…",
> "at, say, ten or eleven"). Neither loses the sentence. That is a band 7.

**Actionable rule for the book:** you do not have to stop hesitating to reach 7.
You have to stop *abandoning sentences*. Train the recovery, not the fluency:
when you stall mid-clause, repeat the last two or three words and continue the
same grammatical structure — never restart with a new one.

### Lexical Resource

| Band | Paraphrase of the 2025 descriptor |
|---|---|
| **8** | Wide resource, used readily and flexibly across all topics for precise meaning. Skilful use of less common and idiomatic items despite occasional slips in word choice and collocation. Paraphrases effectively as required. |
| **7** | Resource used flexibly across a variety of topics. Some ability with less common and idiomatic items; awareness of style and collocation is visible, though inappropriate choices occur. » *"Effective use of paraphrase as required."* |
| **6** | Resource sufficient to discuss topics at length. Word choice may be inappropriate, but the meaning still comes through. **Generally** able to paraphrase successfully. |

**Δ:** substantively unchanged from 2008; the 2025 wording is tightened. The
prior work's summary here holds.

The 6→7 gap is **two words in the descriptor**: "generally able to paraphrase"
becomes "effective use of paraphrase", and "awareness of style and collocation"
appears for the first time.

> **Band 6 (paraphrase succeeds, but visibly):**
> "…the thing that you use for, you know, to keep the food cold."

> **Band 7 (paraphrase effective, plus a collocation):**
> "…some sort of cold storage — a chill cabinet, I suppose you'd call it."
> Note *cold storage* and *chill cabinet*: not rare words, but the right
> collocations, produced without stalling.

**The trap for a French speaker specifically:** band 7 requires *awareness of
style*. French academic register transferred into spoken English reads as
stylistically wrong, not sophisticated. "*It is necessary to underline the
importance of…*" in a spoken answer is an LR problem, not an LR strength.

### Grammatical Range & Accuracy

| Band | Paraphrase of the 2025 descriptor |
|---|---|
| **8** | Wide range of structures, flexibly used; the majority of sentences are error-free. Occasional inappropriacies and non-systematic errors. A few basic errors may persist. |
| **7** | A range of structures used flexibly. » *"Error-free sentences are frequent."* Both simple and complex sentences are used effectively despite some errors. **A few basic errors persist.** |
| **6** | A mix of short and complex sentence forms and a variety of structures, but with limited flexibility. Errors occur frequently in complex structures, though they rarely block communication. |

**Δ — a genuinely useful addition.** The 2025 band 7 adds two clauses the 2008
version did not have: *both simple and complex sentences are used effectively
despite some errors*, and *a few basic errors persist*. Band 8 also tolerates a
few persistent basic errors.

**Consequence for this reader:** you do **not** need to eliminate your
third-person `-s` slips or your article errors to reach 7. Those are exactly the
"few basic errors" the descriptor allows at 7 *and* at 8. What you need is
(a) frequent error-free sentences and (b) complex sentences that *work* — not
complex sentences attempted and botched. That reframes the whole revision
priority: **stop hunting basic slips; start making your complex sentences land.**

> **Band 6 (complex attempted, fails):**
> "If the government would invest more in the public transport, so the people
> will use it more."
> Two errors inside the conditional (*would* in the if-clause; *so* + *will*),
> plus *the* before an abstract mass noun. The complex structure is the thing
> that broke.

> **Band 7 (complex lands; a basic error survives):**
> "If the government invested more in public transport, people would use it far
> more readily — and that in turn take pressure off the roads."
> The second conditional is clean and effective. *that in turn take* is a missing
> third-person `-s` — a "basic error persisting", explicitly permitted at 7.

Highest-yield complex structures to drill, all directly evidenced as band-7
range: second and third conditionals; concessive clauses (*although*, *even
though*, *whereas*); relative clauses (especially non-defining, *which in turn*);
present perfect for change over time; passive for generalisation (*it's often
argued that*).

### Pronunciation

| Band | Paraphrase of the 2025 descriptor |
|---|---|
| **9** | Full range of phonological features conveying precise and subtle meaning. Connected-speech features sustained throughout. Effortless to understand. **Accent has no effect on intelligibility.** |
| **8** | Wide range of phonological features conveying precise and subtle meaning. Can sustain appropriate **rhythm**. Flexible use of stress and intonation across long utterances, with occasional lapses. Easy to understand throughout. **Accent has minimal effect on intelligibility.** |
| **7** | **Defined only by reference to its neighbours:** all the positive features of band 6, plus some — but not all — of band 8. |
| **6** | Uses a range of phonological features, but **control is variable**. Chunking is generally appropriate, but » *"rhythm may be affected by a lack of stress-timing and/or a rapid speech rate."* Some effective use of intonation and stress, but not sustained. Individual words or phonemes may be mispronounced, causing only occasional lack of clarity. Can generally be understood throughout without much effort. |
| **5** | **Defined by reference:** all the positive features of band 4, plus some — but not all — of band 6. |

**Confirmation of the prior work's claim:** yes, **bands 5 and 7 are still
defined by reference to their neighbours** in the current 2025 edition (band 3
is too). Bands 4, 6, 8 and 9 are fully specified. The prior work was right about
this.

**Δ — and this is a large one.** The 2008 band-6 Pronunciation cell said only:
range of features with mixed control, some effective use not sustained, generally
understandable though mispronunciation reduces clarity at times. The **2025 band-6
cell adds three named diagnostics that did not exist in the old version**:

- **chunking** (dividing speech into sensible thought-groups),
- **stress-timing** (English's rhythm, where stressed syllables recur at roughly
  even intervals and unstressed ones compress),
- **rapid speech rate** as an explicit rhythm-wrecker.

These are the exact three things a French-and-Arabic-dominant speaker fails on —
see the next section. The 2025 descriptor has, in effect, published this reader's
pronunciation syllabus.

**How band 7 is actually reached, given it has no positive features of its own.**
Because band 7 = all of band 6 + *some* of band 8, and band 8's positive features
are (i) a wide range of features conveying precise/subtle meaning, (ii) sustained
appropriate rhythm, (iii) flexible stress and intonation over long utterances,
(iv) easy to understand throughout — the cheapest route to 7 is to **fully secure
every band-6 feature and then buy one band-8 feature outright.** For this reader,
the buyable one is **(ii) sustained rhythm**, because it is a trainable motor
habit rather than a vocabulary of new sounds.

> **Band 6 delivery (syllable-timed, flat):**
> `I · THINK · THAT · THE · GOV · ERN · MENT · SHOULD · IN · VEST · MORE`
> Every syllable roughly equal length, no reduction, prominence drifting to the
> ends of words.

> **Band 7 delivery (stress-timed, prominence chosen):**
> `I think the GOVernment should inVEST a lot MORE in it`
> with *the*, *should*, *a*, *in*, *it* compressed to schwa, and three clear
> beats. Same words. Same accent. Different band.

---

## Pronunciation for Arabic + French L1

The reader is a **Tunisian Arabic** L1 speaker who is also **fluent in French**.
That combination is not the same as "an Arabic speaker" and not the same as "a
French speaker", and the generic advice for either is partly wrong for him.

### The transfer map

| Feature | Why it transfers | Evidence |
|---|---|---|
| **/p/ heard as /b/** | Tunisian Arabic has /p/ and /v/ only in non-Arabic loanwords, and they are "usually replaced by /b/"; loanwords get nativised over time (French *appartement* → *buṛtmān*, Italian *pacco* → *bakū*). | Tunisian Arabic phonology descriptions surfaced 2026-07-31 — **Tier 3**, promoted only as background; the *consequence* below is what the book should teach |
| **/p/ heard as /b/ — the French route, which matters more here** | French voiceless stops /p t k/ are **unaspirated**; English word-initial /p t k/ carry ~30–75 ms of aspiration. Learners producing unaspirated word-initial /p/ "may have these perceived by English listeners as voiced stops (*bin* instead of *pin*)." | Phonetics sources on VOT and aspiration, 2026-07-31 — **Tier 3 discovery, but this is textbook articulatory phonetics, not IELTS folklore**. Flag `[UNVERIFIED]` if the book asserts the millisecond figures |
| **/θ/ → [t] or [s]; /ð/ → [d] or [z]** | Two independent pushes. (a) In nonstandard and dialectal Arabic pronunciations /θ/ and /ð/ merge to [t]/[d] or [s]/[z]. (b) The dental fricatives are **absent from French entirely**, and French speakers substitute /s/ or /z/ — "*zis*", "*sink*" for *this*, *think*. | Arabic phonology descriptions + French-L1 pronunciation error sources, 2026-07-31 — **Tier 3**, but consistent across multiple independent sources |
| **/h/ dropped, or inserted where it doesn't belong** | /h/ is absent from the French phonemic inventory. Documented French-L1 behaviour is **both** deletion from h-initial words **and** epenthesis onto vowel-initial words — *eat/heat* confusion in production and perception. | Published research on /h/ in French learners of English, 2026-07-31 — **Tier 3**; well-attested |
| **/v/ → /f/** | /v/ patterns with /p/ in Tunisian Arabic: loanword-only, usually replaced. French *has* /v/, so this should be his weakest interference of the set — check it, don't assume it. | Same Tunisian phonology sources — **Tier 3** |
| **Word stress in the wrong place, drifting to the end** | French has no lexical stress: prominence falls at the end of the rhythmic group, and every syllable gets roughly equal duration. English stress can fall on any syllable and *changes meaning class* (`PHOtograph` → `phoTOgraphy` → `photoGRAPHic`). | French prosody descriptions, 2026-07-31 — **Tier 3 for the sources, Tier 1 for why it matters**: the 2025 descriptor names stress and rhythm at bands 6 and 8 |
| **Syllable-timing instead of stress-timing** | Both French and Arabic are far closer to syllable-timed than English is. French speakers "pronounce every word separately and evenly, making their speech sound very broken — almost robotic." | Same — **Tier 3 for the mechanism**. **But the consequence is Tier 1**: the 2025 band-6 Pronunciation cell explicitly names "a lack of stress-timing" as a rhythm limiter |
| **Final consonant clusters** | English `-skt` (*asked*), `-ksts` (*texts*), `-lfθs` (*twelfths*) are hard for almost every L2 speaker. | Arabic-L1 cluster research, 2026-07-31 — **Tier 3** |

### The cluster myth, corrected for a Tunisian specifically

Generic ELT advice tells "Arabic speakers" they will insert vowels into consonant
clusters — *istudy*, *ispring*, *sitreet*. That advice is built on Modern
Standard Arabic and on Gulf/Egyptian dialects, whose phonotactics **forbid
consonant clusters in the syllable onset**; learners repair them by vowel
epenthesis or re-syllabification.

**Tunisian Arabic does not have that constraint.** Descriptions of Tunisian
phonology state that while Standard Arabic allows only one consonant in an
onset, Tunisian "commonly has two consonants in the onset", and initial `kt-`
is perfectly allowable. (Tier 3 sources, 2026-07-31.)

**So: do not spend this reader's limited weeks drilling *street* and *spring*.**
He is likely to be fine on initial clusters and is *not* fine on English **final**
clusters, which Arabic of any variety does not supply in that density. Check
initial clusters once, confirm, and move on. `[UNVERIFIED — dialect-level claim
from Tier 3 sources; should be checked empirically against the reader's own
recording rather than assumed]`

### Remediation drills — mechanisms, not "practise more"

Each drill below names the articulatory or prosodic mechanism it changes. Every
one is testable from a phone recording, which is the only feedback channel this
text-based coaching system has (a limitation `knowledge/tricks.md` §5 already
identifies).

**1. /p/ — the aspiration drill, not the phoneme drill.**
The problem is almost certainly not that he cannot make [p]; French supplies it.
The problem is that his [p] has near-zero voice onset time, so English ears
categorise it as /b/.
*Mechanism:* add the puff of air (aspiration) on word-initial /p/, /t/, /k/.
*Drill:* hold a strip of thin paper a few centimetres from the lips. Say
**pin – bin, pack – back, pear – bear, port – bort, pray – bray.** The paper must
visibly jump on every *p* word and stay still on every *b* word. Two minutes a
day. Then transfer to running speech: **"a *p*erfect *p*lan for *p*ublic
*t*rans*p*ort."**
*Why it raises the band:* the 2025 band-6 cell tolerates mispronounced individual
phonemes only where they cause "occasional lack of clarity". A systematic
/p/–/b/ merge is not occasional; it turns *pair/bear*, *pack/back*, *port/bought*
into coin-flips for the listener, which is exactly the "reduces clarity" ceiling.

**2. /θ/ and /ð/ — visible tongue, then minimal pairs, then connected speech.**
*Mechanism:* dental fricative — tongue tip touches or lightly protrudes between
the teeth, air kept flowing (fricative, not stop). His likely substitutions are
[t]/[d] (Arabic route) or [s]/[z] (French route), and the two need different
corrections: a [t] substitution means he is *stopping* the airflow, a [s]
substitution means the airflow is right but the tongue is too far back.
*Drill, five minutes, escalating* (structure drawn from published ELT
pronunciation practice, Tier 3, 2026-07-31):
  1. Mirror. Exaggerate the position; the tongue tip must be **visible**.
  2. Isolated words: *think, thought, author, three, this, those, mother,
     weather.*
  3. Minimal pairs, said in random order while someone (or a recording) checks:
     **thin/tin, thank/tank, three/tree, then/den, they/day, breathe/breed,**
     and for the French route **think/sink, thing/sing, mouth/mouse,
     with/wiz.**
  4. A phrase: *"I think they'd rather breathe the other air."*
  5. **Record one sentence and listen back.** This step is the one that
     transfers; the first four alone do not.
*Why it raises the band:* `think`, `the`, `this`, `that`, `they`, `there`,
`with`, `something`, `three` are among the highest-frequency words in spoken
English. A systematic substitution here is not an occasional lapse — it is a
running tax on intelligibility.

**3. Word stress — learn the suffix rules, not the words.**
*Mechanism:* English stress is largely predictable from the suffix, so this is a
rules problem, not a memorisation problem.
  - `-ion`, `-ic`, `-ical`, `-ity`, `-ity`-type endings **pull stress to the
    syllable immediately before them**: `eduCAtion`, `ecoNOMic`, `poLItical`,
    `posSIbility`, `phoTOgraphy`.
  - Two-syllable noun/verb pairs shift: **REcord** (n) vs **reCORD** (v),
    **INcrease** (n) vs **inCREASE** (v), **PREsent** (n) vs **preSENT** (v).
    High-yield for Part 3, where you will use both forms of the same word.
  (Stress-suffix rules surfaced 2026-07-31 — **Tier 3 sources**, but these are
  standard reference-grammar facts; flag `[UNVERIFIED]` only if the book claims
  exhaustiveness.)
*Drill:* take the ten topic words you use most, mark the stressed syllable in
capitals in your vocab bank, and **hum the word before you say it** — hum only
the rhythm, `da-DA-da-da`. If the hum is wrong the word will be wrong.
*Why it raises the band:* stress is named explicitly at bands 6 and 8 of the 2025
Pronunciation descriptor (Tier 1). It is also the single fastest thing to fix,
because it needs no new articulation.

**4. Stress-timing — the rubber-band drill.**
*Mechanism:* English compresses unstressed syllables to schwa so that stressed
beats stay roughly evenly spaced. French and Arabic do not compress. This is the
one the 2025 descriptor names by name at band 6 (Tier 1).
*Drill:* take a sentence with a fixed number of content words and add function
words without adding time.
> **CATS** · **EAT** · **FISH**
> The **CATS** will **EAT** the **FISH**
> The **CATS** would have **EAT**en the **FISH**
Each line must take **the same amount of time to say**. Tap three beats on the
table and force the words to fit. The added words *must* be crushed — *would
have* becomes /wʊdəv/, *the* becomes /ðə/.
*Why it raises the band:* sustained appropriate rhythm is a **band-8** positive
feature (Tier 1). Band 7 = all of band 6 + *some* of band 8. This is the
band-8 feature that is cheapest for him to acquire, and it is therefore his most
efficient single route out of Pronunciation 6.

**5. Chunking — the slash drill.**
*Mechanism:* "chunking" — grouping words into thought units with pauses at the
boundaries — is named in the 2025 descriptor at bands 4 and 6 (Tier 1). Band 6:
chunking generally appropriate. Pausing *inside* a chunk (a French-style
even-tempo delivery, or a mid-phrase language search) is what breaks it.
*Drill:* write out a Part 2 answer and mark the boundaries with slashes:
> To be honest, / the thing I value most / is an old watch / my grandfather
> gave me / when I turned eighteen. //
Read it aloud pausing **only** at slashes. Then say it from keywords and check
the recording: did the pauses land on the slashes, or in the middle of *an old /
watch*?
*Why it raises the band:* it converts hesitation from a coherence-breaker into a
normal prosodic boundary — which is precisely the 2025 FC band-6 vs band-7
distinction (Tier 1). **This drill pays into two criteria at once, which no
other drill on this list does.**

**6. /h/ — the "hot air" check.**
*Mechanism:* French supplies no /h/, and French learners both drop it and add it.
*Drill:* palm in front of the mouth. **eat / heat · art / heart · air / hair ·
old / hold · I / high.** Warm air on the *h* words; nothing on the vowel-initial
ones. The over-insertion half matters as much as the deletion half — *"an 'igh
'ill"* and *"a high-old man"* are equally damaging.

**7. Final clusters — the exit-consonant drill.**
*Drill:* slow, then compress. **ask → asks → asked → he asked me.**
**text → texts → the texts.** **cost → costs → costed.** Exaggerate the final
consonants at half speed, then run them at speed. Do not insert a vowel and do
not drop the whole cluster — English speakers reduce it (*asked* → /ɑːskt/, often
/ɑːst/) but do not delete it.

### What is NOT penalised — the official position on accent

**The decisive statement is in the official Key Assessment Criteria (Tier 1,
created 2023-05-03).** Its list of pronunciation indicators ends with: **the
overall effect of accent on intelligibility.** Accent is assessed *only* through
that effect. There is no indicator for accent itself, for accent "quality", or
for resemblance to any native variety.

The band grid agrees. The word **accent** appears in the 2025 Speaking
descriptors **exactly twice**, and only at the top two bands: band 9, accent has
*no* effect on intelligibility; band 8, accent has *minimal* effect on
intelligibility (Tier 1). It appears nowhere at bands 6 or 7.

Two things follow, and both are load-bearing:

1. **Accent is never rated in itself. Only its effect on intelligibility is
   rated.** A Tunisian/French-accented delivery that is easy to follow is fully
   compatible with band 8.
2. **Trying to acquire a British or American accent is a waste of your six to ten
   weeks — and ielts.org says so directly.** Its "Don't overdo it" article
   (Tier 1) warns against manufacturing an accent you don't have, because
   assessment focuses on actual fluency and pronunciation clarity, not on how
   "interesting" you sound.

What *is* rated, per the 2025 band-6 cell: chunking, rhythm/stress-timing, speech
rate, intonation, stress, and mispronounced individual words or phonemes — judged
by how much clarity they cost (Tier 1).

---

## Strategies found

| # | Strategy | Tier | Source |
|---|---|---|---|
| S1 | Part 1: answer in **two to six sentences**, extending before the examiner has to ask "why?" | 1 | IDP "Seven mistakes to avoid"; IDP Part 1 article, 2026-07-31 |
| S2 | Part 1: **don't parrot the question back** — it wastes time and forfeits a paraphrase opportunity that LR is graded on | 1 | IDP "Seven mistakes" #7, 2026-07-31 |
| S3 | Part 1: **control which version of your life you present** (don't claim both work and study) so the topic stays inside your strongest vocabulary | 1 | IDP Part 1 article, 2026-07-31 |
| S4 | Part 1: match the tense of your answer to the tense of the question; Part 1 frames are built to sample present / present perfect / conditional | 1 | IDP Part 1 article; official sample frame, 2026-07-31 |
| S5 | Part 2: **keywords, not sentences** — roughly 35 seconds of the minute, one or two words per bullet, used as reminders | 2 (two independent) | IELTS Advantage; E2Language, 2026-07-31 |
| S6 | Part 2: lay the paper out as four boxes matching the three bullets plus the final clause; use abbreviations; keep writing until told to start | 1 | IDP Part 2 article, 2026-07-31 |
| S7 | Part 2: use the minute to plan **which grammatical structures you will show**, not only which ideas | 2 | E2Language, 2026-07-31 — corroborated by the 2025 GRA band-7 wording (Tier 1) |
| S8 | Part 2: **keep going until stopped.** Being stopped is pre-announced by the examiner and does not lower the score; finishing early forfeits evidence of the long turn | 1 + 2 | Official examiner frame (Tier 1); IELTS Liz on interruptions (Tier 2), 2026-07-31 |
| S9 | Part 2 extension moves when you dry up: people/place description · comparison · a past memory · a future hope · your opinion · a recommendation | 2 | IELTS Liz, 2026-07-31 |
| S10 | Part 2: **always say yes** if the examiner asks whether you have more to say | 1 | IDP Part 2 article, 2026-07-31 |
| S11 | Part 3: **direct answer → reasons → example → alternatives or consequences** | 1 | ielts.org "Three parts of IELTS Speaking", 2026-07-31 |
| S12 | Part 3: **disagreeing with the examiner is safe** — they mark language, not agreement | 1 | ielts.org "Don't overdo it", 2026-07-31 |
| S13 | Part 3: expect interruption; it is by design, not a warning sign | 1 | ielts.org "Three parts…"; the official Part 3 transcript, 2026-07-31 |
| S14 | Clarification: repetition anywhere a question is asked; **explanation/rephrasing only in Part 3**; never in Part 2; ask once, then pivot | 2 (three independent) | IELTS Liz; IELTS Advantage; Magoosh, 2026-07-31. Reinforced by the Tier 1 fact that comprehension is not a rated criterion |
| S15 | Fillers: **real words are safe, non-word sounds are not.** "Well", "to be honest", "let me see", "I suppose", "I guess", "it's something I haven't really thought about before" keep language flowing; "umm"/"ahh" are breakdowns with no linguistic value | **1** + 2 | **Key Assessment Criteria (Tier 1) lists "spoken discourse markers and fillers" as a coherence indicator**; IELTS Liz "Saying Umm Ahh in IELTS Speaking" (Tier 2), 2026-07-31 |
| S16 | Fillers: use them to buy time for **ideas**, not to hunt for **vocabulary** — the criteria name "pausing during which the test taker searches for words" as the fluency negative | **1** + 2 | Key Assessment Criteria (Tier 1); IELTS Liz (Tier 2); 2025 FC descriptor bands 7/8 (Tier 1) |
| S16b | Repetition is only penalised when **functionless**. Repeating your last two or three words to hold a stalling sentence together is a legitimate recovery move, not a fluency error | **1** | Key Assessment Criteria — the fluency indicator names "**functionless** repetitions of words and phrases", 2026-07-31 |
| S16c | Speak in **spoken sentences**, not written ones. Verbless and elliptical utterances that do a sentence's job ("Depends on the country, really.") are explicitly recognised as sentence units and are **not errors** | **1** | Key Assessment Criteria, definition of a "spoken sentence", 2026-07-31 |
| S16d | Mark your **attitude** to what you're saying — favourable, neutral or unfavourable — with stance language (*regrettably · to be fair · worryingly · it's encouraging that*). This is a named Lexical Resource indicator that almost no candidate trains | **1** | Key Assessment Criteria, LR indicators, 2026-07-31 |
| S16e | Drill the **named** range indicators rather than "complex sentences" in the abstract: subordination · perfect/continuous aspect · **modality** · passive · noun-phrase pre- and post-modification · **clefting and fronting for information focus** (*What really matters is… · It's the parents who…*) | **1** | Key Assessment Criteria, GRA range indicators, 2026-07-31 |
| S17 | Blanking: a native-sounding admission ("I'm so sorry, my mind just went blank") is itself a display of lexical resource | 1 | ielts.org "Don't overdo it", 2026-07-31 |
| S18 | Pace: speak at a measured rate and breathe between sentences — a rapid rate is a **named** band-6 rhythm limiter | 1 | IDP Part 2 article; 2025 Pronunciation band-6 cell, 2026-07-31 |
| S19 | Self-correction: correct **once, fast, and only when the error obscures meaning.** Frequency of self-correction is a limiting feature at every band from 4 to 9, and the GRA accuracy indicators rate **error density** plus the **communicative effect** of the error — so an error that doesn't obscure meaning is the cheapest kind to leave alone | descriptor-derived (Tier 1) + Key Assessment Criteria (Tier 1) + Tier 2 | 2025 FC descriptor; Key Assessment Criteria GRA accuracy indicators; IELTS Liz self-correction article, 2026-07-31 |
| S20 | Record every practice answer on your phone and listen back. It is the only feedback channel a text-based system cannot supply | 1 | British Council practice test pages recommend recording yourself, 2026-07-31 |
| S21 | Do not repeat the same words and phrases — it signals a limited spoken vocabulary | 1 | IDP "Seven mistakes" #5, 2026-07-31 |
| S22 | Don't overuse transition words; written connectives ("furthermore") sound wrong spoken, and overuse is explicitly a **band-5** feature | 1 + Tier 1 descriptor | IDP "Seven mistakes" #6; 2025 FC band-5 cell, 2026-07-31 |

### Self-correction: the honest answer

The brief asks whether correcting yourself helps or hurts. The descriptor answers
it directly, and the answer is uncomfortable.

Self-correction is named as a **limiting** feature at every single band of
Fluency & Coherence in the 2025 grid (Tier 1):

- band 9 — only very occasional; band 8 — only occasional;
- band 7 — some occurs, but does not affect coherence;
- band 6 — **coherence may be lost** because of it;
- band 5 — the candidate **relies on** it to keep going;
- band 4 — "Often self-corrects."

There is no band at which more self-correction is better. The popular advice
"correct yourself so the examiner sees you know the rule" is not supported
anywhere in the descriptor.

**But** a correction that repairs a genuine meaning error is still worth making,
because the alternative is an unclear utterance. The operational rule:

> **Correct it if the listener would otherwise misunderstand you. Otherwise, let
> it go and keep the sentence alive.** Never correct twice. Never go back to a
> sentence you already finished.

Whether the examiner rates the corrected form or the original for GRA purposes is
**not stated anywhere I could find** — logged as an
[open question](#open-questions-for-verifiers).

---

## MYTHS

Score-lowering or unsupported Speaking advice, with the reason it fails the
"how does this raise a band 6.5–7.5 score per the descriptors?" test.

**M1 — "At band 7 your hesitation should be about ideas, not about words."**
This is in the repo's own `knowledge/band-descriptors.md`. It is an
over-extrapolation from the **2008** descriptor. The **2025** band-7 FC cell
states the opposite: hesitation, repetition and self-correction do occur at
band 7, often mid-sentence, and they *do* indicate difficulty accessing
language — the requirement is only that they don't damage coherence.
Hesitating for content rather than language is the **band 8** line.
*Why it hurts:* it sets an unreachable bar, and it aims practice at the wrong
target. The trainable band-7 skill is sentence recovery, not hesitation
elimination. **(Tier 1 — 2025 descriptor PDF.)**

**M2 — "The Cambridge public-version Speaking descriptors are the ones to
study."**
The `assets.cambridgeenglish.org/webinars/…` PDF is a 2008-created, 2013-modified,
one-page document. Studying it means missing chunking, stress-timing, rapid
speech rate, and the band-7 GRA clauses about simple-and-complex sentences and
persisting basic errors — i.e. missing most of what tells this reader what to do.
**(Tier 1 — PDF metadata on both files.)**
*Note:* IDP's own Fluency and Coherence article still quotes the 2008 wording
verbatim. Official partner pages are not automatically current.

**M3 — "Content doesn't matter in Speaking; say anything, the examiner only marks
language."**
Circulating in strong form on Tier 2 sites (IELTS Liz: "Task completion, ideas
and content are irrelevant"). Half true, dangerously stated. **The official Key
Assessment Criteria (Tier 1, 2023) lists "relevance of spoken sentences to the
general purpose of a turn" as a key indicator of coherence** — so relevance is
assessed directly, at every band. On top of that the 2025 FC descriptor rates
**topic development** explicitly at bands 8 and 9 ("Topic development is
coherent, appropriate and relevant"), and IDP (Tier 1) states outright that if
your answer fails to address the question "you could get marks deducted for
coherence."
*Correct version:* your story need not be **true** — nobody verifies it — but it
must be **relevant and developed**.

**M4 — "Learn a British or American accent."**
ielts.org (Tier 1) explicitly warns against manufacturing an accent you don't
have. Accent appears in the descriptor only at bands 8 and 9, and only as *effect
on intelligibility*.
*Why it hurts:* it consumes the weeks that should go to rhythm, stress and the
three or four phonemes that actually cost clarity, and a faked accent usually
degrades intelligibility rather than improving it.

**M5 — "Memorise strong answers for the common topics."**
ielts.org (Tier 1): examiners are highly trained to spot memorised answers,
"which never bodes well"; over-rehearsal produces robotic delivery. IDP (Tier 1)
names it as mistake #1 and warns specifically about Part 1. The descriptor
reinforces it independently — memorised utterances are named as a **band 2/3**
feature in both Lexical Resource and GRA in the 2025 grid.
*Correct version:* learn flexible frameworks, collocations and functional
language. Never scripts.

**M6 — "Use idioms and phrasal verbs to prove your Lexical Resource."**
The band-7 LR descriptor asks for *some* ability with less common and idiomatic
items **and awareness of style and collocation** (Tier 1). A forced idiom is a
collocation failure and a style failure at the same time — it moves you down two
sub-features to gain one.
*Correct version:* precision over rarity. The right ordinary word beats the wrong
unusual one.

**M7 — "Fill every pause with 'That's an interesting question' or 'Well, it
depends'."**
IELTS Liz (Tier 2) separates real-word fillers (safe) from non-word sounds
(unsafe), but that licence is not unlimited: the 2025 FC band-5 cell names
**overuse** of discourse markers and cohesive features as a band-5 feature, and
band 6's fault is using them "not always appropriately" (Tier 1). A stock opener
on every answer is both overuse and a memorised-language flag.
*Correct version:* one or two per test, deployed where you genuinely need the
half-second.

**M8 — "Speak fast to sound fluent."**
The 2025 Pronunciation band-6 cell names **rapid speech rate** as one of two
explicit causes of rhythm failure (Tier 1). IDP (Tier 1) advises a measured pace
with breathing between sentences.
*Why it hurts:* under the descriptor, fluency is *continuity of production*, not
words per minute. Speed buys nothing on FC and actively caps Pronunciation.

**M9 — "Correct every mistake you notice so the examiner knows you know."**
See [self-correction](#self-correction-the-honest-answer). Self-correction is a
limiting feature at all nine bands. Frequent correction cannot raise a band and
can lower FC by a full band via the "coherence lost" clause.

**M10 — "Never ask the examiner to repeat — it looks bad."**
The four rated criteria contain no listening or comprehension component (Tier 1,
2025 grid). Asking cannot cost you a mark. Guessing and answering a different
question can.
*Caveat that is real:* explanation is only available in Part 3, and asking
repeatedly eats your speaking time.

**M11 — "You must cover all three bullet points on the cue card."**
IDP (Tier 1): if time runs out before you get through them, "Don't worry… you
have already shown the examiner that you can speak at length." There is no task-
achievement criterion in Speaking. Racing the bullets to tick them off costs you
the long turn that is actually rated.

**M12 — "Arabic speakers must drill initial consonant clusters — *istudy*,
*ispring*."**
Built on Modern Standard Arabic and on dialects that forbid onset clusters.
**Tunisian Arabic permits two-consonant onsets** (Tier 3 sources, 2026-07-31), so
this reader is unlikely to have the problem at all, while his real cluster
weakness — English **final** clusters (*asked*, *texts*) — goes untouched.
*Why it hurts:* it burns scarce practice time on a non-problem. **Verify against
his own recording before either drilling or skipping it.** `[UNVERIFIED]`

**M13 — "You can't get band 7 with an obvious foreign accent / with basic
grammar slips."**
Both false under the 2025 descriptor (Tier 1). Accent is not rated at 6 or 7 at
all. And band 7 GRA explicitly permits "a few basic errors" to persist — as does
band 8.
*Why it matters:* the opposite belief pushes candidates into slow, over-monitored
speech, which trades a real FC band for an imaginary GRA gain.

**M14 — "The Speaking test is always seven days before or after the written
test."**
Partner-specific and internally contradicted: British Council's FAQ says seven
days before or **two** days after; British Council's own test-format page says
seven days before or after; IDP says up to seven days either side for paper and
**the same day** for computer-delivered (all Tier 1, all fetched 2026-07-31). For
a computer-delivered candidate, "same day" is the expectation.
*Why printing it hurts:* a candidate who plans recovery time around a wrong rule
can arrive at a same-day Speaking test already exhausted from 2h40 of LRW.

**M15 — "Video-call Speaking is easier / harder, so choose your centre
accordingly."**
You don't choose — IDP states the format follows from the centre you book. And
the partners' own research found the score difference between modes negligibly
small, with 80% of examiners judging the modes equivalent (Tier 1).

---

## Open questions for verifiers

1. **Is there a Tier 1 statement of the clarification rules?** The
   "repeat-only in Part 1, explain-or-rephrase in Part 3" split rests on three
   Tier 2 sources plus a descriptor-derived argument. IDP's Part 1 article
   (Tier 1) lists *both* "Could you repeat that, please?" **and** "What does
   _____ mean?" without naming a part, which cuts slightly against the split.
   Look for examiner-facing guidance or a Cambridge handbook statement.

2. **When self-correction occurs, is the corrected or the uncorrected form rated
   for GRA?** Still nothing found either way. The Key Assessment Criteria narrows
   it usefully — GRA accuracy is rated on **error density** and the
   **communicative effect** of errors, which supports "correct only what obscures
   meaning" — but it does not say whether a self-corrected error still counts
   toward density. Material for a 6.5→7 candidate.

3. **Is IELTS Liz right that the examiner cannot interrupt Part 2 before two
   minutes, and that a candidate finishing early must signal it?** The official
   card and frame say "one to two minutes", and the official transcript shows the
   examiner moving on after a short turn without an explicit candidate signal.
   Resolve before printing anything about the two-minute floor.

4. **Confirm the British Council–hosted `ielts_speaking_band_descriptors.pdf` is
   the 2025 edition.** It 403s to curl and WebFetch; the inference rests on the
   indexed title line. If a verifier can retrieve it, compare the md5 against
   `c0f922334ce4…` (the ielts.org CDN file, 2026-07-31).

5. **Resolve British Council's internal contradiction on the Speaking scheduling
   window** — FAQ says "seven days before or two days after", test-format page
   says "seven days before or after". One is stale. Both were live 2026-07-31.

6. **Does any partner still officially describe the *superseded* Speaking
   descriptors as current?** IDP's Fluency and Coherence article quotes the 2008
   wording verbatim as if current. Worth knowing how widespread that is before
   the book cites any partner page for descriptor content.

7. **Tunisian Arabic phonotactics.** The claim that Tunisian permits two-consonant
   onsets (and therefore that initial-cluster epenthesis drills are wasted on this
   reader) rests entirely on Tier 3 descriptive sources. A verifier should either
   find a peer-reviewed reference or the book should present it as a hypothesis
   to test against the reader's own recording, not as fact. **This is the single
   Tier-3-dependent claim with the largest effect on how his practice time is
   spent.**

8. **What happens to the Part 2 notes and task card after the test?** No Tier 1 or
   Tier 2 statement located. Low stakes, but candidates ask. Currently
   `[UNVERIFIED]`.

9. **Is there official confirmation that the four Speaking criteria are weighted
   equally at 25% each?** Two IDP pages say 25% for two different criteria
   (Tier 1), and the descriptor grid is four parallel columns with no weighting
   note, so the inference is safe — but a single explicit Tier 1 sentence would
   be better than an inference stitched from two articles. **Note: the Key
   Assessment Criteria PDF states "There are nine bands and four criteria" and
   then defines all four, but says nothing about weighting either.** If an
   explicit statement exists it is somewhere else.

11. **Is the Speaking Key Assessment Criteria PDF (created 2023-05-03) still
    current, given the band descriptors were reissued 2025-09-16?** The Writing
    equivalent a sibling agent found also dates to 2023-05-03, so a 2023 KAC
    alongside 2025 descriptors may simply be the normal state. But a verifier
    should check `ielts.org/organisations/…/understanding-ielts-scoring` for a
    newer Speaking KAC before the book leans on it as hard as R6 does.

10. **The VCS articulation inference.** I suggest that crisp final consonants
    matter more under video-call delivery, reasoning from the published finding
    that clarification requests in Part 1 more than doubled under
    video-conferencing (26.7% → 63.3%). That is my inference, not the study's
    conclusion. Tagged `[UNVERIFIED]`; drop it or downgrade it to a hedge if a
    verifier disagrees.
