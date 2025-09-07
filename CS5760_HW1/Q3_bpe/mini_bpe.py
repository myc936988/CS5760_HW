# mini_bpe_q3_min.py
# Q3: Manual BPE + Mini BPE (pure Python, no deps)

from collections import Counter
import textwrap

EOW = "_"  # End-of-word marker, appended to every word

"""Convert a word into a list of characters + end-of-word marker."""
def to_seq(w): return list(w) + [EOW]


def count_pairs(seqs):
    """Count frequencies of all adjacent symbol pairs in the sequences."""
    c = Counter()
    for s in seqs:
        for i in range(len(s)-1):
            c[(s[i], s[i+1])] += 1
    return c


def merge_once(seqs, pair):
    """Perform one merge step: replace occurrences of pair (a,b) with token 'ab'."""
    a, b = pair
    out_all = []
    for s in seqs:
        i, out = 0, []
        while i < len(s):
            if i < len(s)-1 and s[i]==a and s[i+1]==b:
                out.append(a+b); i += 2
            else:
                out.append(s[i]); i += 1
        out_all.append(out)
    return out_all


def learn_bpe(seqs, num_merges):
    """Learn BPE merges for a given number of steps.
        Returns the list of merges, snapshots for logging, and the final sequences.
        """
    merges, snaps = [], []
    for step in range(1, num_merges+1):
        pairs = count_pairs(seqs)
        if not pairs: break
        (p, cnt) = pairs.most_common(1)[0]
        merges.append(p)
        seqs = merge_once(seqs, p)
        vocab = Counter(t for s in seqs for t in s)
        snaps.append((step, p, cnt, len(vocab), seqs))
    return merges, snaps, seqs


def apply_bpe(word, merges):
    """Apply a sequence of merges to segment a new word into subwords."""
    s = to_seq(word)
    for a,b in merges:
        i, out = 0, []
        while i < len(s):
            if i < len(s)-1 and s[i]==a and s[i+1]==b:
                out.append(a+b); i += 2
            else:
                out.append(s[i]); i += 1
        s = out
    return s


def show(title): print("\n"+title+"\n"+"="*len(title))


# Q3.1
def q31():
    """Demonstration of 3 manual BPE merge steps on a toy corpus."""
    show("Q3.1 Manual BPE on toy corpus")
    toy = "low low low low low lowest lowest newer newer newer newer newer newer wider wider wider new new".split()
    seqs = [to_seq(w) for w in toy]
    vocab0 = sorted(set(t for s in seqs for t in s))
    print("[Initial vocab |V|=%d] sample: %s%s" %
          (len(vocab0), ", ".join(vocab0[:20]), " ..." if len(vocab0)>20 else ""))
    print("Initial corpus (2 lines):")
    print("  " + " ".join(seqs[0]))
    print("  " + " ".join(seqs[1]))

    for step in range(1, 4):
        pairs = count_pairs(seqs)
        (best, cnt) = pairs.most_common(1)[0]
        seqs = merge_once(seqs, best)
        new_tok = best[0] + best[1]
        vocab = Counter(t for s in seqs for t in s)
        print(f"\nStep {step}: best pair {best} (count={cnt})")
        print("  Updated snippet:")
        print("   • " + " ".join(seqs[0]))
        if len(seqs)>1: print("   • " + " ".join(seqs[1]))
        print(f"  New token: '{new_tok}', updated |V|={len(vocab)}")


# Q3.2
def q32():
    """Learn BPE automatically on toy corpus, print top pairs and segment sample words."""
    show("Q3.2 Mini BPE learner on toy")
    toy = "low low low low low lowest lowest newer newer newer newer newer newer wider wider wider new new".split()
    seqs = [to_seq(w) for w in toy]
    merges, snaps, final = learn_bpe(seqs, num_merges=10)

    print("[Top pair each step + vocab size]")
    for step, p, cnt, V, _ in snaps:
        print(f"  Step {step:>2}: top {p} (count={cnt})  |V|={V}")

    print("\n[Segmentation]")
    for w in ["new", "newer", "lowest", "widest", "newestest"]:
        print(f"  {w:<10} -> {apply_bpe(w, merges)}")

    print("\n[Report bullets]")
    print("  - Subwords compose OOV words from known pieces.")
    print("  - Frequent pairs become whole tokens; rare words decompose.")
    print("  - Some subwords align with morphemes, e.g., 'er_' for comparative/agent.")
    print("  - More merges -> larger vocab, less fragmentation (trade-off).")
    print("  - Small/domain-specific corpora may not transfer well.")


# Q3.3
DEF_PARA = textwrap.dedent("""\
Subword tokenization is widely used in modern NLP models. It helps balance vocabulary size and coverage.
When encountering rare words or misspellings, the model can still break them into known pieces.
However, subwords can sometimes split meaningful units in awkward ways.
Choosing the number of merges involves trade-offs among accuracy, speed, and robustness.
Practitioners often tune merges based on task and data size.
""").strip()


def q33(paragraph=DEF_PARA, merges=30):
    """Train BPE on a real paragraph, show top merges, longest tokens, and segment examples."""
    show(f"Q3.3 Train on your paragraph (merges={merges})")
    words = [w.strip() for w in paragraph.split() if w.strip()]
    seqs = [to_seq(w) for w in words]
    merges_list, snaps, final = learn_bpe(seqs, num_merges=merges)
    vocab = Counter(t for s in final for t in s)

    print("[Top-5 merges (selection order)]")
    for i, (step, p, cnt, V, _) in enumerate(snaps[:5], 1):
        print(f"  {i}. {p}  (count_when_chosen={cnt})  |V|={V}")

    longest5 = sorted(vocab.items(), key=lambda kv: (-len(kv[0]), -kv[1]))[:5]
    print("\n[Longest 5 subwords (token, freq)]")
    for t, f in longest5:
        print(f"  - {t!r} x {f}")

    seen, picks = set(), []
    for w in words:
        if w not in seen:
            seen.add(w); picks.append(w)
            if len(picks) == 5: break
    print("\n[Segmentation of 5 words]")
    for w in picks:
        print(f"  {w:<20} -> {apply_bpe(w, merges_list)}")

    print("\n[Reflection prompts (write 5–8 sentences)]")
    print("  - Which subwords look like prefixes/suffixes/stems/whole-words?")
    print("  - Two pros (OOV handling, compact vocab) and two cons (morpheme splits, domain sensitivity).")
    print("  - How many merges felt right and why? Did tokens reflect productive morphology?")


if __name__ == "__main__":
    q31()
    q32()
    q33()
