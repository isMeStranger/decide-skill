# decide — a Claude Code skill for better decisions

Walks any choice through a structured process: framing, options, facts and base rates, other players (game theory), math (weighted scoring, expected value, sensitivity, value of information, regret, Kelly), a premortem plus a bias and fallacy scan, a psychology check, and a final Decision Card with tripwires.

Effort scales with the stakes: small reversible choices get a quick answer, irreversible ones get the full process.

## Install

```bash
git clone https://github.com/isMeStranger/decide-skill ~/.claude/skills/decide
```

Then in Claude Code type `/decide <your decision>`, or just ask "should I …?".

## Contents

| File | What it holds |
|---|---|
| `SKILL.md` | The 8-step process Claude follows |
| `references/math.md` | Weighted scoring, EV, utility and ruin, Bayes, value of information, decision trees, minimax regret, Kelly, optimal stopping, calibration |
| `references/biases.md` | 23 biases and 13 fallacies, each with a fix, plus replication notes |
| `references/psychology.md` | Emotions as data, quick perspective tests, group decisions, decision journal |
| `scripts/decide.py` | Calculator: `score`, `table`, `kelly`, `test` (no dependencies, Python 3) |

## Sources

Spetzler et al., *Decision Quality* (2016) · Kahneman, Lovallo & Sibony, Mediating Assessments Protocol (MIT Sloan / *Noise*) · reference class forecasting (Kahneman & Tversky; Flyvbjerg) · Tetlock, Good Judgment Project · Many Labs 1 and 2 replication projects.

## License

MIT
