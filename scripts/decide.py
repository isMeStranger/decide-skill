#!/usr/bin/env python3
"""Decision calculator. Reads JSON from a file path or stdin ('-').

  score  Weighted scoring + dominance + sensitivity (weight that flips the winner).
         {"weights": {"pay": 100, "growth": 60}, "options": {"A": {"pay": 7, "growth": 5}, ...}}
  table  Payoff table under scenarios: EV, worst case, max regret, EVPI.
         {"probs": {"boom": 0.3, "bust": 0.7}, "payoffs": {"A": {"boom": 100, "bust": -20}, ...}}
         Omit "probs" for deep uncertainty: only worst case and minimax regret are shown.
  kelly  Bet sizing.  args: p b   (win probability, net odds)
  test   Run self-checks.
"""
import json
import sys


def load(path):
    return json.load(sys.stdin if path == "-" else open(path))


def score(d):
    w, opts = d["weights"], d["options"]
    for name, s in opts.items():
        missing = set(w) - set(s)
        if missing:
            raise SystemExit(f"option {name} lacks scores for {sorted(missing)}")
    total_w = sum(w.values())
    totals = {o: sum(w[c] * s[c] for c in w) / total_w for o, s in opts.items()}
    ranked = sorted(totals, key=totals.get, reverse=True)
    win = ranked[0]
    dominated = [o for o in opts for p in opts
                 if p != o and all(opts[p][c] >= opts[o][c] for c in w)
                 and any(opts[p][c] > opts[o][c] for c in w)]
    # Ranking depends linearly on one raw weight when others are fixed: solve for the crossing point.
    flips = []
    for c in w:
        for o in opts:
            if o == win:
                continue
            rest_win = sum(w[k] * opts[win][k] for k in w if k != c)
            rest_o = sum(w[k] * opts[o][k] for k in w if k != c)
            diff = opts[win][c] - opts[o][c]
            if diff == 0:
                continue
            x = (rest_o - rest_win) / diff
            if x >= 0 and abs(x - w[c]) > 1e-9:
                flips.append((abs(x - w[c]) / w[c] if w[c] else float("inf"), c, o, x))
    flips.sort()
    return {"totals": {o: round(totals[o], 3) for o in ranked}, "winner": win,
            "dominated": sorted(set(dominated)),
            "flips": [f"weight '{c}' {w[c]} -> {x:.1f} makes '{o}' tie the winner ({r:.0%} change)"
                      for r, c, o, x in flips[:5]],
            "robust": not flips or flips[0][0] > 0.5}


def table(d):
    pay, probs = d["payoffs"], d.get("probs")
    scen = list(next(iter(pay.values())))
    best_in = {s: max(pay[o][s] for o in pay) for s in scen}
    out = {}
    for o, row in pay.items():
        r = {"worst": min(row.values()), "max_regret": max(best_in[s] - row[s] for s in scen)}
        if probs:
            r["ev"] = round(sum(probs[s] * row[s] for s in scen), 3)
        out[o] = r
    res = {"options": out, "minimax_regret_choice": min(out, key=lambda o: out[o]["max_regret"]),
           "maximin_choice": max(out, key=lambda o: out[o]["worst"])}
    if probs:
        if abs(sum(probs.values()) - 1) > 1e-6:
            raise SystemExit(f"probabilities sum to {sum(probs.values())}, not 1")
        best = max(out, key=lambda o: out[o]["ev"])
        ev_pi = sum(probs[s] * best_in[s] for s in scen)
        res.update(ev_choice=best, evpi=round(ev_pi - out[best]["ev"], 3))
    return res


def kelly(p, b):
    f = p - (1 - p) / b
    return {"full_kelly": round(f, 4), "half_kelly": round(f / 2, 4),
            "advice": "no edge: do not bet" if f <= 0 else f"stake about {f/2:.1%} of bankroll (half-Kelly)"}


def test():
    s = score({"weights": {"a": 1, "b": 1}, "options": {"X": {"a": 9, "b": 5}, "Y": {"a": 5, "b": 7}, "Z": {"a": 4, "b": 4}}})
    assert s["winner"] == "X" and s["dominated"] == ["Z"], s
    assert any("'b' 1 -> 2.0" in f for f in s["flips"]), s  # 9+5w = 5+7w at w=2
    t = table({"probs": {"up": 0.5, "down": 0.5}, "payoffs": {"A": {"up": 100, "down": 0}, "B": {"up": 40, "down": 40}}})
    assert t["ev_choice"] == "A" and t["evpi"] == 20 and t["minimax_regret_choice"] == "A" and t["maximin_choice"] == "B", t
    assert kelly(0.6, 1)["full_kelly"] == 0.2
    print("ok")


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a or a[0] in ("-h", "--help"):
        print(__doc__)
    elif a[0] == "test":
        test()
    elif a[0] == "kelly":
        print(json.dumps(kelly(float(a[1]), float(a[2])), indent=2))
    else:
        print(json.dumps({"score": score, "table": table}[a[0]](load(a[1] if len(a) > 1 else "-")), indent=2))
