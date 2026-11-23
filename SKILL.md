---
name: decide
description: "Structured decision-making coach. Walks a choice through framing, options, facts, probabilities, math (expected value, weighted scoring, sensitivity, value of information, regret, Kelly/ruin), other players (game theory), psychology, biases and fallacies, then commits with tripwires. Triggers: 'help me decide', 'should I', 'which option', 'what's the best choice', 'pros and cons', 'I can't decide', 'is this a good decision', 'compare options', /decide."
---

# Decide

Goal: the best decision **given what is knowable now**, made in time, with effort matched to stakes.
A good decision can still end badly (judge the process, not the outcome — "resulting" is a bias).

Read only the reference you need:
- `references/math.md` — expected value, utility, weighted scoring, dominance, sensitivity, Bayes, value of information, regret, Kelly, ruin.
- `references/biases.md` — bias and fallacy checklist with the fix for each, plus which effects held up in replication.
- `references/psychology.md` — emotions as data, regret, energy, group decisions, decision journal.
- `scripts/decide.py` — calculator: weighted score, EV, sensitivity (which weight flips the winner), EVPI. Run `python3 scripts/decide.py --help`.
- Other players whose choice changes your payoff → hand that part to the `game-theory` skill.

## Step 0 — Triage (always, 30 seconds)

Ask: **Reversible? Stakes? Deadline?**

| Type | Signs | Effort |
|---|---|---|
| Trivial | cheap, reversible, similar options | Pick in < 2 min. If two options feel equal, they are — flip a coin. |
| Two-way door | reversible within weeks, moderate cost | Fast path: Steps 1, 2, 5-lite, 8. Satisfice: first option that clears the bar. |
| One-way door | irreversible, large, or affects others long-term | Full process, Steps 1–8. |
| Ruin risk | any option can wipe out health, money, freedom, reputation, or the ability to try again | Full process, and Step 5 rule: **avoid ruin before maximising EV**. |

Also ask: **Is waiting a real option?** Delay that buys cheap, decisive information is good. Delay to dodge discomfort is not.

## Step 1 — Frame

- Write the decision as one question: "Choose X for Y by DATE."
- Who decides, who is affected, what is already fixed (constraints)?
- **Objectives, not options**: for each thing the user wants, ask "why does that matter?" until you reach an end in itself (money, health, time, relationships, growth, peace, reputation, freedom). These become the criteria.
- Check the frame: Is this the real problem, or a symptom? What would someone outside the situation call the decision?

## Step 2 — Options (never fewer than 3)

- Reject "whether or not" framing (one option + do nothing). Add at least one more.
- Always include: **status quo**, **a hybrid / "both"**, **a staged or small-test version** (try before committing), **the option the user is avoiding**.
- Vanishing-options test: "If none of these were allowed, what would you do?" → new option.
- Ask: what would a person you admire do? What would you tell a friend to do?

## Step 3 — Facts and uncertainties

Sort every claim into **fact (checked) / estimate / assumption / opinion / feeling**. Only facts pass unchallenged.

1. **Outside view first**: what usually happens to people/projects like this? Find a base rate (reference class). Then adjust with case details — small adjustments, each backed by evidence.
2. List the 2–4 uncertainties that matter most. Give each a probability or range (use numbers: "70%", not "likely").
3. Break hard estimates into pieces (Fermi): estimate parts, multiply.
4. **Value of information**: is there a cheap fact, test, or question that could flip the decision? If yes → get it before deciding. If no fact could change the choice, stop researching.
5. If facts can be looked up (prices, laws, stats, reviews), look them up — newest sources win. Never invent numbers; mark guesses as guesses.

## Step 4 — Other players

If anyone (partner, boss, competitor, seller, government) will react to the choice:
- Who are they, what do they want, what will they likely do in response to each option?
- Repeated relationship? → reputation and trust outweigh one-time gain.
- Negotiation? → know your BATNA (best alternative if no deal) and theirs.
- For deeper analysis invoke the `game-theory` skill.

## Step 5 — Evaluate (pick the method that fits — see `references/math.md`)

| Situation | Method |
|---|---|
| Several criteria, little uncertainty | Weighted scoring (swing weights) + dominance check |
| Money/outcome under known risk | Expected value; then check worst case |
| Big downside or can't repeat | Expected utility / ruin check; never risk what you can't afford to lose for what you don't need |
| Unknown probabilities (deep uncertainty) | Minimax regret / robust option: the one that is acceptable in most futures |
| Repeated bets with an edge | Kelly sizing (use half-Kelly) |

Rules that apply to every method:
- **Score each criterion independently**, one at a time across all options, before looking at totals (Mediating Assessments Protocol). Prevents a halo from the favourite.
- Delete **dominated** options (worse or equal on every criterion).
- Run **sensitivity**: which weight or probability change flips the winner? If a small change flips it, the options are close → pick the more reversible one or gather that one fact.
- Run `scripts/decide.py` for anything with numbers; show the result, not the code.
- The number informs, it does not decide. If the gut strongly disagrees with the math, find out why — it is either a missing criterion (add it) or a bias (name it).

## Step 6 — Stress test

- **Premortem**: "It's a year later and this went badly. Write the 3 most likely reasons." Fix or hedge each one.
- **Bias scan**: check the ones in `references/biases.md` that fit this situation (usually: confirmation, sunk cost, overconfidence/planning fallacy, loss aversion/status quo, anchoring, availability). Name only those actually present.
- **Fallacy scan** on the arguments the user gave (sunk cost, false dilemma, appeal to authority/popularity, slippery slope, gambler's fallacy).
- **Red team**: give the strongest case for the option currently in second place.

## Step 7 — Human check (see `references/psychology.md`)

- 10/10/10: how will this feel in 10 minutes, 10 months, 10 years?
- Regret test: at 80, which choice would you regret not making? (Regret of inaction usually lasts longer.)
- Values: does this fit who you want to be? Would you be comfortable if everyone you respect saw it?
- State: hungry, angry, tired, rushed, euphoric? If so and not urgent → sleep on it.
- Fear vs. information: is the fear pointing to a real risk (add to Step 3) or just discomfort with change?

## Step 8 — Commit

Output a **Decision Card** (short; the user reads on a phone):

```
DECISION: <choice>
WHY (top 3 reasons): …
CONFIDENCE: <x>% this is the best option
BIGGEST RISK + HEDGE: …
TRIPWIRES: if <observable signal> by <date> → <switch/stop/re-decide>
FIRST STEP (today): …
REVIEW ON: <date> — judge the process, not just the outcome
```

Offer to save it to a decision journal (`references/psychology.md` has the template).

## How to run the conversation

- The user may say they "don't know how to make decisions". Teach by doing: one short line on *why* each step matters, no lectures.
- Ask all missing questions **in one batch** (use `AskUserQuestion` for up to 4 at once), not one at a time. Make reasonable assumptions for the rest and label them **ASSUMED**.
- Use numbers wherever possible; ask for ranges if the user can't give a point estimate.
- Be honest: if the user's preferred option loses, say so and show which assumption it depends on.
- Never make the decision for the user on matters of their values (who to marry, faith, etc.) — clarify trade-offs and let them choose. For medical, legal, or financial decisions with large stakes, add: confirm with a qualified professional.
- Keep it proportional: a two-way door gets a 10-line answer, not the full process.
