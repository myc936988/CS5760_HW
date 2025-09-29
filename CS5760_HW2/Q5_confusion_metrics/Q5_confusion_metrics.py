# CS5760 HW2 Q5 — Multi-class precision/recall metrics
# Usage: python Q5_confusion_metrics.py

from typing import Dict, List, Tuple

def per_class_pr(conf: List[List[int]], labels: List[str]) -> Dict[str, Tuple[float,float]]:
    # conf[r][c] = count(pred=labels[r], gold=labels[c])
    n = len(labels)
    # column sums (gold), row sums (pred)
    col_sum = [sum(conf[r][c] for r in range(n)) for c in range(n)]
    row_sum = [sum(conf[r]) for r in range(n)]
    out = {}
    for i, lab in enumerate(labels):
        tp = conf[i][i]
        fp = row_sum[i] - tp
        fn = col_sum[i] - tp
        prec = tp / (tp + fp) if (tp+fp)>0 else 0.0
        rec  = tp / (tp + fn) if (tp+fn)>0 else 0.0
        out[lab] = (prec, rec)
    return out

def macro_micro(conf: List[List[int]], labels: List[str]):
    pcs = per_class_pr(conf, labels)
    # macro
    mp = sum(p for p,_ in pcs.values())/len(labels)
    mr = sum(r for _,r in pcs.values())/len(labels)
    # micro
    tp = sum(conf[i][i] for i in range(len(labels)))
    total = sum(sum(row) for row in conf)
    micro = tp/total if total>0 else 0.0
    return pcs, mp, mr, micro, micro

if __name__ == "__main__":
    labels = ["Cat","Dog","Rabbit"]
    conf = [
        [5,10,5],
        [15,20,10],
        [0,15,10],
    ]
    pcs, mp, mr, microp, micror = macro_micro(conf, labels)
    print("Per-class:")
    for lab,(p,r) in pcs.items():
        print(f"  {lab:6s}  P={p:.3f}  R={r:.3f}")
    print(f"Macro:   P={mp:.3f}  R={mr:.3f}")
    print(f"Micro:   P={microp:.3f}  R={micror:.3f}")
