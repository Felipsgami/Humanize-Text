#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scan.py · AI-slop meter for Brazilian Portuguese and English (US and UK)

Measures the *voice* signals that make a text read as machine-written: a graded lexicon
(strong / weak / watch), sentence rhythm, structure and reflexive formatting. It points
to the most loaded paragraphs so a human (or an agent) reads those first.

It is a STARTING POINT, not a verdict and not an AI detector. A CLEAN score can still be
hollow; a high score can be a human with tics. See ../references/method.md.

USAGE
    python scan.py draft.md                      # language and text type auto-detected
    python scan.py drafts/*.md                   # batch: summary table
    python scan.py draft.md --lang en --variant uk
    python scan.py draft.md --type technical     # light regime: lexicon only, no rhythm
    python scan.py draft.md --dashes zero        # em dash becomes a hard rule
    python scan.py draft.md --json | --detail
    python scan.py --facts BEFORE.md AFTER.md    # no fact may enter or leave unrecorded
    python scan.py --validate-lexicon CORPUS_DIR --lang en
                                                 # density of each rule in human text

TYPES: general (default: posts, notes, emails, descriptions) · literary (essay, fiction)
       script (reads only lines labelled NARRATION/NARRAÇÃO/VO when present) · short
       chat · technical (papers, reports, research: lexicon only, no rhythm checks)

NOT COUNTED: quotations, > blocks, headings, italics (titles, foreign terms), code,
tables, front matter, the references section.
"""
import argparse, glob, json, os, random, re, statistics, sys
from collections import defaultdict

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

HERE = os.path.dirname(os.path.abspath(__file__))

TYPES = {
    "general":   dict(rhythm=True,  close=0.45, triad=4.0, conn=3.0, flat=0.40, frag=3, bold=True),
    "literary":  dict(rhythm=True,  close=0.45, triad=4.0, conn=3.0, flat=0.40, frag=3, bold=True),
    "script":    dict(rhythm=True,  close=0.60, triad=5.0, conn=4.0, flat=0.50, frag=4, bold=False),
    "short":     dict(rhythm=True,  close=0.75, triad=6.0, conn=6.0, flat=0.70, frag=5, bold=False),
    "chat":      dict(rhythm=True,  close=0.45, triad=4.0, conn=3.0, flat=0.40, frag=3, bold=True),
    "technical": dict(rhythm=False, close=1.0,  triad=99,  conn=99,  flat=1.0,  frag=99, bold=False),
}

LANG = {
    "pt": dict(
        lexicon="lexicon_pt-BR.tsv",
        triad=r"\b[\wÀ-ÿ-]+, [\wÀ-ÿ-]+ e [\wÀ-ÿ-]+\b",
        conn=r"(?:^|[.!?] )(?:além disso|por outro lado|por fim|em suma|ou seja|portanto|dessa forma|nesse sentido),?",
        negfrag=r"(?:^|[.!?] )(sem|nenhum[a]?|nem|nada de) [^.!?]{1,30}[.!?]\s+\1 ",
        cue=r"\b(muitos|muita gente|alguns|dizem|costuma|se diz|se pensa|acham|acredit\w*|segundo|senso comum|"
            r"tradi[çc][ãa]o|sustenta|afirma|escreve|argumenta|defende|imagin\w*)\b",
        skip={"e", "mas", "ou", "que"},
        refs=r"refer[êe]ncias?|bibliografia|fontes|obras citadas",
        narr=r"narra[çc][ãa]o|locu[çc][ãa]o|off",
        stop={"que", "não", "uma", "você", "isso", "com", "para", "mais", "como", "mas", "dos", "das", "são"},
    ),
    "en": dict(
        lexicon="lexicon_en.tsv",
        triad=r"\b[\w'-]+, [\w'-]+,? and [\w'-]+\b",
        conn=r"(?:^|[.!?] )(?:moreover|furthermore|additionally|in addition|on the other hand|in conclusion|"
             r"ultimately|that said|as such|consequently|overall),?",
        negfrag=r"(?:^|[.!?] )(no|not|without|never) [^.!?]{1,30}[.!?]\s+\1 ",
        cue=r"\b(many|some (?:people|critics|scholars)|they say|it is often|conventional wisdom|commonly|"
            r"argues?|claims?|writes?|believes?|according to|tradition|insists?)\b",
        skip={"and", "but", "or", "so"},
        refs=r"references|bibliography|sources|works cited|notes",
        narr=r"narration|voice-?over|vo",
        stop={"the", "and", "you", "that", "this", "with", "for", "are", "was", "have", "not", "but", "they"},
    ),
}

# US / UK spelling pairs (regex for the US form, regex for the UK form)
SPELL = [
    (r"\b(?:real|organ|recogn|emphas|summar|categor|priorit|minim|maxim|special|apolog|critic|util|optim|standard|character|visual|final|global)iz(?:e|es|ed|ing|ation)\b",
     r"\b(?:real|organ|recogn|emphas|summar|categor|priorit|minim|maxim|special|apolog|critic|util|optim|standard|character|visual|final|global)is(?:e|es|ed|ing|ation)\b"),
    (r"\banalyz(?:e|es|ed|ing)\b", r"\banalys(?:e|es|ed|ing)\b"),
    (r"\b(?:col|behavi|fav|hon|lab|neighb|hum|flav|harb|rum|endeav)or(?:s|ed|ing|ite|ites|able)?\b",
     r"\b(?:col|behavi|fav|hon|lab|neighb|hum|flav|harb|rum|endeav)our(?:s|ed|ing|ite|ites|able)?\b"),
    (r"\b(?:cent|met|theat|fib|calib)er(?:s)?\b", r"\b(?:cent|met|theat|fib|calib)re(?:s)?\b"),
    (r"\b(?:defen|offen|licen)se\b", r"\b(?:defen|offen|licen)ce\b"),
    (r"\b(?:travel|cancel|model|label|signal)(?:ed|ing|er)\b", r"\b(?:travel|cancel|model|label|signal)l(?:ed|ing|er)\b"),
    (r"\b(?:catalog|dialog|analog)\b", r"\b(?:catalogue|dialogue|analogue)\b"),
]


def detect_lang(text):
    w = re.findall(r"[a-zà-ÿ]+", text.lower()[:20000])
    pt = sum(x in LANG["pt"]["stop"] for x in w)
    en = sum(x in LANG["en"]["stop"] for x in w)
    return "en" if en > pt else "pt"


def load_lexicon(lang):
    rules = []
    path = os.path.join(HERE, LANG[lang]["lexicon"])
    with open(path, encoding="utf-8") as f:
        for n, line in enumerate(f, 1):
            line = line.rstrip("\n")
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            p = line.split(" ::: ")
            if len(p) < 4:
                continue
            tier, rid, applies, rx = [x.strip() for x in p[:4]]
            try:
                cre = re.compile(rx, re.I)
            except re.error as e:
                print(f"WARNING: bad regex in {os.path.basename(path)} line {n} ({rid}): {e}", file=sys.stderr)
                continue
            rules.append(dict(tier=tier, id=rid, applies=applies, rx=cre, note=p[4].strip() if len(p) > 4 else ""))
    return rules


def applies_to(rule, typ):
    a = rule["applies"]
    if a == "all":
        return True
    if a == "no-technical":
        return typ != "technical"
    return typ in [x.strip() for x in a.split(",")]


def type_from_name(path):
    n = os.path.basename(path).lower()
    if re.search(r"artig|article|paper|report|relat|pesquisa|research|dossi|brief", n):
        return "technical"
    if re.search(r"ensaio|essay|conto|story|fiction|cr[ôo]nica", n):
        return "literary"
    if re.search(r"roteiro|script|screenplay", n):
        return "script"
    if re.search(r"curto|short|reel|tiktok", n):
        return "short"
    return "general"


BULLET = re.compile(r"^\s*(?:[-*+]|\d+[.)])\s+")


def paragraphs(text, typ, L):
    lines = text.split("\n")
    i = 0
    if lines and lines[0].strip() == "---":
        for j in range(1, len(lines)):
            if lines[j].strip() == "---":
                i = j + 1
                break
    refs = re.compile(r"^#{1,6}\s*\**\s*(?:" + L["refs"] + r")\b", re.I)
    narr = re.compile(r"^\**\s*(?:" + L["narr"] + r")\s*\**\s*:\**\s*(.*)$", re.I)
    has_narr = typ in ("script", "short") and any(narr.match(x.strip()) for x in lines)
    out, heads, buf, start, incode = [], [], [], None, False

    def flush():
        nonlocal buf, start
        if buf:
            out.append((start, " ".join(buf).strip(), False))
        buf, start = [], None

    for n in range(i, len(lines)):
        s = lines[n].strip()
        if s.startswith("```"):
            flush(); incode = not incode; continue
        if incode:
            continue
        if refs.match(s):
            break
        if has_narr:
            m = narr.match(s)
            if m and m.group(1).strip():
                out.append((n + 1, m.group(1).strip().strip('*"“”'), False))
            continue
        if not s:
            flush(); continue
        if s.startswith("#"):
            flush(); heads.append([n + 1, s.lstrip("#").strip(), None]); continue
        if s.startswith("|") or s.startswith(">") or re.match(r"^[-*_]{3,}$", s):
            flush(); continue
        if BULLET.match(s):
            flush(); out.append((n + 1, BULLET.sub("", s), True)); continue
        if not buf:
            start = n + 1
        buf.append(s)
    flush()
    for h in heads:
        for (ln, tx, is_list) in out:
            if ln > h[0] and not is_list:
                h[2] = tx
                break
    return out, heads


def unbold(t):
    return re.sub(r"\*\*(.+?)\*\*", r"\1", t)


def mask(plain, typ):
    m = re.sub(r"(?<!\*)\*(?!\*)([^*\n]{2,90}?)(?<!\*)\*(?!\*)", lambda x: " " * len(x.group(0)), plain)
    m = re.sub(r"“[^”]{6,600}”|«[^»]{6,600}»|‘[^’]{6,600}’", lambda x: " " * len(x.group(0)), m)
    if typ not in ("script", "short"):
        m = re.sub(r'"[^"\n]{8,400}"', lambda x: " " * len(x.group(0)), m)
    return re.sub(r"`[^`]+`", lambda x: " " * len(x.group(0)), m)


def sentences(t):
    return [f for f in re.split(r"(?<=[.!?…])\s+", t) if f.strip()]


def nwords(t):
    return len(re.findall(r"[A-Za-zÀ-ÿ0-9'’-]+", t))


def analyse(path, typ=None, lang=None, dashes="signal", variant=None):
    text = open(path, encoding="utf-8", errors="ignore").read()
    lang = lang or detect_lang(text)
    L = LANG[lang]
    typ = typ or type_from_name(path)
    cfg = TYPES[typ]
    rules = load_lexicon(lang)
    paras, heads = paragraphs(text, typ, L)
    r = dict(file=os.path.basename(path), lang=lang, type=typ, words=0, hits=defaultdict(list),
             structure={}, loaded=[], points=0, per_1000=0.0, verdict="", hard_rules=[])
    prose = [(ln, t) for (ln, t, is_list) in paras if not is_list]
    r["words"] = sum(nwords(t) for (_, t, _) in paras)
    per_par = defaultdict(float)
    weak_par = defaultdict(list)
    cue = re.compile(L["cue"], re.I)

    for (ln, t, _) in paras:
        plain = unbold(t)
        msk = mask(plain, typ)
        for rg in rules:
            if not applies_to(rg, typ):
                continue
            for m in rg["rx"].finditer(msk):
                snippet = plain[max(0, m.start() - 40):m.end() + 40].replace("\n", " ").strip()
                tier, note = rg["tier"], ""
                if rg["id"] in ("nao-e-x-e-y", "not-x-but-y") and cue.search(msk[max(0, m.start() - 90):m.start() + 20]):
                    tier, note = "watch", "(belief with an owner)"
                r["hits"][tier].append(dict(id=rg["id"], line=ln, snippet=snippet + (" " + note if note else "")))
                if tier == "strong":
                    per_par[ln] += 3
                elif tier == "weak":
                    weak_par[ln].append(rg["id"])
    weak_scored = 0
    for ln, ids in weak_par.items():
        if len(set(ids)) >= 3 or len(ids) >= 4:
            weak_scored += len(ids)
            per_par[ln] += len(ids)
    r["weak_in_clusters"] = weak_scored

    st = r["structure"]
    plain_all = [unbold(t) for (_, t) in prose]
    n_dash = sum(t.count("—") + t.count(" -- ") + len(re.findall(r"\s–\s", t)) for t in plain_all)
    st["em_dashes"] = n_dash
    pts = 0.0
    if cfg["rhythm"] and prose:
        flat = elig = closes = close_elig = frag_runs = open_runs = 0
        for (ln, t) in prose:
            fs = sentences(unbold(t))
            lens = [nwords(f) for f in fs]
            if len(fs) >= 4:
                elig += 1
                mean = statistics.mean(lens)
                if mean and statistics.pstdev(lens) / mean < 0.30:
                    flat += 1; per_par[ln] += 2
            if len(fs) >= 3:
                close_elig += 1
                closes += lens[-1] <= 6
            run = 0
            for n in lens + [99]:
                if n <= 4:
                    run += 1
                else:
                    if run >= cfg["frag"]:
                        frag_runs += 1; per_par[ln] += 2
                    run = 0
            if re.search(L["negfrag"], unbold(t), re.I):
                frag_runs += 1; per_par[ln] += 2
            starts = [re.sub(r"\W", "", f.split()[0].lower()) for f in fs if f.split()]
            run = 1
            for a in range(1, len(starts) + 1):
                if a < len(starts) and starts[a] == starts[a - 1] and starts[a] not in L["skip"]:
                    run += 1
                else:
                    if run >= 3:
                        open_runs += 1; per_par[ln] += 2
                    run = 1
        st["flat_paragraphs"] = f"{flat} of {elig} eligible"
        st["fragment_runs"] = frag_runs
        st["repeated_openings"] = open_runs
        st["punchline_closes_%"] = round(100 * closes / max(close_elig, 1))
        pw = max(sum(nwords(t) for t in plain_all), 1)
        st["triads_per_1000"] = round(1000 * sum(len(re.findall(L["triad"], t)) for t in plain_all) / pw, 1)
        st["connectors_per_1000"] = round(1000 * sum(len(re.findall(L["conn"], t, re.I)) for t in plain_all) / pw, 1)
        flags = []
        if elig >= 4 and flat / elig > cfg["flat"]:
            flags.append("uniform-rhythm")
        if close_elig >= 4 and closes / close_elig > cfg["close"]:
            flags.append("punchline-closes")
        if st["triads_per_1000"] > cfg["triad"]:
            flags.append("triads")
        if st["connectors_per_1000"] > cfg["conn"]:
            flags.append("serial-connectors")
        st["flags"] = flags
        pts += 4 * len(flags) + 2 * frag_runs + 2 * open_runs
    if cfg["bold"]:
        raw = " ".join(t for (_, t, _) in paras)
        st["bold_per_1000"] = round(1000 * len(re.findall(r"\*\*[^*\n]+\*\*", raw)) / max(r["words"], 1), 1)
        st["bold_label_lists"] = len(re.findall(r"^\s*[-*+]\s+\*\*[^*\n]+\*\*", text, re.M))
        if st["bold_per_1000"] > 8:
            st.setdefault("flags", []).append("decorative-bold"); pts += 4
        if st["bold_label_lists"] >= 3:
            st.setdefault("flags", []).append("bold-label-lists"); pts += 4
    if typ in ("general", "technical"):
        rep = 0
        for (ln, h, nxt) in heads:
            if not nxt:
                continue
            first = sentences(nxt)[0] if sentences(nxt) else ""
            a, b = set(re.findall(r"\w{4,}", h.lower())), set(re.findall(r"\w{4,}", first.lower()))
            if a and nwords(first) <= 9 and len(a & b) / len(a) >= 0.6:
                rep += 1
        st["heading_echoed_in_first_sentence"] = rep
        pts += 2 * rep
    if lang == "en":
        title_case = [h for (_, h, _) in heads if len(h.split()) >= 4 and
                      sum(w[:1].isupper() for w in h.split() if len(w) > 3) == len([w for w in h.split() if len(w) > 3])]
        st["title_case_headings"] = len(title_case)
        if len(title_case) >= 3 and typ != "technical":
            st.setdefault("flags", []).append("title-case-headings"); pts += 2
        us = sum(len(re.findall(a, text, re.I)) for a, _ in SPELL)
        uk = sum(len(re.findall(b, text, re.I)) for _, b in SPELL)
        st["spelling_us_uk"] = f"{us}/{uk}"
        if us and uk:
            st.setdefault("flags", []).append("mixed-us-uk-spelling")
        if variant == "us" and uk:
            r["hard_rules"].append(f"{uk} British spelling(s) in a US text")
        if variant == "uk" and us:
            r["hard_rules"].append(f"{us} American spelling(s) in a UK text")
    density = 1000 * n_dash / max(r["words"], 1)
    if dashes == "zero" and n_dash:
        r["hard_rules"].append(f"{n_dash} em dash(es) (limit is zero)")
        pts += min(n_dash, 20)
    elif dashes == "signal" and typ != "technical" and density > 3:
        st.setdefault("flags", []).append("dense-em-dashes")
        pts += min(n_dash, 20)

    strong = len(r["hits"].get("strong", []))
    r["points"] = pts = 3 * strong + weak_scored + pts
    r["per_1000"] = pm = round(1000 * pts / max(r["words"], 1), 1)
    if typ == "technical":
        r["verdict"] = "CLEAN" if pm < 8 else ("TOUCH-UP" if pm < 20 else "DEEP-CLEAN")
    else:
        r["verdict"] = "CLEAN" if pm < 6 else "TOUCH-UP" if pm < 15 else "PARTIAL-REWRITE" if pm < 30 else "REBUILD"
    top = sorted(per_par.items(), key=lambda x: -x[1])[:5]
    lookup = {ln: t for (ln, t, _) in paras}
    r["loaded"] = [dict(line=ln, points=p, opens=lookup.get(ln, "")[:110]) for ln, p in top if p > 0]
    r["hits"] = dict(r["hits"])
    return r


def show(r, detail=True):
    h = r["hits"]
    print("\n" + "=" * 78)
    print(f"{r['file']}  [{r['lang']} · {r['type']}]")
    print(f"  {r['words']} words · strong {len(h.get('strong', []))} · weak {len(h.get('weak', []))} "
          f"(in clusters: {r['weak_in_clusters']}) · watch {len(h.get('watch', []))} · {r['per_1000']} pts/1000 · {r['verdict']}")
    if r["hard_rules"]:
        print("  HARD RULE BROKEN: " + "; ".join(r["hard_rules"]))
    s = r["structure"]
    if s:
        print("  structure: " + " · ".join(f"{k}={v}" for k, v in s.items() if k != "flags"))
        if s.get("flags"):
            print("  FLAGS: " + ", ".join(s["flags"]))
    if not detail:
        return
    for tier in ("strong", "weak", "watch"):
        items = h.get(tier, [])
        if not items:
            continue
        by = defaultdict(list)
        for x in items:
            by[x["id"]].append(x)
        print(f"\n  [{tier.upper()}] {len(items)}")
        for rid, xs in sorted(by.items(), key=lambda kv: -len(kv[1]))[:10 if tier == "strong" else 4]:
            print(f"     {rid} ×{len(xs)} · line {xs[0]['line']}: …{xs[0]['snippet']}…")
    if r["loaded"]:
        print("\n  MOST LOADED PARAGRAPHS (read these first):")
        for p in r["loaded"]:
            print(f"     line {p['line']} · {p['points']:.0f} pts · {p['opens']}…")


def facts(text):
    t = re.sub(r"^---.*?---", "", text, count=1, flags=re.S)
    lower = set(re.findall(r"\b[a-zà-ÿ]{3,}\b", t))
    cap = set(re.findall(r"\b[A-ZÀ-Ý][a-zà-ÿ]{2,}\b", t))
    return {"numbers": set(re.findall(r"\d[\d.,]*\d|\d", t)),
            "dois": set(re.findall(r"10\.\d{4,9}/[-._;()/:A-Za-z0-9]+", t)),
            "urls": set(re.findall(r"https?://[^\s)>\]]+", t)),
            "latex": set(re.findall(r"\$[^$\n]+\$", t)),
            "names": {w for w in cap if w.lower() not in lower}}


def compare_facts(before, after):
    tb = open(before, encoding="utf-8", errors="ignore").read()
    ta = open(after, encoding="utf-8", errors="ignore").read()
    B, A = facts(tb), facts(ta)
    same = True
    print(f"\nFACT DIFF  {os.path.basename(before)}  →  {os.path.basename(after)}")
    for k in ("numbers", "dois", "urls", "latex", "names"):
        gone, new = sorted(B[k] - A[k]), sorted(A[k] - B[k])
        if k == "names":  # a reordered sentence capitalises an ordinary word: not a new name
            exists = lambda w, t: re.search(r"(?<!\w)" + re.escape(w) + r"(?!\w)", t, flags=re.I)
            new = [w for w in new if not exists(w, tb)]
            gone = [w for w in gone if not exists(w, ta)]
        same &= not (gone or new)
        print(f"  [{k}] removed {len(gone)} · added {len(new)}")
        if gone:
            print("     removed: " + ", ".join(gone[:12]) + (" …" if len(gone) > 12 else ""))
        if new:
            print("     ADDED (check the origin of each): " + ", ".join(new[:12]) + (" …" if len(new) > 12 else ""))
    print("  " + ("No fact changed." if same else "Facts changed: every item above needs a justification."))


def validate_lexicon(folder, lang, n, exclude=None):
    """Density of each rule in human text. Use transcripts of people talking (video, podcast,
    interview) or human prose from before 2022. --exclude takes a file listing bad transcripts
    (one path per line; tab-separated lines use the last column), matched by folder/file name."""
    random.seed(7)
    skip = set()
    if exclude:
        for line in open(exclude, encoding="utf-8", errors="ignore"):
            p = line.rstrip("\n").split("\t")[-1].replace("\\", "/").strip()
            if p:
                skip.add("/".join(p.split("/")[-2:]).lower())
    files = [p for ext in ("md", "txt") for p in glob.glob(os.path.join(folder, "**", "*." + ext), recursive=True)
             if os.path.getsize(p) > 3000
             and "/".join(p.replace("\\", "/").split("/")[-2:]).lower() not in skip]
    random.shuffle(files)
    rules, counts, total, used = load_lexicon(lang), defaultdict(int), 0, 0
    for p in files:
        if used >= n:
            break
        t = open(p, encoding="utf-8", errors="ignore").read()
        if detect_lang(t) != lang:
            continue
        used += 1
        total += len(re.findall(r"\w+", t))
        for rg in rules:
            counts[rg["id"]] += len(rg["rx"].findall(t))
    print(f"Human corpus ({lang}): {used} files, {total} words\n{'tier':<8} {'rule':<34} {'per million':>11}")
    for rg in rules:
        pm = counts[rg["id"]] / max(total, 1) * 1e6
        warn = "  ← above 5: should not be 'strong' unless it is an editorial rule" if rg["tier"] == "strong" and pm > 5 else ""
        print(f"{rg['tier']:<8} {rg['id']:<34} {pm:>11.1f}{warn}")


def main():
    ap = argparse.ArgumentParser(description="AI-slop meter (pt-BR / en-US / en-GB)")
    ap.add_argument("files", nargs="*")
    ap.add_argument("--lang", choices=["pt", "en"])
    ap.add_argument("--variant", choices=["us", "uk"], help="English spelling the text must follow")
    ap.add_argument("--type", choices=list(TYPES))
    ap.add_argument("--dashes", choices=["signal", "zero", "ignore"], default="signal")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--detail", action="store_true")
    ap.add_argument("--facts", nargs=2, metavar=("BEFORE", "AFTER"))
    ap.add_argument("--validate-lexicon", metavar="CORPUS_DIR")
    ap.add_argument("--sample", type=int, default=2500)
    ap.add_argument("--exclude", metavar="LIST", help="file listing low-quality transcripts to leave out")
    a = ap.parse_args()
    if a.facts:
        return compare_facts(*a.facts)
    if a.validate_lexicon:
        return validate_lexicon(a.validate_lexicon, a.lang or "pt", a.sample, a.exclude)
    if not a.files:
        ap.error("give a file (or --facts, or --validate-lexicon)")
    targets = []
    for f in a.files:
        targets += sorted(glob.glob(f)) if any(c in f for c in "*?") else [f]
    res = [analyse(f, a.type, a.lang, a.dashes, a.variant) for f in targets]
    if a.json:
        return print(json.dumps(res, ensure_ascii=False, indent=1))
    if len(res) == 1 or a.detail:
        for r in res:
            show(r)
        return
    print(f"{'file':<34} {'lang':<4} {'type':<9} {'words':>6} {'strong':>6} {'weak':>5} {'flags':>5} {'pts/1k':>7}  verdict")
    for r in res:
        print(f"{r['file'][:34]:<34} {r['lang']:<4} {r['type']:<9} {r['words']:>6} {len(r['hits'].get('strong', [])):>6} "
              f"{r['weak_in_clusters']:>5} {len(r['structure'].get('flags', [])):>5} {r['per_1000']:>7}  "
              f"{r['verdict']}{' +HARD-RULE' if r['hard_rules'] else ''}")


if __name__ == "__main__":
    main()
