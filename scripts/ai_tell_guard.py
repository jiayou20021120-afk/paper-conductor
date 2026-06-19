#!/usr/bin/env python3
"""ai_tell_guard — deterministic AI-tell / hard-rule linter for Chinese academic drafts.

This is paper-conductor's stage-5/8 guard. It does NOT ask a model to "self-check";
it runs fixed rules so the same draft always gets the same verdict, with zero tokens.

Hard rules (FAIL, block the stage):
  - em-dash family (— ― ⸺ ⸻ and "——"): the single strongest LLM fingerprint in CN prose.
  - straight quotes (" ' ` " ') where curly 「」""'' are expected.

Soft rules (WARN, surface but do not block):
  - "本文" density above ~1 per 1000 chars (paper-humanlike ceiling).
  - machine-tell filler words and enumeration scaffolding.
  - heavy full-width parenthesis use (prefer 即 / 也就是 inline).
  - over-long sentences (a cognitive-load tell, not an AI tell): split them.
  - high-barrier / translationese terms whose first use lacks a plain anchor.

Inputs: .txt, .md, or .docx (docx text is extracted with the stdlib only, no deps).
Usage:
  python ai_tell_guard.py draft.docx
  python ai_tell_guard.py draft.md --markdown
  cat draft.txt | python ai_tell_guard.py -        # read from stdin
Exit code is 1 if any FAIL is found, else 0, so it can gate a pipeline.
"""

import argparse
import re
import sys
import zipfile

# ----- text extraction ------------------------------------------------------

def read_text(path: str) -> str:
    if path == "-":
        return sys.stdin.read()
    if path.lower().endswith(".docx"):
        return _docx_text(path)
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        return f.read()


def _docx_text(path: str) -> str:
    """Extract visible text from a .docx using only the stdlib.

    A .docx is a zip; word/document.xml holds the runs. We turn paragraph and
    line breaks into newlines so line numbers in the report are meaningful.
    """
    with zipfile.ZipFile(path) as z:
        xml = z.read("word/document.xml").decode("utf-8", errors="replace")
    # turn structure into newlines BEFORE stripping tags so line numbers survive
    xml = re.sub(r"</w:p>", "\n", xml)
    xml = re.sub(r"<w:br[^>]*/?>", "\n", xml)
    xml = re.sub(r"<w:tab[^>]*/?>", "\t", xml)
    # drop every tag; only <w:t> text and the newlines we inserted remain
    body = re.sub(r"<[^>]+>", "", xml)
    return (
        body.replace("&amp;", "&")
        .replace("&lt;", "<")
        .replace("&gt;", ">")
        .replace("&quot;", '"')
        .replace("&apos;", "'")
    )


# ----- rules ----------------------------------------------------------------

# readability (cognitive-load) threshold — tune freely
LONG_SENTENCE_CHARS = 60  # a CN academic sentence past this reads as a run-on

EM_DASHES = {
    "—": "EM DASH —",
    "―": "HORIZONTAL BAR ―",
    "⸺": "TWO-EM DASH ⸺",
    "⸻": "THREE-EM DASH ⸻",
}

STRAIGHT_QUOTES = {'"': "straight double quote", "'": "straight single quote"}


def _is_cjk(c: str) -> bool:
    if not c:
        return False
    o = ord(c)
    return (
        0x3000 <= o <= 0x303F      # CJK punctuation （，。：「」etc.）
        or 0x3400 <= o <= 0x9FFF   # CJK ideographs (+ ext A)
        or 0xF900 <= o <= 0xFAFF   # compatibility ideographs
        or 0xFF00 <= o <= 0xFFEF   # fullwidth forms
    )

FILLER = [
    "值得注意的是", "总而言之", "综上所述", "总的来说", "众所周知",
    "不言而喻", "显而易见", "毋庸置疑", "不难发现", "由此可见",
    "起到了至关重要的作用", "具有重要的意义", "发挥着重要作用",
    "日新月异", "长足的发展", "保驾护航", "添砖加瓦",
]

# 须字辈合规旁白腔：边界该藏进转折式行文（这虽有助于…但也容易…），别明着声明
XU_BOUNDARY = [
    "须注意", "须说明", "须强调", "须指出", "还须澄清", "还需说明",
    "需要交代", "需指出", "需说明", "特别申明", "须看到", "应当指出", "应当看到",
]

# 元叙述 / 过渡腔："我接下来要说 X" 的句子，直接陈述即可
META_NARRATIVE = [
    "说得直白些", "值得多看一眼", "这里容易读错", "接下来将", "下面将",
    "下文将", "本文将", "本节将", "本部分将", "如前所述", "如上所述",
    "正如前文", "正如前所述",
]

# 评论 / 散文递进笔法：混进论证节就是 AI 指纹
ESSAYISTIC = ["再往深处看", "往深处看", "真正的问题或许是", "更进一步看", "细想之下"]

ENUM = ["首先，", "其次，", "再次，", "最后，", "一方面，", "另一方面，",
        "其一，", "其二，", "其三，"]

# 设问悬置：研究问题可用问号，但论证中段问完立答（自问自答）比不问更糟
RHET_Q_OPENERS = ["那么，", "难道", "试问", "不禁要问", "我们不禁", "为什么呢"]

# 高门槛 / 翻译腔术语：词本身可能没错，但首次出现该给一句人话锚点。
# 这是 heuristic 且领域相关——计量/统计稿里「共变」「删失」属正常术语，
# 嫌吵就删掉本列表，长句检测与硬规则都不受影响。
JARGON_ANCHOR = ["右删失", "同侪生产", "能见度", "精化", "拉尖", "共变", "同形", "部均"]


def _is_code_fence_line(line: str) -> bool:
    return line.lstrip().startswith("```") or line.lstrip().startswith("    ")


def scan(text: str):
    lines = text.splitlines()
    findings = []  # (severity, rule, line_no, message, snippet)
    in_fence = False

    for i, line in enumerate(lines, 1):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue

        for ch, name in EM_DASHES.items():
            if ch in line:
                findings.append(("FAIL", "em-dash", i, f"{name} present", line.strip()[:80]))
        if "——" in line and "—" not in line:
            findings.append(("FAIL", "em-dash", i, "double em-dash —— present", line.strip()[:80]))

        for ch, name in STRAIGHT_QUOTES.items():
            # only flag a straight quote that sits next to Chinese; ASCII/code
            # contexts (e.g. version: "0.4.0", English quotes) are left alone
            n = 0
            for pos, c in enumerate(line):
                if c != ch:
                    continue
                prev = line[pos - 1] if pos > 0 else ""
                nxt = line[pos + 1] if pos + 1 < len(line) else ""
                if _is_cjk(prev) or _is_cjk(nxt):
                    n += 1
            if n:
                findings.append(("FAIL", "straight-quote", i, f"{n}x {name} 紧邻中文 (use 「」/“”/‘’)", line.strip()[:80]))

        for words, rule, label in (
            (FILLER, "filler", "machine-tell phrase"),
            (XU_BOUNDARY, "须字辈", "boundary-declaration tone"),
            (META_NARRATIVE, "元叙述", "metanarrative / I-am-about-to-say"),
            (ESSAYISTIC, "评论笔法", "essayistic move in an argument section"),
            (ENUM, "enumeration", "enumeration scaffolding"),
            (RHET_Q_OPENERS, "设问", "rhetorical-question opener"),
        ):
            for w in words:
                if w in line:
                    findings.append(("WARN", rule, i, f"{label}: {w}", line.strip()[:80]))

        # 自问自答：同一行里 ？后面还跟着实质内容（问完立答），论证中段是 AI 指纹
        for pos, c in enumerate(line):
            if c != "？":
                continue
            tail = re.sub(r"\s", "", line[pos + 1:])
            if len(tail) >= 5:
                findings.append(("WARN", "自问自答", i, "设问后紧接作答（论证段慎用）", line.strip()[:80]))
                break

        fw_paren = line.count("（")
        if fw_paren >= 2:
            findings.append(("WARN", "parentheses", i, f"{fw_paren} full-width parens on one line (prefer 即/也就是)", line.strip()[:80]))

        # 超长句：按句末标点切，去空白后字数超阈值就 WARN（认知负荷，非 AI 指纹）
        for seg in re.split(r"[。！？；]", line):
            s = re.sub(r"\s", "", seg)
            if len(s) > LONG_SENTENCE_CHARS:
                findings.append(("WARN", "长句", i,
                                 f"单句 {len(s)} 字 > {LONG_SENTENCE_CHARS}（拆成框架句+逐条定义）", s[:40]))

    # document-level: 本文 density
    chars = len(re.sub(r"\s", "", text))
    benwen = text.count("本文")
    density = (benwen / chars * 1000) if chars else 0.0
    if density > 1.0:
        findings.append(("WARN", "本文-density", 0,
                         f"本文 appears {benwen}x ≈ {density:.2f}/1000 chars (ceiling ~1.0)", ""))

    # document-level: 高门槛术语首现是否给了人话锚点（heuristic, 见 JARGON_ANCHOR 注释）
    for term in JARGON_ANCHOR:
        n = text.count(term)
        if n:
            findings.append(("WARN", "术语锚点", 0,
                             f"高门槛术语「{term}」出现 {n}x，确认首现给了人话注释", ""))

    return findings, {"chars": chars, "benwen": benwen, "density": density}


# ----- reporting ------------------------------------------------------------

def report_text(findings, stats):
    fails = [f for f in findings if f[0] == "FAIL"]
    warns = [f for f in findings if f[0] == "WARN"]
    out = []
    out.append(f"ai_tell_guard: {len(fails)} FAIL, {len(warns)} WARN "
               f"(chars={stats['chars']}, 本文={stats['benwen']}, "
               f"本文/千字={stats['density']:.2f})")
    for sev, rule, ln, msg, snip in findings:
        loc = f"L{ln}" if ln else "doc"
        line = f"  [{sev}] {loc} {rule}: {msg}"
        if snip:
            line += f"  | {snip}"
        out.append(line)
    out.append("VERDICT: " + ("FAIL" if fails else "PASS"))
    return "\n".join(out)


def report_markdown(findings, stats):
    fails = [f for f in findings if f[0] == "FAIL"]
    warns = [f for f in findings if f[0] == "WARN"]
    out = [f"# ai_tell_guard report",
           "",
           f"- FAIL: **{len(fails)}** · WARN: **{len(warns)}**",
           f"- chars: {stats['chars']} · 本文: {stats['benwen']} · 本文/千字: {stats['density']:.2f}",
           f"- VERDICT: **{'FAIL' if fails else 'PASS'}**",
           ""]
    if findings:
        out += ["| sev | loc | rule | message | snippet |",
                "|---|---|---|---|---|"]
        for sev, rule, ln, msg, snip in findings:
            loc = f"L{ln}" if ln else "doc"
            snip = snip.replace("|", "\\|")
            out.append(f"| {sev} | {loc} | {rule} | {msg} | {snip} |")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(description="Deterministic AI-tell / hard-rule guard for CN drafts.")
    ap.add_argument("path", help="draft file (.txt/.md/.docx) or - for stdin")
    ap.add_argument("--markdown", action="store_true", help="emit a markdown report")
    args = ap.parse_args()

    text = read_text(args.path)
    findings, stats = scan(text)
    print(report_markdown(findings, stats) if args.markdown else report_text(findings, stats))
    sys.exit(1 if any(f[0] == "FAIL" for f in findings) else 0)


if __name__ == "__main__":
    main()
