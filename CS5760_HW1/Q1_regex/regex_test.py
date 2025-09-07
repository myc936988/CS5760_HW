
# Q1 quick test runner (pure Python re)
import re, pathlib

tests = pathlib.Path(__file__).with_name("tests.txt").read_text(encoding="utf-8")

patterns = [
    (r"\b\d{5}(?:[- ]\d{4})?\b", "ZIP"),
    (r"\b(?![A-Z])[A-Za-z]+(?:['’-][A-Za-z]+)*\b", "non-capitalized words"),
    (r"(?<!\w)[+-]?(?:\d{1,3}(?:,\d{3})*|\d+)(?:\.\d+)?(?:[eE][+-]?\d+)?(?!\w)", "numbers"),
    (r"(?i)\be[\s\-–—]?mail\b", "email spellings"),
    (r"(?i)\bgo+[!.,?]?\b", "go+ with optional punct"),
    (r"(?m)^.*\?[)\"'’\]\s]*$", "line ending with ? + closing")
]

for pat, name in patterns:
    print("="*60)
    print(f"Pattern: {name}\n{pat}")
    print("- matches -")
    for m in re.finditer(pat, tests):
        snippet = tests[max(0, m.start()-12):m.end()+12].replace("\n","(line break)")
        print(f"  {m.group(0)!r}   ...{snippet}...")
