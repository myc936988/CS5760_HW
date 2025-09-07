
# Q2 tokenization — no external libs; rule-based tokenizer + comparisons
# Author: YOU
# Usage: python tokenization.py

import re, pathlib, json

TEXT_PATH = pathlib.Path(__file__).with_name("sample_text.txt")
text = TEXT_PATH.read_text(encoding="utf-8")

def space_tokenize(s):
    return s.split()

def manual_tokenize(s):
    # protect email-like spans
    protected = {}
    def repl(m):
        key = f"<EMAIL{len(protected)}>"
        protected[key] = m.group(0)
        return f" {key} "
    s2 = re.sub(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", repl, s)

    # separate common punctuations (keep Unicode dashes/quotes)
    s2 = re.sub(r"([“”\"'()\-—–:.,!?])", r" \1 ", s2)
    # normalize spaces
    s2 = re.sub(r"\s+", " ", s2).strip()
    toks = s2.split()

    # restore protected spans
    toks = [protected.get(t, t) for t in toks]
    return toks

def rule_based_tool(s):
    # A slightly different rule set to emulate a "tool" tokenizer
    s2 = re.sub(r"([():,!?])", r" \1 ", s)           # only ASCII punct
    s2 = re.sub(r"\s+", " ", s2).strip()
    toks = s2.split()
    return toks

space_tokens  = space_tokenize(text)
manual_tokens = manual_tokenize(text)
tool_tokens   = rule_based_tool(text)

# Compute diffs (indices where different, up to 20 shown)
diffs = []
for i in range(max(len(manual_tokens), len(tool_tokens))):
    m = manual_tokens[i] if i < len(manual_tokens) else None
    t = tool_tokens[i]  if i < len(tool_tokens)  else None
    if m != t:
        diffs.append((i, m, t))
        if len(diffs) >= 20: break

out = {
    "text": text,
    "space_tokens": space_tokens,
    "manual_tokens": manual_tokens,
    "tool_tokens": tool_tokens,
    "diff_samples": diffs
}

# Save JSON for report
OUTPUT_JSON = TEXT_PATH.with_name("tokenization_output.json")
OUTPUT_JSON.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")

print("Tokenization finished. See tokenization_output.json.")
