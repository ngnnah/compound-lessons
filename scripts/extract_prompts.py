#!/usr/bin/env python3
"""Regenerate docs/PROMPTS.md from the prompts embedded in app/index.html.

The app is the source of truth; run this after editing a prompt so the docs stay in sync:
    python3 scripts/extract_prompts.py
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "app" / "index.html"
OUT = ROOT / "docs" / "PROMPTS.md"

# (title, anchor text that starts the template literal, what it's for)
PROMPTS = [
    ("Daily lessons", "const prompt=`You write one short",
     "Writes each batch of two lessons. Receives the reader's rating profile so later lessons lean toward what they rate highly."),
    ("Value lens", "const prompt=`Write one \"value lens\"",
     "Writes Lens cards: the watchlist through the questions Buffett and Munger are known for asking, in Claude's own words."),
    ("Follow-up threads", "const intro=`You are a concise study companion",
     "Leading instruction turn for follow-up questions on a highlight or a whole card. Answers are capped at about 80 words."),
]


def scan_string(s, i):
    q = s[i]; i += 1
    while s[i] != q:
        i += 2 if s[i] == "\\" else 1
    return i + 1


def scan_expr(s, i):
    depth = 1
    while True:
        c = s[i]
        if c in "\"'":
            i = scan_string(s, i); continue
        if c == "`":
            i = scan_template(s, i); continue
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return i + 1
        i += 1


def scan_template(s, i):
    i += 1
    while True:
        c = s[i]
        if c == "\\":
            i += 2; continue
        if c == "`":
            return i + 1
        if c == "$" and s[i + 1] == "{":
            i = scan_expr(s, i + 2); continue
        i += 1


def main():
    html = SRC.read_text(encoding="utf-8")
    out = ["# Prompts", "",
           "Generated from `app/index.html` by `scripts/extract_prompts.py`. Edit the prompts in the app, then rerun the script.",
           "`${...}` placeholders are filled in at runtime with the reader's watchlist, price snapshot, rating profile and history.", ""]
    for title, anchor, about in PROMPTS:
        start = html.find(anchor)
        if start < 0:
            raise SystemExit(f"Prompt not found: {title!r}. Update the anchor in this script.")
        tick = html.index("`", start)
        body = html[tick + 1: scan_template(html, tick) - 1]
        out += [f"## {title}", "", about, "", "```text", body.strip(), "```", ""]
    OUT.write_text("\n".join(out), encoding="utf-8")
    print(f"Wrote {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
