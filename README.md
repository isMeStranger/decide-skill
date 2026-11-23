# decide

A Claude skill for making a decision you're stuck on.

You describe the choice. Claude lists your options (at least three, including staying put), separates facts from guesses, puts numbers on the risks, checks for common thinking errors, and ends with a short Decision Card: what to do, how sure it is, what would make you change course, and the first step.

Small decisions get a short answer. Big or hard-to-undo ones get the full process.

## Example

> I have a job offer from a 2-year-old startup: $85k plus 0.2% equity, 1-hour commute, interesting work. My current job: $70k, stable, boring, 20-min commute. 6 months of savings. Should I take it?

Part of the answer:

```
DECISION: Take the offer, conditional on
  runway ≥12 months, plus negotiating hybrid days
  or more salary to offset the commute.
CONFIDENCE: 70%
TRIPWIRES:
  - Runway <12 months or they won't say → turn
    it down or ask for $95k+.
  - Work not interesting by 2027-05-23 → re-decide.
FIRST STEP (today): email the hiring manager
  the 4 questions above.
```

It also worked out that the raise only just covers the cost of the commute, that the equity should be treated as worth $0, and that the decision only flips if job security matters about six times more than assumed.

Full output: [examples/job-offer.md](examples/job-offer.md)

## Install

Claude Code, as a plugin:

```
/plugin install decide --marketplace isMeStranger/decide-skill
```

Claude Code, by hand:

```bash
git clone https://github.com/isMeStranger/decide-skill ~/.claude/skills/decide
```

claude.ai (web or desktop; it then works in the phone app too): download this repo as a zip, then go to Customize → Skills → + → Upload a skill. Code execution must be on.

## Use

Type `/decide` followed by your question, or just ask something like "should I…" or "help me choose between…".

## What it uses

- Decision quality framework (Spetzler, Winter & Meyer, *Decision Quality*, 2016)
- Scoring each criterion separately before looking at totals (Kahneman, Lovallo & Sibony, Mediating Assessments Protocol)
- Base rates before details (reference class forecasting)
- Forecasting habits from Tetlock's Good Judgment Project
- Expected value, weighted scoring, value of information, minimax regret, Kelly sizing
- A list of biases and fallacies, with notes on which ones held up in the Many Labs replication studies

## Files

- `SKILL.md`: the steps Claude follows
- `references/`: the math, the bias and fallacy list, and the psychology notes
- `scripts/decide.py`: a calculator for scoring, expected value and bet sizing (Python 3, no dependencies). Run `python3 scripts/decide.py test` to check it.

## License

MIT
