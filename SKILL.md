---
name: humanize-text
description: >
  Turns machine-sounding text into prose a specific human could have written, in Brazilian
  Portuguese and in English (US and UK), without paraphrasing and without losing facts.
  Measures AI-slop with a graded lexicon validated against about 11 million words of human
  speech per language, diagnoses paragraph by paragraph, and rebuilds from the factual spine
  instead of polishing. Also checks the status of claims (analogy turned into definition,
  dispute turned into consensus). Three modes: clean raw AI research, rewrite a draft to
  publish, audit existing texts. Use when asked to "humanize", "make this sound less like
  AI", "remove AI tone", "rewrite this draft", "this reads like ChatGPT", "humanizar",
  "tirar a cara de IA", "reescrever este rascunho", "esse texto ficou genérico". Not a tool
  for evading AI detectors or hiding provenance.
---

# Humanize text · PT-BR and EN (US/UK)

The model writes the most probable text on any subject: the average of what has been written. Humanizing is moving away from that average on purpose, in **substance** first (a specific detail, a position with an argument, new information, an image of your own) and in **signal** second (rhythm, unexpected exact words, clean of tics). Signal over empty content is humanwashing, and it is worse than honest slop.

## Start (in this order)

1. **Language.** Detect it from the text (or ask if mixed). Portuguese → read `references/blacklist-pt-BR.md`. English → read `references/blacklist-en.md` and fix the variant: US or UK (follow the text or the user; ask once if it matters and is unclear).
2. **Mode** (details in `references/method.md`):
   - **A · Raw AI input** used as a source → clean, auditable base; **verify facts before polishing voice**; never humanize research into pretty prose.
   - **B · Draft to publish** → **rebuild from the factual spine**, do not retouch.
   - **C · Audit** of existing texts → **diagnosis first**, edits only with approval.
3. **Genre.** It sets the regime: technical text runs light (rigour first, more precise beats less AI-like); essays, scripts, posts and chat run in full.
4. **Load the bans before writing a word.** Read the blacklist of the language now, not at the end: shaping by what you reject works better than filtering afterwards.
5. **Measure before reading** when you can run Python: `python scripts/scan.py <file>` (auto-detects language and type; `--variant us|uk`; `--dashes zero` if the house style bans em dashes). Read only the paragraphs it flags, plus two it let through as a control. Without Python, run the gate by reading.

## Rules that always hold

- **No paraphrasing.** A revision that only swapped words did nothing. Add what the model lacked: the fact, the position, the image, the experience.
- **No invented facts.** No name, number, date, quote or source enters that was not in the input or verified. Run the fact guard: `python scripts/scan.py --facts BEFORE AFTER` (or list them by hand). Nothing enters or leaves unrecorded.
- **Caveats that add a fact stay.** Empty hedging goes; "works as", "according to [named source]", "where the analogy breaks" are content.
- **Never switch "works as" to "is"** unless the source states identity (`references/status-check.md`).
- **Respect the exceptions:** quotations, titles, proper names, technical terms used technically, and real voice (hesitation, asides, odd details) are not tics.
- **Critical pass:** after the first edit, list up to five things that still give the text away as AI, fix only those, at most two cycles.
- **Both gates before closing:** voice (blacklist) and status (`references/status-check.md`). Then the humanwashing test: with every style marker removed, is anything left that is not in any summary of the topic?
- **No provenance laundering.** This is an editing method, not a way to hide that a tool was used. Success is never measured by an AI detector.

## Close

A short report in the format at the end of `references/method.md`: before/after score, strong hits by rule, which paragraphs got which new substance, the fact-guard result, exceptions kept, pending decisions for the author.

## Files

- `references/method.md` · modes, meter, common flow, report
- `references/blacklist-pt-BR.md` · 28 items, weights, exceptions, genres, em dash, positive techniques, gates (Portuguese)
- `references/blacklist-en.md` · the same for English, with US/UK spelling and punctuation
- `references/status-check.md` · the truth gate: five questions, seven erosion patterns, four-level scale
- `scripts/scan.py` · the meter (Python 3, standard library only) with `lexicon_pt-BR.tsv` and `lexicon_en.tsv`
- `PROMPT.md` · the whole method in one file, to paste into any assistant that does not load skills
