# Method · measure, decide, rebuild

## Three modes

| Mode | Input | Goal |
|---|---|---|
| **A · Raw AI input** | a research report, summary or draft from any AI that will be used as a *source* (not published as is) | a **clean, auditable base**, not pretty prose |
| **B · Draft to publish** | AI text that will become an essay, script, post, newsletter, description, email | a text **only this author could have written** |
| **C · Audit** | existing texts (yours, a client's, an archive) to check whether they pass | **diagnosis first**; edit only with the owner's approval |

**What this skill does NOT do:**
- **No provenance laundering.** Rewriting is an editorial decision. Running text through a model to erase traces and then claiming purely human authorship is out of scope, and success is never measured by an AI detector.
- **No source checking.** Sources, DOIs and hallucinations belong to a fact-checking pass (the companion skill `rigorous-research` does it). This skill treats the voice, plus the status of claims.
- **No paraphrasing.** Swapping words for synonyms does not humanize; a revision that only changed words did nothing.
- **No trimming data for style.** In technical text, more precise beats less AI-like.

## Reading the meter

If you can run Python: `python scripts/scan.py <file>` (language and type auto-detected; `--lang pt|en`, `--variant us|uk`, `--type`, `--dashes signal|zero|ignore`). It returns words, **strong** hits (one calls for an edit), **weak hits in clusters**, structure signals (fragment runs, uniform rhythm, punchline closes, triads, serial connectors, repeated openings, decorative bold, em dashes, Title Case headings, mixed US/UK spelling), **points per 1,000 words**, a **verdict**, and the **most loaded paragraphs**.

| Verdict | pts/1000 (published text) | pts/1000 (technical) | What to do |
|---|---|---|---|
| **CLEAN** | under 6 | under 8 | nothing beyond the five-survivor check |
| **TOUCH-UP** | 6 to 15 | 8 to 20 | edit **only the loaded paragraphs**; touch at most about 10% of the text |
| **PARTIAL-REWRITE** | 15 to 30 | over 20 (deep clean) | rewrite the loaded paragraphs **with new substance** |
| **REBUILD** | over 30 | n/a | do not retouch: mode B from the factual spine |

**Limits:** it measures voice signals, not authorship. CLEAN can be hollow; a high score can be a human with tics. Thresholds are provisional: calibrate them on texts you consider good (if the meter flags them, fix the meter, not the text).

**Without Python** (ChatGPT without code, a phone): run the gate by reading, using the blacklist of the text's language and the five survivors; the scoring is a convenience, the reading is the method.

## Common flow (every mode)

1. **Convert to plain text or Markdown.** A formula that arrived as an image is marked and rewritten in LaTeX, never guessed.
2. **Identify language, type and mode.** The type sets the regime (genre table in the blacklist file).
3. **Measure before reading.** Read the report, then only the paragraphs it points to, plus **two control paragraphs** it let through, to check for false negatives.
4. **Diagnose each flagged paragraph:** which of the five kinds of slop, which of the 28 items. Decide per paragraph: cut · rewrite with the missing fact · add substance · keep (an exception applies; say which).
5. **Critical pass before the final version.** After the first edit, do **not** generate a new version: list up to five things that **still give away that an AI wrote this**, strongest first, and fix only those. Two cycles at most. Pointing without rewriting stops you accepting the first solution.
6. **Fact guard.** `python scripts/scan.py --facts BEFORE.md AFTER.md` compares numbers, DOIs, URLs, LaTeX and proper names. **Nothing enters or leaves unrecorded**: what was removed, and why; what was added, and from where. Without Python, list them by hand.
7. **Both gates:** voice (blacklist file) **and** status (`status-check.md`). Measure again. **A lower score does not prove humanization:** run the humanwashing test.
8. **Report** (format below).

## Mode A · Raw AI input

The goal is a clean, verifiable base. Humanizing raw research is wasted work.

**Order matters: audit first, voice second.** Fact-checking cuts, merges and rewrites a lot; polishing a paragraph that will be deleted is double work.

1. Check sources and claims (the `rigorous-research` skill, or your own verification).
2. Only then run the meter with `--type technical` and clean what the light regime asks for:

| Clean | Leave alone |
|---|---|
| era frame, immersion verb, empty hedging, brochure adjectives | LaTeX, numbers, DOIs, citation format, tables |
| anonymous authority (**demands the source**: also a verification finding) | terminology and technical structure |
| interpretive gerund (asserts meaning: **status gate**) | section order |
| persona preamble and chatty closing | em dashes, rhythm, triads, fragments |
| lyrical metaphor leaking into a technical base | |

3. Never change "works as" into "is" without checking the source.
4. Two AI reports on the same topic: the meter score is supporting data, never the criterion for picking one. The criterion is which sources check out.

## Mode B · Draft to publish

**Rebuild, do not retouch.** Polished AI prose is still the average of what exists, now with makeup on (humanwashing).

- TOUCH-UP: edit the loaded paragraphs, common flow.
- PARTIAL-REWRITE or REBUILD: rebuild.

**How to rebuild:**
1. **Extract the factual spine:** a list of claims, with sources where they exist, and none of the prose.
2. **Throw the prose away.** Do not "improve" it.
3. **Write from scratch:** angles (not text) → a justified choice → a draft with the bans already in force → **the author's own edit** (irreplaceable) → a review that points without rewriting.
4. **Inject the substance the draft lacked:** the author's own reading, a connection between fields only their background produces, the trade's precise vocabulary, a lived memory. A generic paragraph is almost never cured by style.
5. **Voice sample:** if the author has two or three paragraphs written by hand in this genre, read them first. Without a sample, say so.
6. Common flow, steps 5 to 8.

**Anti-paraphrase lock:** the structure of the new text must not mirror the draft heading by heading.

## Mode C · Audit

**Diagnosis, not editing.** The audit answers "passes or not", with quoted passages; editing comes later, with approval.

1. Batch by type: `python scripts/scan.py "texts/*.md"` gives the summary table at zero model cost.
2. Sort by points per 1,000 and open the detailed report only for PARTIAL-REWRITE or worse.
3. A finished, approved text is **never edited silently**: deliver a proposal with the quoted passage, the blacklist item and the suggested replacement.
4. **Verify before cutting:** the meter may flag as a tic something that hides a correct fact ("studies show" in place of a real source). Anonymous authority goes to **verification**, not the scissors.
5. The first audit is the **baseline**: keep the table to calibrate thresholds and measure the next round.

## Report (short)

| Field | Content |
|---|---|
| Text · language · type · mode | |
| Before → after | points per 1,000 and verdict, both sides |
| Strong hits | by rule, with counts |
| Rewritten paragraphs | lines, and **what substance came in** (the fact, the position, the connection) |
| Facts | result of the fact guard: nothing changed, or the list with reasons |
| Exceptions applied | what was kept as quotation, technical term or voice, and why |
| Status | claims reworded, "works as" kept |
| Pending for the author | approved texts, cut decisions, missing voice sample |
