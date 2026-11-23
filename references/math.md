# Decision math — pick one, use it, explain the result in plain words

## 1. Weighted scoring (multi-criteria, MCDA)
1. Criteria = objectives from Step 1 (3–7; merge overlaps; no double counting).
2. Score each option 0–10 on **one criterion at a time** across all options, using facts where possible. Define what 0 and 10 mean in advance (e.g. salary: 0 = current, 10 = +50%).
3. **Swing weights** (not "importance" guesses): "Of all criteria, swinging which one from worst to best option matters most?" Give it 100. Rate the others relative to it. Normalise to sum 1.
4. Total = Σ weight × score.
5. **Dominance**: drop any option that is ≤ another on every criterion.
6. **Sensitivity**: for each weight, how far must it move to change the winner? `scripts/decide.py score` prints this.
7. Must-haves (deal-breakers) are filters applied before scoring, not heavy weights.

## 2. Expected value (EV)
EV = Σ p(outcome) × value(outcome). Probabilities must sum to 1.
- Use when the bet is repeatable or small relative to total wealth/life.
- Always show the **worst case and its probability** next to EV.
- Example: Job A: 100% × $60k = $60k. Startup: 30% × $150k + 50% × $40k + 20% × $0 = $65k. EV favours startup slightly, but 20% chance of $0 — can the user absorb that? → utility.

## 3. Utility and risk
- Losing $X hurts more than gaining $X helps; money has diminishing value. Use log(wealth) as a default utility for money: compare E[log(wealth after)].
- **Ruin rule**: if an option has any meaningful chance of an unrecoverable loss (bankruptcy, health, prison, losing the one relationship), EV is not enough. Remove it or cap the exposure.
- **Certainty equivalent**: "What guaranteed amount would make you indifferent to this gamble?" Reveals real risk attitude.

## 4. Bayes — updating on evidence
Posterior odds = prior odds × likelihood ratio.
- Prior = base rate from the reference class.
- Likelihood ratio = P(evidence | hypothesis true) / P(evidence | false).
- Example: 10% of startups in this sector survive 5 years (prior odds 1:9). Founder has prior exit — such founders are 2× as common among survivors (LR 2) → odds 2:9 → 18%.
- Update often, in small steps. Strong updates need strong evidence.

## 5. Value of information (EVPI / EVSI)
EVPI = E[value if you knew the uncertainty before choosing] − EV of the best choice now.
- If EVPI < cost of getting the info (money + time + lost opportunity) → decide now.
- If info could flip the decision and is cheap → get it first.
- Imperfect info (a test, a trial month, an expert) is worth less than EVPI; EVPI is the ceiling.
- `scripts/decide.py evpi` computes it.

## 6. Decision tree
Squares = choices, circles = chance (with probabilities), leaves = values. Roll back from the right: chance node = EV of branches; choice node = take the max. Good for staged decisions ("test first, then commit").

## 7. Deep uncertainty (no credible probabilities)
- **Minimax regret**: regret = best payoff in that scenario − your payoff. Choose the option whose maximum regret is smallest.
- **Robustness**: choose the option that is "good enough" in the most scenarios.
- **Optionality**: prefer moves that keep future choices open; small, cheap, reversible experiments first.
- **Barbell**: mostly very safe + a small part high-upside; avoid the fragile middle.

## 8. Kelly sizing (repeated bets with an edge)
f* = p − (1 − p)/b   where p = win probability, b = net odds (win b per 1 staked).
- Never bet if f* ≤ 0. Use **half-Kelly**: estimates of p are usually overconfident.
- Example: p = 0.6, b = 1 → f* = 0.2 → bet 10% (half-Kelly).

## 9. Satisficing vs maximising
For reversible or low-stakes choices: set a minimum bar, take the first option that clears it. Maximisers spend more effort and report lower satisfaction.
**Optimal stopping (37% rule)**: when options arrive one at a time and you can't go back, look at the first ~37% without committing, then take the first one better than all those seen.

## 10. Calibration
- Say probabilities as numbers. Score later with Brier = (forecast − outcome)², averaged; 0 is perfect, 0.25 = always saying 50%.
- If you're "90% sure" about many things, ~1 in 10 should be wrong. If none are, you're underconfident; if more are, overconfident.
