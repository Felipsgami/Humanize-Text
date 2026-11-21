# Blacklist and voice rules · English (US and UK)

The language-dependent part of the method. The workflow is in `method.md`; the truth test (status), in `status-check.md`.

## Why AI text sounds like AI

A language model picks, token by token, what is statistically most likely. So AI prose is, by definition, **the most probable text** on its subject: it sits at the average of what has already been written. What is improbable disappears: the unusual but exact word, the broken rhythm, the unexpected connection, the detail only someone who was there would know.

Two measures describe this and double as positive targets:
- **Perplexity:** how surprising the word choices are. Manual test: is this the most obvious word I could put here, or an unexpected one that is still exact?
- **Burstiness:** variation in sentence length and shape. People alternate a three-word sentence with a thirty-word one; models write everything at one length.

**Do not write to fool detectors.** Detectors are unreliable, including against human writers (high false-positive rates, bias against second-language writers, and chained paraphrasing collapses their accuracy). Write this way because it is what human prose does; the detector is a poor mirror of the same thing.

**What is not slop**, and every paragraph needs at least one: a specific detail (name, date, sourced number, place), lived experience, information new to the reader, a point of view someone could disagree with.

**The five kinds of slop** (to diagnose a text that passes the list and is still dead):
1. **Generic:** stock-photo prose; it would fit any topic.
2. **Pseudo-insight:** sounds deep, says nothing new.
3. **Borrowed authority:** an expert's tone with no source shown.
4. **Encyclopedia rewrite:** the first paragraph of the encyclopedia entry, paraphrased.
5. **Wellness:** comforting, universal advice with no concrete action; the worst variant is a serious argument that ends as self-help.

## The blacklist (28 items)

Items 1 to 17 are **first order** (the classic tics); 18 to 28 are **second order** (structural tics that survive a hasty clean-up). Weight and exceptions follow.

**Openings**
1. **Era frame:** "In today's fast-paced world…", "In an ever-changing landscape…", "In the age of…", "Since the dawn of time…", "Throughout history…". Start with the fact.
2. **Immersion verb:** "Let's dive into…", "Let's delve into…", "Join me as we explore…", "Embark on a journey…", "Buckle up". Announcing instead of starting.

**Structure and transition**
3. **Serial connectors:** "Moreover", "Furthermore", "Additionally", "In addition", "On the other hand", "Ultimately" chained by reflex. Prefer a transition that carries content.
4. **Em-dash overuse:** the best-known marker of AI English. The em dash is legitimate punctuation (US style closes it up, "word—word"; UK style often uses a spaced en dash, "word – word"); density is the tell. The meter flags it when dense; for a house style that bans it, run `--dashes zero`. When replacing, choose by role (below).
5. **"It's not X, it's Y"** (and "not just X, but Y", "more than X, it's Y"): the commonest way to fake depth. **Exception:** a negation that corrects a belief **with an owner** named in the sentence ("conventional wisdom says…; Smith argues the opposite"). Without an owner it is a strawman (item 21).
6. **Semicolons chaining** what should be separate sentences.
7. **Lists where prose belongs:** an argument lives in prose; use a list only when list form is the point (spec sheet, steps, catalogue).
8. **Mechanical parallelism:** three examples whenever three fit, mirrored sentences, perfect symmetry. Break it on purpose.

**Tone and content**
9. **Clerk hedging:** "It's important to note that…", "It's worth noting…", "It should be noted that…", "Needless to say…", "in a sense", "so to speak". Cut the frame and say the thing. **Do not confuse with a caveat:** a marker that says whose idea it is, which year the data is from, or where the analogy breaks is content and stays. If the caveat adds a fact, it stays; if it only softens, it goes.
10. **Brochure words:** "fascinating", "incredible", "revolutionary", "robust", "transformative", "vibrant", "seamless", "cutting-edge", "journey", "landscape", "realm", "tapestry", "testament", "delve", "intricate", "multifaceted", "nuanced" as ornament.
11. **"Transform" with no object, direction or scale:** "…transforming the way we think". Say what, for whom and how much.
12. **Fabricated empathy:** "You're not alone", "It's okay to feel…", "Take a deep breath".
13. **Anonymous authority:** "Studies show…", "Experts agree…", "Research suggests…", "Science tells us…" without saying which. Name the source or cut it; a hit here **goes to verification**, not straight to the bin (a real source may be behind it).
14. **Riskless neutrality:** "on the one hand…, on the other…" with no position. Real hesitation is welcome; the cowardice of "it depends" is not.

**Closings**
15. **Vague closing gerund:** "…paving the way for", "…opening new possibilities", "…shaping the future of".
16. **Mechanical recap:** "In conclusion…", "To sum up…", "As we've seen…", "All in all…".
17. **Social-media call to action:** "Let me know in the comments", "Share this with someone who needs it", "Don't forget to like and subscribe".

**Second order: structure and rhythm**
18. **Dramatic fragment runs and one-line closers:** "No X. No Y. Just Z.", three or more very short sentences in a row, every paragraph ending in a punchline. The short sentence is legitimate; in runs it is a tic. At most one impact fragment per section, and it carries information.
19. **Deep-sounding proverb:** "At its core", "The real question is", "What truly matters", "At the end of the day", "The bottom line is".
20. **Scaffolding before the point:** "Here's the thing", "Here's what you need to know", "Let me break it down", "The short answer?".
21. **Arguing with no one (strawman):** refuting an objection nobody raised. If the belief has an owner, name it (item 5); if not, state the thesis.
22. **Forced triad:** three items because three sounds complete, the third decorative. If there truly are three, vary their length.

**Second order: inflation and borrowed authority**
23. **Vague connection:** "linked to", "tied to", "associated with", "the relationship between", "in dialogue with", "resonates with", "speaks to", without saying which relation. Use the real verb: cites, contradicts, derives from, measures, anticipates.
24. **Ornamental gerund:** ", highlighting", ", underscoring", ", reflecting", ", symbolizing/symbolising", ", showcasing", ", fostering". If the gerund asserts **meaning** (what something symbolizes), it is an unsourced claim and a status error too.
25. **Inflated significance:** "a pivotal moment", "an enduring legacy", "stands as a testament to", "left an indelible mark", "continues to thrive", "challenges and future prospects", "the future looks bright", "game-changer". End on the last concrete fact.
26. **Copula avoidance:** "serves as", "stands as", "boasts", "represents", "constitutes" where "is" or "has" would do. **Only switch to "is" where the source states identity.** Where the source speaks of analogy or model, "works as / functions as" stays: it is a status marker (see `status-check.md`).

**Second order: residue and form**
27. **Chatbot residue and knowledge disclaimers:** "Great question!", "I hope this helps", "Feel free to ask", "As of my last update", "While specific details are limited" followed by a guess. Declare a gap; never fill it with the probable.
28. **Reflexive formatting:** decorative bold, lists where every item opens with a bold label and a colon, Title Case Headings On Every Line, the heading repeated in the first sentence, text that talks about its previous version ("now corrected", "previously said"), emoji as bullets.

## Weight and exceptions

| Weight | Rule | Examples |
|---|---|---|
| **Strong** | one occurrence already calls for an edit | ownerless "not X but Y", interpretive gerund, "at its core", chatbot residue, era frame |
| **Weak** | counts only in clusters (3 different kinds in one paragraph, or 4 hits), because people say it | "journey", "fascinating", "landscape", "moreover", "linked to", "at the end of the day" |
| **Watch** | no evidence it is a tic; noted, not scored | "delicate balance", "shed light on", "rich tapestry" |

The weights come from counting: every candidate was measured in about 11 million words of transcribed human speech in English. Spoken habits ("at the end of the day", "here's the thing", "let me know if") are common in people and were demoted to weak; the context (series, emptiness) condemns them, and only reading decides.

**When NOT to act:**
- inside a **quotation**, a **title**, a **proper name**;
- in a passage that **discusses** the expression (this file, an article about clichés);
- in a **technical term** used technically: *paradigm* in Kuhn, *ecosystem* in ecology, *landscape* in fitness-landscape biology, *represents* in mathematics;
- **real hesitation, a genuine aside, an odd detail, mixed feelings, a dated reference:** that is voice, not a tic, and pruning it is the opposite error;
- a **caveat that adds a fact** (item 9);
- **one isolated weak hit**.

**By genre:**

| Genre | Regime | What weighs most | What does not apply |
|---|---|---|---|
| essay, column, fiction | full | fragment runs, "not X but Y", interpretive gerund, vague connection, uniform rhythm | nothing is exempt |
| script, voice-over, podcast | full, on the spoken lines only | era frame, scaffolding, empty fragments, punchline closes | chosen anaphora and short sentences are normal in speech |
| short video, caption | full; short sentences are the genre | generic hook, recap, social CTA | fragments fail only if they carry nothing |
| technical, paper, report, research | **light**: rigour first | items 9, 10, 13, interpretive gerund, chatbot residue | rhythm, triads, fragments, connectors; em dash tolerated |
| post, note, description, email, chat | full | reflexive formatting, echoed headings, chatbot, scaffolding | |

**In technical text, between "more precise" and "less AI-like", choose more precise.** Scientific prose is impersonal and dense by nature, and detectors confuse it with AI; that is not a problem to fix.

## US and UK

Pick one variant and keep it: `--variant us` or `--variant uk` makes the meter report every spelling from the other side (realize/realise, color/colour, center/centre, analyze/analyse, traveled/travelled, defense/defence, catalog/catalogue). Mixed spelling in one text is itself a sign of stitched machine output. Punctuation follows the variant too: US puts commas and full stops inside closing quotation marks and prefers double quotes; UK usually prefers single quotes and puts punctuation inside only when it belongs to the quotation.

## Em dash: choose the replacement by role

- long or explanatory aside → **parentheses**;
- reveal, definition, payoff, the "this:" that announces → **colon**;
- dramatic pause, turn → **full stop** (split the sentence);
- short aside → **commas**.

Replacing every dash with a comma produces long, slack sentences.

## What to put instead (positive techniques)

1. **Burstiness:** one short sentence, then a long one that unfolds and only then lands, then a short one. No paragraph with every sentence the same length. The short sentence is **one**, and it carries information.
2. **Perplexity:** the specific, improbable-but-exact word instead of the generic one (the technical name, the number, the trade's own word).
3. **Verifiable detail:** "a 2016 study in *Nature*", never "research".
4. **A position with an argument:** a thesis and its reason.
5. **A physical image for the abstract**, your own and not stock.
6. **Break the parallelism** nobody chose; chosen anaphora stays.
7. **Let a digression breathe** when it reveals the subject's complexity.

## Preventing costs less than fixing

- **Put the bans before generation**, at the top of the instruction, not only in the final checklist (shaping by what you reject works better than filtering afterwards).
- **Never ask for the final text in one go:** angles (not text) → a justified choice → a draft under the bans → **human editing** (the irreplaceable step) → a review that **points without rewriting** → repeat until nothing is left to point at.
- **Examples beat adjectives:** two or three passages the author wrote by hand teach tone better than any description. A sample installs voice, not substance.
- **Paraphrasing does not humanize.** Swapping words fools detectors and adds nothing. Humanizing means adding what the model lacks: the fact, the position, the image, the experience.

## Voice gate (before closing any text)

**Short text (two lines, a post): the five survivors.** (1) ownerless "not X but Y"; (2) one-line closer or fragment run; (3) em dash; (4) ornamental triad; (5) dangling gerund. If the five pass, the rest usually passes.

**Long text:**
- [ ] blacklist swept (technical text: the light-regime items only);
- [ ] em dashes within the genre's policy; spelling consistent with the chosen variant;
- [ ] burstiness: no paragraph with uniform sentence lengths;
- [ ] substance in every paragraph (detail, position, new information or own image);
- [ ] diagnosis against the five kinds of slop;
- [ ] opening on a fact, no frame; concrete closing, no vague gerund, no recap, no turn to advice;
- [ ] no anonymous authority;
- [ ] the revision added something beyond swapping words;
- [ ] script and voice-over: read aloud, no stumbling;
- [ ] **status gate too** (`status-check.md`): no text closes on the voice gate alone.

## The humanwashing test (the most important one)

Every positive technique above is, from the outside, a **signal** of humanity, and an instructed model produces signals. Installing signals over content that is still the average of what exists is **humanwashing**, and it is worse than declared slop, because it lies about what it is.

> **Signal** is what looks human. **Substance** is what only a specific author could have written. Substance first, then signal.

- [ ] With every style marker deleted from the paragraph, is anything left that is not in any summary of the topic? If not, style is doing the work the content did not do.
- [ ] Does the text's imperfection come from a real mind hesitating, or was it installed because imperfection signals authorship?
- [ ] What here is irreducibly the author's: a reading of their own, a lived memory, a connection between fields only their background produces? "The voice" is not enough, because voice can be imitated.

When a paragraph is generic, the fix is almost never stylistic: bring in the fact, the experience or the connection that was missing.
