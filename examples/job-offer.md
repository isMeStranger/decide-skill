# Example: startup offer vs current job

Prompt:

> /decide I have a job offer from a 2-year-old startup: $85k salary plus 0.2% equity, 1-hour commute, very interesting work. My current job: $70k, stable, boring, 20-min commute, I have been there 4 years. I have 6 months of savings, no kids, rent. Should I take the offer? Don't ask me questions; state assumptions and give me the full analysis and Decision Card.

Output (Claude Code, unedited apart from removing a section produced by the tester's personal settings):

---

**Take the offer, but first get answers on the startup's runway and a way to cut the commute.** Staying wins only if you care about job security about 6× more than I assumed, or about the commute about 5× more.

## Triage
This is a big decision but not a permanent one: if the startup fails, you can get another salaried job within months. It's not a ruin risk either. Your 6 months of savings covers a typical job gap. The real deadline is the offer deadline, so get the missing facts before then.

## Assumptions (all mine, not facts)
- You're in the US, with roughly 25–30% marginal tax.
- The commute is 1 hour each way, 5 days a week. That's about 80 extra minutes a day, or **~300 extra hours a year**.
- If you drive, the longer commute costs about $2.5k a year.
- The startup is at seed or Series A stage, valued around $20M.
- The 0.2% is stock options on a 4-year vesting schedule with a 1-year cliff.
- You can't get promoted or move to a more interesting role at your current job (4 years in suggests that).
- You're not tied to your current flat. You rent, so you could move closer when the lease ends.

## Money (Fermi estimate)
- **Salary:** +$15k gross is about +$10.5k after tax, or about +$8k after commute costs.
- **Paid for the commute:** $8k ÷ 300h ≈ **$26/hour of commuting**, which is about what you earn per hour now after tax. So the raise just pays for the commute. **The money alone doesn't decide this.**
- **Equity:** about 90% of startups never return anything to employees. Rough expected value:
  - 8% chance of a $200M exit. After dilution your stake is ~0.1%, worth ~$200k.
  - 2% chance of a $1B exit. Your stake is ~0.08%, worth ~$800k.
  - That averages out to ~$30k spread over 5–8 years.
  - Plan as if it's worth **$0**. It's a lottery ticket.

**3-year scenarios** (net $k compared with staying):

| Startup | Probability | Take | Stay |
|---|---|---|---|
| Thrives | 25% | +32 | 0 |
| Muddles along | 40% | +17 | 0 |
| Fails by year 2 | 35% | −8 | 0 |

- **Expected gain from taking: +$12k.** Worst case: −$8k, which is about 1.5 months of your savings.
- The most you'd regret staying is $32k. The most you'd regret taking is $8k. That points to taking.

## Options scored
Weights reflect what I assumed you care about most. "Interesting work" and growth rank highest because you led with them.

| Option | Score |
|---|---|
| **Take, then cut the commute (hybrid days or move closer)** | **7.1** |
| Take as offered | 6.5 |
| Use the offer to get a raise and stay | 4.9 |
| Stay | 4.3 |

- **How sure:**
  - The result holds unless the commute matters about 5× more than I weighted it, or security about 6× more.
  - "Take as offered" is beaten by the commute-cutting version on every count. So hybrid days or a move is the thing to push for.
- **The option you're probably avoiding:** keep job-hunting for something interesting *and* closer. That's a fine backup, but it isn't a reason to turn down a real offer.

## Facts that could flip this (ask the startup this week)
1. **Runway:** how many months of cash do they have, and when was the last funding round? Under 12 months with no round in sight makes this far riskier.
2. **Hybrid or remote:** could you work from home 2 days a week? That cuts the commute penalty by about 40%.
3. **Option terms:**
   - strike price
   - how long you have to buy your shares after leaving (90 days is common; longer is better)
   - total shares outstanding, so you can check what 0.2% actually is
4. **What is actually interesting:** the day-to-day work, your manager, and how many people have left recently.

## Premortem: a year from now it went badly. Why?
1. **The money ran out and there were layoffs.** Hedge: check runway first, keep 6 months of savings untouched, and update your CV every quarter.
2. **The commute wore you down.** Research on commuting (Stutzer & Frey) found people underestimate this cost. Treat that as a direction, not a precise number. Hedge: hybrid days now, move closer when your lease ends.
3. **The "interesting work" turned out to be chaos and 60-hour weeks.** Hedge: ask your future teammates directly before you sign.

## Biases to check
- **Staying because it's familiar:** 4 years at a job you call boring is the strongest pull to stay.
- **Shiny-object effect:** "very interesting" is a feeling, so test it in interviews.
- **Taking the equity at face value:** discount it to almost zero.

## Strongest case for staying
- It's guaranteed, you get 300 hours a year back, and nothing is at risk.
- You could job-hunt calmly for something interesting and nearer.
- That case is valid only if you will actually run that search within 3 months. Most people don't.

## Gut check
- **10 / 10 / 10:** in 10 minutes, nerves. In 10 months, probably more engaged but more tired. In 10 years, the startup is a useful CV line whatever happens to it.
- **Regret at 80:** "I stayed 6+ years somewhere boring" is the more likely regret. Regret about things you didn't do tends to last longer.

```
DECISION: Take the offer, conditional on
  runway ≥12 months, plus negotiating hybrid days
  or more salary to offset the commute.
WHY: 1) Growth and interesting work are worth
  more than stability at your stage.
  2) Worst case costs ~1.5 months of savings
  and doesn't touch your safety net.
  3) The raise pays for the commute and you get
  the work upgrade on top.
CONFIDENCE: 70%
BIGGEST RISK + HEDGE: the startup folds →
  check runway first, keep 6 months of savings
  untouched, refresh your CV every quarter.
TRIPWIRES:
  - Runway <12 months or they won't say → turn
    it down or ask for $95k+.
  - No hybrid days and still drained by
    2027-02-23 → plan a move closer or job-hunt.
  - Work not interesting by 2027-05-23 →
    re-decide; you'll have a stronger CV.
FIRST STEP (today): email the hiring manager
  the 4 questions above.
REVIEW ON: 2027-05-23 (judge the process, not
  the outcome).
```

This isn't professional financial advice. For option tax details (for example the 83(b) election or the 90-day window to buy your shares), check with a tax adviser before you sign. I can save this to a decision journal if you want.
