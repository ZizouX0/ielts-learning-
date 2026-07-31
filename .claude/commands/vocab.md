---
name: vocab
description: Build the vocabulary bank (ADD mode) or test it strictly (QUIZ mode) with collocations and IELTS topics.
---

# Vocabulary — ADD and QUIZ

Ask me which mode I want if I have not said: **ADD** or **QUIZ**.

---

# ADD mode — build the bank

## Step 1 — Choose the topic

Read `progress/vocab-bank.md` to see which IELTS topics are already covered, and
`progress/error-log.md` for topics where my vocabulary visibly failed me.

Pick an under-covered topic from the standard IELTS set:

education · technology · environment · health · work and careers · urbanisation ·
crime and justice · media and advertising · travel and tourism · culture and
tradition · family and society · government and public spending · science and
research · globalisation · art and creativity

## Step 2 — Give me 10 items

For each, give **all six fields** — an entry without collocations is close to
useless, because knowing a word and knowing how to use it are different things:

| Field | Requirement |
|---|---|
| **Word** | Include part of speech |
| **Meaning** | Plain English, not a dictionary quotation |
| **Collocations** | 2–3 real ones. This is the most important field. |
| **Example sentence** | IELTS-register, showing the collocation in use |
| **Topic** | From the list above |
| **Last tested** | Today's date |

Aim at **band 7–8 range**: precise, natural, mid-frequency academic vocabulary.
Not obscure showpieces.

> **mitigate** (v.) — to make something bad less severe
> **Collocations:** mitigate the effects of · mitigate the impact · mitigate
> against risk
> **Example:** Planting urban trees does little to reverse warming, but it does
> mitigate the effects of extreme heat in dense city centres.
> **Topic:** environment

## Step 3 — Anti-rules — state these every time

- **Never force idioms into Writing.** Idiomatic language belongs in Speaking.
  In Task 2 it reads as informal and can lower Lexical Resource.
- **Never thesaurus-substitute.** *Ameliorate the pecuniary situation* scores
  lower than *improve finances*, because the collocation is wrong. Band 7 is the
  **right** word, not the rare one.
- **Learn the collocation, not the word.** *Make research* is wrong; *conduct
  research* is right. That is the whole difference.
- **Check the register.** Some words are spoken-only (*a big deal*), some
  written-only (*notwithstanding*).

## Step 4 — Test immediately

Before writing anything to file, ask me to use **3 of the 10** in original
sentences about my own life or opinions. Mark them. Correct any collocation error
on the spot — an item learned wrong is worse than not learned.

## Step 5 — Append and push

Append all 10 to `progress/vocab-bank.md` with today's date. Commit and push:
`progress: vocab ADD — <topic> — 10 items`

---

# QUIZ mode — test the bank

## Step 1 — Select

Read `progress/vocab-bank.md`. Select **10 items** by priority:
1. Items never tested
2. Items with the **oldest** last-tested date
3. Items I have previously got wrong

Do not tell me which items you picked.

## Step 2 — Test

Mix the question types — recognition alone is too easy and does not predict
production:

- **Production:** "Write a sentence using ______ correctly in an IELTS Writing
  Task 2 register."
- **Collocation gap:** "______ research" / "mitigate the ______ of"
- **Definition → word:** "Which word in your bank means *to make something bad
  less severe*?"
- **Error correction:** give a sentence with the word used in a wrong
  collocation and ask me to fix it.

One at a time. Wait for each answer.

## Step 3 — Mark strictly

Right or wrong. No credit for "close".

Mark **wrong** if: the collocation is unnatural, the register is wrong for the
context, the part of speech is wrong, or the spelling is wrong. Explain each
failure — the point is the rule, not the score.

Report **x/10**.

## Step 4 — Update and push

In `progress/vocab-bank.md`:
- Update the **last-tested date** for every item tested
- Mark items I got wrong so they resurface sooner
- Do not delete items I got right — spaced repetition needs them back later

Commit and push: `progress: vocab QUIZ — x/10`

## Step 5 — End the session

One line: the item or collocation pattern most worth remembering.
