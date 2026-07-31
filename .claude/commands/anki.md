---
name: anki
description: Export the vocabulary bank to exports/anki-vocab.csv for Anki import.
---

# Export vocabulary to Anki

## Step 1 — Read the bank

Read `progress/vocab-bank.md`. Parse every entry into: word, meaning,
collocations, example sentence, topic, last-tested date.

Report how many entries you found. If the bank is empty, say so and suggest
running `/vocab` ADD first rather than writing an empty file.

## Step 2 — Build the CSV

Write `exports/anki-vocab.csv` with a header row and these columns:

| Column | Contents |
|---|---|
| `Front` | The word + a cloze prompt (see below) |
| `Back` | Meaning · collocations · example sentence |
| `Tags` | IELTS topic, plus `ielts` and `vocab` |

**The Front must test production, not recognition.** A card showing just the word
tests whether I can recall a definition — useless for the exam. What I need is
recall of the word from its meaning and collocation.

Build the Front as the word **plus a cloze sentence with the word blanked**:

```
mitigate — "Planting urban trees does little to reverse warming, but it does
_________ the effects of extreme heat." (v., environment)
```

And the Back with everything needed to self-mark:

```
mitigate (v.) — to make something bad less severe
Collocations: mitigate the effects of · mitigate the impact · mitigate against risk
Example: Planting urban trees does little to reverse warming, but it does
mitigate the effects of extreme heat in dense city centres.
```

## Step 3 — Escape the CSV properly

This matters — a malformed CSV imports as garbage:
- Quote every field containing a comma, quote mark or newline
- Escape internal double quotes by doubling them (`""`)
- Use UTF-8
- Use `\n` inside quoted fields for line breaks in the Back, or `<br>` if I
  confirm my Anki note type renders HTML

**Verify before finishing:** read the file back with Python's `csv` module and
confirm the row count matches the number of vocabulary entries, and that no row
has the wrong number of columns. Report the result. Do not claim the export
worked without checking it.

## Step 4 — Import instructions

Print these:

> **Importing into Anki**
> 1. Open Anki → **File → Import**
> 2. Select `exports/anki-vocab.csv`
> 3. Type: **Notes in Plain Text (.txt/.csv)**
> 4. Field separator: **Comma**
> 5. Tick **"Allow HTML in fields"** if your Back field uses `<br>`
> 6. Map: Field 1 → **Front**, Field 2 → **Back**, Field 3 → **Tags**
> 7. Choose or create a deck, e.g. **IELTS Vocabulary**
> 8. Tick **"Ignore first line"** (it is the header)
> 9. Click **Import**
>
> On duplicates, Anki matches on the first field — re-importing after adding new
> words updates rather than duplicating existing cards.
>
> **Suggested study setting:** 20 new cards a day, reviews unlimited. Do reviews
> daily; the schedule only works if it is not interrupted.

## Step 5 — Commit and push

Commit `exports/anki-vocab.csv` and push:
`exports: anki vocab CSV — <n> cards`
