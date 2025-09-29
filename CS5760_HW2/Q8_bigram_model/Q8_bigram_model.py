# CS5760 HW2 Q8 — Bigram Language Model (MLE)
# Usage: python Q8_bigram_model.py

from collections import defaultdict, Counter
from typing import List, Tuple

TRAIN = [
    "<s> I love NLP </s>",
    "<s> I love deep learning </s>",
    "<s> deep learning is fun </s>",
]

def tokenize(s: str) -> List[str]:
    return s.split()

def counts_bigrams(corpus: List[str]):
    uni = Counter()
    bi = Counter()
    for line in corpus:
        toks = tokenize(line)
        for i,t in enumerate(toks):
            uni[t] += 1
            if i>0:
                bi[(toks[i-1], t)] += 1
    return uni, bi

def prob_sentence(sent: str, uni: Counter, bi: Counter) -> float:
    toks = tokenize(sent)
    p = 1.0
    for i in range(1, len(toks)):
        prev, cur = toks[i-1], toks[i]
        denom = sum(c for (w,nextw), c in bi.items() if w==prev)
        num = bi[(prev, cur)]
        if denom == 0:  # unseen history
            return 0.0
        p *= num/denom
    return p

if __name__ == "__main__":
    uni, bi = counts_bigrams(TRAIN)
    s1 = "<s> I love NLP </s>"
    s2 = "<s> I love deep learning </s>"
    p1 = prob_sentence(s1, uni, bi)
    p2 = prob_sentence(s2, uni, bi)
    print(f"P(S1)={p1:.6f}   {s1}")
    print(f"P(S2)={p2:.6f}   {s2}")
    if p1 > p2:
        print("Model prefers S1 because P(NLP | love) = 1/2, while P(</s> | learning) = 1/2 adds another factor, making S2 lower overall.")
    elif p2 > p1:
        print("Model prefers S2.")
    else:
        print("Both equal under this training set (unlikely here).")
