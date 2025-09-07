
# Q4 — Edit distance (Levenshtein with custom costs)
# Usage: python edit_distance.py
from typing import Tuple, List


def edit_distance(a: str, b: str, sub_cost: int=1, ins_cost: int=1, del_cost: int=1):
    n, m = len(a), len(b)  # Initialize DP and backtrace tables
    dp = [[0]*(m+1) for _ in range(n+1)]
    back = [[None]*(m+1) for _ in range(n+1)]
    # Base cases: transforming prefix to/from empty string
    for i in range(1, n+1):
        dp[i][0] = i*del_cost
        back[i][0] = ('D', a[i-1])  # delete
    for j in range(1, m+1):
        dp[0][j] = j*ins_cost
        back[0][j] = ('I', b[j-1])  # insert
    # Fill DP table
    for i in range(1, n+1):
        for j in range(1, m+1):
            # Three choices: substitute/match, delete, insert
            cost_sub = dp[i-1][j-1] + (0 if a[i-1] == b[j-1] else sub_cost)
            cost_del = dp[i-1][j] + del_cost
            cost_ins = dp[i][j-1] + ins_cost
            best = cost_sub
            op = ('M' if a[i-1] == b[j-1] else 'S', (a[i-1], b[j-1]))
            if cost_del < best:
                best = cost_del; op = ('D', a[i-1])
            if cost_ins < best:
                best = cost_ins; op = ('I', b[j-1])
            dp[i][j] = best
            back[i][j] = op

    # Backtrace to recover operations
    i, j = n, m
    ops: List[Tuple[str, str]] = []
    while i > 0 or j > 0:
        op = back[i][j]
        if op is None: break
        ops.append(op)
        if op[0] in ('M', 'S'):
            i -= 1; j -= 1
        elif op[0] == 'D':
            i -= 1
        elif op[0] == 'I':
            j -= 1
    ops.reverse()
    return dp[n][m], ops


def pretty_ops(ops):
    """Convert operation tuples into human-readable strings."""
    out = []
    for o in ops:
        if o[0] == 'M':
            out.append(f"Keep '{o[1][0]}'")
        elif o[0] == 'S':
            out.append(f"Substitute '{o[1][0]}' -> '{o[1][1]}'")
        elif o[0] == 'I':
            out.append(f"Insert '{o[1]}'")
        elif o[0] == 'D':
            out.append(f"Delete '{o[1]}'")
    return out


def run_case(a, b, sub, ins, delete):
    """Helper to run one edit distance case with given costs."""
    dist, ops = edit_distance(a, b, sub, ins, delete)
    return {
        "a": a, "b": b, "costs": {"sub": sub, "ins": ins, "del": delete},
        "distance": dist, "ops": pretty_ops(ops)
    }


if __name__ == "__main__":
    caseA = run_case("Sunday", "Saturday", sub=1, ins=1, delete=1)
    caseB = run_case("Sunday", "Saturday", sub=2, ins=1, delete=1)
    import json, pathlib
    OUT = pathlib.Path(__file__).with_name("edit_distance_output.json")
    OUT.write_text(json.dumps({"modelA": caseA, "modelB": caseB}, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Edit distance finished. See edit_distance_output.json.")
